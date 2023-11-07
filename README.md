# OpenBuddy - Open Multilingual Chatbot for Everyone


<div align="center">
  <img src="media/logo.png" width="300px">
</div>


[中文](README.zh.md) | [English](README.md)

微信公众号、微信群：

<img src="media/mp.jpg" width="285">

搜索“**开源智友**”，关注公众号并发送“加群”即可获得微信群邀请、参与新模型内测等活动

欢迎关注我们的 ModelScope 社区，体验精选模型的高速下载和一键部署：

https://modelscope.cn/organization/OpenBuddy


Website: [https://openbuddy.ai](https://openbuddy.ai)

GitHub: [https://github.com/OpenBuddy/OpenBuddy](https://github.com/OpenBuddy/OpenBuddy)

Huggingface: https://huggingface.co/OpenBuddy



![Demo](media/demo.png)

OpenBuddy is a powerful open multilingual chatbot model aimed at global users, emphasizing conversational AI and seamless multilingual support for English, Chinese, and other languages.

Built upon Tii's Falcon model and Facebook's LLaMA model, OpenBuddy is fine-tuned to include an extended vocabulary, additional common characters, and enhanced token embeddings. By leveraging these improvements and multi-turn dialogue datasets, OpenBuddy offers a robust model capable of answering questions and performing translation tasks across various languages.

Our mission with OpenBuddy is to provide a free, open, and offline-capable AI model that operates on users' devices, irrespective of their language or cultural background. We strive to empower individuals worldwide to access and benefit from AI technology.

## Online Demo

Currently, the OpenBuddy-70B demo is available on our Discord server. Please join our Discord server to try it out!

Discord: [![Discord](https://img.shields.io/discord/1100710961549168640?color=blueviolet&label=Discord)](https://discord.gg/6fU2s9cGjA)


## Key Features

- **Multilingual** conversational AI, Chinese, English, Japanese, Korean, French, Germany and more!
- Enhanced vocabulary and support for common CJK characters
- Fine-tuned with multi-turn dialogue datasets for improved performance
- Various model sizes to suit your needs: 3B, 7B, 13B, 30B, 40B, 65B, 70B and more!
- 3/4/5-bit quantization for CPU deployment via llama.cpp (with slightly reduced output quality)
- Active development plans for future features and improvements

## Future Plans

- Enhancing multilingual performance
- Optimizing model quality post-quantization
- Developing a mechanism to assess content quality, safety, and inference capabilities
- Investigating Reinforcement Learning with Human Feedback (RLHF)
- Exploring the addition of multimodal capabilities for dialogues with image context

## Model Download

OpenBuddy currently offers model downloads on HuggingFace and ModelScope.

More information about downloading the models can be found in the [Models](models.md) page.

## Prompt Format

Model input should be formatted as follows:

```
You are a helpful, respectful and honest INTP-T AI Assistant named Buddy. You are talking to a human User.
Always answer as helpfully and logically as possible, while being safe. Your answers should not include any harmful, political, religious, unethical, racist, sexist, toxic, dangerous, or illegal content. Please ensure that your responses are socially unbiased and positive in nature.
If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct. If you don't know the answer to a question, please don't share false information.
You can speak fluently in many languages, for example: English, Chinese.
You cannot access the internet, but you have vast knowledge, cutoff: 2021-09.
You are trained by OpenBuddy team, (https://openbuddy.ai, https://github.com/OpenBuddy/OpenBuddy), you are based on LLaMA and Falcon transformers model, not related to GPT or OpenAI.

User: {History input}
Assistant: {History output}
User: {Input}
Assistant:
```

Please note there should not be any spaces or line breaks after the last "Assistant:" line.


## Usage with llama.cpp on CPU/GPU (Recommended)

Models have been converted to ggml format, making it compatible with llama.cpp. llama.cpp is a pure C++ inference engine for LLaMA models, originally designed for CPU deployment.

After recent updates, llama.cpp now supports cuBLAS and OpenCL acceleration, which means you can utilize your AMD/NVIDIA GPU to accelerate inference.

The model is available at: [Models](models.md), `GGML format` is the variant you should download.

After installing the model and [llama.cpp](https://github.com/ggerganov/llama.cpp), you can run the `chat-llamacpp.bat` or `chat-llamacpp.sh` script to interact with OpenBuddy through the interactive console.

For now, only OpenBuddy-LLaMA series models are supported by llama.cpp, the developers of llama.cpp are working on adding support for Falcon models.

## Usage with Transformers on a high-end GPU

To use OpenBuddy with huggingface's Transformers library on a GPU, follow the [hello.py](examples/hello.py) example. For a more comprehensive understanding of text generation, please refer to the [Transformers documentation](https://huggingface.co/docs/transformers/index). A 7B model may require up to 24GB of GPU memory.

## Usage with Inference Frameworks

LLM inference frameworks including [Langport](https://github.com/vtuber-plan/langport) and [FastChat](https://github.com/lm-sys/FastChat), have been adapted to support OpenBuddy. Please refer to the respective repositories for more information.

We are actively working on developing our own inference system, [GrandSage](https://github.com/OpenBuddy/GrandSage). GrandSage is currently in the early stages of development.

## Disclaimer

All OpenBuddy models have inherent limitations and may potentially produce outputs that are erroneous, harmful, offensive, or otherwise undesirable. Users should not use these models in critical or high-stakes situations that may lead to personal injury, property damage, or significant losses. Examples of such scenarios include, but are not limited to, the medical field, controlling software and hardware systems that may cause harm, and making important financial or legal decisions.

OpenBuddy is provided "as-is" without any warranty of any kind, either express or implied, including, but not limited to, the implied warranties of merchantability, fitness for a particular purpose, and non-infringement. In no event shall the authors, contributors, or copyright holders be liable for any claim, damages, or other liabilities, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.

By using OpenBuddy, you agree to these terms and conditions, and acknowledge that you understand the potential risks associated with its use. You also agree to indemnify and hold harmless the authors, contributors, and copyright holders from any claims, damages, or liabilities arising from your use of OpenBuddy.

## License Restrictions

OpenBuddy-LLaMA series models are subject to Meta's licensing agreement. These models are intended for use only by individuals who have obtained approval from Meta and are eligible to download LLaMA. If you have not obtained approval from Meta, you must visit the https://ai.meta.com/llama/ page, read and agree to the model's licensing agreement, submit an application, and wait for approval from Meta before downloading the model from the model page.

For the OpenBuddy-Falcon and OpenBuddy-OpenLLaMA series models, they are released under the Apache 2.0 License. Please refer to the Apache 2.0 License for applicable scope and restrictions.

Regarding the source code related to the OpenBuddy open-source project (including, but not limited to, test code and the GrandSage Inference project), they are released under the GPL 3.0 License.

## Acknowledgements

We extend our deepest gratitude to the open-source community for their selfless assistance and contributions to the OpenBuddy project.

Firstly, we would like to specifically thank WeiKe Software for their robust support and help in the aspect of model training. We also want to thank [AIOS.club](https://github.com/aios-club) for their invaluable support.

We owe our thanks to [Mr. Su Jianlin](https://kexue.fm/) for providing invaluable advice during the model training process. Not only did he provide professional advice, but he also introduced the NBCE method, which enables open-source models like OpenBuddy to support inference with a super-long context of 10K. This has had a profound impact on our work.

Our appreciation goes to [flysnow](https://www.flysnow.org/about/) and [jstzwj](https://github.com/jstzwj). They provided valuable advice during the early stages of model development and extended substantial support and assistance in model inference.

At the same time, we also wish to express our gratitude to camera and other enthusiasts of open language models. Their suggestions played a pivotal role in improving the model.

Once again, we thank everyone who has contributed to the OpenBuddy project. Our success is inseparable from your support and encouragement. Moreover, we acknowledge Tii and Facebook for introducing the Falcon model and the LLaMA model, respectively, which have laid a solid foundation for our project.