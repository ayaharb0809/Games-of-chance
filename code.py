import random

money = 100

#Write your game of chance functions here
def coinflip(guess, bid):
  heads = 1
  tails = 2
  num = random.randint(heads, tails)
  if num == guess:
    return (bid + 5)
  else:
    return (0-bid)

def even_num(dice):
  if (dice%2) == 0:
    return even
def odd_num(dice):
  if (dice%2) != 0:
    return odd

even = even_num
odd = odd_num

def chohan(guess, bid):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)
  result = dice1 + dice2
  if (guess == even) and (result == even):
    return (bid + 5)
  elif (guess == odd) and (result == odd):
    return (bid + 5)
  elif (guess == odd) and (result == even):
    return (0 - bid)
  else:
    return (0 - bid)
def cards(bid):
  player1 = random.randint(1, 13)
  player2 = random.randint(1, 13)
  if player1 > player2:
    return (bid + 5)
  else:
    return (0 - bid)
  
def roulette(guess, bid):
  result = random.randint(1, 35)
  if (guess == even) and (result == even):
    return (bid + 5)
  elif (guess == odd) and (result == odd):
    return (bid + 5)
  elif (guess == odd) and (result == even):
    return (0 - bid)
  elif (guess == int) and (result == guess):
    return (result + bid)
  elif (guess == int) and (result != guess):
    return (0 - bid)
  else:
    return (0 - bid)
#Call your game of chance functions here
money += coinflip(220, 2)
print("You have " + str(money) + " after the coin flip.")
money += chohan(even, 100)    
print("You have " + str(money) + " after cho han.")
money += cards (60)
print("You have " + str(money) + " after picking a card.")
money += roulette(even, 50)
print("You have " + str(money) + " after playing roulette.")
