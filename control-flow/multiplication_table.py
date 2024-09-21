number = int(input("Enter a number to see its multiplication table:"))

n = 0
for n in range(1,11):
    product = number * n
    print(f"{number} * {n} = {product}")
    