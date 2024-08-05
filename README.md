# Console Roulette Game

Welcome to the Console Roulette Game! This is a fun, console-based simulation of a classic roulette game where players can place bets on color and parity. Watch the roulette wheel spin and see where the ball lands!

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [File Format](#file-format)
- [Adding New Players](#adding-new-players)
- [Customization](#Customization)

## Features

- **Color Bets**: Bet on red or black.
- **Parity Bets**: Bet on odd or even numbers.
- **Range Bets**: Bet on 1-12, 13-24, 25-36, 1-18, 19-36
- **Customizable Animated Wheel**: Watch a simulated indicator move around the linear wheel and land on a number.
- **Persistent Player Data**: Player data is stored in a text file, tracking their balance.
- **Insta Press Menus**: The menus are insta pressable, meaning the user only needs to press the number on their keyboard to go instantly into the menu. 

## Setup

1. Ensure you have python3 installed on your system

2. download 'main.py' and create a 'roulette_users.txt' with names and balances (each on a new line) formatted like this
```
   Name,30
   John,156
   ```
3. Then run ```main.py```

4. The name you enter to the question 'Who is betting' is case-insensative to the text file
   Then once everyone has gone through and placed their bets
   type 'done' inside the "Who is betting?" question

## File Format

The roulette_users.txt file stores player information. Ensure it follows the format:

```
Name,Amount
```
Each player’s name and balance should be on a new line.
Do **not** put commas in players' names or balances.
Balances should be fully integer. No floats or commas

## Adding New Players
To add new players:

Open 'roulette_users.txt'.
Add a new line with the player's name and their starting balance in the following format:
```
NewPlayerName,StartingBalance
```
Example:
```
Chris,125
```

## Customization

In the 'main.py' file at the bottom, there are variables listed out names, values, and descriptions
There you can copy the name of a variable -> do CNTR + F (or CMD + F) to then search for the variable
Find where it is initialized and change the value there. 
**Read The Descriptions Carefully** 
