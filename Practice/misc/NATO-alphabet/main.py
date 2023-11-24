import pandas

is_on = True
df = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row['letter']:row['code'] for (index,row) in df.iterrows()}

def generate_phonetic():
    user_input = input("Type a word to convert: ")

    try: 
        word_list = [nato_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in alphabet please.")
        generate_phonetic()
    else:
        print(word_list)
        
generate_phonetic()



