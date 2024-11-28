import random
print('''Soup\'s \"3x+1\" simulator

''')

def run(number):

    amount = 0
    while number != 1:
        if '.5' in str(number/2):
            number = (number * 3) +1
        else:
            number = (number / 2)
        print(round(number))
        amount += 1
    print('reached loop')
    if amount >= 0:
        print(f'terms until loop: {amount-3}')
    else:
        print(f'terms until loop: 0')
    print('')
    
def runRandom():

    while True:
        rangeRunning = True
        while rangeRunning:
            rangeVar = input ('Enter maximum value: ')
            try:
                rangeVar = int(rangeVar)
                number = random.randint(1,rangeVar)
                rangeRunning = False
            except ValueError:
                print ('Invalid response' )
        print(f'number selected: {number}')
        run(number)

def runInput():
    
    while True:
        inputRunning = True
        while inputRunning:
            numVar = input ('Enter a number: ')
            if numVar.lower() == 'infinity' or numVar.lower() == 'inf':
                print('nuh uh >:P')
            try:
                number = int(numVar)
                inputRunning = False
            except ValueError:
                print ('Invalid response ')
        run(number)


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
