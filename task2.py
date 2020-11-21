# task 2
# case in-sensiive (a= A)
# output should show letters in alphabetical order
# include dictionary

import os

READ_SENTENCE = 'book2.txt'
READ_MODE = 'r'
WRITE_LETTERS = 'summary2.txt'
WRITE_MODE = 'w'
letters = []
frequency = []

try:
    with open (READ_SENTENCE, READ_MODE) as content:
        for line in content:
            content = line.rstrip('\n')
            for letter in content:
                letter = letter.lower()
                if letter not in letters and ord(letter) >= 97 and ord(letter) <= 122:
                    letters += [letter]
                    frequency += [[letter,1]]
                else:
                    for bracket in frequency:
                        if letter in bracket [0]:
                            frequency[frequency.index(bracket)][1] += 1
    letters.sort()

    with open (WRITE_LETTERS, WRITE_MODE) as text:
        for letter in letters:
            for bracket in frequency:
                if letter == bracket[0]:
                    text.write(f'{bracket[0].upper()} {bracket[1]}\n')
            if len(letters) == 26:
                text.write(f'It does have all letters ')
            else:
                text.write(f'It does not have all letters ')
except:
    print(f'File {READ_SENTENCE} not found.')                                                        