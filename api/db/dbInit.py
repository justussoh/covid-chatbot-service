import psycopg2 as psy

class dbInit():
    try:
        try:
            conn = psy.connect("dbname='covid' user='admin' host='35.239.162.61' password='12345678'")
        except:
            print("Error connecting to database.")

        commands = (
                """
                CREATE TABLE users (
                    user_id SERIAL PRIMARY KEY,
                    session_id VARCHAR(255) NOT NULL,
                    name VARCHAR(255) NOT NULL,
                    created_at DATE NOT NULL DEFAULT CURRENT_DATE,
                    checked_in DATE,
                    qurantine_duration INT DEFAULT 14
                )
                """,)
        cur = conn.cursor()
        for command in commands:
            cur.execute(command)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()

    except psy.DatabaseError as e:
        print(e)