# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 11:10:23 2019

@author: Tushar Bana
"""
import tkinter
import matplotlib

from g55correctionfactortrial import *
from plot_graphs import *


#Application Class
class simpleapp_tk(tkinter.Tk):
    temp=0      #To calculate number of time data set is added

    #Application Class initialization function
    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
        self.frame=tkinter.Frame(parent)

    #Initialize the GUI
    def initialize(self):
        self.grid()     #Using grid to manage widgets in Tkinter window
        self.configure(background='LightBlue')
        self.geometry("500x300+300+300")
        #Set the Labels
        self.labelVariable = tkinter.StringVar()
        label = tkinter.Label(self, textvariable=self.labelVariable,
                              anchor="w", fg="black",bg='LightBlue',font='Helvetica 11 bold italic')
        label.grid(column=0, row=0, columnspan=1,padx=(15,25),pady=(50,10), sticky='EW')
        self.labelVariable.set(u"Enter the Path of the file : ")

        self.labelVariable1 = tkinter.StringVar()
        label1 = tkinter.Label(self, textvariable=self.labelVariable1,
                              anchor="w", fg="black",bg='LightBlue',font='Helvetica 11 bold italic')
        label1.grid(column=0, row=1, columnspan=1,padx=(15,25),pady=(10,10), sticky='EW')
        self.labelVariable1.set(u"Enter the Temperature : ")

        self.labelVariable2 = tkinter.StringVar()
        label2 = tkinter.Label(self, textvariable=self.labelVariable2,
                              anchor="w", fg="black",bg='LightBlue',font='Helvetica 11 bold italic')
        label2.grid(column=0, row=2, columnspan=1,padx=(15,25),pady=(10,10), sticky='EW')
        self.labelVariable2.set(u"Enter the Tension : ")

        self.labelVariable3 = tkinter.StringVar()
        label3 = tkinter.Label(self, textvariable=self.labelVariable3,
                               anchor="w", fg="black",bg='LightBlue',font='Helvetica 11 bold italic')
        label3.grid(column=0, row=3, columnspan=1,padx=(15,25),pady=(10,10), sticky='EW')
        self.labelVariable3.set(u"Enter the Avg. ꝺv/ꝺz : ")


        #Set the Entry Variables
        self.entryVariable = tkinter.StringVar()
        self.entry = tkinter.Entry(self)
        self.entry.grid(column=1,row=0,columnspan=8,padx=(15,25),pady=(50,10),sticky='EW')
        self.entry.bind("<Return>", self.OnPressEnter)


        self.entry1 = tkinter.Entry(self)
        self.entry1.grid(column=1, row=1,columnspan=2,padx=(15,25),pady=(10,10), sticky='EW')
        self.entry1.bind("<Return>", self.OnPressEnter)

        self.entry2 = tkinter.Entry(self)
        self.entry2.grid(column=1, row=2,columnspan=2,padx=(15,25),pady=(10,10), sticky='EW')
        self.entry2.bind("<Return>", self.OnPressEnter)

        self.entry3 = tkinter.Entry(self)
        self.entry3.grid(column=1, row=3,columnspan=2,padx=(15,25),pady=(10,10), sticky='EW')
        self.entry3.bind("<Return>", self.OnPressEnter)


        #Define the buttons, their location on the grid and command to execute once clicked
        self.button = tkinter.Button(self, text=u"Open", fg='white',bg='#383a39', font='Helvetica 10 bold', command=self.OnButtonClick)
        self.button.grid(column=2, row=4, rowspan=2, padx=(15,25),pady=(50,10),sticky='SE')

        self.button1 = tkinter.Button(self, text=u"Add", fg='red', font='Helvetica 10 italic', command=self.OnAdd)
        self.button1.grid(column=1, row=4, rowspan=2, padx=(15,25),pady=(50,10),sticky='SW')

        self.button2 = tkinter.Button(self, text=u"Compare", command=self.OnCompare)
        self.button2['state']='disabled'
        self.button2.grid(column=0, row=4, rowspan=2, padx=(15,25),pady=(50,10),sticky='EW')


        #Some required functions of tkinter library to call for setting up gui window
        self.grid_columnconfigure(0,weight=1)
        self.resizable(True,False)
        self.update()
        self.geometry(self.geometry())       
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)


    #Function called when the "Open" button is clicked
    def OnButtonClick(self):
        Rmean,DR,stress,viscosity=self.calc_params()

        plots(Rmean,DR,stress,viscosity,self.entry1.get(),self.entry2.get())            #'plot_graphs.py' function

    #Function to call when "Enter" is pressed. It is same as "Open"
    def OnPressEnter(self, value):
        simpleapp_tk.OnButtonClick(self)

    #Function called when "Compare" Button is clicked
    def OnCompare(self):
        compare_plots(simpleapp_tk.temp)                #'plot_graphs.py' function

    # Function called when "Add" Button is clicked
    def OnAdd(self):
        if simpleapp_tk.temp<6:
            simpleapp_tk.temp+=1        # +1 the number of data sets added
            if simpleapp_tk.temp>=2:
                self.button2['state']='normal'
                self.button2['fg']='green'
                self.button2['font']='Helvetica 10 bold underline'
            Rmean,DR,stress,viscosity=self.calc_params()

            add_plot(Rmean,DR,stress,viscosity,self.entry1.get(),self.entry2.get())         #'plot_graphs.py' function
        else:
            tkinter.messagebox.showinfo("WARNING","Cannot compare more than 6 data sets !!")


    #Function is called when DR, Stress, Viscosity, Rmean and other required parameters are to be calculated using functions of 'g55correctionfactorial.py'
    def calc_params(self):
        self.entry.focus_set()
        self.entry.selection_range(0, tkinter.END)
        T = set_Temp(self.entry1.get())                         #'g55correctionfactorial.py' function
        data, CF = setPath(str(self.entry.get()), T)            #'g55correctionfactorial.py' function
        Rad = rad()                                             #'g55correctionfactorial.py' function
        tension, ftotal = Tension(self.entry2.get())            #'g55correctionfactorial.py' function
        global Rmean, DR
        viscosity, Area, Rmean = VAR(data, Rad)                             #'g55correctionfactorial.py' function
        Area_avg_vis = calc_area_avg_vis(self.entry3.get(), viscosity, Rmean)      #'g55correctionfactorial.py' function

        P1, DR_avg = calc_pressure(ftotal, Area_avg_vis)        #'g55correctionfactorial.py' function
        DR, stress = calc_DR_stress(viscosity, P1, DR_avg)      #'g55correctionfactorial.py' function

        print('\nDR : ', DR, '\nStress : ', stress, '\nViscosity : ', viscosity)
        return Rmean,DR,stress,viscosity


#Main Program
if __name__ == "__main__":
    app = simpleapp_tk(None)
    app.title('my application')
    app.mainloop()



