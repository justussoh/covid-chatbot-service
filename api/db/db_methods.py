import psycopg2 as psy

try:
    conn = psy.connect("dbname='covid' user='admin' host='35.239.162.61' password='12345678'")
    cur = conn.cursor()
except:
    print("Error connecting to database.")

def insert_query(query):
    cur.execute(query)
    cur.close()
    conn.commit()

def fetch_query(query):
    cur.execute(query)
    return cur.fetchall()
