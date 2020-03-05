import csv
import numpy as np
from statistics import mean
from statistics import stdev

# get file name
fileIn = input("File name: \t")

# get patient ID 
pID = input("Patient ID: \t")


with open(fileIn, 'r') as csv_file:
 	csv_reader = csv.reader(csv_file, delimiter = ',')

 	# array to store glu values
 	gluVal = []

 	next(csv_reader)

 	# loops through data appends data to gluVal
 	for row in csv_reader:
 		if row[0] == pID:
 			gluVal.append(int(row[2]))

# standard deviation calculation of gluVal
sd_Glu = stdev(gluVal)

# mean calculation of gluVal
mean_Glu = mean(gluVal)

# J-index calculation
j_index = 0.001 * (mean_Glu + sd_Glu) ** 2

print('J-index: \t', j_index)
