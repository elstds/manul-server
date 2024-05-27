import psycopg2
class Connection:
    def __init__(self, host, user, password, db_name):
        self.host = host
        self.user = user,
        self.password = password,
        self.db_name = db_name,
    def open(self):
        try:
            connection = psycopg2.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.db_name
            )
        except Exception as Ex:
            print("[Info] Connection error: ", Ex)
        finally:
            return connection

    def close(self):
        self._connection.close()
