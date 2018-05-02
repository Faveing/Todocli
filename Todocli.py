import os
import sys

# List that the Todo's will be loaded into
Todos = {
    1:"",
    2:"",
    3:"",
    4:"",
    5:"",
    6:"",
    7:"",
    8:"",
    9:"",
    10:""
}

commands = {
    1:"Add",
}

commadn_lenght = {
    1:"3",
}

Text_box = {
    1:"",
    2:"",
    3:""
}

list = os.listdir("./Todo's") # dir is your directory path
number_files = len(list)
rows, columns = os.popen('stty size', 'r').read().split()

# A function that prints text to a spot in the terminal
def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()

def load():
    for i in range(number_files):
        i = i + 1
        file = open("Todo's/" + str(i) + ".txt", "r")
        Todos[i] = file.read()
        file.close()

def print_line(rows,columns,ore,text):
    if ore == "h":
        print_there(rows,columns,text)
    elif ore == "v":
        for i in range(rows):
            print_there(i,columns,text)

def print_text(row,column,text):
    print_there(row,column,text)

def cycle_text(Text_box):
    Text_box[3] = Text_box[2]
    Text_box[2] = Text_box[1]
    Text_box[1] = " "

#Loads the discplay
def load_display(rows,columns):

    columns_half = int(columns)/2
    os.system("clear")

    for i in range(int(columns)):
        print(" ")

    print_line(1,1,"h","#"*int(columns))
    print_line(int(rows)-2,1,"h","#"*int(columns))
    print_line(12,2,"h","#"*int(columns))

    print_line(int(rows)-2,1,"v","#")
    print_line(int(rows)-2,columns_half,"v","#")
    print_line(int(rows)-2,int(columns),"v","#")

    for i in range(10):
        i = i + 1
        print_text(i + 1, 2,str(i) + ":" + Todos[i])
    
    cycle_text(Text_box)
    print_text(int(rows)-1,1,Text_box[2])

    #for i in range(int(rows)-13):
        #i = i + 1
        #print_text(int(rows)-2,2,Text_box[i])
while True:
    load()
    load_display(rows,columns)
    Command = input(":")

    if Command[:int(commadn_lenght[1])] == commands[1]:
        Text_box[1] = "Added"
