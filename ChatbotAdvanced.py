import openai

# setup API key
openai.api_key = "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"

# define model to use
model_engine = "text-davinci-002"

# prompt for the model
prompt = "Hello World!"

response = openai.Completion.create(
    engine=model_engine, prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5
)

# get the generated response
message = response["choices"][0]["text"]
print(message)
