#!/usr/bin/env python3

# Jamini Bhagu

import sys

pdbname= sys.argv[1]
f = open(pdbname)
lines = f.readlines()

atomlist=[]
for line in lines:
	words= line.split()
	words[1] = int(words[1])
	words[5] = int(words[5])
	words[6]=float(words[6])
	words[7]=float(words[7])
	words[8]=float(words[8])
	words[9]=float(words[9])
	words[10]=float(words[10])
	atomlist.append(words)
#print(atomlist)
f.close

f=open('ATOM', 'w')

for atom in atomlist:
	s = "{0:<5s} {1:<5d} {2:<5.3s} {3:<5s} {4:<5s} {5:<5d} {6:<7.3f} {7:<7.3f} {8:<7.3f} {9:<7.3f} {10:<7.3f} {11:<7s}\n" #{2:s} {3:s} {4:s} {5:i} {6:6.3f} {7:6.3f} {8:6.3f} {9:6.3f} {10:6.3f} {11:s}\n"
	f.write(s.format(atom[0],atom[1],atom[2],atom[3],atom[4],atom[5],atom[6],atom[7],atom[8],atom[9],atom[10],atom[11]))
f.close

	