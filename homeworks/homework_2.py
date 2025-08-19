class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, работаю {self.occupation}.")


class Friend(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я знаком Егором, я родился {self.birth_date}, работаю {self.occupation}.")


class Classmate(Person):
    def introduce(self):
        print(f"Привет, меня зовут {self.name}, я одногруппник Даши, я родился {self.birth_date}, работаю {self.occupation}.")

friend1 = Friend(name="Саша", birth_date="05.04.2001", occupation="Консультантом", higher_education=True)
friend2 = Friend(name="Жанна", birth_date="23.07.1999", occupation="Тестировщиком", higher_education=True)

classmate1 = Classmate(name="Миша", birth_date="09.11.2006", occupation="Официантом", higher_education=True)
classmate2 = Classmate(name="Максат", birth_date="15.07.2001", occupation="Аналитик", higher_education=True)

friend1.introduce()
friend2.introduce()
classmate1.introduce()
classmate2.introduce()