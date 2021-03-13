import pandas
#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
nato = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index,row) in nato.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
name = input('Enter your name: ').upper()
result = [nato_dict[str] for str in name]
print(result)


