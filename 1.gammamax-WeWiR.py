import sys
import math
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import csv
import pandas as pd
import operator
#from matplotlib.ticker import FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from scipy.interpolate import make_interp_spline, BSpline
matplotlib.rc('text', usetex = True)
from scipy.optimize import curve_fit
from scipy import optimize
######################################################################################
######################################################################################
######################################################################################

a1=[]
b1=[]
a1a=[]
b1err=[]
with open('./data/data-beta5-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk244=15500
            a1.append(float(row[1]))
            b1.append(float(row[5]))
            a1a.append(float(row[1])*beta5nk244)
            b1err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a2=[]
b2=[]
a2a=[]
b2err=[]
with open('./data/data-beta5-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk350=30000
            a2.append(float(row[1]))
            b2.append(float(row[5]))
            a2a.append(float(row[1])*beta5nk350)
            b2err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a3=[]
b3=[]
a3a=[]
b3err=[]
with open('./data/data-beta5-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk512=70000
            a3.append(float(row[1]))
            b3.append(float(row[5]))
            a3a.append(float(row[1])*beta5nk512)
            b3err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a4=[]
b4=[]
a4a=[]
b4err=[]
with open('./data/data-beta5-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk848=215000
            a4.append(float(row[1]))
            b4.append(float(row[5]))
            a4a.append(float(row[1])*beta5nk848)
            b4err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a5=[]
b5=[]
a5a=[]
b5err=[]
with open('./data/data-beta5-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk1500=700000
            a5.append(float(row[1]))
            b5.append(float(row[5]))
            a5a.append(float(row[1])*beta5nk1500)
            b5err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a6=[]
b6=[]
a6a=[]
b6err=[]
with open('./data/data-beta9-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk244=20000
            a6.append(float(row[1]))
            b6.append(float(row[5]))
            a6a.append(float(row[1])*beta9nk244)
            b6err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a7=[]
b7=[]
a7a=[]
b7err=[]
with open('./data/data-beta9-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk350=50000
            a7.append(float(row[1]))
            b7.append(float(row[5]))
            a7a.append(float(row[1])*beta9nk350)
            b7err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a8=[]
b8=[]
a8a=[]
b8err=[]
with open('./data/data-beta9-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk512=120000
            a8.append(float(row[1]))
            b8.append(float(row[5]))
            a8a.append(float(row[1])*beta9nk512)
            b8err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a9=[]
b9=[]
a9a=[]
b9err=[]
with open('./data/data-beta9-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk848=300000
            a9.append(float(row[1]))
            b9.append(float(row[5]))
            a9a.append(float(row[1])*beta9nk848)
            b9err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a10=[]
b10=[]
a10a=[]
b10err=[]
with open('./data/data-beta9-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk1500=1000000
            a10.append(float(row[1]))
            b10.append(float(row[5]))
            a10a.append(float(row[1])*beta9nk1500)
            b10err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a11=[]
b11=[]
a11a=[]
b11err=[]
with open('./data/data-beta14-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk244=28000
            a11.append(float(row[1]))
            b11.append(float(row[5]))
            a11a.append(float(row[1])*beta14nk244)
            b11err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a12=[]
b12=[]
a12a=[]
b12err=[]
with open('./data/data-beta14-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk350=70000
            a12.append(float(row[1]))
            b12.append(float(row[5]))
            a12a.append(float(row[1])*beta14nk350)
            b12err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a13=[]
b13=[]
a13a=[]
b13err=[]
with open('./data/data-beta14-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk512=145000
            a13.append(float(row[1]))
            b13.append(float(row[5]))
            a13a.append(float(row[1])*beta14nk512)
            b13err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a14=[]
b14=[]
a14a=[]
b14err=[]
with open('./data/data-beta14-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk848=420000
            a14.append(float(row[1]))
            b14.append(float(row[5]))
            a14a.append(float(row[1])*beta14nk848)
            b14err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a15=[]
b15=[]
a15a=[]
b15err=[]
with open('./data/data-beta14-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk1500=1400000
            a15.append(float(row[1]))
            b15.append(float(row[5]))
            a15a.append(float(row[1])*beta14nk1500)
            b15err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a16=[]
b16=[]
a16a=[]
b16err=[]
with open('./data/data-beta20-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk244=38000
            a16.append(float(row[1]))
            b16.append(float(row[5]))
            a16a.append(float(row[1])*beta20nk244)
            b16err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a17=[]
b17=[]
a17a=[]
b17err=[]
with open('./data/data-beta20-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk350=75000
            a17.append(float(row[1]))
            b17.append(float(row[5]))
            a17a.append(float(row[1])*beta20nk350)
            b17err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a18=[]
b18=[]
a18a=[]
b18err=[]
with open('./data/data-beta20-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk512=174000
            a18.append(float(row[1]))
            b18.append(float(row[5]))
            a18a.append(float(row[1])*beta20nk512)
            b18err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a19=[]
b19=[]
a19a=[]
b19err=[]
with open('./data/data-beta20-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk848=530000
            a19.append(float(row[1]))
            b19.append(float(row[5]))
            a19a.append(float(row[1])*beta20nk848)
            b19err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a20=[]
b20=[]
a20a=[]
b20err=[]
with open('./data/data-beta20-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk1500=1720000
            a20.append(float(row[1]))
            b20.append(float(row[5]))
            a20a.append(float(row[1])*beta20nk1500)
            b20err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a21=[]
b21=[]
a21a=[]
b21err=[]
with open('./data/data-beta27-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk244=45000
            a21.append(float(row[1]))
            b21.append(float(row[5]))
            a21a.append(float(row[1])*beta27nk244)
            b21err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a22=[]
b22=[]
a22a=[]
b22err=[]
with open('./data/data-beta27-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk350=85000
            a22.append(float(row[1]))
            b22.append(float(row[5]))
            a22a.append(float(row[1])*beta27nk350)
            b22err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a23=[]
b23=[]
a23a=[]
b23err=[]
with open('./data/data-beta27-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk512=200000
            a23.append(float(row[1]))
            b23.append(float(row[5]))
            a23a.append(float(row[1])*beta27nk512)
            b23err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a24=[]
b24=[]
a24a=[]
b24err=[]
with open('./data/data-beta27-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk848=620000
            a24.append(float(row[1]))
            b24.append(float(row[5]))
            a24a.append(float(row[1])*beta27nk848)
            b24err.append(0.08*np.sqrt(1/(float(row[5]))**2))

a25=[]
b25=[]
a25a=[]
b25err=[]
with open('./data/data-beta27-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk1500=2350000
            a25.append(float(row[1]))
            b25.append(float(row[5]))
            a25a.append(float(row[1])*beta27nk1500)
            b25err.append(0.08*np.sqrt(1/(float(row[5]))**2))
######################################################################################
######################################################################################
######################################################################################


#gammamax=aWR^b
e=2
f=0
WR3e=0.1
WR3f=100
gammamax3e=e*WR3e**f
gammamax3f=e*WR3f**f
fit1x = (WR3e, WR3f)
fit1y = (gammamax3e, gammamax3f)

#gammamax=cWR^d
g=2
h=0.33
WR4g=1
WR4h=10000
gammamax4g=g*WR4g**h
gammamax4h=g*WR4h**h
fit2x = (WR4g, WR4h)
fit2y = (gammamax4g, gammamax4h)


#############################################################################################################################################################

#################################################################################################
powerlaw = lambda x, amp, index: amp * (x**index)
#################################################################################################
loga1 = np.log(a1)
logb1 = np.log(b1)
logb1err = b1err #ya esta error propagado desde 0.08

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga1, ydata=logb1, p0=[0], sigma=logb1err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs1 = np.sqrt(np.diag(cov))

amp1 = (pars[0])

print 'Linearizing data for beta=5 Nk=244'
print 'prefactor=',amp1,'stdevs prefactor=',(stdevs1[0])
tauRtauK1=np.exp(((amp1)-np.log(2))/0.33)
errtauRtauK1=3.0303*np.sqrt(np.exp(6.06061*(amp1-np.log(2)))*stdevs1[0]**2)
#################################################################################################
#################################################################################################
loga2 = np.log(a2)
logb2 = np.log(b2)
logb2err = (b2err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga2, ydata=logb2, p0=[0], sigma=logb2err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs2 = np.sqrt(np.diag(cov))

amp2 = (pars[0])

print 'Linearizing data for beta=5 Nk=350'
print 'prefactor=',amp2,'stdevs prefactor=',(stdevs2[0])
tauRtauK2=np.exp(((amp2)-np.log(2))/0.33)
errtauRtauK2=3.0303*np.sqrt(np.exp(6.06061*(amp2-np.log(2)))*stdevs2[0]**2)
#################################################################################################
#################################################################################################
loga3 = np.log(a3)
logb3 = np.log(b3)
logb3err = (b3err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga3, ydata=logb3, p0=[0], sigma=logb3err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs3 = np.sqrt(np.diag(cov))

amp3 = (pars[0])

print 'Linearizing data for beta=5 Nk=512'
print 'prefactor=',amp3,'stdevs prefactor=',(stdevs3[0])
tauRtauK3=np.exp(((amp3)-np.log(2))/0.33)
errtauRtauK3=3.0303*np.sqrt(np.exp(6.06061*(amp3-np.log(2)))*stdevs3[0]**2)
#################################################################################################
#################################################################################################
loga4 = np.log(a4)
logb4 = np.log(b4)
logb4err = (b4err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga4, ydata=logb4, p0=[0], sigma=logb4err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs4 = np.sqrt(np.diag(cov))

amp4 = (pars[0])

print 'Linearizing data for beta=5 Nk=848'
print 'prefactor=',amp4,'stdevs prefactor=',(stdevs4[0])
tauRtauK4=np.exp(((amp4)-np.log(2))/0.33)
errtauRtauK4=3.0303*np.sqrt(np.exp(6.06061*(amp4-np.log(2)))*stdevs4[0]**2)
#################################################################################################
#################################################################################################
loga5 = np.log(a5)
logb5 = np.log(b5)
logb5err = (b5err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga5, ydata=logb5, p0=[0], sigma=logb5err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs5 = np.sqrt(np.diag(cov))

amp5 = (pars[0])

print 'Linearizing data for beta=5 Nk=1500'
print 'prefactor=',amp5,'stdevs prefactor=',(stdevs5[0])
tauRtauK5=np.exp(((amp5)-np.log(2))/0.33)
errtauRtauK5=3.0303*np.sqrt(np.exp(6.06061*(amp5-np.log(2)))*stdevs5[0]**2)
#################################################################################################
#################################################################################################
loga6 = np.log(a6)
logb6 = np.log(b6)
logb6err = (b6err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga6, ydata=logb6, p0=[0], sigma=logb6err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs6 = np.sqrt(np.diag(cov))

amp6 = (pars[0])

print 'Linearizing data for beta=9 Nk=244'
print 'prefactor=',amp6,'stdevs prefactor=',(stdevs6[0])
tauRtauK6=np.exp(((amp6)-np.log(2))/0.33)
errtauRtauK6=3.0303*np.sqrt(np.exp(6.06061*(amp6-np.log(2)))*stdevs6[0]**2)
#################################################################################################
#################################################################################################
loga7 = np.log(a7)
logb7 = np.log(b7)
logb7err = (b7err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga7, ydata=logb7, p0=[0], sigma=logb7err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs7 = np.sqrt(np.diag(cov))

amp7 = (pars[0])

print 'Linearizing data for beta=9 Nk=350'
print 'prefactor=',amp7,'stdevs prefactor=',(stdevs7[0])
tauRtauK7=np.exp(((amp7)-np.log(2))/0.33)
errtauRtauK7=3.0303*np.sqrt(np.exp(6.06061*(amp7-np.log(2)))*stdevs7[0]**2)
#################################################################################################
#################################################################################################
loga8 = np.log(a8)
logb8 = np.log(b8)
logb8err = (b8err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga8, ydata=logb8, p0=[0], sigma=logb8err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs8 = np.sqrt(np.diag(cov))

amp8 = (pars[0])

print 'Linearizing data for beta=9 Nk=512'
print 'prefactor=',amp8,'stdevs prefactor=',(stdevs8[0])
tauRtauK8=np.exp(((amp8)-np.log(2))/0.33)
errtauRtauK8=3.0303*np.sqrt(np.exp(6.06061*(amp8-np.log(2)))*stdevs8[0]**2)
#################################################################################################
#################################################################################################
loga9 = np.log(a9)
logb9 = np.log(b9)
logb9err = (b9err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga9, ydata=logb9, p0=[0], sigma=logb9err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs9 = np.sqrt(np.diag(cov))

amp9 = (pars[0])

print 'Linearizing data for beta=9 Nk=848'
print 'prefactor=',amp9,'stdevs prefactor=',(stdevs9[0])
tauRtauK9=np.exp(((amp9)-np.log(2))/0.33)
errtauRtauK9=3.0303*np.sqrt(np.exp(6.06061*(amp9-np.log(2)))*stdevs9[0]**2)
#################################################################################################
#################################################################################################
loga10 = np.log(a10)
logb10 = np.log(b10)
logb10err = (b10err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga10, ydata=logb10, p0=[0], sigma=logb10err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs10 = np.sqrt(np.diag(cov))

amp10 = (pars[0])

print 'Linearizing data for beta=9 Nk=1500'
print 'prefactor=',amp10,'stdevs prefactor=',(stdevs10[0])
tauRtauK10=np.exp(((amp10)-np.log(2))/0.33)
errtauRtauK10=3.0303*np.sqrt(np.exp(6.06061*(amp10-np.log(2)))*stdevs10[0]**2)
#################################################################################################
#################################################################################################
loga11 = np.log(a11)
logb11 = np.log(b11)
logb11err = (b11err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga11, ydata=logb11, p0=[0], sigma=logb11err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs11 = np.sqrt(np.diag(cov))

amp11 = (pars[0])

print 'Linearizing data for beta=14 Nk=244'
print 'prefactor=',amp11,'stdevs prefactor=',(stdevs11[0])
tauRtauK11=np.exp(((amp11)-np.log(2))/0.33)
errtauRtauK11=3.0303*np.sqrt(np.exp(6.06061*(amp11-np.log(2)))*stdevs11[0]**2)
#################################################################################################
#################################################################################################
loga12 = np.log(a12)
logb12 = np.log(b12)
logb12err = (b12err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga12, ydata=logb12, p0=[0], sigma=logb12err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs12 = np.sqrt(np.diag(cov))

amp12 = (pars[0])

print 'Linearizing data for beta=14 Nk=350'
print 'prefactor=',amp12,'stdevs prefactor=',(stdevs12[0])
tauRtauK12=np.exp(((amp12)-np.log(2))/0.33)
errtauRtauK12=3.0303*np.sqrt(np.exp(6.06061*(amp12-np.log(2)))*stdevs12[0]**2)
#################################################################################################
#################################################################################################
loga13 = np.log(a13)
logb13 = np.log(b13)
logb13err = (b13err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga13, ydata=logb13, p0=[0], sigma=logb13err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs13 = np.sqrt(np.diag(cov))

amp13 = (pars[0])

print 'Linearizing data for beta=14 Nk=512'
print 'prefactor=',amp13,'stdevs prefactor=',(stdevs13[0])
tauRtauK13=np.exp(((amp13)-np.log(2))/0.33)
errtauRtauK13=3.0303*np.sqrt(np.exp(6.06061*(amp13-np.log(2)))*stdevs13[0]**2)
#################################################################################################
#################################################################################################
loga14 = np.log(a14)
logb14 = np.log(b14)
logb14err = (b14err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga14, ydata=logb14, p0=[0], sigma=logb14err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs14 = np.sqrt(np.diag(cov))

amp14 = (pars[0])

print 'Linearizing data for beta=14 Nk=848'
print 'prefactor=',amp14,'stdevs prefactor=',(stdevs14[0])
tauRtauK14=np.exp(((amp14)-np.log(2))/0.33)
errtauRtauK14=3.0303*np.sqrt(np.exp(6.06061*(amp14-np.log(2)))*stdevs14[0]**2)
#################################################################################################
#################################################################################################
loga15 = np.log(a15)
logb15 = np.log(b15)
logb15err = (b15err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga15, ydata=logb15, p0=[0], sigma=logb15err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs15 = np.sqrt(np.diag(cov))

amp15 = (pars[0])

print 'Linearizing data for beta=14 Nk=1500'
print 'prefactor=',amp15,'stdevs prefactor=',(stdevs15[0])
tauRtauK15=np.exp(((amp15)-np.log(2))/0.33)
errtauRtauK15=3.0303*np.sqrt(np.exp(6.06061*(amp15-np.log(2)))*stdevs15[0]**2)
#################################################################################################
#################################################################################################
loga16 = np.log(a16)
logb16 = np.log(b16)
logb16err = (b16err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga16, ydata=logb16, p0=[0], sigma=logb16err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs16 = np.sqrt(np.diag(cov))

amp16 = (pars[0])

print 'Linearizing data for beta=20 Nk=244'
print 'prefactor=',amp16,'stdevs prefactor=',(stdevs16[0])
tauRtauK16=np.exp(((amp16)-np.log(2))/0.33)
errtauRtauK16=3.0303*np.sqrt(np.exp(6.06061*(amp16-np.log(2)))*stdevs16[0]**2)
#################################################################################################
#################################################################################################
loga17 = np.log(a17)
logb17 = np.log(b17)
logb17err = (b17err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga17, ydata=logb17, p0=[0], sigma=logb17err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs17 = np.sqrt(np.diag(cov))

amp17 = (pars[0])

print 'Linearizing data for beta=20 Nk=350'
print 'prefactor=',amp17,'stdevs prefactor=',(stdevs17[0])
tauRtauK17=np.exp(((amp17)-np.log(2))/0.33)
errtauRtauK17=3.0303*np.sqrt(np.exp(6.06061*(amp17-np.log(2)))*stdevs17[0]**2)
#################################################################################################
#################################################################################################
loga18 = np.log(a18)
logb18 = np.log(b18)
logb18err = (b18err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga18, ydata=logb18, p0=[0], sigma=logb18err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs18 = np.sqrt(np.diag(cov))

amp18 = (pars[0])

print 'Linearizing data for beta=20 Nk=512'
print 'prefactor=',amp18,'stdevs prefactor=',(stdevs18[0])
tauRtauK18=np.exp(((amp18)-np.log(2))/0.33)
errtauRtauK18=3.0303*np.sqrt(np.exp(6.06061*(amp18-np.log(2)))*stdevs18[0]**2)
#################################################################################################
#################################################################################################
loga19 = np.log(a19)
logb19 = np.log(b19)
logb19err = (b19err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga19, ydata=logb19, p0=[0], sigma=logb19err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs19 = np.sqrt(np.diag(cov))

amp19 = (pars[0])

print 'Linearizing data for beta=20 Nk=848'
print 'prefactor=',amp19,'stdevs prefactor=',(stdevs19[0])
tauRtauK19=np.exp(((amp19)-np.log(2))/0.33)
errtauRtauK19=3.0303*np.sqrt(np.exp(6.06061*(amp19-np.log(2)))*stdevs19[0]**2)
#################################################################################################
#################################################################################################
loga20 = np.log(a20)
logb20 = np.log(b20)
logb20err = (b20err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga20, ydata=logb20, p0=[0], sigma=logb20err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs20 = np.sqrt(np.diag(cov))

amp20 = (pars[0])

print 'Linearizing data for beta=20 Nk=1500'
print 'prefactor=',amp20,'stdevs prefactor=',(stdevs20[0])
tauRtauK20=np.exp(((amp20)-np.log(2))/0.33)
errtauRtauK20=3.0303*np.sqrt(np.exp(6.06061*(amp20-np.log(2)))*stdevs20[0]**2)
#################################################################################################
#################################################################################################
loga21 = np.log(a21)
logb21 = np.log(b21)
logb21err = (b21err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga21, ydata=logb21, p0=[0], sigma=logb21err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs21 = np.sqrt(np.diag(cov))

amp21 = (pars[0])

print 'Linearizing data for beta=27 Nk=244'
print 'prefactor=',amp21,'stdevs prefactor=',(stdevs21[0])
tauRtauK21=np.exp(((amp21)-np.log(2))/0.33)
errtauRtauK21=3.0303*np.sqrt(np.exp(6.06061*(amp21-np.log(2)))*stdevs21[0]**2)
#################################################################################################
#################################################################################################
loga22 = np.log(a22)
logb22 = np.log(b22)
logb22err = (b22err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga22, ydata=logb22, p0=[0], sigma=logb22err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs22 = np.sqrt(np.diag(cov))

amp22 = (pars[0])

print 'Linearizing data for beta=27 Nk=350'
print 'prefactor=',amp22,'stdevs prefactor=',(stdevs22[0])
tauRtauK22=np.exp(((amp22)-np.log(2))/0.33)
errtauRtauK22=3.0303*np.sqrt(np.exp(6.06061*(amp22-np.log(2)))*stdevs22[0]**2)
#################################################################################################
#################################################################################################
loga23 = np.log(a23)
logb23 = np.log(b23)
logb23err = (b23err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga23, ydata=logb23, p0=[0], sigma=logb23err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs23 = np.sqrt(np.diag(cov))

amp23 = (pars[0])

print 'Linearizing data for beta=27 Nk=512'
print 'prefactor=',amp23,'stdevs prefactor=',(stdevs23[0])
tauRtauK23=np.exp(((amp23)-np.log(2))/0.33)
errtauRtauK23=3.0303*np.sqrt(np.exp(6.06061*(amp23-np.log(2)))*stdevs23[0]**2)
#################################################################################################
#################################################################################################
loga24 = np.log(a24)
logb24 = np.log(b24)
logb24err = (b24err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga24, ydata=logb24, p0=[0], sigma=logb24err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs24 = np.sqrt(np.diag(cov))

amp24 = (pars[0])

print 'Linearizing data for beta=27 Nk=848'
print 'prefactor=',amp24,'stdevs prefactor=',(stdevs24[0])
tauRtauK24=np.exp(((amp24)-np.log(2))/0.33)
errtauRtauK24=3.0303*np.sqrt(np.exp(6.06061*(amp24-np.log(2)))*stdevs24[0]**2)
#################################################################################################
#################################################################################################
loga25 = np.log(a25)
logb25 = np.log(b25)
logb25err = (b25err)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga25, ydata=logb25, p0=[0], sigma=logb25err, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevs25 = np.sqrt(np.diag(cov))

amp25 = (pars[0])

print 'Linearizing data for beta=27 Nk=1500'
print 'prefactor=',amp25,'stdevs prefactor=',(stdevs25[0])
tauRtauK25=np.exp(((amp25)-np.log(2))/0.33)
errtauRtauK25=3.0303*np.sqrt(np.exp(6.06061*(amp25-np.log(2)))*stdevs25[0]**2)
#################################################################################################
print '%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%'
print 'tauRtauK=', tauRtauK1,'error=', errtauRtauK1
print 'tauRtauK=', tauRtauK2,'error=', errtauRtauK2
print 'tauRtauK=', tauRtauK3,'error=', errtauRtauK3
print 'tauRtauK=', tauRtauK4,'error=', errtauRtauK4
print 'tauRtauK=', tauRtauK5,'error=', errtauRtauK5
print 'tauRtauK=', tauRtauK6,'error=', errtauRtauK6
print 'tauRtauK=', tauRtauK7,'error=', errtauRtauK7
print 'tauRtauK=', tauRtauK8,'error=', errtauRtauK8
print 'tauRtauK=', tauRtauK9,'error=', errtauRtauK9
print 'tauRtauK=', tauRtauK10,'error=', errtauRtauK10
print 'tauRtauK=', tauRtauK11,'error=', errtauRtauK11
print 'tauRtauK=', tauRtauK12,'error=', errtauRtauK12
print 'tauRtauK=', tauRtauK13,'error=', errtauRtauK13
print 'tauRtauK=', tauRtauK14,'error=', errtauRtauK14
print 'tauRtauK=', tauRtauK15,'error=', errtauRtauK15
print 'tauRtauK=', tauRtauK16,'error=', errtauRtauK16
print 'tauRtauK=', tauRtauK17,'error=', errtauRtauK17
print 'tauRtauK=', tauRtauK18,'error=', errtauRtauK18
print 'tauRtauK=', tauRtauK19,'error=', errtauRtauK19
print 'tauRtauK=', tauRtauK20,'error=', errtauRtauK20
print 'tauRtauK=', tauRtauK21,'error=', errtauRtauK21
print 'tauRtauK=', tauRtauK22,'error=', errtauRtauK22
print 'tauRtauK=', tauRtauK23,'error=', errtauRtauK23
print 'tauRtauK=', tauRtauK24,'error=', errtauRtauK24
print 'tauRtauK=', tauRtauK25,'error=', errtauRtauK25

#################################################################################################

def multiply_list(a,b):
    for i in range(len(a)):
        a[i]=a[i]*b
    return a

#############################################################################################################################################################
#############################################################################################################################################################
fig = plt.figure()

fig.subplots_adjust(hspace=0.3,wspace=0.05)

#############################################################################################################################################################
#############################################################################################################################################################
ax = fig.add_subplot(1,5,1)

ax.plot(fit1x, fit1y,color='k',label=r'',ls='-', linewidth=3)
ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

multiply_list(a1,tauRtauK1)
ax.scatter(a1, b1,color='none',label=r'$N_{\rm K}=244, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK1) , marker='^', edgecolor='#FA8072', linewidth='4', s=1200)
multiply_list(a2,tauRtauK2)
ax.scatter(a2, b2,color='none',label=r'$N_{\rm K}=350, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK2) , marker='o', edgecolor='#FA8072', linewidth='4', s=1200)
multiply_list(a3,tauRtauK3)
ax.scatter(a3, b3,color='none',label=r'$N_{\rm K}=512, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK3) , marker='s', edgecolor='#FA8072', linewidth='4', s=1200)
multiply_list(a4,tauRtauK4)
ax.scatter(a4, b4,color='none',label=r'$N_{\rm K}=848, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK4) , marker='p', edgecolor='#FA8072', linewidth='4', s=1200)
multiply_list(a5,tauRtauK5)
ax.scatter(a5, b5,color='none',label=r'$N_{\rm K}=1500, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK5) , marker='v', edgecolor='#FA8072', linewidth='4', s=1200)


plt.xlabel(r'$\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\gamma_{\rm max}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
#plt.tick_params(axis='y', colors='r')
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
ax.tick_params(which='major', direction='in', length=30, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=20, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
#ax.legend(loc='lower right', bbox_to_anchor=(1.15, 0), shadow=True, ncol=1, prop={'size': 60})
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 0), shadow=True, ncol=1, prop={'size': 50})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.85, textstr1, transform=ax.transAxes, fontsize=70, verticalalignment='top')

textstr2 = '\n'.join((r'$\beta=5$',))
plt.text(0.07, 0.95, textstr2, transform=ax.transAxes, fontsize=80, verticalalignment='top', color='k')

plt.xlim(0.1,1000)
plt.ylim(1,20)
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
ax = fig.add_subplot(1,5,2)

ax.plot(fit1x, fit1y,color='k',label=r'',ls='-', linewidth=3)
ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

multiply_list(a6,tauRtauK6)
ax.scatter(a6, b6,color='none',label=r'$N_{\rm K}=244, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK6) , marker='^', edgecolor='#708090', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'
multiply_list(a7,tauRtauK7)
ax.scatter(a7, b7,color='none',label=r'$N_{\rm K}=350, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK7) , marker='o', edgecolor='#708090', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'
multiply_list(a8,tauRtauK8)
ax.scatter(a8, b8,color='none',label=r'$N_{\rm K}=512, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK8) , marker='s', edgecolor='#708090', linewidth='4', s=1200) #r'${\rm FSM}, \beta=5, N_{\rm K}=848, \langle Z\rangle=142$'
multiply_list(a9,tauRtauK9)
ax.scatter(a9, b9,color='none',label=r'$N_{\rm K}=848, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK9) , marker='p', edgecolor='#708090', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=244, \langle Z\rangle=17$'
multiply_list(a10,tauRtauK10)
ax.scatter(a10, b10,color='none',label=r'$N_{\rm K}=1500, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK10) , marker='v', edgecolor='#708090', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=512, \langle Z\rangle=35$'

plt.xlabel(r'$\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\gamma_{\rm max}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
#plt.tick_params(axis='y', colors='r')
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
ax.tick_params(which='major', direction='in', length=30, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=20, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
#ax.legend(loc='lower right', bbox_to_anchor=(1.15, 0), shadow=True, ncol=1, prop={'size': 60})
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 0), shadow=True, ncol=1, prop={'size': 50})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.85, textstr1, transform=ax.transAxes, fontsize=70, verticalalignment='top')

textstr2 = '\n'.join((r'$\beta=9$',))
plt.text(0.07, 0.95, textstr2, transform=ax.transAxes, fontsize=80, verticalalignment='top', color='k')

plt.xlim(0.1,1000)
plt.ylim(1,20)
# #############################################################################################################################################################
# #############################################################################################################################################################
ax = fig.add_subplot(1,5,3)

ax.plot(fit1x, fit1y,color='k',label=r'',ls='-', linewidth=3)
ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

multiply_list(a11,tauRtauK11)
ax.scatter(a11, b11,color='none',label=r'$N_{\rm K}=244, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK11) , marker='^', edgecolor='maroon', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'
multiply_list(a12,tauRtauK12)
ax.scatter(a12, b12,color='none',label=r'$N_{\rm K}=350, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK12) , marker='o', edgecolor='maroon', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'
multiply_list(a13,tauRtauK13)
ax.scatter(a13, b13,color='none',label=r'$N_{\rm K}=512, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK13) , marker='s', edgecolor='maroon', linewidth='4', s=1200) #r'${\rm FSM}, \beta=5, N_{\rm K}=848, \langle Z\rangle=142$'
multiply_list(a14,tauRtauK14)
ax.scatter(a14, b14,color='none',label=r'$N_{\rm K}=848, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK14) , marker='p', edgecolor='maroon', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=244, \langle Z\rangle=17$'
multiply_list(a15,tauRtauK15)
ax.scatter(a15, b15,color='none',label=r'$N_{\rm K}=1500, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK15) , marker='v', edgecolor='maroon', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=512, \langle Z\rangle=35$'


plt.xlabel(r'$\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\gamma_{\rm max}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
#plt.tick_params(axis='y', colors='r')
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
ax.tick_params(which='major', direction='in', length=30, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=20, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
#ax.legend(loc='lower right', bbox_to_anchor=(1.15, 0), shadow=True, ncol=1, prop={'size': 60})
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 0), shadow=True, ncol=1, prop={'size': 50})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.85, textstr1, transform=ax.transAxes, fontsize=70, verticalalignment='top')

textstr2 = '\n'.join((r'$\beta=14$',))
plt.text(0.07, 0.95, textstr2, transform=ax.transAxes, fontsize=80, verticalalignment='top', color='k')

plt.xlim(0.1,1000)
plt.ylim(1,20)
# #############################################################################################################################################################
# #############################################################################################################################################################
ax = fig.add_subplot(1,5,4)

ax.plot(fit1x, fit1y,color='k',label=r'',ls='-', linewidth=3)
ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

multiply_list(a16,tauRtauK16)
ax.scatter(a16, b16,color='none',label=r'$N_{\rm K}=244, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK16) , marker='^', edgecolor='mediumseagreen', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'
multiply_list(a17,tauRtauK17)
ax.scatter(a17, b17,color='none',label=r'$N_{\rm K}=350, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK17) , marker='o', edgecolor='mediumseagreen', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'
multiply_list(a18,tauRtauK18)
ax.scatter(a18, b18,color='none',label=r'$N_{\rm K}=512, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK18) , marker='s', edgecolor='mediumseagreen', linewidth='4', s=1200) #r'${\rm FSM}, \beta=5, N_{\rm K}=848, \langle Z\rangle=142$'
multiply_list(a19,tauRtauK19)
ax.scatter(a19, b19,color='none',label=r'$N_{\rm K}=848, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK19) , marker='p', edgecolor='mediumseagreen', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=244, \langle Z\rangle=17$'
multiply_list(a20,tauRtauK20)
ax.scatter(a20, b20,color='none',label=r'$N_{\rm K}=1500, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK20) , marker='v', edgecolor='mediumseagreen', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=512, \langle Z\rangle=35$'


plt.xlabel(r'$\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\gamma_{\rm max}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
#plt.tick_params(axis='y', colors='r')
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
ax.tick_params(which='major', direction='in', length=30, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=20, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
#ax.legend(loc='lower right', bbox_to_anchor=(1.15, 0), shadow=True, ncol=1, prop={'size': 60})
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 0), shadow=True, ncol=1, prop={'size': 50})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.85, textstr1, transform=ax.transAxes, fontsize=70, verticalalignment='top')

textstr2 = '\n'.join((r'$\beta=20$',))
plt.text(0.07, 0.95, textstr2, transform=ax.transAxes, fontsize=80, verticalalignment='top', color='k')

plt.xlim(0.1,1000)
plt.ylim(1,20)
#############################################################################################################################################################
#############################################################################################################################################################
ax = fig.add_subplot(1,5,5)

ax.plot(fit1x, fit1y,color='k',label=r'',ls='-', linewidth=3)
ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

multiply_list(a21,tauRtauK21)
ax.scatter(a21, b21,color='none',label=r'$N_{\rm K}=244, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK21) , marker='^', edgecolor='dodgerblue', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'
multiply_list(a22,tauRtauK22)
ax.scatter(a22, b22,color='none',label=r'$N_{\rm K}=350, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK22) , marker='o', edgecolor='dodgerblue', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'
multiply_list(a23,tauRtauK23)
ax.scatter(a23, b23,color='none',label=r'$N_{\rm K}=512, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK23) , marker='s', edgecolor='dodgerblue', linewidth='4', s=1200) #r'${\rm FSM}, \beta=5, N_{\rm K}=848, \langle Z\rangle=142$'
multiply_list(a24,tauRtauK24)
ax.scatter(a24, b24,color='none',label=r'$N_{\rm K}=848, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK24) , marker='p', edgecolor='dodgerblue', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=244, \langle Z\rangle=17$'
multiply_list(a25,tauRtauK25)
ax.scatter(a25, b25,color='none',label=r'$N_{\rm K}=1500, \tau_{\rm R}/\tau_{\rm K}=%7.3f$' % (tauRtauK25) , marker='v', edgecolor='dodgerblue', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=512, \langle Z\rangle=35$'


plt.xlabel(r'$\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\gamma_{\rm max}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
#plt.tick_params(axis='y', colors='r')
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
ax.tick_params(which='major', direction='in', length=30, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=20, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
#ax.legend(loc='lower right', bbox_to_anchor=(1.15, 0), shadow=True, ncol=1, prop={'size': 60})
ax.legend(loc='lower right', bbox_to_anchor=(1.0, 0), shadow=True, ncol=1, prop={'size': 50})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.85, textstr1, transform=ax.transAxes, fontsize=70, verticalalignment='top')

textstr2 = '\n'.join((r'$\beta=27$',))
plt.text(0.07, 0.95, textstr2, transform=ax.transAxes, fontsize=80, verticalalignment='top', color='k')

plt.xlim(0.1,1000)
plt.ylim(1,20)
# #############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#ax.label_outer()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(150, 25)
fig.savefig('gammamax-WeWiR1.eps', dpi=300, bbox_inches='tight')
#plt.show()
