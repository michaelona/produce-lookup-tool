"""
Produce Code Finder
-----------------------
Description:
    A lookup tool for produce codes (PLU) for grocery shopping.
    Users can enter either a produce name or a PLU code
    and get the corresponding match.

    Custom databases can be created or imported on Windows/Mac/Linux platforms
    and include add, update, and delete funcitons to manage custom databases.

    When running on mobile platforms, custom databases
    are disabled and the default database is used.

    Codes and Names are based off data from Ingles Markets.
    
Author: Michael Onate
Date: 9-2-2025
Version: 1.0
"""

# TODO 
# 4 - Save json (if all exists and its good) before program close
# 5 - Test all cases
# 6 - List importing



# IMPORT STATEMENTS
import json, platform, difflib, os

# DEFAULT DATABASES
defaultNameToCode = {
  "apple - fuji": "4131",
  "apple - golden delicious": "4020",
  "apple - granny smith": "4017",
  "banana": "4011",
  "coconut": "4261"
  #ENTER FULL LIST HERE
}
defaultCodeToName = {
  "4131": "apple - fuji",
  "4020": "apple - golden delicious",
  "4017": "apple - granny smith",
  "4011": "banana",
  "4261": "coconut"
  #ENTER FULL LIST HERE
}

# Handlers and Utilities
def problem_child(action_function):     #Used in database modification cmds
    """
    Safety wrapper to catch errors and return to menu.
    """
    try:
        action_function()
    except (KeyError, ValueError) as e:
        print(f"Error: {e}")
        return


def whisper(prompt: str, canCancel: bool=True, numeric: bool=False):
    """
    Input handler that normalizes user input. Allows the user to cancel if enabled. Throws error on 'cancel'.
    """
    while True:
        userInput = input(prompt).strip().lower()

        # Cancel operation is on
        if userInput == "cancel" and canCancel:
            raise ValueError("Operation cancelled by user")
        
        # Cancel operation is off
        if userInput == 'cancel' and not canCancel:
            print("Can't cancel here.")

        # Validate input 
        if numeric:
            if not userInput.isdigit():
                print("Only digits are allowed. Try again.")
                continue
            return int(userInput)
        else:
            if userInput == "":
                if canCancel:
                    print("Input cannot be empty. (or 'cancel')")
                else:
                    print("Input cannot be empty")
                continue
            return userInput

def eagle(query):
    """
    Lookup helper that searches dictionaries with exact, partial, or fuzzy matching.
    Returns a list of (code, name) tuples matching the query.
    """
    global dbCodeToName, dbNameToCode

    results = []

    # Normalize query
    query = str(query).strip().lower()

    # 1. Exact match by code
    if query in dbCodeToName:
        results.append((query, dbCodeToName[query]))
        return results

    # 2. Exact match by name
    if query in dbNameToCode:
        code = dbNameToCode[query]
        results.append((code, query))
        return results

    # 3. Partial match in names
    for name, code in dbNameToCode.items():
        if query in name:
            results.append((code, name))

    if results:
        return results

    # 4. Fuzzy match using difflib
    name_matches = difflib.get_close_matches(query, dbNameToCode.keys(), n=5, cutoff=0.6)
    for name in name_matches:
        code = dbNameToCode[name]
        results.append((code, name))

    return results
    

# Dev Tools
def dbprint(message: str) -> str: 
    print("===[DEVELOPER]===: " + message + "\n")

# Flags & Variables
enableCustomData = False
dbCodeToName = {}
dbNameToCode = {}

