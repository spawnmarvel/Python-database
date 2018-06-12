import sqlite3
from datetime import date, datetime

conn = None
datebase = "database.db"
# statment create
sql_create = "create table if not exists holder(id INTEGER PRIMARY KEY AUTOINCREMENT, note TEXT NOT NULL, published NUMERIC NOT NULL)"
# statement prepared
sql_insert = "insert into holder (note, published) values (?, ?)"
# statment select
sql_select_all = "select * from holder"
sql_select_max_id = "select max(id) from holder"

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
        print("tab created if not existed")
    except sqlite3.OperationalError as e:
        msg = e
    return msg

def insert():
    msg = ""
    try:
        conn = get_conn()
        conn = sqlite3.connect(get_db())
        with conn:
            cur = conn.cursor()
            timeNow = datetime.now()
            global sql_insert
            cur.execute(sql_insert, ("Note test", timeNow))
            conn.commit()
            msg = "added row"
    except sqlite3.OperationalError as e:
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
            print(row)
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
            print(row)
    except sqlite3.OperationalError as e:
        msg = e
    return msg






print(init())
print(insert())
print(select_all())
print(select_id())
