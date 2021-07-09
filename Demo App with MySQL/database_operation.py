'''This module contains all the operation that has
to be carried out in the MySQL'''

from mysql.connector import connect, Error


def insert_user(user_name, first_name, last_name, password, amount):
    try:
        with connect(
            host="localhost",
            # user=input("Enter username: "),
            # password=input("Enter password: "),
            user='root',
            password='1234',
            database='bankapp'
        ) as connection:
            print(connection)

            insert_users_query = '''
                INSERT INTO userdata
                (user_name, first_name, last_name, password, amount)
                VALUES ( %s, %s, %s, %s, %s )
                '''
            insert_user_record = [
                (user_name, first_name, last_name, password, amount),
            ]
            with connection.cursor() as cursor:
                # cursor.execute(create_data_base_query)
                # cursor.execute(create_table_query)
                cursor.executemany(insert_users_query, insert_user_record)
                connection.commit()

            # insert_user()

    except Error as e:
        print(e)


def get_user_detail(user_name):
    try:
        with connect(
            host="localhost",
            # user=input("Enter username: "),
            # password=input("Enter password: "),
            user='root',
            password='1234',
            database='bankapp'
        ) as connection:
            print(connection)
            select_user_query = """
            SELECT user_name, amount
            FROM userdata
            WHERE user_name = %s
            """
            user_data = [
                (user_name)
            ]
            with connection.cursor() as cursor:
                cursor.execute(select_user_query, user_data)
                # cursor.fetchone()
                user = cursor.fetchone()
                print('Found the user_name: ', user[0])
                print('Your balance with us: ', user[1])
        return user
    except Error as e:
        print(e)


def deposit_amount(user_name, amount):
    try:
        with connect(
            host="localhost",
            # user=input("Enter username: "),
            # password=input("Enter password: "),
            user='root',
            password='1234',
            database='bankapp'
        ) as connection:
            print(connection)
            select_user_query = """
            SELECT amount
            FROM userdata
            WHERE user_name = %s
            """
            get_user_data = [
                (user_name)
            ]
            with connection.cursor() as cursor:
                cursor.execute(select_user_query, get_user_data)
                user = cursor.fetchone()
                print(user[0])
                current_amount = int(user[0])
            # print(amount)
            # print(type(amount))
            # amount = str(amount)
            # print(type(amount))

            update_query = """
            UPDATE userdata
            SET amount = %s
            WHERE user_name = %s
            """
            set_user_data = [
                (amount, user_name)
            ]
            with connection.cursor() as cursor:
                cursor.execute(update_query, set_user_data)
                connection.commit()

    except Error as e:
        print(e)


def delete_user_data(username):
    try:
        with connect(
            host="localhost",
            # user=input("Enter username: "),
            # password=input("Enter password: "),
            user='root',
            password='1234',
            database='bankapp'
        ) as connection:
            print(connection)
            delete_query = '''
            DELETE FROM userdata
            WHERE user_name = %s'''
            select_user_query = [
                (username)
            ]
            with connection.cursor() as cursor:
                cursor.execute(delete_query, select_user_query)
                connection.commit()

    except Error as e:
        print(e)
