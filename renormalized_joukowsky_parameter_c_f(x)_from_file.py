# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 12:53:36 2020

@author: yadav
"""

#code for computation of parameter 'c' of Joukowsky transform self consistently for application of NUS paper method to solved example in CR paper. See notebook for details
#Instead of fit for function f(x), actual values from data file are used.
import math
import cmath
import numpy
import contour_integral_from_file
import derivative_central_difference



#gamma=0.77 c=0.75964909760813049    #corrected3 iteration11
#gamma=0.78 c=0.75533091405029995    #corrected3 iteration11
#gamma=0.79 c=0.75116396169710087    #corrected3 iteration11
#gamma=0.8 c=0.74692392576962918    #corrected3 iteration11

# 0.45328548471896202

theta = 1.0001
gamma = 3.0
#alpha = 8.0    # V(x)=rho*x+alpha*x**(1.0/alpha), alpha>1
rho= 2.0    # V(x)=rho*x  
c = 0.50005    # from self-consistent calculation using jouwkowsky_parameters_c_selfconsistent_calculation_CR_problem.py for alpha-log(x) potential.
print c
iteration = 10.0

contr_nu1 = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu1_contour_c="+str(c)+"_theta="+str(theta)+"_18000points_iter1.0.txt",float)
contr_nu2 = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"/contour/nu2_contour_c="+str(c)+"_theta="+str(theta)+"_18000points_iter1.0.txt",float)
# Note that the contour does not depend on parameter 'c' (refer notebook) so we will use the above contour for all different c's.
f_x_input = numpy.loadtxt("input_output_files/rho_"+str(rho)+"/theta_"+str(theta)+"/gamma_"+str(gamma)+"_correction_2/density/f_y_calculation_newton_rapson_method_2_gamma="+str(gamma)+"_max_err_1e-10_theta="+str(theta)+"_18000points_correction4_iter"+str(iteration-1)+".txt",float)

f_nu1 = numpy.empty(len(f_x_input),float)
f_nu2 = f_x_input[:, 1]

deriv_f_x = derivative_central_difference.derivative_cent_diff_(f_x_input[:, 0],f_x_input[:, 1])
deriv_f_x_nu2 = deriv_f_x
deriv_f_x_nu1 = numpy.empty(len(f_x_input),float)

#Following loop to change the order of the data for f_nu1 so that it is compatible with nu1.
for i in range(len(f_x_input)):    # function len() on array gives no. of rows of array
    f_nu1[len(f_x_input)-i-1] =  f_x_input[:, 1][i]
    
#Following loop to change the order of the data for f_nu1 so that it is compatible with nu1.
for i in range(len(f_x_input)):    # function len() on array gives no. of rows of array
    deriv_f_x_nu1[len(f_x_input)-i-1] =  deriv_f_x[i]    

while True:
        
                
    F1_nu1 = ((contour_integral_from_file.contr_intgl(contr_nu1,f_nu1)).real)
    F1_nu2 = ((contour_integral_from_file.contr_intgl(contr_nu2,f_nu2)).real)

            
    F1 = F1_nu1 + F1_nu2 - (1.0+theta)
    
#    def deriv_f1(z):    # derivative of f1(z) w.r.t. c
#            return (1.0/(2.0*(math.pi)*1j))*((b1*deriv_Jc(z)+2.0*b2*Jc(z)*deriv_Jc(z)+3.0*b3*((Jc(z))**2.0)*deriv_Jc(z)+4.0*b4*((Jc(z))**3.0)*deriv_Jc(z))/(z))  
                           
    
#    def deriv_f1(z):    # derivative of f1(z) w.r.t. c
#            return (1.0/(2.0*(math.pi)*1j))*((b1*deriv_Jc(z)+2.0*b2*Jc(z)*deriv_Jc(z)+3.0*b3*((Jc(z))**2)*deriv_Jc(z)+4.0*b4*((Jc(z))**3)*deriv_Jc(z)+5.0*b5*((Jc(z))**4)*deriv_Jc(z)+6.0*b6*((Jc(z))**5)*deriv_Jc(z))/(z))    

#    def deriv_f1(z):    # derivative of f1(z) w.r.t. c
#            return (1.0/(2.0*(math.pi)*1j))*((b1*deriv_Jc(z)+2.0*b2*Jc(z)*deriv_Jc(z)+3.0*b3*((Jc(z))**2)*deriv_Jc(z)+4.0*b4*((Jc(z))**3)*deriv_Jc(z)+5.0*b5*((Jc(z))**4)*deriv_Jc(z)+6.0*b6*((Jc(z))**5)*deriv_Jc(z)+7.0*b7*((Jc(z))**6)*deriv_Jc(z)+8.0*b8*((Jc(z))**7)*deriv_Jc(z))/(z))    


    deriv_F1_nu1 = ((contour_integral_from_file.contr_intgl(contr_nu1,deriv_f_x_nu1)).real)
    deriv_F1_nu2 = ((contour_integral_from_file.contr_intgl(contr_nu2,deriv_f_x_nu2)).real)

    deriv_F1 = deriv_F1_nu1 + deriv_F1_nu2

#    deriv_F1 = ((contour_integral.contr_intgl(contr,deriv_f1)).real)                         
    
    c_next = c - (F1/deriv_F1)    
         
    error = c_next - c
    print('error is', error)
    
    c = c_next

    
#    if(numpy.amax(error)<=1e-2):
    if(abs(error)<=(1e-10)):
        break

print('renormalized parameter c is', c)           