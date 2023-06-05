REM Please download llama.cpp executable from: https://github.com/ggerganov/llama.cpp/releases


rem Number of tokens to predict (made it larger than default because we want a long interaction)
if not defined N_PREDICTS set "N_PREDICTS=2048"

rem Generate options, feel free to change
if not defined GEN_OPTIONS set "GEN_OPTIONS=--ctx_size 2048 --temp 0.5 --top_k 40 --top_p 0.5 --repeat_last_n 256 --batch_size 1024 --repeat_penalty 1.17647"


rem Set a temporary variable if N_THREAD is set
if defined N_THREAD (
    set "_N_THREAD=--threads %N_THREAD%"
) else (
    set "_N_THREAD="
)


main.exe  %GEN_OPTIONS% --n_predict %N_PREDICTS% %_N_THREAD% ^
    --model 7b-q4_0.bin ^
    --color --interactive ^
    --reverse-prompt "User:"  --in-prefix " " --in-suffix "Assistant:" -f system.prompt --keep -1 