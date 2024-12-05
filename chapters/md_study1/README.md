# Study 1: What is the difference between the AI story and what the user accepts? Can it be measured?

## Introduction
Artificial Intelligence (AI) models such as Large Language Models (LLMs) have proven useful in text generation. Because of this, we explore their use in story generation. We aim to generate fictional stories based on Type 2 Diabetes (T2D) patients. These stories are intended to be an addition to their existing T2D management strategies.

## Currently
In the current implementation, the user prompts the system and it generates a story based on the prompt. From there, the user gives feedback on the story and it is regenerated accordingly. This happens until either the user is satisfied with the result, or settles for the result due to constraints in time, interest, benefit of doubt, etc.

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

### Experiment details
#### patient
#### prompt
#### output
#### evaluation criteria - story
#### evaluation criteria - user experience
#### evaluation methods 
#### automation ideas

## The benefits
