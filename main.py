import random
import time
import os
def new_wheel():
    '''
    This function creates a new wheel lists 
    The numbers list will be the random order of the roulett wheel
    The colors list will be filled with symbols that match the color of the number at the same index 
    The colors are @ for green, * for black, O for red.
    Returns:
        tuple - Numbers (List), Colors (List)
    '''
    # create a new list with the order of a roulette wheel
    numbers = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,"00",27,10,25,26,12,8,19,31,18,6,21,33,16,4,23,35,14,2]
    # match the numbers with their color in sybols
    # Black: *
    # Red: O
    # Green: @
    colors = ['@','*','O','*','O','*','O','*','O','*','O','*','O','*','O','*','O','*','O','@','O','*','O','*','O','*','O','*','O','*','O','*','O','*','O','*','O','*']
    return numbers, colors

# numbers, colors = new_wheel()
# print(len(numbers))
# print(len(colors))


def random_index(min,cap):
    # Returns a random number from 0 to the cap integeger 
    return random.randint(min,cap)


def load_user_profiles(filename):
    # Iniculize a new prfile dictionary, storing all the user info
    profiles_dict = {}
    # Open the file that has all the profiles saved on each line
    profiles_file = open(filename,'r')
    # Iterate over every line which each line has a profile in it
    for line in profiles_file:
        # Each profile list will hold the name in the first index and the ammount they have in the second index
        profile_list = line.strip().split(",")
        # Pull out elements
        name = profile_list[0].lower()
        balence = int(profile_list[1])
        # Map profile to dictionary
        profiles_dict[name]=balence
    # Return dictionary with the names mapped to balences
    return profiles_dict

# profiles = load_user_profiles("roulette_users.txt")
# print(profiles)


def collect_profile_info(profiles_dict,who_bets):
    '''
    Returns:
        current_better - Better name
        better_balence - Balence of the better
    '''
    current_better = who_bets
    better_balence = profiles_dict[who_bets]
    return current_better, better_balence


def check_profile_exist(profiles_dict,name):
    '''
    This function will check if a given name exists in the profiles
    Returns:
        True
        False
    '''
    # Check if the key in the profiles dict exists
    try:
        blah = profiles_dict[name]
        return True
    # If it doesnt exist, return False
    except:
        return False


def collect_single_profile_bets(better,balance):
    # store all the betting options visually in the 
    betting_options = """
**** BETTING OPTIONS ****
    Color:    1
    Parity:   2
    Done Betting: 0
"""

    color_options = """
**** COLOR OPTIONS ****
    Black:    1
    Red:      2
    Go Back:  9
"""

    parity_options = """
**** PARITY OPTIONS ****
    Odd:      1
    Even:     2
    Go Back:  9
"""

    range_options = """
**** RANGE OPTIONS ****
    Odd:      1
    Even:     2
    Go Back:  9
"""

    # Iniculize a new dictionary to track their bets 
    user_bets = []

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Hi {}, you have ${} in your balence".format(better.capitalize(),balance))
        print(betting_options)
        user_input = input("Choose an option: ")

        # If color options are selected
        if user_input == "1":
            # Clear the console and print options
            os.system('cls' if os.name == 'nt' else 'clear')
            # Display user info at top
            print("{}, Balance: ${}".format(better.capitalize(),balance))
            # Print all the options for colors (Black or Red)
            print(color_options)
            # Let the user chose the color or go back (9)
            color_choice = input("Select color or go back: ")
            # if they have a proper selecton of color  
            if color_choice in ["1","2"]:
                # Show the user how much they are alloted to bet 
                print("You have: ${}".format(balance))
                # Ask the user how much they want to bet
                bet_ammount = (input("How much do want to bet?\n"))
                # check that the input was proper 
                try:
                    bet_ammount = int(bet_ammount)
                    worked = True
                except:
                    print("You did not give a proper integer")
                    time.sleep(2)
                    continue

                
                # if the profile has suficient funds 
                if balance - bet_ammount >= 0:
                    # update the balance amount
                    balance -= bet_ammount
                    # set the chosen color to a variable 
                    color = "black" if color_choice == "1" else "red"
                    # save that bet in a list with the elements being tuples with the bet type and amount
                    user_bets.append((color,bet_ammount))
                    print("Bet went through!")
                # if the user bet more than their balance, tell them and go back to main menu
                else:
                    print("Insufficient funds. Total funds: ${}".format(balance))
                    continue # Goes back to main menu
            # if they chose to go back after inside the color menu, go back to main menu
            if color_choice == "9":
                continue  # Goes back to main menu
        # if the user chose even/odd choices
        if user_input == "2":
            # Clear the console then print the options
            os.system('cls' if os.name == 'nt' else 'clear')
            # Display user info at top
            print("{}, Balance: ${}".format(better.capitalize(),balance))
            # show the user the options for parity
            print(parity_options)
            # ask which parity they want to bet on
            parity_choice = input("Select parity or go back: ")
            # check that the user selected a valid options
            if parity_choice in ['1','2']:
                # show the user how much balence they have
                print("You have: ${}".format(balance))
                # ask how much they want to bet
                bet_ammount = int(input("How much do want to bet?\n"))
                # check if the user has enough money to bet with 
                if balance - bet_ammount >= 0:
                    # update the balance amount
                    balance -= bet_ammount
                    # set parity to the one they chose
                    parity = "even" if parity_choice == "2" else "odd"
                    # save the bet to a list with elements being tuples with the parity and bet amount inside 
                    user_bets.append((parity,bet_ammount))
                    print("Bet went through!")
                # if the user bet more than their balance, tell them and go back to main menu
                else:
                    print("Insufficient funds. Total funds: ${}".format(balance))
                    continue # Goes back to main menu
        if user_input == "0":
            break
    return user_bets


