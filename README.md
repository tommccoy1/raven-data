# raven-data
Data from the RAVEN project

# Description
All of the files are in `prompts_and_generations/`. The types of files that are included are as follows. Note that, due to data restrictions, the only GPT-2 and WebText files that we can include are ones with prompt length 0:
- Prompts are in the files starting with `webtext_prompts` and `wikitext_prompts`.
- Generated text is in files ending with `.generated`
- The continuations of the prompts from the tests sets are in the files starting `webtext_continuations` and `wikitext_continuations`.
- The generated text annotated for overlap with the training set is in files ending with `.pointwise`. The text annotated for overlap with the context is in files ending with `.context_pointwise`. The text annotated for overlap with the context and/or training set is in files ending with `context_and_training_pointwise`. The format of these files: First is the prompt; then the generated text, after the word `<END_OF_PROMPT>`. Each word is annotated with a number (after a slash); the number is the pointwise novelty score - the size of the smallest novel n-gram ending with that word. E.g., if it is a novel unigram, the number will be 1; if the word itself is not novel but it has never appeared following the word before it, then the number will be 2; etc.
- Reports about n-gram novelty are in files ending with `.ngram_report`.
- Reports about syntactic novelty are in files ending with `.syntax_report`.




