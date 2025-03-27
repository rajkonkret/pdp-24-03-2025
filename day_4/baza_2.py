# baza sql w pythonie
import sqlite3

try:
    sql_connection = sqlite3.connect("sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    query = """
    CREATE TABLE IF NOT EXISTS sqliteDB (
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    """

    # cursor.execute(query)
    # sql_connection.commit()

    with open('table.sql', "r") as file:
        sql_script = file.read()

    # wykonanie skryptu n abazie danych
    cursor.executescript(sql_script)


except sqlite3.Error as e:
    print("Bład otwierania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")

# Baza danych została podłączona
# Baza zostałą zamknięta
