import sqlite3

def create_users_table():
    with sqlite3.connect("data/manul.db") as con:
        cur = con.cursor()
        querry = ("CREATE TABLE IF NOT EXISTS users("
                  "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                  "username TEXT NOT NULL,"
                  "name TEXT NOT NULL,"
                  "surname TEXT NOT NULL,"
                  "password TEXT NOT NULL,"
                  "role_id INTEGER,"
                  "picture TEXT,"
                  "FOREIGN KEY (role_id) REFERENCES roles(id)"
                  ");")
        cur.execute(querry)
        cur.close()

def create_roles_table():
    with sqlite3.connect("data/manul.db") as con:
        cur = con.cursor()
        querry = ("CREATE TABLE IF NOT EXISTS roles("
                  "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                  "rolename TEXT NOT NULL,"
                  "privilegits TEXT"
                  ");")
        cur.execute(querry)
        cur.close()

def add_base_roles():
    with sqlite3.connect("data/manul.db") as con:
        cur = con.cursor()
        querry = "INSERT INTO roles (rolename) VALUES ('Supervisor'), ('Administrator'), ('Master'), ('Manager');"
        cur.execute(querry)
        cur.close()