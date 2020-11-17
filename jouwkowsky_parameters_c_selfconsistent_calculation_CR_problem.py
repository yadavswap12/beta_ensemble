# -*- coding: utf-8 -*-
"""
Created on Tue Feb 05 15:46:16 2019

@author: yadav
"""

#code for computation of parameter 'c' of Joukowsky transform self consistently for alpha-log(x) potential.
import math
import cmath
import numpy
import contour_integral

#b0=-0.14545    # parameters of polynomial fit for f1(x), f1(x)=b0 + b1x + b2x^2 + b3x^3 + b4x^4 
#b1=2.36095    # gamma = 0.9
#b2=-3.9356e-4
#b3=2.72605e-4
#b4=-6.51513e-5
#b5=0.29999
#b6=-0.17164

theta = 2.0
rho = 2.0    # V(x)=rho*x
#alpha = 8.0    # V(x)=gamma*(rho*x+alpha*x**(1.0/alpha)), alpha>1 
gamma = 0.9
c = 1.8    # initialization for c(>0), analytical solution is c=(will calculate later)
#print c

contr = numpy.loadtxt("input_output_files/rho_2.0/contour/nu_contour_c=1_theta=2.0_18000points.txt",float)
# Note that the contour does not depend on parameter 'c' (refer notebook) so we will use the above contour for all different c's.
while True:
        
    def Jc(z):    # joukowsky transformation for hard edge
            return (c*(z+1.0)*(((z+1.0)/z)**(1.0/theta)))
            
    def deriv_Jc(z):    # derivative of joukowsky transformation w.r.t. c
            return (z+1.0)*(((z+1.0)/z)**(1.0/theta))

    def f1(z):    # See notebook
            return (1.0/(2.0*(math.pi)*1j))*((rho*(Jc(z)))/(z))            

#    def f1(z):    # See notebook
#            return (1.0/(2.0*(math.pi)*1j))*((b0+b1*Jc(z)+b2*(Jc(z))**2+b3*(Jc(z))**3+b4*(Jc(z))**4+b5*(Jc(z))**5+b6*(Jc(z))**6)/(z))
    
            
    F1 = ((contour_integral.contr_intgl(contr,f1)).real) - (1.0+theta)
    
    def deriv_f1(z):    # derivative of f1(z) w.r.t. c
            return (1.0/(2.0*(math.pi)*1j))*((rho*(deriv_Jc(z)))/z)  
                           
    
#    def deriv_f1(z):    # derivative of f1(z) w.r.t. c
#            return (1.0/(2.0*(math.pi)*1j))*((b1*deriv_Jc(z)+2.0*b2*Jc(z)*deriv_Jc(z)+3.0*b3*((Jc(z))**2)*deriv_Jc(z)+4.0*b4*((Jc(z))**3)*deriv_Jc(z)+5.0*b5*((Jc(z))**4)*deriv_Jc(z)+6.0*b6*((Jc(z))**5)*deriv_Jc(z))/(z))    
       

    deriv_F1 = ((contour_integral.contr_intgl(contr,deriv_f1)).real)                         
    
    c_next = c - (F1/deriv_F1)    
         
    error = c_next - c
    print('error is', error)
    
    c = c_next

    
#    if(numpy.amax(error)<=1e-2):
    if(abs(error)<=(1e-10)):
        break

print('parameter c is', c)            