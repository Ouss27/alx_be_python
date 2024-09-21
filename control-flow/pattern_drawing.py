size = int(input("Enter the size of the pattern:"))

i = 0
while i < size:
    i += 1
    j = 0
    for j in range(1,size+1):
        print("*", end="")
        j += 1
    print("\n")