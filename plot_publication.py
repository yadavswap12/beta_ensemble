# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:59:04 2018

@author: yadav
"""

# code to plot data from text file
import math
import cmath
import numpy
import matplotlib    #pylab is submodule in matplotlib
#import matplotlib.pylab 
#import pylab    # Use this step to run in anaconda

data1 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.4/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=0.4_theta=1.0001_rho=2.0_18000points_corrected4_iter33.0.txt",float)
#data2 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.5/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=0.5_theta=1.0001_rho=2.0_18000points_corrected4_iter22.0.txt",float)
data3 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.6/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=0.6_theta=1.0001_rho=2.0_18000points_corrected4_iter12.0.txt",float)
#data4 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.7/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=0.7_theta=1.0001_rho=2.0_18000points_corrected4_iter10.0.txt",float)
data5 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.8/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=0.8_theta=1.0001_rho=2.0_18000points_corrected4_iter10.0.txt",float)
#data6 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.9/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=0.9_theta=1.0001_rho=2.0_18000points_corrected4_iter10.0.txt",float)
#data7 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_1.2/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=1.2_theta=1.0001_rho=2.0_18000points_corrected4_iter8.0.txt",float)
data8 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_1.4/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=1.4_theta=1.0001_rho=2.0_18000points_corrected4_iter13.0.txt",float)
#data9 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_1.6/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=1.6_theta=1.0001_rho=2.0_18000points_corrected4_iter12.0.txt",float)
#data10 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_1.8/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=1.8_theta=1.0001_rho=2.0_18000points_corrected4_iter10.0.txt",float)
data11 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.0/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=2.0_theta=1.0001_rho=2.0_18000points_corrected4_iter11.0.txt",float)
#data12 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.2/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=2.2_theta=1.0001_rho=2.0_18000points_corrected4_iter10.0.txt",float)
#data13 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.4/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=2.4_theta=1.0001_rho=2.0_18000points_corrected4_iter8.0.txt",float)
#data14 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.6/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=2.6_theta=1.0001_rho=2.0_18000points_corrected4_iter12.0.txt",float)
#data15 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.8/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=2.8_theta=1.0001_rho=2.0_18000points_corrected4_iter12.0.txt",float)
data16 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_3.0/density/renormalized_density_psi_method_2_epsi=1e-4_gamma=3.0_theta=1.0001_rho=2.0_18000points_corrected4_iter13.0.txt",float)
data33 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_1.0/density/density_psi_epsi=1e-4_c=0.50005_theta=1.0001_18000points.txt",float)

data17 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.4/density/renormalized_potential_from_f2_y_method_2_gamma=0.4_max_err_1e-10_theta=1.0001_18000points_correction4_iter33.0.txt",float)
#data18 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.5/density/renormalized_potential_from_f2_y_method_2_gamma=0.5_max_err_1e-10_theta=1.0001_18000points_correction4_iter22.0.txt",float)
data19 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.6/density/renormalized_potential_from_f2_y_method_2_gamma=0.6_max_err_1e-10_theta=1.0001_18000points_correction4_iter12.0.txt",float)
#data20 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.7/density/renormalized_potential_from_f2_y_method_2_gamma=0.7_max_err_1e-10_theta=1.0001_18000points_correction4_iter10.0.txt",float)
data21 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.8/density/renormalized_potential_from_f2_y_method_2_gamma=0.8_max_err_1e-10_theta=1.0001_18000points_correction4_iter10.0.txt",float)
#data22 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_0.9/density/renormalized_potential_from_f2_y_method_2_gamma=0.9_max_err_1e-10_theta=1.0001_18000points_correction4_iter10.0.txt",float)
#data23 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_1.2/density/renormalized_potential_from_f2_y_method_2_gamma=1.2_max_err_1e-10_theta=1.0001_18000points_correction4_iter8.0.txt",float)
data24 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_1.4/density/renormalized_potential_from_f2_y_method_2_gamma=1.4_max_err_1e-10_theta=1.0001_18000points_correction4_iter13.0.txt",float)
#data25 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_1.6/density/renormalized_potential_from_f2_y_method_2_gamma=1.6_max_err_1e-10_theta=1.0001_18000points_correction4_iter12.0.txt",float)
#data26 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_1.8/density/renormalized_potential_from_f2_y_method_2_gamma=1.8_max_err_1e-10_theta=1.0001_18000points_correction4_iter10.0.txt",float)
data27 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.0/density/renormalized_potential_from_f2_y_method_2_gamma=2.0_max_err_1e-10_theta=1.0001_18000points_correction4_iter11.0.txt",float)
#data28 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.2/density/renormalized_potential_from_f2_y_method_2_gamma=2.2_max_err_1e-10_theta=1.0001_18000points_correction4_iter10.0.txt",float)
#data29 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.4/density/renormalized_potential_from_f2_y_method_2_gamma=2.4_max_err_1e-10_theta=1.0001_18000points_correction4_iter8.0.txt",float)
#data30 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.6/density/renormalized_potential_from_f2_y_method_2_gamma=2.6_max_err_1e-10_theta=1.0001_18000points_correction4_iter12.0.txt",float)
#data31 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_2.8/density/renormalized_potential_from_f2_y_method_2_gamma=2.8_max_err_1e-10_theta=1.0001_18000points_correction4_iter12.0.txt",float)
data32 = numpy.loadtxt("input_output_files/rho_2.0/theta_1.0001/gamma_3.0/density/renormalized_potential_from_f2_y_method_2_gamma=3.0_max_err_1e-10_theta=1.0001_18000points_correction4_iter13.0.txt",float)


x1 = data1[:,0]
y1 = data1[:,1]
#x2 = data2[:,0]
#y2 = data2[:,1]
x3 = data3[:,0]
y3 = data3[:,1]
#x4 = data4[:,0]
#y4 = data4[:,1]
x5 = data5[:,0]
y5 = data5[:,1]
#x6 = data6[:,0]
#y6 = data6[:,1]
#x7 = data7[:,0]
#y7 = data7[:,1]
x8 = data8[:,0]
y8 = data8[:,1]
#x9 = data9[:,0]
#y9 = data9[:,1]
#x10 = data10[:,0]
#y10 = data10[:,1]
x11 = data11[:,0]
y11= data11[:,1]
#x12 = data12[:,0]
#y12 = data12[:,1]
#x13 = data13[:,0]
#y13 = data13[:,1]
#x14 = data14[:,0]
#y14 = data14[:,1]
#x15 = data15[:,0]
#y15 = data15[:,1]
x16 = data16[:,0]
y16 = data16[:,1]
x33 = data33[:,0]
y33 = data33[:,1]

x17 = data17[:,0]
y17 = data17[:,1]
#x18 = data18[:,0]
#y18 = data18[:,1]
x19 = data19[:,0]
y19 = data19[:,1]
#x20 = data20[:,0]
#y20 = data20[:,1]
x21 = data21[:,0]
y21 = data21[:,1]
#x22 = data22[:,0]
#y22 = data22[:,1]
#x23 = data23[:,0]
#y23 = data23[:,1]
x24 = data24[:,0]
y24 = data24[:,1]
#x25 = data25[:,0]
#y25 = data25[:,1]
#x26 = data26[:,0]
#y26 = data26[:,1]
x27 = data27[:,0]
y27= data27[:,1]
#x28 = data28[:,0]
#y28 = data28[:,1]
#x29 = data29[:,0]
#y29 = data29[:,1]
#x30 = data30[:,0]
#y30 = data30[:,1]
#x31 = data31[:,0]
#y31 = data31[:,1]
x32 = data32[:,0]
y32 = data32[:,1]


x = numpy.empty(numpy.size(range(1,200,1))+1)
y = numpy.empty(numpy.size(range(1,200,1))+1)

#following loop to calculate potential V(x)=2x
for i in range(1,200,1):    #only integer step argument is available for range() hence 0 to 18000. to get 180 degrees will later divide by 100
    x[i] = i/1000000.0
    y[i] = 2.0*x[i]

#matplotlib.pylab.plot(x1,y1,"v", markevery=60, markerfacecolor='none', markeredgecolor='r', markersize=4, label="$\gamma=0.4$")
#matplotlib.pylab.plot(x2,y2,"s", markevery=60, markerfacecolor='none', markeredgecolor='g', markersize=4, label="$\gamma=0.5$")
#matplotlib.pylab.plot(x3,y3,"p", markevery=60, markerfacecolor='none', markeredgecolor='b', markersize=4, label="$\gamma=0.6$")
#matplotlib.pylab.plot(x4,y4,"h", markevery=60, markerfacecolor='none',markeredgecolor='c', markersize=4, label="$\gamma=0.7$")
#matplotlib.pylab.plot(x5,y5,"+", markevery=60, markerfacecolor='none',markeredgecolor='m', markersize=4, label="$\gamma=0.8$")
#matplotlib.pylab.plot(x6,y6,"*", markevery=60, markerfacecolor='none',markeredgecolor=(0.3,0.0,0.6,0.8), markersize=4, label="$\gamma=0.9$")
#matplotlib.pylab.plot(x7,y7,"*", markevery=60, markerfacecolor='none',markeredgecolor=(0.1,0.3,0.5,0.8), markersize=4, label="$\gamma=1.2$")
#matplotlib.pylab.plot(x8,y8,"*", markevery=60, markerfacecolor='none',markeredgecolor=(0.4,0.2,0.9,0.8), markersize=4, label="$\gamma=1.4$")
#matplotlib.pylab.plot(x9,y9,"*", markevery=60, markerfacecolor='none',markeredgecolor=(0.4,0.3,0.4,0.8), markersize=4, label="$\gamma=1.6$")
#matplotlib.pylab.plot(x10,y10,"*", markevery=60, markerfacecolor='none',markeredgecolor=(0.9,0.8,0.2,0.8), markersize=4, label="$\gamma=1.8$")
#matplotlib.pylab.plot(x11,y11,"*", markevery=60, markerfacecolor='none',markeredgecolor=(1.0,0.8,0.3,0.8), markersize=4, label="$\gamma=2.0$")
#matplotlib.pylab.plot(x12,y12,"*", markevery=60, markerfacecolor='none',markeredgecolor=(1.0,0.1,0.8,0.8), markersize=4, label="$\gamma=2.2$")
##matplotlib.pylab.plot(x13,y13,"*", markevery=60, markerfacecolor='none',markeredgecolor=(0.0,0.2,0.9,0.8), markersize=4, label="$\gamma=2.4$")
#matplotlib.pylab.plot(x14,y14,"*", markevery=60, markerfacecolor='none',markeredgecolor=(0.9,0.5,0.2,0.8), markersize=4, label="$\gamma=2.6$")
#matplotlib.pylab.plot(x15,y15,"*", markevery=60, markerfacecolor='none',markeredgecolor=(0.9,0.6,0.5,0.8), markersize=4, label="$\gamma=2.8$")
#matplotlib.pylab.plot(x16,y16,"*", markevery=60, markerfacecolor='none',markeredgecolor=(0.1,0.1,0.6,0.8), markersize=4, label="$\gamma=3.0$")

#matplotlib.pylab.plot(x,y,"d", markevery=2, markerfacecolor='none',markeredgecolor=(0.8,0.2,0.2,0.8), markersize=4, label="$\gamma=1$")

#matplotlib.pylab.plot(x,y,"d", markevery=2, label="$\gamma=1$")

#matplotlib.pylab.xlim(0,0.01)
#matplotlib.pylab.ylim(0,14)
#matplotlib.pylab.ylabel(r'$\sigma(x,\gamma$)')
#matplotlib.pylab.xlabel('x')
##matplotlib.pylab.legend(loc='upper right', prop={'size': 8})
#matplotlib.pylab.legend(loc=1, prop={'size': 6})
#matplotlib.pylab.savefig('input_output_files/rho_2.0/theta_1.0001/figures/density_near_origin_beta_ensembles_pub_corrected4.pdf')
#matplotlib.pylab.savefig('input_output_files/rho_2.0/theta_1.0001/figures/density_near_origin_beta_ensembles_pub_corrected4.eps', format='eps', dpi=1000)
#matplotlib.pylab.show()


matplotlib.pylab.plot(x1,y1, '-^', markevery=10, markersize=6, label=r"$\beta=1.4$")    #r (e.g. r"foo\nbar") makes Python interpret the string as a raw string literal, i.e. without converting the escaped character combinations to special characters.
#matplotlib.pylab.plot(x2,y2, '-s', markevery=600, markerfacecolor='none', markersize=4, label="$\gamma=0.5$")
matplotlib.pylab.plot(x3,y3, '-s', markevery=10, markersize=6, label=r"$\beta=1.6$")
#matplotlib.pylab.plot(x4,y4, '-h', markevery=600, markerfacecolor='none', markersize=4, label="$\gamma=0.7$")
matplotlib.pylab.plot(x5,y5, '-p', markevery=10, markersize=6, label=r"$\beta=1.8$")
#matplotlib.pylab.plot(x6,y6, '-*', markevery=600, markerfacecolor='none', markersize=4, label="$\gamma=0.9$")
#matplotlib.pylab.plot(x7,y7, '--', markevery=1, color=(1.0,1.0,0.0,1.0), markersize=4, label="$\gamma=1.2$")
matplotlib.pylab.plot(x8,y8, '-h', markevery=10, markersize=6, label=r"$\beta=2.4$")
#matplotlib.pylab.plot(x9,y9, '--', markevery=1, color=(1.0,0.0,1.0,1.0), markersize=4, label="$\gamma=1.6$")
#matplotlib.pylab.plot(x10,y10, '--', markevery=1, color=(1.0,1.0,1.0,1.0), markersize=4, label="$\gamma=1.8$")
matplotlib.pylab.plot(x11,y11, '-d', markevery=10, markersize=6, label=r"$\beta=3.0$")
#matplotlib.pylab.plot(x12,y12, '--', markevery=1, color=(0.3,0.3,1.0,1.0), markersize=4, label="$\gamma=2.2$")
#matplotlib.pylab.plot(x13,y13, '-*', markevery=60, markerfacecolor='none', markersize=4, label="$\gamma=2.4$")
#matplotlib.pylab.plot(x14,y14, '--', markevery=1, color=(0.3,1.0,0.3,1.0), markersize=4, label="$\gamma=2.6$")
#matplotlib.pylab.plot(x15,y15, '--', markevery=1, color=(1.0,0.3,1.0,1.0), markersize=4, label="$\gamma=2.8$")
matplotlib.pylab.plot(x16,y16, '-v', markevery=10, markersize=6, label=r"$\beta=4.0$")
matplotlib.pylab.plot(x33,y33, '-*', markevery=10, markersize=6, label=r"$\beta=2.0$")

#matplotlib.pylab.plot(x,y, '->', markevery=2, markerfacecolor='none', markersize=4, label="$\gamma=1$")

#matplotlib.pylab.plot(x,y,"d", markevery=2, label="$\gamma=1$")

matplotlib.pylab.xlim(0,0.0001)
matplotlib.pylab.ylim(0,200.0)
matplotlib.pylab.ylabel(r'$\sigma(x,\beta$)')    #r (e.g. r"foo\nbar") makes Python interpret the string as a raw string literal, i.e. without converting the escaped character combinations to special characters.
matplotlib.pylab.xlabel('x')
#matplotlib.pylab.legend(loc='upper right', prop={'size': 8})
matplotlib.pylab.legend(loc=1, prop={'size': 10})
matplotlib.pylab.savefig('input_output_files/rho_2.0/theta_1.0001/figures/density_near_origin_beta_ensembles_pub2_corrected4_2.pdf')
matplotlib.pylab.savefig('input_output_files/rho_2.0/theta_1.0001/figures/density_near_origin_beta_ensembles_pub2_corrected4_2.eps', format='eps', dpi=1000)
matplotlib.pylab.show()


matplotlib.pylab.plot(x17,y17, '-^', markevery=10, markersize=6, label=r"$\beta=1.4$")
#matplotlib.pylab.plot(x18,y18, '-s', markevery=600, markerfacecolor='none', markersize=4, label="$\gamma=0.5$")
matplotlib.pylab.plot(x19,y19, '-s', markevery=10, markersize=6, label=r"$\beta=1.6$")
#matplotlib.pylab.plot(x20,y20, '-h', markevery=600, markerfacecolor='none', markersize=4, label="$\gamma=0.7$")
matplotlib.pylab.plot(x21,y21, '-p', markevery=10, markersize=6, label=r"$\beta=1.8$")
#matplotlib.pylab.plot(x22,y22, '-*', markevery=600, markerfacecolor='none', markersize=4, label="$\gamma=0.9$")
#matplotlib.pylab.plot(x23,y23, '--', markevery=1, color=(1.0,1.0,0.0,1.0), markersize=4, label="$\gamma=1.2$")
matplotlib.pylab.plot(x24,y24, '-h', markevery=10, markersize=6, label=r"$\beta=2.4$")
#matplotlib.pylab.plot(x25,y25, '--', markevery=1, color=(1.0,0.0,1.0,1.0), markersize=4, label="$\gamma=1.6$")
#matplotlib.pylab.plot(x26,y26, '--', markevery=1, color=(1.0,1.0,1.0,1.0), markersize=4, label="$\gamma=1.8$")
matplotlib.pylab.plot(x27,y27, '-d', markevery=10, markersize=6, label=r"$\beta=3.0$")
#matplotlib.pylab.plot(x28,y28, '--', markevery=1, color=(0.3,0.3,1.0,1.0), markersize=4, label="$\gamma=2.2$")
#matplotlib.pylab.plot(x29,y29, '-*', markevery=60, markerfacecolor='none', markersize=4, label="$\gamma=2.4$")
#matplotlib.pylab.plot(x30,y30, '--', markevery=1, color=(0.3,1.0,0.3,1.0), markersize=4, label="$\gamma=2.6$")
#matplotlib.pylab.plot(x31,y31, '--', markevery=1, color=(1.0,0.3,1.0,1.0), markersize=4, label="$\gamma=2.8$")
matplotlib.pylab.plot(x32,y32, '-v', markevery=10, markersize=6, label=r"$\beta=4.0$")
matplotlib.pylab.plot(x,y, '-*', markevery=15, markersize=6, label=r"$\beta=2.0$")

matplotlib.pylab.ylim(0,0.001)
matplotlib.pylab.xlim(0,0.0001)
matplotlib.pylab.ylabel(r'$V_{eff}(x)$')
matplotlib.pylab.xlabel('x')
#matplotlib.pylab.title('renormalized potential')
#matplotlib.pylab.legend(loc='upper right', prop={'size': 6})
matplotlib.pylab.legend(loc=1, prop={'size': 10})
matplotlib.pylab.savefig('input_output_files/rho_2.0/theta_1.0001/figures/potential_near_origin_beta_ensembles_pub2_corrected4_2.pdf')
matplotlib.pylab.savefig('input_output_files/rho_2.0/theta_1.0001/figures/potential_near_origin_beta_ensembles_pub2_corrected4_2.eps', format='eps', dpi=1000)
##matplotlib.pyplot.grid(true)
#matplotlib.pylab.show()
#
#matplotlib.pylab.plot(x28,y28,"g", label="density")
#matplotlib.pylab.plot(x29,y29,"b", label="V(x)")
##matplotlib.pylab.text(2.5, 4, r'$\gamma=0.9$')
#matplotlib.pylab.ylim(0,8)
##matplotlib.pylab.xlim(0,0.01)
#matplotlib.pylab.title('$\gamma=0.99$')
#matplotlib.pylab.ylabel('density')
#matplotlib.pylab.xlabel('x')
#matplotlib.pylab.legend(loc=1, prop={'size': 6})
#matplotlib.pylab.savefig('input_output_files/potential_linear_slope_2/figures/renormalized_density_psi_and_V(x)_gamma_0.99_method_2_CR_solvedproblem.pdf')
#matplotlib.pylab.show()
#
#matplotlib.pylab.plot(x28,y28,"g", label="density")
#matplotlib.pylab.ylim(0,10)
#matplotlib.pylab.xlim(0,0.01)
#matplotlib.pylab.title('$\gamma=0.99$')
#matplotlib.pylab.ylabel('density')
#matplotlib.pylab.xlabel('x')
#matplotlib.pylab.legend(loc=1, prop={'size': 6})
#matplotlib.pylab.savefig('input_output_files/potential_linear_slope_2/figures/renormalized_density_psi_gamma_0.99_method_2_CR_solvedproblem_near_origin.pdf')
#matplotlib.pylab.show()
#
##matplotlib.pylab.plot(x22,y22,"g", label="$\rho=2,\gamma=0.98$")
##matplotlib.pylab.plot(x25,y25,"b", label="$\rho=4,\gamma=0.98$")
##matplotlib.pylab.ylim(0,10)
##matplotlib.pylab.xlim(0,0.01)
##matplotlib.pylab.title('$\gamma=0.98$')
##matplotlib.pylab.ylabel('density')
##matplotlib.pylab.xlabel('x')
##matplotlib.pylab.legend(loc=1, prop={'size': 6})
##matplotlib.pylab.savefig('input_output_files/linear_V_rho=4.0/figures/renormalized_density_psi_gamma_0.98_method_2_CR_solvedproblem.pdf')
##matplotlib.pylab.show()
#
#
##matplotlib.pyplot.plot(x,y)
##pylab.plot(x,y)    # Use this step to run in anaconda