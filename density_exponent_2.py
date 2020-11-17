# -*- coding: utf-8 -*-
"""
Created on Wed Jul 01 18:44:08 2020

@author: yadav
"""

# Code to compute d1 and d2 in eq.(1.35) and (1.36) in CR.

import math
import cmath
import numpy
import contour_integral
import integration_trapezoidal_nonuniformspacing


theta = float(raw_input("theta is: "))    # asks for user input from command line. To be used in terminal.    
gamma = float(raw_input("gamma is: "))    # asks for user input from command line. To be used in terminal.    
#alpha = float(raw_input("alpha is: "))    # asks for user input from command line. To be used in terminal.    
#rho = 2.0
rho = float(raw_input("rho is: "))    # asks for user input from command line. To be used in terminal.    
#c = theta/rho    # eqn.(4.21) in C.R.
#c = 0.49922288952033711    # renormalized c for gamma=0.9 computed from python file 'renormalized_joukowsky_parameter_c.py'
c = theta/rho
sb = 1.0/theta
b = c*((sb+1.0)**((1.0+theta/theta)))*((1.0/sb)**(1.0/theta))
print b

iteration = float(raw_input("iteration is: ")) 

contr = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu2_contour_c="+str(c)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt",float)
mapping = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/mapping/mapping_output_nu2_c="+str(c)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt",float)

I_plus_1 = contr[:,0] + contr[:,1]*1j

I_plus_2 = numpy.conjugate(I_plus_1)

f = (1.0/(I_plus_2+1.0)).imag

integral = integration_trapezoidal_nonuniformspacing.int_trap_non_uniform(mapping[:,0],f)    # See eq.(1.35) in CR.

d1 = (-1.0/((math.pi**2)))*((c)**((-theta)/(theta+1.0)))*(math.sin((math.pi/(theta+1.0))))*(rho)*integral 

print('prefactor d1 is', d1)

J_doubleprime_sb = c*((1.0+theta)/(theta**2.0))*((sb+1.0)**((1.0-theta/theta)))*((1.0/sb)**((1.0+2.0*theta)/theta))

f2 = (1.0/(I_plus_2-sb)).imag

integral2 = integration_trapezoidal_nonuniformspacing.int_trap_non_uniform(mapping[:,0],f2)    # See eq.(1.36) in CR.

d2 = (-1.0/((math.pi**2.0)*b))*((2.0/J_doubleprime_sb)**(0.5))*(rho)*integral2

print('prefactor d2 is', d2)
 

