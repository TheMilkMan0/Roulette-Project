import random
import time
import os
def new_wheel():
    """
    Creates a new roulette wheel setup.

    The function initializes two lists:
    1. `numbers` - the numbers on the roulette wheel in their specific order.
    2. `colors` - corresponding symbols for each number's color on the wheel:
       '@' for green, '*' for black, 'O' for red.

    Returns:
        tuple: A pair containing the list of `numbers` and the list of `colors`.
    """
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
    """
    Generates a random integer between the given range (inclusive).

    Args:
        min (int): The lower bound of the range.
        cap (int): The upper bound of the range.

    Returns:
        int: A random integer within the specified range.
    """
    return random.randint(min,cap)


def load_user_profiles(filename):
    """
    Loads user profiles from a file and stores them in a dictionary.

    Each line in the file represents a user profile with the format "name,balance".

    Args:
        filename (str): The name of the file containing user profiles.

    Returns:
        dict: A dictionary where the keys are usernames (in lowercase) and the values are their balances.
    """
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
    """
    Retrieves the name and balance of a specified bettor from the profiles dictionary.

    Args:
        profiles_dict (dict): Dictionary containing user profiles.
        who_bets (str): The name of the bettor.

    Returns:
        tuple: A pair containing the bettor's name and their balance.
    """
    current_better = who_bets
    better_balence = profiles_dict[who_bets]
    return current_better, better_balence


def check_profile_exist(profiles_dict,name):
    """
    Checks if a given user profile exists in the profiles dictionary.

    Args:
        profiles_dict (dict): Dictionary containing user profiles.
        name (str): The name to check for existence.

    Returns:
        bool: True if the profile exists, False otherwise.
    """
    # This if a if statement checking if a name is in the keys of profiles_dict
    return name in profiles_dict 

def user_selection_animation(input):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(6):
        print(str(input))
        time.sleep(0.1)
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')


def collect_single_profile_bets(user_name,user_balance):
    """
    Collects bets from a single user based on their current balance and chosen options.

    Args:
        user_name (str): The name of the bettor.
        user_balance (int): The bettor's current balance.

    Returns:
        list: A list of tuples representing the user's bets and their respective amounts.
    """
    user_bets = []

    main_header = '**** BETTING OPTIONS ****'
    
    # Store the betting menus inside 
    betting_options = {
        'Color': ['Red','Black','Green'],
        'Parity': ['Odd','Even'],
        'Range': ['1-18','19-36','1-12','13-24','25-36']
    }

    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Hi {}, you have ${} in your balence.\n'.format(user_name,user_balance))
        print(main_header)
        # this counter will be the numbers displayed  
        counter = 1 # has to be reset everytime
        # Show betting options
        for key in betting_options:
            print("     {:10}:{}".format(key,counter))
            counter += 1
        print("\n     Done Betting   :0")

        # Ask for main selection
        user_input = input("Type number of selection: ")
        # confirm input is valid integer by converting 
        try:
            user_input = int(user_input)
        except:
            user_selection_animation("Improper Integer!")
            # skip this entire loop because it was a imporoper input 
            continue
        if user_input == 0:
            # Break from the while loop, returning the bets
            break  
        # the user input will start from 1 going to the length of the betting options
        if 0 < user_input <= len(betting_options):
            # user_selection holds the name of the section, not the index. ex: 'Range' or 'Color'
            user_selection = list(betting_options.keys())[user_input-1] # '-1' index offset
            user_selection_animation(user_selection)

            # Show secondary menu
            print("Hi {}, Balance: ${}\n".format(user_name,user_balance))
            print("**** {} OPTIONS ****".format(user_selection))
            # selection counter for secondary menu (the numbers on the right will be this counter)
            sec_counter = 1
            # sec_key will hold 'black' or '1-12' or 'even' depending which main section the user went into 
            # This will print (show) the menu 
            for sec_key in betting_options[user_selection]:
                print("     {:10}:{}".format(sec_key,sec_counter))
                sec_counter += 1
            print("\n     Go Back   :0")
            sec_user_input = input("Type number of selection: ")
            
            # Here im not sure how i made the go back work and also check if number is valid and how to add the bet to the dictionary and remeove from balanece, and make it all work that if the selection is wrong it will go back to the main menu 
            # Check if the secondary input is valid 
            try:
                sec_user_input = int(sec_user_input)
            except:
                user_selection_animation("Improper Integer!!")
                # Restart at the beggining of the while loop because the imporoper input 
                continue
            if sec_user_input == 0:
                user_selection_animation('Going Back!!!')
                # Restart at the beggining of the while loop because the imporoper input 
                continue
            if 0 < sec_user_input < len(betting_options[user_selection])+1:
                sec_user_selection = list(betting_options[user_selection])[sec_user_input-1]
                print("You have: ${}".format(user_balance))
                bet_ammount = input("Amount to bet on {}?\n".format(sec_user_selection))
                # Check the input is a valid integer 
                try: bet_ammount = int(bet_ammount)
                except: 
                    user_selection_animation("Improper integer!!")
                    # Restart at the beggining of the while loop because the imporoper input 
                    continue 
                # Check the user has enough in their balance
                if user_balance - bet_ammount >= 0:
                    user_balance -= bet_ammount
                    # Save the type of bet and amount being bet 
                    user_bets.append((sec_user_selection,bet_ammount))
                    print("Bet went through!")
                # User doesnt have enough money to bet the money they entered 
                else:
                    print("Insufficient funds. Total funds: ${}".format(user_balance))
                    time.sleep(3)
                    continue


            time.sleep(2)
    user_selection_animation("Bets are in!!")
    return user_bets


