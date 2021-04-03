from tkinter import * # We are not just importing tkinter , we are importing all the functions in tkinter by using *
                      # because if we just use 'import tkinter' some functions like Tk() might not be actually imported

var = "" # Declaring a empty string variable for displaying our output

def btn1_click():  # Defining a function to show what happens when 1 is clicked
    global var
    var = var + "1" # If button 1 is clicked , var variable holds the character 1
    data.set(var) # Setting the data variable with the value in var 
                  # data variable is the variable whose value is displayed in the label widget

def btn2_click(): # Defining a function to show what happens when 2 is clicked
    global var
    var = var + "2"
    data.set(var)

def btn3_click(): # Defining a function to show what happens when 3 is clicked
    global var
    var = var + "3"
    data.set(var)

def btn4_click(): # Defining a function to show what happens when 4 is clicked
    global var
    var = var + "4"
    data.set(var)

def btn5_click(): # Defining a function to show what happens when 5 is clicked
    global var
    var = var + "5"
    data.set(var)

def btn6_click(): # Defining a function to show what happens when 6 is clicked
    global var
    var = var + "6"
    data.set(var)

def btn7_click(): # Defining a function to show what happens when 7 is clicked
    global var
    var = var + "7"
    data.set(var)

def btn8_click(): # Defining a function to show what happens when 8 is clicked
    global var
    var = var + "8"
    data.set(var)

def btn9_click(): # Defining a function to show what happens when 9 is clicked
    global var
    var = var + "9"
    data.set(var)

def btn0_click(): # Defining a function to show what happens when 0 is clicked
    global var
    var = var + "0"
    data.set(var)

def btnC_click(): # Defining a function to show what happens when C is clicked
    global var
    var = "" # Button C stands for Clear
             # When C is clicked , it resets var to a empty string 
    data.set(var)

def btn_plus_click(): # Defining a function to show what happens when + is clicked
    global var
    var = var + "+" # If button + is clicked , var variable holds the character +
    data.set(var)

def btn_minus_click(): # Defining a function to show what happens when - is clicked
    global var
    var = var + "-" 
    data.set(var)

def btn_mult_click(): # Defining a function to show what happens when * is clicked
    global var
    var = var + "*"
    data.set(var)

def btn_div_click(): # Defining a function to show what happens when / is clicked
    global var
    var = var + "/"
    data.set(var)

def last_character_delete(): # Defining a function to eliminate the last character 
                             # if the last character happens to be +,-,*or /
    global var
    length = len(var); # Taking the length of the var variable, so as to find the last index of var
    if(var[length-1] == "+" or var[length-1] == "-" or var[length-1] == "*" or var[length-1] == "/"):
        var = var[:-1] # Removing the last character
        last_character_delete() # Recursive call till last character is not +,-,*or/

def result(): # Defining a function to evaluate the result
    global var
    last_character_delete() # To Eliminate the charcters +,-,*./ if it occurs at last index
    c = 0 # Variable to find the index of 0, if division by 0 occurs
    for i in var: # To check if division by 0 occurs
        c += 1 
        if i == "/":
            if var[c] == "0": # if division by 0 occurs, var is set to "Infinity"
                var = "Infinity"
                data.set(var)
                break # Exiting the loop
           
    temp = var # variable to store the current value of var
    if(temp != "Infinity"): # Evaluation only takes place if division by 0 does not occur
                            # if it occurs, the value in var will be "Infinity" and evaluating
                            # "Infinity" will raise a error
        temp = eval(temp) # Function evaluate the result 
                          # This fubctiob coverts the String input to the neccessary data types and 
                          #evaluates them, it makes things way easier!
        if (type(temp) == float): # To round off the number 
            temp = round(temp,4) # Rounding off upto 4 decimal places
            temp = str(temp)
            if len(temp.split(".", 1)[1]) == 1: # Making sure .0 doesn't come
                if(temp.split(".", 1)[1] == 0):  # eg. To make 8.0 as 8 
                    temp = float(temp)           
                    temp = int(temp)  # Makes the .0 disappears as it converts float to int      
        var = str(temp)  # Converting temp back to string as data variable can only display strings     
    
    data.set(var)
    if (temp == "Infinity"):
        var = "" # Resetting the result to empty string if Infinity appears
                 # Else remaining calculation is going to be carried out with "Infinity"
                 # which might raise error.
     

