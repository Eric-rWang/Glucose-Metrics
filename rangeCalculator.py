import csv

# get file name
fileIn = input("File name: \t")

# get patient ID 
pID = input("Patient ID: \t")


with open(fileIn, 'r') as csv_file:
 	csv_reader = csv.reader(csv_file, delimiter = ',')

 	nCount = 0

 	numInRange_80_200 = 0
 	numInRange_70_180 = 0
 	numInRange_70_140 = 0

 	numBelowRange_80 = 0
 	numBelowRange_50 = 0

 	numAboveRange_250 = 0
 	numAboveRange_200 = 0
 	numAboveRange_180 = 0
 	numAboveRange_140 = 0

 	next(csv_reader)

 	for row in csv_reader:
 		if row[0] == pID:
 			print(row[0], row[2])
 			nCount += 1

 			# percent in range counters
 			if int(row[2]) >= 80 and int(row[2]) <= 200:
 				numInRange_80_200 += 1

 			if int(row[2]) >= 70 and int(row[2]) <= 180:
 				numInRange_70_180 += 1

 			if int(row[2]) >= 70 and int(row[2]) <= 140:
 				numInRange_70_140 += 1

 			# percent below range counters
 			if int(row[2]) <= 80:
 				numBelowRange_80 += 1

 			if int(row[2]) <= 50:
 				numBelowRange_50 += 1

 			# percent above range counters
 			if int(row[2]) >= 250:
 				numAboveRange_250 += 1

 			if int(row[2]) >= 200:
 				numAboveRange_200 += 1

 			if int(row[2]) >= 180:
 				numAboveRange_180 += 1

 			if int(row[2]) >= 140:
 				numAboveRange_140 += 1



# percent in range 80 200
percentInRange_80_200 = numInRange_80_200 / nCount * 100

# percent in range 70 180
percentInRange_70_180 = numInRange_70_180 / nCount * 100

# percent in range 70 140
percentInRange_70_140 = numInRange_70_140 / nCount * 100


# percent below range 80
percentBelowRange_80 = numBelowRange_80 / nCount * 100

# percent below range 50
percentBelowRange_50 = numBelowRange_50 / nCount * 100


# percent above 250
percentAboveRange_250 = numAboveRange_250 / nCount * 100

# percent above 200
percentAboveRange_200 = numAboveRange_200 / nCount * 100

# percent above 180
percentAboveRange_180 = numAboveRange_180 / nCount * 100

# percent above 140
percentAboveRange_140 = numAboveRange_140 / nCount * 100

print('pID: ', pID, '\n')
print('percent in range 80 - 200: \t', percentInRange_80_200)
print('percent in range 70 - 180: \t', percentInRange_70_180)
print('percent in range 70 - 140: \t', percentInRange_70_140, '\n')
print('percent below range 80: \t', percentBelowRange_80)
print('percent below range 50: \t', percentBelowRange_50, '\n')
print('percent above range 250: \t', percentAboveRange_250)
print('percent above range 200: \t', percentAboveRange_200)
print('percent above range 180: \t', percentAboveRange_180)
print('percent above range 140: \t', percentAboveRange_140)