# Options for better:
# Black/Red, Odd/Even, Range (1-12, 13-24, 25,36), Half Ranges (1-18, 19-36), Single Numbers

def betting(profiles_dict):
    """
    Collects bets from all users by asking in console and stores them in a dictionary.

    Args:
        profiles_dict (dict): Dictionary containing user profiles.

    Returns:
        dict: A dictionary where keys are bettor names and values are their list of bets.
    """
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
    """
    Simulates spinning the roulette wheel and returns the result.

    Args:
        wheel_nums (list): List of numbers on the roulette wheel.
        wheel_colors (list): List of colors corresponding to each number.

    Returns:
        tuple: The number and color result of the spin.
    """
    indicator = "!"
    # set a variable to the number of elements on the wheel list
    number_of_possibilities = len(wheel_nums)
    # Create the wheel as a string to be printed repeedetly 
    numbers_wheel = ""

    def create_string_of_color_wheel(wheel_nums,wheel_colors):
        """
        Creates a string with the symbols representing the colors being spaced
        by 3 empty spaces inbetween

        Args:
            wheel_nums (list): List of numbers on the wheel.
            wheel_colors (list): List of colors corresponding to each number.

        Returns:
            str: A formatted string representing the color wheel.
        """
        spaces = 3
        # Itorate all the symbols in the colors list 
        color_wheel = ""
        for i in range(len(wheel_nums)):
            if wheel_nums[i] == 0:
                spaces=0
            else:
                spaces = 3
            color_wheel+="{}{}".format(" "*spaces,wheel_colors[i])
        return color_wheel # a string

    # Create the visual color wheel 
    color_wheel= create_string_of_color_wheel(wheel_nums,wheel_colors)
    for num in wheel_nums:
        len_of_num = len(str(num))
        if len_of_num == 2:
            spacing_between_items = "  "
        else:
            spacing_between_items = "   "
        # add that number and spacing after it to a string
        numbers_wheel += "{}{}".format(num,spacing_between_items)

    def calculate_indicator_location(wheel_nums,starting_pos,ending_pos):
        """
        Calculates the position of the indicator for the wheel.

        Args:
            wheel_nums (list): List of numbers on the wheel.
            starting_pos (int): Where the indicator should be after returning this function
            ending_pos (int): The ending position of the indicator, 
                this is outside this functions scope, only used as a safty net

        Returns:
            str: A formatted string representing the indicator's position.
        """
        indicator_line = ""
        if ending_pos < starting_pos:
            if ending_pos > len(wheel_nums): # saftey net so it doesnt cross over the end 
                spaces = 4 * starting_pos
            indicator_line += "{}{}".format(" "*spaces,indicator)
        else:
            if ending_pos < len(wheel_nums): # saftey net so it doesnt cross over the end 
                spaces = 4 * starting_pos
            indicator_line += "{}{}".format(" "*spaces,indicator)
        
        
        return indicator_line


    def final_sequence(numbers_wheel,color_wheel,spacing_between_items,starting_index):
        """
        Executes the final sequence of a wheel spin, visually displaying the wheel's progression.

        Args:
            numbers_wheel (list): A list of numbers representing positions on the wheel.
            color_wheel (list): A list of colors corresponding to the positions on the wheel.
            spacing_between_items (int): The spacing between items on the display.
            starting_index (int): The index on the wheel where the sequence starts.

        Returns:
            int: The final index on the wheel after the sequence completes.
    """
        final_delay = 0.2
        # get a random index on the wheel that we can pull from
        index_on_wheel = random_index(0,number_of_possibilities-1)
        while index_on_wheel <= starting_index:
            index_on_wheel = random_index(0,number_of_possibilities-1)
        # Find the visual positon of the indicator based off the lengths of the items up until that point

        # go over every index until the spot on the wheel
        for i in range(starting_index,index_on_wheel+1):
            # Craft where the indicator should be 
            indicator_line = calculate_indicator_location(wheel_nums,i,index_on_wheel)
            # Clear the console and Print all the lines
            os.system('cls' if os.name == 'nt' else 'clear')
            print(indicator_line)
            print(numbers_wheel)
            print(color_wheel)
            time.sleep(final_delay)

        return index_on_wheel
    
    def random_move_around(numbers_wheel,color_wheel,spacing_between_items):
        """
        Simulates random movements on the wheel before determining a stopping point for the final sequence function to pick up on. 

        Args:
            numbers_wheel (list): A list of numbers representing positions on the wheel.
            color_wheel (list): A list of colors corresponding to the positions on the wheel.
            spacing_between_items (int): The spacing between items on the display.

        Returns:
            int: The index on the wheel where the random movement stops.
        """
        # how often to move the cursor
        move_delay = 0.2
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
                # Craft where the indicator should be 
                indicator_line = calculate_indicator_location(wheel_nums,j,stoping_point)
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
                # Craft where the indicator should be 
                indicator_line = calculate_indicator_location(wheel_nums,k,stoping_point)
                # Clear the console and Print all the lines
                os.system('cls' if os.name == 'nt' else 'clear')
                print(indicator_line)
                print(numbers_wheel)
                print(color_wheel)
                time.sleep(move_delay)

        return k
    # move around the board randomly 
    it_stoped_here = random_move_around(numbers_wheel,color_wheel,spacing_between_items)
    #then do the final sequence

    # TESTING Vars:
    index_on_wheel = final_sequence(numbers_wheel,color_wheel,spacing_between_items,it_stoped_here)
    return wheel_nums[index_on_wheel],wheel_colors[index_on_wheel]


