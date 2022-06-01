# sql_test
Practice with docker and mysql

## Installation
I'm using this sql database for practice https://www.dropbox.com/s/znmjrtlae6vt4zi/employees.sql?dl=0 </br>
To add it to your server you need to put it in the root of the project sql_test/ and uncomment the line in the docker-compose db:volumes line. 
After you run this once you can then recomment it the line.
```
pip3 install mysql-connector-python
```

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
