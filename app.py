from flask import Flask
app = Flask(__name__)

@app.route("/")

def home():
    return "Instalaçao do Flask"

def teste():
    return "<p> Testando 1 </p>"
    
def teste2():
    return "<p> Testando 2 </p>"

app.add_url_rule("/teste","teste", teste)
app.add_url_rule("/teste2","teste2", teste2)

if __name__ == "__main__":
    app.run(debug=True)