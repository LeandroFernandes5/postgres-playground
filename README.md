![](./PostgreSQL-playground.jpg)

# PostgreSQL Playground

I use to find myself needing a ready-to-go postgres database, usually the latest supported version to test indexing/ partitions/ ideas or anything that was scratching that part of my mind. 

The pursue to find a quick docker-compose.yml that would allow me to run "docker compose up -d" and be ready to test whatever I needed was never straight forward. Sometimes I would have conflicting ports, not the customaziation needed either on pg_hba.conf or postgresql.conf. Even on my best day I would find that docker file, I would still have an empty database.. No tables or data to play with.. 

Relevant information for each custom file provided:

1. [Docker Compose](./docker-compose.yml): 
    - Uses the latest postgres image available
    - Set the container memory to 1G 
    - Set postgres user , password and database to "postgres"
    - Listens on 15432 outside of the container

2. [pg_hba.conf](./pg_hba.conf):
    - Added extra line to accept connections from outside of the container

3. [PostgreSQL config](./postgresql.conf): 
    - Increased shared_buffers to 128MB
    - Changed listen_address to all
    - Log all database statements

### Note:
The database will initiate with a table called user_ which looks like a User information table from a Production application with hopes to allow to simulate real case scenarios.

At this point, our setup was ready we just needed to have data in our table. At this point we decided to create a Python script and use the Faker library to generate some random and usable data. 


A [requirements file](./requirements.txt) with Psycopg3 and Faker.
A [python script](./populate-db.py) that can be used to load whatever amount of records we fill necessary to test our scenario. 
 
### How to Populate PostgreSQL Database 

1. Create a virtual Environment 
```bash
python3 -m venv venv
```

2. Activate/source your new environment
```bash
source venv/bin/active
```

3. Install dependencies
```bash 
pip install -r requirements.txt
```

4. Run populate script 
```bash
python populate-db.py
```
