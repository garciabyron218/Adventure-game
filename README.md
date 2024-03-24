# Adventure-game
# Byron Garcia
# 3/24/24
Newest Version of the game is hosted on github
The game is in English, written in python. Pycharm was used as the IDE
The game is a simple text based adventure game, no min system requirements

Current games is broken into 5 chapters. There is also a Character modnule, and a main file used to run the game

Open the Maingame.py file and run it, the file will call upon the chapter and characters files and open them within. 
The Main file importst a player with stats. The Main file will when open chapter 1 module and import that character through the function. That way any level changes are carried through the chapters.
The game uses a simple leveling system, mostly as a gate check system. 
Most of the actions are functions which are called based on the deicion the player makes. Once the the whole program returns back True, the Chapter ends, making the Main file continue to the next chapter. 
