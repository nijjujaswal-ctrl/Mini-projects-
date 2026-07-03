# Word Frequency Counter

passage = input("Enter a passage: ")

words = passage.lower().split()

frequency = {}

for word in words:
    frequency[word] = frequency.get(word, 0) + 1

freq_dict = {word: count for word, count in frequency.items()}

top_words = sorted(freq_dict.items(),
                   key=lambda x: x[1],
                   reverse=True)[:5]

print("\nWord Frequencies:")
for word, count in frequency.items():
    print(f"{word}: {count}")

print("\nTop 5 Most Frequent Words:")
for word, count in top_words:
    print(f"{word}: {count}")
