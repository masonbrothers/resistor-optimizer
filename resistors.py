# Resistors

import itertools

message1 = "Hello! Please enter a resistor value in ohms: "
goal = float(raw_input(message1))
#message2 = "Please enter a percent error threshold (%): "
#error = float(raw_input(message2))
message3 = "Please enter the resistors you have sperated by spaces: "
# Enter each resistor value as R(N) where R is the resistance, and N is the number of resistors.\n
resistorArray = map(float,raw_input(message3).split())

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

'''
def evaluateResistors(resistors):
	for i in range(len(resistors)):
		if type(resistors[i]) is list:
			resistors[i] = evaluateResistors(resistors[i])
			# try to add up in series. If we cannot, ma
		elif resistors[i] == "s"
'''

#print parallel(resistorArray)

'''
def useArraySeries(array,n):
	for i in range(len(array)):
		if (percentError(goal) < error)

'''

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
	
	#print s[i]
	#print s[i+1]
	#print s[i]['resistors'] == s[i+1]['resistors']
	#print i
	
	#raw_input()
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

#print s