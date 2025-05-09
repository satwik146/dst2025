num = int(input("Enter a number of lines: "))
for row in range(1, num + 1):
    for col in range(1, num + 1):
        if row == col or row + col == num + 1:         
            print("*", end="")
        else:
            print(" ", end="")
    print() 