from flask import Flask

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    return "Login route working!"

if __name__ == '__main__':
    app.run(debug=True)
