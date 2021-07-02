def twoNumberSum(array, targetSum):
	myDict = {}
	answer = []
	for number in array:
		soughtNumber = targetSum - number
		if myDict.get(soughtNumber):
			answer = (number, soughtNumber)
		else:
			myDict[number] = True;
    return answer

