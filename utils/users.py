from utils import hash_password
def add_user(connection, username, name, surname, password, role, pic=""):
    connection.open()
    cursor = connection._connection.cursor()
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
    cursor = connection._connection.cursor()
    querry = "SELECT id, username, name, surname, role FROM users;"

def login():
    pass