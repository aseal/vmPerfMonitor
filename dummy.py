#!/usr/bin/python

from time import sleep
import random
import sys

def openFiles():
	num = random.randint(10,100)
	files = [open('README.txt', 'r') for i in range(num)]
	return files

def MatMul():
	row1 = col2 = random.randint(10,1000)
	col1 = row2 = random.randint(10,1000)

	X = [[random.randint(100, 1000) for i in range(col1)]
									for j in range(row1)]
	Y = [[random.randint(100, 1000) for i in range(col2)]
									for j in range(row2)]
	Z = [[0 for i in range(row1)] for j in range(col2)]

	for i in range(row1):
		for j in range(col2):
			for k in range(col1):
				Z[i][j] += X[i][k] * Y[k][j]

#	for z in Z:
#		print z

seconds = int(sys.argv[1]) * 60
files = openFiles()
MatMul()

sleep(seconds)
