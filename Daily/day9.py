# basic otp generation
# import random

# #Generate 6-digit OTP
# otp = random.randint(100000, 999999)

# print("Your OTP is: ", otp)

###########################################

# import random

# # Generate random number between 1 to 100

# secret_number = random.randint(1, 100)

# print("Welcome to the Number Guessing Game!")

# print("Guess a number between 1 and 100")

# while True:
#     guess = int(input("Enter your guess: "))

###################################################

# Card Shuffler
import random

# Deck of Cards using emojis

suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
ranks=["A","2","3","4","5","6","7","8","9","10","J", "Q","K"]

all_cards = []
for suit in suits:
    print("===================================")
    for rank in ranks:
        card = f"{suit} {rank}"
        print(card)
        all_cards.append(card)
    print("===================================")

print(all_cards)

random.shuffle(all_cards)
random.shuffle(all_cards)
random.shuffle(all_cards)

print(all_cards)

# def get_random_card():
#     f"{random.choice(suits)} {random.choice(ranks)}"

# first_card = get_random_card()
# second_card = get_random_card()
# third_card = get_random_card()

# print(first_card, second_card, third_card)