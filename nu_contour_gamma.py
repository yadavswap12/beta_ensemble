# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 10:08:32 2018

@author: yadav
"""

# code to generate contour nu, nu1 and nu2 for J(s)=c(s+1)((s+1)/s)**(1/theta)
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

# note that for given joukowsky transformation the contour does not depend on 'c' (refer notebook for locus eqn.) yet we give gamma reference in contour file name for sake of clarity.
 
f_out=file("input_output_files/rho_2.0/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu_contour_gamma="+str(gamma)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt","w")
f_out1=file("input_output_files/rho_2.0/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu1_contour_gamma="+str(gamma)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt","w")
f_out2=file("input_output_files/rho_2.0/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu2_contour_gamma="+str(gamma)+"_theta="+str(theta)+"_18000points_iter"+str(iteration)+".txt","w")
for i in range(1,18000,1):    #only integer step argument is available for range() hence 0 to 18000. to get 180 degrees will later divide by 100
    r = (math.tan((math.radians(i/100.0)/(1.0+theta))))/(math.sin(math.radians(i/100.0))-math.cos(math.radians(i/100.0))*math.tan((math.radians(i/100.0)/(1.0+theta))))    
    x = r*math.cos(math.radians(i/100.0))
    y = r*math.sin(math.radians(i/100.0))
    #f_out.write(str(r)+" "+str(x)+" "+str(y)+" "+str(i)+'\n')
    f_out.write(str(x)+" "+str(y)+'\n')
    f_out1.write(str(x)+" "+str(y)+'\n')
#f_out.close()    # () at the end is necessary to close the file
f_out1.close()    # () at the end is necessary to close the file
for i in range(17999,0,-1):    #only integer step argument is available for range() hence 0 to 36000. to get 360 degrees will later divide by 100
    r = (math.tan((math.radians(i/100.0)/(1.0+theta))))/(math.sin(math.radians(i/100.0))-math.cos(math.radians(i/100.0))*math.tan((math.radians(i/100.0)/(1.0+theta))))    
    x = r*math.cos(math.radians(i/100.0))
    y = -r*math.sin(math.radians(i/100.0))
    #f_out.write(str(r)+" "+str(x)+" "+str(y)+" "+str(i)+'\n')
    f_out.write(str(x)+" "+str(y)+'\n')
    f_out2.write(str(x)+" "+str(y)+'\n')
f_out.close()    # () at the end is necessary to close the file    
f_out2.close()    # () at the end is necessary to close the file     
   