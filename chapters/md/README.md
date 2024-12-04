# Literature

## Of Human Criteria and Automatic Metrics: A Benchmark of Evaluation of Story Generation

**year, subject, code**
2022, Benchmark, https://github.com/dig-team/hanna-benchmark-asg

**background**
Automatic Story Generation (ASG) relies heavily on human and automatic evaluation.

**problem**
- there is no consensus on which human evaluation criteria to use,
- and no analysis of how well automatic criteria correlate with them.

**solution**
- they introduce a set of 6 orthogonal and comprehensive human criteria, carefully motivated by the social sciences literature.
  - Relevance (RE): how well the story matches its prompt
  - Coherence (CH): how much the story makes sense,
  - Empathy (EM): how well the reader understood the character’s emotions, derived from the importance of emotional commentary, passion , and empathy
  - Surprise (SU): how surprising the end of the story was, derived from the importance of schema violation, or unexpectedness, postdictability, and novelty
  - Engagement (EG): how much the reader engaged with the story; a more subjective criterion associated with projecting volitive modality (making the reader formulate a subjective judgment and express a desire to see something accomplished) and story outcome, which is an underlying cause of story liking
  - Complexity (CX): how elaborate the story is; derived from the importance of detailed descriptions and sophisticated problem-solving and good world-building
- they also present HANNA, an annotated dataset of 1,056 stories
  - produced by 10 different ASG systems
  - for ASG evaluation.
  - it has
    - story prompt
    - human story from the prompt
    - ai story from the prompt
    - ai model used
    - then human ratings on the 6 new criteria
- they evaluate the performance of 72 existing automatic metrics against their proposed human criteria.

**results**
- they demonstrate the limitations of current automatic evaluation methods.
- they make recommendations on which metrics to use for ASG evaluation.

**conclusion / future**
- Large pre-trained language models seem to produce the best results for ASG.
- we need automatic metrics that target each of their newly-proposed proposed human criteria.
- these newly-proposed proposed human criteria are overall weakly-correlated with one another, which shows they're non-redundant and produce coherent system rankings.
- all ASG metrics are very weak. BLEUΞ§ and ROUGEΞ§. chrFΞ§ and BARTScoreΞε are the best performers at the story- and system-level respectively.
  - The Ξ means they evaluate the candidate text by comparing it to a reference text (the human story).
  - The § means the evaluation is string-based and cannot handle synonyms, paraphrases.
  - The ε means the evaluation is embedding-based (using word2vec, BERT, etc) and can handle synonyms, paraphrases.

**summary**
- they created 6 human metrics to use for ASG. These are
- they created a dataset Human-ANnotated NArratives (HANNA),
- they tested LLMs against these metrics. How?
- they found that all LLMs tested performed poorly.

**thoughts**
- what are humans looking for when they evaluate AI stories, systems, results?
- all the tested models are OLD. Can we rerun this experiment with GPT and its friends?
- can we come up with a dataset that takes into account the 6 new criteria? or augment an existing one?

## InfoLM: A New Metric to Evaluate Summarization & Data2Text Generation
- proposes a way to fix the metrics (e.g., BLEU) that miss synonyms in evaluation. 
- they introduce InfoLM a family of untrained metrics that can be viewed as a string-based metric.
- they address the aforementioned flaws thanks to a pre-trained masked language model.
- DOI 10.1609/aaai.v36i10.21299

## Survey2Persona: Rendering Survey Responses as Personas

**year, subject, code**
2022, App/System, https://s2p.qcri.org/

**background**
personas useful for stakeholders in product and service creation.

**problem**
- creating personas is difficult

**solution**
- create them with AI
  - preserves privacy of individuals
  - allows the fine grain detail close to real people details
- use outlier detection in real-time. details unclear.
- tested with datasets:
  - “COVID-19 Beliefs, Behaviors & Norms Survey” published by MIT in collaboration with Facebook and the World Health Organization
  - “American Trends Panel Data” (AMTRENDS) from Pew Internet Research
  - an artificial dataset (ARTIFICIAL) that we created by randomly generating statements using a text generator and then randomly assigning values from the Likert range of 1-5 to 1708 unique demographic groups (i.e., each group was assigned a random value for each statement).

