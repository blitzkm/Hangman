import random

class RandomAnswerProvider:
    def random_valid_word_from_file(self, filename: str) -> str:
        with open(filename, "r") as file:
            word_list = [line.strip() for line in file]
        return random.choice(word_list)

class HangmanModel:
    def __init__(self) -> None:
        provider = RandomAnswerProvider()  # Create an instance
        self.answer: str = provider.random_valid_word_from_file("possible_answers.txt").upper()  # Use method correctly
        self.word_length: int = len(self.answer)
        self.max_guess: int = 5
        # self.correct_guesses: list[str] = list(self.answer)
        self.player_correct_guesses: list[str] = list()
        self.player_incorrect_guesses: list[str] = list()


        if self.max_guess <= 0:
            raise ValueError(f'Out of guesses already')


    def make_guess(self, guess: str) -> None:
        if len(guess) != 1 or not guess.isalpha():
            raise ValueError('Should only be a single letter')

        guess = guess.upper()

        if guess in self.player_correct_guesses or guess in self.player_incorrect_guesses:
            print("You've already guessed that letter!")
            return

        if guess in self.answer:
            self.player_correct_guesses.append(guess)

        else:
            self.player_incorrect_guesses.append(guess)
            self.max_guess -= 1
        

    def is_game_over(self) -> bool:
        return self.max_guess == 0 or set(self.answer) == set(self.player_correct_guesses)



            






        


'''SANITY CHECKS'''
game = HangmanModel()
print(game.answer)  # Should print a random word from the file
print(game.make_guess('i'))
print(game.max_guess)
print(game.player_correct_guesses)
print(game.player_incorrect_guesses)
print(game.make_guess('a'))
print(game.max_guess)
print(game.player_correct_guesses)
print(game.player_incorrect_guesses)
print(game.make_guess('b'))
print(game.max_guess)
print(game.player_correct_guesses)
print(game.player_incorrect_guesses)
print(game.make_guess('k'))
print(game.max_guess)
print(game.player_correct_guesses)
print(game.player_incorrect_guesses)
print(game.is_game_over())
print(game.make_guess('l'))
print(game.max_guess)
print(game.player_correct_guesses)
print(game.player_incorrect_guesses)
print(game.is_game_over())
