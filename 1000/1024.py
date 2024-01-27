N = int(input())

for i in range(N):
    msg = input()
    newmsg = ''

    for i in msg:
        if ord(i) >= 65 and ord(i) <= 90:
            newmsg += chr(ord(i)+3)
        elif ord(i) >= 97 and ord(i) <= 122:
            newmsg += chr(ord(i)+3)
        else:
            newmsg += i

    newmsg = newmsg[::-1]
    meio = int((len(newmsg)/2))
    metade1 = newmsg[0:meio]
    metade2 = newmsg[meio:]
    metade_new = ''

    for i in metade2:
        metade_new += chr(ord(i)-1)

    texto_final = metade1+metade_new

    print(texto_final)