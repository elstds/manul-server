from utils import hash_password
import sqlite3
from utils import check_for_injection

def add_user(username, name, surname, password, role, pic=""):
    with sqlite3.connect("data/manul.db") as con:
        cur = con.cursor()
        password = hash_password(password)
        querry = (f"INSERT INTO users (username, name, surname, password, role_id, picture) VALUES "
                  f"('{username}', '{name}', '{surname}', '{password}', '{role}', '{pic}');")
        if check_for_injection(querry):
            cur.execute(querry)
            cur.close()
            return True
        else:
            cur.close()
            return False


def rm_user(username):
    with sqlite3.connect("data/manul.db") as con:
        cur = con.cursor()
        querry = f"DELETE FROM users WHERE username='{username}';"
        if check_for_injection(querry):
            cur.execute(querry)
            cur.close()
        else:
            return false

def list_users():
    with sqlite3.connect("data/manul.db") as con:
        cur = con.cursor()
        querry = "SELECT id, username, name, surname, role_id FROM users;"
        cur.execute(querry)
        res = cur.fetchall()
        cur.close()
        return res


def login(username, password):
    with sqlite3.connect('data/manul.db') as con:
        cur = con.cursor()
        password = hash_password(password)
        querry = f"SELECT * FROM users WHERE username='{username}' AND password='{password}';"
        if check_for_injection(querry):
            cur.execute(querry)
            res = cur.fetchone()
            cur.close()
            return res
        else:
            return False
