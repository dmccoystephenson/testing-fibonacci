import time
import sys

sleepTime = .1

li = []

li.append(0)
li.append(1)

i = 2

def printNext():
	global i
	li.append(li[i-2] + li[i-1])
	i = i + 1
	return li[i-1]

x = 1	
print "[%d] %d" % (x, li[0])
time.sleep(sleepTime)
x += 1

print "[%d] %d" % (x, li[1])
time.sleep(sleepTime)
x += 1

while True:
	print "[%d] %d" % (x, printNext())
	time.sleep(sleepTime)
	x += 1
