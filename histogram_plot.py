import matplotlib.pyplot as plt
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

        with open(fileName, "r") as input:
            reader = csv.reader(input, delimiter = ";", )
            #next(reader, None)

            df = pd.DataFrame(reader)
            print(df.head())

            #x = open(fileName, "r")
            data = []

            for row in reader:
                data.append(int(row[histRow]))
            
           


            plt.hist(data)
            plt.show()
        clear()

    elif menuSelect == 0:
        sys.exit([0])


#("jpeg files","*.jpg"),("all files","*.*"))