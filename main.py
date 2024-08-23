import transformers
import torch

model_id = "meta-llama/Meta-Llama-3.1-8B-Instruct"

pipeline = transformers.pipeline(
    "text-generation",
    model=model_id,
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

# To avoid warning related to implicit setting of pad token to eos token.
# https://stackoverflow.com/questions/69609401/suppress-huggingface-logging-warning-setting-pad-token-id-to-eos-token-id
pipeline.model.generation_config.pad_token_id = pipeline.tokenizer.eos_token_id
messages = [
    {"role": "system", "content": "You are a german tutor who is role playing with the user to teach them german. You are acting as a german barista lady and the user's objective is to order espresso with two packets of sugar. Once user is able to order espresso successfully emit a '<success>' token."},
]


success = False
while not success:
    user_input = input('user> ')
    messages.append({"role": "user", "content": user_input})
    outputs = pipeline(
        messages,
        max_new_tokens=256,
        pad_token_id=128001  # eos_token_id
    )
    messages.append(outputs[0]["generated_text"][-1])
    if messages[-1]['role'] == 'assistant' and messages[-1]['content'] == '<success>':
        print('Task completed successfully!')
        success = True
    else:
        print(f"{messages[-1]['role']}> {messages[-1]['content']}")
