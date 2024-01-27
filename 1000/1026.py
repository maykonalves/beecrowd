while True:

    try:
        n = input().split()
        a, b = n
        print(int(a) ^int(b))
    except:
        break