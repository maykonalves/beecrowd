A, B, C = [int(x) for x in input().split()]

maior = (A+B+abs(A-B))/2

maior = (maior+C+abs(maior-C))/2

print("{:.0f} eh o maior".format(maior))