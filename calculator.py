from time import sleep

print('options 1 or 2')

userchoice = input('enter choice 1 add 2 sub:')

if (userchoice == '1' or userchoice == '2'):#the while loop was just pointless. here we are checking if the input is valid
	if userchoice == '1':
		add1 = int(input('enter first num: '))
		add2 = int(input('enter second num: '))
		print(add1 + add2)#having the user choice = 3 to break from the loop is the same as just not having a loop

	elif userchoice == '2':#i know that this could just be an else, but this is a lot easier to read
		sub1 = int(input('first num to sub: '))#minor typo
		sub2 = int(input('second num to sub: '))
		print(sub1 - sub2)
else:
	print("input is invalid!")

sleep(5)#2 minutes is a long time