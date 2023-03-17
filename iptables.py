# save this as app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/start")
def index():
    if request_method == 'POST':
        return cred()
    else:    
        return render_template("index.html")

@app.route("/rules_filter")
def rules_filter():
    return render_template("rules_filter.html")

@app.route("/rules_nat")
def rules_nat():
    return render_template("ules_nat.html")

@app.route("/rules_nat_add")
def rules_nat_add():
    return "?"

@app.route("/alias")
def alias():
    return render_template("alias.html")

@app.route("/check_credentials", methods=["GET", "POST"])
def cred():
    #si login:mot de passe correspont à credential.txt 
    #donc connexion réussie
    #sinon connexion échouée
    entered_login = ? #retreive login from the page
    entered_pass = ? #retreive password from the form
    plain_text_to_check = entered_login + ":" + entered_pass
    base_64_char_entered_by_user_to_check = base64.b64encode(plain_text_to_check)
    
    f = open("credentials.txt", "r")
    base_64_login_in_data_base = f.read()
    

    if base_64_login_in_data_base == base_64_char_entered_by_user_to_check():
        return "Connexion réussie"
    else:
        return "Connexion échouée"