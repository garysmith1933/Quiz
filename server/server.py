from flask import Flask
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="garysmith1933",
  passwd="root",
  database="questions"
)

mycursor = db.cursor()

app = Flask(__name__)

@app.route("/questions")
def get_questions():
  # get questions from database 
  pass

if __name__ == "__main__":
  app.run(debug=True, port=8080)