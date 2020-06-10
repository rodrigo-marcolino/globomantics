import sqlite3
import os

db_abs_path = os.path.dirname(os.path.realpath(__file__)) + '/globomantics.db'

print("Options: (items, comments, categories, subcategories, all)")
table = input("Show table: ")

conn = sqlite3.connect(db_abs_path)
c = conn.cursor()

def show_items():
    try:
        items = c.execute("""SELECT
                                i.id, i.title, i.description, i.price, i.image, c.name, c.id, s.name, s.id
                             FROM
                                items AS i
                             INNER JOIN categories     AS c ON i.category_id     = c.id
                             INNER JOIN subcategories  AS s ON i.subcategory_id  = s.id
        """)

        print("ITEMS")
        print("#############")
        for row in items:
            print("ID:             ", row[0]),
            print("Title:          ", row[1]),
            print("Description:    ", row[2]),
            print("Price:          ", row[3]),
            print("Image:          ", row[4]),
            print("Category:       ", row[5], "(", row[6], ")"),
            print("SubCategory:    ", row[7], "(", row[8], ")"),
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_comments():
    try:
        comments = c.execute("""SELECT
                                    c.id, c.content, i.title, i.id
                                 FROM
                                    comments AS c
                                 INNER JOIN items AS i ON c.item_id = i.id
        """)

        print("COMMENTS")
        print("#############")
        for row in comments:
            print("ID:             ", row[0]),
            print("Content:        ", row[1]),
            print("Item:           ", row[2], "(", row[3], ")")
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_categories():
    try:
        categories = c.execute("SELECT * FROM categories")

        print("CATEGORIES")
        print("#############")
        for row in categories:
            print("ID:             ", row[0]),
            print("Name:           ", row[1])
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()

def show_subcategories():
    try:
        subcategories = c.execute("SELECT s.id, s.name, c.name, c.id FROM subcategories AS s INNER JOIN categories AS c ON s.category_id = c.id")
        print("SUBCATEGORIES")
        print("#############")
        for row in subcategories:
            print("ID:             ", row[0]),
            print("Name:           ", row[1]),
            print("Category:       ", row[2], "(", row[3], ")")
            print("\n")
    except:
        print("Something went wrong, please run db_init.py to initialize the database.")
        conn.close()


if table == "items":
    show_items()
elif table == "comments":
    show_comments()
elif table == "categories":
    show_categories()
elif table == "subcategories":
    show_subcategories()
elif table == "all":
    show_items()
    show_comments()
    show_categories()
    show_subcategories()
else:
    print("This option does not exist.")

conn.close()
