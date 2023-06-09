from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# You need to download the model into the `examples` directory
model_path = './openbuddy-falcon-7b-v1.5-fp16/'
model = AutoModelForCausalLM.from_pretrained(model_path, device_map="auto", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained(model_path)

with open('../system.prompt', 'r', encoding='utf-8') as f:
    prompt = f.read()

prompt += "\n\nUser: Write a poem about yourself.\nAssistant:"
input_ids = tokenizer.encode(prompt, return_tensors='pt')
output_ids = model.generate(input_ids, max_new_tokens=100)
print(tokenizer.decode(output_ids[0], skip_special_tokens=True))