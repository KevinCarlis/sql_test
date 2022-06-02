from flask import Flask
import mysql.connector
from mysql.connector import errorcode
app = Flask(__name__)

#import os
#host = os.popen('ip route show | grep "default" | awk \'{print $3}\'').read().split('\n')[0]
#print(host)

def connect():
    try:
        cnx = mysql.connector.connect(user='root',
                                      password='password',                      
                                      host='db',
                                      #host=host,
                                      #host='localhost',
                                      port='3306',
                                      database='employees')
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()

@app.route('/')
def query():
    cnx = connect()
    cursor = cnx.cursor()
    query = ("SELECT employees.first_name, employees.last_name, departments.dept_name, salaries.salary "
             "FROM dept_manager "
                 "INNER JOIN employees ON dept_manager.emp_no=employees.emp_no "
                 "INNER JOIN departments ON dept_manager.dept_no=departments.dept_no "
                 "INNER JOIN salaries ON dept_manager.emp_no=salaries.emp_no "
             "WHERE dept_manager.to_date='9999-01-01' AND salaries.to_date='9999-01-01'")
    cursor.execute(query)
    ret = ''
    for x in cursor:
        ret += "{:14} {:16} {:20} {: >6}\n".format(*x)
    return ret

if __name__ == '__main__':
    app.run()

