import time
wheel_nums = [0,28,9,26,30,11,7,20,32,17,5,22,34,15,3,24,36,13,1,"00",27,10,25,26,12,8,19,31,18,6,21,33,16,4,23,35,14,2]
wheel_colors = ['@','*','O','*','O','*','O','*','O','*','O','*','O','*','O','*','O','*','O','@','O','*','O','*','O','*','O','*','O','*','O','*','O','*','O','*','O','*']
spacing_between_items = "   "

def string_color_wheel(wheel_nums,wheel_colors):
        # Itorate all the symbols in the colors list 
        color_wheel = ""
        for i in range(len(wheel_nums)):
            if i == 0:
                spaces = 0
            else:
                spaces = 3
            color_wheel+="{}{}".format(" "*spaces,wheel_colors[i])
        return color_wheel # a string

# Create the visual color wheel 
color_wheel= string_color_wheel(wheel_nums,wheel_colors)

numbers_wheel = ""
for num in wheel_nums:
    len_of_num = len(str(num))
    if len_of_num == 2:
        spacing_between_items = "  "
    else:
        spacing_between_items = "   "
    # add that number and spacing after it to a string
    numbers_wheel += "{}{}".format(num,spacing_between_items)

def new_idea_indicator_location(wheel_nums,end_pos,start_pos):
    '''
    Start pos is more of a indicator of where the indicator should be 
    '''
    indicator_line = ""
    
    if end_pos < len(wheel_nums): # saftey net so it doesnt cross over the end 
        spaces = 4 * start_pos
        indicator_line += "{}{}".format(" "*spaces,"!")
    return indicator_line



def forwards_calculate_indicator_location(wheel_nums,end_pos):
    indicator_pos = ""
    spaces = 0
    if end_pos < len(wheel_nums):
        for j in range(end_pos+1):
            if wheel_nums[0] != wheel_nums[j]:
                spaces+=len(str(wheel_nums[j]))+len(spacing_between_items)
        indicator_pos+="{}{}".format(" "*spaces,"!")
    else:
        return "INVALID"
    return indicator_pos # a string


def backwards_calculate_indicator_location(wheel_nums,start,end_pos):
    indicator_pos = ""
    spaces = 0
    for j in range(start,end_pos+1,-1):
        if wheel_nums[start] != wheel_nums[j] and j > 0:
            spaces+=len(str(wheel_nums[j]))+len(spacing_between_items)
    indicator_pos+="{}{}".format(" "*spaces,"!")
    return indicator_pos # a string



# for i in range(15):
#     indicator_line = new_idea_indicator_location(wheel_nums,15,i)
#     print(indicator_line)
#     print(numbers_wheel)
#     print(color_wheel)
#     time.sleep(0.5)
import os

def user_selection_animation(input):
    os.system('cls' if os.name == 'nt' else 'clear')
    for i in range(6):
        print(str(input))
        time.sleep(0.1)
    time.sleep(0.1)
    os.system('cls' if os.name == 'nt' else 'clear')

def ask_for_individual_bets_from_user():
    user_name = "Alex"
    user_balance = 10
    user_bets = []

    main_header = '**** BETTING OPTIONS ****'
    

    betting_options = {
        'Color': {'Red':1,'Black':2,'Green':3},
        'Parity': {'Odd':1,'Even':2},
        'Range': {'1-18':1,'19-36':2,'1-12':3,'13-24':4,'25-36':5}
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


            time.sleep(4)
    user_selection_animation("Bets are in!!")
    return user_bets
        

    

print(ask_for_individual_bets_from_user())