**results**
- Medium or high number of demographic groups = many personas are generated. Few demographics = few personas.
- The number of demographic groups is more important than the number of statements and responses.
- a decent sample size of 10,169 is not adequate to generate a high number of personas when there are only a few statements and demographic groups.
- Overall, S2P’s ability to generate personas does not appear great when there is a small number of statements or demographic groups.

**issues**
- surveys that are split by some answer choice,
- binary or other categorical answers not following the Likert scale,
- open-ended answers,
- items that do not include statements or are formulated as questions,
- latent constructs, i.e., multiple items belong to the same measure.

**conclusion / future**
- Future research is needed to define the lower boundary conditions for meaningful persona generation using S2P. currently, it only works well for large-scale survey datasets with a variety of statements (>10), demographic groups (>100)
- what should be the optimal range for information in persona profiles?
- there are issues with using mean-based SD for outlier detection, including poor performance with imbalanced (non-normal) data and small sample sizes. they're looking into MAD (mean absolute deviation)

**summary**
- generate personas from 
	- analytics data
	- survery responses themselves

**thoughts**
- can we do GroundTruthData2Personas? we get T2D healthcare data/stats and make personas from it?

## Towards Measuring and Modeling “Culture” in LLMs: A Survey
**year, subject, code**  
2024, Survey, https://github.com/faridlazuarda/cultural-llm-papers

**background**  
sample background

**problem**  
how is culture measured and modeled in LLMs?

**solution**  
survey of more than 90% of papers that aim to study culture in LLMs.

**results**
- none of the studies defines culture; attempted definitions are "broad-brush"
- others (un)knowingly define what (proxies of) culture is/are with the datasets they use.
- Culture in the Social Sciences
	- cultural heritage
	- interpersonal interactions
	- ways of life
	- in Anthropology
		- thin: as understood from outsiders perspective.
		- thick: as understood from outsiders perspective, but adds actors' own explanation of context and behaviour.
- Culture in NLP
	- Hershcovich et al. (2022)
		- common ground
		- aboutness
		- objectives and values
	- Liu et al., 2024a
		- within human
		- between humans
		- outside of human 
- studies use aspects of culture which they call proxies of culture.
	- demographic proxies: Culture is, almost always, described at the level of a community or group of people, who share certain common demographic attributes. These could be ethnicity (Masai culture), religion (Islamic culture), age (Gen Z culture), socio-economic class (middle class or urban), race, gender, language, region (Indonesian culture) and so on, and their intersections (e.g., Indian middle class).
	- semantic proxies: Often cultures are defined in terms of the emotions and values, food and drink, kinship terms, social etiquette, etc. prevalent within a group of people.
	- Note that the semantic and demographic proxies are orthogonal and simultaneously apply to any study. For instance one could choose to study the festivals (a semantic proxy) celebrated in a particular country (a demographic proxy).
- they also categorise the probing methods
	- black-box approach which only relies on the observed responses
	- white-box approach where the internal states of the models can be observed
	- Discriminative Probing, where the model chooses a specific answer from options
	- Generative Probing uses an open-ended fill-in-the-blank evaluation method. answers under different culture are compared.
- parts of culture that have been studied: objectives & values
- parts of culture that haven't been studied: multitude of semantic domains, aboutness
![alt text](image.png)
![alt text](image-1.png)
![alt text](image-2.png)

**conclusion / future**
- they point out a lack of robustness of probing techniques
- a lack of situated studies on the impact of cultural mis- and under-representation in LLM-based applications
- lack of studies that use white-box probing methods
- work on the robust and interpretable methods for culture
- need for culturally situated multilingual datasets from scratch
- consider anthropology and HCI 

**summary**  
- Overview of papers that cover culture.
- many ways of defining `culture`
- some ways of defining culture have been overly investigated, others haven't

**thoughts**
- can we explore an idea of cultural mosiac, where a person subscribes to one or more cultures at the same time, and applies one of them to specific parts of his life at specific times?

## CHAE: Fine-Grained Controllable Story Generation with Characters, Actions and Emotions
**year, subject, code**  
2022, App/System, https://github.com/victorup/CHAE

**background**  
- most work focusses on coherence based on keywords, outlines, commonsense knowledge
- other work generates stories based on emotion, style, topic

