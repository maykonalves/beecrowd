x = input().split()
a, b, c = x

a = float(a)
b = float(b)
c = float(c)

delta = b ** 2 - 4 * a * c

if a == 0:
    print("Impossivel calcular")
elif delta < 0:
    x = -b / (2*a)
    print("Impossivel calcular")
else:
    r1 = (-b + (delta ** 0.5)) / (2 * a)
    r2 = (-b - (delta ** 0.5)) / (2 * a)
    print("R1 = {}\nR2 = {}".format(round(r1, 5), round(r2, 5)))
