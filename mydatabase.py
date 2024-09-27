from sqlite3 import connect

class Database:
    db=None

    @staticmethod
    def connect_database():
        Database.db = connect("number.db")
        cursor = Database.db.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users
            (
                id integer PRIMARY KEY,
                email text NOT NULL,
                password text NOT NULL
            );
        """)
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fact_table
            (
                id integer PRIMARY KEY,
                email text NOT NULL,
                fact text NOT NULL
            );
        """)

        Database.db.commit()
        print("Connected succesfully")

    @staticmethod
    def insert_data(email, password):
        sql = "INSERT INTO users (email, password) VALUES (?, ?)"
        val = (f"{email}", f"{password}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)

        Database.db.commit()

    @staticmethod
    def email_valid(email):
        sql = f"SELECT * FROM users WHERE email='{email}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        if result:
            return False
        return True

    @staticmethod
    def user_exists(email, password):
        sql = f"SELECT * FROM users WHERE email='{email}' AND password='{password}'"

        cursor = Database.db.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        if result:
            return True
        return False
    
    @staticmethod
    def insert_fact(email, fact):
        sql = "INSERT INTO fact_table (email, fact) VALUES (?, ?)"
        val = (f"{email}", f"{fact}")
        cursor = Database.db.cursor()
        cursor.execute(sql, val)

        Database.db.commit()

    @staticmethod
    def retrieve_facts(email):
        sql = f"SELECT fact FROM fact_table WHERE email = '{email}'"
        cursor = Database.db.cursor()
        cursor.execute(sql)

        result = cursor.fetchall()

        return result