*previous story gen ideas:*
- using keywords
- using outlines
- incorporating external knowledge
- generating in specified styles suing leading context
- generating stories iwth desired titles and protagonists' emotional arcs
- generating stories considering the changes in the psychological state, while they just control the emotion lines instead of the detailed contents.

*previous **controllable** story gen ideas:*
- CTRL can control the overall attributes such as domain, style and topic of the generated text by adding control codes and prompts.
- PPLM can guide text generation without further training the language model, by plugging in a discriminator.
- CoCon ﬁnetunes an intermediate block with self-supervised learning to control high-level attributes i.e., sentiment and topic.

**problem**  
- no finegrained control guiding the story generation

**solution**  
- CHAE generates stories from CHaracters, their Actions, and Emotions.
- We ﬁrst take the characters with their actions and emotions of the story into account to conduct more ﬁne-grained controllable story generation.
- We propose a model CHAE with a novel input form that helps the model control the story in various aspects, and a character-wise emotion loss to relate the characters and the corresponding emotions.
- built on top of BART (bidirectional encoder) rather than GPT-2 (transformer, fully auto-regressive)
- they create a special token *Chae* inspired by the practice of leveraging special tokens for controllable generation.
- *Chae* the token is different from **CHAE** the model
![alt text](image-3.png)
  
**results**  
- The results of both automatic and human evaluation show that our model has strong controllability to generate customized stories.
- The traditional seq2seq model SoCP has worse performance.
- the CHAE model outperforms all others.

**conclusion / future**  
- The dataset contains only stories with 5 sentences, which is not enough for learning to generate longer stories. 
- The training of our model heavily relies on the annotations of characters, emotions, and actions in the dataset, while it
is very expensive to obtain the annotated data. 
- The Chae in the dataset actually has some noise, i.e., some descriptions in Chae are not reﬂected in the corresponding sente nces. 
- Our iterative generation method will result in a long time to train a story and may cause a cascade problem, which affects the overall quality of story generation.

future:
- we will adopt datasets with much more data and longer stories, such as Writing-Prompts and WikiPlots2. 
- In addition, we will consider using commonsense reasoning techniques to reason about the emotions and actions of the characters in the story before further generating the story. 
- Regarding the noise of Chae, we plan to conduct denoising in preprocessing to ﬁlter out the samples whose Chae are inconsistent with the corresponding sentence. The problem can also be alleviated by dynamically controlling the weight of the conditions. 
- We are also further exploring more convenient and effective training methods to generate controllable stories by inputting control conditions in one go, rather than iterative generation.

**summary**  
- CHAE introduces Chae, a way to embed more details into the story generation process using controllable generation tokens.
- They also finetune a BART model to make the CHAE model.

**thoughts**  
- what are n-grams?
- what are special tokens for controllable gen?
- what difference the underlying arch of the LLM makes in story gen 

**testing**
they tested for:
- Perplexity which represents the general quality of the generated stories
- BLEU to compare the coverage n-gram in the candidate stories and the reference stories because the words in Chae usually appear in the reference stories.
- Distinct is used to evaluate generation diversity by calculating the percentage of unique n-grams.
- Accuracy of emotions(ACC): We use emotion labels to calculate the accuracy of  the emotions of generated sentences toreﬂect the controllability of emotion.

**dataset**
- ROCStory with labeled characters’ emotions and actions
- The emotions come from Plutchik psychology theory

**models**
- CHAE they developed by finetuning BART [i think]

testing with:
- GPT-2
- BART
- SoCP
- Stylized-Story-Generation (SSG)

## What Makes a Good Story and How Can We Measure It? A Comprehensive Survey of Story Evaluation
**year, subject, code**
2024, Survey, 

**background** 
- BLEU  and ROUGE are widely used, but they often fail to assess semantic aspects and show a low correlation with human judgments. 
- More recent metrics that utilize neural embeddings or generation probabilities, such as BERTScore and BARTScore, perform better in terms of semantic comprehension, but they are still not particularly effective for evaluating stories.
- Some have proposed metrics trained on human evaluation benchmarks achieving better correlation with human criteria. However, these metrics are still limited by the benchmark itself and the size of the model.
- LLM-based metrics provide evaluations that are more consistent with human judgment. 
	- Additionally, they can provide the reasoning process for the generated score, greatly improving the reliability and interpretability of automatic evaluation scores. 
	- This progress also fosters collaborative evaluation, which can leverage both the strength of human and automatic evaluation.

