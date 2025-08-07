n = int(input())
def cal_sum(n):
    total = 0
    for i in range(1, n):
        if i%3==0 or i%5==0:
            total = total + i
    return total
result=cal_sum(n)
print(result)

