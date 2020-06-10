#import matplotlib.pyplot as plt
import csv
from tkinter import filedialog
from tkinter import *
import os, sys
import pandas as pd

clear = lambda: os.system('cls')
clear()

while True:
    menuSelect = int(input("MAIN MENU\n\n1. View Histogram\n0. Exit\n"))
    histRow = 0

    if menuSelect == 1:
        histRow = int(input("\nIn which column is your data?\n"))

        root = Tk()
        fileName =  filedialog.askopenfilename(initialdir = "/",title = "Select file")

        data = pd.read_excel(fileName, skiprows = 0)
        

        df = pd.DataFrame(data)
        print(df.head())

        #x = open(fileName, "r")
        #dataList = []
        #next(data, None)
        #for row in data:
        #    dataList.append(int(row[histRow]))
            
           

        #df.hist(column = 0)
            #plt.hist(data)
            #plt.show()
        clear()

    elif menuSelect == 0:
        sys.exit([0])


#("jpeg files","*.jpg"),("all files","*.*"))
