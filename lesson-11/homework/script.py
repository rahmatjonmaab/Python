python -m venv myenv
source myenv/bin/activate  

myenv\Scripts\activate  

pip install requests
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
  def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count
  geometry/
    __init__.py
    circle.py
import math

def calculate_area(radius):
    return math.pi * radius ** 2

def calculate_circumference(radius):
    return 2 * math.pi * radius
  file_operations/
    __init__.py
    file_reader.py
    file_writer.py
def write_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content)
