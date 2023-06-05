#!/bin/bash

# Please clone and build llama.cpp from: https://github.com/ggerganov/llama.cpp

# Number of tokens to predict (made it larger than default because we want a long interaction)
N_PREDICTS="${N_PREDICTS:-2048}"

# Note: you can also override the generation options by specifying them on the command line:
GEN_OPTIONS="${GEN_OPTIONS:---ctx_size 2048 --temp 0.5 --top_k 40 --top_p 0.5 --repeat_last_n 256 --batch_size 1024 --repeat_penalty 1.17647}"



./main $GEN_OPTIONS --n_predict "$N_PREDICTS" \
    --model 7b-q4_0.bin \
    --color --interactive \
    --reverse-prompt "User:"  --in-prefix " " --in-suffix "Assistant:" -f llamacpp.prompt --keep -1