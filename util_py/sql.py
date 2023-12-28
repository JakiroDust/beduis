import psycopg2

password = "4feehGQ4diL3S45mAbhJleSihTcq"
def executeSQL(sql_queue,database): 
    # Establish a connection to the PostgreSQL server with AUTOCOMMIT enabled
    cnx = psycopg2.connect(
        user="citus",
        password=password,
        host="dbcloudeapp.postgres.database.azure.com",
        port=5432,
        database=database
    )

    # Create a cursor
    cursor = cnx.cursor()

    cursor.execute(sql_queue)

    # Commit the transaction
    cnx.commit()

    # Close the cursor and connection
    cursor.close()
    cnx.close()
    

def executeSQL_expectReturn(sql_queue,database): 
    # Establish a connection to the PostgreSQL server with AUTOCOMMIT enabled
    cnx = psycopg2.connect(
        user="citus",
        password=password,
        host="dbcloudeapp.postgres.database.azure.com",
        port=5432,
        database=database
    )

    # Create a cursor
    cursor = cnx.cursor()

    cursor.execute(sql_queue)
    result=cursor.fetchall()

    # Commit the transaction
    cnx.commit()

    # Close the cursor and connection
    cursor.close()
    cnx.close()
    return result
def executeSQL_expectReturn_clean(sql_queue,database): 
    return executeSQL_expectReturn(sql_queue,database)[0][0]