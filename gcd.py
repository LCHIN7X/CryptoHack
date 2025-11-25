def gcd(a,b):
    while b != 0:
        a,b = b,a %b
    return a

a = 66528
b = 52920

print (gcd(a,b))

#66528 % 52920 = 13608
#52920 % 13608 = 12096
#13608 % 12096 = 1512
#12096 % 1512 = 0

#simple example:
#12 % 8 = 4
#8 % 4  = 0, gcd = 4