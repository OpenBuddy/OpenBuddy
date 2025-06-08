# Controlling Thinking Behavior in OpenBuddy thinker models

This guide explains how to control the thinking behavior of the OpenBuddy thinker models across different API protocols, assuming the model is served via `vllm`.

This guide is applicable with our `thinker` models, `version 26` and above.

## Using with /v1/chat/completions API

### Thinking Mode

For detailed, step-by-step reasoning responses, use the following system prompt:

```
You(assistant) are a helpful, respectful and honest INTP-T AI Assistant named Buddy. You are talking to a human(user).
Current mode: System 2, think step-by-step and answer.
```

This mode encourages the model to break down complex problems and show its reasoning process before providing a final answer.

### Non-thinking Mode

For direct, concise responses without showing the reasoning process, use:

```
You(assistant) are a helpful, respectful and honest INTP-T AI Assistant named Buddy. You are talking to a human(user).
Current mode: System 1, answer directly.
```

## Using with /v1/completions API

We recommend using the raw `/v1/completions` API for precise control of the thinking behavior, particularly in complex dialogues requiring mixed thinking/non-thinking modes.

### For Thinking Mode

```
<|role|>system<|says|>system prompt...<|end|>
<|role|>user<|says|>History input 1<|end|>
<|role|>assistant<|says|>History output 1<|end|>
<|role|>user<|says|>Current input<|end|>
<|role|>assistant<|says|><think>
```

### For Non-thinking Mode

```
<|role|>system<|says|>system prompt...<|end|>
<|role|>user<|says|>History input 1<|end|>
<|role|>assistant<|says|>History output 1<|end|>
<|role|>user<|says|>Current input<|end|>
<|role|>assistant<|says|><think></think>
```

The special tags `<think>` and `</think>` at the end of the assistant prompt control whether the model shows its reasoning process or provides direct answers.


