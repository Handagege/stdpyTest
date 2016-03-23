#!/usr/bin/python
#Filename:func_doc.py

def printMax(x,y):
	'''Print the maximum of two numbers.

	The two values must be integers.'''

#print printMax.__doc__

sentence1 = 'the supper man hi...'
sentence2 = sentence1
sentence2 += "add content"
sentence3 = sentence2.replace(' ','_')
print "sentence1: "+sentence1
print "sentence2: "+sentence2
print "sentence3: "+sentence3
