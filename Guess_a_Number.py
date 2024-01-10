import random
gtn="""⟦G⟧⟦U⟧⟦E⟧⟦S⟧⟦S⟧ ⟦T⟧⟦H⟧⟦E⟧ ⟦N⟧⟦U⟧⟦M⟧⟦B⟧⟦E⟧⟦R⟧"""

class GuessTheNumber:
    def __init__(self, level):
        self.secret_number = random.randint(1, 50)
        self.attempts = 10 if level == 'easy' else 5

    def start_game(self):
        print(f"\n\n-------------------{gtn}-------------------")
        print("\nLet me think of a number between 1 to 50 : ")

        while self.attempts > 0:
            print(f"\nYou have {self.attempts} attempts remaining to guess a number")
            
            # Get the user's guess
            try :
                user_guess = int(input("Have a guess : "))
                if 1 <= user_guess <= 50:
                # Check if the guess is correct
                    if user_guess == self.secret_number:
                        print("Congrats! You guessed the number.")
                        break
                    elif user_guess < self.secret_number:
                        print("Your guess is too low.")
                    else:
                        print("Your guess is too high.")
    
                    self.attempts -= 1
                else:
                    print("Invalid input! Please enter a number between 1 and 50.")
            except ValueError:
                    print("Invalid input! Please enter a valid number.")   

        if self.attempts == 0:
            print(f"\nSorry, you ran out of attempts. The correct number was {self.secret_number}.")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            self.reset_game()
            self.start_game()
        else:
            print("Thank you for playing Guess the Number!")


if __name__ == "__main__":
    level_choice = input("\n\nChoose level... Type 'easy' or 'hard' : ").lower()
    game = GuessTheNumber(level=level_choice)
    game.start_game()

    
