# raven-data
Data from the RAVEN project. Most of the information about the project is at the [main Git repo](https://github.com/tommccoy1/raven); this repo is just for the data (which is separate from the main repo because it involves a large number of large files that most users of the code won't need).

WARNING: Some of the documents in this repository contain toxic or inappropriate text. These documents were produced by generating text from large language models, a process that often results in objectionable content.

## Description
All of the files are in `prompts_and_generations/`. The types of files that are included are as follows. Note that, due to data restrictions, the only GPT-2 and WebText files that we can include are ones with prompt length 0:
- Prompts are in the files starting with `webtext_prompts` and `wikitext_prompts`.
- Generated text is in files ending with `.generated`
- The continuations of the prompts from the tests sets are in the files starting `webtext_continuations` and `wikitext_continuations`.
- The generated text annotated for overlap with the training set is in files ending with `.pointwise`. The text annotated for overlap with the context is in files ending with `.context_pointwise`. The text annotated for overlap with the context and/or training set is in files ending with `context_and_training_pointwise`. The format of these files: First is the prompt; then the generated text, after the word `<END_OF_PROMPT>`. Each word is annotated with a number (after a slash); the number is the pointwise novelty score - the size of the smallest novel n-gram ending with that word. E.g., if it is a novel unigram, the number will be 1; if the word itself is not novel but it has never appeared following the word before it, then the number will be 2; etc.
- Reports about n-gram novelty are in files ending with `.ngram_report`.
- Reports about syntactic novelty are in files ending with `.syntax_report`.

## Details of conditions

There are results for all combinations of the following: 
- The models `lstm`, `transformer`, `transfo-xl`, `gpt2` (which is the small size of GPT-2), `gpt2-medium`, `gpt2-large`, and `gpt2-xl`
- The prompt lengths 0, 16, 128, and 512 (except that, for GPT-2 models, we are only able to share files for prompt length 0).
- Top-1 sampling, top-10 sampling, top-40 sampling, top-800 sampling, top-0.75 sampling, top-0.90 sampling, top-0.95 sampling, top-1.0 sampling (i.e., pure sampling), top-1.0 sampling with a temperature of 0.7, top-1.0 sampling with a temperature of 0.9, top-1.0 sampling with a temperature of 1.1, and top-1.0 sampling with a temperature of 1.3. Across model types, the notation in the filenames is somewhat inconsistent, but it should be reasonably clear what condition each file is for; please ask if any are unclear.
- Currently a couple files are missing for gpt2-xl with temperature 1.1 and for gpt2 with top-10 sampling. We are trying to track these down now.

## License

This code is licensed under an [MIT license](https://github.com/tommccoy1/raven/blob/main/LICENSE).

## Citing

If you make use of this code, please cite the following ([bibtex](https://tommccoy1.github.io/raven_bib.html)):

R. Thomas McCoy, Paul Smolensky, Tal Linzen, Jianfeng Gao, and Asli Celikyilmaz.  2021. How much do language models copy from their training data? Evaluating linguistic novelty in text generation using RAVEN.  *arXiv preprint arXiv 2111.09509*.

*Questions? Comments? Email [tom.mccoy@princeton.edu](mailto:tom.mccoy@princeton.edu).*




