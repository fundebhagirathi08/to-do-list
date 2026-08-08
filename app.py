from flask import Flask ,render_template

app =Flask(__name__)

todos = [
    {"id": 1, "task": "Learn Flask","desc":"this is first task", "status": "pending"}]
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True ,port=8000)

