import random
Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---._(___)

'''

Paper = '''
    ______
---'   ___)_____
          ______)
          _______)
         _______)
---._________)

'''

Scissors = '''
    ______
---'   ___)_____
          ______)
       __________)
      (____)
---.__(___)

'''
rps_logo= '''⦏R̂⦎⦏ô⦎⦏ĉ⦎⦏k̂⦎ ⦏P̂⦎⦏â⦎⦏p̂⦎⦏ê⦎⦏r̂⦎ ⦏Ŝ⦎⦏ĉ⦎⦏î⦎⦏ŝ⦎⦏ŝ⦎⦏ô⦎⦏r̂⦎⦏ŝ⦎'''
class Rps_game:
    def __init__(self):
        self.choices=[Rock,Paper,Scissors]

    def get_user_input(self):
        while True:
            try:
                print(f'\n\n    --------------{rps_logo} --------------')
                user_input=int(input("\n\n 0 for Rock \n 1 for Paper \n 2 for Scissors \n\n Choose your Option(0/1/2):"))
                if 0 <= user_input <=2:
                    return user_input
                else:
                    print("Invalid input ! Enter 0/1/2 ")
            except ValueError:
                print(" Invalid input! Please Enter a Number :")
    def play_game(self,user):
        print('\n You Choose         :',user, self.choices[user])
        com=random.randint(0,len(self.choices)-1)
        print("\n Computer choose    : ",com,self.choices[com])
        if com == user:
            print('\n\n \tIT IS A DRAW')
        elif (user == 0 and com == 2) or (user == 1 and com == 0) or (user == 2 and com == 1):
            print("\n    CONGRATS\nYOU WON THE MATCH")
        else:
            print("\n\t SORRY \n  YOU LOSE THE MATCH")
    def start_game(self):
        while True:
            user=self.get_user_input()
            self.play_game(user)
            play_again = input("\n\n Do you want to play again? (Y/N): ").lower()
            if play_again != 'y':
                print("\n Thank you for playing...!   I hope you enjoyed the game.")
                break

if __name__ == "__main__":
    game=Rps_game()
    game.start_game()



























        
