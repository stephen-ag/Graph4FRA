""" THis macro is to extract frequency response displacement values and plot the graphs
In ansys WB create named sections based on region of interest
extract the deformation ux,uy,uz results for the above named selections in WB and using chart option
export it to excel file and rename the file with extension .xlsx
the input file for this macro is userlist1.txt file which has the component names created in ansys workbench
"""
""" Plots to create for each results eg N1 or N2 independently w.r.t component. run it for N1,N2,N3 and N4 separately
list of named selection from the workbench file in the kept in file listname1.txt"""


import glob
import os
import xlsxwriter
import openpyxl
import pandas as pd
from tkinter import filedialog
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure
from openpyxl import load_workbook
from pandas import read_excel

import csv

def graph1():

    try:

        fpath = filedialog.askopenfilename(title='Select the xlsx file for N1')
        print(fpath)
        df2 = pd.read_excel(fpath)
        df2 = df2[df2.filter(regex='^(?!Unnamed)').columns]
        print(df2)

        #
        names= df2.columns
        print(df2.shape)
        #print(names)

        df_freq= df2.filter(items=['Frequency [Hz]'])
        print(df_freq)
        fff=df_freq['Frequency [Hz]'].tolist()
        print(fff)
        df3 = df2.filter(regex='(Amplitude)')
        slno=[]
        with open('C:/Users/Public/Documents/userlist1.txt', mode='r') as file:

            csvFile = csv.reader(file)
            for lines in csvFile:
                slno.append(lines)
                print(lines)

        #listname1=['Dome IF(Ux)','Dome IF(Uy)','Dome IF(Uz)','Dome OF(Ux)','Dome OF(Uy)','Dome OF(Uz)','Pin OD(Ux)','Pin OD(Uy)','Pin OD(Uz)','HS UPPER(Ux)','HS UPPER(Uy)','HS UPPER(Uz)','HS LOWER(Ux)','HS LOWER(Uy)','HS LOWER(Uz)','OL Exit(Ux)','OL Exit(Uy)','OL Exit(Uz)','OL Probe hole(Ux)','OL Probe hole(Uy)','OL Probe hole(Uz)','IL EXIT(Ux)','IL EXIT(Uy)','IL EXIT(Uz)','IL HS_EXIT(Ux)','IL HS_EXIT(Uy)','IL HS_EXIT(Uz)','DAMPER TIP(Ux)','DAMPER TIP(Uy)','DAMPER TIP(Uz)','FRA_IP(Ux)','FRA_IP(Uy)','FRA_IP(Uz)','FRA_HS(Ux)','FRA_HS(Uy)','FRA_HS(Uz)'
        #]
        #listname1=['Dome IF(Ux)','Dome IF(Uy)','Dome IF(Uz)','Dome OF(Ux)','Dome OF(Uy)','Dome OF(Uz)','Pin OD(Ux)','Pin OD(Uy)','Pin OD(Uz)','HS UPPER(Ux)','HS UPPER(Uy)','HS UPPER(Uz)','HS LOWER(Ux)','HS LOWER(Uy)','HS LOWER(Uz)','OL Exit(Ux)','OL Exit(Uy)','OL Exit(Uz)','OL Probe hole(Ux)','OL Probe hole(Uy)','OL Probe hole(Uz)','IL EXIT(Ux)','IL EXIT(Uy)','IL EXIT(Uz)','IL HS_EXIT(Ux)','IL HS_EXIT(Uy)','IL HS_EXIT(Uz)','DAMPER TIP(Ux)','DAMPER TIP(Uy)','DAMPER TIP(Uz)','FRA_IP(Ux)','FRA_IP(Uy)','FRA_IP(Uz)','FRA_HS(Ux)','FRA_HS(Uy)','FRA_HS(Uz)'
        #]
        print(slno[0])
        df3.index=fff

        df3 = df3.set_axis(slno[0], axis='columns')
        #df3.set_axis(fff, axis='rows', inplace=True)
        print(df3)

        df3.to_excel('Excel_output.xlsx')
        print(df3.columns)

        df_b =df3
        df4 = df3
        maxValues = pd.DataFrame()
        maxValues['Index'] = df4.idxmax()
        maxValues['Values'] = df4.max()
        maxV = df4.max()
        print(maxV)
        print(maxValues)
        print(maxValues.shape)

        maxValueIndex = maxV.idxmax()
        print(maxValueIndex)

        maxValues.to_excel( 'Max_values.xlsx')
        #mx= pd.Series(maxValues)
        #maxValueIndex = maxValues.idxmax()
        #mx=df4[[maxValueIndex]].idxmax()
        #print(mx)
        #df_one =df3[['Dome IF(Ux)','Dome IF(Uy)','Dome IF(Uz)']] by column names.
        df_one = df3.iloc[ :, 0: 3] # by column ID's.
        print(df_one)
        print(df_one.shape)


        df_b = df_b.drop(df_b.iloc[:, 0:3],  axis=1)
        print(df_b)
        n=int(len(df3.columns)/3)
        print(n)

        #Yaxis_limit = float(inputValue)
        Yaxis_limit= float(input("Yaxis_limit for the plot ( 0.1 upto 2) ="))
        print("you have entered the limit value of", Yaxis_limit ,"fine tune based on the full plot")


        for i in range(1,n+1):
            df_i = df3.iloc[:, 0: 3]
            comp=df_i.columns[2]
            #print(comp)
            comp1=str(comp[0:-4])
            print(comp1)
            #fig, ax = plt.subplots()
            #kwargs = dict(linestyle='solid', color=['blue', 'red', 'green'], linewidth=1.2)
            ax = df_i.plot.line(color=['blue', 'red', 'green'],ylim=(0, Yaxis_limit)) # limit of y axis set to 0.5 using ylim=(0, 0.14))
            #plt.text( comp1, fontsize=10)
            maxV = pd.DataFrame()
            maxV['Index'] = df_i.idxmax()
            maxV['Values'] = df_i.max()

            for ix, iy in zip(maxV['Index'], maxV['Values']):
                plt.text(ix, iy, '({})'.format(ix))
           # plt.text(ix, iy, comp1, fontsize=10)
            #ax.axhline(y = 4.5, xmin = 400, xmax = 650,color = 'w', linestyle = '--')
            ax.grid()
            #plt.hlines(0.4, 400, 500, color='red', linewidth=2.2)
            plt.xlabel('Frequency, Hz')
            plt.ylabel('Amplitude,mm')
            plt.title('Frequency response \n'+ os.path.splitext(os.path.basename(fpath))[0])
            plt.savefig('FRA' +str(i)+ '.jpg', dpi=300)
            df3 = df3.drop(df3.iloc[:, 0:3], axis=1)
            plt.close()

        values =df3
        kwargs= dict (linestyle='solid', color=['blue', 'crimson','green'],  linewidth=1.2)
        #kwargs2= dict (linestyle='solid', color=['blue', 'crimson','green'],  linewidth=1.2)
        ##line_plot = revenue.plot( y = 'interviews', figsize= (10,6),**kwargs, marker='x' )
        ax= df4.plot.line(**kwargs )
        #ax= df4.iloc[:,2:6].plot.line(**kwargs2 )
        ax.plot(maxValues['Index'],maxValues['Values'],color ='black',marker='+',linestyle='None')

        ax.grid()
        for i_x, i_y in zip(maxValues['Index'],maxValues['Values']):
            plt.text(i_x, i_y, '({})'.format(i_x))


        #plt.hlines(0.4, 400, 500, color='red', linewidth=2.2)
        #plt.hlines(0.45, 450, 600, color='red', linewidth=2.2)
        #plt.axhline(y=0.25, linewidth=2.2, label= 'horizontal-line')
        plt.xlabel('Frequency, Hz')
        plt.ylabel('Amplitude,mm')
        plt.title('Frequency response \n'+ os.path.splitext(os.path.basename(fpath))[0])
        plt.legend(ncol=3,fontsize="5",loc ="best")
        plt.savefig('New' + '.jpg', dpi=300)
        plt.show()
        plt.close()
        return()
    except Exception as e:
        return ('The Exception message is:\n ', e)
#run=graph1()
#print("excecution completed")




