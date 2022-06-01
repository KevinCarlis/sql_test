# sql_test
Practice with docker and mysql

## Installation
I'm using this sql database for practice https://www.dropbox.com/s/znmjrtlae6vt4zi/employees.sql?dl=0 
to add it to your server you need to uncomment the line in the docker-compose db:volumes line and you can then recomment it after running once.

## Notes
I am not using the Dockerfile currently.

## Run
```
docker-compose up --build -d
```
```
python3 test.py
```
## Troubleshoot Server
```
docker exec -it test_sql mysql -uroot -p
```
password=password