# Options for better:
# Black/Red, Odd/Even, Range (1-12, 13-24, 25,36), Half Ranges (1-18, 19-36), Single Numbers

def betting(profiles_dict):
    '''
    This function will collect all the bets from every user until everyone is done 
    and return the bets in the form of a dictionary 
    '''
    all_bets = {}
    # ask who is betting, if the user types "Done Betting" then move on to spin the wheel
    while True:
        # ask who is betting
        who_bets = input("Who is betting?\n").lower()
        if who_bets.lower() == "done" or who_bets.lower() == "d":
            break
        # if the user input of the person betting is a profile 
        if check_profile_exist(profiles_dict,who_bets):
            # set the profile info to name and balance
            better_name, balance = collect_profile_info(profiles_dict,who_bets)
            # Collect that person bets
            user_bets = collect_single_profile_bets(better_name,balance)
            # Assign that persons bets to 
            all_bets[better_name] = user_bets
        else:
            print("Non-Existant Profile Name, Please Try Again\n")

    # Example
    # {'alex':[(red,20),(even,5)],'xyra':(black,10)}
    return all_bets 


def spin_wheel(wheel_nums, wheel_colors):
    indicator = "!"
    # set a variable to the number of elements on the wheel list
    number_of_possibilities = len(wheel_nums)
    # 
    spacing_between_items = "   "
    # Create the wheel as a string to be printed repeedetly 
    numbers_wheel = ""

    def calculate_spaces_for_color_wheel(wheel_nums,wheel_colors):
        spaces = 0
        # Itorate all the symbols in the colors list 
        color_wheel = ""
        for i in range(len(wheel_nums)):
            if wheel_nums[i] != 0:
                spaces=len(str(wheel_nums[i]))+len(spacing_between_items)-1
            color_wheel+="{}{}".format(" "*spaces,wheel_colors[i])
        return color_wheel # a string

    # Create the visual color wheel 
    color_wheel= calculate_spaces_for_color_wheel(wheel_nums,wheel_colors)
    for num in wheel_nums:
        # add that number and spacing after it to a string
        numbers_wheel += "{}{}".format(num,spacing_between_items)


    def final_sequence(numbers_wheel,color_wheel,spacing_between_items,starting_index,true_position):
        final_delay = 0.4
        # get a random index on the wheel that we can pull from
        index_on_wheel = random_index(0,number_of_possibilities-1)
        while index_on_wheel <= starting_index:
            index_on_wheel = random_index(0,number_of_possibilities-1)
        # Find the visual positon of the indicator based off the lengths of the items up until that point

        # go over every index until the spot on the wheel
        for i in range(starting_index,index_on_wheel):
            # add the length of the item in the number wheel and the spacing to the true position

            true_position += len(str(wheel_nums[i]))
            true_position += len(spacing_between_items)
            # Craft where the indicator should be 
            indicator_line = " " * true_position + indicator
            # Clear the console and Print all the lines
            os.system('cls' if os.name == 'nt' else 'clear')
            print(indicator_line)
            print(numbers_wheel)
            print(color_wheel)
            time.sleep(final_delay)

        return index_on_wheel
    
    def random_move_around(numbers_wheel,color_wheel,spacing_between_items):
        # how often to move the cursor
        move_delay = 0.4
        # Find the visual positon of the indicator based off the lengths of the items up until that point
        true_position = 0
        # ajust how many random turn arounds you want to have
        number_of_randomness = random_index(0,3)
        k = 0
        for i in range(number_of_randomness):
            stoping_point = random_index(k,number_of_possibilities-1)
            # go forwards from 0 index to the random stoping point
            for j in range(k,stoping_point+1):
                # add the length of the item in the number wheel and the spacing to the true position
                true_position += len(str(wheel_nums[j]))
                true_position += len(spacing_between_items)
                # Craft where the indicator should be 
                indicator_line = " " * true_position + indicator
                # Clear the console and Print all the lines
                os.system('cls' if os.name == 'nt' else 'clear')
                print(indicator_line)
                print(numbers_wheel)
                print(color_wheel)
                time.sleep(move_delay)
            # go backwards from the stoping point to zero
            random_backwards_point = random_index(0,stoping_point)
            for k in range(stoping_point,random_backwards_point-1,-1):
                # add the length of the item in the number wheel and the spacing to the true position
                true_position -= len(spacing_between_items)
                true_position -= len(str(wheel_nums[k-1]))
                # Craft where the indicator should be 
                indicator_line = " " * true_position + indicator
                # Clear the console and Print all the lines
                os.system('cls' if os.name == 'nt' else 'clear')
                print(indicator_line)
                print(numbers_wheel)
                print(color_wheel)
                time.sleep(move_delay)

        return k, true_position
    # move around the board randomly 
    it_stoped_here, true_position = random_move_around(numbers_wheel,color_wheel,spacing_between_items)
    # then do the final sequence
    index_on_wheel = final_sequence(numbers_wheel,color_wheel,spacing_between_items,it_stoped_here,true_position)
    return wheel_nums[index_on_wheel],wheel_colors[index_on_wheel]


