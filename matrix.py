rows = int(input("input rows: "))
cols = int(input("input columns: "))

matrix = []

for row in range(rows):
    for col in range(cols):
        if col == 0:    
            matrix.append([])

        value = int(input(f"enter value for element [{row}][{col}]:"))
        matrix[row].append(value)


print(matrix)