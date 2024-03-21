# Python 2048 Game

This repository contains a Python implementation of the popular 2048 game. It uses the Flask web framework to create a user-friendly web interface that allows players to slide numbered tiles on a grid to combine them and reach the number 2048.

## Installation

Before you can run the game, ensure you have Python 3.x installed on your system. Additionally, you will need Flask. If Flask is not already installed, you can install it by following the guide provided here: [Install Flask](https://phoenixnap.com/kb/install-flask).

## How to Play

Once the installation is complete, you can start the game with the following command:

```bash
flask run
```

Then just go to your lcoal host at http://127.0.0.1:5000/ in your web browser to begin playing. You'll see a grid of tiles. You use your keyboard's arrow keys to slide the tiles up, down, left, and right. When two tiles with the same number touch, they'll merge into one combining their value. Your goal is to create a tile with the value 2048.

<p align="center">
  <img src="https://camo.githubusercontent.com/14395f3871b0714bcc86674acf940a60bd80b8b4bc26cfd3f6bb5fd4f5a1cfb9/68747470733a2f2f75706c6f61642e77696b696d656469612e6f72672f77696b6970656469612f636f6d6d6f6e732f7468756d622f332f33632f466c61736b5f6c6f676f2e7376672f3132303070782d466c61736b5f6c6f676f2e7376672e706e67" alt="Flask" width="200" height="100" />
</p>

## Details
The game logic is handled by Python, while Flask manages dynamic GUI. The front end is a blend of HTML, CSS, and JavaScript to render the game.

## Summary
This project was just to test out web packages such as Flask to make something interactive like the 2048 game. I did put all the html, CSS styling, and JS in the index.html file, but for best practices it is better to separate these files 
Enjoy the game, and feel free to contribute any improvements or new features.
