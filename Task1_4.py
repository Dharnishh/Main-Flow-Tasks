def fibonacci(n):
    sequence=[]
    a,b=0,1
    for i in range(n):
        sequence.append(a)
        a,b=b,a+b
    return sequence
n=int(input("enter the fibonacci number to generate: "))
fib_sequence=fibonacci(n)
print("the first",n,"fibonacci sequence is:",fib_sequence)