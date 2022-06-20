#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                                Nato Alphabet                                  # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Type word and it gives phonetic alphabet for each letter.                             #
#                                                                                       #
# Guide:                                                                                #
# Launch by clicking run button in top right in VSCode or: py -3 main.py                #
#########################################################################################

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
