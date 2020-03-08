import psycopg2 as psy

# Use this script to populate data

seed_data = (
        """INSERT INTO users (session_id,name)
        VALUES ( 'A1234567C', 'Pereira Yip');""",)

try:
    conn = psy.connect("dbname='covid' user='admin' host='35.239.162.61' password='12345678'")
except:
    print("Error connecting to database.")

cur = conn.cursor()
for seed in seed_data:
    cur.execute(seed)

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()

