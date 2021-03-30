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
with open('./data/data-beta5-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk244=15500
            a1.append(float(row[1]))
            b1.append(float(row[5]))
            a1a.append(float(row[1])*beta5nk244)

a2=[]
b2=[]
a2a=[]
with open('./data/data-beta5-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk350=30000
            a2.append(float(row[1]))
            b2.append(float(row[5]))
            a2a.append(float(row[1])*beta5nk350)

a3=[]
b3=[]
a3a=[]
with open('./data/data-beta5-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk512=70000
            a3.append(float(row[1]))
            b3.append(float(row[5]))
            a3a.append(float(row[1])*beta5nk512)

a4=[]
b4=[]
a4a=[]
with open('./data/data-beta5-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk848=215000
            a4.append(float(row[1]))
            b4.append(float(row[5]))
            a4a.append(float(row[1])*beta5nk848)

a5=[]
b5=[]
a5a=[]
with open('./data/data-beta5-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta5nk1500=700000
            a5.append(float(row[1]))
            b5.append(float(row[5]))
            a5a.append(float(row[1])*beta5nk1500)

a6=[]
b6=[]
a6a=[]
with open('./data/data-beta9-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk244=20000
            a6.append(float(row[1]))
            b6.append(float(row[5]))
            a6a.append(float(row[1])*beta9nk244)

a7=[]
b7=[]
a7a=[]
with open('./data/data-beta9-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk350=50000
            a7.append(float(row[1]))
            b7.append(float(row[5]))
            a7a.append(float(row[1])*beta9nk350)

a8=[]
b8=[]
a8a=[]
with open('./data/data-beta9-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk512=120000
            a8.append(float(row[1]))
            b8.append(float(row[5]))
            a8a.append(float(row[1])*beta9nk512)

a9=[]
b9=[]
a9a=[]
with open('./data/data-beta9-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk848=300000
            a9.append(float(row[1]))
            b9.append(float(row[5]))
            a9a.append(float(row[1])*beta9nk848)

a10=[]
b10=[]
a10a=[]
with open('./data/data-beta9-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta9nk1500=1000000
            a10.append(float(row[1]))
            b10.append(float(row[5]))
            a10a.append(float(row[1])*beta9nk1500)

a11=[]
b11=[]
a11a=[]
with open('./data/data-beta14-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk244=28000
            a11.append(float(row[1]))
            b11.append(float(row[5]))
            a11a.append(float(row[1])*beta14nk244)

a12=[]
b12=[]
a12a=[]
with open('./data/data-beta14-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk350=70000
            a12.append(float(row[1]))
            b12.append(float(row[5]))
            a12a.append(float(row[1])*beta14nk350)

a13=[]
b13=[]
a13a=[]
with open('./data/data-beta14-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk512=145000
            a13.append(float(row[1]))
            b13.append(float(row[5]))
            a13a.append(float(row[1])*beta14nk512)

a14=[]
b14=[]
a14a=[]
with open('./data/data-beta14-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk848=420000
            a14.append(float(row[1]))
            b14.append(float(row[5]))
            a14a.append(float(row[1])*beta14nk848)

a15=[]
b15=[]
a15a=[]
with open('./data/data-beta14-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta14nk1500=1400000
            a15.append(float(row[1]))
            b15.append(float(row[5]))
            a15a.append(float(row[1])*beta14nk1500)

a16=[]
b16=[]
a16a=[]
with open('./data/data-beta20-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk244=38000
            a16.append(float(row[1]))
            b16.append(float(row[5]))
            a16a.append(float(row[1])*beta20nk244)

a17=[]
b17=[]
a17a=[]
with open('./data/data-beta20-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk350=75000
            a17.append(float(row[1]))
            b17.append(float(row[5]))
            a17a.append(float(row[1])*beta20nk350)

a18=[]
b18=[]
a18a=[]
with open('./data/data-beta20-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk512=174000
            a18.append(float(row[1]))
            b18.append(float(row[5]))
            a18a.append(float(row[1])*beta20nk512)

a19=[]
b19=[]
a19a=[]
with open('./data/data-beta20-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk848=530000
            a19.append(float(row[1]))
            b19.append(float(row[5]))
            a19a.append(float(row[1])*beta20nk848)

a20=[]
b20=[]
a20a=[]
with open('./data/data-beta20-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta20nk1500=1720000
            a20.append(float(row[1]))
            b20.append(float(row[5]))
            a20a.append(float(row[1])*beta20nk1500)

a21=[]
b21=[]
a21a=[]
with open('./data/data-beta27-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk244=45000
            a21.append(float(row[1]))
            b21.append(float(row[5]))
            a21a.append(float(row[1])*beta27nk244)

a22=[]
b22=[]
a22a=[]
with open('./data/data-beta27-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk350=85000
            a22.append(float(row[1]))
            b22.append(float(row[5]))
            a22a.append(float(row[1])*beta27nk350)

a23=[]
b23=[]
a23a=[]
with open('./data/data-beta27-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk512=200000
            a23.append(float(row[1]))
            b23.append(float(row[5]))
            a23a.append(float(row[1])*beta27nk512)

a24=[]
b24=[]
a24a=[]
with open('./data/data-beta27-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk848=620000
            a24.append(float(row[1]))
            b24.append(float(row[5]))
            a24a.append(float(row[1])*beta27nk848)

a25=[]
b25=[]
a25a=[]
with open('./data/data-beta27-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            beta27nk1500=2350000
            a25.append(float(row[1]))
            b25.append(float(row[5]))
            a25a.append(float(row[1])*beta27nk1500)
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

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga1, ydata=logb1, p0=[0], bounds=(-np.inf, np.inf))

stdevs1 = np.sqrt(np.diag(cov))

amp1 = np.exp(pars[0])

print 'Linearizing data for beta=5 Nk=244'
print 'prefactor=',amp1
print 'stdevs prefactor=',np.exp(stdevs1[0])
tauRtauK1=np.exp((np.log(amp1)-np.log(2))/0.33)
print tauRtauK1
#################################################################################################
#################################################################################################
loga2 = np.log(a2)
logb2 = np.log(b2)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga2, ydata=logb2, p0=[0], bounds=(-np.inf, np.inf))

stdevs2 = np.sqrt(np.diag(cov))

amp2 = np.exp(pars[0])

print 'Linearizing data for beta=5 Nk=350'
print 'prefactor=',amp2
print 'stdevs prefactor=',np.exp(stdevs2[0])
tauRtauK2=np.exp((np.log(amp2)-np.log(2))/0.33)
print tauRtauK2
#################################################################################################
#################################################################################################
loga3 = np.log(a3)
logb3 = np.log(b3)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga3, ydata=logb3, p0=[0], bounds=(-np.inf, np.inf))

stdevs3 = np.sqrt(np.diag(cov))

amp3 = np.exp(pars[0])

print 'Linearizing data for beta=5 Nk=512'
print 'prefactor=',amp3
print 'stdevs prefactor=',np.exp(stdevs3[0])
tauRtauK3=np.exp((np.log(amp3)-np.log(2))/0.33)
print tauRtauK3
#################################################################################################

#################################################################################################
loga4 = np.log(a4)
logb4 = np.log(b4)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga4, ydata=logb4, p0=[0], bounds=(-np.inf, np.inf))

stdevs4 = np.sqrt(np.diag(cov))

amp4 = np.exp(pars[0])

print 'Linearizing data for beta=5 Nk=848'
print 'prefactor=',amp4
print 'stdevs prefactor=',np.exp(stdevs4[0])
tauRtauK4=np.exp((np.log(amp4)-np.log(2))/0.33)
print tauRtauK4
#################################################################################################
#################################################################################################
loga5 = np.log(a5)
logb5 = np.log(b5)

def model(x, a):
   return a + 0.33 * x

pars, cov = curve_fit(f=model, xdata=loga5, ydata=logb5, p0=[0], bounds=(-np.inf, np.inf))

stdevs5 = np.sqrt(np.diag(cov))

amp5 = np.exp(pars[0])

print 'Linearizing data for beta=5 Nk=1500'
print 'prefactor=',amp5
print 'stdevs prefactor=',np.exp(stdevs5[0])
tauRtauK5=np.exp((np.log(amp5)-np.log(2))/0.33)
print tauRtauK5
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
ax = fig.add_subplot(1,1,1)

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


plt.xlabel(r'$\dot{\gamma}\tau_{\rm K}$',fontsize=90)
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
# #############################################################################################################################################################
# ax = fig.add_subplot(1,5,2)
#
# ax.plot(fit1x, fit1y,color='k',label=r'',ls='-', linewidth=3)
# ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)
#
# ax.scatter(a6, b6,color='none',label=r'$\beta=9, N_{\rm K}=244$', marker='^', edgecolor='#708090', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'
# ax.scatter(a7, b7,color='none',label=r'$\beta=9, N_{\rm K}=350$', marker='o', edgecolor='#708090', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'
# ax.scatter(a8, b8,color='none',label=r'$\beta=9, N_{\rm K}=512$', marker='s', edgecolor='#708090', linewidth='4', s=1200) #r'${\rm FSM}, \beta=5, N_{\rm K}=848, \langle Z\rangle=142$'
# ax.scatter(a9, b9,color='none',label=r'$\beta=9, N_{\rm K}=848$', marker='D', edgecolor='#708090', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=244, \langle Z\rangle=17$'
# ax.scatter(a10, b10,color='none',label=r'$\beta=9, N_{\rm K}=1500$', marker='v', edgecolor='#708090', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=512, \langle Z\rangle=35$'
# #ax.scatter(x6, y6,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='^', edgecolor='#708090', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=848, \langle Z\rangle=57$'
# #ax.scatter(x11, y11,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='s', edgecolor='#FED001', linewidth='4', s=1200) #r'${\rm FSM}, \beta=27, N_{\rm K}=244, \langle Z\rangle=10$'
#
# plt.xlabel(r'$\dot{\gamma}\tau_{\rm K}$',fontsize=90)
# plt.ylabel(r'$\gamma_{\rm max}$',fontsize=90)
# plt.xticks(fontsize=90)
# plt.yticks(fontsize=90)
# plt.xscale('log')
# plt.yscale('log')
# #plt.tick_params(axis='y', colors='r')
# #ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
# #ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
# ax.tick_params(which='major', direction='in', length=20, axis='both', colors='k', pad=35)
# ax.tick_params(which='minor', direction='in', length=10, axis='both', colors='k', pad=35)
# ax.yaxis.set_ticks_position('both')
# ax.xaxis.set_ticks_position('both')
# plt.legend()
# chartBox = ax.get_position()
# ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
# ax.legend(loc='lower right', bbox_to_anchor=(1.5, 0), shadow=True, ncol=1, prop={'size': 40})
#
# textstr1 = '\n'.join((r'$\angle 0.33$',))
# plt.text(0.8, 0.85, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')
#
# plt.xlim(0.0000001,0.1)
# plt.ylim(1,20)
# # #############################################################################################################################################################
# # #############################################################################################################################################################
# ax = fig.add_subplot(1,5,3)
#
# ax.plot(fit1x, fit1y,color='k',label=r'',ls='-', linewidth=3)
# ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)
#
# ax.scatter(a11, b11,color='none',label=r'$\beta=14, N_{\rm K}=244$', marker='^', edgecolor='#FED001', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'
# ax.scatter(a12, b12,color='none',label=r'$\beta=14, N_{\rm K}=350$', marker='o', edgecolor='#FED001', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'
# ax.scatter(a13, b13,color='none',label=r'$\beta=14, N_{\rm K}=512$', marker='s', edgecolor='#FED001', linewidth='4', s=1200) #r'${\rm FSM}, \beta=5, N_{\rm K}=848, \langle Z\rangle=142$'
# ax.scatter(a14, b14,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='D', edgecolor='#FED001', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=244, \langle Z\rangle=17$'
# ax.scatter(a15, b15,color='none',label=r'$\beta=14, N_{\rm K}=1500$', marker='v', edgecolor='#FED001', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=512, \langle Z\rangle=35$'
# #ax.scatter(x6, y6,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='^', edgecolor='#708090', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=848, \langle Z\rangle=57$'
# #ax.scatter(x11, y11,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='s', edgecolor='#FED001', linewidth='4', s=1200) #r'${\rm FSM}, \beta=27, N_{\rm K}=244, \langle Z\rangle=10$'
#
# plt.xlabel(r'$\dot{\gamma}\tau_{\rm K}$',fontsize=90)
# plt.ylabel(r'$\gamma_{\rm max}$',fontsize=90)
# plt.xticks(fontsize=90)
# plt.yticks(fontsize=90)
# plt.xscale('log')
# plt.yscale('log')
# #plt.tick_params(axis='y', colors='r')
# #ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
# #ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
# ax.tick_params(which='major', direction='in', length=20, axis='both', colors='k', pad=35)
# ax.tick_params(which='minor', direction='in', length=10, axis='both', colors='k', pad=35)
# ax.yaxis.set_ticks_position('both')
# ax.xaxis.set_ticks_position('both')
# plt.legend()
# chartBox = ax.get_position()
# ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
# ax.legend(loc='lower right', bbox_to_anchor=(1.5, 0), shadow=True, ncol=1, prop={'size': 40})
#
# textstr1 = '\n'.join((r'$\angle 0.33$',))
# plt.text(0.8, 0.85, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')
#
# plt.xlim(0.0000001,0.1)
# plt.ylim(1,20)
# # #############################################################################################################################################################
# # #############################################################################################################################################################
# ax = fig.add_subplot(1,5,4)
#
# ax.plot(fit1x, fit1y,color='k',label=r'',ls='-', linewidth=3)
# ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)
#
# ax.scatter(a16, b16,color='none',label=r'$\beta=20, N_{\rm K}=244$', marker='^', edgecolor='#64F0A4', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'
# ax.scatter(a17, b17,color='none',label=r'$\beta=20, N_{\rm K}=350$', marker='o', edgecolor='#64F0A4', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'
# ax.scatter(a18, b18,color='none',label=r'$\beta=20, N_{\rm K}=512$', marker='s', edgecolor='#64F0A4', linewidth='4', s=1200) #r'${\rm FSM}, \beta=5, N_{\rm K}=848, \langle Z\rangle=142$'
# ax.scatter(a19, b19,color='none',label=r'$\beta=20, N_{\rm K}=848$', marker='D', edgecolor='#64F0A4', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=244, \langle Z\rangle=17$'
# ax.scatter(a20, b20,color='none',label=r'$\beta=20, N_{\rm K}=1500$', marker='v', edgecolor='#64F0A4', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=512, \langle Z\rangle=35$'
# #ax.scatter(x6, y6,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='^', edgecolor='#708090', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=848, \langle Z\rangle=57$'
# #ax.scatter(x11, y11,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='s', edgecolor='#FED001', linewidth='4', s=1200) #r'${\rm FSM}, \beta=27, N_{\rm K}=244, \langle Z\rangle=10$'
#
# plt.xlabel(r'$\dot{\gamma}\tau_{\rm K}$',fontsize=90)
# plt.ylabel(r'$\gamma_{\rm max}$',fontsize=90)
# plt.xticks(fontsize=90)
# plt.yticks(fontsize=90)
# plt.xscale('log')
# plt.yscale('log')
# #plt.tick_params(axis='y', colors='r')
# #ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
# #ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
# ax.tick_params(which='major', direction='in', length=20, axis='both', colors='k', pad=35)
# ax.tick_params(which='minor', direction='in', length=10, axis='both', colors='k', pad=35)
# ax.yaxis.set_ticks_position('both')
# ax.xaxis.set_ticks_position('both')
# plt.legend()
# chartBox = ax.get_position()
# ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
# ax.legend(loc='lower right', bbox_to_anchor=(1.5, 0), shadow=True, ncol=1, prop={'size': 40})
#
# textstr1 = '\n'.join((r'$\angle 0.33$',))
# plt.text(0.8, 0.85, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')
#
# plt.xlim(0.0000001,0.1)
# plt.ylim(1,20)
# #############################################################################################################################################################
# #############################################################################################################################################################
# ax = fig.add_subplot(1,5,5)
#
# ax.plot(fit1x, fit1y,color='k',label=r'',ls='-', linewidth=3)
# ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)
#
# ax.scatter(a21, b21,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='^', edgecolor='#23BFE5', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'
# ax.scatter(a22, b22,color='none',label=r'$\beta=27, N_{\rm K}=350$', marker='o', edgecolor='#23BFE5', linewidth='4', s=1200)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'
# ax.scatter(a23, b23,color='none',label=r'$\beta=27, N_{\rm K}=512$', marker='s', edgecolor='#23BFE5', linewidth='4', s=1200) #r'${\rm FSM}, \beta=5, N_{\rm K}=848, \langle Z\rangle=142$'
# ax.scatter(a24, b24,color='none',label=r'$\beta=27, N_{\rm K}=848$', marker='D', edgecolor='#23BFE5', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=244, \langle Z\rangle=17$'
# ax.scatter(a25, b25,color='none',label=r'$\beta=27, N_{\rm K}=1500$', marker='v', edgecolor='#23BFE5', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=512, \langle Z\rangle=35$'
# #ax.scatter(x6, y6,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='^', edgecolor='#708090', linewidth='4', s=1200)   #r'${\rm FSM}, \beta=14, N_{\rm K}=848, \langle Z\rangle=57$'
# #ax.scatter(x11, y11,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='s', edgecolor='#FED001', linewidth='4', s=1200) #r'${\rm FSM}, \beta=27, N_{\rm K}=244, \langle Z\rangle=10$'
#
# plt.xlabel(r'$\dot{\gamma}\tau_{\rm K}$',fontsize=90)
# plt.ylabel(r'$\gamma_{\rm max}$',fontsize=90)
# plt.xticks(fontsize=90)
# plt.yticks(fontsize=90)
# plt.xscale('log')
# plt.yscale('log')
# #plt.tick_params(axis='y', colors='r')
# #ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
# #ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
# ax.tick_params(which='major', direction='in', length=20, axis='both', colors='k', pad=35)
# ax.tick_params(which='minor', direction='in', length=10, axis='both', colors='k', pad=35)
# ax.yaxis.set_ticks_position('both')
# ax.xaxis.set_ticks_position('both')
# plt.legend()
# chartBox = ax.get_position()
# ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
# ax.legend(loc='lower right', bbox_to_anchor=(1.5, 0), shadow=True, ncol=1, prop={'size': 40})
#
# textstr1 = '\n'.join((r'$\angle 0.33$',))
# plt.text(0.8, 0.85, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')
#
# plt.xlim(0.0000001,0.1)
# plt.ylim(1,20)
# #############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#ax.label_outer()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(30, 25)
fig.savefig('gammamax-WeWiR1.eps', dpi=300, bbox_inches='tight')
#plt.show()
