from flask import Flask
app = Flask(__name__)
# * since we are using session
app.secret_key = "shhh"