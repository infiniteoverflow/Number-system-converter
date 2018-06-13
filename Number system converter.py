import os

print('\n\t\tWhich type of number do you want to convert??')
print('\n\t1.. Binary')
print('\n\t2.. Decimal')
print('\n\t3.. Octal')
print('\n\t4.. Hexadecimal')

ch=input('\n\tEnter your choice:')
ch = int(ch)

if ch == 1:
    os.system('cls')
    binary=input('\n\t\tEnter your binary number:')
    d = int(binary,2)
    o = oct(d)
    h = hex(d)
    print('\n\n\tDecimal : {} \n\n\tOctal : {} \n\n\tHexadecimal : {}'.format(d,o,h))

elif ch == 2:
    os.system('cls')
    decimal=int(input('\n\t\tEnter your Decimal number:'))
    b = bin(decimal)
    o = oct(decimal)
    h = hex(decimal)
    print('\n\n\tBinary : {} \n\n\tOctal : {} \n\n\tHexadecimal : {}'.format(b,o,h))

elif ch == 3:
    os.system('cls')
    octal=input('\n\t\tEnter your Octal number:')
    d = int(octal)
    b = bin(d)
    h = hex(d)
    print('\n\n\tBinary : {} \n\n\tDecimal : {} \n\n\tHexadecimal : {}'.format(b,d,h))

elif ch == 4:
    os.system('cls')
    hexa=input('\n\tEnter your Hexadecimal number:')
    d = int(hexa,16)
    b = bin(d)
    o = oct(d)
    print('\n\n\tBinary : {} \n\n\tDecimal : {} \n\n\tOctal : {}'.format(b,d,o))

else:
    print('\nEnter a valid choice')

a = input()

          
