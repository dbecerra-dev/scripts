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
def lighten_color(color, amount=0.5):
    """
    Lightens the given color by multiplying (1-luminosity) by the given amount.
    Input can be matplotlib color string, hex string, or RGB Tuple.

    Examples:
    >> lighten_color('g', 0.3)
    >> lighten_color('#F034A3', 0.6)
    >> lighten_color((.3,.55,.1), 0.5)
    """
    import matplotlib.colors as mc
    import colorsys
    try:
        c = mc.cnames[color]
    except:
        c = color
    c = colorsys.rgb_to_hls(*mc.to_rgb(c))
    return colorsys.hls_to_rgb(c[0], 1 - amount * (1 - c[1]), c[2])
######################################################################################
######################################################################################
x1=[]
y1=[]
with open('./data-nk/data-nk244','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            x1.append(float(row[1]))
            y1.append(float(row[2]))

x2=[]
y2=[]
with open('./data-nk/data-nk350','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            x2.append(float(row[1]))
            y2.append(float(row[2]))

x3=[]
y3=[]
with open('./data-nk/data-nk512','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            x3.append(float(row[1]))
            y3.append(float(row[2]))

x4=[]
y4=[]
with open('./data-nk/data-nk848','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            x4.append(float(row[1]))
            y4.append(float(row[2]))

x5=[]
y5=[]
with open('./data-nk/data-nk1500','r') as csvfile:
    #line1,line2,line3= next(csvfile),next(csvfile),next(csvfile)
    for line in csvfile:
        plots=csv.reader(csvfile, delimiter='\t')
        for row in plots:
            x5.append(float(row[1]))
            y5.append(float(row[2]))
#################################################################################################
powerlaw = lambda x, amp, index: amp * (x**index)
#################################################################################################
logx1 = np.log10(x1)
logy1 = np.log10(y1)

def model(x, a, b):
   return a + b * x

pars, cov = curve_fit(f=model, xdata=logx1, ydata=logy1, p0=[0, 0], bounds=(-np.inf, np.inf))

stdevs1 = np.sqrt(np.diag(cov))

amp1 = 10.0**pars[0]
index1 = pars[1]

print 'Linearizing data for Nk=244'
print 'prefactor=',amp1,', exponent=', index1
print 'stdevs prefactor=',10**stdevs1[0],', stdevs exponent=',stdevs1[1]
#################################################################################################
logx2 = np.log10(x2)
logy2 = np.log10(y2)

def model(x, a, b):
   return a + b * x

pars, cov = curve_fit(f=model, xdata=logx2, ydata=logy2, p0=[0, 0], bounds=(-np.inf, np.inf))

stdevs2 = np.sqrt(np.diag(cov))

amp2 = 10.0**pars[0]
index2 = pars[1]

print 'Linearizing data for Nk=244'
print 'prefactor=',amp2,', exponent=', index2
print 'stdevs prefactor=',10**stdevs2[0],', stdevs exponent=',stdevs2[1]
#################################################################################################
logx3 = np.log10(x3)
logy3 = np.log10(y3)

def model(x, a, b):
   return a + b * x

pars, cov = curve_fit(f=model, xdata=logx3, ydata=logy3, p0=[0, 0], bounds=(-np.inf, np.inf))

stdevs3 = np.sqrt(np.diag(cov))

amp3 = 10.0**pars[0]
index3 = pars[1]

print 'Linearizing data for Nk=244'
print 'prefactor=',amp3,', exponent=', index3
print 'stdevs prefactor=',10**stdevs3[0],', stdevs exponent=',stdevs3[1]
#################################################################################################
logx4 = np.log10(x4)
logy4 = np.log10(y4)

def model(x, a, b):
   return a + b * x

pars, cov = curve_fit(f=model, xdata=logx4, ydata=logy4, p0=[0, 0], bounds=(-np.inf, np.inf))

stdevs4 = np.sqrt(np.diag(cov))

amp4 = 10.0**pars[0]
index4 = pars[1]

print 'Linearizing data for Nk=244'
print 'prefactor=',amp4,', exponent=', index4
print 'stdevs prefactor=',10**stdevs4[0],', stdevs exponent=',stdevs4[1]
#################################################################################################
logx5 = np.log10(x5)
logy5 = np.log10(y5)

def model(x, a, b):
   return a + b * x

pars, cov = curve_fit(f=model, xdata=logx5, ydata=logy5, p0=[0, 0], bounds=(-np.inf, np.inf))

stdevs5 = np.sqrt(np.diag(cov))

amp5 = 10.0**pars[0]
index5 = pars[1]

print 'Linearizing data for Nk=244'
print 'prefactor=',amp5,', exponent=', index5
print 'stdevs prefactor=',10**stdevs5[0],', stdevs exponent=',stdevs5[1]
#############################################################################################################################################################
Zclist = [11, 40, 100, 160]
x11=[]
y11=[]
x40=[]
y40=[]
x100=[]
y100=[]
x160=[]
y160=[]
y11m=[]
y40m=[]
y100m=[]
y160m=[]
y11p=[]
y40p=[]
y100p=[]
y160p=[]
# Using for loop
for Zc in Zclist:
    #print(Zc)
    for beta in range(1,31):                      # Number of monomers per chain (insert a number from properties.ods)
        Z=((0.823*Zc+0.515)-1)/0.74+1
        NK=Z*(beta+1)-beta
        tauRfsmtauc=0.085*NK**(2.026)*beta**(0.000077*NK+0.58)/(0.265*beta**(2.666666667))
        error=math.sqrt(0.000198848*NK**(4.05137)*beta**(-4.16579+0.000154703*NK)+0.000630846*NK**(4.05136)*beta**(-4.16579+0.000154703*NK)*math.log(NK)**2+0.000115917*NK**(4.05137)*beta**(-4.16579+0.000154703*NK)*math.log(beta)**2+0.000000000155897*NK**(6.05136)*beta**(-4.16579+0.000154703*NK)*math.log(beta)**2)
        tauRfsmtaucminus=(0.085*NK**(2.026)*beta**(0.000077*NK+0.58)/(0.265*beta**(2.666666667)))-error
        tauRfsmtaucplus=(0.085*NK**(2.026)*beta**(0.000077*NK+0.58)/(0.265*beta**(2.666666667)))+error
        # tauRfsmtauc=0.085*NK**(2.026)*beta**(0.000077*NK+0.58)
        # error=math.sqrt(0.0000139641*NK**(4.05137)*beta**(1.16754+0.000154703*NK)+0.0000443011*NK**(4.05136)*beta**(1.16754+0.000154703*NK)*math.log(NK)**2+0.00000814029*NK**(4.05137)*beta**(1.16754+0.000154703*NK)*math.log(beta)**2+0.0000000000109478*NK**(6.05136)*beta**(1.16754+0.000154703*NK)*math.log(beta)**2)
        # tauRfsmtaucminus=(0.085*NK**(2.026)*beta**(0.000077*NK+0.58))-error
        # tauRfsmtaucplus=(0.085*NK**(2.026)*beta**(0.000077*NK+0.58))+error
        if Zc==11:
            x11.append(float(beta))
            y11.append(float(tauRfsmtauc))
            y11m.append(float(tauRfsmtaucminus))
            y11p.append(float(tauRfsmtaucplus))
        if Zc==40:
            x40.append(float(beta))
            y40.append(float(tauRfsmtauc))
            y40m.append(float(tauRfsmtaucminus))
            y40p.append(float(tauRfsmtaucplus))
        if Zc==100:
            x100.append(float(beta))
            y100.append(float(tauRfsmtauc))
            y100m.append(float(tauRfsmtaucminus))
            y100p.append(float(tauRfsmtaucplus))
        if Zc==160:
            x160.append(float(beta))
            y160.append(float(tauRfsmtauc))
            y160m.append(float(tauRfsmtaucminus))
            y160p.append(float(tauRfsmtaucplus))

x11a_smooth = np.linspace(min(x11),max(x11),10000)
spl = make_interp_spline(x11, y11, k=3)
y11a_smooth = spl(x11a_smooth)

x40a_smooth = np.linspace(min(x40),max(x40),10000)
spl = make_interp_spline(x40, y40, k=3)
y40a_smooth = spl(x40a_smooth)

x100a_smooth = np.linspace(min(x100),max(x100),10000)
spl = make_interp_spline(x100, y100, k=3)
y100a_smooth = spl(x100a_smooth)

x160a_smooth = np.linspace(min(x160),max(x160),10000)
spl = make_interp_spline(x160, y160, k=3)
y160a_smooth = spl(x160a_smooth)
#############################################################################################################################################################
Zclist = [11, 40, 100, 160]
x11=[]
y11=[]
x40=[]
y40=[]
x100=[]
y100=[]
x160=[]
y160=[]
# Using for loop
for Zc in Zclist:
    #print(Zc)
    for beta in range(1,31):                      # Number of monomers per chain (insert a number from properties.ods)
        Z=((0.823*Zc+0.515)-1)/0.74+1
        NK=Z*(beta+1)-beta
        Nc=Zc*2-1
        tauRfsmtauc=0.085*NK**(2.026)*beta**(0.000077*NK+0.58)/(0.265*beta**(2.666666667))
        tauRcfsmtauc=0.321974*(-0.310811+2.22432*Zc)**2.02568
        #tauRcfsmtauc=0.085*NK**(2.026)*1**(0.000077*NK+0.58)/(0.265*1**(2.666666667))
        ejey=abs(tauRfsmtauc-tauRcfsmtauc)/float(tauRfsmtauc)

        if Zc==11:
            x11.append(float(beta))
            y11.append(float(ejey))
        if Zc==40:
            x40.append(float(beta))
            y40.append(float(ejey))
        if Zc==100:
            x100.append(float(beta))
            y100.append(float(ejey))
        if Zc==160:
            x160.append(float(beta))
            y160.append(float(ejey))


x11b_smooth = np.linspace(min(x11),max(x11),10000)
spl = make_interp_spline(x11, y11, k=3)
y11b_smooth = spl(x11b_smooth)

x40b_smooth = np.linspace(min(x40),max(x40),10000)
spl = make_interp_spline(x40, y40, k=3)
y40b_smooth = spl(x40b_smooth)

x100b_smooth = np.linspace(min(x100),max(x100),10000)
spl = make_interp_spline(x100, y100, k=3)
y100b_smooth = spl(x100b_smooth)

x160b_smooth = np.linspace(min(x160),max(x160),10000)
spl = make_interp_spline(x160, y160, k=3)
y160b_smooth = spl(x160b_smooth)
#############################################################################################################################################################
fig = plt.figure()

fig.subplots_adjust(hspace=0,wspace=0.05)
Nk=np.linspace(0,30)
#############################################################################################################################################################
ax = fig.add_subplot(2,1,1)

ax.plot(Nk, powerlaw(Nk, amp1, index1),color='#FA8072',label=r'$N_{\rm K}=244, \tau_{\rm R}/\tau_{\rm K}=(5.6\times10^{3}\pm1.2){{\beta}}^{0.6\pm0.066}$',ls='-', linewidth=5)
ax.plot(Nk, powerlaw(Nk, amp2, index2),color='#708090',label=r'$N_{\rm K}=350, \tau_{\rm R}/\tau_{\rm K}=(1.2\times10^{4}\pm1.1){{\beta}}^{0.61\pm0.052}$',ls='-', linewidth=5)
ax.plot(Nk, powerlaw(Nk, amp3, index3),color='maroon',label=r'$N_{\rm K}=512, \tau_{\rm R}/\tau_{\rm K}=(2.6\times10^{4}\pm1.1){{\beta}}^{0.63\pm0.025}$',ls='-', linewidth=5)
ax.plot(Nk, powerlaw(Nk, amp4, index4),color='mediumseagreen',label=r'$N_{\rm K}=848, \tau_{\rm R}/\tau_{\rm K}=(7.5\times10^{4}\pm1.1){{\beta}}^{0.64\pm0.021}$',ls='-', linewidth=5)
ax.plot(Nk, powerlaw(Nk, amp5, index5),color='dodgerblue',label=r'$N_{\rm K}=1500, \tau_{\rm R}/\tau_{\rm K}=(2.2\times10^{5}\pm1.1){{\beta}}^{0.70\pm0.036}$',ls='-', linewidth=5)

ax.scatter(x1, y1,color='none',label=r'', marker='^', edgecolor='#FA8072', linewidth='5', s=2000)    #r'${\rm FSM}, \beta=5, N_{\rm K}=244, \langle Z\rangle=42$'
ax.scatter(x2, y2,color='none',label=r'', marker='o', edgecolor='#708090', linewidth='5', s=2000)    #r'${\rm FSM}, \beta=5, N_{\rm K}=512, \langle Z\rangle=86$'
ax.scatter(x3, y3,color='none',label=r'', marker='s', edgecolor='maroon', linewidth='5', s=2000) #r'${\rm FSM}, \beta=5, N_{\rm K}=848, \langle Z\rangle=142$'
ax.scatter(x4, y4,color='none',label=r'', marker='p', edgecolor='mediumseagreen', linewidth='5', s=2000)   #r'${\rm FSM}, \beta=14, N_{\rm K}=244, \langle Z\rangle=17$'
ax.scatter(x5, y5,color='none',label=r'', marker='v', edgecolor='dodgerblue', linewidth='5', s=2000)   #r'${\rm FSM}, \beta=14, N_{\rm K}=512, \langle Z\rangle=35$'

# plt.xlabel(r'${\beta}$',fontsize=120)
plt.ylabel(r'$\tau_{\rm R}/\tau_{\rm K}$',fontsize=120)
plt.xticks(fontsize=100)
plt.yticks(fontsize=100)
plt.xscale('log')
plt.yscale('log')
#plt.tick_params(axis='y', colors='r')
#ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
ax.tick_params(which='major', direction='in', length=30, axis='x', colors='k', pad=35, labelsize=0)
ax.tick_params(which='minor', direction='in', length=20, axis='x', colors='k', pad=35, labelsize=0)
ax.tick_params(which='major', direction='in', length=30, axis='y', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=20, axis='y', colors='k', pad=35, labelsize=75)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
#ax.legend(loc='upper left', bbox_to_anchor=(1.5, 0), shadow=True, ncol=1, prop={'size': 40})
ax.legend(loc='upper left', shadow=True, ncol=1, prop={'size': 60})

#textstr1 = '\n'.join((r'$\angle 0.33$',))
#plt.text(0.86, 0.85, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')
#ax.xaxis.set_ticks(np.arange(0, 30.01, 5))
plt.xlim(3.01,30)
plt.ylim(10000,30000000)
#############################################################################################################################################################
ax = fig.add_subplot(2,1,2)

ax.plot(x11a_smooth, y11a_smooth,color='goldenrod',label=r'$\langle Z_{c}\rangle=11$',ls='-', linewidth=5)
ax.plot(x40a_smooth, y40a_smooth,color='indianred',label=r'$\langle Z_{c}\rangle=40$',ls='-', linewidth=5)
#ax.plot(x100a_smooth, y100a_smooth,color='#FED001',label=r'$\langle Z_{c}\rangle=100$',ls='-', linewidth=3)
ax.plot(x160a_smooth, y160a_smooth,color='cadetblue',label=r'$\langle Z_{c}\rangle=160$',ls='-', linewidth=5)

# ax.plot(Nk, powerlaw(Nk, amp1, index1),color='#FA8072',label=r'$N_{\rm K}=244, \tau_{\rm R}/\tau_{\rm K}=(%7.3f\pm%7.3f){{\beta}}^{%7.3f\pm%7.3f}$' % (amp1,10**stdevs1[0],index1,stdevs1[1]),ls='--', linewidth=3)
# ax.plot(Nk, powerlaw(Nk, amp2, index2),color='#708090',label=r'$N_{\rm K}=350, \tau_{\rm R}/\tau_{\rm K}=(%7.3f\pm%7.3f){{\beta}}^{%7.3f\pm%7.3f}$' % (amp2,10**stdevs2[0],index2,stdevs2[1]),ls='--', linewidth=3)
# ax.plot(Nk, powerlaw(Nk, amp3, index3),color='#FED001',label=r'$N_{\rm K}=512, \tau_{\rm R}/\tau_{\rm K}=(%7.3f\pm%7.3f){{\beta}}^{%7.3f\pm%7.3f}$' % (amp3,10**stdevs3[0],index3,stdevs3[1]),ls='--', linewidth=3)
# ax.plot(Nk, powerlaw(Nk, amp4, index4),color='#64F0A4',label=r'$N_{\rm K}=848, \tau_{\rm R}/\tau_{\rm K}=(%7.3f\pm%7.3f){{\beta}}^{%7.3f\pm%7.3f}$' % (amp4,10**stdevs4[0],index4,stdevs4[1]),ls='--', linewidth=3)
# ax.plot(Nk, powerlaw(Nk, amp5, index5),color='#23BFE5',label=r'$N_{\rm K}=1500, \tau_{\rm R}/\tau_{\rm K}=(%7.3f\pm%7.3f){{\beta}}^{%7.3f\pm%7.3f}$' % (amp5,10**stdevs5[0],index5,stdevs5[1]),ls='--', linewidth=3)

#map_objectminus = map(operator.sub, y2, yerr2)
#y2minus = list(map_objectminus)
#map_objectplus = map(operator.add, y2, yerr2)
#y2plus = list(map_objectplus)
plt.fill_between(x11, y11m, y11p,alpha=0.001, edgecolor='goldenrod', facecolor=lighten_color('goldenrod',0.4))
plt.fill_between(x40, y40m, y40p,alpha=0.001, edgecolor='indianred', facecolor=lighten_color('indianred',0.4))
#plt.fill_between(x100, y100m, y100p,alpha=0.001, edgecolor='#FED001', facecolor=lighten_color('#FED001',0.4))
plt.fill_between(x160, y160m, y160p,alpha=0.001, edgecolor='cadetblue', facecolor=lighten_color('cadetblue',0.4))

# ax.errorbar(x2,y2,yerr=yerr2,errorevery=8,linestyle='None',ecolor='#00008B',capsize=5)
# ax.errorbar(x2,y2,yerr=yerr2,errorevery=1,linestyle='None',ecolor='#FF0000',capsize=5)
# ax.errorbar(x3,y3,yerr=yerr3,errorevery=1,linestyle='None',ecolor='#8B008B',capsize=5)
# ax.errorbar(x4,y4,yerr=yerr4,errorevery=1,linestyle='None',ecolor='#006400',capsize=5)


plt.xlabel(r'${\beta}$',fontsize=120)
plt.ylabel(r'$\tau_{\rm R}/\tau_{\rm c}$',fontsize=120)
plt.xticks(fontsize=100)
plt.yticks(fontsize=100)
plt.xscale('log')
plt.yscale('log')
#plt.tick_params(axis='y', colors='r')
# ax.xaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
# ax.xaxis.set_minor_formatter(mtick.FormatStrFormatter('$%0.0f$'))
#ax.yaxis.set_major_formatter(mtick.FormatStrFormatter('%0.1f'))
ax.tick_params(which='major', direction='in', length=30, axis='both', colors='k', pad=35)
ax.tick_params(which='minor', direction='in', length=20, axis='both', colors='k', pad=35, labelsize=75)
ax.yaxis.set_ticks_position('both')
ax.xaxis.set_ticks_position('both')
plt.legend()
chartBox = ax.get_position()
ax.set_position([chartBox.x0, chartBox.y0, chartBox.width*0.8, chartBox.height])
#ax.legend(loc='upper left', bbox_to_anchor=(1.5, 0), shadow=True, ncol=1, prop={'size': 40})
ax.legend(loc='upper left', shadow=True, ncol=1, prop={'size': 65})

#textstr1 = '\n'.join((r'$\angle 0.33$',))
#plt.text(0.86, 0.85, textstr1, transform=ax.transAxes, fontsize=60, verticalalignment='top')
# ax.xaxis.set_ticks(np.arange(10, 30.01, 10))
plt.xlim(3.01,30)
plt.ylim(10,800000)
#############################################################################################################################################################

#############################################################################################################################################################

#############################################################################################################################################################

#############################################################################################################################################################

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

#ax.label_outer()
fig = matplotlib.pyplot.gcf()
fig.set_size_inches(35, 65)
fig.savefig('fit.eps', dpi=300, bbox_inches='tight')
#plt.show()
