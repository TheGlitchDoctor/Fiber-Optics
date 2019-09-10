"""
Created on Fri Jun 23 10:48:51 2019

@author: Tushar Bana
"""

import tkinter as tk
import matplotlib.pyplot as plt
from datetime import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from g55correctionfactortrial import *



global temp
temp=list()     #Variable that will store data sets temporarily

#Function to calculate Dynamic Viscosity(mPa) from Viscosity in Pa
def calc_dyn_vis(viscosity):
    dyn_vis=[x/1000000 for x in viscosity]
    return dyn_vis

#When 'Save' button is clicked for open graphs to save data to .csv file
def OnSaveClick(Rmean,X,label):
    write_data(Rmean,X,label)           #'g55correctionfactortrial.py' function
    tk.messagebox.showinfo("File Saved", "Data saved in file " + label + ' successfully!')


#Function called when 'Open' button is clicked on main window
def plots(Rmean,DR,Stress,Viscosity,T,Tension):
    app=tk.Tk()     #1st tkinter window
    app1=tk.Tk()    #2nd tkinter window
    app.wm_title('Graphs: Radius VS ꝺv/ꝺz    &&    Radius VS Viscosity')
    app1.wm_title('Graph: Radius VS Stress')
    for i in range(3):
        #plt.ion()
        fig=plt.figure(figsize=(6,4),dpi=96)        #define a figure using matplotlib.pyplot

        ax=fig.add_subplot(111)                     #add a subplot

        if i==0:            #For first : Radius VS ꝺv/ꝺz
            line,=ax.plot(Rmean,DR,'b-',label='Temp : '+str(T) + '\tTension : ' + str(Tension))
            ax.set_xlabel('Radius (micron)')
            ax.set_ylabel('dv/dz ')
            plt.legend(loc='best')

            graph = FigureCanvasTkAgg(fig, master=app)          #add figure to Tkinter window
            canvas = graph.get_tk_widget()
            canvas.grid(row=0, column=0, rowspan=11, padx=10, pady=5)       #define location of figure on tkinter window using canvas grid

            label = 'Rmean_DR'+str(datetime.now().strftime("%d_%m_%Y_at_%H_%M_%S"))+'.csv'          #Excel File name in which data will be stored on save
            button = tk.Button(app, text=u"Save", command=lambda : OnSaveClick(Rmean, DR, label))       #Save Button
            button.grid(column=0, row=14)

        elif i==1:          #For second : Radius VS Viscosity
            dyn_vis = calc_dyn_vis(Viscosity)

            line2,=ax.plot(Rmean,dyn_vis,'b-',label='Temp : '+str(T) + '\tTension : ' + str(Tension))
            ax.set_xlabel('Radius (microns)')
            ax.set_ylabel('Viscosity (mPa.s)')
            plt.legend(loc='best')

            graph = FigureCanvasTkAgg(fig, master=app)
            canvas = graph.get_tk_widget()
            canvas.grid(row=0, column=1, rowspan=11, padx=10, pady=5)

            label1 = 'Rmean_Viscosity'+str(datetime.now().strftime("%d_%m_%Y_at_%H_%M_%S"))+'.csv'
            button1 = tk.Button(app, text=u"Save", command=lambda : OnSaveClick(Rmean, Viscosity, label1))
            button1.grid(column=1, row=14)

        elif i==2:          #For Third : Radius VS Stress
            line3,=ax.plot(Rmean,Stress,'b-',label='Temp : '+str(T) + '\tTension : ' + str(Tension))

            ax.set_xlabel('Radius (micron)')
            ax.set_ylabel('Stress (mPa)')
            plt.legend(loc='best')


            graph = FigureCanvasTkAgg(fig, master=app1)
            canvas = graph.get_tk_widget()
            canvas.grid(row=0, column=0, rowspan=11, padx=10, pady=5)

            label2 = 'Rmean_Stress'+str(datetime.now().strftime("%d_%m_%Y_at_%H_%M_%S"))+'.csv'
            button2 = tk.Button(app1, text=u"Save", command=lambda : OnSaveClick(Rmean, Stress, label2))
            button2.grid(column=0, row=14)

        plt.close()     #Close the Pyplot Figure windows so that only tkinter windows are open now

    app.mainloop()      #Initialize first application window
    app1.mainloop()     #Initialize second application window


