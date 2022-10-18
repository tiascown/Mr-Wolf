-- mrwolf_schema.sql

create table city (
    id          integer primary key autoincrement not null,
    name        text,
    timezone    text not null references timezone(id)
);

create table timezone (
    id           integer primary key autoincrement not null,
    name         text
);