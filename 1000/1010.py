item1 = input().split(" ")
item2 = input().split(" ")

cod1, qtd1, value1 = item1
cod2, qtd2, value2 = item2

total = (int(qtd1)*float(value1))+(int(qtd2)*float(value2))

print("VALOR A PAGAR: R$ %.2f" %total)