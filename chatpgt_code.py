import time
import os

def print_roulette_wheel(numbers, position):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clears the console
    spacing_between_numbers = "   "
    true_position = 0
    for i in range(position):
        true_position += len(str(numbers[i]))
        true_position += len(spacing_between_numbers)

    indicator_line = ' ' * (true_position) + '^'  # Create spacing for the indicator
    wheel = ""
    for num in numbers:
        wheel += "{}{}".format(num,spacing_between_numbers)

    print(indicator_line)
    print(wheel)

def main():
    numbers = [0, 32, 15, 19, 4, 21, 2, 25]  # Simplified roulette wheel numbers
    current_position = 0
    num_cycles = 30  # Number of movements
    delay = 0.5  # Half a second between updates

    for _ in range(num_cycles):
        print_roulette_wheel(numbers, current_position)
        current_position = (current_position + 1) % len(numbers)
        time.sleep(delay)

if __name__ == "__main__":
    main()
