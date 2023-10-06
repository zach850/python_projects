import random 
from game_data import data  
from art import logo
from art import vs

continue_game = True 
count = 0

    
def random_character(data):
    get_random_data = random.choice(data)
    return get_random_data

def compare(a,b):
    global count 
    global continue_game

    more_followers = input("Who has more followers? Type 'A' or 'B': ")
    if more_followers.upper() == "A" and a['follower_count'] > b['follower_count']:
        count+=1
        print(f"You're right! Current score: {count}")
    elif more_followers.upper() == "B" and b['follower_count'] > a['follower_count']:
        count+=1
        print(f"You're right! Current score: {count}")
    else:
        continue_game = False 
        print("That is wrong.")

def play_game():
    global continue_game
    
    while continue_game:
        a = random_character(data)
        b = random_character(data)
        print(logo)
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}")
        compare(a,b)
 
            
if continue_game == True:
    play_game()