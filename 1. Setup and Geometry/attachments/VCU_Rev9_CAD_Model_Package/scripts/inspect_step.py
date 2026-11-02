#!/usr/bin/env python3
"""Inventory an AP242/STEP assembly with names, transforms, and bounding boxes."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import cadquery as cq
from OCP.BRepBuilderAPI import BRepBuilderAPI_Transform
from OCP.STEPCAFControl import STEPCAFControl_Reader
from OCP.TCollection import TCollection_ExtendedString
from OCP.TDataStd import TDataStd_Name
from OCP.TDF import TDF_Label, TDF_LabelSequence
from OCP.TDocStd import TDocStd_Document
from OCP.XCAFDoc import XCAFDoc_DocumentTool


def label_name(label: TDF_Label) -> str:
    attr = TDataStd_Name()
    if label.FindAttribute(TDataStd_Name.GetID_s(), attr):
        return attr.Get().ToExtString()
    return "<unnamed>"


def identity_transform():
    return cq.Matrix().wrapped.Trsf()


def transform_shape(shape, trsf):
    return BRepBuilderAPI_Transform(shape, trsf, True).Shape()


def shape_metrics(shape, trsf):
    moved = cq.Shape(transform_shape(shape, trsf))
    bb = moved.BoundingBox()
    center = moved.Center()
    try:
        volume = moved.Volume()
    except Exception:
        volume = 0.0
    try:
        solids = len(moved.Solids())
    except Exception:
        solids = 0
    return {
        "xmin": bb.xmin,
        "ymin": bb.ymin,
        "zmin": bb.zmin,
        "xmax": bb.xmax,
        "ymax": bb.ymax,
        "zmax": bb.zmax,
        "dx": bb.xlen,
        "dy": bb.ylen,
        "dz": bb.zlen,
        "cx": center.x,
        "cy": center.y,
        "cz": center.z,
        "volume": volume,
        "solids": solids,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("step", type=Path)
    parser.add_argument("--json", type=Path, required=True)
    parser.add_argument("--csv", type=Path, required=True)
    args = parser.parse_args()

    doc = TDocStd_Document(TCollection_ExtendedString("XmlXCAF"))
    reader = STEPCAFControl_Reader()
    reader.SetNameMode(True)
    reader.SetColorMode(True)
    status = reader.ReadFile(str(args.step))
    if "RetDone" not in str(status):
        raise RuntimeError(f"STEP read failed: {status}")
    if not reader.Transfer(doc):
        raise RuntimeError("STEP transfer to XCAF failed")

    tool = XCAFDoc_DocumentTool.ShapeTool_s(doc.Main())
    records: list[dict] = []

    def walk_definition(label: TDF_Label, parent_trsf, path: list[str], depth: int) -> None:
        name = label_name(label)
        current_path = path + [name]
        if tool.IsAssembly_s(label):
            components = TDF_LabelSequence()
            tool.GetComponents_s(label, components, False)
            for idx in range(1, components.Length() + 1):
                component = components.Value(idx)
                referred = TDF_Label()
                if not tool.GetReferredShape_s(component, referred):
                    continue
                local = tool.GetLocation_s(component).Transformation()
                world = parent_trsf.Multiplied(local)
                instance_name = label_name(component)
                def_name = label_name(referred)
                component_path = current_path + [instance_name]
                try:
                    metrics = shape_metrics(tool.GetShape_s(referred), world)
                except Exception as exc:
                    metrics = {"metric_error": str(exc)}
                records.append(
                    {
                        "depth": depth + 1,
                        "kind": "assembly" if tool.IsAssembly_s(referred) else "part",
                        "instance": instance_name,
                        "definition": def_name,
                        "path": "/".join(component_path),
                        **metrics,
                    }
                )
                if tool.IsAssembly_s(referred):
                    walk_definition(referred, world, component_path, depth + 1)
        elif tool.IsSimpleShape_s(label):
            metrics = shape_metrics(tool.GetShape_s(label), parent_trsf)
            records.append(
                {
                    "depth": depth,
                    "kind": "part",
                    "instance": name,
                    "definition": name,
                    "path": "/".join(current_path),
                    **metrics,
                }
            )

    free = TDF_LabelSequence()
    tool.GetFreeShapes(free)
    for idx in range(1, free.Length() + 1):
        label = free.Value(idx)
        if tool.IsAssembly_s(label):
            walk_definition(label, identity_transform(), [], 0)
        else:
            walk_definition(label, identity_transform(), [], 0)

    args.json.parent.mkdir(parents=True, exist_ok=True)
    args.json.write_text(json.dumps(records, indent=2), encoding="utf-8")
    fieldnames = sorted({key for record in records for key in record})
    with args.csv.open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(records)
    print(f"Wrote {len(records)} records")


if __name__ == "__main__":
    main()
