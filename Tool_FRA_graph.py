from tkinter import filedialog
from PIL import ImageTk,Image
import os
from tkinter import *
from tkinter import ttk
import fileinput
import pandas as pd
from tkinter.filedialog import  askopenfile
import csv
import tkinter.messagebox
from FRA_ver1_1 import graph1
from FRA_ver2_1 import graph2
from FRA_ver22 import graph3
from FRA_ver3 import graph4
#import xlrd
import shutil

root = Tk()
root.geometry("1600x1600+20+40")
root['bg']='lightgrey'
root['bd']= 3
# image resizing


#img = ImageTk.PhotoImage(file ="fatigue1.png")


#panel = Label(root,  height = 400, width = 300)
#panel.place(x=1000, y=250)
#oldlace'azure'
root.title('FRA displacement plot Tool v1.0 ')
Label(root,text = "FRA Displacement Response GRAPH Creation ", bg="DarkCyan",height ="2",\
      width = "800", fg ="white",
      font = ("Calibri",40)).pack()
Label(root,text = "Note: This tool is specific to project requirement, read the requirement\
  of this tool for process and input data. Files with binary excel format not supported",
      height ="3",
      width = "400",
      font = ("Calibri",12)).pack()
print("entering post processing module")

textBox=Text(root, height=6, width=90)
textBox.pack(side=TOP)
Fact = """Requirements :
> Excel file .xlsx with displacement amplitude and phase angle exported from ANSYS WB for various load cases.
> listfile1.txt kept in a public Document folder containing the names of ANSYS WB named selection for various load cases.
> response Graph .jpg files for all the components requested will be created in a folder. """

textBox.insert(END, Fact)
textBox.tag_configure("right", justify='center')

#e=Entry(root, width =100, font=('Arial 14'),borderwidth = 5)

#e.place(x = 400, y = 240, width=380, height=100)

#e.pack(padx=10, pady=10)
#e.insert(0,'Enter the data:')
#fpath = e.get()
print("getting path from string")
#print(fpath)

def retrieve_input():
    global inputValue
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
textBox=Text(root, height=2, width=10)
textBox.pack()
buttonCommit=Button(root, height=1, width=10, text="Commit",
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

def getFolderPath():
    global folder
    folder = filedialog.askdirectory()
    print(folder)

def plot1():
    group1=graph1()

def plot2():
    group1=graph2()
def plot3():
    group1=graph3()
def plot4():
    group1=graph4()

def submit1():
    global HTC,Tbulk,pressure
    currdir = os.getcwd()
    filepath = filedialog.askopenfile(parent=root, initialdir=currdir, title='Please select a directory')
    filepath1=filepath.name
    print(filepath.name)

    #filepath = ('Static\working_data.xlsx')
    # data1 = pd.read_excel(file)

    # data1 = pd.read_excel(filepath1,sheet_name='Temp vs Time', skiprows = 3)
    # temp_data= pd.read_excel(filepath1,sheet_name='Temperature difference', skiprows = 1)
    df = pd.read_excel(filepath1, index_col=None)
    #print(pressure_data)
    df = df[df.filter(regex='^(?!Unnamed)').columns]
    df = df.iloc[:, 2:]
    print(df)
    datalist=df.columns.tolist()
    print(datalist)

    df1=df.iloc[0:1]
    HTC=df1.values.tolist()[0]
    df2 = df.iloc[1:2]
    Tbulk = df2.values.tolist()[0]
    df3 = df.iloc[2:3]
    Pressure = df3.values.tolist()[0]
    print (HTC)
    print(Tbulk)
    print(Pressure)

    # Remove the 1st row with units from the table
    #pressure_data = pressure_data.drop(pressure_data.index[[0]])
    #data1 = pressure_data
#def execute():
#    global HTC, Tbulk, pressure
    global my_label1
    global fpath
    #fpath=e.get()
    #print(fpath)
    #path ='C:\\Users\\arpuste\\HTC_TBULK_OCT.py'
    path = folder + '/HTC_TBULK_OCT.py'
    file1 = open(path, 'r', encoding='utf-8')
    Lines = file1.readlines()
    print(Lines)

    #liness = []
    #line = input("enter the tiles")
    #if line:
     #   liness.append(line)
    #else:
     #   null
    #text = '\n'.join(liness)


    #data = input('enter the Data name list \n')
    #data1 = input('enter the HTC \n')
    #data2 = input('enter the Tbulk \n')

    #print(Lines)
    Lines[15]='datalist='+str(datalist) +'\n'
    #Lines[14]=data1 +'\n'
    Lines[17]= 'HTC='+str(HTC)+'\n'
    Lines[19] = 'Tbulk='+str(Tbulk)+'\n'
    Lines[21] = 'Pressure='+str(Pressure) + '\n'
    # Strips the newline character
    mylines = []

    for myline in Lines:
        mylines.append(myline.rstrip('\n'))
        cnt= len(mylines)
    print ("TOTAL NUMBER OF LINES",cnt)
    #print(mylines)

    lbl1 = []
    for myline in mylines:
        if 'analysis = model.Analyses[1]' in myline:
            lbl1.append(mylines.index(myline))
    cnt2=len(lbl1)
    print(lbl1)

    with open('script.py', 'w', encoding='utf-8') as file:
        file.writelines(Lines)
    tkinter.messagebox.showinfo("scrip file", " script.py File created ")

    Lines[lbl1[0]]='analysis = model.Analyses[0]'+ '\n'
    for i in range(40,49,1):
        Lines[i]=''
    with open('script_pr.py', 'w', encoding='utf-8') as file:
        file.writelines(Lines)
def close():
    root.destroy()
def execute():
    pass
print("entering button controls")
#---------------------------------

button1 = Button(root,text = "Plot Displacement Graph", height ="2", width = "25",\
                 font = ("Calibri",13),bg="teal",fg ="white", command = plot1)
button1.place(x = 60, y = 240)

#---------------------------------
button2 = Button(root,text = " Compare 2 Displacement Graph", height ="2", width = "25",\
                 font = ("Calibri",13),bg="teal",fg ="white", command = plot2)
button2.place(x = 60, y = 340)
#---------------------------------
#---------------------------------
button3 = Button(root,text = " Compare 3 Displacement Graph", height ="2", width = "25",\
                 font = ("Calibri",13),bg="teal",fg ="white", command = plot3)
button3.place(x = 60, y = 440)
#---------------------------------

#---------------------------------
button4 = Button(root,text = " Plot N1-N2-N3-N4 Graph", height ="2", width = "25",\
                 font = ("Calibri",13),bg="teal",fg ="white", command = plot4)
button4.place(x = 60, y = 540)
#---------------------------------
#---------------------------------
#---------------------------------
#button2 = Button(root,text = "  execute ",height ="2", width = "25",\
#                 font = ("Calibri",13),bg="teal",fg ="white", command =execute)
#button2.place(x = 60, y = 307)
#--------------------------------
#---------------------------------
button6 = Button(root,text = " Close ",height ="2", width = "25",\
                 font = ("Calibri",13),bg="teal",fg ="white", command = close)
button6.place(x = 60, y = 640)
#--------------------------------

print("completed button controls")
root.state("zoomed")
root.mainloop()