#Function to append data set to 'temp' variable when 'Add' Button is clicked
def add_plot(Rmean,DR,Stress,Viscosity,T,Tension):
    dyn_vis=calc_dyn_vis(Viscosity)
    temp.append([Rmean,DR,Stress,dyn_vis,T,Tension])
    tk.messagebox.showinfo('ADDED', "Data Set added successfully !!")


#Function to call when 'Compare' Button is clicked to compare between data sets that have been added to 'temp'
def compare_plots(N):
    if N==1:
        tk.messagebox.showinfo('NOTE', "Add Minimum 2 Data sets to compare !!")
    else:
        win_list=[]
        for i in range(3):
            app=subplots(i,N)
            win_list.append(app)

        while i<len(win_list):
            win_list[i].mainloop()


fig=['fig1','fig2','fig3']
#Function that will be called by Compare to add subplots in one figure as per number of data sets added
def subplots(i,N):

    if N == 2:      #N = Number of data sets added
        fig[i]= plt.figure()
        axs=fig[i].add_subplot(1,1,1)
        axs1=fig[i].add_subplot(1,1,1)
        axs.plot(temp[0][0],temp[0][i+1],'b-',label='Temp : '+str(temp[0][4]) + '\tTension : ' + str(temp[0][5]))
        axs1.plot(temp[1][0],temp[1][i+1],'r-',label='Temp : '+str(temp[1][4]) + '\tTension : ' + str(temp[1][5]))

    if N == 3:
        fig[i] = plt.figure()
        axs = fig[i].add_subplot(1, 1, 1)
        axs1 = fig[i].add_subplot(1, 1, 1)
        axs2=fig[i].add_subplot(1,1,1)
        axs.plot(temp[0][0], temp[0][i + 1], 'b-', label='Temp : '+str(temp[0][4]) + '\tTension : ' + str(temp[0][5]))
        axs1.plot(temp[1][0], temp[1][i + 1], 'r-', label='Temp : '+str(temp[1][4]) + '\tTension : ' + str(temp[1][5]))
        axs2.plot(temp[2][0],temp[2][i+1], 'g-', label='Temp : '+str(temp[2][4]) + '\tTension : ' + str(temp[2][5]))

    if N == 4:
        fig[i] = plt.figure()
        axs = fig[i].add_subplot(1, 1, 1)
        axs1 = fig[i].add_subplot(1, 1, 1)
        axs2 = fig[i].add_subplot(1, 1, 1)
        axs3=fig[i].add_subplot(1,1,1)
        axs.plot(temp[0][0], temp[0][i + 1], 'b-', label='Temp : '+str(temp[0][4]) + '\tTension : ' + str(temp[0][5]))
        axs1.plot(temp[1][0], temp[1][i + 1], 'r-', label='Temp : '+str(temp[1][4]) + '\tTension : ' + str(temp[1][5]))
        axs2.plot(temp[2][0], temp[2][i + 1], 'g-', label='Temp : '+str(temp[2][4]) + '\tTension : ' + str(temp[2][5]))
        axs3.plot(temp[3][0],temp[3][i+1], 'k-',label='Temp : '+str(temp[3][4]) + '\tTension : ' + str(temp[3][5]))

    if N==5:
        fig[i] = plt.figure()
        axs = fig[i].add_subplot(1, 1, 1)
        axs1 = fig[i].add_subplot(1, 1, 1)
        axs2 = fig[i].add_subplot(1, 1, 1)
        axs3 = fig[i].add_subplot(1, 1, 1)
        axs4=fig[i].add_subplot(1,1,1)
        axs.plot(temp[0][0], temp[0][i + 1], 'b-', label='Temp : ' + str(temp[0][4]) + '\tTension : ' + str(temp[0][5]))
        axs1.plot(temp[1][0], temp[1][i + 1], 'r-',label='Temp : ' + str(temp[1][4]) + '\tTension : ' + str(temp[1][5]))
        axs2.plot(temp[2][0], temp[2][i + 1], 'g-',label='Temp : ' + str(temp[2][4]) + '\tTension : ' + str(temp[2][5]))
        axs3.plot(temp[3][0], temp[3][i + 1], 'k-',label='Temp : ' + str(temp[3][4]) + '\tTension : ' + str(temp[3][5]))
        axs4.plot(temp[4][0], temp[4][i + 1], 'y-',label='Temp : ' + str(temp[4][4]) + '\tTension : ' + str(temp[4][5]))

    if N==6:
        fig[i] = plt.figure()
        axs = fig[i].add_subplot(1, 1, 1)
        axs1 = fig[i].add_subplot(1, 1, 1)
        axs2 = fig[i].add_subplot(1, 1, 1)
        axs3 = fig[i].add_subplot(1, 1, 1)
        axs4 = fig[i].add_subplot(1, 1, 1)
        axs5=fig[i].add_subplot(1,1,1)
        axs.plot(temp[0][0], temp[0][i + 1], 'b-', label='Temp : ' + str(temp[0][4]) + '\tTension : ' + str(temp[0][5]))
        axs1.plot(temp[1][0], temp[1][i + 1], 'r-',
                  label='Temp : ' + str(temp[1][4]) + '\tTension : ' + str(temp[1][5]))
        axs2.plot(temp[2][0], temp[2][i + 1], 'g-',
                  label='Temp : ' + str(temp[2][4]) + '\tTension : ' + str(temp[2][5]))
        axs3.plot(temp[3][0], temp[3][i + 1], 'k-',
                  label='Temp : ' + str(temp[3][4]) + '\tTension : ' + str(temp[3][5]))
        axs4.plot(temp[4][0], temp[4][i + 1], 'y-',
                  label='Temp : ' + str(temp[4][4]) + '\tTension : ' + str(temp[4][5]))
        axs5.plot(temp[5][0],temp[5][i+1], 'm-', label='Temp : ' + str(temp[5][4]) + '\tTension : ' + str(temp[5][5]))

    elif N > 6:         #If more than 6 Data sets
        tk.messagebox.showinfo('WARNING', "Cannot compare more than 6 data sets !!")

    fig[i].set_size_inches(15, 8, forward=True)         #Increase size of the figure as per monitor window size

    if i==0:        #For Radius vs ꝺv/ꝺz figure
        app = tk.Tk()
        app.wm_title('Radius vs ꝺv/ꝺz')

        plt.legend(loc='best')
        axs.set_xlabel('Radius (microns)')
        axs.set_ylabel('dv/dz')
        graph = FigureCanvasTkAgg(fig[i], master=app)
        canvas = graph.get_tk_widget()
        canvas.grid(row=0, column=0, rowspan=20,columnspan=20, padx=10, pady=5)

        label='Radius_DR_compare_'+str(datetime.now().strftime("%d_%m_%Y_at_%H_%M_%S"))+'.png'          #Image label name to save the compared image
        button = tk.Button(app, text=u"Save Image", command=lambda: OnSaveImage(fig[i],label))          #'Save Image' Button
        button.grid(column=0, row=14)
        plt.close()             #Close the pyplot open figure windows
        return app
    elif i==1:      #For Radius vs Stress
        app1 = tk.Tk()
        app1.wm_title('Radius vs Stress')

        plt.legend(loc='best')
        axs.set_xlabel('Radius (microns')
        axs.set_ylabel('Stress (mPa)')

        graph = FigureCanvasTkAgg(fig[i], master=app1)
        canvas = graph.get_tk_widget()
        canvas.grid(row=0, column=0, rowspan=11, padx=10, pady=5)

        label = 'Radius_Stress_compare_' + str(datetime.now().strftime("%d_%m_%Y_at_%H_%M_%S"))+'.png'
        button = tk.Button(app1, text=u"Save Image", command=lambda: OnSaveImage(fig[i],label))
        button.grid(column=0, row=14)
        plt.close()
        return app1
    elif i==2:      #For Radius vs Viscosity
        app2 = tk.Tk()
        app2.wm_title('Radius vs Viscosity')

        plt.legend(loc='best')
        axs.set_xlabel('Radius (microns)')
        axs.set_ylabel('Viscosity (mPa.s)')

        graph = FigureCanvasTkAgg(fig[i], master=app2)
        canvas = graph.get_tk_widget()
        canvas.grid(row=0, column=0, rowspan=11, padx=10, pady=5)

        label = 'Radius_Viscosity_compare_' + str(datetime.now().strftime("%d_%m_%Y_at_%H_%M_%S"))+'.png'
        button = tk.Button(app2, text=u"Save Image", command=lambda: OnSaveImage(fig[i],label))
        button.grid(column=0, row=14)

        plt.close()
        return app2
#Function to call if 'Save Image' Button is clicked
def OnSaveImage(fig,label):
    fig.savefig(label,dpi=100)