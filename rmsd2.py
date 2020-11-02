#!/usr/bin/env python3

# Jamini Bhagu -- https://github.com/jamini96/bch5884me.git

import sys, math

def readfile1(pdbname1):
	'''Parse the pdb file and returns type casts the elements'''
	f=open(pdbname1)
	lines = f.readlines()
	f.close
	
	#empty lists to store values for elements and coordinates
	contents1 = []
	
	# the following code is parsing the pdb file	
	for line in lines:
		if line[:4]=="ATOM":
			pdbdict={}
			pdbdict['name']=line[0:6]
			pdbdict['numb']=int(line[6:11])
			pdbdict['type']=line[12:16]
			pdbdict['loc']=line[16:17]
			pdbdict['residue']=line[17:20]
			pdbdict['chain']=line[21:22]
			pdbdict['rnumb']=int(line[22:26])
			pdbdict['code']=line[26:27]
			pdbdict['x']=float(line[30:38])
			pdbdict['y']=float(line[38:46])
			pdbdict['z']=float(line[46:54])
			pdbdict['occupancy']=float(line[54:60])
			pdbdict['tempfac']=float(line[60:66])
			pdbdict['element']=line[76:78]
			pdbdict['charge']=line[78:80]
			contents1.append(pdbdict)
	return contents1

#this function performs the same operation as above, just for the second pdb file
def readfile2(pdbname2):
	f2 = open(pdbname2)
	lines2 = f2.readlines()
	f2.close
	
	contents2 = []
	for line in lines2:
		if line[:4]=="ATOM":
			pdbdict2={}
			pdbdict2['name']=line[0:6]
			pdbdict2['numb']=int(line[6:11])
			pdbdict2['type']=line[12:16]
			pdbdict2['loc']=line[16:17]
			pdbdict2['residue']=line[17:20]
			pdbdict2['chain']=line[21:22]
			pdbdict2['rnumb']=int(line[22:26])
			pdbdict2['code']=line[26:27]
			pdbdict2['x']=float(line[30:38])
			pdbdict2['y']=float(line[38:46])
			pdbdict2['z']=float(line[46:54])
			pdbdict2['occupancy']=float(line[54:60])
			pdbdict2['tempfac']=float(line[60:66])
			pdbdict2['element']=line[76:78]
			pdbdict2['charge']=line[78:80]
			contents2.append(pdbdict2)
	return contents2

def rmsd(atomlist1,atomlist2): 
	'''Returns the root-mean-squared deviation between two pdb files.'''
	sumx=0
	sumy=0
	sumz=0
	total=0
	n = len(atomlist1)
	for atom1,atom2, in zip(atomlist1,atomlist2):
		sumx+=(atom1['x']-atom2['x'])**2 # this is performing the (vxi-wxi)^2 portion of the rmsd equation where v and w are for the two pdbfiles
		sumy+=(atom1['y']-atom2['y'])**2 # same as above but for the y
		sumz+=(atom1['z']-atom2['z'])**2 # same as above but for the but for z
		total+= sumx + sumy + sumz #sums up all of the x,y,z sums from above
		
	rmsd = math.sqrt((1/n)*total) # calculates the rmsd using the values determined above
	return rmsd
		
if  __name__=="__main__":
	pdbname1=sys.argv[1]		
	pdbname2=sys.argv[2]
	atomlist1=readfile1(pdbname1)
	atomlist2=readfile2(pdbname2)
	
	root_mean = rmsd(atomlist1,atomlist2)
	print("the root-mean-squared deviation is", root_mean)
		
	
	
	

