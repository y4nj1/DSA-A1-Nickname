# Assignment 1:
# Create a program that will print your nickname using only asterisk character (*)

name = "YANJI"
print_Y = [[" " for i in range(5)] for j in range(5)]
print_A = [[" " for i in range(5)] for j in range(5)]
print_N = [[" " for i in range(5)] for j in range(5)]
print_J = [[" " for i in range(5)] for j in range(5)]
print_I = [[" " for i in range(5)] for j in range(5)]

# code for Y
for row in range(5):
    for col in range(5):
        if ((col==2 and row>1) or row==col and col<2) or (row==0 and col==4) or (row==1 and col==3):
            print_Y[row][col]= "*"

# code for A
for row in range(5):
    for col in range(5):
        if ((col==0 or col==4) and row!=0 or row==2 or (row==0 and (col!=0 and col!=4))):
            print_A[row][col]= "*"

# code for N
for row in range(5):
    for col in range(5):
        if ((col==0 or col==4) or row==col):
            print_N[row][col]= "*"

# code for J
for row in range(5):
    for col in range(5):
        if (row==4 and (col!=0 and col!=4)) or (col==4 and row!=4) or (col==0 and (row!=0 and row!=1 and row!=4)):
            print_J[row][col]= "*"

# code for I
for row in range(5):
    for col in range(5):
        if row==0 or col==2 or row==4:
            print_I[row][col]= "*"

for i in range(5):
    for j in range(5):
        print(print_Y[i][j], end=" ")
    print(end="  ")
    for j in range(5):
        print(print_A[i][j], end=" ")
    print(end="  ")
    for j in range(5):
        print(print_N[i][j], end=" ")
    print(end="  ")
    for j in range(5):
        print(print_J[i][j], end=" ")
    print(end="  ")
    for j in range(5):
        print(print_I[i][j], end=" ")
    print(end="  ")
    print()