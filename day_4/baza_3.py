# baza sql w pythonie
import sqlite3

data = [
    (11, 'Python', 2000.0),
    (12, 'Spark', 3456.0),
    (13, 'PHP', 5000.0),
]

try:
    sql_connection = sqlite3.connect("sqlite_python.db")
    cursor = sql_connection.cursor()
    print("Baza danych została podłączona")

    insert = """
    INSERT INTO software (id,name,price) VALUES (1,'Python', 200);
    """

    # cursor.execute(insert)
    # sql_connection.commit()

    select_all = """
    SELECT * FROM software;
    """

    for row in cursor.execute(select_all):
        print(row)  # (1, 'Python', 200.0)

    select = """
    SELECT * FROM software WHERE id=1;
    """
    for row in cursor.execute(select_all):
        print(row)  # (1, 'Python', 200.0)

    update = """
    UPDATE software SET price=2000 WHERE id=1;
    """

    # cursor.execute(update)
    # sql_connection.commit()

    insert2 = """
    INSERT INTO software (id,name,price) VALUES (?,?,?);
    """

    # cursor.execute(insert2, ("2", "Tomek", 3500))
    # sql_connection.commit()

    insert_many = """
    INSERT INTO software (id,name,price) VALUES (?,?,?);
    """

    # cursor.executemany(insert_many, data)
    # sql_connection.commit()

    delete = """
    DELETE FROM software WHERE id=1;
    """

    cursor.execute(delete)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Bład otwierania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza zostałą zamknięta")

# Baza danych została podłączona
# Baza zostałą zamknięta
