import os
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import string


folder_path = "csv"  

all_text = ""


for filename in os.listdir(folder_path):
    if filename.endswith(".csv"):
        filepath = os.path.join(folder_path, filename)
        df = pd.read_csv(filepath)

        
        lyrics_col = None
        for col in df.columns:
            if "lyric" in col.lower():
                lyrics_col = col
                break
        
        if lyrics_col is None:
            continue 

        lyrics_list = df[lyrics_col].dropna().astype(str).tolist()
        all_text += " ".join(lyrics_list) + " "

all_text = all_text.lower()
all_text = all_text.translate(str.maketrans("", "", string.punctuation))
words = all_text.split()

counter = Counter(words)
top20 = counter.most_common(20)
labels, counts = zip(*top20)

plt.figure(figsize=(12, 6))
plt.bar(labels, counts)
plt.title("Top 20 Most Frequently Used Words in Lyrics")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
