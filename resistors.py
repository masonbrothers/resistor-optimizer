# Resistors

import itertools


def fromSI(string):
	fix = string[len(string)-1]
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
		sum += float(array[i])
	return float(sum)

def parallel(array):
	sum = 0
	for i in range(len(array)):
		if float(array[i]) == 0:
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




solutions = []
for i in range(len(resistorArray)+1):
	for c in itertools.combinations(resistorArray,i):
		c = sorted(c, key=lambda x: x)
		newStruct = {'resistors':c, 'resistance':series(c), 'type':'s'}
		solutions.append(newStruct)
		newStruct = {'resistors':c, 'resistance':parallel(c), 'type':'p'}
		solutions.append(newStruct)	

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
