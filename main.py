from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
from statements import *
import launch, train, dataParser
import datasets.dataParser as ds

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)
ds.parseData()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if "train" in request.form:

            train.train()
            return 'success'
        elif "title" in request.form:
            #fetch form data
            ratingDetails = request.form
            title = ratingDetails['title']
            rating = ratingDetails['rating']
            cur = mysql.connection.cursor()
            cur.execute(insert_rating.format(title, rating))
            mysql.connection.commit()
            cur.close()

            return redirect('/ratings')
    return render_template('index.html')

@app.route('/ratings')
def showRatings():
    cur = mysql.connection.cursor()
    res = cur.execute('SELECT * from ratings')
    if res > 0:
         ratingDetails = cur.fetchall()
         return render_template('ratings.html', ratingDetails=ratingDetails)


if __name__ == '__main__':
    app.run(debug=True)


