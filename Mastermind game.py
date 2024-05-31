import random

def mastermind_game():
  """
  A simple implementation of the Mastermind game.

  This version uses numbers instead of colors.
  """

  # Set the number of digits in the code
  num_digits = 4

  # Generate the secret code
  secret_code = [random.randint(1, 9) for _ in range(num_digits)]

  # Initialize the number of guesses
  guesses_left = 10

  print("Welcome to Mastermind!")
  print(f"I have generated a {num_digits}-digit code with numbers between 1 and 9.")

  # Game loop
  while guesses_left > 0:
    print(f"You have {guesses_left} guesses left.")

    # Get the player's guess
    guess = input("Enter your guess (e.g., 1234): ")

    # Validate the guess
    if len(guess) != num_digits or not guess.isdigit():
      print("Invalid guess. Please enter a valid {num_digits}-digit number.")
      continue

    # Convert the guess to a list of digits
    guess = [int(digit) for digit in guess]

    # Evaluate the guess
    correct_digits = sum(1 for i in range(num_digits) if guess[i] == secret_code[i])
    correct_positions = sum(1 for i in range(num_digits) if guess[i] in secret_code)

    print(f"You have {correct_digits} correct digits in the correct positions.")
    print(f"You have {correct_positions} correct digits.")

    # Check if the player won
    if correct_digits == num_digits:
      print("Congratulations, you won!")
      return

    # Update the number of guesses
    guesses_left -= 1

  # Game over
  print(f"You ran out of guesses. The secret code was: {secret_code}")

# Start the game
mastermind_game()