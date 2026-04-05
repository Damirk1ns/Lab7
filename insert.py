import psycopg2
import csv
from config import load_config

def insert_contact(name, phone):
    """ Insert a single contact into the table """
    sql = "INSERT INTO contacts(contact_name, phone_number) VALUES(%s, %s)"
    config = load_config()
    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql, (name, phone))
                conn.commit()
                print(f"Contact '{name}' added successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")

def insert_from_csv(filepath):
    """ Insert contacts from a CSV file """
    sql = "INSERT INTO contacts(contact_name, phone_number) VALUES(%s, %s)"
    config = load_config()
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            reader = csv.reader(file)
            contact_list = list(reader)
            
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                cur.executemany(sql, contact_list)
                conn.commit()
                print("Contacts from CSV imported successfully.")
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Error: {error}")