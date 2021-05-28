# Object-Relational Mapping and MySQLAlchemy

## Mandatory

### 0-select_states.py
- Displays all states from database
    - Uses: 0-select_states.sql

### 1-filter_states.py
- Displays all states starting with N
    - Uses: 0-select_states.sql

### 2-my_filter_states.py
- Displays all values where name matches argument
    - Uses: 0-select_states.sql

### 3-my_safe_filter_states.py
- Displays all values where name matches argument but safe from MySQL injections

### 4-cities_by_state.py
- Displays all cities from database
    - Uses: 4-cities_by_state.sql

### 5-filter_cities.py
- Displays all cities where argument matches
    - Uses: 4-cities_by_state.sql

### model_state.py
- Defines State class that inherits from Base class and links to states table
    - Uses: 6-model_state.sql

### 7-model_state_fetch_all.py
- Displays all State objects from database
    - Uses: 7-model_state_fetch_all.sql

### 8-model_state_fetch_first.py
- Displays first State object

### 9-model_state_filter_a.py
- Displays all State objects that contain letter 'a'

### 10-model_state_my_get.py
- Displays State object where argument matches

### 11-model_state_insert.py
- Adds State object to database

### 12-model_state_update_id_2.py
- Changes/updates State object based on id

### 13-model_state_delete_a.py
- Deletes State objects that contain letter 'a'

### 14-model_city_fetch_by_state.py
- Defines City class that inherits from Base class and links to cities table
    - Uses:
        - 14-model_city_fetch_by_state.sql
        - model_city.py

## Learning Objectives
- Why Python programming is awesome
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table
