"""
Created on Fri Jun 11 12:22:37 2019

@author: Tushar Bana
"""


import math



def NA_mismatch_loss(): #To calculate the coupling loss between two fibres of different numerical apertures
    NA1 =input("Enter numerical aperture for fiber1 : ")
    NA2 =input("Enter numerical aperture for fiber2 : ")


    Loss = 20 * (math.log(NA1 / NA2) / math.log(10))  # NA mismatch coupling loss

    print "\nThe NA mismatch coupling loss = ", Loss, " dB\n\n"



def calc_scattering_loss(): #To calculate scattering loss in a fibre given Input and Output Power in W
    Pin = 5.31 * math.pow(10, -9) #Power from Source in W
    Pout = 98.45 * math.pow(10, -6) #Power at output in W
    L = input("Enter lenght in km : ")
    print "\nInput Power is set as :  ", Pin, ' W'
    print "Output Power is set as :  ", Pout, ' W'

    sc_loss = (4.343 * math.pow(10, 5) / L) * (Pin / Pout)  # scattering loss in the fiber in dB

    print "\n The scattering loss in the fiber = ", sc_loss, "dB/km\n\n"




def calc_crit_na_acc(): #To calculate Critical Angle, Numerical Aperture(NA) and Acceptance angle in an optical fibre
    n1 = input("Enter refractive index of core : ")
    n2 = input("Enter refractive index of clad : ")


    crit_angle = math.degrees(math.asin(n2 / n1))  # Critical Angle

    NA = math.sqrt(n1 ** 2 - n2 ** 2)  # Numerical Aperture

    acc_angle = math.degrees(math.asin(NA))  #Acceptance Angle

    print "\nCritical angle =  ", crit_angle, " degrees"
    print "Numerical Aperature =   ", NA
    print "Acceptance angle =  ", acc_angle, " degrees\n\n"


def max_transmission_distance(): #To calculate maximum transmission distance given Input Power, Output Power and Attenuation
    Pin = 1 * 10 ** -3   # Input power
    A = input("Enter Attenuation in dB/km :  ")
    Pout = 50 * 10 ** -6  # Output Power

    print "\nInput Power is set as :  ", Pin, ' W'
    print "Output Power is set as :  ", Pout, ' W'


    L = (10 / A) * math.log10(Pin / Pout)  #Max transmission distance

    print "\nMaximum transmission distance =  ", L, " km\n\n"


def calc_attenuation(): #To calculate attenuation and Rayleigh scattering coefficient for fiber
    n = input("Enter the refractive index of core : ")
    p = 0.286   # Average photoelastic coefficient
    B = 7.25 * 10 ** -11  # Isothermal compressibility
    k = 1.38 * 10 ** -23  # Boltzmann's constant
    T = 1350 #Fictive Temperature
    l = 1 * 10 ** -6  # Wavelength of light
    L = 10 ** 3  # Length

    print "\nAverage Photoelastic Coefficient(p) is set as : ", p
    print "Isothermal Compressibility (B) is set as : ", B
    print "Boltzmann's Constant : ", k
    print "Fictive Temperature of glass : ", T
    print "Wavelength is set as : ", l, ' m'
    print "Length of fiber is set as : ", L, ' km'


    y1 = 8 * (math.pi) ** 3 * (n) ** 8 * (p) ** 2 * B * k * T / (3 * (l) ** 4)  # Rayleigh scattering coefficient for length


    T1 = math.exp(-(y1 * L))  #Attenuation


    print"\nFirst Rayleigh scattering coefficient = ", y1

    print"Attenuation  = ", T1, " dB/km\n\n"


def calc_mode_param(): #To calculate mode of light transmission given refractive index of core, clad and core radius with wavelength of light
    n1 = input("Enter refractive index of core : ")
    n2 = input("Enter refractive index of clad : ")
    a = 4 * 10 ** -6  # core radius
    lamda = 1 * 10 ** -6  # light wavelength

    print "\nCore Radius is set as : ", a, ' m'
    print "Wavelength : ", lamda, ' m'


    V = (2 *math.pi * a * math.sqrt(n1 ** 2 - n2 ** 2)) / (lamda)

    if (V<2.4048):
        print "\nWavelength of light is longer than cutoff wavelength. \nLight will travel in Single-Mode as Mode parameter is = ", V, "\n\n"
    else:
        print "\nWavelength of light is less than cutoff wavelength.\n Light will travel in Multiple-Modes as Mode parameter is = ", V, "\n\n"



def calc_no_of_modes(): #To calculate no. of guided modes in a multi mode fiber (V>2.4048)
    lamda = 1.30*10**-6  # Wavelength
    a = 25*10**-6  #Core diameter of fiber
    delta = 0.01  #Relative refractive index
    n1 =input("Enter Refractive index of core : ")

    print "\nCore Diameter is set as : ", a, ' m'
    print "Wavelength : ", lamda, ' m'
    print "Relative Refractive Index is : ", delta

    v = (2 * math.pi * a * n1 / lamda)*((2 * delta)**(0.5))  # Normalized Frequency (Multi mode if V>2.4048)


    if (v>2.4048):
        m = v ** 2 / 2  #Number of guided modes



        print"\nNormalized frequency =   ", v
        print"Number of guided modes =   ", m, "\n\n"
    else:
        print "Single-Mode Fibre with Normalized Frequency = ", v, "\n\n"


