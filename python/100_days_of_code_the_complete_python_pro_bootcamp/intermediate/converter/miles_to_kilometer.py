from tkinter import *

#Creating a new window and configurations
window = Tk()
window.title("Converter")
window.minsize(width=300, height=50)
window.config(padx=20,pady=20)

def miles_to_km():
    miles = input.get()
    km = round(float(miles) * 1.609,2)
    result.config(text=f'{km}')

input = Entry(width=7)
input.grid(column=1,row=0)

label = Label(text="Miles")
label.grid(column=2,row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0,row=1)

result = Label(text="0")
result.grid(column=1,row=1)

satuan_label = Label(text="kilometer")
satuan_label.grid(column=2,row=1)

calculate = Button(text="Calculate",command=miles_to_km)
calculate.grid(column=1,row=2)




window.mainloop()