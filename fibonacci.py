import time
li = []

li.append(0)
li.append(1)

i = 2

def printNext():
	global i
	li.append(li[i-2] + li[i-1])
	print li[i]
	i = i + 1
	
print li[0]
time.sleep(1)

print li[1]
time.sleep(1)

while True:
	printNext()
	time.sleep(1)
