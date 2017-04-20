import time
import sys

li = []

li.append(0)
li.append(1)

i = 2

def printNext():
	global i
	li.append(li[i-2] + li[i-1])
	i = i + 1
	return li[i-1]
	
print "%d," % li[0],
sys.stdout.flush()
time.sleep(1)

print "%d," % li[1],
sys.stdout.flush()
time.sleep(1)

while True:
	print "%d," % printNext(),
	sys.stdout.flush()
	time.sleep(1)
