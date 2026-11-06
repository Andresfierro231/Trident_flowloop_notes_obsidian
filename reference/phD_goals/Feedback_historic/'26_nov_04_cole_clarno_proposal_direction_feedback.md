Show the NS relevant equations, show how they become how they become the 1d model (can have a brief derivation that points at literature sources) to show how they become the 1d model. 

- Main points of derivation in appendix  
  - Want to get what is new relatively quickly, show what parts you are changing.   
- Need to show in main document where you are going to enforce closures   
- Need to show : this is how this is normally done (perhaps in less exotic cases)   
  - Reference to typical 1d molten salt modeling (Nuclear systems 1? Ishii?)   
  - Even comparable to single-channel water flow  
  - Need to demonstrate how traditional ways may be insufficient.  
    - Do other people do digital twin, combination of high fidelity, experiments, and reduced model  
- How do people usually come up with the closure?   
  - What are you doing similar and what are you doing differently? Need something that is applicable to our use cases  
- For each of the closure terms, need to be explicit about how we are going to generate them  
  - Super specific about model form and how we are going to manipulate/tune  
  - What has been tried in literature? Can I use that? If not, how is my method different?   
    - Need to look principled, know the thing we don’t know, what you are trying to account for  
      - **why we are justified in making the tweaks that we did**   
      - Where models we used break down, what to do when it does  
      - What are other formulations  
    - History of what works and what does not work, reason for doing things well explained, principled backing of why doing what you are doing

Need to be explicit: here are the flaws; this is what I am trying to fill in, figure out what you can implement, and what you need to innovate. Here is what is normally done, is this sufficient? Here is how I am going to figure out if it is sufficient. If it doesn’t work, here is my solution, how I am going ot tests it, next steps. 

People want to be able to use this in SAM

- Need to be able to demonstrate the method beyond your 1d solver. Need to investigate how to do these flow profiles, friction factor forms, etc in SAM.   
- See if SAM can do what we want it to do. **This is a big deal**

Then, demonstration of if vcu models map onto acu loop, 

- how we plan to compare, next steps planned. 

Then, mapping 1d solution to detector responses

- What are typical ways it is done, what are potential solutions we are going to explore   
- Closure terms and mapping from 1d sol to detector response. 

### ***The committee wants to know if you know the theory well enough to explain it***

Practice writing a grant proposal 

→ Here is what I have so far, here is what I plan to do. If I do that, is that enough for phD

- Literature review should be done, roadmap needs to be highly detailed, there need to be promising results so far  
- 

—----------------------  
Show where in SAM numerically stable

- Sources of divergence (State matrix of divergence) \- state space where we can use SAM  
  - Sam invalid near freezing (thermophysical   properties)
  - Identifying and removing sources of instability
  - 
- Diagram of operating conditions/envelope sam is capable of modeling, overlain operating condition/envelope we expect for acu loop  
    - min mass flow rate, max mass flow rate (because velocity forces timestep unreasonably low to respect courant limit or similar)
- Need to have down to a science where and when SAM crashes. Need good analysis and understanding of that. 

Use the TAMU loop experiments, be able to do the friction factors and heat transfer paths in SAM

On the experimental side, proposal needs to show that I can use steady state data to get resistance terms, that I can take isothermal cooldown transiences to calculate cp, k, and effective time between transients. Need to show that using experimental data, I can suggest boundary conditions for the cfd. 

On the modeling side, need to be able to use model to get centerline temperatures, surface thermocouple temperatures first for assumed steady state. We need to be able to have this map from SAM and understand it super well. 

Then, assuming we have CFD, identifying state-dependent some steady state flow profiles. If we identify need of some cfd, make it known and we can evaluate whether we can create it. 

Need literature to show how much of this has been done and which parts have not been done
