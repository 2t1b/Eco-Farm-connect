from flask import Flask, render_template , jsonify

app = Flask(__name__)

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
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)