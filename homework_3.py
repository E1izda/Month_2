class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.__occupation = occupation
        self.__higher_education = higher_education

    @property
    def occupation(self):
        return self.__occupation

    @property
    def higher_education(self):
        return self.__higher_education

    def introduce(self):
        edu = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}, я родился {self.birth_date}, моя профессия {self.occupation}. {edu}")


class Friend(Person):
    def introduce(self):
        edu = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}, я знаком с Егором,"
              f" я родился {self.birth_date}, моя профессия {self.occupation}. {edu}")


class Classmate(Person):
    def introduce(self):
        edu = "У меня есть высшее образование." if self.higher_education else "У меня нет высшего образования."
        print(f"Привет, меня зовут {self.name}, я одногруппник Даши,"
              f" я родился {self.birth_date}, моя профессия {self.occupation}. {edu}")


friend1 = Friend(name="Саша", birth_date="05.04.2001", occupation="Консультант", higher_education=True)
friend2 = Friend(name="Жанна", birth_date="23.07.1999", occupation="Тестировщик", higher_education=True)

classmate1 = Classmate(name="Миша", birth_date="09.11.2006", occupation="Официант", higher_education=False)
classmate2 = Classmate(name="Максат", birth_date="15.07.2001", occupation="Аналитик", higher_education=True)

friend1.introduce()
friend2.introduce()
classmate1.introduce()
classmate2.introduce()
