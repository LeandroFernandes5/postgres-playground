import psycopg
from faker import Faker
from random import randint 
import time

'''
Change according to how many records you want to insert. 
Recommendation is to use anything above 1 000 000
    the bigger the number the bigger the performance improvement using prepared statements
'''
records_to_insert = 10000
url_string = 'postgres://postgres:postgres@localhost:15432/postgres'

'''
    Edit as per your database connection details
'''
fake = Faker()
data = []

print(f" == Generating random data. == \n")
for i in range(records_to_insert):
    firstname = fake.first_name()
    lastname = fake.last_name()
    name = fake.name()
    createdat = fake.date_between(start_date='-4y', end_date='-1y')
    emailaddress = fake.email()
    lockout = fake.boolean()
    status = randint(1,5)
    lockout_date = None if lockout == False else fake.date_between(start_date='-1y', end_date='today')

    data.append((firstname, lastname, name, createdat, emailaddress, lockout, status, lockout_date))

with psycopg.connect(conninfo=url_string) as conn:

    with conn.cursor() as cur:
        print(f" == Starting insert statements into user_ table.== \n")
        start = time.time()
        cur.executemany('''insert into user_ (FIRSTNAME, LASTNAME, NAME, CREATEDAT, 
                            EMAILADDRESS, LOCKOUT, STATUS, LOCKOUT_DATE) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)''', data)
        end = time.time()
        
        conn.commit()
        
        print(f" == Time taken to populate table: {end - start : .2f} seconds. ==")