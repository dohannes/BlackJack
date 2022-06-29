"""
    Simple Black Jack Game!
            Closest to 21 wins!
        1. Ask user if they wish to play
        2. If yes, present them with 2 RANDOM cards; if no, exit loop
        3. Present computers RANDOMLY selected card... (singular)
        4. Ask User if they want to "hit". If yes, add another card; if no, continue game
        5. If the users update card list is  greater than 21, computer wins; else, user wins!
            End
"""
# import necessary modules
import random

# make default values, along with this allow all special cards to the value 10
card_deck={"default": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}

# functions
def user_pick_random(hands:dict, key:str):
    # create array each iteration of code
    gen_numbers=[]
    # generate two random numbers to append to our empty array
    for user_nums in range(2):
        ran_numbers=random.choice(hands[key]) # generate random number from our passed in parameters
        gen_numbers.append(ran_numbers)

    return gen_numbers

def comp_pick_random(hands:list, key:str):
    comp_gen=[] # empty array for the computer numbers
    # create two seperate numbers for the bot
    for comp_nums in range(2):
        ran_comp_numbers=random.choice(hands[key])
        comp_gen.append(ran_comp_numbers)

    return comp_gen

def create_user_score(selected_array:list):
    # we want to add the two numbers together, for this we must print out the array
    user_score=0 # initialize user score to increment later

    # get two parts from generated arary
    first_num=selected_array[0]
    second_num=selected_array[1]

    # add the two together
    total_value=first_num+second_num
    # increment user_score by this total_value
    user_score+=total_value

    return user_score

def hit_me(selected_array:list, key:str, user_score:int):
    # generate random number to increment score
    new_number=random.choice(selected_array[key])
    return new_number

# open ASCII art for start
with open("./art.txt", "r") as art_file:
    # access external file, read all the lines and save them in a variable we will produce later in code!
    ascii_art=art_file.read()

print(f"\n{ascii_art}") # produce the lines read from art_file

while True:
    # allow user to select to play or not    
    game_choice=input("1. Play    2. Rules    3. Exit\nChoice: ")

    # catch error if input isn't at base 10; unfortunately, i cannot seem to implement a float detection protocol :(
    try: 
        int(game_choice) # try to convert input value to intger
    except ValueError: # catch error, output print statement, and return user to decision
        print("Invalid Command!\n")

    # wrap choice in int data type as we require it to be an integer
    if int(game_choice) == 1:
        user_cards=user_pick_random(hands=card_deck, key="default")
        # create variable that holds 
        player_score=create_user_score(selected_array=user_cards)
        print(f"Your score is: {player_score}!\n")
        # create bool var to be altered if score is greater than 21
        above = False
        # create loop to hit again :)
        while True:
            new_choice=input("Do you want to hit again?\n1. Yes\n2. No\nChoice: ")
            
            # try except for value error
            try:
                int(new_choice)
            except ValueError:
                print("Please enter a valid selection!")
            finally:
                if int(new_choice) == 1:
                    new_player_score=hit_me(selected_array=card_deck, key="default", user_score=player_score)
                    player_score+=new_player_score
                    # now check if the score is above or lesser than 21
                    while above == False:
                        if player_score > 21:
                            above = True
                            print(f"TOO BAD! YOU LOSE :)\nYour score was {player_score} Better Luck next time!")
                            break
                        else:
                            print(f"Great job! Your score is now {player_score} :)")
                            break
                elif int(new_choice) == 2:
                    print(f"Your final score was: {player_score}!")
                    break
                else:
                    print("Exiting game...")
                    break


    elif int(game_choice) == 2:
        print("Choice 2")
        break
    elif int(game_choice) == 3:
        print("Choice 3")
        break