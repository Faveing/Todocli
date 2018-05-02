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
        print(i)
#Loads the discplay
def load_display(rows,columns):
    os.system("clear")
    print_there(1,1,"#"*int(columns))
    print_there(int(rows),1,"#"*int(columns))
    #prints the edges of the display
    for i in range(int(columns)):
        print_there(i,1,"#")
        print_there(i,int(columns),"#")

load()
load_display(rows,columns)
