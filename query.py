import psycopg2
from config import load_config

def search_contact(term):
    """ Search contacts by name or phone number """
    sql = "SELECT * FROM contacts WHERE contact_name ILIKE %s OR phone_number LIKE %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                search_pattern = f"%{term}%"
                cur.execute(sql, (search_pattern, search_pattern))
                rows = cur.fetchall()
                
                print(f"Total records found: {len(rows)}")
                for row in rows:
                    print(f"ID: {row[0]} | Name: {row[1]} | Phone: {row[2]}")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")