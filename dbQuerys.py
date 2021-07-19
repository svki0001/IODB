from DB import db
class dbQuerys:
    @classmethod
    def add_user(self, cardID, username, email, prename, surname, birthDate, sex, validityDate, state, note, rights, street, postcode, city):
        db.connection.ping(reconnect = True)

        cursor = db.connection.cursor()

        sql = (
            "INSERT INTO Users (cardID, username, email, prename, surname, birthDate, sex, validityDate, state, note, rights, street, postcode, city)"
            f"VALUES ('{cardID}', '{username}', '{email}', '{prename}', '{surname}', '{birthDate}', '{sex}', '{validityDate}', '{state}', '{note}', '{rights}', '{street}', {postcode}, '{city}')"
        )
        cursor.execute(sql)

        cursor.execute(sql)

    @classmethod
    def get_random_cardID(self):
        db.connection.ping(reconnect = True)

        cursor = db.connection.cursor(dictionary = True, buffered = True)

        sql = """SELECT cardID FROM Users
                 ORDER BY RAND()
                 LIMIT 1;"""

        cursor.execute(sql)

        data = cursor.fetchone()

        return data["cardID"]

    @classmethod
    def addStrike(self, strikeID, sessionID, description):
        db.connection.ping(reconnect = True)

        cursor = db.connection.cursor()

        sql = (
            "INSERT INTO Strikes (strikeID, sessionID, description)"
            f"VALUES ('{strikeID}', '{sessionID}', '{description}')"
        )
        cursor.execute(sql)

    @classmethod
    def addLog(self, sessionID, cardID, checkIn, checkOut):
        db.connection.ping(reconnect = True)

        cursor = db.connection.cursor()

        sql = (
            "INSERT INTO Log_Users (sessionID, cardID, checkIn, checkOut)"
            f"VALUES ('{sessionID}', '{cardID}', '{checkIn}', '{checkOut}')"
        )
        cursor.execute(sql)

    @classmethod
    def addContract(self, contractID, email, contractBegin, contractEnd, contractPath, contractPaid):
        db.connection.ping(reconnect = True)

        cursor = db.connection.cursor()

        sql = (
            "INSERT INTO Contracts (contractID, email, contractBegin, contractEnd, contractPath, contractPaid)"
            f"VALUES ('{contractID}', '{email}', '{contractBegin}', '{contractEnd}', '{contractPath}', '{contractPaid}')"
        )
        cursor.execute(sql)
