#By Khanh Nguyen
#Farenheit
ctnue = True
while(ctnue == True):
    try:
        celsius = int(input('C:'))
    except:
        print('This is not a number')
    else:
        farenheit = celsius * ( 9 / 5 ) + 32
        print('F:',farenheit)
        checkCtnue = input('Continue? y/n')
        if checkCtnue == 'y':
            ctnue = True
        else:
            break
