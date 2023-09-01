import nltk
from nltk.corpus import words

# Get a list of English words
english_words = set(words.words())

# Function to find words that fit the pattern
def find_words_with_pattern(pattern):
    matching_words = []
    for word in english_words:
        if len(word) == len(pattern):
            match = True
            for i in range(len(word)):
                if pattern[i] != '*' and pattern[i] != word[i]:
                    match = False
                    break
            if match:
                matching_words.append(word)
    return matching_words

# Input word pattern from the user
input_pattern = input("Enter a word pattern with '*' for missing letters: ")

# Find words that fit the pattern
matching_words = find_words_with_pattern(input_pattern)

# Print the matching words
if matching_words:
    print("Words that fit the pattern:", matching_words)
else:
    print("No matching words found for the pattern.")
