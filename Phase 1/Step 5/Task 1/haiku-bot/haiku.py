from google import genai

# Create Gemini client with your API key
client = genai.Client(api_key="AIzaSyCl266WsixWTSdUq00cG6i5Y4pOVXUcdo8")

def generate_haiku(word):
    prompt = f"""
    Write a haiku about the word "{word}".
    Follow the 5-7-5 syllable structure strictly.
    """

    response = client.models.generate_content(
        model="models/gemini-pro-latest",
        contents=prompt
    )

    return response.text


# Main program
word = input("Enter a word: ")
print("\nYour Haiku:\n")
print(generate_haiku(word))
