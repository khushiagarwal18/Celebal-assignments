# UPPER TRIANGLE
def upper_triangle(n):
    for i in range(n):
        print("  " * i + "* " * (n - i))

upper_triangle(5)