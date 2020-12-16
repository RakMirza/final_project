from flask import Flask, render_template,jsonify
import json, sqlite3, datetime,requests
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["ENV"] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///covid19_death.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class  DBTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    state= db.Column(db.Text, nullable=False)
    age_group = db.Column(db.Text, nullable=False)
    condition_group = db.Column(db.Text, nullable=False)
    number_covid19_death= db.Column(db.Float, nullable=False)
   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api', methods=['GET'])
def get_data():
    table = DBTable.query.all()
    d = []
    for row  in table:  
        d.append(
            {
                'state': row.state, 
                'age_group': row.age_group,
                'condition_group': row.condition_group,
                'number_covid19_death' : row.number_covid19_death
            } )        
    return jsonify(d)

@app.route('/data')
def display_data():
    table = DBTable.query.all()
    d = []
    for row  in table:  
        d.append(
            {
                'state': row.state, 
                'age_group': row.age_group,
                'condition_group': row.condition_group,
                'number_covid19_death' : row.number_covid19_death
            } )        
    return render_template('base.html',data=d)
if __name__ == '__main__':
    app.run(debug=True)



