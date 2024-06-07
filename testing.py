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
    indicator_line = ""
    if end_pos < len(wheel_nums):
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



for i in range(15):
    indicator_line = new_idea_indicator_location(wheel_nums,15,i)
    print(indicator_line)
    print(numbers_wheel)
    print(color_wheel)
    time.sleep(0.5)


