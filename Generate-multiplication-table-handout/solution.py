n, m = map(int, input().split())
def generate_multiplication_table(n,m):
    for i in range(1, m + 1):
        print(f"{n} * {i} = {n * i}")
generate_multiplication_table(n,m)
