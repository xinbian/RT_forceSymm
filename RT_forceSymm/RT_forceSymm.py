# -*- coding: utf-8 -*-
"""
#you can use this to extend RT domain in z direction
#orginal nx ny nz after nx ny 2*nz
#velocity is set to zero 
#density is set to horizotal average at top and bottom with 40 grid porints offset
#pressure is similar to density and use hydrostatic equation rho*g*dz
@author: Xin
"""

import h5py
import numpy as np
import os
import os.path

curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath,os.pardir))
parentDir = os.path.abspath(os.path.join(curDir,os.pardir)) 

#not used 
#rhoL=1
#rhoH=1.0833

#specify inout parameters here
g=1.0
inFile='temp.h5'
outFile="tests_single_new.h5"
#input done

mylist = [parentDir,'/',inFile]
delimiter = ''
filepath = delimiter.join(mylist)
#nz enlarged only 
variable = ['PVx','PVy','PVz','PPress', 'Prho']
h5file = h5py.File(filepath,'r')
mylist = [parentDir,'/',outFile]
delimiter = ''
filepath = delimiter.join(mylist)
h5new = h5py.File(filepath,'w')

istep='001000'
#read dataset dimensions
mylist = ['Fields/','Prho','/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)
nz=m1.shape[0]
ny=m1.shape[1]
nx=m1.shape[2]
dz=3.2/nz


 
#Vy antisymmetric
delimiter = ''
mylist = ['Fields/',variable[1],'/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)

m2=np.zeros((nz, ny/2, nx))
m2=(m1[:,0:ny/2,:]-m1[:,ny-1:ny/2-1:-1,:])/2
m1[:,0:ny/2,:]=m2
m1[:,ny-1:ny/2-1:-1,:]=-m2
h5new.create_dataset(filepath,data=m1)
#
#Vz
delimiter = ''
mylist = ['Fields/',variable[2],'/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)

m2=np.zeros((nz, ny/2, nx))
m2=(m1[:,0:ny/2,:]+m1[:,ny-1:ny/2-1:-1,:])/2
m1[:,0:ny/2,:]=m2
m1[:,ny-1:ny/2-1:-1,:]=m2
h5new.create_dataset(filepath,data=m1)
##rho
delimiter = ''
mylist = ['Fields/',variable[4],'/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)


m2=np.zeros((nz, ny/2, nx))
m2=(m1[:,0:ny/2,:]+m1[:,ny-1:ny/2-1:-1,:])/2
m1[:,0:ny/2,:]=m2
m1[:,ny-1:ny/2-1:-1,:]=m2
h5new.create_dataset(filepath,data=m1)
#
#
#
#
#
#
#
#
#
#
##pressure

delimiter = ''
mylist = ['Fields/',variable[3],'/',istep]
filepath = delimiter.join(mylist)
databk = h5file.get(filepath)
m1 = np.array(databk)

m2=np.zeros((nz, ny/2, nx))
m2=(m1[:,0:ny/2,:]+m1[:,ny-1:ny/2-1:-1,:])/2
m1[:,0:ny/2,:]=m2
m1[:,ny-1:ny/2-1:-1,:]=m2
h5new.create_dataset(filepath,data=m1)
#

#
#
#
h5file.close()
h5new.close()

#f = open('output.d','w')
#for zz_ref in range(nz):
# f.write("%4s\t%10s\n" % (zz_ref, np.mean(m1[zz_ref,:,:])))
#f.close()
    
    
    
