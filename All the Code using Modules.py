# Importing necessary modules
#import os
from Hangman_Game import HangmanGame
from Rock_Paper_Scissors import Rps_game
from Guess_a_Number import GuessTheNumber
from GK_Quiz import GeneralKnowledgeQuiz
from Tic_Tac_Toe import TicTacToe
from Anagram_Solver import AnagramSolver

# ASCII art logo for the game hub
logo= """

   ______                                      __    __          __       
  /      \                                    |  \  |  \        |  \      
 |  ▓▓▓▓▓▓\ ______  ______ ____   ______      | ▓▓  | ▓▓__    __| ▓▓____  
 | ▓▓ __\▓▓|      \|      \    \ /      \     | ▓▓__| ▓▓  \  |  \ ▓▓    \ 
 | ▓▓|    \ \▓▓▓▓▓▓\ ▓▓▓▓▓▓\▓▓▓▓\  ▓▓▓▓▓▓\    | ▓▓    ▓▓ ▓▓  | ▓▓ ▓▓▓▓▓▓▓\
                                                              ▓▓ \▓▓▓▓/      ▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓    ▓▓    | ▓▓▓▓▓▓▓▓ ▓▓  | ▓▓ ▓▓  | ▓▓
 | ▓▓__| ▓▓  ▓▓▓▓▓▓▓ ▓▓ | ▓▓ | ▓▓ ▓▓▓▓▓▓▓▓    | ▓▓  | ▓▓ ▓▓__/ ▓▓ ▓▓__/ ▓▓
  \▓▓    ▓▓\▓▓    ▓▓ ▓▓ | ▓▓ | ▓▓\▓▓     \    | ▓▓  | ▓▓\▓▓    ▓▓ ▓▓    ▓▓
   \▓▓▓▓▓▓  \▓▓▓▓▓▓▓\▓▓  \▓▓  \▓▓ \▓▓▓▓▓▓▓     \▓▓   \▓▓ \▓▓▓▓▓▓ \▓▓▓▓▓▓▓ 
                                                                         
                                                                         
                                                                         
          """

font_choose= """                       .-----------------------------.
─────★───── ─────★───| ░▒▓█ 𝐏𝐋𝐀𝐘𝐄𝐑 𝐆𝐀𝐌𝐄 𝐒𝐄𝐋𝐄𝐂𝐓𝐈𝐎𝐍 █▓▒░ | ─────★───── ─────★─
                       '-----------------------------' """

class GameHub:
    def __init__(self):
        # Initializing instances for different games
        self.rps_game = None
        self.guess_the_number = None
        self.general_knowledge_quiz = None
        self.hangman_game = None

        self.tictactoe_game= None
        self.anagram_solver = None

    def start_game_hub(self):
        while True:
            # Displaying the game hub menu
            print(logo)
            print("\n ------------------- ▀▄▀▄▀▄   ⒼⒶⓂⒺ ⒽⓊⒷ    ▄▀▄▀▄▀ -------------------")
            print("\n\n\n ★⋆ 1. ROCK PAPER SCISSORS")
            print("\n ★⋆ 2. GUESS THE NUMBER")
            print("\n ★⋆ 3. GENERAL KNOWLEDGE QUIZ")
            print("\n ★⋆ 4. HANGMAN GAME")
            print("\n ★⋆ 5. TIC TAC TOE")
            print("\n ★⋆ 6. ANAGRAM SOLVER")
            print("\n ★⋆ 7. QUIT\n")
            
            # Prompting user for game choice
            choice = input(f"{font_choose}\n\n\n ➤➤➤➤  Choose a game (1/2/3/4/5/6/7) : ")

            # Handling user choices and initializing game instances
            if choice == '1':
                if self.rps_game is None:
                    self.rps_game = Rps_game()
                self.rps_game.start_game()
            elif choice == '2':
                if self.guess_the_number is None:
                    self.guess_the_number = GuessTheNumber(level='easy')
                self.guess_the_number.start_game()
            elif choice == '3':
                if self.general_knowledge_quiz is None:
                    self.general_knowledge_quiz = GeneralKnowledgeQuiz()
                self.general_knowledge_quiz.play_quiz()
            elif choice == '4':
                if self.hangman_game is None:
                    self.hangman_game = HangmanGame()
                self.hangman_game.play()  # Call the modified play() method
            elif choice == '5':
                if self.tictactoe_game is None:
                    self.tictactoe_game = TicTacToe()
                self.tictactoe_game.play()
            elif choice == '6':
                if self.anagram_solver is None:
                    self.anagram_solver = AnagramSolver('word_dictionary.txt')
                self.anagram_solver.get_anagrams_from_user_input()
            elif choice=='7':
                 print("\n Thank you for playing Game Hub! ")
                 break
            else:
                print("\n Invalid choice! Please enter 1, 2, 3, 4,5 OR 6.")

if __name__ == "__main__":
    game_hub = GameHub()
    game_hub.start_game_hub()


