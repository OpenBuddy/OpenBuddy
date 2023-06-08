# OpenBuddy - Open Multilingual Chatbot for Everyone


<div align="center">
  <img src="media/logo.png" width="300px">
</div>


[中文](README.zh.md) | [English](README.md)

Website: [https://openbuddy.ai](https://openbuddy.ai)

GitHub: [https://github.com/OpenBuddy/OpenBuddy](https://github.com/OpenBuddy/OpenBuddy)

Huggingface: https://huggingface.co/OpenBuddy

![Demo](media/demo.png)

OpenBuddy is a powerful open multilingual chatbot model aimed at global users, emphasizing conversational AI and seamless multilingual support for English, Chinese, and other languages.

Built upon Facebook's LLaMA model, OpenBuddy is fine-tuned to include an extended vocabulary, additional common characters, and enhanced token embeddings. By leveraging these improvements and multi-turn dialogue datasets, OpenBuddy offers a robust model capable of answering questions and performing translation tasks across various languages.

Our mission with OpenBuddy is to provide a free, open, and offline-capable AI model that operates on users' devices, irrespective of their language or cultural background. We strive to empower individuals worldwide to access and benefit from AI technology.

## Online Demo

Currently, the OpenBuddy-13B demo is available on our Discord server. Please join our Discord server to try it out!

Discord: [![Discord](https://img.shields.io/discord/1100710961549168640?color=blueviolet&label=Discord)](https://discord.gg/6fU2s9cGjA)


## Key Features

- **Multilingual** conversational AI, Chinese, English, Japanese, Korean, French, Germany and more!
- Built on top of the LLaMA model from Facebook
- Enhanced vocabulary and support for common CJK characters
- Fine-tuned with multi-turn dialogue datasets for improved performance
- Two model versions: 7B and 13B
- 4-bit quantization for CPU deployment via llama.cpp (with slightly reduced output quality)
- Active development plans for future features and improvements

## Model Versions

OpenBuddy currently offers two model versions: 7B and 13B.

More information about downloading the models can be found in the [Models](models.md) page.

## Future Plans

- Enhancing multilingual performance
- Optimizing model quality post-quantization
- Developing a mechanism to assess content quality, safety, and inference capabilities
- Investigating Reinforcement Learning with Human Feedback (RLHF)
- Exploring the addition of multimodal capabilities for dialogues with image context

## Installation

Due to LLaMA licensing restrictions, you need the original LLaMA-7B model to utilize this model. To decrypt the model weights:

1. Acquire the original LLaMA-7B model (not the Huggingface version).
2. Clone this GitHub repository.
3. Ensure that you have Python 3.7 or higher and numpy installed, you can install numpy with `pip install numpy`.
4. Run the following command, try python3 if python does not work:

```
python decrypt.py [path-to-consolidated.00.pth] [path-to-our-model-folder]
```

## Usage with llama.cpp on CPU/GPU (Recommended)

The 7B model has been converted to ggml format, making it compatible with llama.cpp. llama.cpp is a pure C++ inference engine for LLaMA models, originally designed for CPU deployment.

After recent updates, llama.cpp now supports cuBLAS and OpenCL acceleration, which means you can utilize your AMD/NVIDIA GPU to accelerate inference.

The model is available at: [Models](models.md), `(5-bit, CPU/GPU, llama.cpp)` is the variant you should download.

After installing the model and [llama.cpp](https://github.com/ggerganov/llama.cpp), you can run the `chat-llamacpp.bat` or `chat-llamacpp.sh` script to interact with OpenBuddy through the interactive console.

## Usage with Transformers on GPU

Please ensure that your GPU supports bf16 (bfloat16) before attempting to use OpenBuddy with the huggingface's `Transformers` library on a GPU. A 7B model may require up to 24GB of GPU memory.

To use OpenBuddy with huggingface's Transformers library on a GPU, follow the [hello.py](examples/hello.py) example. For a more comprehensive understanding of text generation, please refer to the [Transformers documentation](https://huggingface.co/docs/transformers/index).

## Usage with Inference Frameworks

LLM inference frameworks including [Langport](https://github.com/vtuber-plan/langport) and [FastChat](https://github.com/lm-sys/FastChat), have been adapted to support OpenBuddy. Please refer to the respective repositories for more information.

We are actively working on developing our own inference system, [GrandSage](https://github.com/OpenBuddy/GrandSage). GrandSage is currently in the early stages of development.

## Disclaimer

All OpenBuddy models have inherent limitations and may potentially produce outputs that are erroneous, harmful, offensive, or otherwise undesirable. Users should not use these models in critical or high-stakes situations that may lead to personal injury, property damage, or significant losses. Examples of such scenarios include, but are not limited to, the medical field, controlling software and hardware systems that may cause harm, and making important financial or legal decisions.

OpenBuddy is provided "as-is" without any warranty of any kind, either express or implied, including, but not limited to, the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors, contributors, or copyright holders be liable for any claim, damages, or other liabilities, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

By using OpenBuddy, you agree to these terms and conditions, and acknowledge that you understand the potential risks associated with its use. You also agree to indemnify and hold harmless the authors, contributors, and copyright holders from any claims, damages, or liabilities arising from your use of OpenBuddy.

## License Restrictions

OpenBuddy-LLaMA series models are strictly prohibited for commercial use and are intended for research purposes only. For more information, please refer to the LLaMA License.

For the OpenBuddy-Falcon series models, they are released under the Apache 2.0 License. Please refer to the Apache 2.0 License for applicable scope and restrictions.

Regarding the source code related to the OpenBuddy open-source project (including, but not limited to, test code and the GrandSage Inference project), they are released under the GPL 3.0 License.

## Acknowledgements

We want to thank [AIOS.club](https://github.com/aios-club) for their invaluable support and collaboration in this project. Our appreciation extends to the Facebook AI team for releasing the LLaMA model, which has served as a solid foundation for OpenBuddy's development. Finally, we extend our thanks to the open-source community for their continued support and contributions.
