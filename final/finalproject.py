#!/usr/bin/env python

# https://github.com/jamini96/bch5884me.git

import nmrlibrary
import sys

if len(sys.argv) != 4:
		print("Usage: finalproject.py <nmrfile1.txt>  <nmrfile2.txt> <outputfile.html>")
		sys.exit()

# Raw Data from NMR
		
file1=sys.argv[1]
file2=sys.argv[2]

# New output HTML file

newfile=sys.argv[3]
f=open(newfile,'w')

# uses the function from the library to parse the files
nmrdict1=nmrlibrary.readfile(file1)
nmrdict2=nmrlibrary.readfile(file2)

#plots the data
nmrlibrary.nmrplot(nmrdict1,nmrdict2)

# calculates the correlation coefficient and the spectral similarity
R=nmrlibrary.corrcoeff(nmrdict1,nmrdict2)
s=nmrlibrary.similarity(R)

#outputs the HTML file
nmrlibrary.openHTML(newfile,R,s)