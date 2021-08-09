import calculator
print("Enter the numbers")
print("If completed press q")
l=[]
while(1):
	n=input()
	q="q"
	if(n==q):
		break
	else:
		l.append(int(n))
print("Enter the operation to be performed : if addition press 1 for + or subtraction press 0 -:")
symbol=int(input())
if (symbol== 1):
	print(calculator.add(l))
if(symbol== 0):
	print(calculator.subtract(l))
