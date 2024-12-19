
from flask import Flask, render_template, url_for, request, jsonify

app = Flask(__name__)


GRID_SIZES = {
    "easy": (5,5),
    "medium": (10,10),
    "hard": (15,15)
}

class Cell:
    def __init__(self, mine=False, show=False, score=0, mark=0):
        self.mine = mine
        self.show = show
        self.score = score
        self.mark = mark 

    def __repr__(self):
        return f"Cell({self.mine},{self.show},{self.score},{self.mark})"
    
    def to_dict(self):
        return {"mine": self.mine, "show": self.show, "score": self.score, "mark": self.mark}

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


@app.route("/start_game", methods=["POST"])
def start_game():
    data = request.get_json()
    difficulty = data.get("difficulty", "easy")
    rows, cols = GRID_SIZES.get(difficulty, (5,5))

    grid = [[Cell() for _ in range(cols)] for _ in range (rows)]
    app.config["grid"] = grid

    return jsonify({"rows": rows, "colums": cols})


def update_cell():
    grid = app.config.get("grid", [])
    data = request.get_json()
    row, col =  data.get("row"), data.get("col")

    if 0 <= row < len(grid)and 0 <= col < len(grid[0]):

        cell = grid[row][col]
        cell.show = True
        cell.score += 1

        return jsonify(cell.to_dict())
    else:
        return jsonify({"error": "Invalid cell coordinates"}), 400
    

if __name__ == "__main__":
    app.run(debug=True)

