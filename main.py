import csv
from flask import Flask, render_template, request, jsonify, redirect, url_for,redirect
import os
app = Flask(__name__)
app.static_url_path = '/static'
app.static_folder = 'static'

List = [
    {
        'id': 1,
        'title': 'Teff supplier needed',
        'location': 'Addis Ababa, Ethiopia',
        'price': '8000 Br per quintal'
    },
    {
        'id': 2,
        'title': 'Sorghum supplier needed',
        'location': 'Shashemene, Ethiopia',
        'price': '5000 Br per quintal'
    },
    {
        'id': 3,
        'title': 'Wheat and Maize supplier needed',
        'location': 'Arbaminch, Ethiopia',
        'price': '6000-7700 Br per quintal'
    },
    {
        'id': 4,
        'title': 'Chickpea supplier needed',
        'location': 'Addis Ababa, Ethiopia',
        'price': '5500 Br per quintal'
    },
    {
        'id': 5,
        'title': 'Soybean supplier needed',
        'location': 'Adama, Ethiopia',
        'price': '9000 Br per quintal'
    }
]

def save_profile_to_csv(profile_data):
    fieldnames = ['First Name', 'Last Name', 'Username', 'Password', 'Country', 'Town', 'Phone Number','value']
    csv_file = 'user_profiles.csv'

    with open(csv_file, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        if file.tell() == 0:
            writer.writeheader()

        writer.writerow(profile_data)

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
    return render_template('home.html', list=List)
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
@app.route('/buyer')
def post():
    return render_template('buyer_requirements.html')
@app.route('/back')
def exit():
    return render_template('home.html')
@app.route('/user')
def dash_board():
    return render_template('user.html')
@app.route('/dashuser')
def dash_board2():
    return render_template('dashuser.html')
@app.route('/buyer_requirements', methods=['GET'])
def buyer_requirements():
    return render_template('buyer_requirements.html')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if not check_login_credentials(username, password):
            return render_template('home.html', login_failed=True)

        return redirect(url_for('dash_board'))

    return render_template('home.html', login_failed=False)
@app.route('/submit_buyer_request.php', methods=['POST'])
def submit_buyer_request():
    if request.method == 'POST':
        products = request.form.get('products')
        requirements = request.form.get('requirements')
        price = request.form.get('price')
        contact = request.form.get('contact')

        if not products or not requirements or not price or not contact:
           
            return "Please fill in all the required fields"

        
        data = [products, requirements, price, contact]

        
        csvFilePath = 'buyer_requests.csv'

       
        with open(csvFilePath, 'a') as file:
            file.write(','.join(data) + '\n')

       
        return redirect('user')

    return "Invalid request"

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
    return render_template('registration.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)