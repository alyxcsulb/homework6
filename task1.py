# task 1
# output should have the following:
# Total word count
# Total character count
# The average word length
# The average sentence length
# A word distribution of all words ending in “ly”
# A list of top 10 longest words.

import os

READ_FILE_NAME = 'book1.txt'
READ_MODE = 'r'
WRITE_FILE_NAME = 'summary1.txt'
WRITE_MODE = 'w'

word_count = 0
total_char = 0
avg_sentence = 0
ly_words = 0
top_ten = 0

try:
    book_file = open(READ_FILE_NAME, READ_MODE)
    write_file = open(WRITE_FILE_NAME, WRITE_MODE)

    with write_file, book_file:
        lines = book_file.read()    
        
        # word count
        word_count = lines.split()
        write_file.write(f'Total word count: {len(word_count)}\n')

        #character count
        total_char += sum(len(char) for char in word_count)
        write_file.write(f'Total character count: {len(total_char)}\n')

        #Average word length
        avg_length = 0
        for word in word_count:
            char = len(word)
            total += char
        avg_length = total / len(word_count)
        write_file.write(f'The average word length is: {int(avg_length)}\n')
        
        # Average sentence length 
        avg_sentence = lines.split('.')
        write_file.write(f'The average sentence length is: {int(total / len(avg_sentence))}\n')
        
        # Word distribution of all words ending in "ly"
        # come back to 
        write_file.write('A word distribution of all words ending in "ly" \n')
   
        # List of top 10 longest words in descending order
        # come back to
        write_file.write('A list of top 10 longest words \n')
except:
    print(f'File {READ_FILE_NAME} not found.')