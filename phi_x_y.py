# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 11:39:38 2020

@author: yadav
"""

import math
import cmath
import numpy
import contour_integral
import integration_trapezoidal_nonuniformspacing
import derivative_central_difference
import matplotlib    #pylab is submodule in matplotlib

gamma = float(raw_input("gamma is: "))    # asks for user input from command line. to be used in terminal    
theta = float(raw_input("theta is: "))    # parameters from solved C.R. problem    # asks for user input from command line. to be used in terminal
rho = float(raw_input("rho is: "))    # V(x)=rho*x    # parameters from solved C.R. problem    # asks for user input from command line. to be used in terminal
#alpha = float(raw_input("alpha is: "))    # V(x)=rho*x+alpha*x**(1.0/alpha), alpha>1    # asks for user input from command line. to be used in terminal 
#c = float(raw_input("c is: "))    # from self-consistent calculation using jouwkowsky_parameters_c_selfconsistent_calculation_CR_problem.py for alpha-log(x) potential.
c_short = float(raw_input("c_short is: "))
iteration = float(raw_input("iteration is: "))

epsi = 1e-4

data1 = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu1_contour_c="+str(c_short)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt",float)
data2 = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu2_contour_c="+str(c_short)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt",float)
data3 = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/mapping/mapping_output_nu1_c="+str(c_short)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt",float)
data4 = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/mapping/mapping_output_nu2_c="+str(c_short)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt",float)
contr = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu1_contour_c="+str(c_short)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt",float)
f_out1=file("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/density/phi_x_9_gamma="+str(gamma)+"_max_err_1e-10_theta="+str(theta)+"_18000points_correction4_iter"+str(iteration)+".txt","w")
f_out2=file("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/density/deriv_hbar_gamma="+str(gamma)+"_max_err_1e-10_theta="+str(theta)+"_18000points_correction4_iter"+str(iteration)+".txt","w")

x = data4[:, 0]    # Array Slicing: Accessing array's first column(i.e. index-zero column), https://jakevdp.github.io/PythonDataScienceHandbook/02.02-the-basics-of-numpy-arrays.html
x1 = data1[:, 0]    # for nu1    # Note- to convert integer type array(x) to float type array(xx) Use: xx = x.astype(float)
y1 = data1[:, 1]    # for nu1
r1 = numpy.sqrt(x1**2+y1**2)
x2 = data2[:, 0]    # for nu2    # Note- to convert integer type array(x) to float type array(xx) Use: xx = x.astype(float)
y2 = data2[:, 1]    # for nu2
r2 = numpy.sqrt(x2**2+y2**2)

hbar_x = x2+y2*1j    # h(x) in formula in notebook
h_x = numpy.conjugate(hbar_x)    # hbar(x) in formula in notebook 
#h_y = x1*(1.0+epsi/r1)+y1*(1.0+epsi/r1)*1j    # Adding small epsilon radially, h(y) in formula in notebook
h_x_plus = (h_x.real)*(1.0+epsi/r2)+(h_x.imag)*(1.0+epsi/r2)*1j    # Adding small epsilon radially, h(y) in formula in notebook
hbar_x_plus = (x2)*(1.0+epsi/r2)+(y2)*(1.0+epsi/r2)*1j    # hbar(y) in formula

deriv_hbar_real = derivative_central_difference.derivative_cent_diff_(x,x2)
deriv_hbar_imag = derivative_central_difference.derivative_cent_diff_(x,y2)
deriv_hbar = deriv_hbar_real + deriv_hbar_imag*1j

phi_x_9 = ((((1.0/(h_x_plus[9]-hbar_x))+(1.0/(hbar_x_plus[9]-hbar_x)))*deriv_hbar).imag)    # for phi(x,y(from 0 to 17999)) see eq.(26) from paper(https://iopscience.iop.org/article/10.1088/1751-8121/ab56e0/pdf) 

for m in range(len(x)):    # function len() on array gives no. of rows of array
    f_out1.write(str(x[m])+" "+str(phi_x_9[m])+'\n')
    f_out2.write(str(x[m])+" "+str(deriv_hbar_real[m])+" "+str(deriv_hbar_imag[m])+'\n')

f_out1.close()    # () at the end is necessary to close the file                
f_out2.close()    # () at the end is necessary to close the file                

matplotlib.pylab.plot(x,phi_x_9)
#matplotlib.pylab.plot(x2,y2)
matplotlib.pylab.xlim(-0.2,1.6)
matplotlib.pylab.ylim(-100,100)
matplotlib.pylab.show()

matplotlib.pylab.plot(x,deriv_hbar_real)
matplotlib.pylab.show()

matplotlib.pylab.plot(x,deriv_hbar_imag)
matplotlib.pylab.show()



