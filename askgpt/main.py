import openai
import os

# Set up the OpenAI API key
openai.api_key = "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"

# Call the OpenAI API to generate text
response = openai.Image.create(
    prompt="A guy showing the program to his girlfriend at the beach",
    n=1,
    size="1024x1024"
)
image_url = response['data'][0]['url']

# Print the generated text
print(image_url)
