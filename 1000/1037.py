x = float(input())

range = [(0, 25), (25, 50), (50, 75), (75, 100)]

result = "Fora de intervalo"

for i in range:
    if i[0] <= x <= i[1]:
        if 0 == i[0]:
            result = f"Intervalo [{i[0]},{i[1]}]"
        else:
            result = f"Intervalo ({i[0]},{i[1]}]"
        break

print(result)