# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# file_open =open("nato_phonetic_alphabet.csv")
# print(file_open)

import pandas

open_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(open_data)
print(open_data.to_dict())

phonatic_data = {row.letter:row.code for (index, row) in open_data.iterrows()}
print(phonatic_data)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

text = input("Enter Your Name: ").upper()
# answer = [phonatic_data[new] for new in text]
###################################################### OR ##############################
final_answer = [phonatic_data[letter] for letter in text]
print(final_answer)

# for name in text:
#     if name in "data":
#         print(name)