def process_bets(num_result, color_result, all_bets, profiles):
    # if someone wins this amount or over it will show a message congradulaing them 
    big_winner_threshold = 30

    # small bet threshold, meaning if they only won this or less it will show a small frouny face
    small_bet_threshold = 4

    winning_bets = []

    
    # Process the result 
    if num_result == "00" or num_result == "0":
        winning_bets.append("zero")
    elif num_result % 2 == 0:
        winning_bets.append("even")
    elif num_result % 2 == 1:
        winning_bets.append("odd")

    if color_result == "*":
        winning_bets.append("black")
    elif color_result == "O":
        winning_bets.append("red")
    else:
        winning_bets.append("green")

    bets_multiply = {"even":2,"odd":2,
                     "black":2,"red":2,
                     "doubleZero": 35, "zero":35} # just add all the types of bets here and their multiplicity 
    
    for key in all_bets:
        betters_losings = 0
        betters_winnings = 0
        # Key will equal the name of the better
        better_name = key
        list_of_bets = all_bets[key] # [("red",20),("odd",5)]
        for bet in list_of_bets:
            # bet will be ("red",20)
            type_of_bet = bet[0] # type of bet will be "red" in this case
            bet_ammount = bet[1] # bet_ammount is 20 in this case
            if type_of_bet in winning_bets:
                # if the type of bet they placed is a winning bet
                # then add to their winnings their bet amount times the 
                # amount that bet gets multiplied because the type of bet
                betters_winnings += bet_ammount * bets_multiply[type_of_bet]
            # if that bet didnt win
            else:
                betters_losings += bet_ammount
        # add the winnings to their profile 
        profiles[better_name] += betters_winnings - betters_losings
        # Now that we are done using dictionarys, we switch to the capitalized name
        better_name = better_name.capitalize()
        if betters_winnings == 0:
            print("{} didnt win... Better Luck Next Time!".format(better_name,betters_winnings))
        # if this better won only a small amount print a sad message
        elif betters_winnings <= small_bet_threshold:
            print("{} only won: ${} so sad :(".format(better_name,betters_winnings))
        # if this better won a okay amount print default message
        elif betters_winnings < big_winner_threshold:
            print("{} won: ${}".format(better_name,betters_winnings))
        # if the better won big then print message
        elif betters_winnings >= big_winner_threshold:
            print("\n!!! BIG WINNER BIG WINNER!!!")
            print("   {} won: ${}\n".format(better_name,betters_winnings))

    # save all the profile info in a text file
    save_profiles(profiles)


def save_profiles(profiles):
    user_file = open("roulette_users.txt",'w')
    for key in profiles:
        betters_name = key
        betters_balence = profiles[key]
        user_file.write("{},{}\n".format(betters_name,betters_balence))
    user_file.close()


    

if __name__ == "__main__":

    wheel_nums, wheel_colors = new_wheel()
    while True:
        profiles = load_user_profiles("roulette_users.txt")
        all_bets = betting(profiles)
        num_result, color_result = spin_wheel(wheel_nums,wheel_colors)
        process_bets(num_result,color_result,all_bets,profiles)




# Variables you can change
# indicator = "!" 
#   the thing shown above the number its at (represents the ball)

# spacing_between_items = "   "
#   the spaces between the wheel items show visually 

# final_delay = 0.4
#   the timing of the indicator moving on the final roll to the winning number

# move_delay = 0.08
#   the timing of the indicator moving during the random moving to throw off the players

# number_of_randomness = 6
#   number of times we mess with the player going back and forth before the final winning number

# big_winner_threshold = 30
#   the threshold for a winning bet to be considered a big win. If the total number of winnings for a better is this number or over this number it will print a big message congradulating them

# small_bet_threshold = 4
#   the threshold for a winning bet to be considered a small win. If the total number of winnings for a better is this number or smaller than this number it will print a sad message; encauraging them to bet more to win more.