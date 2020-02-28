import sqlite3
import datetime as datetime
from app_logger import Logger

logger = Logger().get()
logger.info("sqlite")
class SqlLiteAdapter():

    # statments create
    SQL_CREATE_TABLE = "create table if not exists postit(id INTEGER PRIMARY KEY AUTOINCREMENT, title text check(length(title) <= 15) NOT NULL,  note text NOT NULL, published DATETIME NOT NULL)"
    SQL_CREATE_INDEX = "create index if not exists postit_id_index on postit (id)"
    # show tables
    SQL_SHOW_TABLES = "select * from sqlite_master where type='table'"
    # statment select
    SQL_SELECT_ALL= "select * from postit"
    # statement prepared
    SQL_INSERT = "insert into postit (title, note, published) values (?, ?, ?)"

    def __init__(self, database):
        self.connection = None
        self.database = database + ".db"
        self.connection_status = False


    def initialize_sqllite_database(self):
        try:
            self.connection = self.connect_sqllite_database()
            with self.connection:
                cur = self.connection.cursor()
                cur.execute(self.SQL_CREATE_TABLE)
                logger.info("Created database: " + str(self.database))
        except sqlite3.OperationalError as ex:
            logger.error(ex)

    def initialize_sqllite_index(self):
        try:
            self.connection = self.connect_sqllite_database()
            with self.connection:
                cur = self.connection.cursor()
                cur.execute(self.SQL_CREATE_INDEX)
                logger.info("Created index")
        except sqlite3.OperationalError as ex:
            logger.error(ex)

    def connect_sqllite_database(self):
        try:
            self.connection = sqlite3.connect(self.database)
            self.connection_status = True
        except Exception as ex:
            logger.error(ex)
        return self.connection


    def close_sqllite_database(self):
        try:
            self.connection.close()
            logger.info("Closing connection")
        except sqlite3.OperationalError as ex:
            logger.info(ex)

    def show_sqllite_tables(self):
        try:
            self.connection = self.connect_sqllite_database()
            with self.connection:
                cur = self.connection.cursor()
                cur.execute(self.SQL_SHOW_TABLES)
                row = cur.fetchall()
                logger.info("Show tables: " + str(row))
        except sqlite3.OperationalError as ex:
            logger.error(ex)

    def get_all_sqllite(self):
        try:
            self.connection = self.connect_sqllite_database()
            with self.connection:
                cur = self.connection.cursor()
                cur.execute(self.SQL_SELECT_ALL)
                row = cur.fetchall()
                logger.info("Show rows: " + str(row))
        except sqlite3.OperationalError as ex:
            logger.error(ex)

    def insert_sqllite(self, note_title, note_comment):
        try:
            self.connection = self.connect_sqllite_database()
            with self.connection:
                ts = datetime.datetime.now()
                cur = self.connection.cursor()
                cur.execute(self.SQL_INSERT, (note_title, note_comment, ts))# wrap it
                self.connection.commit()
                row = cur.fetchone()
                logger.info("Insert rows: " + str(row))
        except sqlite3.OperationalError as ex:
            logger.error(ex)
        except sqlite3.IntegrityError as ex:
            logger.error(ex)

    def update_sqllite(self):
        pass
    def delete_sqllite(self):
        pass



if __name__ == "__main__":
    sq = SqlLiteAdapter("test2")
    sq.initialize_sqllite_database()
    sq.initialize_sqllite_index()
    sq.show_sqllite_tables()
    sq.insert_sqllite("Netflix", "Series")
    sq.get_all_sqllite()
