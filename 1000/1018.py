value = int(input())

n100 = value//100
n50 = (value-(n100*100))//50
n20 = (value-(n100*100)-(n50*50))//20
n10 = (value-(n100*100)-(n50*50)-(n20*20))//10
n5 = (value-(n100*100)-(n50*50)-(n20*20)-(n10*10))//5
n2 = (value-(n100*100)-(n50*50)-(n20*20)-(n10*10)-(n5*5))//2
n1 = (value-(n100*100)-(n50*50)-(n20*20)-(n10*10)-(n5*5)-(n2*2))//1

print(value)
print("{} nota(s) de R$ 100,00".format(n100))
print("{} nota(s) de R$ 50,00".format(n50))
print("{} nota(s) de R$ 20,00".format(n20))
print("{} nota(s) de R$ 10,00".format(n10))
print("{} nota(s) de R$ 5,00".format(n5))
print("{} nota(s) de R$ 2,00".format(n2))
print("{} nota(s) de R$ 1,00".format(n1))
