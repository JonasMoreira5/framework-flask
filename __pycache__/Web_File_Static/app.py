from flask import Flask

app = Flask(__name__, static_folder='static')

# code

if __name__=='__main__':
    app.run(debug=True)
