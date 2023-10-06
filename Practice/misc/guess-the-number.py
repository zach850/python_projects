import random 
def game():
    continue_game = True

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    rand_num = random.randint(1,100)
    print(f"Pssst, the correct number answer is {rand_num}")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    def num_attempts(difficulty):
        if difficulty == 'easy':
            attempts = 10
            return attempts
        elif difficulty == 'hard':
            attempts = 5 
            return attempts

    attempts = num_attempts(difficulty)

    while continue_game: 
        print(f"You have {attempts} attempts remaining to guess the number")
        user_guess = int(input("Make a guess: "))

        if user_guess == rand_num:
            continue_game = False
            print("You have successfully guessed the correct number!")
        elif attempts <= 1:
            continue_game = False 
            print("You ran out of guesses. You lose!")
        elif user_guess > rand_num:
            print("Too high.")
            print("Guess again.")
            attempts -= 1
        elif user_guess < rand_num:
            print("Too low.")
            print("Guess again.")
            attempts -= 1

game()
    
