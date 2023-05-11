
import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Letterboard
class LetterBoard():
    MAX_MOVES = 7
    WORD_BANK = ("cat", "theology", "pineapple", "phlogiston",
     "mystery", "catastrophe", "wedge", "minutiae", "warehouse", "hangman")

    def __init__(self):
        # Pick the word to be guessed
        self.word = LetterBoard.WORD_BANK[random.randint(0, len(LetterBoard.WORD_BANK)-1)]
        self.guessed_letters = []
        self.number_of_moves = 0

    def show_word(self):
        clear_screen()
        board = ["_ " if letter not in self.guessed_letters else letter for letter in self.word]
        for letter in board:
            print(letter, end="")
        print()            
        print("Guessed Letters: ", end="")
        if self.guessed_letters:    
            for letter in self.guessed_letters:
                print(letter, end=" ")
        else:
            print("You haven't guessed yet", end="")
        print()
        print(f"You have {LetterBoard.MAX_MOVES - self.number_of_moves} moves left")
    
    def guess_letter(self, letter):
        if len(letter)>1 or letter.isdigit():
            print("Invalid Guess, must be a single LETTER!")
            return
        if letter in self.word:
            count = self.word.count(letter)
            print(f"You found {count} {letter}{'s' if count > 1 else ''}")
        else:
            print(f"{letter} is not in the word")
            self.number_of_moves += 1
        self.guessed_letters.append(letter)
        
    def has_guesses_left(self):
        return self.number_of_moves < LetterBoard.MAX_MOVES
    
    def guess_word_correct(self, word):
        return word == self.word

    def check_if_all_letters_guessed(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def user_won(self):
        print("Congrats You solved the Puzzle")

    def user_lost(self):
        print("I am SOOOOOOO Sorry you ARE SOOOOO BAD at his game ....  Why don't You got hang yourself")


# UI
class UI():
    def __init__(self):
        self.letterboard = LetterBoard()
    
    def play_game(self):
        while True:
            # Display the game board to the user
            self.letterboard.show_word()
            
            # Ask for a letter
            letter = input("What letter would you like to guess? ")

            # Respond with whether or not the letter is on the board 
                #(and take a guess away if its not; if it is reveal letter)
            self.letterboard.guess_letter(letter)

            # Display the game board to the user (updated)
            self.letterboard.show_word()
    
            # Check if the answer was solved with the last guess
            if self.letterboard.check_if_all_letters_guessed():
                # User wins
                self.letterboard.user_won()
                break

            # Let Them guess the word
            word_guess = input("Would you like to guess the word (Y/Yes) ").lower()
            if word_guess == 'y' or word_guess == "yes":
                word = input("What is your guess for the word? ").lower()
                if self.letterboard.guess_word_correct(word):
                    # User wins
                    self.letterboard.user_won()
                    break

            # Check if the user has guesses left
            if not self.letterboard.has_guesses_left():
                # YOUR A LOSER!
                self.letterboard.user_lost()
                break

            # Repeat step step until they solved or lost

def main():
    # Driver Code -- Makes stuff happen
    ui = UI()
    ui.play_game()

if __name__ == "__main__":
    main()

