#!/usr/bin/env python

# https://github.com/jamini96/bch5884me.git

import math, sys, numpy
from matplotlib import pyplot

def readfile(filename):
	""" Parses the file and returns lists"""
	file=open(filename)
	lines=file.readlines()
	file.close()
	
	nmrdict=[]
	
	for line in lines:
		cords=line.split()
		#d={}
		cords[0]=numpy.array(int(cords[0]))
		cords[1]=numpy.array(int(cords[1]))
		cords[2]=numpy.array(float(cords[2]))
		cords[3]=numpy.array(float(cords[3]))
		nmrdict.append(cords)
	return nmrdict

def corrcoeff(nmrdict1,nmrdict2):

#this part of the function is finding the mean for the intensities in each of the NMR data	
	n=len(nmrdict1)
	sum1=0
	sum2=0
	for i in nmrdict1:
		sum1+=i[1]
	
	for j in nmrdict2:
		sum2+=j[1]

	mean1=sum1/n
	mean2=sum2/n
	
#this part of the function is finding the standard deviation for the intensities in each of the NMR data	
	
	nm1=0
	nm2=0
	for i in nmrdict1:
		nm1+=(i[1]-mean1)**2
	
	for j in nmrdict2:
		nm2+=(i[1]-mean2)**2
	std1=numpy.sqrt(nm1/n)
	std2=numpy.sqrt(nm2/n)
	
# this part of the function is using the mean and standard deviation to find the covariance
	newsum=0
	for i,j in zip(nmrdict1,nmrdict2):
		newsum+=(i[1]-mean1)*(j[1]-mean2)

# This is calculating the covariance and the correlation coefficient	
	cov=newsum/(n-1)
	R = cov/(std1*std2)
	return 	R
# this function is plotting the raw nmr data
def nmrplot(nmrdict1,nmrdict2):
	intensity1=[]
	intensity2=[]
	
	for i in nmrdict1:
		intensity1.append(i[1])
	
	for i in nmrdict2:
		intensity2.append(i[1])
	
	pyplot.plot(intensity1,color='r')
	pyplot.plot(intensity2,color='g')
	pyplot.show()


if __name__=="__main__":
	file1=sys.argv[1]
	file2=sys.argv[2]
	nmrdict1=readfile(file1)
	nmrdict2=readfile(file2)
	
	nmrplot(nmrdict1,nmrdict2)
		
	R=corrcoeff(nmrdict1,nmrdict2)
	print(R)
