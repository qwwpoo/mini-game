import random

def guess_the_number():
    """
    Number Guessing Game: The computer chooses a random number, and the user tries to guess it.
    """
    
    # 1. Define the range from which the computer will choose the number
    lower_bound = 1
    upper_bound = 100
    
    # 2. The computer chooses a random secret number
    secret_number = random.randint(lower_bound, upper_bound)
    
    # 3. Number of guesses taken by the user
    guesses_taken = 0
    
    # Welcome message
    print("Welcome to the Number Guessing Game!") 
    
    # Instructions for the user
    print("I have chosen a secret number between {} and {}. Try to guess it!".format(lower_bound, upper_bound))

    while True:
        try:
            # 4. Request a guess from the user
            user_guess = int(input("Your guess: "))
            guesses_taken += 1

            # 5. Compare the user's guess with the secret number
            if user_guess < secret_number:
                print("Your guess is too low! Try again.")
            elif user_guess > secret_number:
                print("Your guess is too high! Try again.")
            else:
                # Correct guess message
                print("Congratulations! You guessed the number {} successfully in {} tries!".format(secret_number, guesses_taken))
                break # Exit the game after a correct guess

        except ValueError:
            print("Invalid input! Please enter a number.")
        except Exception as e:
            # Error handling message
            print("An error occurred: {}".format(e))

# Run the game
if __name__ == "__main__":
    guess_the_number()