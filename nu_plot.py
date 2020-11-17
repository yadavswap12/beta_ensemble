# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:10:42 2018

@author: yadav
"""


# code to plot nu
import math
import cmath
import numpy
import matplotlib    #pylab is submodule in matplotlib
#import matplotlib.pylab 
#import pylab    # Use this step to run in anaconda
data1 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_3.0/density/renormalized_potential_from_f2_y_method_2_gamma=3.0_max_err_1e-10_theta=1.0001_18000points_correction4_iter13.0.txt",float)
data2 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.1/gamma_3.0/density/renormalized_potential_from_f2_y_method_2_gamma=3.0_max_err_1e-10_theta=1.1_18000points_correction4_iter19.0_with_alpha.txt",float)
data3 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.01/gamma_3.0/density/renormalized_potential_from_f2_y_method_2_gamma=3.0_max_err_1e-10_theta=1.01_18000points_correction4_iter12.0.txt",float)
data4 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.06/gamma_3.0/density/renormalized_potential_from_f2_y_method_2_gamma=3.0_max_err_1e-10_theta=1.06_18000points_correction4_iter10.0.txt",float)


x1 = data1[:,0]    # The plain [:] operator slices from beginning to end-1, Eg. a[:,0:n] gives all the rows from 0th column to n-1 column 
y1 = data1[:,1]
#y1 = data1[:,1]*10**10
x2 = data2[:,0]    # The plain [:] operator slices from beginning to end-1, Eg. a[:,0:n] gives all the rows from 0th column to n-1 column 
y2 = data2[:,1]
x3 = data3[:,0]    # The plain [:] operator slices from beginning to end-1, Eg. a[:,0:n] gives all the rows from 0th column to n-1 column 
y3 = data3[:,1]
x4 = data4[:,0]    # The plain [:] operator slices from beginning to end-1, Eg. a[:,0:n] gives all the rows from 0th column to n-1 column 
y4 = data4[:,1]


#matplotlib.pylab.xlim(0.3,0.34)
matplotlib.pylab.plot(x1,y1, label=r"$\theta=1.0001$")
matplotlib.pylab.plot(x3,y3, label=r"$\theta=1.01$")
matplotlib.pylab.plot(x4,y4, label=r"$\theta=1.06$")
matplotlib.pylab.plot(x2,y2, label=r"$\theta=1.1$")
#matplotlib.pylab.plot(x1,y1, '-^', markevery=60, markerfacecolor='none', markersize=4,)
#matplotlib.pylab.plot(x1,y1, '-^', markevery=60, markerfacecolor='none', markersize=4, label="$\gamma=0.7$")
#matplotlib.pylab.plot(x2,y2, '-s', markevery=600, markerfacecolor='none', markersize=4, label="$\gamma=1.0$")
#matplotlib.pylab.plot(x3,y3, '-p', markevery=600, markerfacecolor='none', markersize=4, label="$\gamma=1.2$")
#matplotlib.pylab.axis('equal')
matplotlib.pylab.xlim(0,0.02)
matplotlib.pylab.ylim(0,0.03)
#matplotlib.pylab.ylabel(r'$iy(\times 10^{10})$')
matplotlib.pylab.ylabel(r'$V_{eff}(x)$')
matplotlib.pylab.xlabel('x')
matplotlib.pylab.title(r'$\gamma=3.0$')
matplotlib.pylab.legend(loc=1, prop={'size': 10})
matplotlib.pylab.savefig('input_output_files/rho_2.0/theta_1.0001/figures/potential_theta_comparison_gamma_3pt0_near_origin2.pdf')
matplotlib.pylab.savefig('input_output_files/rho_2.0/theta_1.0001/figures/potential_theta_comparison_gamma_3pt0_near_origin2.eps', format='eps', dpi=1000)
matplotlib.pylab.show()


#matplotlib.pyplot.plot(x,y)
#pylab.plot(x,y)    # Use this step to run in anaconda