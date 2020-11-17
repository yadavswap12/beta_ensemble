# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:12:39 2018

@author: yadav
"""

# code to generate complex mapping J(s)

#https://stackoverflow.com/questions/16669428/process-very-large-20gb-text-file-line-by-line
#modified from https://stackoverflow.com/questions/30216573/reading-specific-columns-from-a-text-file-in-python
#https://docs.python.org/3.3/tutorial/inputoutput.html
import math
import cmath
import numpy

theta = 1.5
rho = 2.0    # V(x)=rho*x+alpha*x**(1.0/alpha), alpha>1
#alpha = 8.0    # V(x)=rho*x+alpha*x**(1.0/alpha), alpha>1
c =  1.586697316299037    # from self-consistent calculation using jouwkowsky_parameters_c_selfconsistent_calculation_CR_problem.py for alpha-log(x) potential.
#c_short = 0.878
gamma = 3.0
iteration = 14.0

#c0 = 1.0/2
f_in=file("input_output_files/rho_2.0/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu1_contour_gamma="+str(gamma)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt","r")
f_out=file("input_output_files/rho_2.0/theta_"+str(theta)+"/gamma_"+str(gamma)+"/mapping/mapping_output_nu1_gamma="+str(gamma)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt","w")
lines=f_in.readlines()
#i=0
for data in lines:
    x= data.split(' ')[0]  
    y= data.split(' ')[1]  
    #z(i)=x(i)+y(i)j    gives syntax error
    z=complex(float(x),float(y))    
    x_nu1 = c*(z+1)*(((z+1)/z)**(1/theta))
    #f_out.write(str(x_nu1.real)+'\n')
    f_out.write(str(x_nu1.real)+" "+str(x_nu1.imag)+'\n')
    #i+=1
f_in.close()    # () at the end is necessary to close the file
f_out.close()    # () at the end is necessary to close the file

f_in=file("input_output_files/rho_2.0/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu2_contour_gamma="+str(gamma)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt","r")
f_out=file("input_output_files/rho_2.0/theta_"+str(theta)+"/gamma_"+str(gamma)+"/mapping/mapping_output_nu2_gamma="+str(gamma)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt","w")
lines=f_in.readlines()
#i=0
for data in lines:
    x= data.split(' ')[0]  
    y= data.split(' ')[1]  
    #z(i)=x(i)+y(i)j    gives syntax error
    z=complex(float(x),float(y))
    x_nu2 = c*(z+1)*(((z+1)/z)**(1/theta))
    #f_out.write(str(x_nu2.real)+'\n')
    f_out.write(str(x_nu2.real)+" "+str(x_nu2.imag)+'\n')
    #i+=1
f_in.close()    # () at the end is necessary to close the file
f_out.close()    # () at the end is necessary to close the file