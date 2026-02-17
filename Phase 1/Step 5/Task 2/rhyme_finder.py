import requests

word = input("Enter a word: ")

prompt = f"Generate a list of 10 English words that rhyme with '{word}'. Only output the words separated by commas."

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "gemma3:4b",
        "prompt": prompt,
        "stream": False
    }
)

data = response.json()

print("\nRhyming words:")
print(data["response"])