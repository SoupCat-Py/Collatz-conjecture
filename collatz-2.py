import random
print('Soup\'s Collatz Conjecture Simulator version 2')
print('')
print('')

def start(style):
    while True:
        numList = []
        asking = True
        while asking:
            if style == 'input':
                number = input('enter any number ')
                asking = False
            elif style == 'random':
                number = input('enter maximum value ')
                asking = False
                
            try:
                number = int(number)
                asking = False
            except ValueError:
                if number.lower() == 'inf' or number.lower() == 'infinity':
                    print('nuh uh >:P')
                else:
                    print('invalid input ')
                asking = True

        if style == 'random':
            number = random.randint(1,number)
            print(f'''chosen number: {number}
            ''')
            
        while number != 1:
            if '.5' not in str(number / 2):
                number = number / 2
            else:
                number = number * 3 + 1
            print(round(number))
            numList.append(number)
        numList.sort()
        print(f'''reached loop
terms until 4-2-1 loop: {len(numList) - 3}
largest number: {round(numList[len(numList)-1])}
''')

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
