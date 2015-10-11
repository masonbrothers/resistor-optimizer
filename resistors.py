# Resistors

import itertools


def fromSI(string):
	multipiler = 1
	if len(string) > 1:
		fix = string[-1]
		if isinstance(string[len(string)-1], (int, long)) != True:
			string = string[:-1]
		if fix == 'k':
			multipiler = 1e3
		elif fix == 'M':
			multipiler = 1e6
		elif fix == 'G':
			multipiler = 1e9
		elif fix == 'T':
			multipiler = 1e12
		elif fix == 'm':
			multipiler = 1e-3
		elif fix == 'u':
			multipiler = 1e-6
		elif fix == 'n':
			multipiler = 1e-9
		elif fix == 'p':
			multipiler = 1e-12
		else:
			multipiler = 1
	return float(multipiler*float(string))

def percentError(theoretical, emperical):
	return (float(emperical)-float(theoretical))/float(theoretical)*100

def series(array):
	sum = 0

	for i in range(len(array)):
		if isinstance(array[i],list):
			if array[i][0] == "s":
				sum += float(series(array[i][1:]))
			elif array[i][0] == "p":
				sum += float(parallel(array[i][1:]))
		else:
			sum += float(array[i])
	return float(sum)

def parallel(array):
	sum = 0
	for i in range(len(array)):
		if isinstance(array[i],list):
			if array[i][0] == "s":
				sum += 1/float(series(array[i][1:]))
			elif array[i][0] == "p":
				sum += 1/float(parallel(array[i][1:]))
		elif float(array[i]) == 0:
			sum += float('inf')
		else:
			sum += 1/float(array[i])
	if float(sum) == 0:
		return float('inf')
	else:
		return 1/float(sum)







print "Welcome to the resistor optimization program!\nThis program is designed to find the best resistance values for mulitple resistor resistors.\nNote: You can enter in the engineering suffix after your resistor!"
message1 = "Hello! Please enter a resistor value in ohms: "
goal = float(fromSI(raw_input(message1)))
message2 = "Please enter the resistors you have sperated by spaces: "
resistorArray = map(fromSI,raw_input(message2).split())


def getOtherElements(listOne, ListTwo):
	#returns elements in listOne that are not in list 2
	outputList = []
	for i in range(listOne):
		isThere = 0
		for j in range(ListTwo):
			if (listOne[i] == listTwo[i]):
				isThere = 1
		if isThere == 0:
			outputList.push(listOne[i])


def generateList(resistorArray):
	remainingList = resistorArray
	start = ['s','p']
	for i in range(len(start)):
		subarray.push(start[i])
		for j in range(len(resistorArray)+1):
			for c in itertools.combinations(resistorArray,j):
				for j in range(len(c)):
					subarray.push(c[j])
				newList = []
				if i == 0:
					newList.push(start[1])
				if i == 1:
					newList.push(start[0])
				otherElements = getOtherElements(resistorArray,c)
				
				for k in range(len(otherElements)):
					newList.push(otherElements[i])
				generateList(otherElements)
	return 




def generateAllCircuits(resistorArray):
	solutions = []
	for i in range(len(resistorArray)+1):
		for c in itertools.combinations(resistorArray,i):
			subarray = []
			
	return solutions

		


newCircuit = ['p',['s',4,3],2,3,4]
#newCircuit = ['',['s',4,3],]




def evaluateCircuit(circuit):
	value = 0
	for i in range(len(newCircuit)):
		if newCircuit[0] == 'p':
			value = parallel(newCircuit[1:])
		elif newCircuit[0] == 's':
			value = series(newCircuit[1:])
	return value


print evaluateCircuit(newCircuit)








'''
s = sorted(solutions, key=lambda x: abs(goal - x["resistance"]))

i = 0

while True:
	if s[i]['resistors'] == s[i+1]['resistors'] and s[i]['resistance'] == s[i+1]['resistance']:
		s.pop(i)
		i = i - 1
	i = i + 1
	if i == len(s)-2:
		break

print "\nComparing the generated values to the given value of " + str(goal) + "ohms."

print "Rank\tType\tohms\tP_Error\tResistors"
print "----------------------------------------------------------------------"
for i in range(len(s)):
	outputString = str(i+1) + "\t" + str(s[i]['type'])
	outputString += "\t%.1f" % s[i]['resistance']
	outputString += "\t%.1f" % percentError(goal,s[i]['resistance'])
	outputString += "\t" + str(s[i]['resistors'])
	print outputString
'''