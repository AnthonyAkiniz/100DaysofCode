#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                          Band Name Generator                                  # * #
# * #                          project by: Anthony Akiniz                           # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Python script asks 2 questions, concatenates thems and outputs band name.             #
#                                                                                       #
# Guide:                                                                                #
# Launch by clicking run button in top right in VSCode or: py -3 band_name.py           #
#########################################################################################
print("Welcome to the Band Name Generator.")
street = input("What's name of the street you grew up on?\n")
pet = input("What's your pet's name?\n")
print("Your band name could be " + street + " " + pet)
