import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/globomantics.db'
conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS items")
c.execute("DROP TABLE IF EXISTS categories")
c.execute("DROP TABLE IF EXISTS subcategories")
c.execute("DROP TABLE IF EXISTS comments")

c.execute("""CREATE TABLE categories(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    name            TEXT
)""")

c.execute("""CREATE TABLE subcategories(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    name            TEXT,
                    category_id     INTEGER,
                    FOREIGN KEY(category_id) REFERENCES categories(id)
)""")

c.execute("""CREATE TABLE items(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    title           TEXT,
                    description     TEXT,
                    price           REAL,
                    image           TEXT,
                    category_id     INTEGER,
                    subcategory_id  INTEGER,
                    FOREIGN KEY(category_id) REFERENCES categories(id),
                    FOREIGN KEY(subcategory_id) REFERENCES subcategories(id)
)""")

c.execute("""CREATE TABLE comments(
                    id              INTEGER PRIMARY KEY AUTOINCREMENT,
                    content         TEXT,
                    item_id         INTEGER,
                    FOREIGN KEY(item_id) REFERENCES items(id)
)""")

categories = [
    ("Food",),
    ("Technology",),
    ("Books",)
]
c.executemany("INSERT INTO categories (name) VALUES (?)", categories)

subcategories = [
    ("Fruit", 1),
    ("Dairy product", 1),
    ("Cassette", 2),
    ("Phone", 2),
    ("TV", 2),
    ("Historical fiction", 3),
    ("Science fiction", 3)
]
c.executemany("INSERT INTO subcategories (name, category_id) VALUES (?,?)", subcategories)

items = [
    ("Old Tape", "You can record anything.", 2.0, "", 2, 3),
    ("Bananas", "1kg of fresh bananas.", 1.0, "", 1, 1),
    ("Vintage TV", "In color!", 150.0, "", 2, 5),
    ("Cow Milk", "From the best farms.", 5.0, "", 1, 2)
]
c.executemany("INSERT INTO items (title, description, price, image, category_id, subcategory_id) VALUES (?,?,?,?,?,?)", items)

comments = [
    ("This item is great!", 1),
    ("Whats up?", 2),
    ("Spam spam", 3)
]
c.executemany("INSERT INTO comments (content, item_id) VALUES (?,?)", comments)

conn.commit()
conn.close()

print("Database is created and initialized.")
print("You can see the tables with the show_tables.py script.")
