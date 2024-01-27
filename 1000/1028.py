def mdc(a,b):
    resto = ''
    while resto != 0:
        resto = a % b
        a = b
        b = resto
    return a

trocas = int(input())

for i in range(trocas):
    n = [int(i) for i in input().split()]
    print(mdc(n[0], n[1]))