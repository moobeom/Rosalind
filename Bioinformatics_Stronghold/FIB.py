### Rabbits and recurrence relations ###

def Fibo(n,k):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return Fibo(n-1,k) + k * Fibo(n-2,k)

print(Fibo(30,3))