from Connection import Connection
from config import *
from utils import hash_password
from utils import users

def main():
    con = Connection(host, user, password, db_name)
    users.add_user(con, "excretory", "Данила", "Шаталкин", "hello_world", "supervisor", "./data/avatars/001.png")

if __name__ == "__main__":
        main()