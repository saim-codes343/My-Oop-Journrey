sentence = input("Enter a sentence: ")
count = {}
for words in sentence.split():
    count[words] = count.get(words, 0) + 1
for word, count in count.items():
    print(f"{word}: {count}")    