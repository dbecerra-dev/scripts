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
from scipy.optimize import curve_fit
from scipy import optimize
from uncertainties import ufloat
from uncertainties.umath import *  # sin(), etc.

######################################################################################
######################################################################################
######################################################################################
x1=[]
y1=[]
y1err=[]
y1erro=[]
err1=[]
with open('./data-pref_exp/data-prefactor','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            x1.append(float(row[1]))
            y1.append(float(row[2]))
            err1.append(float(row[3]))
            y1err.append(float(row[3])*np.sqrt(1/(float(row[2]))**2))
            y1erro.append(1/float(row[2])*(float(row[3])*np.sqrt(1/(float(row[2]))**2)))

x2=[]
y2=[]
y2err=[]
y2erro=[]
err2=[]
with open('./data-pref_exp/data-exponent','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            x2.append(float(row[1]))
            y2.append(float(row[2]))
            err2.append(float(row[3]))

#################################################################################################
# #Fitting for the prefactor by using optimize.leastsq
#
# powerlaw = lambda x, amp, index: amp * (x**index)
#
# xdata = np.array(x1)
# ydata = np.array(y1)
# yerr = np.array(y1err)
#
# logx = np.log10(x1)
# logy = np.log10(y1)
# logyerr = np.log10(y1err)
#
# fitfunc = lambda p, x: p[0] + p[1] * x
# errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err
#
# pinit = [1.0, 1.0]
# out = optimize.leastsq(errfunc, pinit,
#                        args=(logx, logy, logyerr), full_output=1)
#
#
# pfinal = out[0]
# covar = out[1]
#
# amp1 = 10.0**pfinal[0]
# index1 = pfinal[1]
#
#
# stdevp1 = np.sqrt(np.diag(covar))
#
# print 'Fitting for the Prefactor by using optimize.leastsq'
# print 'prefactor=',amp1,', exponent=', index1
# print 'stdevs prefactor=',10**stdevp1[0],', stdevs exponent=',stdevp1[1]
# print ''
#################################################################################################
#Fitting for the prefactor by using curve_fit

powerlaw = lambda x, amp, index: amp * (x**index)

logx1 = np.log(x1)
logy1 = np.log(y1)
logyerr = (y1err)

def model(x, a, b):
   return a + b * x

pars, cov = curve_fit(f=model, xdata=logx1, ydata=logy1, p0=[0, 0], sigma=logyerr, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdevp2 = np.sqrt(np.diag(cov))

amp2 = pars[0]
index2 = pars[1]

print 'Fitting for the PREFACTOR by using curve_fit'
print 'prefactor=',amp2,', exponent=', index2
print 'stdevs prefactor=',stdevp2[0],', stdevs exponent=',stdevp2[1]
print ''
#################################################################################################
# #Fitting for the Exponent by using optimize.leastsq
#
# linear = lambda x, slope, coeff:  slope*x+coeff
#
# xdata = np.array(x2)
# ydata = np.array(y2)
# yerr = np.array(y2err)
#
# fitfunc = lambda p, x: p[0] + p[1] * x
# errfunc = lambda p, x, y, err: (y - fitfunc(p, x)) / err
#
# pinit = [1.0, 1.0]
# out = optimize.leastsq(errfunc, pinit,
#                        args=(xdata, ydata, yerr), full_output=1)
#
# pfinal = out[0]
# covar = out[1]
#
# coeff1 = pfinal[0]
# slope1 = pfinal[1]
#
# stdeve1 = np.sqrt(np.diag(covar))
#
# print 'Fitting for the EXPONENT by using optimize.leastsq'
# print 'coeff=', coeff1, 'slope=',slope1
# print 'stdevs coeff=',stdeve1[0],'stdevs slope=',stdeve1[1]
# print ''
#################################################################################################
#Fitting for the Exponent by using curve_fit

linear = lambda x, slope, coeff:  slope*x+coeff

xdata = np.array(x2)
ydata = np.array(y2)
yerr = np.array(err2)

def model(x, a, b):
   return a + b * x

pars, cov = curve_fit(f=model, xdata=xdata, ydata=ydata, p0=[0, 0], sigma=yerr, absolute_sigma=True, bounds=(-np.inf, np.inf))

stdeve2 = np.sqrt(np.diag(cov))

coeff2 = pars[0]
slope2 = pars[1]

print 'Fitting for the EXPONENT by using curve_fit'
print 'coeff=', coeff2, 'slope=',slope2
print 'stdevs coeff=',stdeve2[0],'stdevs slope=',stdeve2[1]
print ''
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################
fig = plt.figure()

fig.subplots_adjust(hspace=0.3,wspace=0.05)
Nk = np.linspace(0, 2500)
#############################################################################################################################################################
ax = fig.add_subplot(1,2,1)

ax.plot(Nk, powerlaw(Nk, np.exp(amp2), index2),color='darkblue',label=r'${\rm Prefactor}=(%7.3f\pm 0.01431)N_{\rm K}^{%7.3f\pm%7.3f}$' % (np.exp(amp2),index2,stdevp2[1]),ls='--', linewidth=3)
ax.scatter(x1, y1,color='none',label=r'', marker='s', edgecolor='darkblue', linewidth='4', s=1600)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'

ax.errorbar(x1,y1,yerr=err1,errorevery=1,linestyle='None',ecolor='darkblue',capsize=5, elinewidth=3,capthick=3)

plt.xlabel(r'$N_{\rm K}$',fontsize=110)
plt.ylabel(r'${\rm Prefactor}$', color='k', fontsize=110)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
#plt.xscale('log')
#plt.yscale('log')
#plt.tick_params(axis='y', colors='r')
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
ax.tick_params(which='major', direction='in', length=20, axis='both', colors='k', pad=45)
ax.tick_params(which='minor', direction='in', length=10, axis='both', colors='k', pad=45)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
#ax.legend(loc='upper left', bbox_to_anchor=(1.5, 0), shadow=True, ncol=1, prop={'size': 40})
ax.legend(loc='upper left', shadow=True, ncol=1, prop={'size': 56})

#textstr1 = '\n'.join((r'$\angle 0.33$',))
#plt.text(0.86, 0.85, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')
ax.xaxis.set_ticks(np.arange(0, 1600.01, 200))
plt.xlim(0,1600)
plt.ylim(0,250000)
#########################################################################################f####################################################################
ax = fig.add_subplot(1,2,2)

ax.plot(Nk, linear(Nk, slope2, coeff2),color='darkred',label=r'${\rm Exp.}=(%7.6f\pm%7.6f)N_{\rm K}+(%7.3f\pm%7.3f)$' % (slope2,stdeve2[1],coeff2,stdeve2[0]), ls='--', linewidth=3)
ax.scatter(x2, y2,color='none',label=r'', marker='o', edgecolor='darkred', linewidth='4', s=1600)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'

ax.errorbar(x2,y2,yerr=err2,errorevery=1,linestyle='None',ecolor='darkred',capsize=5, elinewidth=3,capthick=3)

plt.xlabel(r'$N_{\rm K}$',fontsize=110)
plt.ylabel(r'${\rm Exponent}$', color='k', fontsize=110)
plt.xticks(fontsize=90)
plt.yticks(fontsize=90)
#plt.xscale('log')
#plt.yscale('log')
#plt.tick_params(axis='y', colors='r')
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
ax.tick_params(which='major', direction='in', length=20, axis='both', colors='k', pad=45)
ax.tick_params(which='minor', direction='in', length=10, axis='both', colors='k', pad=45, labelsize=45)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
#ax.legend(loc='upper left', bbox_to_anchor=(1.5, 0), shadow=True, ncol=1, prop={'size': 40})
ax.legend(loc='upper left', shadow=True, ncol=1, prop={'size': 56})

#textstr1 = '\n'.join((r'$\angle 0.33$',))
#plt.text(0.86, 0.85, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')
#ax.xaxis.set_ticks(np.arange(0, 30.01, 5))
plt.xlim(0,1600)
plt.ylim(0.5,0.8)
#############################################################################################################################################################

#############################################################################################################################################################

#############################################################################################################################################################

#############################################################################################################################################################

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#ax.label_outer()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(65, 30)
fig.savefig('prefactorexp-nk.eps', dpi=300, bbox_inches='tight')
#plt.show()
