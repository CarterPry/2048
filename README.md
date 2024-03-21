# 2048 Game in Python

This is a Python implementation of the popular game 2048, where the player slides tiles to combine numbers and add the tiles all the way to 2048. This implementation uses the Flask web framework to create a user-friendly interface that can be easily navigated and interacted with.
Installation

To run this game, you need to have Python 3 and Flask installed on your computer. If you don't have Flask installed, you can follow the instructions in this [guide](https://phoenixnap.com/kb/install-flask) to install it.
How to Play

<p align="center">
  <img src="https://camo.githubusercontent.com/14395f3871b0714bcc86674acf940a60bd80b8b4bc26cfd3f6bb5fd4f5a1cfb9/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f332f33632f466c61736b5f6c6f676f2e7376672f3132303070782d466c61736b5f6c6f676f2e7376672e706e67" alt="Flask" width="400" height="200" />
</p>


To start the game, run the following command in your terminal:

flask run

Then, open your web browser and go to http://127.0.0.1:5000/. You should see the game board with a grid of tiles. Use the arrow keys on your keyboard to move the tiles in the desired direction. The goal is to combine tiles with the same number to create a tile with a larger number, and ultimately reach the tile with the number 2048.
Implementation Details

The game is implemented in Python and uses the Flask web framework to handle the user inputs, update the game state, and update the grid in the HTML table. The numbers on the tiles are represented as text in the HTML table, and are updated dynamically as the player moves the tiles.

One of the challenges in implementing this game for the web was to create a smooth animation when the tiles move and combine. At the moment, the tiles simply appear and disappear instantly when they are combined. This is an area that could be improved in future versions of the game.

In summary, this project demonstrates the power of combining Flask, HTML, JavaScript, and CSS to create a web-based game. The JavaScript and CSS code was included directly in the HTML file for simplicity, although it would be better practice to separate them into separate files. Overall, this project was a fun exercise in exploring the possibilities of running Python code on the web.