#1 - Initialize Database
def initData():
    """    
    Sets up database in RAM. THIS MUST RUN FIRST, OTHERWISE DATABASE WILL BE EMPTY.
    If user is on mobile, custom databases are disabled.
    """
    global enableCustomData, dbCodeToName, dbNameToCode

    # Disable custom data on mobile platforms
    if platform.system() == "Windows" or platform.system() == "Darwin":
        # dbprint("running on " + platform.system())
        enableCustomData = True

    # Handling custom datasets
    if enableCustomData:        
        code_file_exists = os.path.exists('codeToName.json')
        name_file_exists = os.path.exists('nameToCode.json')
        if code_file_exists and name_file_exists:
            with open('codeToName.json', 'r') as f:
                dbCodeToName = json.load(f)
            with open('nameToCode.json', 'r') as s:
                dbNameToCode = json.load(s)
        elif not code_file_exists and not name_file_exists:
            print("Welcome to Produce Lookup Tool!\n")
            print("Custom databases allow you to add, remove, and modify item codes and names to \nyour specifications. These files are stored in the same folder as this program.\n")
            userResponse = input("Would you like to create a new set with default values? (y/n): ").strip().lower()
            if userResponse == "y":
                with open('codeToName.json', 'w') as f:
                    json.dump(defaultCodeToName, f, indent=2)
                with open('nameToCode.json', 'w') as s:
                    json.dump(defaultNameToCode, s, indent=2)
                dbCodeToName = defaultCodeToName
                dbNameToCode = defaultNameToCode
                print("Files created successfully.")
            else:
                print("\nProceeding with default values.")
                enableCustomData = False
                dbCodeToName = defaultCodeToName
                dbNameToCode = defaultNameToCode
        else:
            print("Inconsistent database state: Only one of codeToName.json or nameToCode.json exists.")
            print("Please delete the existing file(s) so both can be created together with defaults.\n")
            print("Proceeding with default values.")
            enableCustomData = False
            dbCodeToName = defaultCodeToName
            dbNameToCode = defaultNameToCode
    else:
        dbCodeToName = defaultCodeToName
        dbNameToCode = defaultNameToCode

def saveDatabases():
    """Writes the current database dictionaries to JSON files, if custom data is enabled."""
    global enableCustomData, dbCodeToName, dbNameToCode

    if not enableCustomData:
        return  # Do nothing
    
    try:
        with open('codeToName.json', 'w') as f:
            json.dump(dbCodeToName, f, indent=2)
        with open('nameToCode.json', 'w') as s:
            json.dump(dbNameToCode, s, indent=2)
        print("Databases saved successfully.")
    except Exception as e:
        print(f"Error saving database: {e}")


# ===================== USER ACTION FUNCTIONS =====================

#1 - Search
def searchItem():
    query = whisper("Enter produce name or PLU code to search (or 'cancel'): ", True, False)
    results = eagle(query)

    if not results:
        print("No matches found.")
        return
    
    print("\n=== Search Results ===")
    for code, name in results:
        print(f"{code} - {name}")
    print()

#2 - Add Item
def databaseAdd():
    global dbCodeToName, dbNameToCode
    query_name = whisper("ADD: Enter new item name (or 'cancel'): ", True, False)
    query_code = whisper("Enter new item code (or 'cancel'): ", True, True)

    # Prevent duplicates
    if query_code in dbCodeToName:
        print(f"\nPLU code '{query_code}' already exists for '{dbCodeToName[query_code]}'.")
        return
    if query_name in dbNameToCode:
        print(f"Produce name '{query_name}' already exists with PLU code '{dbNameToCode[query_name]}'.")
        return

    if query_name and query_code:
        dbCodeToName[query_code] = query_name
        dbNameToCode[query_name] = query_code
        print(f"=== Added item: {query_code} - {query_name} ===")
        if enableCustomData:
            saveDatabases()
        print(f"JSON files updated Successfully!")
    else:
        print("Add operation cancelled.")


#3 - Remove item
def databaseRemove():
    global dbCodeToName, dbNameToCode
    user_input = whisper("REMOVE: Enter item code or exact name to remove (or 'cancel'): ", True, False)
    # Try as code
    if user_input in dbCodeToName:
        name = dbCodeToName[user_input]
        confirm = input(f"Are you sure you want to remove '{user_input} - {name}'? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Delete cancelled.")
            return
        del dbCodeToName[user_input]
        if name in dbNameToCode:
            del dbNameToCode[name]
        print(f"Removed item: {user_input} - {name}")
        if enableCustomData:
            saveDatabases()
        print(f"JSON files updated Successfully!")
        return
    # Try as name
    if user_input in dbNameToCode:
        code = dbNameToCode[user_input]
        confirm = input(f"Are you sure you want to remove '{code} - {user_input}'? (y/n): ").strip().lower()
        if confirm != 'y':
            print("Delete cancelled.")
            return
        del dbNameToCode[user_input]
        if code in dbCodeToName:
            del dbCodeToName[code]
        print(f"Removed item: {code} - {user_input}")
        if enableCustomData:
            saveDatabases()
        print(f"JSON files updated Successfully!")
        return
    print("Item not found.")


