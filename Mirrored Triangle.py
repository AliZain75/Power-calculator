rows = int(input("Enter the number of rows: "))

print("\nRight-Angled Triangle and Mirrored Triangle:\n")
for i in range(1, rows + 1):
    left_triangle = '*' * i
    right_triangle = ' ' * (rows - i) + '*' * i
    print(left_triangle + '   ' + right_triangle)
