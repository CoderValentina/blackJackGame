# Author: Megan Morales
# Date: 5/2/24
import random
#from replit import clear
import os
from art import logo

############### Blackjack House Rules for this Game #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## The following list are the deck of cards: [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.

# Initialize the scores for both players
user_score = -1
computer_score = -1

def deal_card():
  '''Returns a random card from the deck'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card


def calculate_score(cards):
  if sum(cards) == 21 and len(cards) == 2: 
    return 0  #0 = Blackjack

  # Check for an 11 (Ace). If the score is already over 21, remove the 11 and replace it with a 1 because the Ace can be a 1 as well
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  
  return sum(cards)

def compare(user_score, computer_score):
  '''Compares the scores of the user and computer and returns the winner'''
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack 😒"
  elif user_score == 0:
    return "Win with a Blackjack 🥳"
  elif user_score > 21:
    return "You went over. You lose 😤"
  elif computer_score > 21:
    return "Opponent went over. You win 🥳"
  elif user_score > computer_score:
    return "You win 😊"
  else:
    return "You lose 😖"

def play_game():
  print(logo)

  user_cards = []
  computer_cards = []
  is_game_over = False

  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f"\nYour cards: \t\t{user_cards} = {user_score}")
    print(f"Computer's 1st card: \t {computer_cards[0]}")
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      # If the player has Blackjack or they went over, end the game
      is_game_over = True
    else:
      # Ask the user if they want to draw another card, keep asking until they say no
      user_should_deal = input("\nType 'y' to get another card, type 'n' to pass:")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True

  # Once the user is done, let computer keep drawing cards until they reach 17 or more.
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)

  # Show the final score
  print(f"\nYour final hand: \t{user_cards} = {user_score}")
  print(f"\nComputer's final hand: \t{computer_cards} = {computer_score}")

  final_score = compare(user_score, computer_score)
  print(f"\n{final_score}")

  # See if the user wants to play again. If so, clear the console and start again
  while input(
      "\n\nDo you want to play a new game of Blackjack? Type 'y' or 'n': ") == "y":
    os.system('cls')
    play_game()

def main():
  play_game()

if __name__ == "__main__":
  main()