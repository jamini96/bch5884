#!/usr/bin/env python3

# Jamini Bhagu

import sys

pdbname= sys.argv[1]
f = open(pdbname)
lines = f.readlines()
center = str(input("Where do you want to pdb file center? Enter 'COM' for Center of mass or 'GC' for gravitational center. " ))
#above commands opens the file, splits the rows into lists and requests a input for centering the data
f.close
atomlist= []
elementlist= []
xl = []
yl = []
zl =[]
masslist=[]
atom=[]	
atom1=[]
#empty lists to store values for elements and coordinates
if center == "GC":
	for line in lines:
		words= line.split()
		words[1] = int(line[6:11])
		words[5] = int(line[22:26])
		words[9]=float(line[54:60])
		words[10]=float(line[60:66])
		words[6]=float(line[30:38])
		words[7]=float(line[38:46])
		words[8]=float(line[46:54])
		elementlist.append(words[11])
		xl.append(words[6])
		yl.append(words[7])
		zl.append(words[8])
		atomlist.append(words)
	
	avgx= (sum(xl)/len(xl))
	avgy=(sum(yl)/len(yl))
	avgz=(sum(zl)/len(zl))	
	for line in lines:
		words=line.split()
		words[1] = int(line[6:11])
		words[5] = int(line[22:26])
		words[9]=float(line[54:60])
		words[10]=float(line[60:66])
		words[6]=round(float(line[30:38])-avgx,3)
		words[7]=round(float(line[38:46])-avgy,3)
		words[8]=round(float(line[46:54])-avgz,3)
		atom1.append(words)
		
	
	# above command parsed the file and type-casted the elements
	#also created separate lists for the x,y,z and elements 

		
	f=open('ATOM-G', 'w')
	for m in atom1:
		s = "{0:<6s} {1:>4d} {2:<3s} {3:>s} {4:>1s} {5:<7d} {6:<7.3f} {7:<7.3f} {8:<7.3f} {9:>5.2f} {10:<7.2f} {11:>10s}\n"
		f.write(s.format(m[0],m[1],m[2],m[3],m[4],m[5], m[6], m[7],m[8],m[9],m[10],m[11])) 
	f.close
elif center == "COM":	
	for line in lines:
		words= line.split()
		words[1] = int(line[6:11])
		words[5] = int(line[22:26])
		words[9]=float(line[54:60])
		words[10]=float(line[60:66])
		words[6]=float(line[30:38])
		words[7]=float(line[38:46])
		words[8]=float(line[46:54])
		elementlist.append(words[11])
		xl.append(words[6])
		yl.append(words[7])
		zl.append(words[8])
		atomlist.append(words)
	for elements in elementlist:
		if elements== "N":
			mass = 14.01
		elif elements == "C":
			mass = 12.01
		elif elements == "O":
			mass = 16.0
		elif elements == "H":
			mass = 1.01
		elif elements== "P":
			mass = 30.97
		elif elements=="S":
			mass = 32.07
		elif elements=="MG":
			mass = 24.30
		else:
			mass="NONE"
		masslist.append(mass)
	cxl=[]
	cyl=[]
	czl=[]
	for i,j in zip(masslist,xl):
		cx = i*j
		cxl.append(cx)
	for i,j in zip(masslist,yl):
		cy=i*j
		cyl.append(cy)
	for i,j in zip(masslist,zl):
		cz=i*j
		czl.append(cz)
	sumx=sum(cxl)
	sumy=sum(cyl)
	sumz=sum(czl)
	summass= sum(masslist)
	#print(sumx,sumy,sumz,summass)
	centerx =sumx/summass
	centery =sumy/summass	
	centerz =sumz/summass
	#print(centerx,centery,centerz)
	for line in lines: 
		words=line.split()
		words[1] = int(line[6:11])
		words[5] = int(line[22:26])
		words[9]=float(line[54:60])
		words[10]=float(line[60:66])
		words[6]=round(float(line[30:38])-centerx,3)
		words[7]=round(float(line[38:46])-centery,3)
		words[8]=round(float(line[46:54])-centerz,3)
		atom.append(words)
	f=open('ATOM-M', 'w')
	for m in atom:
		s = "{0:<6s} {1:>4d} {2:<3s} {3:>s} {4:>3s} {5:<7d} {6:<6.3f} {7:<6.3f} {8:<6.3f} {9:>5.2f} {10:<7.2f} {11:>10s}\n"
		f.write(s.format(m[0],m[1],m[2],m[3],m[4],m[5], m[6], m[7],m[8],m[9],m[10],m[11]))
	f.close	
else:
	print("Invalid Input. Please try again.")
		
		
		