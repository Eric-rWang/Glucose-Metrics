import csv
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
 			gluVal.append(int(row[2]))


# mean calculation of gluVal
mean_Glu = mean(gluVal)

print('mean glu value: \t', mean_Glu)
