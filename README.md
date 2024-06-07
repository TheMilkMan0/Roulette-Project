# Console Roulette Game

Welcome to the Console Roulette Game! This is a fun, console-based simulation of a classic roulette game where players can place bets on color and parity. Watch the roulette wheel spin and see where the ball lands!

## Table of Contents

- [Features](#features)
- [Setup](#setup)
- [File Format](#file-format)
- [Adding New Players](#adding-new-players)

## Features

- **Color Bets**: Bet on red or black.
- **Parity Bets**: Bet on odd or even numbers.
- **Animated Wheel**: Watch a simulated indicator move around the wheel and land on a number.
- **Persistent Player Data**: Player data is stored in a text file, tracking their balance.

## Setup

1. download 'main.py' and create a 'roulette_users.py' with names and balances (each on a new line) formated like this
```
   Name,30
   John,156
   ```
2. Then run ```main.py```

3. The name you enter to the question 'Who is betting' is CASE-SENSITIVE to the next file
   Then once everyone is done betting type 'done' inside the "Who is betting?" question

## File Format
The roulette_users.txt file stores player information. Ensure it follows the format:

```
Name,Amount
```
Each player’s name and balance should be on a new line.

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
