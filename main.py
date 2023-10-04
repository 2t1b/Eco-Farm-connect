from flask import Flask, render_template , request , send_from_directory

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


@app.route("/")
def hello_selam():
    return render_template('home.html', list=List)

@app.route("/api/list")
def request_list():
    return jsonify(List)

@app.route('/register')
def register():
    return render_template('registration.html')
  
@app.route('/buyer')
def post():
    return render_template('buyer_requirements.html')
  
@app.route('/back')
def exit ():
    return render_template('home.html')
@app.route('/user')
def dash_board ():
    return render_template('user.html')
  
@app.route('/dashuser')
def dash_board2 ():
    return render_template('dashuser.html')

@app.route('/buyer_requirements', methods=['GET'])
def buyer_requirements():
    return render_template('buyer_requirements.html')

@app.route('/submit_requirements', methods=['POST'])
def submit_requirements():
    items = request.form.get('items')
    requirements = request.form.get('requirements')
    price = request.form.get('price')
   
  
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)