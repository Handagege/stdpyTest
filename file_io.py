#!/usr/bin/python
#Filename=file_io.py

print "This is My IO exercise py...\n"

text_file = open("poem_Pushkin.txt","w")
#text_file.write('\nzhanghan edit\n')


lines = ["zhanghan edit\n","weibo\n","staff\n","bit\n","Tue Apr 14 14:31:30 CST 2015\n"]
text_file.writelines(lines)
text_file.close()

text_file = open("poem_Pushkin.txt","r")

print(text_file.read())

#print(text_file.readline())

#lines = text_file.readlines()

#for sentence in lines:
#	print sentence.replace(' ','_')

text_file.close()
