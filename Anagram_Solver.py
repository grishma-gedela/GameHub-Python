
from itertools import permutations

ass = """⟦A⟧⟦N⟧⟦A⟧⟦G⟧⟦R⟧⟦A⟧⟦M⟧ ⟦S⟧⟦O⟧⟦L⟧⟦V⟧⟦E⟧⟦R⟧"""

class AnagramSolver:
    def __init__(self, dictionary_file_path):
        self.dictionary = self.load_dictionary(dictionary_file_path)

    def load_dictionary(self, file_path):
        try:
            with open(file_path, 'r') as file:
                return set(word.strip().lower() for word in file)
        except FileNotFoundError:
            print(f"Error: Dictionary file '{file_path}' not found.")
            exit()
        except Exception as e:
            print(f"Error loading dictionary: {e}")
            exit()

    def get_anagrams_from_user_input(self):
        while True:
            print(f"\n\n----------------- {ass} -----------------")
            
            # Input validation for a valid word
            user_input = input(" \n\nEnter a word: ").strip().lower()
            if not user_input.isalpha():
                print("\n\nInvalid input! Please enter a valid word.")
                continue

            anagrams = self.get_anagrams(user_input)

            if anagrams:
                print("\nAnagrams found:")
                # Display the first 10 anagrams or all if there are fewer than 10
                for anagram in anagrams[:10]:
                    print(anagram)

                # Display a message if there are more anagrams
                if len(anagrams) > 10:
                    print(f"({len(anagrams) - 10} more anagrams not displayed)")
            else:
                print("\nNo anagrams found.")

            play_again = input("\n\nDo you want to play again? (yes/no): ")
            if play_again.lower() != 'yes':
                print("Returning to the Game Hub.")
                break

    def get_anagrams(self, word):
        word = word.lower()
        valid_permutations = filter(lambda p: p in self.dictionary, (''.join(p) for p in permutations(word)))
        return list(valid_permutations)

if __name__ == "__main__":
    dictionary_file_path = 'word_dictionary.txt'
    anagram_solver = AnagramSolver(dictionary_file_path)
    anagram_solver.get_anagrams_from_user_input()
