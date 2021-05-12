# File I/O and JSON

## Mandatory

### 0-read_file.py
- Reads text file and prints it to stdout
    - Prototype: def read_file(filename=""):
    - Used with: 0main.py

### 1-write_file.py
- Writes string to text file
    - Prototype: def write_file(filename="", text=""):
    - Used with 1main.py

### 2-append_write.py
- Appends string to end of text file
    - def append_write(filename="", text=""):
    - Used with 2main.py

### 3-to_json_string.py
- Returns JSON representation of string
    - Prototype: def to_json_string(my_obj):
    - Used with 3main.py

### 4-from_json_string.py
- Returns object representated by JSON string
    - Prototype: def from_json_string(my_str):
    - Used with 4main.py

### 5-save_to_json_file.py
- Writes object to text file using JSON representation
    - Prototype: def save_to_json_file(my_obj, filename):
    - Used with 5main.py

### 6-load_from_json_file.py
- Creates object from JSON file
    - Prototype: def load_from_json_file(filename):
    - Used with 6main.py

### 7-add_item.py
- Adds all arguments to list and saves to file
    - Imports:
        - 5-save_to_json_file.py
        - 6-load_from_json_file.py

### 8-class_to_json.py
- Returns dictionary description for JSON object
    - Prototype: def class_to_json(obj):
    - Used with: 8main.py, 8main_2.py 8-my_class.py, 8-my_class_2.py

### 9-student.py
- Defines Student class with public attributes first_name, last_name, and age
    - New method prototypes:
        - def __init__(self, first_name, last_name, age):
        - def to_json(self):
    - Used with: 9main.py

### 10-student.py
- ** Add explanation later
    - Used with: 10main.py
    - Adds onto: 9-student.py

### 11-student.py
- Replace all attributes of Student instance with JSON
    - New method prototype: def reload_from_json(self, json):
    - Used with: 11main.py
    - Adds onto: 10-student.py

### 12-pascal_triangle.py
- Technical interview preparation
- Return list of integers representing Pascal's triangle
    - Prototype: def pascal_triangle(n):
    - Used with: 12main.py

## Learning Objectives

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure