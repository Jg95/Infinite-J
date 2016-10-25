import random

while (1):
	#A =  random.randrange(0, 7, 1)
	A=0
	B =  random.randrange(90, 99, 1)
	code = "[" + str(A) + ";" + str(B) + "m"
	print chr(27)+ code + "j",
