from homeworks.distance import Distance

if __name__ == "__main__":
    d1 = Distance(10, "m")
    d2 = Distance(200, "km")
    d3 = Distance(50, "cm")

    print("Инициализация:")
    print(d1)
    print(d2)
    print(d3)

    print("\nСложение:")
    print(d1 + d2)
    print(d2 + d3)
    print(d1 + d3)

    print("\nВычитание:")
    print(d2 - d1)
    print(d1 - d3)