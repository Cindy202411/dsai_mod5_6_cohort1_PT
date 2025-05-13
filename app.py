#gemini
from flask import Flask,request,render_template

app = Flask(__name__)

@app.route("/",method=["GET","POST"])
def index():
    return(render_template("index.html"))
if_name_=="_main_":
    app.run()