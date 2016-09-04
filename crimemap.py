# Flask imports
from flask import Flask
from flask import request
from flask import render_template

# Db imports
from dbhelper import DBHelper

# Flask app instance
app = Flask(__name__)
# DB helper instance
DB = DBHelper()

# Home page
@app.route("/")
def home():
 try:
     data = DB.get_all_inputs()
 except Exception as e:
     print e
     data = None
 return render_template("home.html", data=data)

# Add a Crime report
@app.route("/add", methods=["POST"])
def add():
 try:
     data = request.form.get("userinput")
     DB.add_input(data)
 except Exception as e:
     print e
 return home()

@app.route("/clear")
# Clear all data
def clear():
 try:
     DB.clear_all()
 except Exception as e:
     print e
 return home()

if __name__ == '__main__':
 app.run(port=5000, debug=True)
