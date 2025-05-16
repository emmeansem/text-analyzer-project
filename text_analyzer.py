import string
# Load text from file
with open("article.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Clean text
translator = str.maketrans('', '', string.punctuation)
cleaned_text = text.translate(translator).lower()
words = cleaned_text.split()

# First exercise: Unique words
unique_words = set(words)

# Second exercise: Vowel and consonant count
vowels = "aeiou"
counts = {'vowels': 0, 'consonants': 0}

for char in cleaned_text:
    if char.isalpha():
        if char in vowels:
            counts['vowels'] += 1
        else:
            counts['consonants'] += 1

# Word frequencies
word_freq = {}
for word in words:
    word_freq[word] = word_freq.get(word, 0) + 1

# Third exercise: Top 10 most frequent words
sorted_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
top_10 = sorted_words[:10]
top_10_list = [word for word, freq in top_10]

# Printing output
print("\n--- Text Analysis Summary ---")
print(f"Total words: {len(words)}")
print(f"Unique words: {len(unique_words)}")
print(f"Vowel count: {counts['vowels']}")
print(f"Consonant count: {counts['consonants']}")
print("Top 10 most frequent words:")
for word, freq in top_10:
    print(f"{word}: {freq} times")
