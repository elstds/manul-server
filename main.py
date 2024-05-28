from utils import tables
from utils import users
from utils import check_for_injection

def main():
    querry = "INSERT INTO users (name) VALUES (1); DROP TABLE users;"
    print(check_for_injection(querry))


if __name__ == "__main__":
        main()