def calc_core_radius(): #To calculate radius of core given normalized frequency, wavelength and refractive index
    lamda = 0.85 * 10 ** -6  # Wavelength
    delta = 0.015  # Relative refractive index
    n1 = input('Enter Refractive Index of Core : ')
    v = 2.403  # Normalized frequency for single mode fiber

    print "\nRelative Refractive Index is : ", delta
    print "Wavelength : ", lamda, ' m'
    print "Normalized frequency for Single-mode Fiber is : ", v



    a = v * lamda / (2 * math.pi * n1 * math.sqrt(2 * delta))  #Core radius using Formula of Normalized Frequency
    a = a * 10 ** 6

    print"\nRadius of core = ", a, " mm\n\n"


def calc_cutoff(): #To calculate cutoff wavelength given normalized frequency, refractive index and core radius
    V = 2.403  # Normalized frequency for single-mode fiber
    delta = 0.25  # Relative refractive index
    n1 = input("Enter refractive index of Core : ")
    a = 4.5 * 10 ** -6  # Radius of core

    print "\nCore Radius is set as : ", a, ' m'
    print "Relative Refractive Index is : ", delta
    print "Normalized frequency for Single-Mode Fiber is : ", V


    lamda = (2 * math.pi * a * n1 * (math.sqrt(2 * delta))) / V  #cutoff wavelength

    print"\nCut off wavelength =  ", lamda * 10 ** 8, " nm\n\n"


#To calculate Total insertion loss due to lateral offset and Angular Misalignment given normalized frequency,
#  refractive index, core radius, numerical aperture and lateral and angular misalignment in m
def calc_total_insertion_loss():
    V = 2.50  # normalised frequency
    n1 = input("Enter Refractive Index of Core : ")
    a = 4.5 * math.pow(10, -6)  # core radius in m
    NA = 0.2  # numerical aperture

    y = 3 * math.pow(10, -6)  # lateral misalignment in m
    w = a * ((0.65 + 1.62 * math.pow((V), -1.5) + 2.88 * math.pow((V), -6)) / math.pow(2,0.5))  # normalised spot size in m

    print "\nCore Radius is set as : ", a, ' m'
    print "Normalized Frequency is  : ", V
    print "Numerical Aperture is : ", NA
    print "Lateral Misalignment is set as : ", y, ' m'
    print "Normalised Spot Size is : ", w, ' m'

    T1 = 2.17 * math.pow((y / w), 2)  # Loss due to lateral offset in dB

    print "\nLoss due to lateral offset is : ", T1, ' dB'


    x = (math.pi / 180) * w #Angular Misalignment in radian

    print "\nAngular Misalignment is set as : ", x, ' radian'

    Ta = 2.17 * math.pow(((x * n1 * V) / (a * NA)), 2)  # loss due to angular misalignment in dB

    print "\nLoss due to angular Misalignment is : ", Ta, ' dB'

    T = T1 + Ta  # total insertion loss in dB

    print "\nAs Total Insertion loss is sum of Loss due to lateral misalignment(T1) and Loss due to Angular misalignment(Ta).\n" \
          " Hence, The total insertion loss  = ", T, " dB\n\n"



while True:
    n=raw_input(" <<<<<PRESS ENTER TO START THE PROGRAM>>>>> ")
    if n=="":
        print "1.Calculate Coupling Loss due to Numerical Aperture Mismatch\n2.Calculate Scattering Loss in a fiber with Input and Output Power\n3.Calculate Critical Angle, Numerical Aperture and Acceptance Angle" \
              "\n4.Calculate Maximum Transmission Distance of Fiber with given Attenuation\n5.Calculate Attenuation per km and Rayleigh Scattering Coefficient" \
              "\n6.Calculate Mode of Light Transmission in fiber given Light Wavelength\n7.Calculate Number of Guided Modes in Multi-Mode Fiber" \
              "\n8.Calculate Core radius\n9.Calculate Cutoff Wavelength for a fiber\n10.Calculate Total Insertion Loss due to Lateral and Angular misalignment of fibers\n "

        ch=str(raw_input("Select a Option  : "))

        if ch=='1':
            NA_mismatch_loss()
        elif ch=='2':
            calc_scattering_loss()
        elif ch=='3':
            calc_crit_na_acc()
        elif ch=='4':
            max_transmission_distance()
        elif ch=='5':
            calc_attenuation()
        elif ch=='6':
            calc_mode_param()
        elif ch=='7':
            calc_no_of_modes()
        elif ch=='8':
            calc_core_radius()
        elif ch=='9':
            calc_cutoff()
        elif ch=='10':

            calc_total_insertion_loss()
        else:
            print"\nIncorrect Option Selected !! \n Select Again ... \n"

