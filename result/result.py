# Result

import sqlite3


def connect():
    conn = sqlite3.connect('results.db')
    cursor = conn.cursor()
    return conn, cursor


def disconnect(conn):
    conn.commit()
    conn.close()


def create_saved_table():
    conn, cursor = connect()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Saved (
            Saved REAL
        )
    ''')
    disconnect(conn)


def write_saved(saved):
    conn, cursor = connect()
    cursor.execute('INSERT INTO Saved (Saved) VALUES (?)', (saved,))
    disconnect(conn)


def read_saved():
    conn, cursor = connect()
    val = cursor.execute("SELECT * FROM Saved").fetchall()
    disconnect(conn)
    return [row[0] for row in val]


def calc_saved_avg():
    conn, cursor = connect()
    val = cursor.execute("SELECT AVG(Saved) FROM Saved").fetchone()[0]
    disconnect(conn)
    return val


def create_saved_avg_table():
    conn, cursor = connect()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS SavedAVG (
            SavedAVG REAL,
            NBpeople INTEGER
        )
    ''')
    disconnect(conn)


def write_saved_avg(savedavg, nbpeople):
    conn, cursor = connect()
    cursor.execute('INSERT INTO SavedAVG (SavedAVG, NBpeople) VALUES (?,?)', (savedavg, nbpeople))
    disconnect(conn)


def read_all_saved_avg():
    conn, cursor = connect()
    val = cursor.execute("SELECT SavedAVG FROM SavedAVG").fetchall()
    disconnect(conn)
    return [row[0] for row in val]


def read_all_nbpeople():
    conn, cursor = connect()
    val = cursor.execute("SELECT NBpeople FROM SavedAVG").fetchall()
    disconnect(conn)
    return [row[0] for row in val]


def get_nb_saved_values():
    conn, cursor = connect()
    val = cursor.execute("SELECT COUNT(*) FROM Saved;").fetchall()
    disconnect(conn)
    return val[0][0]

def test():
    create_saved_table()
    create_saved_avg_table()

    for i in range(1,5):
        write_saved(i+5)

    val = calc_saved_avg()
    peop = get_nb_saved_values()
    write_saved_avg(val, peop)

    print(read_saved())
    print(read_all_saved_avg())
    print(read_all_nbpeople())