import game_mechanics
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")

@app.route("/training_game")
def training_game():
    return render_template("training_game.html")

@app.route("/handle_click", methods=["POST"])
def handle_click():
    data = request.get_json()
    row = data.get("row")
    column = data.get("column")
    print(f"Received click at Row: {row}, Column: {column}")

    return jsonify({"status": "success", "row":row, "column":column})

if __name__ == "__main__":
    app.run(debug=True)

