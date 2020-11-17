# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 08:15:34 2020

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
#c_short = float(raw_input("c_short is: "))
iteration = int(raw_input("iteration is: "))

for i in range(iteration-1):    # function len() on array gives no. of rows of array
    f_x_input1 = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/density/f_y_calculation_newton_rapson_method_2_gamma="+str(gamma)+"_max_err_1e-10_theta="+str(theta)+"_18000points_correction4_iter"+str(i+1.0)+".txt",float)
    f_x_input2 = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/density/f_y_calculation_newton_rapson_method_2_gamma="+str(gamma)+"_max_err_1e-10_theta="+str(theta)+"_18000points_correction4_iter"+str(i+2.0)+".txt",float)
    f_x_1 = f_x_input1[:,1]
    f_x_2 = f_x_input2[:,1]   
    max_error = numpy.amax(abs(f_x_2 - f_x_1))
    print('maximum error and iteration are', max_error, i+2)

error = numpy.empty([f_x_input1.shape[0],f_x_input1.shape[1]],float)
error[:,0] = f_x_input1[:,0]
error[:,1] = f_x_2 - f_x_1

matplotlib.pylab.plot(error[:,0],error[:,1])

    