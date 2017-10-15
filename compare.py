print ("Nhap so thu nhat")
number1 = input()
number1 = float(number1)
print ("Nhap so thu hai")
number2 = input()
number2 = float(number2)
if number1>number2:
	bigger = number1
	smaller = number2
elif number1<number2:
	bigger = number2
	smaller = number1
else:
	equal = True

if equal == True:
	print ("Hai so bang nhau")
else:
	print ("Bigger number is:", bigger)
	print ("Small number is:", smaller)

