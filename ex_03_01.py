
nhours = input("Enter Hours")
nrate = input("Enter Rate")

hours = float(nhours)
rate = float(nrate)

if hours > 40:
	regular = hours * rate
	extra = (hours - 40.0) * (rate * 0.5) 
	pay = regular + extra
	#print(pay)
else:
	pay = hours * rate
	#print(pay)
print(pay)


