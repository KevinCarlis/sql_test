import mysql.connector
from mysql.connector import errorcode

#import os
#host = os.popen('ip route show | grep "default" | awk \'{print $3}\'').read().split('\n')[0]
#print(host)

try:
    cnx = mysql.connector.connect(user='root',
                                  password='password',                      
                                  #host='127.20.48.1',
                                  #host='localhost',
                                  database='employees')
    cursor = cnx.cursor()
    query = ("SELECT employees.first_name, employees.last_name, departments.dept_name, salaries.salary "
             "FROM dept_manager "
                "INNER JOIN employees ON dept_manager.emp_no=employees.emp_no "
                "INNER JOIN departments ON dept_manager.dept_no=departments.dept_no "
                "INNER JOIN salaries ON dept_manager.emp_no=salaries.emp_no "
             "WHERE dept_manager.to_date='9999-01-01' AND salaries.to_date='9999-01-01'")
    cursor.execute(query)
    for x in cursor:
        print("{:14} {:16} {:20} {: >6}".format(*x))
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cnx.close()

