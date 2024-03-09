# Dice Roll Simulation Documentation

This project simulates the rolling of a six-sided dice using Python. When executed, it randomly selects a number between 1 and 6, inclusive, and prints a visual representation of the dice face corresponding to the number.

## How It Works

The script uses the `random` module to generate a random integer between 1 and 6, each representing a side of a six-sided dice. Depending on the number generated, a pattern that represents the dice face is printed to the console.

### Patterns Representation

- **1:** A single dot in the middle
- **2:** A dot on the top right and bottom left
- **3:** Three dots in a diagonal line from the bottom left to the top right
- **4:** Four dots in each corner
- **5:** Four dots in each corner and one in the middle
- **6:** Two columns of three dots each

## Prerequisites

To run this script, you need:

- Python (This script was tested with Python 3.8)

## Running the Script

1. Ensure you have Python installed on your machine.
2. Open your terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script ```
5. The script will prompt you with `"Input 'yes', if you want roll your dice : "`. Type `yes` and press Enter to roll the dice.
6. To exit the program, type anything other than `yes` when prompted.

## Modifications and Customization

Feel free to modify the script to include more sides, change the patterns, or enhance the user interface. This script serves as a basic demonstration of using conditional statements and loops in Python.

## License

This project is open-sourced and free to use. If you improve upon it or have suggestions, please share them back with the community.

