
def simpleGeneratorFun():
	yield 1
	yield 2
	yield 330


for value in simpleGeneratorFun():
	print(value)