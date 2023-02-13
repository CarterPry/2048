from flask import Flask, render_template
import random
app = Flask(__name__)

griddy = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

def left(griddy):
    for row in range(4):
        empty = [i for i in range(4) if griddy[row][i] == 0]
        non_empty = [i for i in range(4) if griddy[row][i] != 0]
        griddy[row] = [griddy[row][i] for i in non_empty] + [0 for i in empty]
        for i in range(3):
            if griddy[row][i] == griddy[row][i + 1]:
                griddy[row][i] *= 2
                griddy[row][i + 1] = 0
        empty = [i for i in range(4) if griddy[row][i] == 0]
        non_empty = [i for i in range(4) if griddy[row][i] != 0]
        griddy[row] = [griddy[row][i] for i in non_empty] + [0 for i in empty]
    return griddy



def right(griddy):
    for row in range(4):
        empty = [i for i in range(4) if griddy[row][3 - i] == 0]
        non_empty = [i for i in range(4) if griddy[row][3 - i] != 0]
        griddy[row] = [0 for i in empty] + [griddy[row][3 - i] for i in non_empty]
        for i in range(3, 0, -1):
            if griddy[row][i] == griddy[row][i - 1]:
                griddy[row][i] *= 2
                griddy[row][i - 1] = 0
        empty = [i for i in range(4) if griddy[row][3 - i] == 0]
        non_empty = [i for i in range(4) if griddy[row][3 - i] != 0]
        griddy[row] = [0 for i in empty] + [griddy[row][3 - i] for i in non_empty]
    return griddy



def up(griddy):
    griddy = [[griddy[j][i] for j in range(4)] for i in range(4)]
    griddy = left(griddy)
    griddy = [[griddy[j][i] for j in range(4)] for i in range(4)]
    return griddy



def down(griddy):
    griddy = [[griddy[j][i] for j in range(4)] for i in range(4)]
    griddy = right(griddy)
    griddy = [[griddy[j][i] for j in range(4)] for i in range(4)]
    return griddy



@app.route('/')
def index():
    global griddy
    griddy = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    pop_up()
    return render_template('index.html', griddy=griddy)



@app.route('/move/<direction>')
def move(direction):
    global griddy
    if direction == 'left':
        pop_up()
        griddy = left(griddy)
    elif direction == 'right':
        pop_up()
        griddy = right(griddy)
    elif direction == 'up':
        pop_up()
        griddy = up(griddy)
    elif direction == 'down':
        pop_up()
        griddy = down(griddy)
        pop_up()
    return render_template('index.html', griddy = griddy)



@app.route('/random')
def pop_up():
    global griddy
    empty_locations = [(i, j) for i in range(4) for j in range(4) if griddy[i][j] == 0]
    if len(empty_locations) == 0:
        return
    elif len(empty_locations) == 1:
        i, j = empty_locations[0]
        griddy[i][j] = 2 if random.random() < 0.9 else 4
    else:
        random_location1, random_location2 = random.sample(empty_locations, 2)
        i1, j1 = random_location1
        i2, j2 = random_location2
        griddy[i1][j1] = 2
        griddy[i2][j2] = 2
    return render_template('index.html', griddy=griddy)

    
