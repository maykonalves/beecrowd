value = float(input())
value = value + 0.001

Notas = [100,50,20,10,5,2]
Moedas = [1.00,0.5,0.25,0.10,0.05,0.01]

print("NOTAS:")
for i in Notas:
    Notas = int(value//i)
    print("{} nota(s) de R$ {:.2f}".format(int(Notas),i))
    value %= i

print("MOEDAS:")
for i in Moedas:
    Moedas = int(value//i)
    print("{} moeda(s) de R$ {:.2f}".format(int(Moedas),i))
    value %= i