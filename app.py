#gemini

from dotenv import load_dotenv
load_dotenv()
from flask import Flask,request,render_template
import google.generativeai as genai
import os

api_key= os.getenv('gemini_key') #load from rander
genai.configure(api_key=os.environ["GEMINI_KEY"]) # load from genai
#genai.configure(api_key="gemini_key")
model = genai.GenerativeModel("gemini-2.0-flash")
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))
@app.route("/gemini",methods=["GET","POST"])
def gemini():
    return(render_template("gemini.html"))
@app.route("/gemini_reply",methods=["GET","POST"])
def gemini_reply():
    q = request.form.get("q")
    print(q)
    r = model.generate_content(q)
    return(render_template("gemini_reply.html",r=r.text))
if __name__ == "__main__":
    app.run()


#gemini

# from flask import Flask, request, render_template
# import google.generativeai as genai
# from openai import OpenAI
# import os

# # Configure Gemini
# # genai.configure(api_key=os.environ["gemini_key"])
# genai.configure(api_key="gemini_key")

# # Configure OpenAI
# client = OpenAI(api_key="gemini_key")

# # Configure Gemini model
# model = genai.GenerativeModel("gemini-2.0-flash")

# # Flask
# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     return(render_template("index.html"))

# @app.route("/gemini",methods=["GET","POST"])
# def gemini():
#     return(render_template("gemini.html"))

# @app.route("/gemini_reply",methods=["GET","POST"])
# def gemini_reply():
#     q = request.form.get("q")
#     print(q)
#     r = model.generate_content(q)
#     r = r.text
#     return(render_template("gemini_reply.html",r=r))

# @app.route("/openai",methods=["GET","POST"])
# def openai():
#     return(render_template("openai.html"))

# @app.route("/openai_reply",methods=["GET","POST"])
# def openai_reply():
#     q = request.form.get("q")
#     response = client.chat.completions.create(
#       model="gpt-4-turbo",
#       messages=[{"role": "user", "content": q}]
#     )
#     r = response.choices[0].message.content
#     return(render_template("openai_reply.html",r=r))

# if __name__ == "__main__":
#     app.run()

# Chatgpt generated
# from dotenv import load_dotenv
# load_dotenv()

# from flask import Flask, request, render_template
# import google.generativeai as genai
# import os

# # Safely fetch Gemini API key
# api_key = os.getenv("gemini_key")
# if not api_key:
#     raise ValueError("Gemini API key not found in environment variables.")
# genai.configure(api_key=api_key)

# # Load Gemini model
# model = genai.GenerativeModel("gemini-2.0-flash")

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def index():
#     return render_template("index.html")

# @app.route("/gemini", methods=["GET", "POST"])
# def gemini():
#     return render_template("gemini.html")

# @app.route("/gemini_reply", methods=["GET", "POST"])
# def gemini_reply():
#     q = request.form.get("q")
#     print("User question:", q)
#     r = model.generate_content(q)
#     return render_template("gemini_reply.html", r=r.text)

# if __name__ == "__main__":
#     app.run()
