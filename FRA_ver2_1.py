
""" Plots to create and compare. baseline DDR  vs current results w.r.t component. select two files one for
 baseline and current analysis
  """
""" Plots to compare baseline vs current iteration
list of named selection from the workbench file in the kept in file listname2.txt"""


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

# this method can be used to import multiple files
#file = filedialog.askopenfilename(multiple=True)
#print(file)
#f1path = os.path.basename(file[0])
#f2path = os.path.basename(file[1])
#print(os.path.splitext(f1path)[0])
#print(f2path)

def graph2():
    try:

        # individual file opening method used here
        fpath = filedialog.askopenfilename(title='Select the xlsx file of current Iteration for N tone')
        print(fpath)
        df2 = pd.read_excel(fpath)
        df2 = df2[df2.filter(regex='^(?!Unnamed)').columns]
        print(df2)

        fpath2 = filedialog.askopenfilename(title='Select the xlsx file for comparison N tone')
        print(fpath2)
        df22 = pd.read_excel(fpath2)
        df22 = df22[df22.filter(regex='^(?!Unnamed)').columns]
        print(df22)


        #
        names= df2.columns
        print(df2.shape)
        print(names)

        df_freq = df2.filter(items=['Frequency [Hz]'])
        df_freq1 = df22.filter(items=['Frequency [Hz]'])

        print(df_freq)
        print(df_freq1)

        fff = df_freq['Frequency [Hz]'].tolist()
        fff22 = df_freq1['Frequency [Hz]'].tolist()

        print(fff)
        print(fff22)

        df3 = df2.filter(regex='(Amplitude)')
        df33 = df22.filter(regex='(Amplitude)')

        import csv
        slno=[]
        with open('C:/Users/Public/Documents/userlist2.txt', mode='r') as file:
            csvFile = csv.reader(file)
            for lines in csvFile:
                slno.append(lines)
                print(lines)

        #listname1=['9ppm_Dome IF(Ux)','9ppm_Dome IF(Uy)','9ppm_Dome IF(Uz)','9ppm_Dome OF(Ux)','9ppm_Dome OF(Uy)','9ppm_Dome OF(Uz)','9ppm_Pin OD(Ux)','9ppm_Pin OD(Uy)','9ppm_Pin OD(Uz)','9ppm_HS UPPER(Ux)','9ppm_HS UPPER(Uy)','9ppm_HS UPPER(Uz)','9ppm_HS LOWER(Ux)','9ppm_HS LOWER(Uy)','9ppm_HS LOWER(Uz)','9ppm_OL Exit(Ux)','9ppm_OL Exit(Uy)','9ppm_OL Exit(Uz)','9ppm_OL Probe hole(Ux)','9ppm_OL Probe hole(Uy)','9ppm_OL Probe hole(Uz)','9ppm_IL EXIT(Ux)','9ppm_IL EXIT(Uy)','9ppm_IL EXIT(Uz)','9ppm_IL HS_EXIT(Ux)','9ppm_IL HS_EXIT(Uy)','9ppm_IL HS_EXIT(Uz)','9ppm_DAMPER TIP(Ux)','9ppm_DAMPER TIP(Uy)','9ppm_DAMPER TIP(Uz)','9ppm_IP(Ux)','9ppm_IP(Uy)','9ppm_IP(Uz)','9ppm_HS(Ux)','9ppm_HS(Uy)','9ppm_HS(Uz)']
        #listname1=['Dome IF(Ux)','Dome IF(Uy)','Dome IF(Uz)','Dome OF(Ux)','Dome OF(Uy)','Dome OF(Uz)','Pin OD(Ux)','Pin OD(Uy)','Pin OD(Uz)','HS UPPER(Ux)','HS UPPER(Uy)','HS UPPER(Uz)','HS LOWER(Ux)','HS LOWER(Uy)','HS LOWER(Uz)','OL Exit(Ux)','OL Exit(Uy)','OL Exit(Uz)','OL Probe hole(Ux)','OL Probe hole(Uy)','OL Probe hole(Uz)','IL EXIT(Ux)','IL EXIT(Uy)','IL EXIT(Uz)','IL HS_EXIT(Ux)','IL HS_EXIT(Uy)','IL HS_EXIT(Uz)','DAMPER TIP(Ux)','DAMPER TIP(Uy)','DAMPER TIP(Uz)','FRA_IP(Ux)','FRA_IP(Uy)','FRA_IP(Uz)','FRA_HS(Ux)','FRA_HS(Uy)','FRA_HS(Uz)'
        #]
        #listname2=['DDR_Dome IF(Ux)','DDR_Dome IF(Uy)','DDR_Dome IF(Uz)','DDR_Dome OF(Ux)','DDR_Dome OF(Uy)','DDR_Dome OF(Uz)','DDR_Pin OD(Ux)','DDR_Pin OD(Uy)','DDR_Pin OD(Uz)','DDR_HS UPPER(Ux)','DDR_HS UPPER(Uy)','DDR_HS UPPER(Uz)','DDR_HS LOWER(Ux)','DDR_HS LOWER(Uy)','DDR_HS LOWER(Uz)','DDR_OL Exit(Ux)','DDR_OL Exit(Uy)','DDR_OL Exit(Uz)','DDR_OL Probe hole(Ux)','DDR_OL Probe hole(Uy)','DDR_OL Probe hole(Uz)','DDR_IL EXIT(Ux)','DDR_IL EXIT(Uy)','DDR_IL EXIT(Uz)','DDR_IL HS_EXIT(Ux)','DDR_IL HS_EXIT(Uy)','DDR_IL HS_EXIT(Uz)','DDR_DAMPER TIP(Ux)','DDR_DAMPER TIP(Uy)','DDR_DAMPER TIP(Uz)','DDR_FRA_IP(Ux)','DDR_FRA_IP(Uy)','DDR_FRA_IP(Uz)','DDR_FRA_HS(Ux)','DDR_FRA_HS(Uy)','DDR_FRA_HS(Uz)']
        df3.index=fff
        df33.index=fff22



        df3 = df3.set_axis(slno[0], axis='columns')
        df33 = df33.set_axis(slno[1], axis='columns')

        #df3.set_axis(fff, axis='rows', inplace=True)
        print(df3)
        print(df33)


        vertical_concat = pd.concat([df3, df33], axis=0)

        df3.to_excel('Excel_output.xlsx')
        vertical_concat.to_excel('concat_Excel_output.xlsx')

        #df3=vertical_concat
        #df_b =df3
        df4=df3
        df44=df33
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


        #df_b = df_b.drop(df_b.iloc[:, 0:3],  axis=1)
        #print(df_b)
        n=int(len(df3.columns)/3)
        print(n)

        Yaxis_limit= float(input("Yaxis_limit for the plot ( 0.1 upto 2) ="))
        print("you have entered the limit value of", Yaxis_limit ,"fine tune based on the full plot")


        for i in range(1,n+1):
            df_i = df3.iloc[:, 0: 3]
            dff_i = df33.iloc[:, 0: 3]
            #fig, ax = plt.subplots()
            ax = df_i.plot.line(ylim=(0, Yaxis_limit),color=['blue','red', 'green'])
            maxV = pd.DataFrame()
            maxV['Index'] = df_i.idxmax()
            maxV['Values'] = df_i.max()
            maxV2 = pd.DataFrame()
            maxV2['Index'] = dff_i.idxmax()
            maxV2['Values'] = dff_i.max()

            for ix, iy in zip(maxV['Index'], maxV['Values']):
                plt.text(ix, iy, '({})'.format(ix),fontsize="8")
            for ixx, iyy in zip(maxV2['Index'], maxV2['Values']):
                plt.text(ixx, iyy, '({})'.format(ixx),color='grey',fontsize="8")

            dff_i.plot.line(ax=ax,linestyle='dashed',color=['blue','red', 'green'])
            #ax.axhline(y = 4.5, xmin = 400, xmax = 650,color = 'w', linestyle = '--')
            ax.grid()
            #plt.hlines(0.4, 400, 500, color='red', linewidth=2.2)
            plt.xlabel('Frequency, Hz')
            plt.ylabel('Amplitude,mm')
            plt.title('Frequency response \n'+ os.path.splitext(os.path.basename(fpath))[0]+' vs '+ os.path.splitext(os.path.basename(fpath2))[0],wrap=True)
            plt.legend(ncol=1, fontsize="8", loc="best")
            plt.savefig('FRA' +str(i)+ '.jpg', dpi=300)
            df3 = df3.drop(df3.iloc[:, 0:3], axis=1)
            df33 = df33.drop(df33.iloc[:, 0:3], axis=1)
            plt.close()



        values =df3
        kwargs= dict (linestyle='dashed', color=['blue','red', 'green'],  linewidth=1.2)
        ##line_plot = revenue.plot( y = 'interviews', figsize= (10,6),**kwargs, marker='x' )
        ax= df4.plot.line(**kwargs )
        df44.plot.line(ax=ax,linestyle='solid',color=['blue','red', 'green'] )
        ax.grid()
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
#run=graph2()
#print("excecution completed")





