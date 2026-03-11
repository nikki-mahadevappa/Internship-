from transformers import pipeline

classifier = pipeline("sentiment-analysis")

text = input("Enter text to analyze sentiment: ")

result = classifier(text)

print("Sentiment:", result[0]['label'])
print("Confidence:", result[0]['score'])