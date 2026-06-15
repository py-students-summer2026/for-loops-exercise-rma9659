"""
This file contains an incomplete function definition.  
Your task is to complete the incomplete function definition. so that it behaves as indicated in the documentation.

Do not run this file directly.
Rather, call this function from main.py and run that file.
"""


def guess_number(low, high, num_attempts):
    number = random.randint(low, high)  # generate a pseudo-random integer in the given range, inclusive
    print(f"I'm thinking of a number between {low} and {high}.")
    print(f"You have {num_attempts} attempts to guess the number.")
    for attempt in range(num_attempts):
        guess = input("Enter your guess: ")
        try:
            guess = int(guess)  # try to convert the guess to an integer
        except ValueError:
            print("That's not a valid number. Try again.")
            continue  # skip the rest of the loop and go to the next iteration

        if guess == number:
            print("Congratulations! You guessed the number!")
            return True  # exit the function immediately if the user guesses correctly
        else:
            print("That's not correct. Try again.")
    print(f"Sorry, you've used all your attempts. The number was {number}.")
    return False  # return False if the user fails to guess the number within the given attempts

    """
    This function, named 'guess_number', generates a psudo-random integer in a given range, inclusive.
    The user is given a certain number of attempts to guess the correct number.
    The function prints the range to the user and informs the user of how many attempts they have.
    The function asks the user to guess the number the given number of times.
    You must use the random module's randint function to generate the pseudo-random integer.
    You must use a for loop to give the user multiple attempts.
    If the user enters a non-numeric response, the program must not crash, but simply count that as an incorrect answer.
    If the user guesses any attempt correctly, the function immediately exits the loop and returns True.
    If the user enters all attempts incorrectly, the function returns False.

    :param low: The low end of the range in which the pseudo-random number is generated.
    :param high: the high end of the range in which the pseudo-random number is generated.
    :param num_attempts: The number of attempts the user is given to guess the correct number.
    :returns: True if the user answers any attempt correctly, False otherwise.
    """
