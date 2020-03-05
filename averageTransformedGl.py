import csv
import numpy as np
import math
from statistics import mean

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

 			# weighted average of glucose calculation
			# R = 100 mg/dL
 			avg_transGl = 1000 * pow(abs(np.log(int(row[2]) / 100)), 3)
			
 			gluVal.append(avg_transGl)



# mean calculation of gluVal
mean_Glu = mean(gluVal)

print('M100 (MR with R = 100 mg/dL): \t', mean_Glu)

