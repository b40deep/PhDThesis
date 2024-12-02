# Literature

## Of Human Criteria and Automatic Metrics: A Benchmark of **Evaluation of Story Generation

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

**conclusion / future**
- they point out a lack of robustness of probing techniques
- a lack of situated studies on the impact of cultural mis- and under-representation in LLM-based applications
- lack of studies that use white-box probing methods

**summary**
**thoughts**
- can we explore an idea of cultural mosiac, where a person subscribes to one or more cultures at the same time, and applies one of them to specific parts of his life at specific times?

##
**year, subject, code**
**background**
**problem**
**solution**
**results**
**conclusion / future**
**summary**
**thoughts**
