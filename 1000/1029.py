call = [1, 1]
f = [0, 1]

for i in range(2, 42):
    call.append(call[i-1] + call[i-2] + 1)
    f.append(f[i-1] + f[i-2])


t = int(input())
for i in range(t):
    n = int(input())
    print("fib(%d) = %d calls = %d" %(n, call[n]-1, f[n]))