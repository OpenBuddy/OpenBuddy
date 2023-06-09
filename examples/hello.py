from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_path = 'OpenBuddy/openbuddy-falcon-7b-v5-fp16'
model = AutoModelForCausalLM.from_pretrained(
    model_path, 
    device_map="auto", 
    trust_remote_code=True, 
    torch_dtype=torch.float16)
tokenizer = AutoTokenizer.from_pretrained(model_path)

with open('../system.prompt', 'r', encoding='utf-8') as f:
    prompt = f.read()

prompt += "\n\nUser: Write a poem about yourself.\nAssistant:"
input_ids = tokenizer.encode(prompt, return_tensors='pt').to('cuda')

with torch.no_grad():
    output_ids = model.generate(
        input_ids=input_ids, 
        max_new_tokens=100, 
        eos_token_id=tokenizer.eos_token_id)

print(tokenizer.decode(output_ids[0], skip_special_tokens=True))