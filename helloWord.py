#!/usr/bin/python
#Filename:helloWorld.py


def printMax(a,b):
	if a>b:
		print a,' is Max!'
	else:
		print b,' is Max!'

number=23

guess=int(raw_input("Enter an integer:"))

if guess==number:
	print("Congratulations, you guessed it.")
	print("but you do not win any prizes!")
elif guess<number:
	print("No, it is a little higher than that")
else:
	print("No, it is a little lower than that")


for i in range(0,5):
	print i

print("Done")

while True:
	guess1=int(raw_input("Enter an integer:"))
	guess2=int(raw_input("Enter an integer:"))
	if( guess1 != guess2 ):
		printMax(guess1,guess2)
	else:
		break

