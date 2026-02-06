from Django import models

CREATE TABLE User (
    id BIGINT PRIMARY KEY,
    name varchar(255),
    password varchar(255),
    created_at 
)