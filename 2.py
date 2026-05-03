import random

secret_number = random.randint(1, 10)
attempts = 3

print("Гра «Вгадай число». У вас є 3 спроби, щоб вгадати число від 1 до 10.")

for _ in range(attempts):
    guess = int(input("Ваш варіант: "))

    if guess == secret_number:
        print("Ви вгадали!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Спроби закінчились. Загадане число було: {secret_number}")