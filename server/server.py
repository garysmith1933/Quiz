from flask import Flask

app = Flask(__name__)

@app.route("/questions")
def get_questions():
  # get questions from database 
  pass

if __name__ == "__main__":
  app.run(debug=True, port=8080)