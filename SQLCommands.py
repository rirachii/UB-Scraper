import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


def create_table(conn, template):
    try:
        c = conn.cursor()
        c.execute(template)
    except Error as e:
        print(e)


def create_project(conn, project):
    sql = ''' INSERT INTO cse(course,professor,rating, difficulty, num_of_rating, spring21, summer21, fall21)
              VALUES(?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, project)
    conn.commit()
    return cur.lastrowid


def dbappend(course, prof):
    database = "pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        project = (course, prof, 0, 0, 0, "", "✔", "")
        create_project(conn, project)


def courseindb(coursename):
    c = create_connection(db_file="pythonsqlite.db").cursor()
    c.execute("SELECT id FROM cse WHERE course = ?", (coursename,))
    data = c.fetchall()
    if len(data) == 0:
        return False
    else:
        # print(map(str, next(zip(*data))))
        return True


def profNOTindb(prof):
    c = create_connection(db_file="pythonsqlite.db").cursor()
    c.execute("SELECT id FROM cse WHERE professor = ?", (prof,))
    data = c.fetchall()
    if len(data) == 0:
        return True
    else:
        return False


def profandcourse(prof, course):
    c = create_connection(db_file="pythonsqlite.db").cursor()
    c.execute("SELECT id FROM cse WHERE professor = ? AND course = ?", (prof, course))
    data = c.fetchall()
    if len(data) == 0:
        return True
    else:
        return False


def update_rating(update):
    c = create_connection(db_file="pythonsqlite.db")
    cur = c.cursor()
    sql = ''' UPDATE cse
              SET rating = ? ,
                  difficulty = ? ,
                  num_of_rating = ?
              WHERE professor = ?'''
    cur.execute(sql, update)
    c.commit()


def get_all_prof():
    c = create_connection(db_file="pythonsqlite.db")
    c.row_factory = lambda cursor, row: row[0]
    cur = c.cursor()
    cur.execute("SELECT professor FROM cse")
    rows = cur.fetchall()
    c.close()
    return rows

def update_semester(update):
    c = create_connection(db_file="pythonsqlite.db")
    cur = c.cursor()
    sql = ''' UPDATE cse
              SET summer21 = ?
              WHERE professor = ? AND course = ?
              '''
    cur.execute(sql, update)
    c.commit()


def main():
    database = "pythonsqlite.db"
    conn = create_connection(database)
    with conn:
        tabletemplate = """ CREATE TABLE IF NOT EXISTS cse (
                                                    id integer PRIMARY KEY,
                                                    course text NOT NULL,
                                                    professor text NOT NULL,
                                                    rating integer,
                                                    difficulty integer,
                                                    num_of_rating integer,
                                                    spring21 text,
                                                    summer21 text,
                                                    fall21 text
                                            ); """
    create_table(conn, tabletemplate)
    conn.close()


if __name__ == '__main__':
    main()
