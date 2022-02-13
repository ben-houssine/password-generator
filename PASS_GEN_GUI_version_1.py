import string
import random
from tkinter import *
import tkinter as tk
from datetime import datetime
import time



def printSomething():
    characters = list(string.ascii_letters + string.digits + "!@#$%^&*()_-")
    char1 = []
    char2 = []
    char3 = []
    char4 = []
    char5 = []
    char6 = []
    char7 = []
    char8 = []
    char9 = []
    char10 = []

    char1.append(random.choice(characters))
    char2.append(random.choice(characters))
    char3.append(random.choice(characters))
    char4.append(random.choice(characters))
    char5.append(random.choice(characters))
    char6.append(random.choice(characters))
    char7.append(random.choice(characters))
    char8.append(random.choice(characters))
    char9.append(random.choice(characters))
    char10.append(random.choice(characters))

    ## now combine it all together to a single varaible
    combine_all_char = char1 + char2 + char3 + char4 + char5 +char6 + char7 + char8 + char9 + char10

    ## join it together without the "" in between
    password = "".join(combine_all_char)

    label = Label(root, text= password)           
    label.pack() 



## adding current time to gui   
def show_time():      
    current_time = time.strftime("%H:%M:%S")
    label_2 = Label(root, text= current_time)
    label_2.pack()
    print(current_time)

##public var for current time
current_time = time.strftime("%H:%M:%S")



##gui and Buttons
root = Tk()
## creating Buttons
button_1 = Button(root, text=" ▶ Start ", command=printSomething)
#button_2 = Button(root, text=" Time ", command=show_time)


##gui design
root.title("Password Generator - version 1")
root.geometry("400x400")
button_1.place(x=20, y=20)
#button_2.place(x=20,y=50)
Upper_right = tk.Label(root,text =current_time)
 


## postion
Upper_right.place(relx = 1.0,
                  rely = 0.0,
                  anchor ='ne')


root.mainloop()

## crated 12.02.2022
## by Mr. Youssef Ben Houssine
## https://github.com/ben-houssine