i = 2
for n in range(7):
    if n == 3 or n == 4 or n == 5:
        print(" " * (6 - n), " *", " " * (n - i), "*")
        i -= 1
    else:
        print(" " * (6 - n), " *" * n)




