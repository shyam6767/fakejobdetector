from flask import Flask;
app = Flask(__name__)
@app.route("/")
def home():
    return "6767676767676767676767"
if __name__ == '__main__':
    app.run(debug=True)