#4 - Edit item
def databaseEditEntry():
    global dbCodeToName, dbNameToCode
    user_input = whisper("EDIT: Enter item code or exact name to edit (or 'cancel'): ", True, False)

    # Set target item
    if user_input in dbCodeToName:
        code = user_input
        name = dbCodeToName[code]
    elif user_input in dbNameToCode:
        name = user_input
        code = dbNameToCode[name]
    else:
        print("Item not found.")
        return

    # Request new data
    print(f"Editing item: {code} - {name}")
    new_name = whisper(f"Enter new name (Old name: '{name}'): ", True, False)
    new_code = whisper(f"Enter new code (Old code: '{code}'): ", True, True)

    # Validate and update name
    if new_name and new_name != name:
        if new_name in dbNameToCode:
            print("That name already exists.")
            return
        del dbNameToCode[name]
        dbNameToCode[new_name] = code
        dbCodeToName[code] = new_name
        name = new_name

    # Validate and update code
    if new_code and str(new_code) != code:
        new_code_str = str(new_code)
        if new_code_str in dbCodeToName:
            print("That code already exists.")
            return
        del dbCodeToName[code]
        dbCodeToName[new_code_str] = name
        dbNameToCode[name] = new_code_str
        code = new_code_str

    print(f"Updated item: {code} - {name}")
    if enableCustomData:
        saveDatabases()
        print(f"JSON files updated Successfully!")



#5 - Show all
def display_all_items():
    global dbCodeToName
    print()
    print("=== Current PLU Database ===")
    print()
    if not dbCodeToName or len(dbCodeToName) == 0:
        print("Database is empty.")
        return
    # Find max length for code for formatting
    code_width = max([len(str(code)) for code in dbCodeToName.keys()] + [4])
    name_width = max([len(str(name)) for name in dbCodeToName.values()] + [12])
    # Header
    print(f"{'PLU':<{code_width}}  {'Produce Name':<{name_width}}")
    print("-" * (code_width + 2 + name_width))
    # Sort by produce name alphabetically
    for code, name in sorted(dbCodeToName.items(), key=lambda item: item[1].lower()):
        print(f"{code:<{code_width}}  {name:<{name_width}}")
    print()
    print()








# Main Menu Loop
def mainMenu() -> None:
    """
    Displays menu items based on enableCustomData flag and handles user navigation.
    If sub-functions raise errors, they are caught and the user is returned to this menu.
    """
    global enableCustomData
    isRunning = True

    # Define menu options
    menu_options = {
        1: ("Search", searchItem),
        2: ("Add item", databaseAdd),
        3: ("Remove item", databaseRemove),
        4: ("Edit item", databaseEditEntry),
        5: ("Show All", display_all_items),
        6: ("Quit", lambda: print("Goodbye!"))
    }

    # Filter options for Limited Mode
    if not enableCustomData:
        menu_options = {key: value for key, value in menu_options.items() if key in [1, 5, 6]}

    def display_menu():
        """
        Displays the menu options based on the available options.
        """
        print("\n\t === PLU2 Lookup === \t\n")
        for key, (description, _) in menu_options.items():
            print(f"[{key}] {description}")
        print("\n")

    # Main loop
    while isRunning:
        display_menu()
        userInput = whisper("Enter an option: ", False, True)
        if userInput in menu_options:
            action = menu_options[userInput][1]
            if userInput == 6:  # Quit option
                isRunning = False
                if enableCustomData:
                    saveDatabases()
                    print(f"Syncing JSON files...")
                print("Goodbye!")
            problem_child(action)
        else:
            print("Invalid option. Please try again.")


# ===================== MAIN =====================
initData()
mainMenu()