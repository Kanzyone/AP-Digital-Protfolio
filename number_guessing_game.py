import random

# This code was developed by the student with AI-assisted debugging and refinement.


def analyze_guess(current_guess, secret_number, guess_history):
    """
    Analyzes the player's guess using sequencing, selection, and iteration.
    Parameters:
        current_guess (int): User's current guess
        secret_number (int): Random target number
        guess_history (list): List of all guesses
    Returns:
        str: Result message
    """

    # Iteration through guess history to calculate total attempts
    attempt_count = 0
    for guess in guess_history:
        attempt_count += 1

    # Selection logic
    if current_guess > secret_number:
        return f"Too high! Attempts so far: {attempt_count}"
    elif current_guess < secret_number:
        return f"Too low! Attempts so far: {attempt_count}"
    else:
        return f"Correct! You guessed it in {attempt_count} attempts."


# Main game loop
play_again = True

while play_again:
    secret_number = random.randint(1, 100)
    guesses = []
    guessed_correctly = False

    print("\nWelcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    while not guessed_correctly:
        try:
            user_guess = int(input("Enter your guess: "))

            # Input validation
            if user_guess < 1 or user_guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            # Store guess in list
            guesses.append(user_guess)

            # Call student-developed procedure
            result = analyze_guess(user_guess, secret_number, guesses)
            print(result)

            # End game if correct
            if user_guess == secret_number:
                guessed_correctly = True

        except ValueError:
            print("Invalid input. Please enter a whole number.")

    # Output full guess history
    print("Your guesses were:", guesses)

    # Additional list usage to manage complexity
    print("Highest guess:", max(guesses))
    print("Lowest guess:", min(guesses))
    print("Average guess:", round(sum(guesses) / len(guesses), 2))

    # Replay option
    replay = input("Would you like to play again? (yes/no): ").lower()

    if replay != "yes":
        play_again = False
        print("Thanks for playing!")