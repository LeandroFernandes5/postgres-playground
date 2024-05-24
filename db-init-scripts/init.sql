CREATE TABLE IF NOT EXISTS USER_ (
    id serial primary key, 
    firstname varchar(300),
    lastname varchar(300),
    name varchar(300), 
    createdat timestamp(6) without time zone,
    emailaddress varchar(300),
    lockout boolean, 
    status numeric(30, 0),
    lockout_date timestamp(6) without time zone
)