import csv
from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float, text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import declarative_base
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['APP_CONFIG']

db = SQLAlchemy(app)

engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Base = declarative_base()

class Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250))
    location = db.Column(db.String(250))
    price = db.Column(db.String(100))  # Specify the column type as Numeric
    requirement = db.Column(db.String(2000))
    phone_number = db.Column(db.String(20))


def load_request_from_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM jobs"))
            result_all = result.all()
            
            result_dicts = []
            for row in result_all:
                result_dicts.append(result_dict(row))
                
            return result_dicts
    except Exception as e:
        # Handle the exception or log the error
        print(f"An error occurred: {str(e)}")
def save_profile_to_csv(profile_data):
    fieldnames = ['First Name', 'Last Name', 'Username', 'Password', 'Country', 'Town', 'Phone Number', 'User Type']
    csv_file = 'user_profiles.csv'

    try:
        with open(csv_file, 'a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if file.tell() == 0:
                writer.writeheader()

            writer.writerow(profile_data)

    except Exception as e:
        # Handle the exception or log the error
        print(f"An error occurred: {str(e)}")

def is_username_registered(username):
    csv_file = 'user_profiles.csv'

    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] == username:
                return True

    return False

def check_login_credentials(username, password):
    csv_file = 'user_profiles.csv'
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] == username and row['Password'] == password:
                return True
    return False

@app.route("/")
def hello_selam():
    jobs = Jobs.query.all()
    return render_template('ho.html', jobs=jobs)
   
   

@app.route("/api/list")
def request_list():
    return jsonify(List)
@app.route('/register', methods=['GET', 'POST'])
def register():
    not_registered = False
    if request.method == 'POST':
        first_name = request.form.get('firstName')
        last_name = request.form.get('lastName')
        username = request.form.get('username')
        password = request.form.get('password')
        country = request.form.get('country')
        town = request.form.get('town')
        phone_number = request.form.get('phoneNumber')
        user_type = request.form.get('userType')
        if is_username_registered(username):
            not_registered = True
        else:
            profile_data = {
                'First Name': first_name,
                'Last Name': last_name,
                'Username': username,
                'Password': password,
                'Country': country,
                'Town': town,
                'Phone Number': phone_number,
                'User Type': user_type
            }
            save_profile_to_csv(profile_data)

    return render_template('registration.html', not_registered=not_registered)
  
@app.route('/buyer/', methods=['GET', 'POST'])
def buy():
    if request.method == 'POST':
        jobs = Jobs(
            title=request.form.get('title'),
            location=request.form.get('location'),
            price=request.form.get('price'),
            requirement=request.form.get('requirement'),
            phone_number=request.form.get('phone_number')
        )
        db.session.add(jobs)
        db.session.commit()
        return redirect(url_for('buyer_post'))
    else:
        return render_template('list.html')

@app.route('/buyer/post')
def buyer_post():
    jobs = Jobs.query.all()
    return render_template('post.html', jobs=jobs)
   
@app.route('/back')
def exit():
    return render_template('ho.html')
@app.route('/user')
def dash_board():
    return render_template('user.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not check_login_credentials(username, password):
            return render_template('ho.html', login_failed=True)

        return redirect(url_for('dash_board'))

    return render_template('ho.html', login_failed=False)
  
@app.route('/save.php', methods=['POST'])
def save_form_data():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        username = request.form['username']
        password = request.form['password']
        country = request.form['country']
        town = request.form['town']
        phone_number = request.form['phoneNumber']
        user_type = request.form.get('userType')

       
        if not all([first_name, last_name, username, password, country, town, phone_number]):
            error_message = 'Please fill in all fields!'
            return render_template('registtration.html', error_message=error_message)

        profile_data = {
            'First Name': first_name,
            'Last Name': last_name,
            'Username': username,
            'Password': password,
            'Country': country,
            'Town': town,
            'Phone Number': phone_number
        }

        
        save_profile_to_csv(profile_data)

      
        return redirect(url_for('dash_board'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True) 
