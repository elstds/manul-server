from utils import hash_password
import sqlite3
def add_user(username, name, surname, password, role, pic=""):
    with sqlite3.connect("data/manul.db") as con:
        cur = con.cursor()
        password = hash_password(password)
        querry = (f"INSERT INTO users (username, name, surname, password, role, picture) VALUES (%s, %s, %s, %s, %s, %s);")
        try:
            cursor.execute(querry, (username, name, surname, password, role, pic))
        except Exception as ex:
            print("[Info] Ошибка добавления данных:", ex)
        finally:
            cursor.close()
            connection.close()


def rm_user(connection, user_id):
    pass

def list_users(connection):
    connection.open()
    cursor = connection.cursor()
    querry = "SELECT id, username, name, surname, role FROM users;"
    try:
        cursor.execute(querry)
        res = cursor.fetchone()
    except Exception as ex:
        print("[Info] Ошибка чтения данных:", ex)
    finally:
        cursor.close()
        connection.close()
        return res

def login():
    pass