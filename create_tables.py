import psycopg2
from config import load_config

def create_tables():
    """ Creating table in database PostgreSQL """
    commands = (
        """
        CREATE TABLE contacts (
            contact_id SERIAL PRIMARY KEY,
            contact_name VARCHAR(255) NOT NULL,
            phone_number VARCHAR(50) NOT NULL
        )
        """,
    )
    try:
        config = load_config()
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                for command in commands:
                    cur.execute(command)
                    
        print("Table contacts successfully created!")
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

if __name__ == '__main__':
    create_tables()