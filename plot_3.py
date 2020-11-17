# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:06:05 2019

@author: yadav
"""

# code to plot 
import math
import cmath
import numpy
import matplotlib    #pylab is submodule in matplotlib
#import matplotlib.pylab 
#import pylab    # Use this step to run in anaconda
data1 = numpy.loadtxt("input_output_files/alpha_8.0_rho_2.0/gamma_0.8/density/JcSaiter11_corrected3.TXT",float)
#data2 = numpy.loadtxt("input_output_files/alpha_0.5_rho_2.0/density/JcSa_corrected2.TXT",float)
#data3 = numpy.loadtxt("input_output_files/alpha_0.8_rho_2.0/density/JcSa_corrected2.TXT",float)

x1 = data1[:,0]    # The plain [:] operator slices from beginning to end-1, Eg. a[:,0:n] gives all the rows from 0th column to n-1 column 
y1 = data1[:,1]
#x2 = data2[:,0]    # The plain [:] operator slices from beginning to end-1, Eg. a[:,0:n] gives all the rows from 0th column to n-1 column 
#y2 = data2[:,1]
#x3 = data3[:,0]    # The plain [:] operator slices from beginning to end-1, Eg. a[:,0:n] gives all the rows from 0th column to n-1 column 
#y3 = data3[:,1]
#x2 = data[:,2]    # The plain [:] operator slices from beginning to end-1, Eg. a[:,0:n] gives all the rows from 0th column to n-1 column 


matplotlib.pylab.scatter(x1,y1, s=40, c="r", marker="v", label=r"$\alpha=0.125$")
#matplotlib.pylab.scatter(x2,y2, s=40,c="g", marker="s", label=r"$\alpha=0.5$")
#matplotlib.pylab.scatter(x3,y3, s=40,c="b", marker="o", label=r"$\alpha=0.8$")
#matplotlib.axes.Axes.axhline(linestyle='--', color='k')
matplotlib.pylab.axhline(y=0, linestyle='--',  color='k')
#matplotlib.pylab.xlim(0.5,1)
matplotlib.pylab.ylim(-0.002,0.012)
matplotlib.pylab.ylabel(r'$a(\gamma$)')
matplotlib.pylab.xlabel(r'$\gamma$')
matplotlib.pylab.legend(loc='upper right', prop={'size': 12})
#matplotlib.pylab.legend(loc=1, prop={'size': 6})
matplotlib.pylab.savefig('input_output_files/alpha_8.0_rho_2.0/figures/for_publication/JcSa_transition_pub1_corrected3_all_iter11.pdf')
matplotlib.pylab.savefig('input_output_files/alpha_8.0_rho_2.0/figures/for_publication/JcSa_transition_pub1_corrected3_all_iter11.eps', format='eps', dpi=1000)
matplotlib.pylab.show()

#matplotlib.pylab.scatter(x2,y)
##matplotlib.pylab.xlim(0.15,0.35)
##matplotlib.pylab.ylim(-0.005,0.015)
#matplotlib.pylab.ylabel(r'$a(\gamma$)')
#matplotlib.pylab.xlabel(r'$1-\gamma$')
##matplotlib.pylab.legend(loc='upper right', prop={'size': 6})
#matplotlib.pylab.legend(loc=1, prop={'size': 6})
#matplotlib.pylab.savefig('input_output_files/alpha_0.5_rho_2.0/figures/for_publication/JcSa_transition_pub2_corrected2.pdf')
#matplotlib.pylab.savefig('input_output_files/alpha_0.5_rho_2.0/figures/for_publication/JcSa_transition_pub2_corrected2.eps', format='eps', dpi=1000)
#matplotlib.pylab.show()
