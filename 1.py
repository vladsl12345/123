name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))

print(f"Привіт {name}, тобі {age}!")

if age > 18:
    print("Вхід дозволено!")
else:
    print("Вхід заборонено!")