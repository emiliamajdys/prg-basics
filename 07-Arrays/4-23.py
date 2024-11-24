import MyText

text = "An apple a day keeps the doctor away"


num_words = MyText.fa(text)
words_longest = MyText.fb(text)
words_alpha = MyText.fc(text)

# Print results
print(f"Text: {text}")
print(f"Number of words: {num_words}")
print(f"Words from the longest: {', '.join(words_longest)}")
print(f"Words ordered alphabetically: {', '.join(words_alpha)}")

