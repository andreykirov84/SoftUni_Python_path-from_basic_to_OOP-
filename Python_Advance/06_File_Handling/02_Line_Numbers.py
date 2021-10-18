line_number = 1
punctuation_marks = ('!', '.', "'", '-', '"', '?', ';', ',', ':', '_')

with open('text.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        else:
            punctuation_mark_counter = 0
            char_number = 0
            for char in line:
                if char in punctuation_marks:
                    punctuation_mark_counter += 1
                if char.isalpha():
                    char_number += 1
            print(f'Line {line_number}: {line.strip()} ({char_number})({punctuation_mark_counter})')
            line_number += 1

