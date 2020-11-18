#!/usr/bin/env python3

# https://github.com/jamini96/bch5884me.git


import numpy, sys
from matplotlib import pyplot


#open the file
file1=sys.argv[1]	
f = open(file1)
lines=f.readlines()
f.close()

t= []
a= []

# parse the file
for line in lines[3:]:
	cords = line.split()
	try:
			t.append(float(cords[0]))
			a.append(float(cords[1]))	
	except:
			print('Parsing Error',line)	
	continue

# Converts the data to numpy arrays
a=numpy.array(a)
t=numpy.array(t)

mean=numpy.mean(a)
std=numpy.std(a)

# Calculated the slopes
dt = numpy.diff(t)
da = numpy.diff(a)
s = da/dt


# creates lists containing all the values of a and t where the slopes are increasing and decreasing
threshold = 5
pos_t = []
neg_t = []
pos_a = []
neg_a = []

#increasing slopes 
for i in range(len(s)):
	if s[i] > threshold:
		pos_t.append(t[i])
		pos_a.append(a[i])
	elif s[i] < threshold: 
		neg_t.append(t[i])
		neg_a.append(a[i])

slope=[]
for i in range(len(pos_a)):
	s2=pos_a[i]/pos_t[i]
	slope.append(s2)
#decreasing slopes
neg_slope=[]
for i in range(len(neg_a)):
		if i == 0:
			continue
		else:	
			s2=neg_a[i]/neg_t[i]
			neg_slope.append(s2)
# this is calculating the points where the peaks start
startt=[]
starta=[]
for i in range(len(neg_slope)-1):
	if neg_slope[i]<neg_slope[i-1] and neg_slope[i]<neg_slope[i+1]:
		startt.append(neg_t[i])
		starta.append(neg_a[i])

# This is calculating the points where the peaks end
endt=[]
enda=[]
for i in range(len(slope)-1):
	if slope[i]<slope[i-1] and slope[i]<slope[i+1]:
		endt.append(pos_t[i])
		enda.append(pos_a[i])

for i in range(len(neg_slope)-1):
	if neg_slope[i]<neg_slope[i-1] and neg_slope[i]<neg_slope[i+1]:
		endt.append(neg_t[i])
		enda.append(neg_a[i])

#This is calculating the peaks
peakt=[]
peaka=[]
# this is plotting the peaks of the data with the mean set as the threshold
for i in range(len(a)-1):
	if a[i]>mean and a[i]>mean:
		if a[i]>a[i-1] and a[i]>a[i+1]:
			peakt.append(t[i])
			peaka.append(a[i])

#this plots the data
pyplot.plot(t,a)
pyplot.plot(startt,starta,'o',color="red")
pyplot.plot(endt,enda,'x',color="green")
pyplot.plot(peakt,peaka,'o',color="black")


pyplot.show()
for i in range(len(peakt)):
	print('Peak', i+1, "begins at time", startt[i],"and ends at", endt[i], ". It has an a max absorbance of", peaka[i],"that occurs at time", peakt[i])
	