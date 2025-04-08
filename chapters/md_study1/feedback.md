# current questions
- where am I going to run my studies from? Kenya? UK? UG?
- what other experiments can I do that don't need physical users present?



# study 1 details:
- how many testers? how to get that number aside from guessing.
- after gathering user and LLM 6C feedback, how do I do the comparison?
    - LLMs can give us ratings on which is better: we can run this through the LLM generating the story and other StoryEval LLMs. Add DeltaScore for fine-grained evaluations.
    - Then we show these results to the user and the accompanying explanations, and they agree/disagree with reasons. similar to COEVAL but better.
- how do I do the user experience testing? find some questionnaires.
    - they are mannyyyyy!
    - for now, we'll use these from Mirowski et al.:
        - Helpfulness: I found the AI system helpful.
        - Collaboration: I felt like I was collaborating with the AI system.
        - Ease: I found it easy to write with the AI system.
        - Enjoyment: I enjoyed writing with the AI system.
        - Expression: I was able to express my creative goals while writing with the AI system.
        - Unique: The script(s) written with the AI system feel unique.
        - Ownership: I feel I have ownership over the created script(s).
        - Surprise: I was surprised by the responses from the AI system.
        - Proud: I’m proud of the final outputs.



# dec 5 2024
Feedback:
- add more context things. Clarify that the wider context is world but currently testing with Africa. 
- add questions to 6 criteria. What will you ask and what will you be looking for? 
- automation is part 2. Focus on part 1 for now. Add detail to part 1. How many people, what tasks, how many times you'll ask? What scores? What qualitative? Why they've made the change? 
- what's been changed. What they changed to. Why they changed it. Trying to find patterns. 
- title is trying to find patterns 
- study specifically looking at doctor's changes to stories. 
- could quantify based on the 6 criteria
- updated plan on Tuesday. 
Add a clarification that we're doing the analysis to get changes and feedback the system to make it better. 

Questions:
- Two separate versions of the app?
- Share my ideas with them or keep separate?
Ask what the pipeline is. I give them and they give me. Try and get an agreement and see if you get something back. Could it be a chapter? Is there a way to incorporate it into the PhD? Or get your name on a paper? 

I should be on the Sept paper. 


## rough thesis project summary
Imagine Travis, a 19-year-old University student, meets with Nurse Lee to discuss lifestyle changes to manage Type 2 Diabetes (T2D), particularly smoking cessation. They develop strategies for each that Lee uses to seed a story that helps Travis remember his cognitive prompts when he needs to turn away from smoking. Travis keeps the story on his phone and watches it before he goes out to keep his motivation high. At a follow-up appointment, Travis says he is using the story as an aid, but he doesn’t relate to the character. He wants a character that looks like the future version of himself once he is in control of his diabetes. They work to imagine his appearance and generate that character together. The story is then remade. Stories like Travis’ can become a reality, with huge potential to improve lives of T2D patients worldwide. This thesis seeks to develop and test methods and systems that would assist Healthcare providers (HPs) like doctors, nurses, and patient carers to generate stories and accompanying images that help the patient. Participants interact with these interventions and provide feedback. Previous work has highlighted the benefits of technologies like Artificial Intelligence (AI) in Healthcare using text (Chatbots). This has the potential to improve both the quality and accessibility of such healthcare interventions. We attempt to find out if GenAI can be used to create culturally appropriate material, particularly for patients in the Global South.


Could you please explain to me, in layman's terms, 
- the generative AI tools you employed, 
- how you used them, 
- why you chose them, 
- and their application? 

I am planning to include this information in our methods section to provide context.

The software system is split into two parts, story generation and image generation. We used a Large Lanugage Model (LLM) and a Text To Image (T2I) model. The LLM is the current state-of-the-art technologies for generating stories in natural language. The T2I used is a diffusion model since these are also state-of-the-art in image generation. A user inputs a story prompt to the LLM and it generates a full story with accompanying image prompts. The user can then edit and regenerate both to their satisfaction. Once the user approves, the image prompts are sent to the T2I model which generates images accompanying the story. The user can also edit the image prompts and regenerate the images to their satisfaction. Altogether, a user is able to input a lifestyle need and outcome, and have a story and accompanying images generated for them in response.