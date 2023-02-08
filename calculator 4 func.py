from time import sleep

print('options 1, 2, 3 or 4')

userchoice = input('enter choice 1 add 2 sub 3 mult 4 div:')

#again same issues as 2 function calc
if (userchoice == '1' or userchoice == '2' or userchoice =='3' or userchoice == '4'):
	if userchoice == '1':
		add1 = int(input('enter first num to add: '))
		add2 = int(input('enter second num to add: '))
		print(add1 + add2)

	elif userchoice == '2':
		sub1 = int(input('first num to subtract: '))
		sub2 = int(input('second num to subtract: '))
		print(sub1 - sub2)

	elif userchoice == '3':
		mult1 = int(input('first num to multiply: '))
		mult2 = int(input('second num to multiply: '))
		print(mult1 * mult2)

	elif userchoice == '4':
		div1 = int(input('first num to divide: '))
		div2 = int(input('second num to divide: '))
		print(div1 / div2)

else:
	print("input is invalid!")

sleep(5)