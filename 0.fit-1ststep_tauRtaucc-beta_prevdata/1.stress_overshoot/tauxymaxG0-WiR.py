import sys
import math
import matplotlib
import numpy as np
from matplotlib import pyplot as plt
import csv
import pandas as pd
#from matplotlib.ticker import FormatStrFormatter
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
from scipy.interpolate import make_interp_spline, BSpline
matplotlib.rc('text', usetex = True)
######################################################################################
######################################################################################
x1=[]
y1=[]
with open('./data/data-beta5-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=39.5
            Nk=244
            beta=5
            x1.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y1.append(float(row[3])/G0)

x2=[]
y2=[]
with open('./data/data-beta5-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=57.16666
            Nk=350
            beta=5
            x2.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y2.append(float(row[3])/G0)

x3=[]
y3=[]
with open('./data/data-beta5-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=84.166666
            Nk=512
            beta=5
            x3.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y3.append(float(row[3])/G0)

x4=[]
y4=[]
with open('./data/data-beta5-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=140.1666666
            Nk=848
            beta=5
            x4.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y4.append(float(row[3])/G0)

x5=[]
y5=[]
with open('./data/data-beta5-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=248.833333
            Nk=1500
            beta=5
            x5.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y5.append(float(row[3])/G0)

x6=[]
y6=[]
with open('./data/data-beta9-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=23.3
            Nk=244
            beta=9
            x6.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y6.append(float(row[3])/G0)

x7=[]
y7=[]
with open('./data/data-beta9-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=33.9
            Nk=350
            beta=9
            x7.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y7.append(float(row[3])/G0)

x8=[]
y8=[]
with open('./data/data-beta9-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=50.1
            Nk=512
            beta=9
            x8.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y8.append(float(row[3])/G0)

x9=[]
y9=[]
with open('./data/data-beta9-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=83.7
            Nk=848
            beta=9
            x9.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y9.append(float(row[3])/G0)

x10=[]
y10=[]
with open('./data/data-beta9-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=148.9
            Nk=1500
            beta=9
            x10.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y10.append(float(row[3])/G0)

x11=[]
y11=[]
with open('./data/data-beta14-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=15.17333
            Nk=244
            beta=14
            x11.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y11.append(float(row[3])/G0)

x12=[]
y12=[]
with open('./data/data-beta14-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=22.2666
            Nk=350
            beta=14
            x12.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y12.append(float(row[3])/G0)

x13=[]
y13=[]
with open('./data/data-beta14-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=33.093333
            Nk=512
            beta=14
            x13.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y13.append(float(row[3])/G0)

x14=[]
y14=[]
with open('./data/data-beta14-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=55.493333
            Nk=848
            beta=14
            x14.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y14.append(float(row[3])/G0)

x15=[]
y15=[]
with open('./data/data-beta14-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=98.9333333
            Nk=1500
            beta=14
            x15.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y15.append(float(row[3])/G0)

x16=[]
y16=[]
with open('./data/data-beta20-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=10.57142857
            Nk=244
            beta=20
            x16.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y16.append(float(row[3])/G0)

x17=[]
y17=[]
with open('./data/data-beta20-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=15.61904762
            Nk=350
            beta=20
            x17.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y17.append(float(row[3])/G0)

x18=[]
y18=[]
with open('./data/data-beta20-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=23.3333333
            Nk=512
            beta=20
            x18.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y18.append(float(row[3])/G0)

x19=[]
y19=[]
with open('./data/data-beta20-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=39.33333333
            Nk=848
            beta=20
            x19.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y19.append(float(row[3])/G0)

x20=[]
y20=[]
with open('./data/data-beta20-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=70.38095238
            Nk=1500
            beta=20
            x20.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y20.append(float(row[3])/G0)

x21=[]
y21=[]
with open('./data/data-beta27-NK244-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=7.678571429
            Nk=244
            beta=27
            x21.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y21.append(float(row[3])/G0)

x22=[]
y22=[]
with open('./data/data-beta27-NK350-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=11.46428571
            Nk=350
            beta=27
            x22.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y22.append(float(row[3])/G0)

x23=[]
y23=[]
with open('./data/data-beta27-NK512-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=17.25
            Nk=512
            beta=27
            x23.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y23.append(float(row[3])/G0)

x24=[]
y24=[]
with open('./data/data-beta27-NK848-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=29.25
            Nk=848
            beta=27
            x24.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y24.append(float(row[3])/G0)

x25=[]
y25=[]
with open('./data/data-beta27-NK1500-gammatauk','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            G0=52.53571429
            Nk=1500
            beta=27
            x25.append(float(row[1])*0.082189*Nk**(2.0286126)*beta**(0.0000815477*Nk+0.5804668))
            y25.append(float(row[3])/G0)

#gammamax=cWR^d
g=0.64
h=0.33
WR4g=0.00001
WR4h=10000
gammamax4g=g*WR4g**h
gammamax4h=g*WR4h**h
fit2x = (WR4g, WR4h)
fit2y = (gammamax4g, gammamax4h)

######################################################################################
fit1a = (0.04, 0.04)
fit1b = (0.1, 100)

fit2a = (0.042, 0.042)
fit2b = (0.1, 100)

fit3a = (0.044, 0.044)
fit3b = (0.1, 100)

fit4a = (20, 20)
fit4b = (0.1, 100)

fit5a = (19.5, 19.5)
fit5b = (0.1, 100)

fit6a = (19, 19)
fit6b = (0.1, 100)
######################################################################################

fig = plt.figure()

fig.subplots_adjust(hspace=0,wspace=0.1)

#############################################################################################################################################################
ax = fig.add_subplot(1,5,1)

ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

ax.scatter(x1, y1,color='none',label=r'$\beta=5, N_{\rm K}=244$', marker='^', edgecolor='#FA8072', linewidth='4', s=1200)
ax.scatter(x2, y2,color='none',label=r'$\beta=5, N_{\rm K}=350$', marker='o', edgecolor='#FA8072', linewidth='4', s=1200)
ax.scatter(x3, y3,color='none',label=r'$\beta=5, N_{\rm K}=512$', marker='s', edgecolor='#FA8072', linewidth='4', s=1200)
ax.scatter(x4, y4,color='none',label=r'$\beta=5, N_{\rm K}=848$', marker='p', edgecolor='#FA8072', linewidth='4', s=1200)
ax.scatter(x5, y5,color='none',label=r'$\beta=5, N_{\rm K}=1500$', marker='v', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x6, y6,color='none',label=r'$\beta=9, N_{\rm K}=244$', marker='^', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x7, y7,color='none',label=r'$\beta=9, N_{\rm K}=350$', marker='o', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x8, y8,color='none',label=r'$\beta=9, N_{\rm K}=512$', marker='s', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x9, y9,color='none',label=r'$\beta=9, N_{\rm K}=848$', marker='D', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x10, y10,color='none',label=r'$\beta=9, N_{\rm K}=1500$', marker='v', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x11, y11,color='none',label=r'$\beta=14, N_{\rm K}=244$', marker='^', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x12, y12,color='none',label=r'$\beta=14, N_{\rm K}=350$', marker='o', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x13, y13,color='none',label=r'$\beta=14, N_{\rm K}=512$', marker='s', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x14, y14,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='D', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x15, y15,color='none',label=r'$\beta=14, N_{\rm K}=1500$', marker='v', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x16, y16,color='none',label=r'$\beta=20, N_{\rm K}=244$', marker='^', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x17, y17,color='none',label=r'$\beta=20, N_{\rm K}=350$', marker='o', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x18, y18,color='none',label=r'$\beta=20, N_{\rm K}=512$', marker='s', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x19, y19,color='none',label=r'$\beta=20, N_{\rm K}=848$', marker='D', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x20, y20,color='none',label=r'$\beta=20, N_{\rm K}=1500$', marker='v', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x21, y21,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='^', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x22, y22,color='none',label=r'$\beta=27, N_{\rm K}=350$', marker='o', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x23, y23,color='none',label=r'$\beta=27, N_{\rm K}=512$', marker='s', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x24, y24,color='none',label=r'$\beta=27, N_{\rm K}=848$', marker='D', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x25, y25,color='none',label=r'$\beta=27, N_{\rm K}=1500$', marker='v', edgecolor='#23BFE5', linewidth='4', s=1200)

# ax.plot(fit1a, fit1b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit2a, fit2b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit3a, fit3b,color='#FED001',label=r'',ls='-', linewidth=3)
# ax.plot(fit4a, fit4b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit5a, fit5b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit6a, fit6b,color='#FED001',label=r'',ls='-', linewidth=3)

plt.xlabel(r'$Wi_{\rm R}=\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\tau_{xy}^{\rm max}/G_{0}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
ax.tick_params(which='major', direction='in', length=11, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=6, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
ax.legend(loc='upper left', shadow=True, ncol=1, prop={'size': 60})
#ax.legend(loc='lower right', bbox_to_anchor=(1.4, 0), shadow=True, ncol=1, prop={'size': 40})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.73, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')

plt.xlim(0.01,1000)
plt.ylim(0.3,10)
#############################################################################################################################################################
ax = fig.add_subplot(1,5,2)

ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

# ax.scatter(x1, y1,color='none',label=r'$\beta=5, N_{\rm K}=244$', marker='^', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x2, y2,color='none',label=r'$\beta=5, N_{\rm K}=350$', marker='o', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x3, y3,color='none',label=r'$\beta=5, N_{\rm K}=512$', marker='s', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x4, y4,color='none',label=r'$\beta=5, N_{\rm K}=848$', marker='D', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x5, y5,color='none',label=r'$\beta=5, N_{\rm K}=1500$', marker='v', edgecolor='#FA8072', linewidth='4', s=1200)
ax.scatter(x6, y6,color='none',label=r'$\beta=9, N_{\rm K}=244$', marker='^', edgecolor='#708090', linewidth='4', s=1200)
ax.scatter(x7, y7,color='none',label=r'$\beta=9, N_{\rm K}=350$', marker='o', edgecolor='#708090', linewidth='4', s=1200)
ax.scatter(x8, y8,color='none',label=r'$\beta=9, N_{\rm K}=512$', marker='s', edgecolor='#708090', linewidth='4', s=1200)
ax.scatter(x9, y9,color='none',label=r'$\beta=9, N_{\rm K}=848$', marker='p', edgecolor='#708090', linewidth='4', s=1200)
ax.scatter(x10, y10,color='none',label=r'$\beta=9, N_{\rm K}=1500$', marker='v', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x11, y11,color='none',label=r'$\beta=14, N_{\rm K}=244$', marker='^', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x12, y12,color='none',label=r'$\beta=14, N_{\rm K}=350$', marker='o', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x13, y13,color='none',label=r'$\beta=14, N_{\rm K}=512$', marker='s', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x14, y14,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='D', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x15, y15,color='none',label=r'$\beta=14, N_{\rm K}=1500$', marker='v', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x16, y16,color='none',label=r'$\beta=20, N_{\rm K}=244$', marker='^', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x17, y17,color='none',label=r'$\beta=20, N_{\rm K}=350$', marker='o', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x18, y18,color='none',label=r'$\beta=20, N_{\rm K}=512$', marker='s', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x19, y19,color='none',label=r'$\beta=20, N_{\rm K}=848$', marker='D', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x20, y20,color='none',label=r'$\beta=20, N_{\rm K}=1500$', marker='v', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x21, y21,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='^', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x22, y22,color='none',label=r'$\beta=27, N_{\rm K}=350$', marker='o', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x23, y23,color='none',label=r'$\beta=27, N_{\rm K}=512$', marker='s', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x24, y24,color='none',label=r'$\beta=27, N_{\rm K}=848$', marker='D', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x25, y25,color='none',label=r'$\beta=27, N_{\rm K}=1500$', marker='v', edgecolor='#23BFE5', linewidth='4', s=1200)

# ax.plot(fit1a, fit1b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit2a, fit2b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit3a, fit3b,color='#FED001',label=r'',ls='-', linewidth=3)
# ax.plot(fit4a, fit4b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit5a, fit5b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit6a, fit6b,color='#FED001',label=r'',ls='-', linewidth=3)

plt.xlabel(r'$Wi_{\rm R}=\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\tau_{xy}^{\rm max}/G_{0}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
ax.tick_params(which='major', direction='in', length=11, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=6, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
ax.legend(loc='upper left', shadow=True, ncol=1, prop={'size': 60})
#ax.legend(loc='lower right', bbox_to_anchor=(1.4, 0), shadow=True, ncol=1, prop={'size': 40})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.73, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')

plt.xlim(0.01,1000)
plt.ylim(0.3,10)
#############################################################################################################################################################
ax = fig.add_subplot(1,5,3)

ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

# ax.scatter(x1, y1,color='none',label=r'$\beta=5, N_{\rm K}=244$', marker='^', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x2, y2,color='none',label=r'$\beta=5, N_{\rm K}=350$', marker='o', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x3, y3,color='none',label=r'$\beta=5, N_{\rm K}=512$', marker='s', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x4, y4,color='none',label=r'$\beta=5, N_{\rm K}=848$', marker='D', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x5, y5,color='none',label=r'$\beta=5, N_{\rm K}=1500$', marker='v', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x6, y6,color='none',label=r'$\beta=9, N_{\rm K}=244$', marker='^', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x7, y7,color='none',label=r'$\beta=9, N_{\rm K}=350$', marker='o', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x8, y8,color='none',label=r'$\beta=9, N_{\rm K}=512$', marker='s', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x9, y9,color='none',label=r'$\beta=9, N_{\rm K}=848$', marker='D', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x10, y10,color='none',label=r'$\beta=9, N_{\rm K}=1500$', marker='v', edgecolor='#708090', linewidth='4', s=1200)
ax.scatter(x11, y11,color='none',label=r'$\beta=14, N_{\rm K}=244$', marker='^', edgecolor='maroon', linewidth='4', s=1200)
ax.scatter(x12, y12,color='none',label=r'$\beta=14, N_{\rm K}=350$', marker='o', edgecolor='maroon', linewidth='4', s=1200)
ax.scatter(x13, y13,color='none',label=r'$\beta=14, N_{\rm K}=512$', marker='s', edgecolor='maroon', linewidth='4', s=1200)
ax.scatter(x14, y14,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='p', edgecolor='maroon', linewidth='4', s=1200)
ax.scatter(x15, y15,color='none',label=r'$\beta=14, N_{\rm K}=1500$', marker='v', edgecolor='maroon', linewidth='4', s=1200)
# ax.scatter(x16, y16,color='none',label=r'$\beta=20, N_{\rm K}=244$', marker='^', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x17, y17,color='none',label=r'$\beta=20, N_{\rm K}=350$', marker='o', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x18, y18,color='none',label=r'$\beta=20, N_{\rm K}=512$', marker='s', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x19, y19,color='none',label=r'$\beta=20, N_{\rm K}=848$', marker='D', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x20, y20,color='none',label=r'$\beta=20, N_{\rm K}=1500$', marker='v', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x21, y21,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='^', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x22, y22,color='none',label=r'$\beta=27, N_{\rm K}=350$', marker='o', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x23, y23,color='none',label=r'$\beta=27, N_{\rm K}=512$', marker='s', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x24, y24,color='none',label=r'$\beta=27, N_{\rm K}=848$', marker='D', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x25, y25,color='none',label=r'$\beta=27, N_{\rm K}=1500$', marker='v', edgecolor='#23BFE5', linewidth='4', s=1200)

# ax.plot(fit1a, fit1b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit2a, fit2b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit3a, fit3b,color='#FED001',label=r'',ls='-', linewidth=3)
# ax.plot(fit4a, fit4b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit5a, fit5b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit6a, fit6b,color='#FED001',label=r'',ls='-', linewidth=3)

plt.xlabel(r'$Wi_{\rm R}=\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\tau_{xy}^{\rm max}/G_{0}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
ax.tick_params(which='major', direction='in', length=11, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=6, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
ax.legend(loc='upper left', shadow=True, ncol=1, prop={'size': 60})
#ax.legend(loc='lower right', bbox_to_anchor=(1.4, 0), shadow=True, ncol=1, prop={'size': 40})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.73, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')

plt.xlim(0.01,1000)
plt.ylim(0.3,10)
#############################################################################################################################################################
ax = fig.add_subplot(1,5,4)

ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

# ax.scatter(x1, y1,color='none',label=r'$\beta=5, N_{\rm K}=244$', marker='^', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x2, y2,color='none',label=r'$\beta=5, N_{\rm K}=350$', marker='o', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x3, y3,color='none',label=r'$\beta=5, N_{\rm K}=512$', marker='s', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x4, y4,color='none',label=r'$\beta=5, N_{\rm K}=848$', marker='D', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x5, y5,color='none',label=r'$\beta=5, N_{\rm K}=1500$', marker='v', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x6, y6,color='none',label=r'$\beta=9, N_{\rm K}=244$', marker='^', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x7, y7,color='none',label=r'$\beta=9, N_{\rm K}=350$', marker='o', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x8, y8,color='none',label=r'$\beta=9, N_{\rm K}=512$', marker='s', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x9, y9,color='none',label=r'$\beta=9, N_{\rm K}=848$', marker='D', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x10, y10,color='none',label=r'$\beta=9, N_{\rm K}=1500$', marker='v', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x11, y11,color='none',label=r'$\beta=14, N_{\rm K}=244$', marker='^', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x12, y12,color='none',label=r'$\beta=14, N_{\rm K}=350$', marker='o', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x13, y13,color='none',label=r'$\beta=14, N_{\rm K}=512$', marker='s', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x14, y14,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='D', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x15, y15,color='none',label=r'$\beta=14, N_{\rm K}=1500$', marker='v', edgecolor='#FED001', linewidth='4', s=1200)
ax.scatter(x16, y16,color='none',label=r'$\beta=20, N_{\rm K}=244$', marker='^', edgecolor='mediumseagreen', linewidth='4', s=1200)
ax.scatter(x17, y17,color='none',label=r'$\beta=20, N_{\rm K}=350$', marker='o', edgecolor='mediumseagreen', linewidth='4', s=1200)
ax.scatter(x18, y18,color='none',label=r'$\beta=20, N_{\rm K}=512$', marker='s', edgecolor='mediumseagreen', linewidth='4', s=1200)
ax.scatter(x19, y19,color='none',label=r'$\beta=20, N_{\rm K}=848$', marker='p', edgecolor='mediumseagreen', linewidth='4', s=1200)
ax.scatter(x20, y20,color='none',label=r'$\beta=20, N_{\rm K}=1500$', marker='v', edgecolor='mediumseagreen', linewidth='4', s=1200)
# ax.scatter(x21, y21,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='^', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x22, y22,color='none',label=r'$\beta=27, N_{\rm K}=350$', marker='o', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x23, y23,color='none',label=r'$\beta=27, N_{\rm K}=512$', marker='s', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x24, y24,color='none',label=r'$\beta=27, N_{\rm K}=848$', marker='D', edgecolor='#23BFE5', linewidth='4', s=1200)
# ax.scatter(x25, y25,color='none',label=r'$\beta=27, N_{\rm K}=1500$', marker='v', edgecolor='#23BFE5', linewidth='4', s=1200)

# ax.plot(fit1a, fit1b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit2a, fit2b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit3a, fit3b,color='#FED001',label=r'',ls='-', linewidth=3)
# ax.plot(fit4a, fit4b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit5a, fit5b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit6a, fit6b,color='#FED001',label=r'',ls='-', linewidth=3)

plt.xlabel(r'$Wi_{\rm R}=\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\tau_{xy}^{\rm max}/G_{0}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
ax.tick_params(which='major', direction='in', length=11, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=6, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
ax.legend(loc='upper left', shadow=True, ncol=1, prop={'size': 60})
#ax.legend(loc='lower right', bbox_to_anchor=(1.4, 0), shadow=True, ncol=1, prop={'size': 40})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.73, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')

plt.xlim(0.01,1000)
plt.ylim(0.3,10)
#############################################################################################################################################################
ax = fig.add_subplot(1,5,5)

ax.plot(fit2x, fit2y,color='k',label=r'',ls='--', linewidth=3)

# ax.scatter(x1, y1,color='none',label=r'$\beta=5, N_{\rm K}=244$', marker='^', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x2, y2,color='none',label=r'$\beta=5, N_{\rm K}=350$', marker='o', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x3, y3,color='none',label=r'$\beta=5, N_{\rm K}=512$', marker='s', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x4, y4,color='none',label=r'$\beta=5, N_{\rm K}=848$', marker='D', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x5, y5,color='none',label=r'$\beta=5, N_{\rm K}=1500$', marker='v', edgecolor='#FA8072', linewidth='4', s=1200)
# ax.scatter(x6, y6,color='none',label=r'$\beta=9, N_{\rm K}=244$', marker='^', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x7, y7,color='none',label=r'$\beta=9, N_{\rm K}=350$', marker='o', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x8, y8,color='none',label=r'$\beta=9, N_{\rm K}=512$', marker='s', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x9, y9,color='none',label=r'$\beta=9, N_{\rm K}=848$', marker='D', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x10, y10,color='none',label=r'$\beta=9, N_{\rm K}=1500$', marker='v', edgecolor='#708090', linewidth='4', s=1200)
# ax.scatter(x11, y11,color='none',label=r'$\beta=14, N_{\rm K}=244$', marker='^', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x12, y12,color='none',label=r'$\beta=14, N_{\rm K}=350$', marker='o', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x13, y13,color='none',label=r'$\beta=14, N_{\rm K}=512$', marker='s', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x14, y14,color='none',label=r'$\beta=14, N_{\rm K}=848$', marker='D', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x15, y15,color='none',label=r'$\beta=14, N_{\rm K}=1500$', marker='v', edgecolor='#FED001', linewidth='4', s=1200)
# ax.scatter(x16, y16,color='none',label=r'$\beta=20, N_{\rm K}=244$', marker='^', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x17, y17,color='none',label=r'$\beta=20, N_{\rm K}=350$', marker='o', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x18, y18,color='none',label=r'$\beta=20, N_{\rm K}=512$', marker='s', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x19, y19,color='none',label=r'$\beta=20, N_{\rm K}=848$', marker='D', edgecolor='#64F0A4', linewidth='4', s=1200)
# ax.scatter(x20, y20,color='none',label=r'$\beta=20, N_{\rm K}=1500$', marker='v', edgecolor='#64F0A4', linewidth='4', s=1200)
ax.scatter(x21, y21,color='none',label=r'$\beta=27, N_{\rm K}=244$', marker='^', edgecolor='dodgerblue', linewidth='4', s=1200)
ax.scatter(x22, y22,color='none',label=r'$\beta=27, N_{\rm K}=350$', marker='o', edgecolor='dodgerblue', linewidth='4', s=1200)
ax.scatter(x23, y23,color='none',label=r'$\beta=27, N_{\rm K}=512$', marker='s', edgecolor='dodgerblue', linewidth='4', s=1200)
ax.scatter(x24, y24,color='none',label=r'$\beta=27, N_{\rm K}=848$', marker='p', edgecolor='dodgerblue', linewidth='4', s=1200)
ax.scatter(x25, y25,color='none',label=r'$\beta=27, N_{\rm K}=1500$', marker='v', edgecolor='dodgerblue', linewidth='4', s=1200)

# ax.plot(fit1a, fit1b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit2a, fit2b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit3a, fit3b,color='#FED001',label=r'',ls='-', linewidth=3)
# ax.plot(fit4a, fit4b,color='#FA8072',label=r'',ls='-', linewidth=3)
# ax.plot(fit5a, fit5b,color='#708090',label=r'',ls='-', linewidth=3)
# ax.plot(fit6a, fit6b,color='#FED001',label=r'',ls='-', linewidth=3)

plt.xlabel(r'$Wi_{\rm R}=\dot{\gamma}\tau_{\rm R}$',fontsize=90)
plt.ylabel(r'$\tau_{xy}^{\rm max}/G_{0}$',fontsize=90)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
plt.xscale('log')
plt.yscale('log')
ax.tick_params(which='major', direction='in', length=11, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=6, axis='both', colors='k', pad=35)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
ax.legend(loc='upper left', shadow=True, ncol=1, prop={'size': 60})
#ax.legend(loc='lower right', bbox_to_anchor=(1.4, 0), shadow=True, ncol=1, prop={'size': 40})

textstr1 = '\n'.join((r'$\angle 0.33$',))
plt.text(0.87, 0.73, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')

plt.xlim(0.01,1000)
plt.ylim(0.3,10)
##############################################################################################################################
#ax.label_outer()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(150, 24)
fig.savefig('tauxymaxG0-WiR.eps', dpi=300, bbox_inches='tight')
#plt.show()
