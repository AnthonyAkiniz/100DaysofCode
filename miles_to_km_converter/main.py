#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                           Miles to KM Converter                               # * #
# * #                         project by: Anthony Akiniz                            # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Uses tkinter GUI to convert between miles and kilometers.                             #
#                                                                                       #
# Guide:                                                                                #
# Launch by clicking run button in top right in VSCode or: py -3 main.py                #
#########################################################################################

from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.title("Miles/Km Converter")
window.minsize(width=300, height=100)
window.config(padx=50, pady=50)


input = Entry(width=10)
input.insert(END, string="0")
input.grid(column=1, row=0)

label_source = Label(text="Miles", font=("Helvetica", 8, "bold"))
label_source.grid(column=2, row=0)
label_source.config(padx=20)

label_equal = Label(text="is equal to", font=("Helvetica", 8, "normal"))
label_equal.grid(column=0, row=1)

factor = 1.609344
label_value = Label(text="0", font=("Helvetica", 8, "bold"))
label_value.grid(column=1, row=1)


def calc_result():
    miles = float(input.get())
    kms = round(miles * factor, 2)
    label_value.config(text=str(kms))


label_target = Label(text="Km", font=("Helvetica", 8, "bold"))
label_target.grid(column=2, row=1)

button = Button(text="Calculate", command=calc_result)
button.grid(column=1, row=2)


def default2miles():
    global factor
    label_source.config(text="Miles")
    label_target.config(text="Km")
    factor = 1.609344
    calc_result()


def default2km():
    global factor
    label_source.config(text="Km")
    label_target.config(text="Miles")
    factor = 0.62137
    calc_result()


radio_state = IntVar()
radiobutton1 = Radiobutton(text="Miles->Km", value=0,
                           variable=radio_state, command=default2miles)
radiobutton2 = Radiobutton(text="Km->Miles", value=1,
                           variable=radio_state, command=default2km)
radiobutton1.grid(column=1, row=4)
radiobutton2.grid(column=1, row=5)

window.mainloop()
