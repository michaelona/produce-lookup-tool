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
# 5 - Test all cases
# 6 - List importing



# IMPORT STATEMENTS
import json, platform, difflib, os

# DEFAULT DATABASES
defaultNameToCode = {
  "apples - ambrosia": "3438",
  "apples - braeburn": "4103",
  "apples - cameo": "3066",
  "apples - cortland": "4106",
  "apples - empire": "4124",
  "apples - envy": "3616",
  "apples - fuji": "4131",
  "apples - gala": "4135",
  "apples - golden delicious": "4020",
  "apples - granny smith": "4017",
  "apples - honey crisp": "3283",
  "apples - jazz": "4200",
  "apples - jonagold": "4147",
  "apples - koru": "3620",
  "apples - macoun": "3073",
  "apples - mcintosh": "4152",
  "apples - pinata": "4215",
  "apples - pink lady": "4130",
  "apples - rave": "3487",
  "apples - red delicious": "3284",
  "apples - rome": "4172",
  "apples - sweet tango": "3603",
  "apples - winesap": "4183",
  "apricots": "4218",
  "apricots - velvet": "3044",
  "artichokes": "4520",
  "asparagus": "4080",
  "asparagus - white": "4522",
  "aspiration": "3277",
  "avocados - green skin": "4771",
  "avocados - hass": "4046",
  "bananas": "4011",
  "beans": "4535",
  "bok choy": "4545",
  "broccoli": "4060",
  "broccoli crowns": "3082",
  "broc-o-flower": "4567",
  "brussel sprout": "4550",
  "bunch beets": "94539",
  "cabbage - green": "4069",
  "cabbage - napa": "4552",
  "cabbage - red": "4554",
  "cabbage - savoy": "4555",
  "cactus pears (tunas)": "4255",
  "candy": "4883",
  "canela (cinnamon sticks)": "4821",
  "cantaloupe - eastern": "4319",
  "cantaloupe - western": "4050",
  "carrots - bulk": "4564",
  "cauliflower": "4079",
  "celery - stalk": "4070",
  "celery hearts": "4575",
  "celery root": "4585",
  "cherries": "4045",
  "cherries - rainier": "4258",
  "chest nuts": "4927",
  "cilantro": "4889",
  "coconut": "4261",
  "coconut - young white": "4260",
  "corn - bi-color": "4590",
  "corn - white": "4077",
  "corn - yellow": "4078",
  "cranberries - bulk": "4242",
  "cucumbers": "4597",
  "cucumbers - pickling": "4596",
  "cucumbers - hot house cukes": "4593",
  "dates - medjool": "3047",
  "dragon fruit": "3040",
  "eggplant": "4081",
  "garlic": "4608",
  "ginger root (organic)": "94612",
  "grape tomatoes (bulk)": "3147",
  "grapefruit - red": "4282",
  "grapefruit - white": "4293",
  "grapes - black seedless": "4056",
  "grapes - red seedless": "4023",
  "grapes - white seedless": "4022",
  "collard greens": "4614",
  "creasy greens": "4620",
  "kale": "4627",
  "mustard greens": "4616",
  "turnip greens": "4619",
  "herbs - fresh arugula": "4884",
  "herbs - fresh basil": "4885",
  "herbs - fresh chives": "4888",
  "herbs - fresh dill": "4891",
  "herbs - fresh mint": "4896",
  "herbs - fresh oregano": "4897",
  "herbs - fresh rosemary": "4903",
  "herbs - fresh sage": "4904",
  "herbs - fresh thyme": "4907",
  "honeydew": "4034",
  "horseradish root (organic)": "94625",
  "jamaica": "4505",
  "jicama": "4626",
  "kiwi fruit": "4030",
  "kohlrabi": "4628",
  "kumquats": "4303",
  "leeks": "4629",
  "lemons - meyer": "4304",
  "lemons": "4053",
  "lettuce - boston": "4632",
  "lettuce - cello head": "4061",
  "lettuce - endive": "4604",
  "lettuce - belgium endive": "4543",
  "lettuce - escarole": "4605",
  "lime": "4048",
  "mandarinquat": "4471",
  "mangoes": "4051",
  "mangoes - ataulfo": "4312",
  "melons - pepino": "4333",
  "mushrooms (bulk)": "4653",
  "name": "3276",
  "nectarines": "4036",
  "nectarines - white": "3035",
  "nuts - loose bulk": "4929",
  "okra": "4655",
  "onions - green": "4068",
  "onions - sweet": "4166",
  "onions - red": "4082",
  "onions - white": "4663",
  "onions - yellow": "4093",
  "oranges - cara cara": "3110",
  "oranges - mandarins": "4455",
  "oranges - navel": "3107",
  "oranges - satsuma": "3029",
  "papayas": "3111",
  "papayas - maradol": "3112",
  "parsley - curly": "4900",
  "parsley - italian": "4901",
  "parsnips": "4672",
  "peaches": "4038",
  "peaches - donut white": "3113",
  "peaches - southern": "4403",
  "peaches - white": "4401",
  "peanuts - raw or green": "4931",
  "pears - anjou": "4416",
  "pears - asian": "4408",
  "pears - bartlett": "4409",
  "pears - bosc": "4413",
  "pears - comice": "4414",
  "pears - red": "4415",
  "pepitas": "4501",
  "green bell peppers": "4065",
  "orange peppers": "3121",
  "red peppers": "4688",
  "yellow peppers": "4689",
  "habanero peppers": "3125",
  "all chile peppers": "4691",
  "persimmons": "4427",
  "piloncillo (brown sugar cane)": "4820",
  "pineapple": "4433",
  "plantain bananas": "4235",
  "plums - black": "4040",
  "plums - lemons": "4442",
  "plums - red": "4042",
  "pluots": "3278",
  "pomegranates": "3127",
  "potato - baking": "4072",
  "potato - red": "4073",
  "potato - sweet": "4091",
  "potato - white": "4083",
  "pummelos": "3129",
  "pumpkins": "4736",
  "pie pumpkins": "3134",
  "radicchio": "4738",
  "radish bunch": "4089",
  "rapini": "4547",
  "rhubarb": "4745",
  "rutabagas": "4747",
  "flowering kale": "3095",
  "shallots": "4662",
  "snow peas": "4092",
  "squash - banana": "4757",
  "squash - acorn gold": "4751",
  "squash - acorn green": "4750",
  "squash - butternut": "4759",
  "squash - chayote": "4761",
  "squash - delicotta": "4763",
  "squash - golden nugget": "4767",
  "squash - hubbard": "4768",
  "squash - kabocha": "4769",
  "squash - spaghetti": "4776",
  "squash - sweet dumpling": "4764",
  "squash - turban": "4780",
  "squash - yellow": "4784",
  "squash - zucchini": "4067",
  "squash - buttercup": "4758",
  "star fruit": "4256",
  "tamarindo": "4448",
  "tangelos (monneola)": "4383",
  "tangerines - pixie": "4457",
  "tangerines - sunburst": "4449",
  "tomatillos": "4801",
  "tomato - cluster": "4664",
  "tomato - green": "4064",
  "tomato - greenhouse": "4799",
  "tomato - heirloom": "4807",
  "tomato - locally grown": "4800",
  "tomato - roma": "4087",
  "tomato - vintage vineripe": "3423",
  "tomato - yellow": "4778",
  "turnip roots": "4813",
  "ugli fruit": "4459",
  "personal watermelon": "3421",
  "slice of watermelon": "4376",
  "watermelon (seeded)": "4031",
  "watermelon (seedless)": "4032",
  "yuca root": "4819",
  "bagels": "320",
  "christmas trees": "1225",
  "cookies by bag": "301",
  "cookies by box": "305",
  "self serve donuts": "300",
  "dry ice": "900",
  "muffins": "315",
  "olive bar": "351",
  "rolls": "309",
  "salad bar": "350",
  "whole bean coffee": "328",
  "almond butter": "4950",
  "organic peanut butter": "4951",
  "honey peanut butter": "4948",
  "dry roast butter": "4947",
  "croissants": "726",
  "wing bar": "7202",
  "peanut": "9901"
}

