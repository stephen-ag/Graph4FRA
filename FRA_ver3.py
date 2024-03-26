"""THis code is usded for Frequency reponse analysis to extract the deformation response results (in X,Y,and Z for the named selections.
Extract the data from Ansys WB chart options as xlsx.These are the input for tool macro.
"""
""" Plots to compare N1,N2,N3 and N4 """


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

def graph4():
    try:

        # this method can be used to import multiple files
        file = filedialog.askopenfilename(multiple=True,title='Select the  four xlsx files of N1,N2,N3,N4 tone')
        print(file)
        #f1path = os.path.basename(file[0])
        #f2path = os.path.basename(file[1])
        fpath = file[0]
        fpath2 = file[1]
        fpath3 = file[2]
        fpath4 = file[3]

        #fpath = filedialog.askopenfilename(title='Select the xlsx file for N1')
        print(fpath)
        df2 = pd.read_excel(fpath)
        df2 = df2[df2.filter(regex='^(?!Unnamed)').columns]
        print(df2)

        #fpath2 = filedialog.askopenfilename(title='Select the xlsx file for N2')
        print(fpath2)
        df22 = pd.read_excel(fpath2)
        df22 = df22[df22.filter(regex='^(?!Unnamed)').columns]
        print(df22)

        #fpath3 = filedialog.askopenfilename(title='Select the xlsx file for N3')
        print(fpath3)
        df222 = pd.read_excel(fpath3)
        df222 = df222[df222.filter(regex='^(?!Unnamed)').columns]
        print(df222)

        #fpath4 = filedialog.askopenfilename(title='Select the xlsx file for N4')
        print(fpath3)
        df2222 = pd.read_excel(fpath4)
        df2222 = df2222[df2222.filter(regex='^(?!Unnamed)').columns]
        print(df2222)

        #
        names= df2.columns
        print(df2.shape)
        print(names)

        df_freq = df2.filter(items=['Frequency [Hz]'])
        df_freq1 = df22.filter(items=['Frequency [Hz]'])
        df_freq2 = df222.filter(items=['Frequency [Hz]'])
        df_freq3 = df2222.filter(items=['Frequency [Hz]'])
        print(df_freq)
        print(df_freq1)
        print(df_freq2)
        fff = df_freq['Frequency [Hz]'].tolist()
        fff22 = df_freq1['Frequency [Hz]'].tolist()
        fff220 = df_freq2['Frequency [Hz]'].tolist()
        fff230 = df_freq3['Frequency [Hz]'].tolist()
        print(fff)
        print(fff22)
        print(fff220)
        df3 = df2.filter(regex='(Amplitude)')
        df33 = df22.filter(regex='(Amplitude)')
        df330 = df222.filter(regex='(Amplitude)')
        df340 = df2222.filter(regex='(Amplitude)')

        import csv
        slno=[]
        with open('C:/Users/Public/Documents/userlist4.txt', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                slno.append(lines)
                print(lines)


        df3.index=fff
        df33.index=fff22
        df330.index=fff220
        df340.index=fff230

        df3.set_axis(slno[0], axis='columns', inplace=True,)
        df33.set_axis(slno[1], axis='columns', inplace=True,)
        df330.set_axis(slno[2], axis='columns', inplace=True,)
        df340.set_axis(slno[3], axis='columns', inplace=True,)
        #df3.set_axis(fff, axis='rows', inplace=True)
        print(df3)
        print(df33)
        print(df330)
        print(df340)

        vertical_concat = pd.concat([df3, df33,df330,df340], axis=0)

        df3.to_excel('Excel_output.xlsx')
        vertical_concat.to_excel('concat_Excel_output.xlsx')

        #df3=vertical_concat
        #df_b =df3
        df4=df3
        df44=df33
        df444=df330
        df4444=df340
        maxValues = df4.max()

        print(maxValues)
        maxValueIndex = maxValues.idxmax()
        mx=df4[[maxValueIndex]].idxmax()
        print(mx)
        #df_one =df3[['Dome IF(Ux)','Dome IF(Uy)','Dome IF(Uz)']] by column names.
        df_one = df3.iloc[ :, 0: 3] # by column ID's.
        print(df_one)
        print(df_one.shape)

        df_one1 = df33.iloc[ :, 0: 3] # by column ID's.
        print(df_one1)
        print(df_one1.shape)

        df_one2 = df330.iloc[ :, 0: 3] # by column ID's.
        print(df_one2)
        print(df_one2.shape)

        df_one3 = df340.iloc[ :, 0: 3] # by column ID's.
        print(df_one3)
        print(df_one3.shape)


        #df_b = df_b.drop(df_b.iloc[:, 0:3],  axis=1)
        #print(df_b)
        n=int(len(df3.columns)/3)
        print(n)

        Yaxis_limit= float(input("Yaxis_limit for the plot ( 0.1 upto 2) ="))
        print("you have entered the limit value of", Yaxis_limit ,"fine tune based on the full plot")

        for i in range(1,n+1):
            df_i = df3.iloc[:, 0: 3]
            dff_i = df33.iloc[:, 0: 3]
            dfdf_i = df330.iloc[:, 0: 3]
            dfdff_i = df340.iloc[:, 0: 3]
            comp=df_i.columns[2]
            comp1=comp[3:-4]
            #fig, ax = plt.subplots()
            ax = df_i.plot.line(ylim=(0, Yaxis_limit), color=['blue', 'red', 'green'])
            #ax = df_i.plot.line(color=['blue','red', 'green'])
            dff_i.plot.line(ax=ax,linestyle='dotted',color=['blue','red', 'green'])
            dfdf_i.plot.line(ax=ax, linestyle='solid', color=['blue', 'red', 'green'])
            dfdff_i.plot.line(ax=ax, linestyle='dotted', color=['blue', 'red', 'green'])
            x=[247,368,408,610,604,920,876,1208]
            y=Yaxis_limit-0.1
            x1 = [247,368]
            y1 = [y,y]
            x2 = [408,610]
            y2 = [y+0.05,y+0.05]
            x3 = [604,920]
            y3 = [y,y]
            x4 = [876,1208]
            y4 = [y+0.05,y+0.05]


           # plt.plot(x,y,marker='x')
            ax.plot(x1, y1,  marker='+',markersize = 8)
            ax.plot(x2, y2, marker='+', markersize=8)
            ax.plot(x3, y3, marker='+', markersize=8)
            ax.plot(x4, y4, marker='+', markersize=8)
            plt.text(x1[0]+10, y1[0], 'N1', color="grey",fontsize="10")
            plt.text(x2[0]+10, y2[0], 'N2', color="grey",fontsize="10")
            plt.text(x3[0]+10, y3[0], 'N3', color="grey",fontsize="10")
            plt.text(x4[0]+10, y4[0], 'N4', color="grey",fontsize="10")

            #ax.axhline(y = 4.5, xmin = 400, xmax = 650,color = 'w', linestyle = '--')
            ax.grid(which = "major", linewidth = 1)
            ax.grid(which = "minor",linestyle='dashdot', linewidth = 0.2)
            ax.minorticks_on()
            #plt.hlines(0.4, 400, 500, color='red', linewidth=2.2)
            plt.xlabel('Frequency, Hz')
            plt.ylabel('Amplitude,mm')

            plt.title(comp1 +' N1-N2-N3-N4 @10kPa 0-P,2%DR',wrap=True,fontsize="12")
            plt.legend(ncol=2, fontsize="6", loc="best")
            #plt.title('Frequency response'+ os.path.basename(fpath) )
            plt.savefig('FRA' +str(i)+ '.jpg', dpi=300)
            df3 = df3.drop(df3.iloc[:, 0:3], axis=1)
            df33 = df33.drop(df33.iloc[:, 0:3], axis=1)
            df330 = df330.drop(df330.iloc[:, 0:3], axis=1)
            df340 = df340.drop(df340.iloc[:, 0:3], axis=1)
            plt.close()



        values =df3
        kwargs= dict (linestyle='solid', color=['blue','red', 'green'],  linewidth=1.2)
        ##line_plot = revenue.plot( y = 'interviews', figsize= (10,6),**kwargs, marker='x' )
        ax= df4.plot.line(**kwargs )
        df44.plot.line(ax=ax,linestyle='dotted',color=['blue','red', 'green'] )
        df444.plot.line(ax=ax,linestyle='solid',color=['blue','red', 'green'] )
        df4444.plot.line(ax=ax,linestyle='dotted',color=['blue','red', 'green'] )
        ax.grid()
        #plt.hlines(0.4, 400, 500, color='red', linewidth=2.2)
        #plt.hlines(0.45, 450, 600, color='red', linewidth=2.2)
        #plt.axhline(y=0.25, linewidth=2.2, label= 'horizontal-line')
        plt.xlabel('Frequency, Hz')
        plt.ylabel('Amplitude,mm')
        plt.title('Frequency response')
        #plt.legend(ncol=6,fontsize="5",loc ="best")
        plt.legend(loc="best",ncol=3,fontsize="3")
        plt.savefig('New' + '.jpg', dpi=300)
        plt.show()
        plt.close()

        return()
    except Exception as e:
        return ('The Exception message is:\n ', e)
#run=graph4()
#print("excecution completed")
