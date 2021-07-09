from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=input("Enter password: "),
        database='bankapp'

    ) as connection:
        print(connection)
        create_data_base_query = '''
        CREATE DATABASE bankapp
        '''
        create_table_query = '''
        CREATE TABLE userdata(
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_name VARCHAR(100),
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        password VARCHAR(100),
        amount INT
        )
        '''
        insert_users_query = '''
        INSERT INTO userdata
        (user_name, first_name, last_name, password, amount)
        VALUES ( %s, %s, %s, %s, %s )
        '''
        insert_user_record = [
            ('akhshy1', 'akhshy', 'balakannan', 'akhshy123', '10000'),
            ('ashwin', 'ashwin', 'balakannan', 'ashwin123', '1000')
        ]
        with connection.cursor() as cursor:
            # cursor.execute(create_data_base_query)
            # cursor.execute(create_table_query)
            cursor.executemany(insert_users_query, insert_user_record)
            connection.commit()


except Error as e:
    print(e)
