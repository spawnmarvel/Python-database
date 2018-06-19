


import psycopg2
import sys
import json
import datetime as d


class DbConnector:
    """docstring for DbConnector"""

    def __init__(self):
        self.auth_status = False
        self.now = d.datetime.today().replace(microsecond=0)
        self.conn = None
    # format for auth
    # { "database":"ip21", "user":"youruser", "host":"localhost", "pw":"yourpass", "port":5432 }
    def get_auth(self):
        json_result = ""
        try:
            with open("auth.json", "r") as json_file:
                json_result = json.load(json_file)
        except FileNotFoundError as e:
            print(e)
        except Exception as e:
            print("Unexpected Error:", sys.exc_info()[0] + " " + e)
        return json_result

    def db_connector_open(self):
        json_result = self.get_auth()
        try:
            db, us, ho, pa, po = json_result["database"], json_result[
                "user"], json_result["host"], json_result["pw"], json_result["port"]
            self.conn = psycopg2.connect(
                database=db, user=us, host=ho, password=pa, port=po)
            self.auth_status = True
            print("Connected with psycopg2 \n" + format(self.now))
        except psycopg2.Warning as e:
            print("Warn " + str(e))
        except psycopg2.Error as e:
            print("Erro " + str(e))
        except Exception as e:
            print(e)
            print("Unexpected Error:", sys.exc_info()[0])
        return self.conn

    def db_connector_close(self, connector):
        conn_status = False
        try:
            if self.auth_status:
                connector.close()
                conn_status = True
                print("db is closed")
            else:
                print("No need to close db")
        except psycopg2.Warning as e:
            print(e)
        except psycopg2.Error as e:
            print(e)
        except Exception as e:
            print("Unexpected Error:", sys.exc_info()[0] + " " + e)
        return conn_status


    
    def sql_all(self, *args):
        rows = None
        try:
            tmp_connector = self.db_connector_open()
            if self.auth_status:
                cur = self.conn.cursor()
                sql = "select * from ip_discretedef"
                cur.execute(sql)
                rows = cur.fetchall()
                self.db_connector_close(tmp_connector)

            else:
                print("Auth is not working")

        except TypeError as e:
            print(e)
        except IndexError as e:
            print(e)
        except psycopg2.Warning as e:
            print(e)
        except psycopg2.Error as e:
            print(e)
        except Exception as e:
            print(e)
            print("Unexpected Error:", sys.exc_info()[0])
        return rows

    def sql_update(self, tag_id, tag_value):
        rows = None
        try:
            tmp_connector = self.db_connector_open()
            if self.auth_status:
                cur = self.conn.cursor()
                sql = "update ip_discretedef set tag_value = " + str(tag_value) + ", tagtime = '" + str(self.now) + "' where id = 1" #  + format(tag_id)
                print(sql)
                cur.execute(sql)
                tmp_connector.commit()
                rows = "Insert one"
                self.db_connector_close(tmp_connector)

            else:
                print("Auth is not working")

        except TypeError as e:
            print(e)
        except IndexError as e:
            print(e)
        except psycopg2.Warning as e:
            print(e)
        except psycopg2.Error as e:
            print(e)
        except Exception as e:
            print(e)
            print("Unexpected Error:", sys.exc_info()[0])
        return rows




data = DbConnector()
# rv = data.sql_all()
# for r in rv:
#     print(r)

# update
print(data.sql_update(1, 250))
