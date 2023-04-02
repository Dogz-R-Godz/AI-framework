# AI-framework
An AI framework that can let you make a game with a few conditions and it will train an AI to play it.


To make a new game, follow the following steps:
1: Make a file with the name of your game. 
2: You then go to line 8 in main.py, and add your game in. The two numbers in the dict is the inputs for the AI, and the outputs. 
3: You will also need to add your game to line 9 in main.py. These are the inputs from the AI to your game. 
4: Add your file name to the main_importer.py file
5: Import any textures you need into the main.py line 34. 
6: In the run_correct_game function, add your game. The inputs for it are the ones listed for the other two games already implimented. I will be changing it so its easier to impliment all of this later on. 
7: Add your game to the start_new_game function in main.py. Use the same inputs again as run_correct_game. 
8: In your games file, start with "from game_importer import *". This will import all nessassary imports. 
9: Your games file will need to include a run_frame function that takes an input of the same ammount inputs as the run_correct_game function. The function must output 8 variables, 4 of which will be inputted back into the function in the next frame. The third output must be a dictionary called instructions. This dict looks like instructions={"lines":[],"circles":[],"text":[],"rects":[],"tape":[]}. The function will append to these lists in the dict, and when it goes back into the main.py, it will be drawn on the screen. It has to return the inputs for the AI as the 6th returned variable. This one starts at 1, and ends at the amount of inputs you specified. These inputs can be a maximum of 1 and a minimum of 0. The 7th variable must be an alive variable, with True for if the player is alive, and False if its dead. Finally, it must calculate the score as well. This score is crucial in deciding what bots actually pass on their genes. 
10: Have Fun with my AI library. 
11: Change the curr_game variable to a string of your games name.


You also need to do pip install pygame, pip install pickle, and I think you need to do pip install multiprocessing
