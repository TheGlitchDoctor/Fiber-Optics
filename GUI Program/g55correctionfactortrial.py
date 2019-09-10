# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 17:33:48 2019

@author: Ranjith.Balakrishnan
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:18:15 2019

@author: Ranjith.Balakrishnan
"""

import math as m
import csv

#Defining some required constants
RI_Sil=1.444
W1=0
dr=0.15292 #radius intervel in excel sheet
OR=60 #outer radius of fiber
n=250 #Number of division of fiber for analysis

global Y_final_list
Y_final_list = []
global Y_final_list1
Y_final_list1 = []


#Function to set temperature from the given input
def set_Temp(str):
    if int(str):
        T=int(str)
    else:
        print("Enter Temperature in numbers!")
    return T


#Function to set path of the data file from the given input
def setPath(s, T):
    d_file=str(s)
#Importing data from txt file
    f = open(d_file, 'r')
    f1 = []
    flag = 0
    for x in f:
        if flag == 0:
            if "0\t" in x:
                f1.append(x)
                flag = 1
        elif flag == 1:
            if "End" in x:
                break
            else:
                f1.append(x)
    data = list()
    for i in f1:
        i.strip('\t\n')
        temp = i.split("\t")
        temp = [float(temp[0]), float(temp[1])]
        data.append(temp)

    #Finding zero correction factor
    cflist=[]
    for x in range(len(data)):
        if data[x][0]>20:
         cflist.append(data[x][1])
         CF= -1*min(cflist)

    # Creating 3rd column list of required dele and weight average
    for x in range(len(data)):
        if data[x][0] <= len(data):
            data[x].append(germ_region_delperccalc(data[x][0], data[x][1], CF, T))

    cflist = []
    for x in range(len(data)):
        if data[x][0] > 10:
            cflist.append(data[x][1])
            CF = max(cflist)

    return data, CF


#Germanium del% calculation function
def germ_region_delperccalc(r,del_e,CF,T):
    
    global Y_final_list1
#    if r<=13.97:
    LVSil = (-6.7401 + (4.904 * W1) - (0.70732 * W1 * W1)) + ((28437 - (10681 * W1) + (1600.4 * W1 * W1)) / (273 + T))
    del_zero_coin = del_e+CF
    RI_glass = del_zero_coin + RI_Sil
    del_perc =(RI_glass**2-RI_Sil**2)/(2*RI_glass**2) 
    if RI_glass>1.444000: #Germanium region
     LVGerm = LVSil+(m.log(m.exp(-0.5*(del_perc*100)))/m.log(10))
     V=(10**LVGerm)
     return(V)
    else:  #Chlorine region
     W3=(del_perc*100)/(0.08)
     W2=W3/3
     LVFlu =(-6.7401+(4.904*W2)-(0.70732*W2*W2))+((28437-(10681*W2)+(1600.4*W2*W2))/(273+T))
     Vis=10**LVFlu
     return(Vis)



#Equal Radius seperation list function
def rad():
    Rad=[]
    R=0
    for x in range (120):
        R=R+0.5
        Rad.append(R)
    return Rad
#

#Based on above equal radius and constants we calculate the following : (del avg, Area, Rmean for each rad section)
def VAR(data,Rad):
    i = 0
    j = 0
    viscosity = []
    Area = []
    Rmean = []
    for p in range(len(Rad)):
        vis_avg = 0
        A=0
        R1=0
        while (data[i][0]<=Rad[p]):
            i=i+1

        for z in range(j,i):
            vis_avg= vis_avg + (0.5/(data[i][0]**2-data[j][0]**2))*(data[z][0]+data[z+1][0])*(data[z][2]+data[z+1][2])*dr
            A=(m.pi*(data[i][0]**2-data[j][0]**2))
            R1=(data[i][0]+data[j][0])/2
        viscosity.append(vis_avg)
        Area.append(A)
        Rmean.append(R1)
        i=i
        j=i
    return viscosity,Area,Rmean
#
##Using delavg of each section viscosity profile is made and stored in Rmean
#vis=[]
#LVSil =m.log((m.exp(515400/(8.314*(T+273))))*(5.8*10**-7))/m.log(10)
#for i in range(len(Rad)):
#    LVGerm = LVSil+(m.log(m.exp(-0.5*(del_a[i]*100)))/m.log(10))
#    V1=10**LVGerm
#    vis.append(V1)
#print("Viscosity of entire regions"+str(vis))
#

#
#

#Function to set the Tension from the given input and Ftotal calculation
def Tension(str):
    if int(str):
        Tension=int(str)
    else:
        print("Enter Tension in numbers!")
    Ftotal=(Tension*9.81)/1000
    return Tension, Ftotal
#

#Function to calculate Area_avg_viscosity
def calc_area_avg_vis(s,viscosity,Rmean):
    if int(s):
        #avg viscosity value 18
        for i in range(len(Rmean)):
            if int(Rmean[i])==int(s):
                y=i
                print(Rmean[i])
                break
        #Area_avg_vis= viscosity[18]
        Area_avg_vis=viscosity[int(y)]

    else:
        print('Enter number only!')

    return Area_avg_vis


#Function to calculate Pressure
def calc_pressure(Ftotal,Area_avg_vis):
#overall pressure
    P1= Ftotal/(m.pi*((60*10**-6)**2))

#Average deformation ratio
    DR_avg=P1/(3*Area_avg_vis*0.1)
    return P1, DR_avg


#Function to calculate DR and Stress
def calc_DR_stress(viscosity,P1,DR_avg):
    #Individual DR ratio
    DR=[]
    for t in range(len(viscosity)):
        D=P1/(3*viscosity[t]*0.1)
        DR.append(D)
    #stress
    stress=[]
    for i in range (len(DR)):
        s=(3*viscosity[i]*0.1*(DR_avg-DR[i]))/10**6
        stress.append(s)

    return DR, stress


#def plot_graph(Rmean,DR):
#    import matplotlib.pyplot as plt
#    plt.plot(Rmean,DR)
#    plt.xlabel('Radius')
#    plt.ylabel('stress(Mpa)')
#    plt.title('Residualstressplot')


    #plt.axis([0, 60,-35,10 ])



#Function to write calculated data in excel(.csv) file
def write_data(Rmean,X,label):
    Resultwithcl2 = []
    for i in range(len(X)):
        Resultwithcl2.append([Rmean[i],X[i]])

    myFile = open(label, 'w',newline= '')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(Resultwithcl2)
#    
#            
