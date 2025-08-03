n=int(input())
def calculate_fact(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        i=i+1
    return fact
result=calculate_fact(n)
print(result)