**problem**  
under-explored areas:
- personalized evaluation (particularly in terms of subjective aspects like empathy and interestingness), 
- long story evaluation
- 

**solution**  
Our survey provides a comprehensive review of story evaluation. Outline:
- We first summarize the existing story generation tasks and datasets, including text-to-text, visual-to-text, and text-to-visual. 
	- also discuss evaluation considerations and challenges of various tasks.
- We outline detailed standards to evaluate stories. To address the issue of vague and inconsistent evaluation criteria, we analyze the commonly considered aspects and their definitions, which differ from general NLG tasks. 
	- We then present the existing story evaluation benchmarks and the aspects they cover.
- We describe existing metrics using the taxonomy we propose, 
	- and explore their correlation with human annotators for story evaluation. 
- We introduce a taxonomy to organize existing metrics that have been proposed or can be adopted for story evaluation. 
- We then provide detailed descriptions of traditional metrics and LLM-based metrics. 
	- we also specifically discuss the capabilities of different metrics in evaluating stories.

end of outline
- The development of automatic generation and evaluation also encourages human-AI collaborative writing and evaluation. we discuss the collaborative evaluation, and the methods for measuring collaborative writing systems.
- we recommend potential future research directions in story evaluation, which can also be extended to general domain.

**results**  
Story generation:
- stories generated with:
	- Title/Topic
	- Prompt/Premise
	- Outline/Plot/Storyline
	- Other Control Signals
- **problem** of plot repetition / incoherence **solved** with hierarchical generation process (user gives or app makes outline first, then generates based on that)

Common aspects used for evaluating story quality and their definitions:
- common ones are in the table below
- others that might be needed in specific situations are:
	- Style. can be simplified as a specific emotion or sentiment, and evaluated by style classification accuracy.
	- Controllable Accuracy. such as scene descriptions and character relationships
	- Toxicity. rude, unreasonable, or disrespectful components.
	- Naturalness/Human-like. is the story likely to be written by a human?
	- Non-Hallucination. does story contain unreasonable information that cannot be supported by the source input?
	- 
![Common aspects used for evaluating story quality and their definitions.](image-5.png)

Taxonomy of evalutation metrics:
![alt text](image-7.png)
![alt text](image-8.png)

Different types of neural models for automatic evaluation metrics:
![alt text](image-9.png)

Evaluation methods:
- Lexical-Based. Such methods process the story as bag-of tokens or n-grams (n continuous tokens). They are usually used to measure the similarity between two stories or to assess the diversity of stories generated by one model.
- Embedding-Based. some embedding-based approaches use pre-trained models to encode the source input, target story, and its reference as multiple embeddings, then perform further processing.
- Probability-Based. These types of methods calculate the evaluation score based on the generation probability of the target text through generative models.
- Generative-Based. aka prompt-based methods. They provide humans or generative models with an evaluation prompt and collect the generated results.
- Trained. These methods might employ any of the three model types from the table above, with further training on evaluation benchmark datasets to improve the evaluating abilities.

Evaluation metrics, tested story aspects, working methods, and output formats:
![alt text](image-10.png)
![alt text](image-11.png)


**conclusion / future** 
- Note that most story-related generation tasks do not have a standard result.
Therefore, while **reference-based** metrics (comparing target text to reference text) can be useful, **reference-free** metrics (evaluating target text based on its overall or multi-aspect quality) may be more appropriate. There are also some **hybrid** metrics that combine reference-free and reference-based results.

helpful strategies:
- In the evaluation prompt, clear and concise instructions are better than complex ones 
- Generating the reasoning process or detailed error analysis can aid the final evaluation.
- Decomposing a complicated task into simpler, clearer sub-tasks is helpful. 
- Aggregating multiple evaluations incorporating a debating process, and using multi-agent assessment can all improve the performance and robustness of the results. 
- In-context learning could be helpful especially for personalized evaluation.

