# parking
First small Python program.


# Parking Management System Documentation

## Introduction
The provided Python code represents a simple parking management system. It allows users to manage vehicle entry and exit, view the list of vehicles in the parking lot, and change the parking fee rates.

## Code Structure

### Import Statements
```python
import shelve
import sys
from time import *
from parking import int
```
- The `shelve` module is used for persistent storage of data.
- `sys` is used for system-specific functionality.
- `time` is imported for time-related operations.
- `parking` is imported, but it seems to be an unused import, and the import statement itself contains a typo (`int` instead of `print`).

### Global Variables
```python
global base, rate, period
```
- `base`: Represents the database storing information about parked vehicles and rate settings.
- `rate`: Represents the parking fee rate.
- `period`: Represents the time period for which the rate is applied.

### Function: `rate_change()`
```python
def rate_change():
    # ...
```
- Allows users to change the parking fee rate and time period.
- Retrieves input for the new rate and time period, and updates the global variables accordingly.
- Saves the new rate and time period in the database.

### Function: `init()`
```python
def init():
    # ...
```
- Initializes the parking management system.
- Attempts to open the database using the `shelve` module.
- If successful, checks if rate information exists in the database and initializes global variables accordingly.
- If not, sets default rate and period values and calls `rate_change()` to load user input.

### Function: `menu()`
```python
def menu():
    # ...
```
- Displays the main menu for the parking management system.
- Accepts user input for menu options (Entry, Exit, Vehicles, Rate, Close).
- Returns the user's choice.

### Function: `vehicles()`
```python
def vehicles():
    # ...
```
- Displays a list of vehicles in the parking lot.
- Uses the `strftime` function to format and display registration numbers and park hours.

### Function: `exit_()`
```python
def exit_():
    # ...
```
- Handles the process when a vehicle exits the parking lot.
- Retrieves the registration number and checks if the vehicle was parked.
- Calculates the parking duration and fee, deletes the registration from the database.

### Function: `enter()`
```python
def enter():
    # ...
```
- Handles the process when a vehicle enters the parking lot.
- Retrieves the current time and prompts the user to enter the vehicle's registration number.
- Checks if the vehicle is not already parked and updates the database accordingly.

### Function: `choice()`
```python
def choice():
    # ...
```
- Implements user choices based on the selected menu option.
- Calls the corresponding functions (rate_change, vehicles, exit_, enter) based on the user's choice.

### Main Program
```python
init()  # Open database
try:
    choice()  # User interface
except:
    print("Critical error.")
base.close()  # Close database
```
- Initiates the parking management system by calling `init()`.
- Executes the main user interface loop (`choice()`).
- Catches exceptions and prints a critical error message if encountered.
- Closes the database before exiting.

## Conclusion
This documentation provides an overview of the structure and functionality of the provided parking management system. Users can interact with the system to manage vehicle entry and exit, view the list of vehicles, and modify parking fee rates.
