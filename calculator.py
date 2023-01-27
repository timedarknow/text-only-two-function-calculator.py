from time import sleep

print('options 1 or 2')

userchoice = input('enter choice 1 add 2 sub:')



while (userchoice != '1') | (userchoice != '2'):
    if userchoice == '1':
      add1 = int(input('enter first num: '))
      add2 = int(input('enter second num: '))
      print(add1 + add2)
      userchoice = '3'
    
    
    elif userchoice == '2':
      sub1 = int(input('second num to sub: '))
      sub2 = int(input('second num to sub: '))
      print(sub1 - sub2)
      userchoice = '3'
    
    elif userchoice == '3':
      sleep(120)
    
      break


    


