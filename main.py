class Song:
    def __init__(self, title, lyrics, key, bpm):
        self.title = title
        self.lyrics = lyrics
        self.key = key
        self.bpm = bpm
    def countwords(self):
        total_words = 0
        for line in self.lyrics:
            words = line.split()
            total_words += len(words)
        return total_words
lyrics = [
    "Tum hi ho ab tum hi ho",
    "Zindagi ab tum hi ho",
    "Chain bhi mera dard bhi",
    "Meri aashiqui ab tum hi ho"
]
song = Song("Aashiqui Love Theme", lyrics, "G Minor", 90)
print(song.countwords())
