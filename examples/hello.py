from transformers import LlamaForCausalLM, LlamaTokenizer
import torch

model_path = './openbuddy-7b-v1.3-bf16'
model = LlamaForCausalLM.from_pretrained(model_path, torch_dtype=torch.bfloat16, device_map="auto") 
tokenizer = LlamaTokenizer.from_pretrained(model_path)

with open('../system.prompt', 'r', encoding='utf-8') as f:
    prompt = f.read()

prompt += "\n\nUser: Write a poem about yourself.\nAssistant:"
input_ids = tokenizer.encode(prompt, return_tensors='pt')
output_ids = model.generate(input_ids, max_length=100)
print(tokenizer.decode(output_ids[0], skip_special_tokens=True))