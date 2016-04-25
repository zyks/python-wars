## python-wars

Python-wars is a simple, multiplatform, online multiplayer game written in python3 and pygame library. It is a modification of popular Snake game, except that there are many snakes on the game board and they can fight with each other.
#### Screenschots
![Gameplay](media/gameplay0.png?raw=true  "Gameplay with two players")
### Rules
* Player can bite off one's tail fragment when it's shorter than the player's total length.
* The fragment's length is a number of segments between the bitten one and the snake end.
* It is possible to eat whole snake.
* Eating opponent's tail's fragment increases player's length by length of that fragment.
* Power-ups spawns randomly and one can be taken by only one player.
* Player loses when he the hits wall or is eaten by another player.
* Player wins when other players lost, or when he reaches a length of 20 segments.

### Power-ups
* ![Apple](media/apple.png?raw=true  "") Apple - increases player's length by 1 
* ![Apple](media/rotten_apple.png?raw=true  "") Wormy apple - decreases player's length by 1

### Running the game
First run `python_wars.py` in server mode (use `-h` or `--help` argument for help). `-p` specifies the players number. Example:  
```sh
$ python3 python_wars.py server -p 2
```  
Then to connect player, run `python_wars.py` in client mode and use `--port` argument to set player's port. You can also use `-n` argument to specify a player's name. Example:  
```sh
$ python3 python_wars.py client -n Alfred --port 40001
```

### Gameplay
Use keyboard to control your snake.  
<kbd>◀</kbd> - turn left  
<kbd>▶</kbd> - turn right  
<kbd>▲</kbd> - turn up  
<kbd>▼</kbd> - turn down  
Fight your opponents, gather power-ups and have fun!  


