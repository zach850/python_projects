import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
nato_dict = {row['letter']:row['code'] for (index,row) in df.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Type a word to convert: ")

word_list = [nato_dict[letter.upper()] for letter in user_input]
print(word_list)




