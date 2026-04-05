import psycopg2
from config import load_config

def update_contact(name, new_phone):
    """ Update a contact's phone number """
    sql = "UPDATE contacts SET phone_number = %s WHERE contact_name = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (new_phone, name))
                conn.commit()
                if cur.rowcount > 0:
                    print(f"Contact '{name}' updated successfully.")
                else:
                    print(f"Contact '{name}' not found.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def delete_contact(name):
    """ Delete a contact by name """
    sql = "DELETE FROM contacts WHERE contact_name = %s"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name,))
                conn.commit()
                if cur.rowcount > 0:
                    print(f"Contact '{name}' deleted successfully.")
                else:
                    print(f"Contact '{name}' not found.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")