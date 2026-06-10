import sqlite3

DB_NAME = 'MoviesInfo.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    conn.close()

init_db()

def create_table():
    query = '''CREATE TABLE IF NOT EXISTS Movies
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT,
    country TEXT,
    year INTEGER,
    imdb_rate REAL)
            '''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()

create_table()

def insert_record(movie_name, country, year, imdb_rate):
    query = '''INSERT INTO Movies(movie_name, country, year, imdb_rate)
    VALUES(?,?,?,?)'''
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(query, (movie_name, country, year, imdb_rate))
    conn.commit()
    conn.close()

def update_record(movie_name, country, year, imdb_rate):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = '''
        UPDATE Movies
        SET movie_name = ?,
            country = ?,
            year = ?,
            imdb_rate = ?
        WHERE movie_name = ?
    '''
    cursor.execute(query,
    (movie_name, country, year, imdb_rate, movie_name))

    conn.commit()
    conn.close()

def select_all_records():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = '''SELECT * FROM Movies'''
    cursor.execute(query)
    records = cursor.fetchall()
    conn.close()
    return records

def delete_record(movie_name):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    query = '''DELETE FROM Movies WHERE movie_name = ?'''
    cursor.execute(query, (movie_name,))
    conn.commit()
    conn.close()

if __name__ == '__main__':
    app_db.py()