#!/usr/bin/python

class people:
    name = ''
    age = 0
    __weight = 0
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s is speaking: I am %d years old" %(self.name,self.age))


p = people('tom',10,30)
p.speak()

str1 = '20150415'
str2 = '20150415333'
str3 = '20150416'

print str1+'_compare_'+str2+'='+str(cmp(str1,str2))
print str3+'_compare_'+str2+'='+str(cmp(str3,str2))
