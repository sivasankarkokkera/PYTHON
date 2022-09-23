a = input('Enter your name here: ')
b = int(input('your salary here: '))
c = input('your gender here (M/F) : ')
if b < 10000 and c == 'M':
    print(str(a) + ' your salary with bonus is ' + str(b * 1.07))
elif b < 10000 and c == 'F':
    print(str(a) + ' your salary with bonus is ' + str(b * 1.12))

if b >= 10000 and c == 'M':
    print(str(a) + ' your salary with  bonus is '+ str(b * 1.05))

elif b >= 10000 and c=='F':
        print(str(a) + ' your salary with  bonus is '+ str(b * 1.1))
