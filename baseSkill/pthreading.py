#!/usr/bin/python
# -*- coding: utf-8 -*-


import threading
import time
from time import ctime,sleep


def music(func,lock):
	lock.acquire()
        for i in range(3):
                print "I was listening to %s. %s" %(func,ctime())
                sleep(1)
	lock.release()

def move(func,lock):
	lock.acquire()
        for i in range(3):
                print "I was at the %s! %s" %(func,ctime())
                sleep(1)
	lock.release()

def test1():
	threadLock = threading.Lock()
	threads = []
	t1 = threading.Thread(target=music,args=('zhanghan',threadLock))
	threads.append(t1)
	t2 = threading.Thread(target=move,args=('liuhuan',threadLock))
	threads.append(t2)
        print threads
	threads[0].start()
	threads[1].start()
	threads[0].join()
	threads[1].join()
        print "all over %s" %ctime()

def test2():
	exitFlag = 0
	
	class myThread (threading.Thread):   #继承父类threading.Thread
		threadLock = threading.Lock()
		def __init__(self, threadID, name, counter):
			threading.Thread.__init__(self)
			self.threadID = threadID
			self.name = name
			self.counter = counter
		def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数 
			myThread.threadLock.acquire()
			print "Starting " + self.name
			self.print_time(self.name, self.counter, 5)
			myThread.threadLock.release()
			print "Exiting " + self.name
	
		def print_time(self, threadName, delay, counter):
			while counter:
				if exitFlag:
					thread.exit()
				time.sleep(delay)
				print "%s: %s" % (threadName, time.ctime(time.time()))
				counter -= 1
	# 创建新线程
	thread1 = myThread(1, "Thread-1", 1)
	thread2 = myThread(2, "Thread-2", 1)

	# 开启线程
	thread1.start()
	thread2.start()

	print "Exiting Main Thread"



if __name__ == '__main__':
	test1()

