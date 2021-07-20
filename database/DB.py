import mysql.connector
import time

class DB():
    connection = None

    def __init__(self, host, user, password, database):
        self.host = host;
        self.user = user;
        self.password = password;
        self.database = database;

        self.connect()

    def connect(self):
        try:
            self.connection =  mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database,
                autocommit = True,
            )
        except Exception as exception:
            print("[DBCONNECTION] {exception} Retrying in 5 seconds.".format(exception = str(exception)))
            time.sleep(5)
            self.connect()


# test
db = DB("91.204.46.200", "k146591_jonas", "Q6zo9!r3", "k146591_Sportraum_IODB")
