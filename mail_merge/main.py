#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                   Mail Merge for Birthday Invitation Letters                  # * #
# * #                         project by: Anthony Akiniz                            # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Merges a list of names into a letter template and outputs all individual letters.     #
#                                                                                       #
# Guide:                                                                                #
# rename folder mail_merge, cd mail_merge                                               #
# Modify Letter Template at: Input/Letters/starting_letter                              #
# Modify Name List at: Input/Names/invited_names                                        #
# Launch by clicking run button in top right in VSCode or: py -3 main.py                #
# View all letters at: Output/ReadToSend                                                #
#########################################################################################

PLACEHOLDER = "[name]"


with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)
