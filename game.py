import random
import statistics
import time

high_score = None
user_guesses = []


def game_welcome():
    print(f'''
          \r**** Welcome to the Number Guessing Game ****
          \n*********************************************
          ''')
    if type(high_score) == int:
        print(f"Can you beat the highschore of {high_score}?\n")
    else:
        print("Good luck, Challenger\n")


def create_number():
    return random.randint(1, 5)


def user_guess(winning_number):
    false_guess = True
    while false_guess:
        try:
            user_guess = int(input("Guess a number from 1-5(testing):  "))
        except ValueError:
            print("Please enter a whole number.")
        else:
            if user_guess > 100 or user_guess < 1:
                print("Sorry you guessed a number outside the range, try again.")
            elif user_guess > winning_number:
                print(f"Your guess of {user_guess} is higher than the winning number. Try again.")
                user_guesses.append(user_guess)
            elif user_guess < winning_number:
                print(f"Your guess of {user_guess} is lower than the winning number. Try again.")
                user_guesses.append(user_guess)
            else:
                false_guess = False
                print(f"You guessed the correct number it was {winning_number}")
                user_guesses.append(user_guess)


def set_highscore(high_score):
    if high_score == None:
        print(f"Congrats you scored a {len(user_guesses)}, it is now the highscore. Try and beat it!")
        return len(user_guesses)
    elif high_score < len(user_guesses):
        print(f"Congrats you have the new highscore of {len(user_guesses)}")
        return len(user_guesses)
    elif high_score == len(user_guesses):
        print(f"You scored {high_score} and tied the highscore. Try again to beat it! ")
        return high_score
    else:
        print(f"Your score of {len(user_guesses)} did not beat the highscore of {high_score}. Try again!")
        return high_score


def view_data():
    game_guess_count = len(user_guesses)
    game_mean = statistics.mean(user_guesses)
    game_median = statistics.median(user_guesses)
    game_mode = statistics.mode(user_guesses)
    
    print(f'Guesses Count: {game_guess_count}\nMean: {game_mean}\nMedian: {game_median}\nMode: {game_mode}')


def play_again():
    error_check = True
    while error_check:
        print("Thank you for playing")
        user_input = input("Would you like to play again?[Y/N]  ")
        if user_input[0].upper() == "Y":
            error_check = False
            start_game()
        elif user_input[0].upper() == "N":
            error_check = False
            exit()
        else:
            print("You entered an incorrect choice, try again.")


def start_game():
    game_welcome()
    winning_number = create_number()
    user_guess(winning_number)
    time.sleep(1)
    set_highscore(high_score)
    time.sleep(1)
    view_data()
    play_again()
    
    
if __name__ == "__main__":
    start_game()
    pass