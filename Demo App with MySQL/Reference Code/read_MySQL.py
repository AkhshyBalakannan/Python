from mysql.connector import connect, Error

try:
    with connect(
        host="localhost",
        user=input("Enter username: "),
        password=input("Enter password: "),
        database="online_movie_rating",
    ) as connection:
        print(connection)
        # Reading Records Using the SELECT Statement
        select_movies_query = "SELECT * FROM movies LIMIT 5" 
        # this limits the output that we get at a time we also have offset by giving limit 2,5 
        # which the 2 is the offset and the 5 is row count that is to be sorted
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            result = cursor.fetchall() # This fetchall collects all data at once and stores in list
            for row in result:
                print(row)
        select_movies_query = "SELECT title, release_year FROM movies LIMIT 5"
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for row in cursor.fetchall():
                print(row)
        
        # Filtering Results Using the WHERE Clause

        select_movies_query = """
        SELECT title, collection_in_mil
        FROM movies
        WHERE collection_in_mil > 300
        ORDER BY collection_in_mil DESC
        """
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(movie)
        

        # we also have concatenating strings in MySQl
        select_movies_query = """
        SELECT CONCAT(title, " (", release_year, ")"),
        collection_in_mil
        FROM movies
        ORDER BY collection_in_mil DESC
        LIMIT 5"""
        with connection.cursor() as cursor:
            cursor.execute(select_movies_query)
            for movie in cursor.fetchall():
                print(movie)
        
        # Updating and Deleting Records From the Database
        update_query = """
        UPDATE
        reviewers
        SET
        last_name = "Cooper"
        WHERE
        first_name = "Amy"
        """
        with connection.cursor() as cursor:
            cursor.execute(update_query)
            connection.commit()
        
        # this where is the point which tells MySQL to look to make changes

        # DELETE Command

        delete_query = "DELETE FROM ratings WHERE reviewer_id = 2"
        with connection.cursor() as cursor:
            cursor.execute(delete_query)
            connection.commit()
except Error as e:
    print(e)