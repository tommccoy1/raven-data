

import os
filenames = os.listdir(".")

found = 0
total = 0

suffixes = [".generated", ".generated.trimmed.context_and_training_pointwise", ".generated.trimmed.context_and_training_pointwise.ngram_report", ".generated.trimmed.context_pointwise", ".generated.trimmed.context_pointwise.ngram_report", ".generated.trimmed.pointwise", ".generated.trimmed.pointwise.ngram_report", ".generated.trimmed.detokenized.sentences.parsed.syntax_report"]

# LSTM
for prompt_length in ["0", "16", "128", "512"]:
    for method in ["topk_1_topp_None_temp_1.0", "topk_10_topp_None_temp_1.0", "topk_40_topp_None_temp_1.0", "topk_800_topp_None_temp_1.0", "topk_None_topp_0.75_temp_1.0", "topk_None_topp_0.9_temp_1.0", "topk_None_topp_0.95_temp_1.0", "topk_None_topp_1.0_temp_1.0", "topk_None_topp_None_temp_0.7", "topk_None_topp_None_temp_0.9", "topk_None_topp_None_temp_1.1", "topk_None_topp_None_temp_1.3"]:
        for suffix in suffixes:
            filename = "lstm_wikitext_prompts_length" + prompt_length + "_1of1.txt_" + method + "_length_1010" + suffix
            if filename in filenames:
                found += 1
            else:
                print(filename)

            total += 1

# Transformer-XL
for prompt_length in ["0", "16", "128", "512"]:
    for method in ["k1_p1.0_temp1.0", "k10_p1.0_temp1.0", "k40_p1.0_temp1.0", "k800_p1.0_temp1.0", "k1234567890_p0.75_temp1.0", "k1234567890_p0.9_temp1.0", "k1234567890_p0.95_temp1.0", "k1234567890_p1.0_temp1.0", "k1234567890_p1.0_temp0.7", "k1234567890_p1.0_temp0.9", "k1234567890_p1.0_temp1.1", "k1234567890_p1.0_temp1.3"]:
        for suffix in suffixes:
            filename = "transfo-xl-wt103_wikitext_prompts_length" + prompt_length + "_1of1.txt_" + method + "_beam1_len1010_batchsize4" + suffix
            if filename in filenames:
                found += 1
            else:
                print(filename)

            total += 1

# Transformer
for prompt_length in ["0", "16", "128", "512"]:
    for method in ["k1_pNone_tempNone", "k10_pNone_tempNone", "k40_pNone_tempNone", "k800_pNone_tempNone", "kNone_p0.75_tempNone", "kNone_p0.9_tempNone", "kNone_p0.95_tempNone", "kNone_p1.0_tempNone", "kNone_pNone_temp0.7", "kNone_pNone_temp0.9", "kNone_pNone_temp1.1", "kNone_pNone_temp1.3"]:
        for suffix in suffixes:
            filename = "transformer_wikitext_prompts_length" + prompt_length + "_1of1.txt." + method + suffix
            if filename in filenames:
                found += 1
            else:
                print(filename)

            total += 1

# GPT-2
for size, batchsize in [("", "50"), ("-medium", "32"), ("-large", "16"), ("-xl", "5")]:
    for prompt_length in ["0"]:
        for method in ["k1_p1_temp1.0", "k10_p1_temp1.0", "k40_p1_temp1.0", "k800_p1_temp1.0", "k1234567890_p0.75_temp1.0", "k1234567890_p0.9_temp1.0", "k1234567890_p0.95_temp1.0", "k1234567890_p1.0_temp1.0", "k1234567890_p1.0_temp0.7", "k1234567890_p1.0_temp0.9", "k1234567890_p1.0_temp1.1", "k1234567890_p1.0_temp1.3"]:
            for suffix in suffixes:
                filename = "gpt2" + size + "_webtext_prompts_length" + prompt_length + "_1of1_" + method + "_beam1_len1300_batchsize" + batchsize + suffix.replace(".trimmed", ".trimmed.word.moses").replace(".word.moses.detokenized.sentences", ".word.sentences")
                if filename in filenames:
                    found += 1
                else:
                    print(filename)

                total += 1




print(found, total)




