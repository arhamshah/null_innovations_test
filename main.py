from functions import *

# Task 1 (First Part)
data = extract_text_file('source.txt')
transformed_data_1 = capital_words(data)
write_text_file('task1.txt', transformed_data_1)

# Task 2 (Second Part)
transformed_data_2 = count_word_occurrences(data)
write_text_file('task2.txt', transformed_data_2)
