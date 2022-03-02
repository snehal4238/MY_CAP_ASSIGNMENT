def fibo(x):
    a= 0
    b= 1
    print(a)
    print(b)

    for i in range(2,x):
        c= a+b
        a=b
        b=c
        print(a+b)
fibo(8)
