
def add(l):
	sum=0
	for i in l:
		sum+=i
	return sum

def subtract(l):
	diff=l[0]
	length=len(l)
	for i in range(1,length):
		diff-=l[i]
	return diff

