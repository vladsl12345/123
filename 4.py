n = int(input("Введіть число для обчислення факторіалу: "))
factorial = 1

if n < 0:
    print("Факторіал від'ємного числа не існує.")
elif n == 0:
    print("Факторіал числа 0 дорівнює 1.")
else:
    for i in range(1, n + 1):
        factorial = i
    print(f"Факторіал числа {n} дорівнює {factorial}")