<p align="center" width="100%">
<img src="assets/cabra.png" alt="Cabra" style="width: 20%; min-width: 300px; display: block; margin: auto;">
</p>

# Cabra: A portuguese finetuned instruction Open-LLaMA

This repository is intended to share all the steps and resources that we used to finetune our version of Open-LLaMA.

This model is allowed to commercial purposes, by having the license cc-by-sa-3.0. It only used commercially licensed sources.

The project was strongly inspired by Cabrita ( https://github.com/22-hours/cabrita ), that had a similar solution but without using commercial licensed sources and a smaller 7B model instead of a 13B.

The resulting models can be downloaded at Hugging Face:

[Cabra-13B-LoRA](TODO) - To use with the [original model](https://huggingface.co/VMware/open-llama-13b-open-instruct);
[Cabra-13B-Merged] (TODO) - To standalone use;
[Cabra-13B-GGML] (TODO) - For CPU inference, using [llama.cpp](https://github.com/ggerganov/llama.cpp) or [koboldcpp](https://github.com/LostRuins/koboldcpp);

## References

> If I have seen further it is by standing on the sholders [sic] of Giants.
> -- <cite>Isaac Newton</cite>

We started this section with this citation because everything we did was only possible due to the strong community and works that other people and groups did. For our work, we rely mainly in the works developed by: [Cabrita](https://github.com/22-hours/cabrita), [OpenLlama](https://github.com/openlm-research/open_llama), [Hugging Face](https://huggingface.co/), [Open-Instruct](https://github.com/allenai/open-instruct), [VMware](https://huggingface.co/VMware/open-llama-13b-open-instruct), [Dolly](https://github.com/databrickslabs/dolly) and [LibreTranslate](https://github.com/LibreTranslate/LibreTranslate) .So, thank you all for the great work and contribution to the open-source community!


## Data

We translated the [databricks-dolly-15k.jsonl](https://huggingface.co/datasets/databricks/databricks-dolly-15k/resolve/main/databricks-dolly-15k.jsonl) to portuguese using LibreTranslate. Even if this translation is flawed, the tradeoff between speed, cost and results is good. We could do it at some hours at a consumer grade laptop.
If you want to know more about how the dataset was built go to: [Dolly](https://github.com/databrickslabs/dolly).

We avoided using GPT to the translation, like the original Cabrita project did, because of the problems with licensing.

## Finetuning

To finetuned the OpenLLaMA model we used the code available on [Cabrita](https://github.com/22-hours/cabrita), which provides code to finetune the LLaMA model using PEFT from Hugging Face, we just adapted it to OpenLlama-Instruct. With this, we could run our finetuning step using 1 A4000 at Paperspace on top of OpenLLaMA-OpenInstruct-13B. We trained during around 7 hours and we found the results pretty incredible with just that much time. The notebook we used is avaible [here](TODO).


## Example outputs

open-llama-13b-open-instruct:
```
Instruction: Invente uma desculpa criativa pra dizer que não preciso ir à festa.
Response: Eu preciso se concentrar em trabalho importante para mim, por isso eu não posso ir à festa.
```

Cabra:
```
Instrução: 
Invente uma desculpa criativa pra dizer que não preciso ir à festa.

Resposta: 
"TODO"
```


open-llama-13b-open-instruct:
```
Instruction: Como posso começar a carreira como cientista de dados? Escreva na forma de lista.
Response:
1. Comece por se especializar em um campo específico, como big data, computação, bioinformática ou estatística.
2. Obtivere um diploma em um programa de graduação relacionado a ciência de dados, como informática, matemática ou estatística.
3. Aquisite experiência prática através de internships ou projetos em empresas ou instituições.
4. Ameize sua resumo e currículo com resultados relevantes e experiência em trabalho relacionado.
5. Leia artigos, livros e atualizações sobre ciência de dados.
6. Crie um portfólio com projetos e experimentos que tenha realizado.
7. Receba um certificado de qualificação em alguma área de ciência de dados.
8. Tente obter contato com profissionais da área para conversar sobre oportunidades de emprego.
9. Acesse redes sociais, como LinkedIn, para encontrar empregos e conexões.
10. Continui sua formação atualizando-se com tecnologias e ferramentas de ciência de dados.
```

Cabrita:
```
Instrução: 
Como posso começar a carreira como cientista de dados? Escreva na forma de lista.

Resposta: 
TODO
```

You can test it using the eval notebook [here](TODO).

## Next steps

- Create a better portuguese dataset, using a better tool to translate (some options at DeepL or manual adjust);
- Use a bigger open dataset, avaliable to commercial use, like [RedPajama-Data](https://github.com/togethercomputer/RedPajama-Data);
- Finetune large models when a new OpenLlama is released;

## Authors

- [gustrd](https://github.com/gustrd)
