<p align="center" width="100%">
<img src="assets/cabra.png" alt="Cabra" style="width: 20%; min-width: 300px; display: block; margin: auto;">
</p>

# Cabra: A portuguese finetuned instruction Open-LLaMA

This repository is intended to share all the steps and resources that we used to finetune our version of Open-LLaMA.

This model is allowed for commercial purposes, by having the license cc-by-sa-3.0. It only used commercially licensed sources.

The project was strongly inspired by [Cabrita](https://github.com/22-hours/cabrita), which had a similar solution but without using commercially licensed sources, and used a smaller 7B model instead of a 13B.

The resulting models can be downloaded at Hugging Face:

- [Cabra-13B-LoRA](https://huggingface.co/Gustrd/open-llama-13b-lora-cabra-adapter) - To use with the [original model](https://huggingface.co/VMware/open-llama-13b-open-instruct);

- [Cabra-13B-Merged](TODO) - To standalone use - TODO;

- [Cabra-13B-GGML](https://huggingface.co/Gustrd/open-llama-13b-lora-cabra-adapter) - For CPU inference, using [llama.cpp](https://github.com/ggerganov/llama.cpp) or [koboldcpp](https://github.com/LostRuins/koboldcpp). Only with the adapter for now;

You can test the inference online at Kaggle [here](https://www.kaggle.com/gustavorochadias/inference-cabra-kaggle-v1-0).

## Benchmarks

We have introduced a novel benchmark to assess the performance of models in English-to-Portuguese translation tasks. Named HIPPO (High-level Interlingual Performance Proximity Optimized), this automated benchmark evaluates not only the absence of grammatical errors but also the semantic closeness of the translation to a reference, using embeddings. You can access the documentation for the HIPPO Benchmark [here](TODO).

For these models, we utilized the parameters listed below, which we believe can still be optimized:

- Dataset: 2k rows - [opus-100 en-pt validation subset](https://huggingface.co/datasets/opus100/viewer/en-pt/validation);
- Temperature: 0.3;
- Top-P value: 0.9;

Results Overview:

| Model | Fine-tuned? | Original Model | Allows Commercial Use? |HIPPO-Opus100-Grammar | HIPPO-Opus100-Paraphrase | HIPPO-Opus100-Combined |
|-------|-------------|----------------|------------------------|----------------------|--------------------------|------------------------|
| Llama-7B | No | N/A | No | 6.11% | 8.91% | 2.10% |
| Alpaca-7B | Yes | Llama-7B | No | 32.60% | 46.30% | 15.25% |
| Cabrita-7B | Yes | Llama-7B | No | 34.00% | 33.85% | 10.60% |
| OpenLlama-Instruct-13B | Yes | OpenLlama-13B | Yes | 26.35% | 32.50% | 8.75% |
| Cabra-13B (ours) | Yes | OpenLlama-Instruct-13B | Yes | 35.75% | 37.75% | 12.40% |
| LibreTranslate (reference) | Not-LLM | Not-LLM | Yes | 44.55% | 66.40% | 27.90% |

- Fine-tuning models specifically for the target language significantly improves their capability.
- Alpaca-7B showcases remarkable efficiency even without Portuguese-specific fine-tuning. This could be attributed to the superiority of the Alpaca Dataset compared to Dolly or possibly because Llama's foundational training surpasses that of OpenLlama.
- Cabrita made improvements but lags behind Alpaca-7B. This might be due to the quick implementation of LoRA fine-tuning.
- Cabra, despite its gains, still offers considerable room for enhancement, especially given its higher parameter count.
- LibreTranslate, taken as a reference, faces challenges with this benchmark as well, indicating the complexities and nuances of certain translation tasks.

## References

> If I have seen further it is by standing on the sholders [sic] of Giants.
> -- <cite>Isaac Newton</cite>

We started this section with this citation because everything we accomplished was only possible due to the strong community and the work that other people and groups have done. For our work, we mainly rely on the works developed by: [Cabrita](https://github.com/22-hours/cabrita), [OpenLlama](https://github.com/openlm-research/open_llama), [Hugging Face](https://huggingface.co/), [Open-Instruct](https://github.com/allenai/open-instruct), [VMware](https://huggingface.co/VMware/open-llama-13b-open-instruct), [Dolly](https://github.com/databrickslabs/dolly) and [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) .So, thank you all for the great work and contribution to the open-source community!


## Data

We translated the [databricks-dolly-15k.jsonl](https://huggingface.co/datasets/databricks/databricks-dolly-15k/resolve/main/databricks-dolly-15k.jsonl) into Portuguese using LibreTranslate. Even if this translation is flawed, the tradeoff between speed, cost and results is good. We were able to do it in a few hours on a consumer-grade laptop. The translation script is at this repository.

If you want to know more about how the dataset was built go to: [Dolly](https://github.com/databrickslabs/dolly).

We refrained from using GPT for translation, as the original Cabrita project did, due to licensing issues. Also, the recently released Llama 2 model is currently not licensed for use in Portuguese.

## Finetuning

To fine-tune the OpenLLaMA model, we used as base the code available on [Cabrita](https://github.com/22-hours/cabrita), which provides code to finetune the LLaMA model using PEFT from Hugging Face, we just adapted it to OpenLlama-Instruct. With this, we could run our finetuning step using 1 A4000 at Paperspace on top of OpenLLaMA-OpenInstruct-13B. We trained for about 7 hours and we found the results to be pretty incredible in just that amount of time. The notebook we used is avaible [here](https://github.com/gustrd/cabra/blob/dev/notebooks/qLora-Training-Cabra%20-%20Paperspace.ipynb).

## Example outputs

open-llama-13b-open-instruct:
```
Instruction: Invente uma desculpa criativa pra dizer que não preciso ir à festa.
Response: Sentimento de culpa. Eu não quero ir à festa, pois esse tipo de evento é um local em que as pessoas se reúnem para ter aulas de dança e canto, e também para se divertir e socializar. Mas eu não quero ir, pois estou comum ao público e não quero expor a minha alma ao risco de ser criticada ou ridicularizada.
```

Cabra:
```
Instrução: 
Invente uma desculpa criativa pra dizer que não preciso ir à festa.

Resposta: 
Tenho problemas financeiros.
```

open-llama-13b-open-instruct:
```
Instruction: Como posso começar a carreira como cientista de dados? Escreva na forma de lista.
Response:
1. Obtenha um bacharelado em ciência da computação ou em engenharia da computação.
2. Obtenha um mestrado em ciência da computação ou em engenharia da computação com ênfase em inteligência artificial.
3. Comece a trabalhar em um campo de interesse, como a mensagem, o negócio ou a ciência.
4. Participação em eventos de ciência da computação, como conferências, workshops e congressos.
5. Aplique para bolsas de pesquisa e desenvolvimento.
6. Aplique para o Programa de Pós-Doutoramento em Ciência da Computação da Microsoft.
7. Aplique para o Programa de Pós-Doutoramento em Ciência da Computação da Facebook.
8. Aplique para o Programa de Pós-Doutoramento em Ciência da Computação da Google.
9. Aplique para o Programa de Pós-Doutoramento em Ciência da Computação da Amazon.
```

Cabra:
```
Instrução: 
Como posso começar a carreira como cientista de dados? Escreva na forma de lista.

Resposta: 
- Estudar matemática, ciência da computação e engenharia. 
- Aprender a usar um framework de desenvolvimento de software que você goste. 
- Aprendendo sobre os conceitos de análise de dados e análises estatísticas. 
- Aprender a fazer visualizações de dados e apresentações. 
- Fazer programas para realizar processamentos de dados. 
- Selecionando uma área de interesse e trabalhando nela. 
- Desenvolver habilidades de comunicação e organização que são importantes para trabalho de dados. 
- Trabalhando em projetos em grupo ou sozinho.
```

You can download the eval notebook to test [here](https://github.com/gustrd/cabra/blob/dev/notebooks/inference-cabra-kaggle.ipynb).

## Recent Advancements

- 2023-08-07: Introduced the HIPPO-Opus100 benchmark to assess the quality of each model's fine-tuning.

## Upcoming Objectives

- Language Impact on Prompt Structure: Investigate the differential impacts of using the Alpaca prompt structure in English compared to Portuguese.
- Efficiency Analysis: Examine the efficiency of [Emotional Stimuly](https://techxplore.com/news/2023-08-exploring-effects-emotional-stimuli-large.html) in model performance and response.
- Dataset Enhancement: We aim to improve the Portuguese dataset using advanced translation tools. Our current strategy involves leveraging the [open-instruct-v1-oasst-dolly-hhrlhf](https://huggingface.co/datasets/VMware/open-instruct-v1-oasst-dolly-hhrlhf) dataset, combined with automatic translations from MarinMT and LibreTranslate. The subsequent dataset will undergo HIPPO filtering to eliminate rows containing grammatical errors or those with suboptimal semantic proximity.
- Model Fine-Tuning: As new versions of OpenLlama are launched, we plan to fine-tune our larger models accordingly.
- Alternative Model Study: We are researching alternatives to OpenLlama that are not only efficient but also permit commercial usage, such as the MPT.

## Authors

- [gustrd](https://github.com/gustrd)
