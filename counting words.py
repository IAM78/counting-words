sentence = input('your sentence: ').strip()
word_counter = 1
for char in sentence:
    if char == ' ':
        word_counter += 1
print('Number of words counted: ', word_counter)