my_calculator = Tk() # Creating a window
my_calculator.title("Calculator") # Giving a title to the window
my_calculator.geometry("250x300") # Defining the dimensions of the window
my_calculator.resizable(0,0) # Disabling the resizing property of the window
                             # i.e window cannot be resized, this is because the window looks
                             # more beautiful when it's in the fixed size, if it is resized 
                             # contents will look weird.

data = StringVar() # Variable for displaying the result
 
display_text = Frame(my_calculator) # Creating a Frame for the label, where result is displayed
display_text.pack(expand=True, fill="both") # Adjusting the size and spacing of the frame

label = Label(      # Creating a Label widget
    display_text,  
    anchor=SE, # Setting the position where result should be displayed 
               # i.e here it's South East of the Frame , bottom right corner
    font=("Verdana",22), # Fixing the font and size 
    textvariable=data,  # Passing the data variable which holds the result to be displayed
    )
label.pack(expand=True, fill="both") # Setting the size and spacing for the Label widget

button_row_1 = Frame(my_calculator) # Creating a Frame for row 1
button_row_1.pack(expand=True, fill="both")

button_row_2 = Frame(my_calculator) # Creating a Frame for row 2
button_row_2.pack(expand=True, fill="both")

button_row_3 = Frame(my_calculator) # Creating a Frame for row 3
button_row_3.pack(expand=True, fill="both")

button_row_4 = Frame(my_calculator) # Creating a Frame for row 4
button_row_4.pack(expand=True, fill="both")

# Button Row 1
button_value_1 = Button( # Setting the properties of the button
    button_row_1,
    text="1", # Setting the text to be displayed on the button
    font=("Verdana", 15),
    relief=GROOVE, # Eliminating the outward push effect of the button
    border=0, # Removing the border effect of the button
    command=btn1_click, # Passing the function it should execute, when it's clicked
)
button_value_1.pack(side="left", expand=True, fill="both") # Setting the size and spacing for the button

button_value_2 = Button(
    button_row_1,
    text="2",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn2_click,
)
button_value_2.pack(side="left", expand=True, fill="both")

button_value_3 = Button(
    button_row_1,
    text="3",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn3_click,
)
button_value_3.pack(side="left", expand=True, fill="both")

button_value_plus = Button(
    button_row_1,
    text="+",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn_plus_click,
)
button_value_plus.pack(side="left", expand=True, fill="both")

# Button Row 2
button_value_4 = Button(
    button_row_2,
    text="4",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn4_click,
)
button_value_4.pack(side="left", expand=True, fill="both")

button_value_5 = Button(
    button_row_2,
    text="5",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn5_click
)
button_value_5.pack(side="left", expand=True, fill="both")

button_value_6 = Button(
    button_row_2,
    text="6",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn6_click,
)
button_value_6.pack(side="left", expand=True, fill="both")

button_value_minus = Button(
    button_row_2,
    text="-",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn_minus_click,
)
button_value_minus.pack(side="left", expand=True, fill="both")

# Button Row 3
button_value_7 = Button(
    button_row_3,
    text="7",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn7_click,
)
button_value_7.pack(side="left", expand=True, fill="both")

button_value_8 = Button(
    button_row_3,
    text="8",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn8_click,
)
button_value_8.pack(side="left", expand=True, fill="both")

button_value_9 = Button(
    button_row_3,
    text="9",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn9_click,
)
button_value_9.pack(side="left", expand=True, fill="both")

button_value_mult = Button(
    button_row_3,
    text="*",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn_mult_click,
)
button_value_mult.pack(side="left", expand=True, fill="both")

# Button Row 4
button_value_C = Button(
    button_row_4,
    text="C",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btnC_click,
)
button_value_C.pack(side="left", expand=True, fill="both")

button_value_0 = Button(
    button_row_4,
    text="0",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn0_click,
)
button_value_0.pack(side="left", expand=True, fill="both")

button_value_eq = Button(
    button_row_4,
    text="=",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=result,
)
button_value_eq.pack(side="left", expand=True, fill="both")

button_value_div = Button(
    button_row_4,
    text="/",
    font=("Verdana", 15),
    relief=GROOVE,
    border=0,
    command=btn_div_click,
)
button_value_div.pack(side="left", expand=True, fill="both")


my_calculator.mainloop() # This loops our event, till the close button is clicked