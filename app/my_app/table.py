from flask import Blueprint
from flask import render_template

from my_app.db import get_db

bp = Blueprint("table", __name__)

@bp.route('/')
def table():
    db = get_db()
    cursor = db.cursor()
    query = ("SELECT employees.first_name, employees.last_name, departments.dept_name, salaries.salary "
             "FROM dept_manager "
                 "INNER JOIN employees ON dept_manager.emp_no=employees.emp_no "
                 "INNER JOIN departments ON dept_manager.dept_no=departments.dept_no "
                 "INNER JOIN salaries ON dept_manager.emp_no=salaries.emp_no "
             "WHERE dept_manager.to_date='9999-01-01' AND salaries.to_date='9999-01-01'")
    cursor.execute(query)
    return render_template('table.html', tables=cursor)

if __name__ == '__main__':
    app.run()

