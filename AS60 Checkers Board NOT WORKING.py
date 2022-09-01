#AS60 CHECKERS BOARD	Given two numbers nn and mm.
#Create a two-dimensional array of size (n×m)(n×m) and populate it with the characters "." and "*" in a checkerboard pattern.
#The top left corner should have the character "." .

nn = int(input("Enter the number of rows: "))
mm = int(input("Enter the number of columns: "))
board = []
a = []
b = []
dot = "."
ast = "*"

for i in range(nn):
    if i % 2 == 0:
        a.append(dot)
        for i in range(mm-1):
            if a[i] == ".":
                a.append(ast)
            else:
                a.append(dot)
        board.append(a)
    else:
        b.append(ast)
        for j in range(mm-1):
            if b[j] == "*":
                a.append(dot)
            else:
                a.append(ast)
        board.append(b)


for row in board:
    for elem in row:
        print(elem, end=' ')
    print()

print(board)