import calculator
print("Enter the numbers")
print("If completed press q")
while(1):
	n=input()
	q="q"
	if(n==q):
		break
	else:
		l.append(int(n))
print("Enter the operation to be performed : if addition press + or 
	subtraction -:")
symbol=int(input())
if (symbol== "+"):
	print(calculator.add(l))
if(symbol== "-"):
	print(calculator.subtract())
