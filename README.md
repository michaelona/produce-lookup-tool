# Produce Lookup Tool

An easy tool to lookup common grocery produce codes (PLU). Search, add, edit, or remove items with custom databases.

---

### Features

- Search by produce name or PLU code (**exact, partial, or fuzzy matches**)
- Add new items safely, preventing duplicates
- Edit existing items (name or code)
- Remove items with confirmation prompts
- Display all items in a formatted table
- Support for **custom JSON databases** (Windows/macOS only)
- Fuzzy search using `difflib`
- Error handling ensures safe operations

---

### Installation

1. Clone the repository:
2. Navigate into the directory:
   ```cd produce-lookup-tool```
3. Run the program:
   ```python pluSearch.py``` or ```python3 pluSearch.py```

---

### Usage
- Follow the interactive menu to search, add, edit, remove, or display items.
- First-time users on Windows/macOS will be prompted to create a custom database. Mobile users will use default values.

### File Structure

```
produceFinder/
│
├── pluSearch.py/        # Main program file
├── codeToName.json      # Optional custom database
├── nameToCode.json      # Optional custom database
└── README.md            # This documentation
```