# import tkinter

# window = tkinter.Tk()
# window.title("My page")
# window.minsize(width=500 , height=300 )

# #label
# my_label = tkinter.Label(text="I am a label",font=("Arial",24,"bold","italic"))
# my_label.pack()




# window.mainloop()


def add(*args):    
    sum = 0
    for n in args:
        sum += n
    return sum

def calculate(n,**kwargs):
    print(kwargs)
    # for key,value in kwargs.items():
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
        

calculate(2,add=3,multiply=5)