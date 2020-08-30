# M1-Internship-Dynamic
## Verification of ever-changing reconfigurable industrial systems

### Ulysse Remond’s Internship at LTU AIC3lab

## Background
  Industrial automation is facing challenges related to a manufacturing change from mass production to mass customization. As a result, the focus of automation has been shifting to flexibility, reconfigurability, and safety assurance. With this shift, the existing software verification and validation (V&V) techniques, such as testing and simulation, become inadequate. Formal verification promises much more comprehensive discovery of possible errors in software but has problems with applicability and complexity.
  
  
  Despite the initial R&D successes and promises of these techniques, the reality is that formal verification techniques are rarely used in the development practice by industrial automation engineers. Indeed, it seems that the existing tools and methods do not fit to the processes of automation system engineering.
  
  
  To go beyond these limits, we propose a closed-loop verification framework which we believe will be more efficient and feasible in model checking of control systems in the industrial automation domain. The framework consists of 4 main steps: 
  
  
1) Developing a closed-loop function block application of the control system and a simulation model with initial testing of the control logic by simulation;


2) Automatic generation (and composition) of formal models as a closed-loop model; 


3) Model checking the resulting formal model and verifying for a comprehensive set of requirements, which generates counterexamples for any failed properties;


4) Playback of the counterexample from Step 3 in the same simulation model generated in Step 1. 


Factory floors with the on the fly changeable machines layout was demonstrated recently in our research and reported in [1]. Such systems make a representative case of Cyber-Physical System (CPS) with collaborating autonomous mobile units that need to operate in the environment also accessed by people. The proposed framework, as depicted in Fig. 1, will comprehensively support verification of the system’s behaviour in the loop with the model in two ways: 1) before deployment, and 2) online verification during the operation by means of 2.1) using the automatically generated safety supervisors which would protect CPS from entering dangerous states, and 2.2) using the bounded model-checking methods conducted in the Fog which enable exploration of the system’s state space to a certain depth as the real-time requirements permit. It will be performed at every essential system configuration change which may impact on the overall safety properties of the entire CPS.


  Adaptive cognitive computations will enable adaptive corrections of the swarm participants behaviour for errors originating in the unpredictable nature of wireless communications and complex dynamics of the system.
  
  
    Implementation of this framework is based on the recent progress achieved both at the research group at LTU and globally, in particular on the methods for plant model learning [2],  tool-chains for the automatic formal model generation [3] and combined use of explicit state and symbolic model-checkers for extending the range of verifiable systems [4]. For the latter, the Verification Director will generate models in the input format of a particular discrete-state and hybrid model-checkers and will invoke them dependent on properties of a particular model and expectations of model-checking complexity of a particular method, leveraging the fact that these methods may have substantially different complexities.
For the online verification, safety supervisors will be generated and automatically added to the executable specification of CPS in form of IEC 61499 function blocks. The synthesis will be done based on the set of safety requirements and constraints, and the multi-closed loop model of the CPS, provided by the Verification Director. 

## Task for the student
The work in this task will include the integration of software tools for requirements management, formal modeling and verification into a targeted tool-chain, capable of extending the standard testing methods with capabilities of checking and proving correct behavior of Cyber-Physical Systems (CPS), that will typically be encoded into IEC 61499 function blocks (FB).


The task will include some of the following development subtasks (and learning tools supporting the other steps): 


-Develop a generator of formal models from the system-level descriptions of CPS; 


-Develop a framework for the synthesis of safety supervisors; 

The toolchain will include at least two model-checkers, one supporting symbolic, and the other explicit state model-checking, to achieve maximum efficiency for a given verification task. 


The verification tool will be integrated into the development environments 4DIAC and/or nxtStudio, aiming at the routine use of formal verification by CPS control engineers through the life cycle of the systems. The intention is to hide the complicated technicalities from the control engineer, letting her/him operate at the level of the modelling language, user-friendly format of specifications and interpretation of counter-examples. 

## References

[1]D. Drozdov, U. Atmojo, S. Patil, et al. A Product-Driven software design pattern for distributed industrial automation system, 17th IEEE conference on industrial informatics (INDIN 2019), 2019, Helsinki-Espoo


[2]Buzhinsky, I. and Vyatkin, V., 2017. Automatic inference of finite-state plant models from traces and temporal properties. IEEE Transactions on Industrial Informatics, 13(4), pp.1521-1530


[3]D. Drozdov, S. Patil, V. Vyatkin, “Towards Formal Verification for Cyber-physically Agnostic Software: a Case Study”, International Annual Conference of IEEE Industrial Electronics Society IECON’17, Beijing, 2017


[4]I. Buzhinsky, V. Vyatkin, “Explicit-State and Symbolic Model Checking of Nuclear I&C Systems: A Comparison”, 43rd International Annual Conference of IEEE Industrial Electronics Society IECON’17, Beijing, 2017
