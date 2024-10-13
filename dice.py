import random
def roll_dice():
  """Rolls a six-sided dice and returns the result."""
  return random.randint(1, 6)
# Get the user's input for the number of rolls
num_rolls = int(input("How many times do you want to roll the dice? "))
# Roll the dice the specified number of times
for _ in range(num_rolls):
  roll = roll_dice()
  print("You rolled a", roll)