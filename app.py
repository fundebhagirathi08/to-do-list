from flask import Flask ,render_template

app =Flask(__name__)

todos = [
    {"id": 1, "task": "Learn Flask",
     "desc":"this is sample task for todo list", "date_created":"08-08-26", "status":"pending"}
     ]
@app.route("/")
def home():
    return render_template("index.html",allTodos =todos)

if __name__ == "__main__":
    app.run(debug=True ,port=8000)

