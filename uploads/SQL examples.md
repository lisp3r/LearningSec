# SQL examples

Simple UNION SELECT:

    select * from demo where ID > 10 UNION SELECT NULL, username, NULL from users;