def count_words(sentence):
    words = sentence.split()
    return len(words)


text = input("Please, enter your sentence: ")
print(count_words(text))
