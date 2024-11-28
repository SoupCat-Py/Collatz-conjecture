import random
print('Soup\'s Collatz Conjecture Simulator version 2')
print('')
print('')

#main loop/function
def start(style):
    while True:
        numList = []
        asking = True
        #get number or max value
        while asking:
            if style == 'input':
                number = input('enter any number ')
                asking = False
            elif style == 'random':
                number = input('enter maximum value ')
                asking = False

            #see if the input is a number, infinity, or invalid
            try:
                number = int(number)
                asking = False
            except ValueError:
                if number.lower() == 'inf' or number.lower() == 'infinity':
                    print('nuh uh >:P')
                else:
                    print('invalid input ')
                asking = True

        #set random range
        if style == 'random':
            number = random.randint(1,number)
            print(f'''chosen number: {number}
            ''')

        #actual collatz math
        while number != 1:
            #chech if odd or even
            if '.5' not in str(number / 2):
                number = number / 2
            else:
                number = number * 3 + 1
            #show the number and add it to the list
            print(round(number))
            numList.append(number)
        #add the 4-2-1 to avoid having a negative amount of terms printed later
        numList.append(4)
        numList.appaend(2)
        numList.append(1)
        #sort the list so the largest num is at the end
        numList.sort()
        #show stats to the user
        print('reached loop')
        print(f'''
terms until 4-2-1 loop: {len(numList) - 3}
largest number: {round(numList[len(numList)-1])}
''')

#get the mode (random or user choice)
asking = True
while asking:
    mode = input('input or random? ')
    if mode.lower() == 'random':
        asking = False
        start('random')
    elif mode.lower() == 'input':
        asking = False
        start('input')
    else:
        print('invalid input ')
