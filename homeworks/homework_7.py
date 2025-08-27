import sqlite3

def create_tables():
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

def insert_books():
    books = [
        ("1984", "Джордж Оруэлл", 1949, "Антиутопия", 328, 4),
        ("Унесённые ветром", "Маргарет Митчелл", 1936, "Исторический роман", 1037, 2),
        ("Три товарища", "Эрих Мария Ремарк", 1936, "Драма", 496, 3),
        ("Цветы для Элджернона", "Дэниел Киз", 1966, "Научная фантастика", 311, 5),
        ("451 градус по Фаренгейту", "Рэй Брэдбери", 1953, "Фантастика", 256, 4),
        ("Маленький принц", "Антуан де Сент-Экзюпери", 1943, "Сказка", 96, 6),
        ("Автостопом по галактике", "Дуглас Адамс", 1979, "Научная фантастика", 224, 3),
        ("Гарри Поттер и философский камень", "Джоан Роулинг", 1997, "Фэнтези", 352, 8),
        ("Молчание ягнят", "Томас Харрис", 1988, "Триллер", 367, 2),
        ("Шантарам", "Грегори Дэвид Робертс", 2003, "Приключения", 936, 1)
    ]

    conn.executemany("""
        INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
        VALUES (?, ?, ?, ?, ?, ?
    """, books)

def delete_book(book_name):
    conn.execute("DELETE FROM books WHERE name = ?", (book_name,))

if __name__ == '__main__':
    conn = sqlite3.connect('hw7.db')

    create_tables()
    insert_books()
    delete_book("Молчание ягнят")
    delete_book("Шантарам")

    conn.commit()
    conn.close()