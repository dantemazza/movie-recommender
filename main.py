from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        #fetch form data
        ratingDetails = request.form
        title = ratingDetails['title']
        rating = ratingDetails['rating']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO useratings(title, rating) VALUES(%s, %s)", (title, rating))
        mysql.connection.commit()
        cur.close()
        return redirect('/useratings')
    return render_template('index.html')

@app.route('/useratings')
def useratings():
    cur = mysql.connection.cursor()
    res = cur.execute('SELECT * from useratings')
    if res > 0:
         ratingDetails = cur.fetchall()
         return render_template('ratings.html', ratingDetails=ratingDetails)


if __name__ == '__main__':
    app.run(debug=True)