defaultCodeToName = {
  "3438": "apples - ambrosia",
  "4103": "apples - braeburn",
  "3066": "apples - cameo",
  "4106": "apples - cortland",
  "4124": "apples - empire",
  "3616": "apples - envy",
  "4131": "apples - fuji",
  "4135": "apples - gala",
  "4020": "apples - golden delicious",
  "4017": "apples - granny smith",
  "3283": "apples - honey crisp",
  "4200": "apples - jazz",
  "4147": "apples - jonagold",
  "3620": "apples - koru",
  "3073": "apples - macoun",
  "4152": "apples - mcintosh",
  "4215": "apples - pinata",
  "4130": "apples - pink lady",
  "3487": "apples - rave",
  "3284": "apples - red delicious",
  "4172": "apples - rome",
  "3603": "apples - sweet tango",
  "4183": "apples - winesap",
  "4218": "apricots",
  "3044": "apricots - velvet",
  "4520": "artichokes",
  "4080": "asparagus",
  "4522": "asparagus - white",
  "3277": "aspiration",
  "4771": "avocados - green skin",
  "4046": "avocados - hass",
  "4011": "bananas",
  "4535": "beans",
  "4545": "bok choy",
  "4060": "broccoli",
  "3082": "broccoli crowns",
  "4567": "broc-o-flower",
  "4550": "brussel sprout",
  "94539": "bunch beets",
  "4069": "cabbage - green",
  "4552": "cabbage - napa",
  "4554": "cabbage - red",
  "4555": "cabbage - savoy",
  "4255": "cactus pears (tunas)",
  "4883": "candy",
  "4821": "canela (cinnamon sticks)",
  "4319": "cantaloupe - eastern",
  "4050": "cantaloupe - western",
  "4564": "carrots - bulk",
  "4079": "cauliflower",
  "4070": "celery - stalk",
  "4575": "celery hearts",
  "4585": "celery root",
  "4045": "cherries",
  "4258": "cherries - rainier",
  "4927": "chest nuts",
  "4889": "cilantro",
  "4261": "coconut",
  "4260": "coconut - young white",
  "4590": "corn - bi-color",
  "4077": "corn - white",
  "4078": "corn - yellow",
  "4242": "cranberries - bulk",
  "4597": "cucumbers",
  "4596": "cucumbers - pickling",
  "4593": "cucumbers - hot house cukes",
  "3047": "dates - medjool",
  "3040": "dragon fruit",
  "4081": "eggplant",
  "4608": "garlic",
  "94612": "ginger root (organic)",
  "3147": "grape tomatoes (bulk)",
  "4282": "grapefruit - red",
  "4293": "grapefruit - white",
  "4056": "grapes - black seedless",
  "4023": "grapes - red seedless",
  "4022": "grapes - white seedless",
  "4614": "collard greens",
  "4620": "creasy greens",
  "4627": "kale",
  "4616": "mustard greens",
  "4619": "turnip greens",
  "4884": "herbs - fresh arugula",
  "4885": "herbs - fresh basil",
  "4888": "herbs - fresh chives",
  "4891": "herbs - fresh dill",
  "4896": "herbs - fresh mint",
  "4897": "herbs - fresh oregano",
  "4903": "herbs - fresh rosemary",
  "4904": "herbs - fresh sage",
  "4907": "herbs - fresh thyme",
  "4034": "honeydew",
  "94625": "horseradish root (organic)",
  "4505": "jamaica",
  "4626": "jicama",
  "4030": "kiwi fruit",
  "4628": "kohlrabi",
  "4303": "kumquats",
  "4629": "leeks",
  "4304": "lemons - meyer",
  "4053": "lemons",
  "4632": "lettuce - boston",
  "4061": "lettuce - cello head",
  "4604": "lettuce - endive",
  "4543": "lettuce - belgium endive",
  "4605": "lettuce - escarole",
  "4048": "lime",
  "4471": "mandarinquat",
  "4051": "mangoes",
  "4312": "mangoes - ataulfo",
  "4333": "melons - pepino",
  "4653": "mushrooms (bulk)",
  "3276": "name",
  "4036": "nectarines",
  "3035": "nectarines - white",
  "4929": "nuts - loose bulk",
  "4655": "okra",
  "4068": "onions - green",
  "4166": "onions - sweet",
  "4082": "onions - red",
  "4663": "onions - white",
  "4093": "onions - yellow",
  "3110": "oranges - cara cara",
  "4455": "oranges - mandarins",
  "3107": "oranges - navel",
  "3029": "oranges - satsuma",
  "3111": "papayas",
  "3112": "papayas - maradol",
  "4900": "parsley - curly",
  "4901": "parsley - italian",
  "4672": "parsnips",
  "4038": "peaches",
  "3113": "peaches - donut white",
  "4403": "peaches - southern",
  "4401": "peaches - white",
  "4931": "peanuts - raw or green",
  "4416": "pears - anjou",
  "4408": "pears - asian",
  "4409": "pears - bartlett",
  "4413": "pears - bosc",
  "4414": "pears - comice",
  "4415": "pears - red",
  "4501": "pepitas",
  "4065": "green bell peppers",
  "3121": "orange peppers",
  "4688": "red peppers",
  "4689": "yellow peppers",
  "3125": "habanero peppers",
  "4691": "all chile peppers",
  "4427": "persimmons",
  "4820": "piloncillo (brown sugar cane)",
  "4433": "pineapple",
  "4235": "plantain bananas",
  "4040": "plums - black",
  "4442": "plums - lemons",
  "4042": "plums - red",
  "3278": "pluots",
  "3127": "pomegranates",
  "4072": "potato - baking",
  "4073": "potato - red",
  "4091": "potato - sweet",
  "4083": "potato - white",
  "3129": "pummelos",
  "4736": "pumpkins",
  "3134": "pie pumpkins",
  "4738": "radicchio",
  "4089": "radish bunch",
  "4547": "rapini",
  "4745": "rhubarb",
  "4747": "rutabagas",
  "3095": "flowering kale",
  "4662": "shallots",
  "4092": "snow peas",
  "4757": "squash - banana",
  "4751": "squash - acorn gold",
  "4750": "squash - acorn green",
  "4759": "squash - butternut",
  "4761": "squash - chayote",
  "4763": "squash - delicotta",
  "4767": "squash - golden nugget",
  "4768": "squash - hubbard",
  "4769": "squash - kabocha",
  "4776": "squash - spaghetti",
  "4764": "squash - sweet dumpling",
  "4780": "squash - turban",
  "4784": "squash - yellow",
  "4067": "squash - zucchini",
  "4758": "squash - buttercup",
  "4256": "star fruit",
  "4448": "tamarindo",
  "4383": "tangelos (monneola)",
  "4457": "tangerines - pixie",
  "4449": "tangerines - sunburst",
  "4801": "tomatillos",
  "4664": "tomato - cluster",
  "4064": "tomato - green",
  "4799": "tomato - greenhouse",
  "4807": "tomato - heirloom",
  "4800": "tomato - locally grown",
  "4087": "tomato - roma",
  "3423": "tomato - vintage vineripe",
  "4778": "tomato - yellow",
  "4813": "turnip roots",
  "4459": "ugli fruit",
  "3421": "personal watermelon",
  "4376": "slice of watermelon",
  "4031": "watermelon (seeded)",
  "4032": "watermelon (seedless)",
  "4819": "yuca root",
  "320": "bagels",
  "1225": "christmas trees",
  "301": "cookies by bag",
  "305": "cookies by box",
  "300": "self serve donuts",
  "900": "dry ice",
  "315": "muffins",
  "351": "olive bar",
  "309": "rolls",
  "350": "salad bar",
  "328": "whole bean coffee",
  "4950": "almond butter",
  "4951": "organic peanut butter",
  "4948": "honey peanut butter",
  "4947": "dry roast butter",
  "726": "croissants",
  "7202": "wing bar",
  "9901": "peanut"
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
        print("Saving JSON files...")
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

    # query_code from int -> string
    query_code = str(query_code).strip()

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
            problem_child(action)
        else:
            print("Invalid option. Please try again.")


# ===================== MAIN =====================
initData()
mainMenu()