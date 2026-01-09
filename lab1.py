import numpy as np


sig_x = 16
sig_y = 9
tau_xy = 5

def normal_stress (x,y,t,p):
    return (x+y)/2+(x-y)/2*np.cos(2*p)+t*np.sin(2*p)

def shear_stress(x,y,t,p):
    return -(x-y)/2*np.sin(2*p)+t*np.cos(2*p)


def princ_stresses(sig_x, sig_y, tau_xy):
    """solve for phi_p first which tells us the angle at which the normal stress is max 
       (principle stress states (at 45 or pi/2 degrees from this is the max in second direction) and we know shear is zero)
        
        next solve for phi_s which tells us the angle at which  shear stress is max
        we then know at that angle the shear is max and each normal stress is a function of the avg of normal stresses"""
    
    phi_p = np.atan((2*tau_xy)/(sig_x - sig_y))/2
    
    max_normal = normal_stress(sig_x, sig_y,tau_xy, phi_p)
    
    print (max_normal, np.rad2deg(phi_p))
    
    
    
    
    

princ_stresses(sig_x, sig_y, tau_xy)


    
    
    
