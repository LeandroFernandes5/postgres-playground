![](PostgreSQL-Playground.webp)

# PostgreSQL Playground

I use to find myself needing a ready-to-go postgres database, usually the latest supported version to test indexing/ partitions/ ideas or anything that was scratching that part of my mind. 

The pursue to find a quick docker-compose.yml that would allow me to run "docker compose up -d" and be ready to test whatever I needed was never straight forward. Sometimes I would have conflicting ports, not the customaziation needed either on pg_hba.conf or postgresql.conf. Even on my best day I would find that docker file, I would still have an empty database.. No tables or data to play with.. 

Relevant information for each custom file provided:

[Docker Compose](./docker-compose.yml): 
1. Uses the latest postgres image available
2. Set the container memory to 1G 
3. Set postgres user , password and database to "postgres"
4. Listens on 15432 outside of the container

[pg_hba.conf](./pg_hba.conf):
1. Added extra line to accept connections from outside of the container

[PostgreSQL config](./postgresql.conf): 
1. Increased shared_buffers to 128MB
2. Changed listen_address to all
3. Log all database statements

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
