from random import choice
list_of_words = ['apple', 'strawberry', 'blackberry', 'orange', 'cherry']
word = list(choice(list_of_words))
current_word = list('*' * len(word))
for i in range(5):
    letter = input('Guess a letter: ')
    if letter in word:
        print('Hit!', end='\n\n')
        for idx, val in enumerate(word):
            if val == letter:
                current_word[idx] = val
    else:
        print(f'Missed, mistake {i + 1} out of 5.', end='\n\n')
    wordToPrint = ''.join(current_word)
    print(f'The word: {wordToPrint}', end='\n\n')
if current_word == word:
    print('You won!')
else:
    print('You lost!')
