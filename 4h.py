class Тварина:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def make_sound(self):
        return "Якийсь незрозумілий звук"

    def __str__(self):
        return f"Тварина: {self.name}, Вік: {self.age} років"


class Собака(Тварина):
    def __init__(self, name: str, age: int, breed: str):
        self.name = name
        self.age = age
        self.breed = breed

    def make_sound(self):
        return "Гав-гав!"

    def __str__(self):
        return f"Собака {self.name} (Порода: {self.breed}, Вік: {self.age} років)"


class Кіт(Тварина):
    def __init__(self, name: str, age: int, color: str):
        self.name = name
        self.age = age
        self.color = color

    def make_sound(self):
        return "Мяу-мяу!"

    def __str__(self):
        return f"Кіт {self.name} (Колір: {self.color}, Вік: {self.age} років)"

if __name__ == "__main__":
    some_animal = Тварина("Хтось", 5)
    print(some_animal)
    print("Звук:", some_animal.make_sound())
    print("-" * 30)

    my_dog = Собака("Рекс", 3, "Вівчарка")
    print(my_dog)
    print("Звук:", my_dog.make_sound())
    print("-" * 30)

    my_cat = Кіт("Барсік", 2, "Рудий")
    print(my_cat)
    print("Звук:", my_cat.make_sound())