import pandas as pd

#TODO 1. Create a dictionary in this format:
df = pd.read_csv("/Users/ferdinand.sanjaya/Documents/Course/python/100_days_of_code_the_complete_python_pro_bootcamp/intermediate/nato_alphabet/nato_phonetic_alphabet.csv")
# print(df)
alphabet_dictionary = {row.letter:row.code for (index,row) in df.iterrows()}
# {"A": "Alfa", "B": "Bravo"}
# print(alphabet_dictionary)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
spelling = input(f'Enter a word: ').upper()
character = [alphabet_dictionary[letter] for letter in spelling]
print(character)
