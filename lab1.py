import numpy as np


sig_x = 16
sig_y = 9
tau_xy = 5

def normal_stress (x,y,t,p):
    return (x+y)/2+(x-y)/2*np.cos(2*p)+t*np.sin(2*p)

def shear_stress(x,y,t,p):
    return -(x-y)/2*np.sin(2*p)+t*np.cos(2*p)

def shear_stress_normal(x,y,t,p):
    return (x+y)/2

def phi_p(x,y,t):
    return np.atan((2*t)/(x - y))/2

def phi_s(x,y,t):
    return np.atan(-(x - y)/(2*t))/2


def print_stresses(sig_x, sig_y, tau_xy):
    """solve for phi_p first which tells us the angle at which the normal stress is max 
       (principle stress states (at 45 or pi/2 degrees from this is the max in second direction) and we know shear is zero)
        
        next solve for phi_s which tells us the angle at which  shear stress is max
        we then know at that angle the shear is max and each normal stress is a function of the avg of normal stresses"""
    
    phi_princ = phi_p(sig_x, sig_y, tau_xy)
    print (f"the angle for principle stresses is {np.rad2deg(phi_princ)} degrees and {np.rad2deg(phi_princ + np.pi/2)} degrees")
    phi_shear = phi_s(sig_x, sig_y, tau_xy)
    print (f"the angle for max shear stresses is {np.rad2deg(phi_shear)} degrees and {np.rad2deg(phi_shear + np.pi/2)} degrees")
    print("--------------------------------------------------")


    max_normal = normal_stress(sig_x, sig_y,tau_xy, phi_princ)
    max_normal_2 = normal_stress(sig_x, sig_y,tau_xy, phi_princ + np.pi/2)
    print (f"the max normal stress is {max_normal} and the angle is {np.rad2deg(phi_princ)} degrees")
    print (f"the second max normal stress is {max_normal_2} and the angle is {np.rad2deg(phi_princ + np.pi/2)} degrees")
    print(f"the shear stress at these angles are {shear_stress(sig_x, sig_y, tau_xy, phi_princ)} and {shear_stress(sig_x, sig_y, tau_xy, phi_princ + np.pi/2)}")
    print("--------------------------------------------------")

    max_shear = shear_stress(sig_x, sig_y, tau_xy, phi_shear)
    max_shear_2 = shear_stress(sig_x, sig_y, tau_xy, phi_shear + np.pi/2)
    print (f"the max shear stress is {max_shear} and the angle is {np.rad2deg(phi_shear)} degrees") 
    print (f"the second max shear stress is {max_shear_2} and the angle is {np.rad2deg(phi_shear + np.pi/2)} degrees")
    print(f'the normal stresses at these angles are {shear_stress_normal(sig_x, sig_y, tau_xy, phi_shear)} and {shear_stress_normal(sig_x, sig_y, tau_xy, phi_shear + np.pi/2)}')


sig_xx = 20
sig_yy = 10
sig_zz = 0
sig_xy = 30
sig_xz = -10
sig_yz = 80

def stress_tensor(sig_xx, sig_yy, sig_zz, sig_xy, sig_xz, sig_yz):
    return np.array([[sig_xx, sig_xy, sig_xz],
                     [sig_xy, sig_yy, sig_yz],
                     [sig_xz, sig_yz, sig_zz]])

def principal_stresses(tensor):
    eigvals, eigvecs = np.linalg.eig(tensor)
    return eigvals, eigvecs

def print_3d_stresses(sig_xx, sig_yy, sig_zz, sig_xy, sig_xz, sig_yz):
    print("--------------------------------------------------")
    tensor = stress_tensor(sig_xx, sig_yy, sig_zz, sig_xy, sig_xz, sig_yz)
    eigvals, eigvecs = principal_stresses(tensor)
    print("The principal stresses are:")
    for i, val in enumerate(eigvals):
        print(f"Principal Stress {i+1}: {val}")
    print("The directions of the principal stresses are given by the corresponding eigenvectors:")
    for i, vec in enumerate(eigvecs.T):
        print(f"Direction {i+1}: {vec}")




print_stresses(sig_x, sig_y, tau_xy)
print_3d_stresses(sig_xx, sig_yy, sig_zz, sig_xy, sig_xz, sig_yz)

    
    
    
