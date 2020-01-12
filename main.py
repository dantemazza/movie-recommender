from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
import yaml
from common.statements import *
import train
import datasets.dataParser as ds
import common.configuration as config
import common.const as const

app = Flask(__name__)

# Configure db
db = yaml.load(open('db.yaml'))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)
if config.launch:
    exec("launch.py")
else:
    ds.parseData()

@app.route('/', methods=['GET', 'POST'])
def index():
    cur = mysql.connection.cursor()
    if request.method == 'POST':
        if "output" in request.form:
            if config.train:
                cur = mysql.connection.cursor()
                cur.execute(get_ratings)
                data = cur.fetchall()
                train.train(data)
            movies = train.output()
            return const.html_list_wrapper.format(*movies)
        elif "title" in request.form:
            #fetch form data
            ratingDetails = request.form
            title = ratingDetails['title']
            rating = ratingDetails['rating']
            cur.execute(insert_rating.format(title, rating))
            mysql.connection.commit()
            cur.close()
            return redirect('/ratings')
        # elif "search" in request.form:
        #     search = request.form
        #     search_text = search['search']

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


