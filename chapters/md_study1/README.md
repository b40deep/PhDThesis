# Study 1: What is the difference between the AI story and what the user accepts? Can it be measured?

## Introduction
Artificial Intelligence (AI) models such as Large Language Models (LLMs) have proven useful in text generation. Because of this, we explore their use in story generation. We aim to generate fictional stories based on Type 2 Diabetes (T2D) patients. These stories are intended to be an addition to their existing T2D management strategies.

## Currently
In the current implementation of the system, the user prompts the it and it generates a story based on the prompt. From there, the user gives feedback on the story and it is regenerated accordingly. This happens until either the user is satisfied with the result, or settles for the result due to constraints in time, interest, benefit of doubt, etc.

## The gap
- There is no way for the system to *learn* the preferences of the user.
- Each generated story must undergo edits from the user to make it acceptable to them.

## The experiment
This study proposes an iteration of the system that:
- generates a story outline first.
- the outline can then be edited and/or approved by the user
- the system collects feedback from the user on the changes made
- the actual story is then generated.
- the story can also be edited by the user until it is acceptable to them.
- the system collects feedback from the user on the changes made
- after the workflow, the changes and feedback from the user are analysed.

Experiment details
### patient
Patient attributes are required to generate relevant stories for them. The goal is to find a balance between patient confidentiality and useful detail. Searching for that balance could be a separate study. This study takes collects the following information from the patient:
- Physical attributes: needed for story and image generation
    - age range
    - gender
    - ethnicity
    - body shape/size
    - disability & mobility accessories
    - (optional) bonus details: hair, dress style, accessories, etc
- Health attributes: to ground the story generation in patient's current health situation
    - health status
    - previous health recommendation(s)
    - current health recommendation(s)
- Location attributes: to place the story generated in patient's locations
    - common locations: home, school/work
    - important locations: religious, social, commercial, cultural, lifestyle

*In the future:* We could also consider generating patient personas from the Official SouthAfrican national T2D data.

### prompt
The prompt portion covers both the outline and story generation and refining. The outline is a nested list of story parts. Each part is a summary that is used to generate the full story portion. We can modify the CHAE (CHaracter, Action, Emotion) idea to include the Setting. CHASE is:
- CHaracter: the patient
- Action: the suggested action for that part of the story
- Setting: the location of the event
- Emotion: the patient's emotion during the event

*In the future:* We could consider commonsense reasoning techniques / agents to generate and verify the outline before presenting it to the user.

### output
The primary output is the story the user requested.

Other outputs that are useful are:
- the story outline useful for getting the facts right before generating the full story
- the user feedback from the generated outline
- the user feedback from the generated story

### evaluation
The evaluation of the system will hopefully shed some light on how we can close the gaps mentioned above. An evaluation approach from literature is to evaluate both the story and user's experience. 
#### story evaluation
We can evaluate the story based on 6 criteria that cover the different ways to present culture in stories. These are:
- Relevance (RE): how well the story matches its prompt. RB
- Coherence (CH): how much the story makes sense,. RF
- Empathy (EM): how well the reader understood the character’s emotions, derived from the importance of emotional commentary, passion , and empathy. RF
- Surprise (SU): how surprising the end of the story was, derived from the importance of schema violation, or unexpectedness, postdictability, and novelty. RB
- Engagement (EG): how much the reader engaged with the story; a more subjective criterion associated with projecting volitive modality (making the reader formulate a subjective judgment and express a desire to see something accomplished) and story outcome, which is an underlying cause of story liking. RB
- Complexity (CX): how elaborate the story is; derived from the importance of detailed descriptions and sophisticated problem-solving and good world-building. RB

RB are reference-based metrics so we'll compare their output to a ground truth. RF are reference-free and we'll measure those without ground truth. 
#### user experience evaluation
The most important benefit of the user experience feedback is the reasoning process behind the decisions/changes they make to the outlines and stories. There are a number of questionnaires we can adapt to collect this information from them. It will contain feedback on both the generated content and the experience of using the system. 
#### evaluation methods 
- The literature shows that LLMs are already used for evaluating stories. They are good because they can provide some 'reasoning' in many cases. They do require concise instructions to get useful results from them. The common bias problem can be addressed by giving them ground truths to use for evaluations, rather than have them rely on their training data.
- Another option that's available are pre-trained evaluation LLMs that are built specifically for such tasks. Some examples are AUTO-J and TigerScore. UniEval and COMET22 seem to perform well, and in some cases, better than off-the-shelf LLMs.

### automation ideas
#### the 6 criteria:
Consider the output to be the outline and the story. Some evaluation result examples are:
- Relevance (RE): how closely-matched is output to prompt?
- Coherence (CH): does the output make sense? (sense == output flow)
- Empathy (EM): does (health+context) ground truth influence output emotions? does reader understand that?
- Surprise (SU): does output have novelty in finding a solution/resolution? (should be based on health+context ground truth)
- Engagement (EG): did reader form their own opinion agreeing/disagreeing, based on the output?
- Complexity (CX): how much detail, problem-solving, world-building is in the output?

From the above, we can get:
- which criteria of the output are lagging behind (and gather more from the user/domain on those)
- how those criteria are lagging behind (lack of info/detail, or irrelevant info/detail?)
- which criteria are more useful to the user (🤔how can we have the user rank them?)
- the difference between the LLMs' output and the user's accepted output. (correlation?)
- the difference between the LLMs' and the user's evaluations. (correlation?)
- the difference between the user feedback and the user's typed edits. (correlation?)

#### personas
Can we then automate persona generation (like S2P paper). These patient personas would be a starting point for app users to select as an avatar, and customise later. They help with data privacy and yet enable the system get the information it needs to generate useful stories over time. These can be generated from:
- the official SouthAfrican national T2D data.
- user feedback that is collected over time.

#### outline and story generation
This process can later be improved by using multi-agent working. Here, each agent can be responsible for a particular part of the output or metric, and communication between them ensures final outputs are compliant with the many demanding requirements. These would also be useful for evaluation. Specific user feedback can also go directly to the relevant agent.  

## The benefits
- Understanding the difference between the AI output and what the user accepts can help us augment the system so that future outputs are closer to what the user wants. 
- Trying to measure these differences can help us make structures useful for filling in the gaps that AI has when making context-relevant output.

## The design
The diagram shows the system 
![alt text](image-1.png)