# 打印一个由星号组成的三角形
# 打印一个由星号组成的三角形bbbzzz---joehe
def print_triangle(rows):
    for i in range(1, rows + 1):
        print('*' * i)

# 输入三角形的行数
num_rows = 5
print_triangle(num_rows)