def process_bets(num_result, color_result, all_bets, profiles):
    """
    Processes all bets based on the result of the wheel spin and updates player profiles.

    Args:
        num_result (int or str): The number result of the wheel spin.
        color_result (str): The color result of the wheel spin ('*' for black, 'O' for red, other for green).
        all_bets (dict): A dictionary where keys are player names and values are lists of tuples with bet types and amounts.
        profiles (dict): A dictionary where keys are player names and values are their current balances.

    Returns:
        None
    """
    # if someone wins this amount or over it will show a message congradulaing them 
    big_winner_threshold = 30

    # small bet threshold, meaning if they only won this or less it will show a small frouny face
    small_bet_threshold = 4

    winning_bets = []

    
    # Process the result 
    if num_result == "00" or num_result == "0":
        winning_bets.append("Zero")
    elif num_result % 2 == 0:
        winning_bets.append("Even")
    elif num_result % 2 == 1:
        winning_bets.append("Odd")

    if color_result == "*":
        winning_bets.append("Black")
    elif color_result == "O":
        winning_bets.append("Red")
    else:
        winning_bets.append("Green")
    
    if num_result != "00" and num_result != "0":
        if 1 <= num_result <= 18:
            winning_bets.append("1-18")
        if 19 <= num_result <= 36:
            winning_bets.append("19-36")
        if 1 <= num_result <= 12:
            winning_bets.append("1-12")
        if 13 <= num_result <= 24:
            winning_bets.append("13-24")
        if 25 <= num_result <= 36:
            winning_bets.append("25-36")
    

    bets_multiply = {"Even":2,"Odd":2,
                     "Black":2,"Red":2,
                     "doubleZero": 35, "Zero":35,
                     "1-12": 3, "13-24":3, "25-36":3,
                     "1-18":2, "19-36":2} # just add all the types of bets here and their multiplicity 

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
        print()
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
    """
    Saves the profiles with updated balances to a text file.

    Args:
        profiles (dict): A dictionary where keys are player names and values are their current balances.

    Returns:
        None
    """
    user_file = open("roulette_users.txt",'w')
    for key in profiles:
        betters_name = key
        betters_balence = profiles[key]
        user_file.write("{},{}\n".format(betters_name,betters_balence))
    user_file.close()
    print("\nProfiles Saved.")


    

if __name__ == "__main__":
    color_key = {'@':'Green','*':'Black','O':'Red'}
    wheel_nums, wheel_colors = new_wheel()
    while True:
        profiles = load_user_profiles("roulette_users.txt")
        all_bets = betting(profiles)
        num_result, color_result = spin_wheel(wheel_nums,wheel_colors)
        print("{} {}".format(str(num_result),color_key[str(color_result)]))
        process_bets(num_result,color_result,all_bets,profiles)




# Variables you can change
# indicator = "!" 
#   the thing shown above the number its at (represents the ball)

# spacing_between_items = "   " or "   "
#   the spaces between the wheel items show visually 
#   !!!! if you were to change this you have to change both (inside the if statements) an equal amount!!!

# final_delay = 0.2
#   the timing of the indicator moving on the final roll to the winning number

# move_delay = 0.2
#   the timing of the indicator moving during the random moving to throw off the players

# number_of_randomness = random_index(0,3)
#   number of times (randomized) we mess with the player going back and forth before the final winning number
#   Change the second number in 'random_index(0,3)' to increase the number of times it MAY be able to switch around
#   If you want it to always switch around a set amount of times remove the 'random_index(0,3)' and replace it with a integer

# big_winner_threshold = 30
#   the threshold for a winning bet to be considered a big win. If the total number of winnings for a better is this number or over this number it will print a big message congradulating them

# small_bet_threshold = 4
#   the threshold for a winning bet to be considered a small win. If the total number of winnings for a better is this number or smaller than this number it will print a sad message; encauraging them to bet more to win more.



