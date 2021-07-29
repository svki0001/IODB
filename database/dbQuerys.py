from mysql.connector.cursor import CursorBase
from .DB import db

def add_user(cardID, username, email, prename, surname, birthDate, sex, validityDate, state, note, rights, street, postcode, city):
    cursor = db.connection.cursor()

    sql = (
        "INSERT INTO Users (cardID, username, email, prename, surname, birthDate, sex, validityDate, state, note, rights, street, postcode, city)"
        f"VALUES ('{cardID}', '{username}', '{email}', '{prename}', '{surname}', '{birthDate}', '{sex}', '{validityDate}', '{state}', '{note}', '{rights}', '{street}', {postcode}, '{city}')"
    )
    cursor.execute(sql)

def check_email(email):
    cursor = db.connection.cursor(dictionary = True, buffered = True)

    sql = f"SELECT 1 FROM Users WHERE email = '{email}';"

    cursor.execute(sql)

    data = cursor.fetchone()

    return data != None

def get_random_cardID():
    cursor = db.connection.cursor(dictionary = True, buffered = True)

    sql = """SELECT cardID FROM Users
                ORDER BY RAND()
                LIMIT 1;"""

    cursor.execute(sql)

    data = cursor.fetchone()

    return data["cardID"]

def add_strike(sessionID, description):
    cursor = db.connection.cursor()

    sql = (
        "INSERT INTO Strikes (sessionID, description)"
        f"VALUES ('{sessionID}', '{description}')"
    )
    cursor.execute(sql)

def add_log(cardID, checkIn, checkOut):
    cursor = db.connection.cursor()

    sql = (
        "INSERT INTO Log_Users (cardID, checkIn, checkOut)"
        f"VALUES ('{cardID}', '{checkIn}', '{checkOut}')"
    )
    cursor.execute(sql)

def add_contract(contractID, email, contractBegin, contractEnd, contractPath, contractPaid):
    cursor = db.connection.cursor()

    sql = (
        "INSERT INTO Contracts (contractID, email, contractBegin, contractEnd, contractPath, contractPaid)"
        f"VALUES ('{contractID}', '{email}', '{contractBegin}', '{contractEnd}', '{contractPath}', '{contractPaid}')"
    )
    cursor.execute(sql)

def select_contract_begin(contractID):
    cursor = db.connection.cursor(dictionary = True, buffered = True)

    sql = (
        "SELECT contractBegin "
        "FROM Contracts "
        f"WHERE contractID = '{contractID}'"
    )

    cursor.execute(sql)
    data = cursor.fetchone()

    return data["contractBegin"]

def select_cardids_by_rights(rights):
    cursor : CursorBase = db.connection.cursor(dictionary = True, buffered = True)

    sql = f"SELECT cardID FROM Users WHERE rights = '{rights}'"

    cursor.execute(sql)
    data = cursor.fetchall()

    return data

def update_user_note(note, cardID):
    cursor = db.connection.cursor()
    sql = f"UPDATE Users SET note = '{note}' WHERE cardID = '{cardID}'"
    cursor.execute(sql)

def update_user_rights_by_right(rights, where_rights):
    cursor = db.connection.cursor(dictionary = True, buffered = True)
    sql = f"UPDATE Users SET rights = '{rights}' WHERE rights = '{where_rights}'"
    cursor.execute(sql)

def update_user_rights_by_cardID(rights, cardID):
    cursor = db.connection.cursor(dictionary = True, buffered = True)
    sql = f"UPDATE Users SET rights = '{rights}' WHERE cardID = '{cardID}'"
    cursor.execute(sql)

def update_contract_end(contractID, contractEnd):
    cursor = db.connection.cursor()
    sql = f"UPDATE Contracts SET contractEnd = '{contractEnd}' WHERE contractID = '{contractID}'"
    cursor.execute(sql)