def print_operation_table(operation, num_rows=6, num_columns=6):
    table = [[operation(row, col) for col in range(1, num_columns+1)] for row in range(1, num_rows+1)]
    print('{:^10}'.format(''), end='')
    for col in range(1, num_columns+1):
        print('{:^10}'.format(col), end='')
    print()
    for row in range(num_rows):
        print('{:^10}'.format(row+1), end='')
        for col in range(num_columns):
            print('{:^10}'.format(table[row][col]), end='')
        print()

def multiply(x, y):
    return x * y
print("\nТаблица умножения:")
print_operation_table(multiply, 6, 6)