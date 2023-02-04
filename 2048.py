from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    game_grid = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    move = request.form.get("move")

    if request.method == "POST":
        if move == "up":
            game_grid = move_up(game_grid)
        elif move == "down":
            game_grid = move_down(game_grid)
        elif move == "left":
            game_grid = move_left(game_grid)
        elif move == "right":
            game_grid = move_right(game_grid)

        # add a new value to the grid after each move
        empty_cells = [i for i, x in enumerate(game_grid) if x == 0]
        if empty_cells:
            index = random.choice(empty_cells)
            game_grid[index] = 2

    return render_template("2048.html", game_grid=game_grid)

def move_up(grid):
    new_grid = [0] * 16
    for col in range(4):
        current_col = [grid[row * 4 + col] for row in range(4)]
        current_col = merge_values(current_col)
        for row in range(4):
            new_grid[row * 4 + col] = current_col[row]
    return new_grid

def move_down(grid):
    new_grid = [0] * 16
    for col in range(4):
        current_col = [grid[row * 4 + col] for row in range(3, -1, -1)]
        current_col = merge_values(current_col)
        for row in range(4):
            new_grid[(3 - row) * 4 + col] = current_col[row]
    return new_grid

def move_left(grid):
    new_grid = [0] * 16
    for row in range(4):
        current_row = grid[row * 4 : row * 4 + 4]
        current_row = merge_values(current_row)
        new_grid[row * 4 : row * 4 + 4] = current_row
    return new_grid

def move_right(grid):
    new_grid = [0] * 16
    for row in range(4):
        current_row = grid[row * 4 : row * 4 + 4]
        current_row = merge_values(current_row)[::-1]
        new_grid[row * 4 : row * 4 + 4] = current_row[::-1]
    return new_grid

def merge_values(values):
# merge adjacent cells with the same value
i = 0
while i < len(values) - 1:
if values[i] == values[i + 1]:
values[i] *= 2
del values[i + 1]
values.append(0)
i += 1
# move all values to the left
new_values = [x for x in values if x != 0]
new_values += [0] * (len(values) - len(new_values))
return new_values

if name == "main":
 app.run(debug=True)
