import sqlite3

conn = sqlite3.connect("coffee.sqlite")
cur = conn.cursor()

cur.executescript("""
CREATE TABLE coffee (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sort TEXT NOT NULL,
    roast TEXT NOT NULL,
    grind_or_beans TEXT NOT NULL,
    taste TEXT,
    price REAL,
    volume REAL
);

INSERT INTO coffee (sort, roast, grind_or_beans, taste, price, volume)
VALUES 
('Арабика', 'Средняя', 'В зернах', 'Насыщенный вкус с фруктовыми нотками', 10.5, 250),
('Робуста', 'Темная', 'Молотый', 'Сильный, горьковатый вкус', 8.0, 500);
""")

conn.commit()
conn.close()