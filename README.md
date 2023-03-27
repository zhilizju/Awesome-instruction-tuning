# Awesome-instruction-tuning
A curated list of open-source instruction tuning datasets, models and papers.
## Datasets and Models

|Release| Datasets|  Number of Tasks | Number of Instances | Model_name | Base | Model_Size| 
|  ----  | ----  | ----  | ----  | ----  | ----  | ----  | 
| 2020-05 | UnifiedQA |46 | 750k | UnifiedQA | RoBerta | 110-340 M |
| 2021-04 | CrossFit |159 | 71.M | BART-CrossFit | BART | 140 M |
| 2021-04 | Natural Inst v1.0 |61 | 620 k | Gen. BART | BART |140 M |
| 2021-09 | Flan 2021 |62 | 4.4M | Flan-LaMDA | LaMDA | 137B |
| 2021-10 | P3 | 62 | 12M |TO, TO+, TO++ | T5-LM| 3-11B | 
| 2021-10 | MetalCL |142 | 3.5M |MetalCL | GPT-2 | 770 M |
| 2021-11 | ExMix | 107 | 500 k | ExT5 | T5 | 220M-11B |  
| 2022-04 | [Super-Natural Inst.](https://github.com/allenai/natural-instructions) |1613 | 5M | Tk-Instruct | T5-LM, mT5 | 17-13B |
| 2022-10 | GLM | 77 | 12M | GLM-130B | GLM | 130 B |
| 2022-10 | Flan 2022 |1836 | 15M | Flan-T5, Flan-PaLM | T5-LM, PaLM | 10 M-540 B |
| 2022-11 | xP3 | 71 | 81M | BLOOMz, mTO | BLOOM, mT5 | 13-176B |
| 2022-12 | Unnatural Inst. | 117 | 64 k | T5-LM-Unnat. Inst. | T5-LM | 11B |
| 2022-12 | OPT-IML Bench|2207 | 18M | OPT-IML | OPT | 30-175B |




|Release|  Model_name | Base | Model_Size| Datasets | Number of Instances | Language|
|  ----  | ----  | ----  | ----  | ----  | ----  | ----  | 
| 2022-12 | GPT-3 Self Inst. | GPT-3 | 175B | Self-Instruct | 82 k |En | 
| 2022-03-03| [alpaca](https://github.com/tatsu-lab/stanford_alpaca)| | | | |  | 
| 2022-03-19| [alpaca-lora](https://github.com/tloen/alpaca-lora/commits/main)  | | | | | |
| 2022-03-25|[dolly](https://github.com/databrickslabs/dolly)|  | | | | | |
| 2022-03-25|[guanaco](https://huggingface.co/KBlueLeaf/guanaco-7B-leh)| | |[GuanacoDataset](https://huggingface.co/datasets/JosephusCheung/GuanacoDataset)| | |


## Papers

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
