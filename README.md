# Awesome-instruction-tuning
A curated list of open-source instruction tuning datasets, models, papers, repositories.

## Datasets and Models

### Modified from Traditional NLP 

Following [Longpre et al.](https://arxiv.org/pdf/2301.13688.pdf), we list all existing instruction tuning datasets modified from traditional NLP tasks.
|Release| Datasets|  Number of Tasks | Number of Instances | Model_name | Base | Model_Size| 
|  ----  | ----  | ----  | ----  | ----  | ----  | ----  | 
| 2020-05 | [UnifiedQA](https://github.com/allenai/unifiedqa) |46 | 750k | UnifiedQA | RoBerta | 110-340 M |
| 2021-04 | [CrossFit](https://github.com/INK-USC/CrossFit) |159 | 71.M | BART-CrossFit | BART | 140 M |
| 2021-04 | [Natural Inst v1.0](https://instructions.apps.allenai.org/) |61 | 620 k | Gen. BART | BART |140 M |
| 2021-09 | [Flan 2021](https://github.com/google-research/FLAN/tree/main#flan-2021) |62 | 4.4M | Flan-LaMDA | LaMDA | 137B |
| 2021-10 | [P3](https://github.com/bigscience-workshop/promptsource) | 62 | 12M |TO, TO+, TO++ | T5-LM| 3-11B | 
| 2021-10 | [MetalCL](https://github.com/facebookresearch/MetaICL) |142 | 3.5M |MetalCL | GPT-2 | 770 M |
| 2021-11 | [ExMix](https://github.com/google-research/text-to-text-transfer-transformer) | 107 | 500 k | ExT5 | T5 | 220M-11B |  
| 2022-04 | [Super-Natural Inst.](https://github.com/allenai/natural-instructions) |1613 | 5M | Tk-Instruct | T5-LM, mT5 | 17-13B |
| 2022-10 | [GLM](https://github.com/THUDM/GLM-130B) | 77 | 12M | GLM-130B | GLM | 130 B |
| 2022-10 | [Flan 2022](https://github.com/google-research/FLAN/tree/main/flan/v2) |1836 | 15M | Flan-T5, Flan-PaLM | T5-LM, PaLM | 10 M-540 B |
| 2022-11 | [xP3](https://huggingface.co/datasets/bigscience/xP3) | 71 | 81M | BLOOMz, mTO | BLOOM, mT5 | 13-176B |
| 2022-12 | [Unnatural Inst.](https://github.com/orhonovich/unnatural-instructions) | 117 | 64 k | T5-LM-Unnat. Inst. | T5-LM | 11B |




### Generated by LLMs
|Release|  Model_name | Base | Model_Size| Datasets | Number of Instances | Language|
|  ----  | ----  | ----  | ----  | ----  | ----  | ----  | 
| 2022-12 | GPT-3 Self Inst. | GPT-3 | 175B | Self-Instruct | 82 k |En | 
| 2023-03-03|[alpaca](https://github.com/tatsu-lab/stanford_alpaca)| LLaMA | 7B |[alpaca_data](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json)| 52 k | En | 
| 2023-03-19|[alpaca-lora](https://github.com/tloen/alpaca-lora/commits/main)  | LLaMA | 7B 13B 30B|[alpaca_data](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json)、[alpaca_data_cleaned](https://github.com/tloen/alpaca-lora/blob/main/alpaca_data_cleaned.json) |52 k | En|
| 2023-03-25|[dolly](https://github.com/databrickslabs/dolly)| dolly | 6B |[alpaca_data](https://github.com/tatsu-lab/stanford_alpaca/blob/main/alpaca_data.json)| 52 k|En |
| 2023-03-25|[guanaco](https://huggingface.co/KBlueLeaf/guanaco-7B-leh)| LLaMA | 7B |[GuanacoDataset](https://huggingface.co/datasets/JosephusCheung/GuanacoDataset)| 534 k | En Zh Ja De|
|2023-03-29|[ColossalChat](https://github.com/hpcaitech/ColossalAI)| LLaMA |7B 13B |[InstructionWild](https://github.com/XueFuzhao/InstructionWild) |104 k |En Zh  | 
| 2023-03-31| [Luotuo](https://github.com/LC1332/Luotuo-Chinese-LLM) | LLaMA ChatGLM  | 7B 6B  | [trans_chinese_alpaca_data](https://github.com/LC1332/Chinese-alpaca-lora/blob/main/data/trans_chinese_alpaca_data.json)  | 52k  | Zh  | 

### Multilingual tools
Most existing datasets are in English. However, most of the world’s population is under-served in terms of availability of data for their languages. How to ensure that everyone across the world is able to benefit from generative AI ? We have developed a straightforward and open-source translation tool based on Helsinki-NLP, capable of translating English datasets into 100+ languages at no cost. Although these translated datasets may contain some noise, they serve as a viable alternative to costly, high-quality data. See below.
#### Use of translator.py:
````
python  translator.py  model_name  source_data_path
````
#### Example:
````
python  translator.py  Helsinki-NLP/opus-mt-en-zh  alpaca_data.json
````
Our tool is designed to work with alpaca data and the Helsinki-NLP/opus-mt-en-zh model. Different datasets or Helsinki-NLP models yield varying results.  Due to the limitations of the model, Constrained by the model's capabilities, the translation quality may not always be optimal. For example，we observed instances of repeated words in the translations from English to Chinese，which lead us to develop "process.py" to eliminate translated prompts containing strings of any length that appear three consecutive times. We provide the final version in "translated_alpaca_data.json".

#### Use of process.py:
````
python  process.py  unprocessed_data_path
````
#### Example:
````
python  process.py  translated_data.json
````
\# the Helsinki-NLP model may have a maximum input sentence length limit. We have discarded the prompts which exceed the limit before translate them.

## Papers

We have extensively reviewed papers in this field and have listed the most valuable ones below:

[**Finetuned language models are zero-shot learners**](https://arxiv.org/abs/2109.01652) 2021.9

[**Multitask Prompted Training Enables Zero-Shot Task Generalization**](https://arxiv.org/abs/2110.08207) 2021.10

[**Training language models to follow instructions with human feedback**](https://arxiv.org/abs/2203.02155) 2022.3
     
[**Super-NaturalInstructions: Generalization via Declarative Instructions on 1600+ NLP Tasks**](https://arxiv.org/abs/2204.07705) 2022.4

[**Unsupervised Cross-Task Generalization via Retrieval Augmentation**](https://arxiv.org/abs/2204.07937) 2022.4
  
[**Instruction Induction: From Few Examples to Natural Language Task Descriptions**](https://arxiv.org/abs/2205.10782) 2022.5
    
[**Scaling Instruction-Finetuned Language Models**](https://arxiv.org/abs/2210.11416) 2022.10

[**Guess the Instruction! Flipped Learning Makes Language Models Stronger Zero-Shot Learners**](https://arxiv.org/abs/2210.02969) 2022.10
   
[**Unnatural Instructions: Tuning Language Models with (Almost) No Human Labor**](https://arxiv.org/abs/2212.09689)  2022.12

[**Improving Cross-task Generalization of Unified Table-to-text Models with Compositional Task Configurations**](https://arxiv.org/abs/2212.08780) 2022.12

[**Self-Instruct: Aligning Language Model with Self Generated Instructions**](https://arxiv.org/abs/2212.10560) 2022.12

[**MultiInstruct: Improving Multi-Modal Zero-Shot Learning via Instruction Tuning**](https://arxiv.org/abs/2212.10773) 2022.12

[**The Flan Collection: Designing Data and Methods for Effective Instruction Tuning**](https://arxiv.org/abs/2301.13688) 2023.1

[**In-Context Instruction Learning**](https://arxiv.org/abs/2302.14691) 2023.2


## Repositories
Additionally, we have provided a list of related repositories for further reference.

### Instruction
[awesome-instruction-learning](https://github.com/RenzeLou/awesome-instruction-learning)

[awesome-instruction-dataset](https://github.com/yaodongC/awesome-instruction-dataset)


### ICL
[ICL_PaperList](https://github.com/dqxiu/ICL_PaperList)

[prompt-in-context-learning](https://github.com/EgoAlpha/prompt-in-context-learning)

### Reason
[LM-reasoning](https://github.com/jeffhj/LM-reasoning)

[LLM-Reasoning-Papers](https://github.com/atfortes/LLM-Reasoning-Papers)

[Chain-of-ThoughtsPapers](https://github.com/Timothyxxx/Chain-of-ThoughtsPapers)


### Framework
[OpenICL](https://github.com/Shark-NLP/OpenICL)

