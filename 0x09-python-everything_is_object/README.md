# Objects - Q&A

## Mandatory
### Note: These are easily testable. Do not test. Think about the answer.

### 0-answer.txt
- Name of function that prints type of object

### 1-answer.txt
- Name of function that prints variable identifier

### 2-answer.txt
- Answer to "do a and b point to same object?"
    - a = 89
    - b = 100

### 3-answer.txt
- Answer to "do a and b point to same object?"
    - a = 89
    - b = 89

### 4-answer.txt
- Answer to "do a and b point to same object?"
    - a = 89
    - b = a

### 5-answer.txt
- Answer to "do a and b point to same object?"
    - a = 89
    - b = a + 1

### 6-answer.txt
- Answer to "what do these lines print?"
    - s1 = "Holberton"
    - s2 = s1
    - print(s1 == s2)

### 7-answer.txt
- Answer to "what do these lines print?"
    - s1 = "Holberton"
    - s2 = s1
    - print(s1 is s2)

### 8-answer.txt
- Answer to "what do these lines print?"
    - s1 = "Holberton"
    - s2 = "Holberton"
    - print(s1 == s2)

### 9-answer.txt
- Answer to "what do these lines print?"
    - s1 = "Holberton"
    - s2 = "Holberton"
    - print(s1 is s2)

### 10-answer.txt
- Answer to "what do these lines print?"
    - l1 = [1, 2, 3]
    - l2 = [1, 2, 3]
    - print(l1 == l2)

### 11-answer.txt
- Answer to "what do these lines print?"
    - l1 = [1, 2, 3]
    - l2 = [1, 2, 3]
    - print(l1 is l2)

### 12-answer.txt
- Answer to "what do these lines print?"
    - l1 = [1, 2, 3]
    - l2 = l1
    - print(l1 == l2)

### 13-answer.txt
- Answer to "what do these lines print?"
    - l1 = [1, 2, 3]
    - l2 = l1
    - print(l1 is l2)

### 14-answer.txt
- Answer to "what does this script print?"
    - l1 = [1, 2, 3]
    - l2 = l1
    - l1.append(4)
    - print(l2)

### 15-answer.txt
- Answer to "what does this script print?"
    - l1 = [1, 2, 3]
    - l2 = l1
    - l1 = l1 + [4]
    - print(l2)

### 16-answer.txt
- Answer to "what does this script print?"
    - def increment(n):
        - n += 1
    - a = 1
    - increment(a)
    - print(a)

### 17-answer.txt
- Answer to "what does this script print?"
    - def increment(n):
        - n.append(4)
    - l = [1, 2, 3]
    - increment(l)
    - print(l)

### 18-answer.txt
- Answer to "what does this script print?"
    - def assign_value(n, v):
        - n = v
    - l1 = [1, 2, 3]
    - l2 = [4, 5, 6]
    - assign_value(l1, l2)
    - print(l1)

### 19-copy_list.py
- Returns copy of list
    - Prototype: def copy_list(l):
    - Used with: 19main.py

### 20-answer.txt
- Answer to "is a a tuple?"
    - a = ()

### 21-answer.txt
- Answer to "is a a tuple?"
    - a = (1, 2)

### 22-answer.txt
- Answer to "is a a tuple?"
    - a = (1)

### 23-answer.txt
- Answer to "is a a tuple?"
    - a = (1, )

### 24-answer.txt
- Answer to "what does this script print?"
    - a = (1)
    - b = (1)
    - a is b

### 25-answer.txt
- Answer to "what does this script print?"
    - a = (1, 2)
    - b = (1, 2)
    - a is b

### 26-answer.txt
- Answer to "what does this script print?"
    - a = ()
    - b = ()
    - a is b

### 27-answer.txt
- Answer to "will the id remain the same?"
    - id(a)
        - 139926795932424
    - print(a)
        - [1, 2, 3, 4]
    - a = a + [5]
    - id(a)

### 28-answer.txt
- Answer to "will the id remain the same?"
    - a
        - [1, 2, 3]
    - id(a)
        - 139926795932424
    - a += [4]
    - id(a)
