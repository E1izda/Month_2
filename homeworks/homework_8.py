import sqlite3

def create_tables():
    conn.execute("DROP TABLE IF EXISTS books")
    conn.execute("DROP TABLE IF EXISTS genres")

    conn.execute("""
        CREATE TABLE genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT,
            publication_year INTEGER,
            pages INTEGER,
            copies INTEGER,
            genre_id INTEGER,
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
    """)

def add_genre(name: str):
    conn.execute("INSERT INTO genres (name) VALUES (?)", (name,))
    conn.commit()

def add_book(title: str, author: str, year: int, pages: int, copies: int, genre_id: int):
    conn.execute(
        "INSERT INTO books (title, author, publication_year, pages, copies, genre_id) VALUES (?, ?, ?, ?, ?, ?)",
        (title, author, year, pages, copies, genre_id)
    )
    conn.commit()

def get_books_with_genre():
    result = conn.execute("""
        SELECT books.title, books.author, books.publication_year, genres.name
        FROM books
        LEFT JOIN genres ON genres.id = books.genre_id
    """)
    return result

if __name__ == '__main__':
    conn = sqlite3.connect('hw7.db')

    create_tables()

    add_genre('Антиутопия')
    add_genre('Исторический роман')
    add_genre('Фантастика')
    add_genre('Фэнтези')
    add_genre('Триллер')

    add_book('1984', 'Джордж Оруэлл', 1949, 328, 4, 1)
    add_book('Унесённые ветром', 'Маргарет Митчелл', 1936, 1037, 2, 2)
    add_book('451 градус по Фаренгейту', 'Рэй Брэдбери', 1953, 256, 4, 3)
    add_book('Гарри Поттер и философский камень', 'Джоан Роулинг', 1997, 352, 8, 4)
    add_book('Молчание ягнят', 'Томас Харрис', 1988, 367, 2, 5)
    add_book('Песнь отраленной любви', 'Неизвестный автор', 2025, 123, 1, None)

    for row in get_books_with_genre():
        print(row)

    conn.close()
