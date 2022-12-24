from flask import Flask,render_template

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
        return render_template('index.html')
@app.route('/name/<username>')
def show_user(username):
    return f"<h3>您的名字是<strong>{username}</strong></h3>"