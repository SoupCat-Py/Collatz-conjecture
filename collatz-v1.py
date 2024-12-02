import random
print('''Soup\'s Collatz Conjecture - \"3x+1\" simulator

''')

#actual math function
def run(number):
    amount = 0
    while number != 1:
        #check if odd or even
        if '.5' in str(number/2):
            number = (number * 3) +1
        else:
            number = (number / 2)
        #print number and add to the list
        print(round(number))
        amount += 1
    #show stats to user
    print('reached loop')
    if amount >= 0:
        print(f'terms until loop: {amount-3}')
    else:
        print(f'terms until loop: 0')
    print('')

#get number and set random range
def runRandom():
    while True:
        rangeRunning = True
        #get user input
        while rangeRunning:
            rangeVar = input ('Enter maximum value: ')
            #check for infinity or integer
            if numVar.lower() == 'infinity' or numVar.lower() == 'inf':
                print('nuh uh >:P')
            try:
                rangeVar = int(rangeVar)
                number = random.randint(1,rangeVar)
                rangeRunning = False
            except ValueError:
                print ('Invalid response' )
        print(f'number selected: {number}')
        #call main function with random number
        run(number)

#get number set by user
def runInput():
    while True:
        inputRunning = True
        while inputRunning:
            #get user input
            numVar = input ('Enter a number: ')
            #check for infinity or integer
            if numVar.lower() == 'infinity' or numVar.lower() == 'inf':
                print('nuh uh >:P')
            try:
                number = int(numVar)
                inputRunning = False
            except ValueError:
                print ('Invalid response ')
        #call main function with user input
        run(number)

#get mode - random or user input
asking = True
while asking:
    mode = input ('Input or Random? ')
    if mode.lower() == 'random':
        asking = False
        runRandom()
    elif mode.lower() == 'input':
        asking = False
        runInput()
    else:
        asking = True
