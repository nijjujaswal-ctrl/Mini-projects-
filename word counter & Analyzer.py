# Word Counter & Analyzer

paragraph = input("Enter a paragraph: ")

words = paragraph.split()
word_count = len(words)

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

vowel_count = 0
vowels = "aeiouAEIOU"

for char in paragraph:
    if char in vowels:
        vowel_count += 1

print("\n----- Analysis Result -----")
print("Total Words:", word_count)
print("Longest Word:", longest_word)
print("Length of Longest Word:", len(longest_word))
print("Total Vowels:", vowel_count)
