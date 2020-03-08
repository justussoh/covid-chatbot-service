import psycopg2 as psy

# Use this script to populate data

seed_data = (
        """INSERT INTO users (session_id,name)
        VALUES ( 'A1234567C', 'Pereira Yip');""",)

cur = conn.cursor()
for seed in seed_data:
    cur.execute(seed)

# close communication with the PostgreSQL database server
cur.close()
# commit the changes
conn.commit()