There are four types of discovered biases: 
- Format Bias, which means the optimal performance is only achieved under specific prompt formats. 
	- Designing more professional prompts or fine-tuning the model with more diverse instructions can mitigate this problem. 
- Position bias, a common problem in LLM-based evaluations, which means that LLM exhibits a preference for the first displayed candidate 
	- To address this problem, a simple solution is to combine evaluations using different sample orderings. Specifically for generative-based methods, Wang et al. aggregates results across various orders to determine the final score; for trained methods, Li et al. change the order of the candidates within each training sample to double the training data. 
- Knowledge bias, which means LLM-based evaluators tend to favor the results they have seen or results that are generated by themselves. This can be partially mitigated by replacing proper nouns, but it remains a very challenging issue. 
- Likelihood Bias, which is showcased in probability-based methods, because the probability of a sentence can vary due to superficial differences, especially in aspects like relevance.

end of discovered biases.

- Open-source metrics that show comparable results to ChatGPT are preferable alternatives. Specifically, metrics trained for story evaluation such as Union, or evaluation expertise LLMs like TigerScore and AUTO-J are worth considering.
- Evaluating collaborative writing requires consideration of both story *quality* and *user experience*. 
	- Quantitative evaluations of human experience include edit distance, percentage of accepted suggestions or applied model-generated stories, generation productivity (words written per unit time), and story completion time. 
	- Lee et al. apply the concepts from Storch, redefining equality as the even distribution of writing events between humans and AI, and mutuality as the proportion of user-system interactions among all operations.
	- User feedback might be more important for evaluating collaborative writing systems. Several studies have developed questionnaires to gather this feedback. These questions either assess the overall performance (whether the framework is a good platform and if they would use it again); or assess multiple aspects, focusing on the helpfulness, user-friendliness, user experience, and effectiveness of the collaborative writing framework.
- exploring methods for effective subset sampling so humans can evaluate few useful stories from large datasets in a way that we can use to train / automate their preferences.
- look into personalised evaluation which solves the inter-annotator agreement problem. the evaluation will match the user giving initial preferences.
- Explore the Difference between Human-written and AI-generated Stories.
	- to explore the gap between AI-generated and human-written stories in order to enhance the quality of generated content. 
	- to develop methods for distinguishing between AI-generated and human-written stories, with the aim of preventing potential harm, such as the spread of fake news stories.

**summary** 
- Although LLM-based evaluations achieve much better results than traditional methods, there is still a long way to go in realizing reliable and robust evaluation.
- UniEval and COMET22 trained on human eval, show even stronger results than some reference-based LLM metrics.

**thoughts** 
- look into metrics trained on human evaluation benchmarks. is it true that basing them on human evaluation gives better correlation?
- what if we have a culture vector insitantialised by the person? Imagine the vector as a multi-segment line, with each point on the line being a cultural proxy. Can we use that vector as the ground truth, and the closer a generated story's vector points are to it, the more culturally good the story is.
- how can we structure story gen around character development, and use that as evaluation too? since it's what drives the story progression and is what's important at the end of the story.
- look into the helpful strategies of LLM evaluation from the **future** section.
- maybe reference-based metrics for details and reference-free for bigger picture/creativity.
- look into collaborative evalutation COEVAL and EvalLM
	- one of those metrics for evalutating the story *quality*
	- and questionares for evalutating the *user experience* (see **future** section)
- on personalised evaluation, would we take the preferences of the patient, HP, caretaker, or other? to determine whether the story is good.

**dataset**

Detailed statistics of existing story generation datasets:
![alt text](image-4.png)

Story evaluation benchmark datasets:
- OpenMEVA propose evaluation on overall quality,
- HANNA annotates evaluation scores on multiple aspects of a story. 
- COHESENTIA firstly introduces a benchmark for the vague aspect of coherence, 
	- evaluating both global and local coherence (scoring sentence by sentence). 
- PERSE firstly focuses on personalized story evaluation, considering the readers’ personal preferences.
- see table below:

![alt text](image-6.png)

**models**


## 
**year, subject, code**  
**background**  
**problem**  
**solution**  
**results**  
**conclusion / future**  
**summary**  
**thoughts**  
**dataset**
**models**

