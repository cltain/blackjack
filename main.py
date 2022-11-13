import random
from art import logo
from replit import clear

def get_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calc_score(cards):
  sums = sum(cards)
  if 11 in cards and sums > 21:
    cards.remove(11)
    cards.append(1)
  if sum == 21 and len(cards) == 2:
    return 0
  else:
    return sums
    
def compare(score1, score2):
  if score1 == score2:
    print("Draw")
  elif score1 == 21:
    print("You win! :D")
  elif score2 == 21:
    print(f"Dealer wins. Dealers score: {score2} :(")
  elif score1 > 21:
    print("You lose!!! Went over 21.")
  else:
    if score1 > score2:
      print(f"You win! Your score was {score1} and the dealer's score was {score2}")
    elif score2 > score1:
      print(f"Dealer wins!!! Dealer's score: {score2}")
answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

def blackjack():
  is_game_over = False
  print(logo)
  user_cards = []
  dealer_cards = []
  for _ in range(2):
    user_cards.append(get_card())
    dealer_cards.append(get_card())
  while not is_game_over:
    user_score = calc_score(user_cards)
    dealer_score = calc_score(dealer_cards)
      
    print(f"Your cards: {user_cards}, current score = {user_score}\nComputer's first card: {dealer_cards[0]}")
    if user_score == 0 or dealer_score == 0 or user_score > 21:
        is_game_over = True
    else:
      user_deals = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_deals == 'y':
        user_cards.append(get_card())
      else:
        is_game_over = True
  while dealer_score != 0 and dealer_score < 17:
    dealer_cards.append(get_card())
    dealer_score = calc_score(dealer_cards)
  
  compare(score1 = user_score, score2 = dealer_score)
  again = input("Type 'y' to play again, type 'n' to leave: ")
  if again == 'y':
    clear()
    blackjack()
  else:
    print("bye bye")
if answer == 'y':
  blackjack()
elif answer == 'n':
  print("bye bye")
