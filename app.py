import random

# function to guess a randomly generated number within a range
def guess(x):
  random_num = random.randint(1, x)
  guess = 0
  while guess != random_num:
    guess = int(input(f"Guess a number between 1 and {x}: "))
    if guess < random_num:
      print("Try again, too low.")
    elif guess > random_num:
      print("Try again, too high.")
  
  print(f"Congrats, you have guessed the number {x}!")

# guess(10)

# Function to have the computer guess your own secret number
def computer_guess(x):
  low = 1
  high = x
  feedback = ''
  while feedback != 'c':
    if low != high:
      guess = random.randint(low, high)
    else:
      guess = low # could also be high b/c low = high

    feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?').lower()
    if feedback == 'h':
      high = guess - 1
    elif feedback == 'l':
      low = guess + 1
  print(f'Computer has guessed your number, {guess}, correctly!')

computer_guess(20)