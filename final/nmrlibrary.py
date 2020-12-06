#!/usr/bin/env python

# https://github.com/jamini96/bch5884me.git

import sys, numpy
from matplotlib import pyplot

# this function parses the files
def readfile(filename):
	""" Parses the file and returns lists"""
	file=open(filename)
	lines=file.readlines()
	file.close()
	
	nmrdict=[]
	
	for line in lines:
		cords=line.split()
		cords[0]=numpy.array(int(cords[0]))
		cords[1]=numpy.array(int(cords[1]))
		cords[2]=numpy.array(float(cords[2]))
		cords[3]=numpy.array(float(cords[3]))
		nmrdict.append(cords)
	return nmrdict

def corrcoeff(nmrdict1,nmrdict2):

	intensity1=[]
	intensity2=[]
	x1=[]
	x2=[]
#creating a list with intensity values and chemical shift values
	for i in nmrdict1:
		intensity1.append(i[1])
		x1.append(i[3])

	for i in nmrdict2:
		intensity2.append(i[1])
		x2.append(i[3])
#this part of the function is finding the mean for the intensities in each of the NMR data	
	n=len(intensity1)
	mean1=sum(intensity1)/n
	mean2=sum(intensity2)/n

	std1=numpy.std(intensity1)
	std2=numpy.std(intensity2)
	
# this part of the function is using the mean and standard deviation to find the covariance
	newsum=0
	for i,j in zip(intensity1,intensity2):
		newsum+=(i-mean1)*(j-mean2)
	cov=newsum/(n-1)
	R = cov/(std1*std2)
	return 	R

# this is calculating the similarity between the two spectra	
def similarity(R):
	
	r = R/(1-R)
	s = 10*numpy.log(r)
	return s
	
# this function is plotting the raw nmr data
def nmrplot(nmrdict1,nmrdict2):
	intensity1=[]
	intensity2=[]
	x1=[]
	x2=[]

	for i in nmrdict1:
		intensity1.append(i[1])
		x1.append(i[3])

	for i in nmrdict2:
		intensity2.append(i[1])
		x2.append(i[3])
	
	# plots the data for the bulk experiment
	pyplot.figure()	
	pyplot.plot(x1,intensity1,color='r')
	pyplot.savefig('Bulk plot.png')
	
	# plots the data for the interface experiment
	pyplot.figure()	
	pyplot.plot(x2,intensity2,color='g')
	pyplot.savefig('Interface plot.png')
	
	
	# plots the overlay of the two experiments
	pyplot.figure()	
	pyplot.plot(x1,intensity1,color='r')
	pyplot.plot(x2,intensity2,color='g')
	pyplot.savefig('Bulk and interface plot.png')
	

# the function below is to output an html file with an image of the plot from above and the R and s values 
def openHTML(file,R,s):
	f=open(file, 'w')

	f.write("""<!DOCTYPE html>
	<html>
	<head> 
		<title> Jamini Bhagu's Final Project </title>
		<style>
			div {
				font-family: Times New Roman;
				text-align:center;
				line-height: 2.0;
			}
			img {
				height: 25%%
				width: 25%%}
		</style>
	<body>
	<div>	
	 Biopharmaceuticals, like mAbs, are becoming the drug of choice for various illness like cancer. Studies are currently being conducted on using mAbs to treat Covid-19.
     Monoclonal antibodies are a type of amphiphilic protein. Due to this property, the protein can undergo conformational changes at hydrophobic interfaces like air/water or oil water/interfaces.
	 These interfaces are present when drugs are administered using IV bags or syringes. Studies have been conducted using methods like UV spectroscopy, Nuclear reflection and CD; however, these methods aren't able to provide detailed information on the changes in the conformation. We would like to use 1D and 2D  NMR spectroscopy to study the structure of the mAbs in the bulk, and at a silicone oil interface. 
	 We then plan to add a surfactant, to see if that will resolve the issue of adsorption. We also plan to chemically denature mAbs to better compare the data.
	 The NMR data will be analyzed and compared using a spectral similarity calculation
	</div>
	<div>
	<img src= 'Bulk and interface plot.png' /> 
	</div>
	<div>
	This figure shows the overlay of NMR spectra of the bulk and the interface of mAbs.
	The bilk is shown in red and the the interface is shown in green
	</div>
	<div>
	<img src= 'Bulk plot.png'/>
	</div>
	<div>
	This figure shows the NMR spectra of the bulk sample of mAbs.
	</div>
	<div>
	<img src= 'Interface plot.png'/> 
	</div>
	<div>
	This figure shows the NMR spectra of the interface sample of mAbs.
	</div>
	<div>
	The correlation coefficient for the two data sets is %f
	The similarity of the two spectra was calculated using the function
	</div>
	<div>
	 S = 10*log(R/1-R)
	</div>
	<div>
	where R is the correlation coefficient calculated above.
	The spectral similarity for these two data sets is %f
	</div>
	</body>""" %(R,s))
	f.close()
	