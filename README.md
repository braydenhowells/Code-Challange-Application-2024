# Coding-Challenge-2024
Notes: I used the full 4 hours for this challenge. I started by brainstorming the type of program I wanted to make, whether it should be recursive or function-based. I thought functions would be easier, so I outlined some ideas on paper for how the functions would flow. 

About an hour in I decided that I wanted to make sure and validate the user prompts to make sure they didn’t break the program, so I wrote a validate function that I used in several places.

I wrote the beginning and end of the tic tac toe experience first, and made sure that I could start and end games properly. After that, I worked on the grid display, and wrote the player turn function to edit the display. 

I then made a delete function that would remove any opportunity to select a move on the grid that was already taken by either yourself or the opponent. After testing that to satisfaction, I used random to have the computer play against the user. It worked really well on the first try so that was great. 

Next I made sure that all of the possible game-ending scenarios were checked after each move, with a results screen to follow. At this point, my game would ask to play again, and I was finished with the basic program. 

For extra features, I gave the program a bit of personality, and also chose to keep an overall score counter to keep track of the user’s wins and losses. With 30 minutes left I tried to add a two player mode instead of just facing a computer opponent. I tried to add another game mode in the startup process, which resulted in a ‘game_mode’ parameter being added to almost every function. I ended up scrapping this due to time. My original plan was not designed for two players and I kept breaking the one player functions to have two player functions. I deleted this and stuck with my original game. 

I learned that designing certain features is something that should be planned in advance, as my core functions weren’t easily adapted to my new ideas. I also learned that making a copy file to tinker with is better than changing your completed project. I think debugging this was fun! 
