# OpenBuddy - 开放的跨语言对话模型

[中文](README.zh.md) | [English](README.md)

![Demo](media/demo.png)

OpenBuddy 是一个功能强大的开源跨语言对话模型，提供无缝的多语言支持，包括中文、英语和其他语言。

基于 Facebook 的 LLaMA 基础模型，OpenBuddy 已经对词表进行了扩展并提升了 Token Embedding。通过将这些改进与多轮对话数据集相结合，OpenBuddy 提供了一款能够用中文、英文和其它多种语言回答问题并完成翻译等跨语言任务的强大模型。

## 主要特点

- 专注于跨语言能力、创造力的对话型语言模型
- 基于 Facebook 的 LLaMA 模型构建
- 扩展词汇表，增加常用CJK字符支持
- 结合多轮对话数据集进行微调以提高性能
- 提供两个模型版本：7B 和 13B
- 可以量化为 4 位，使用 llama.cpp 在 CPU 上部署（输出质量略有降低）
- 持续演进，未来会提供更多功能和改进

## 模型版本

OpenBuddy 目前提供两个模型版本：7B 和 13B。

模型的更多信息和下载地址请参阅 [models.md](models.md)。

## 未来计划

- 进一步完善对更多语言的支持
- 优化量化后的内容质量
- 建立评估模型的内容质量、安全性、推理能力的机制
- 尝试人类反馈强化学习（RLHF）
- 尝试添加针对输入图片开展对话的多模态能力

## 安装

由于 LLaMA 的许可限制，您需要拥有原版的 LLaMA-7B 模型才能使用此模型。要解密模型权重，请先获取原版的LLaMA-7B模型（不是huggingface版本的），然后使用以下命令：

```
python(3) decrypt.py [path-to-consolidated.00.pth] [path-to-our-model-folder]
```

## 使用 llama.cpp 在 CPU 上运行（推荐）

7B 模型已转换为 ggml 4-bit 格式，与 llama.cpp 兼容。

模型可在以下位置获取：[Models](models.md)，`(4-bit, CPU, llama.cpp)`是针对 llama.cpp 的量化模型。

安装模型和 [llama.cpp](https://github.com/ggerganov/llama.cpp) 后，运行 `chat-llamacpp.bat` 或 `chat-llamacpp.sh` 脚本，即可通过交互式控制台与 OpenBuddy 互动。

## 在 GPU 上使用 Transformers 运行

首先，请确保 GPU 支持 bf16（bfloat16）格式。

要在 GPU 上使用 OpenBuddy，请参考以下示例代码：

```Python
from transformers import LlamaForCausalLM, LlamaTokenizer
model_path = './openbuddy-7b-bf16-enc'
model = LlamaForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map="auto") 
tokenizer = LlamaTokenizer.from_pretrained(model_path)
```

使用 Huggingface Transformers 库加载 OpenBuddy 模型和 tokenizer 后，可以通过模型的 generate 方法生成文本。要更全面地了解文本生成，请参阅 Transformers 文档。

## 免责声明

OpenBuddy 按照不提供任何明示或暗示的保证的前提下提供。作者和贡献者不对因使用或无法使用本软件而产生的任何损害承担责任。使用 OpenBuddy 即表示您同意这些条款和条件。

## 许可限制

OpenBuddy 仅限于非商业的研究目的使用，与 LLaMA 模型的限制相同。严禁任何超出此范围的使用。

## 鸣谢

我们要感谢 [AIOS.club](https://github.com/aios-club) 在此项目中提供的宝贵支持与合作。同时，我们感谢 Facebook AI 团队发布了 LLaMA 模型，这为 OpenBuddy 的发展奠定了坚实的基础。最后，我们要感谢开源社区的持续支持与贡献。
