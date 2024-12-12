import openai

openai.api_key = "eyJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6IjIzZjIwMDI2NzFAZHMuc3R1ZHkuaWl0bS5hYy5pbiJ9.uj4hO1sInU9sGJBVWubSiIi0k8Bq7qWeeU3cHdLTa-0"

# Example prompt
prompt = "Does this Python code correctly calculate the mean of a column?\n"
prompt += "import pandas as pd\ndata = pd.DataFrame({'A': [1, 2, 3]})\nprint(data['A'].mean())"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message['content'])
