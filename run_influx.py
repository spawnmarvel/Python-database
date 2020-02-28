from app_exceptions.custom_exceptions import CustomExceptions
from app_logs.app_logger import Logger
import random
import json
import datetime
import influxdb
from requests.exceptions import ConnectionError

INFLUX_HOST = "localhost"
INFLUX_PORT = 8086
INFLUX_USER = "admin"
INFLUX_CRED = "admin"
INFLUX_DB = "gtech" # it is default in env docker

logger = Logger().get()


class InfluxAdapter():

    def __init__(self):
        self.client = None
        self.database = None
        self.connection_status = False
        self.database = INFLUX_DB

    def connect_influxdb(self):
        try:
            self.client = influxdb.InfluxDBClient(
                host=INFLUX_HOST, port=INFLUX_PORT, username=INFLUX_USER, password=INFLUX_CRED)
            self.connection_status = True
            available_db = self.client.get_list_database()
            self.check_influx_database(available_db)
            self.client.switch_database(self.database)
            self.connection_status = True
        except ConnectionError as ex:
            logger.error(ex)
        return self.client

    def check_influx_database(self, li):
        db_exist = False
        try:
            for item in li:
                if item["name"] == self.database:
                    db_exist = True
            if db_exist:
                logger.info("Database already existed " + self.database)
            else:
                logger.info("Creating database " + self.database)
                self.client.create_database(self.database)
                new_available_db = self.client.get_list_database()
                logger.info(new_available_db)
        except CustomExceptions("Could not check database") as ex:
            logger.error(ex)
        return db_exist

    def get_influx_database(self, selected_db="test"):
        self.database = self.client[self.database]
        return self.database

    def close_influx_database(self):
        logger.info("Closing ...")
        self.client.close()

    def insert_influx(self, msg, batch=1000):
        rv = False
        count = 0
        try:
            rv = self.client.write_points(msg)
            for x in msg:
                logger.info(x["measurement"])
                logger.info(x["time"])
                logger.info(x["fields"]["Int_value"])
                count +=1
           
            # rv = self.client.write_points(msg, database="tullll")
        except influxdb.exceptions.InfluxDBClientError as ex:
            self.connection_status = False
            logger.info(ex)
        except AttributeError as ex:
            self.connection_status = False
            logger.error(
                "Tried to insert, but attribute error (influx_worker), raises AttributeError" + str(ex))
        logger.info("Insert : " + str(rv) + ". Amount: " + str(count))
        return rv

    def update_influx(self):
        pass

    def get_influx(self):
        rv = self.client.query('SELECT * FROM "sim11"')
        logger.info(rv)
    def get_measurements(self):
        rv = self.client.get_list_measurements()
        logger.info(rv)

    def delete_influx(self):
        pass

    def create_msg(self, meas_name, meas_time, meas_value):
        json_body = {
            
                "measurement": meas_name,
                "tags": {
                    "host": "simu",
                    "region": "us-west",
                    "security": "tbd"
                },
                "time": meas_time,
                "fields": {
                    # "Float_value": f_value,
                    "Int_value": meas_value,
                    # "String_value": "Text",
                    "Bool_value": True,
                    "sent_time": str(meas_time)
                }
            }
        
        return json_body

    def simulate_msg(self, msg_amount):
        li = []
        ran_name = random.randint(11, 12)
        name = "sim11"+ str(ran_name)
        value = random.randint(20, 79)
        ts = datetime.datetime.now()
        for x in range(msg_amount):
            msg = self.create_msg(
                meas_name=name, meas_time=ts, meas_value=value)
            li.append(msg)
        return li


if __name__ == "__main__":

    try:
        logger.info("##### INF start #####")
        inf = InfluxAdapter()
        inf.connect_influxdb()
        msg = inf.simulate_msg(4)
        inf.insert_influx(msg)
        inf.get_measurements()
        logger.info("\n")
        inf.get_influx()

        inf.close_influx_database()
        logger.info("\n")
        logger.info("https://influxdb-python.readthedocs.io/en/latest/api-documentation.html")
    except KeyboardInterrupt as ex:
        logger.error(ex)
        logger.info("closing")
