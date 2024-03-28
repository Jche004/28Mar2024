from flask import Flask, request, render_template
import google.generativeai as palm
palm.configure(api_key="AIzaSyBGBdFfivWDEhKhQP8yU9wu69TyoCD2sEk")
model = { 
    'model': "models/chat-bison-001",
    }

name = ""
flag = 1

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

# 0 means keeps your name 
# 1 means change your name
@app.route("/main",methods=["GET","POST"])
def main():
    global name, flag
    if flag == 1:
        name = request.form.get("q")
        flag = 0
    return(render_template("main.html",r=name))
    
@app.route("/main",methods=["GET","POST"])
def result():
    r = request.form.get("q")
    return(render_template("main.html",r=r))
    
@app.route("/text",methods=["GET","POST"])
def text():
    return(render_template("text.html"))

@app.route("/text_generator",methods=["GET","POST"])
def text_generator():
    q = request.form.get('q')
    r = palm.chat(**model,messages=q)
    return(render_template("text_generator.html", r = r.last))
    
@app.route("/end",methods=["GET","POST"])
def end():
    global flag
    print("ending process......")
    flag = 1
    return(render_template("index.html"))
    
if __name__ == "__main__":
    app.run()
