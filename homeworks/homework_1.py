class Person:
    def __init__(self, name, birth_date, occupation, higher_education):
        self.name = name
        self.birth_date = birth_date
        self.occupation = occupation
        self.higher_education = higher_education

person1 = Person("Donald Trump", "14-06-1946", "President", True)
person2 = Person("Fuodor Dostoevsky", "11-11-1821", "Writer", True)
person3 = Person("Ozzy Osbourne", "03-12-1048", "Rock-singer", False)

for person in (person1, person2, person3):
    print(f"Name: {person.name}")
    print(f"Dirth Date: {person.birth_date}")
    print(f"Occupation: {person.occupation}")
    print(f"Higher education: {person.higher_education}")
    print("-" * 25)