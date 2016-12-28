#! /usr/bin/python
def splitExp(exp):
	operators = ["+", "-", "*", "/", "%", "**"]
	for operate in operators:
		splitArr = exp.split(operate)
		if(len(splitArr) == 2):
			num1 = float(splitArr[0])
			num2 = float(splitArr[1])
			if(operate == "+"):
				return num1 + num2
			elif operate == "-":
				return num1 - num2
			elif operate == "/":
				return num1 / num2
			elif operate == "%":
				return num1 % num2
			elif operate == "**":
				return num1 ** num2			

while True:
	print "Input expression:"
	expre = raw_input()
	print splitExp(expre)
	expre 
	if expre == ":q":
		break

