
import sqlite3
from datetime import date, datetime

conn = None
datebase = "database.db"
# statments create
sql_create = "create table if not exists holder(id INTEGER PRIMARY KEY AUTOINCREMENT, title text check(length(title) <= 15) NOT NULL,  note text NOT NULL, published DATETIME NOT NULL)"
# statement prepared
sql_insert = "insert into holder (title, note, published) values (?, ?, ?)"
# statment select
sql_select_all = "select * from holder"
sql_select_max_id = "select max(id) from holder"
# statment update
sql_update_note = "update holder set note = ? where id = ?"
# statment del
sql_delete_id = "delete from holder where id = ?"

print("\nSQLite3 project " + str(datetime.now()) + " data\n")

def get_conn():
    global conn
    return conn

def get_db():
    global datebase
    return datebase

def init():
    msg = ""
    try:
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        cur = conn.cursor()
        global sql_create
        cur.execute(sql_create)
        row = cur.fetchone()
        if row == None:
            msg =  "Table exists holder"
        else:
            msg = "Table created holder"
    except sqlite3.OperationalError as e:
        msg = e
    return msg

def insert(note_title, note):
    msg = ""
    try:
        n_title = str(note_title)
        n_note = str(note)
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        with conn:
            cur = conn.cursor()
            timeNow = datetime.now()
            global sql_insert
            cur.execute(sql_insert, (n_title, n_note, timeNow))
            conn.commit()
            row = cur.fetchone()
            msg = row
    except sqlite3.OperationalError as e:
        msg = e
    except sqlite3.IntegrityError as i:
        msg = i
    except Exception as e:
        msg = e
    return msg

def update(note, note_id):
    msg = ""
    try:
        n_id = int(note_id)
        n_note = str(note)
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        with conn:
            cur = conn.cursor()
            global sql_update_note
            cur.execute(sql_update_note,  (n_note, n_id))
            conn.commit()
            row = cur.fetchall()
            msg = row
    except sqlite3.OperationalError as e:
        msg = e
    except Exception as e:
        msg = e
    return msg

def delete(note_id):
    msg = ""
    try:
        n_id = int(note_id)
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        with conn:
            cur = conn.cursor()
            global sql_delete_id
            cur.execute(sql_delete_id, (n_id,))
            row = cur.fetchall()
            msg = row
    except sqlite3.OperationalError as e:
        msg = e
    except Exception as e:
        msg = e
    return msg

def select_all():
    msg = ""
    try:
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        with conn:
            cur = conn.cursor()
            global sql_select_all
            cur.execute(sql_select_all)
            row = cur.fetchall()
            msg = row       
    except sqlite3.OperationalError as e:
        msg = e
    return msg

def select_id():
    msg = ""
    try:
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        with conn:
            cur = conn.cursor()
            global sql_select_max_id
            cur.execute(sql_select_max_id)
            row = cur.fetchall()
            msg = row
    except sqlite3.OperationalError as e:
        msg = e
    return msg





# valid
print(init())
# valid
print(insert("Testnote", "Testing a note insert"))
# iter
rv = select_all()
for r in rv:
    print(r) 
# valid
print(select_id())
print(update("new note", 2))
# should cast exception
# print(delete("gfygyg"))
# valid
print(delete(2))
