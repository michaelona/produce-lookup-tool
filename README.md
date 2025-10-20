# Produce Lookup Tool

A simple and easy CLI tool to lookup common grocery produce codes (PLU). Search, add, edit, or remove entries with custom databases for your own items.

---

## ✨ Features

- Search by PLU code or produce name (exact, partial, or fuzzy matches)
- Add new items safely and prevent duplicates
- Edit existing items (name or code)
- Display saved items in neatly and in alphabetical order
- Support for custom JSON databases
- Fuzzy search using `difflib`
- Error handling ensures safe operations

---

## 💾 Installation

1. Clone the repository or download the latest ZIP release.
2. Navigate into the directory:
   ```cd produce-lookup-tool```
3. Run the program:
   ```python pluSearch.py``` or ```python3 pluSearch.py```

---

## ⌨️ Usage
- Follow the main menu functions to search, add, edit, remove, or display items.
- First-time users on Windows/macOS can choose to create a custom database. Mobile users are restricted to the default dataset.

#

### **Main Menu Functions:**
(\* = Available on mobile)
1. **Search\*** — Searches the database after entering a produce name or PLU code. Supports partial and fuzzy matches. Returns the 

2. **Add Item** — Adds a new item entry given a name or PLU code. Checks for duplicates before writing to the database.

3. **Remove Item** — Deletes an item from the database given an exact name or PLU code.

4. **Edit Item** — Update an existing entry's name, code, or both.

5. **Show All\*** — Prints the entire PLU database in a formatted table.

6. **Reset to Defaults** — Restores both JSON databases to the original built-in default values.

7. **Quit\*** — Saves any changes to custom databases (if enabled) and exits the program safely.


## 📁 File Structure

```
produceFinder/
│
├── pluSearch.py/        # Main program file
├── codeToName.json      # Optional custom database
├── nameToCode.json      # Optional custom database
└── README.md           
```