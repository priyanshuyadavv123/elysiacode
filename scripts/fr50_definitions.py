# scripts/fr50_definitions.py
# Complete verified definitions for Functions & Recursion: 50 Questions (FR-01 to FR-50)
# Organized into 10 progressive levels (Levels 1-5: Functions, Levels 6-10: Recursion)

FR50_QUESTIONS_RAW = [
    # =========================================================================
    # Functions - Level 1: Defining and calling a function (FR-01 to FR-06)
    # =========================================================================
    {
        "q_num": 1,
        "title": "Say Hello Three Times",
        "level": "Level 1 of 10: Defining and calling a function",
        "subtopic": "Defining and calling a function",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A new student is learning how a function works. The function is written once and called again and again.",
        "task": "Define a function say_hello() that prints Hello, Python learner! Call it three times.",
        "sample_input": "",
        "expected_output": "Hello, Python learner!\nHello, Python learner!\nHello, Python learner!",
        "hint": "Write def say_hello(): and indent the print line under it. Then call say_hello() three times.",
        "starter_code": """# [FR-01] Say Hello Three Times
# Level 1 of 10: Defining and calling a function
# TODO: Define say_hello() and call it three times:
def say_hello():
    pass
""",
        "solution_code": """def say_hello():
    print("Hello, Python learner!")

say_hello()
say_hello()
say_hello()"""
    },
    {
        "q_num": 2,
        "title": "Separator Line",
        "level": "Level 1 of 10: Defining and calling a function",
        "subtopic": "Functions that print",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A report printer uses a separator line between sections.",
        "task": "Define print_line() that prints 10 dashes. Print a separator line, the title Welcome, call print_line(), print the message Start, then call print_line() again.",
        "sample_input": "",
        "expected_output": "----------\nWelcome\n----------\nStart\n----------",
        "hint": "Use the string multiplication trick: '-' * 10.",
        "starter_code": """# [FR-02] Separator Line
# Level 1 of 10: Functions that print
# TODO: Define print_line() and print the report layout matching Sample Output:
def print_line():
    pass
""",
        "solution_code": """def print_line():
    print("-" * 10)

print_line()
print("Welcome")
print_line()
print("Start")
print_line()"""
    },
    {
        "q_num": 3,
        "title": "Count to Five",
        "level": "Level 1 of 10: Defining and calling a function",
        "subtopic": "Calling a function with a loop",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A teacher wants to show students a counting routine that can be reused for a second class.",
        "task": "Define count_to_five() that prints the numbers 1 to 5, one per line. Call it, print a line with --, then call it again.",
        "sample_input": "",
        "expected_output": "1\n2\n3\n4\n5\n--\n1\n2\n3\n4\n5",
        "hint": "Put a for loop inside the function body.",
        "starter_code": """# [FR-03] Count to Five
# Level 1 of 10: Calling a function with a loop
# TODO: Define count_to_five() and call it twice with '--' in between:
def count_to_five():
    pass
""",
        "solution_code": """def count_to_five():
    for i in range(1, 6):
        print(i)

count_to_five()
print("--")
count_to_five()"""
    },
    {
        "q_num": 4,
        "title": "Shop Menu",
        "level": "Level 1 of 10: Defining and calling a function",
        "subtopic": "Functions that show a menu",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A small shop kiosk shows a menu and then reads the customer's choice.",
        "task": "Define show_menu() that prints three lines: 1. Add item, 2. View items, 3. Exit. Call show_menu(), read the customer's choice, and print Selected: followed by the choice.",
        "sample_input": "2",
        "expected_output": "1. Add item\n2. View items\n3. Exit\nSelected: 2",
        "hint": "The function only prints. The choice is read with input() outside the function.",
        "starter_code": """# [FR-04] Shop Menu
# Level 1 of 10: Functions that show a menu
def show_menu():
    # TODO: Print the three menu lines
    pass

# TODO: Call show_menu(), read choice with input(), and print Selected: <choice>
""",
        "solution_code": """def show_menu():
    print("1. Add item")
    print("2. View items")
    print("3. Exit")

show_menu()
choice = input().strip()
print(f"Selected: {choice}")"""
    },
    {
        "q_num": 5,
        "title": "Table Header",
        "level": "Level 1 of 10: Defining and calling a function",
        "subtopic": "Functions that print headings",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A bill printer prints a fixed header before each row.",
        "task": "Define print_header() that prints Item | Price and then -----|------. Call it once, then print the row Pen | 10.",
        "sample_input": "",
        "expected_output": "Item | Price\n-----|------\nPen | 10",
        "hint": "Each print() call prints one line.",
        "starter_code": """# [FR-05] Table Header
# Level 1 of 10: Functions that print headings
# TODO: Define print_header() and print the table row:
def print_header():
    pass
""",
        "solution_code": """def print_header():
    print("Item | Price")
    print("-----|------")

print_header()
print("Pen | 10")"""
    },
    {
        "q_num": 6,
        "title": "Ask for a Name",
        "level": "Level 1 of 10: Defining and calling a function",
        "subtopic": "Functions that read input",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A kiosk greets two visitors one after another, using the same function each time.",
        "task": "Define ask_name() that reads a name with input() and prints Hi NAME!. Call the function twice.",
        "sample_input": "Asha\nRavi",
        "expected_output": "Hi Asha!\nHi Ravi!",
        "hint": "Read the name inside the function, then print it.",
        "starter_code": """# [FR-06] Ask for a Name
# Level 1 of 10: Functions that read input
def ask_name():
    # TODO: Read name with input() and print Hi <name>!
    pass

ask_name()
ask_name()
""",
        "solution_code": """def ask_name():
    name = input().strip()
    print(f"Hi {name}!")

ask_name()
ask_name()"""
    },

    # =========================================================================
    # Functions - Level 2: Parameters and arguments (FR-07 to FR-13)
    # =========================================================================
    {
        "q_num": 7,
        "title": "Greet a Person",
        "level": "Level 2 of 10: Parameters and arguments",
        "subtopic": "One parameter",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A welcome desk greets each visitor by name.",
        "task": "Define greet(name) that prints Hello, NAME!. Read a name and call greet with it.",
        "sample_input": "Asha",
        "expected_output": "Hello, Asha!",
        "hint": "The value you pass in the brackets becomes the parameter name inside the function.",
        "starter_code": """# [FR-07] Greet a Person
# Level 2 of 10: Parameters and arguments
def greet(name):
    pass

visitor_name = input().strip()
# TODO: Call greet with visitor_name
""",
        "solution_code": """def greet(name):
    print(f"Hello, {name}!")

visitor_name = input().strip()
greet(visitor_name)"""
    },
    {
        "q_num": 8,
        "title": "Rectangle Area",
        "level": "Level 2 of 10: Parameters and arguments",
        "subtopic": "Two parameters",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A carpenter measures a board and needs its area.",
        "task": "Define rectangle_area(length, width) that prints Area: followed by the area. Read the length and width, then call the function.",
        "sample_input": "5\n8",
        "expected_output": "Area: 40",
        "hint": "Convert the inputs to int before passing them, then multiply inside the function.",
        "starter_code": """# [FR-08] Rectangle Area
# Level 2 of 10: Two parameters
def rectangle_area(length, width):
    pass

length = int(input())
width = int(input())
# TODO: Call rectangle_area(length, width)
""",
        "solution_code": """def rectangle_area(length, width):
    print(f"Area: {length * width}")

length = int(input())
width = int(input())
rectangle_area(length, width)"""
    },
    {
        "q_num": 9,
        "title": "Describe a Pet",
        "level": "Level 2 of 10: Parameters and arguments",
        "subtopic": "Positional arguments",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A pet register asks for the type of animal and its name.",
        "task": "Define describe_pet(animal, name) that prints I have a ANIMAL named NAME. Read the animal and the name, then call describe_pet with them in that order.",
        "sample_input": "dog\nTommy",
        "expected_output": "I have a dog named Tommy.",
        "hint": "The first argument goes to the first parameter, the second to the second.",
        "starter_code": """# [FR-09] Describe a Pet
# Level 2 of 10: Positional arguments
def describe_pet(animal, name):
    pass

animal = input().strip()
name = input().strip()
# TODO: Call describe_pet(animal, name)
""",
        "solution_code": """def describe_pet(animal, name):
    print(f"I have a {animal} named {name}.")

animal = input().strip()
name = input().strip()
describe_pet(animal, name)"""
    },
    {
        "q_num": 10,
        "title": "Multiply Two Numbers",
        "level": "Level 2 of 10: Parameters and arguments",
        "subtopic": "Calculations inside a function",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A bakery needs a quick multiplication helper for recipe scaling.",
        "task": "Define multiply(a, b) that prints the product of a and b. Read two numbers and call multiply.",
        "sample_input": "6\n7",
        "expected_output": "42",
        "hint": "The function does the work and prints the answer.",
        "starter_code": """# [FR-10] Multiply Two Numbers
# Level 2 of 10: Calculations inside a function
def multiply(a, b):
    pass

a = int(input())
b = int(input())
# TODO: Call multiply(a, b)
""",
        "solution_code": """def multiply(a, b):
    print(a * b)

a = int(input())
b = int(input())
multiply(a, b)"""
    },
    {
        "q_num": 11,
        "title": "Order Total",
        "level": "Level 2 of 10: Parameters and arguments",
        "subtopic": "Argument order",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A cashier shows each bill line as quantity x price.",
        "task": "Define show_total(quantity, price) that prints QUANTITY x PRICE = TOTAL. Read the quantity and then the price, and call show_total in that order.",
        "sample_input": "3\n25",
        "expected_output": "3 x 25 = 75",
        "hint": "Order matters: pass quantity first because the function expects it first.",
        "starter_code": """# [FR-11] Order Total
# Level 2 of 10: Argument order
def show_total(quantity, price):
    pass

quantity = int(input())
price = int(input())
# TODO: Call show_total(quantity, price)
""",
        "solution_code": """def show_total(quantity, price):
    print(f"{quantity} x {price} = {quantity * price}")

quantity = int(input())
price = int(input())
show_total(quantity, price)"""
    },
    {
        "q_num": 12,
        "title": "Describe a Book",
        "level": "Level 2 of 10: Parameters and arguments",
        "subtopic": "Keyword arguments",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A library catalogue calls the same function with the arguments named.",
        "task": 'Define describe_book(title, author) that prints TITLE by AUTHOR. Call it with author="R.K. Narayan" and title="Malgudi Days".',
        "sample_input": "",
        "expected_output": "Malgudi Days by R.K. Narayan",
        "hint": "Write the name of each parameter followed by = and the value when you call the function.",
        "starter_code": """# [FR-12] Describe a Book
# Level 2 of 10: Keyword arguments
def describe_book(title, author):
    pass

# TODO: Call describe_book using keyword arguments author="R.K. Narayan" and title="Malgudi Days"
""",
        "solution_code": """def describe_book(title, author):
    print(f"{title} by {author}")

describe_book(author="R.K. Narayan", title="Malgudi Days")"""
    },
    {
        "q_num": 13,
        "title": "Average of Three Marks",
        "level": "Level 2 of 10: Parameters and arguments",
        "subtopic": "Parameters with calculations",
        "difficulty": "Beginner",
        "xp": 35,
        "scenario": "A teacher wants the average of three test marks using a reusable function.",
        "task": "Define average_of_three(a, b, c) that prints the average with two decimal places. Read three marks and call the function.",
        "sample_input": "80\n90\n75",
        "expected_output": "Average: 81.67",
        "hint": "Add the three parameters and divide by 3.",
        "starter_code": """# [FR-13] Average of Three Marks
# Level 2 of 10: Parameters with calculations
def average_of_three(a, b, c):
    pass

a = int(input())
b = int(input())
c = int(input())
# TODO: Call average_of_three(a, b, c)
""",
        "solution_code": """def average_of_three(a, b, c):
    avg = (a + b + c) / 3
    print(f"Average: {avg:.2f}")

a = int(input())
b = int(input())
c = int(input())
average_of_three(a, b, c)"""
    },

    # =========================================================================
    # Functions - Level 3: Return values (FR-14 to FR-20)
    # =========================================================================
    {
        "q_num": 14,
        "title": "Square Returned",
        "level": "Level 3 of 10: Return values",
        "subtopic": "Returning a value",
        "difficulty": "Beginner",
        "xp": 35,
        "scenario": "A maths app uses a function that gives the square back to the program, not just prints it.",
        "task": "Define square(n) that returns n multiplied by n. Read a number, call square, and print the returned value.",
        "sample_input": "7",
        "expected_output": "49",
        "hint": "Use return instead of print inside the function.",
        "starter_code": """# [FR-14] Square Returned
# Level 3 of 10: Return values
def square(n):
    pass

n = int(input())
# TODO: Print the returned value of square(n)
""",
        "solution_code": """def square(n):
    return n * n

n = int(input())
print(square(n))"""
    },
    {
        "q_num": 15,
        "title": "Even or Odd",
        "level": "Level 3 of 10: Return values",
        "subtopic": "Returning True or False",
        "difficulty": "Beginner",
        "xp": 35,
        "scenario": "A quiz uses a helper that answers yes or no to a question about a number.",
        "task": "Define is_even(n) that returns True if n is even, otherwise False. Read a number, then print Even if is_even returns True, otherwise print Odd.",
        "sample_input": "10",
        "expected_output": "Even",
        "hint": "The expression n % 2 == 0 is already True or False, so return it directly.",
        "starter_code": """# [FR-15] Even or Odd
# Level 3 of 10: Returning True or False
def is_even(n):
    pass

n = int(input())
# TODO: Print Even or Odd based on is_even(n)
""",
        "solution_code": """def is_even(n):
    return n % 2 == 0

n = int(input())
if is_even(n):
    print("Even")
else:
    print("Odd")"""
    },
    {
        "q_num": 16,
        "title": "Larger of Two",
        "level": "Level 3 of 10: Return values",
        "subtopic": "Returning from a comparison",
        "difficulty": "Beginner",
        "xp": 35,
        "scenario": "A sports app picks the higher of two scores.",
        "task": "Define larger(a, b) that returns the bigger number. Read two numbers and print the value returned.",
        "sample_input": "15\n42",
        "expected_output": "42",
        "hint": "Use an if statement with two return statements, or use the max-style comparison.",
        "starter_code": """# [FR-16] Larger of Two
# Level 3 of 10: Returning from a comparison
def larger(a, b):
    pass

a = int(input())
b = int(input())
# TODO: Call larger(a, b) and print the result
""",
        "solution_code": """def larger(a, b):
    if a > b:
        return a
    return b

a = int(input())
b = int(input())
print(larger(a, b))"""
    },
    {
        "q_num": 17,
        "title": "Celsius to Fahrenheit",
        "level": "Level 3 of 10: Return values",
        "subtopic": "Returning a decimal value",
        "difficulty": "Beginner",
        "xp": 35,
        "scenario": "A weather station reports in Celsius, but a traveller wants Fahrenheit.",
        "task": "Define celsius_to_fahrenheit(c) that returns c * 9 / 5 + 32. Read a temperature and print Fahrenheit: with one decimal place.",
        "sample_input": "25",
        "expected_output": "Fahrenheit: 77.0",
        "hint": "Keep the calculation inside the function and only format the result in the print statement.",
        "starter_code": """# [FR-17] Celsius to Fahrenheit
# Level 3 of 10: Returning a decimal value
def celsius_to_fahrenheit(c):
    pass

c = float(input())
# TODO: Print Fahrenheit: followed by value with 1 decimal place
""",
        "solution_code": """def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

c = float(input())
print(f"Fahrenheit: {celsius_to_fahrenheit(c):.1f}")"""
    },
    {
        "q_num": 18,
        "title": "Minimum and Maximum",
        "level": "Level 3 of 10: Return values",
        "subtopic": "Returning several values",
        "difficulty": "Intermediate",
        "xp": 45,
        "scenario": "A sensor reports three readings, and the program needs the lowest and highest.",
        "task": "Define min_max(a, b, c) that returns two values: the minimum and the maximum. Read three numbers, store both returned values, and print them.",
        "sample_input": "4\n9\n2",
        "expected_output": "Min: 2\nMax: 9",
        "hint": "return value1, value2 sends back two values. Store them with two names on the left side.",
        "starter_code": """# [FR-18] Minimum and Maximum
# Level 3 of 10: Returning several values
def min_max(a, b, c):
    pass

a = int(input())
b = int(input())
c = int(input())
# TODO: Unpack returned min & max and print them
""",
        "solution_code": """def min_max(a, b, c):
    return min(a, b, c), max(a, b, c)

a = int(input())
b = int(input())
c = int(input())
mn, mx = min_max(a, b, c)
print(f"Min: {mn}")
print(f"Max: {mx}")"""
    },
    {
        "q_num": 19,
        "title": "Discount then GST",
        "level": "Level 3 of 10: Return values",
        "subtopic": "Using a returned value",
        "difficulty": "Intermediate",
        "xp": 45,
        "scenario": "A shop gives a discount first, then adds 18% GST on the discounted price.",
        "task": "Define final_price(price, percent) that returns the price after the discount. Read the price and the discount percent. Print the price after discount with two decimals, then the amount with 18% GST (using the returned value).",
        "sample_input": "1000\n20",
        "expected_output": "Price after discount: 800.00\nAmount with 18% GST: 944.00",
        "hint": "Store the result of final_price in a variable, then use that variable in the next calculation.",
        "starter_code": """# [FR-19] Discount then GST
# Level 3 of 10: Using a returned value
def final_price(price, percent):
    pass

price = float(input())
percent = float(input())
# TODO: Call final_price and print discounted price and amount with 18% GST
""",
        "solution_code": """def final_price(price, percent):
    return price * (1 - percent / 100)

price = float(input())
percent = float(input())
discounted = final_price(price, percent)
with_gst = discounted * 1.18
print(f"Price after discount: {discounted:.2f}")
print(f"Amount with 18% GST: {with_gst:.2f}")"""
    },
    {
        "q_num": 20,
        "title": "Total with Tax",
        "level": "Level 3 of 10: Return values",
        "subtopic": "Chaining functions",
        "difficulty": "Intermediate",
        "xp": 45,
        "scenario": "A billing system calculates a total, then passes it to a tax function.",
        "task": "Define total_cost(price, qty) that returns price times quantity, and add_tax(amount) that returns amount times 1.18. Read the price and quantity, print the base total, then print the total with tax to two decimals.",
        "sample_input": "200\n3",
        "expected_output": "Base total: 600\nTotal with tax: 708.00",
        "hint": "Call add_tax with the value returned by total_cost.",
        "starter_code": """# [FR-20] Total with Tax
# Level 3 of 10: Chaining functions
def total_cost(price, qty):
    pass

def add_tax(amount):
    pass

price = int(input())
qty = int(input())
# TODO: Print Base total and Total with tax
""",
        "solution_code": """def total_cost(price, qty):
    return price * qty

def add_tax(amount):
    return amount * 1.18

price = int(input())
qty = int(input())
base = total_cost(price, qty)
final_amt = add_tax(base)
print(f"Base total: {base}")
print(f"Total with tax: {final_amt:.2f}")"""
    },

    # =========================================================================
    # Functions - Level 4: Default and keyword arguments (FR-21 to FR-24)
    # =========================================================================
    {
        "q_num": 21,
        "title": "Greeting with a Default",
        "level": "Level 4 of 10: Default and keyword arguments",
        "subtopic": "Default arguments",
        "difficulty": "Beginner",
        "xp": 40,
        "scenario": "A reception desk says Hello by default, but sometimes uses a different greeting.",
        "task": 'Define greet(name, greeting="Hello") that prints GREETING, NAME!. Read a name, call greet with only the name, then call it with the greeting Good morning.',
        "sample_input": "Asha",
        "expected_output": "Hello, Asha!\nGood morning, Asha!",
        "hint": "Give the parameter a default value with = inside def. Leave the argument out to use the default.",
        "starter_code": """# [FR-21] Greeting with a Default
# Level 4 of 10: Default arguments
def greet(name, greeting="Hello"):
    pass

name = input().strip()
# TODO: Call greet(name) and greet(name, "Good morning")
""",
        "solution_code": """def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

name = input().strip()
greet(name)
greet(name, "Good morning")"""
    },
    {
        "q_num": 22,
        "title": "Bill with Default Tax",
        "level": "Level 4 of 10: Default and keyword arguments",
        "subtopic": "Default parameter values",
        "difficulty": "Beginner",
        "xp": 40,
        "scenario": "A restaurant adds a standard 5% tax, but a special bill can use 12%.",
        "task": "Define calculate_bill(amount, tax=5) that returns amount plus tax percentage. Print the bill with the default tax, then the bill with tax=12 as a keyword argument. Show two decimals.",
        "sample_input": "",
        "expected_output": "Bill with default tax: 1050.00\nBill with 12% tax: 1120.00",
        "hint": "Use calculate_bill(1000) for the default and calculate_bill(1000, tax=12) for the other.",
        "starter_code": """# [FR-22] Bill with Default Tax
# Level 4 of 10: Default parameter values
def calculate_bill(amount, tax=5):
    pass

# TODO: Print Bill with default tax (1000) and Bill with 12% tax (1000, tax=12)
""",
        "solution_code": """def calculate_bill(amount, tax=5):
    return amount + (amount * tax / 100)

print(f"Bill with default tax: {calculate_bill(1000):.2f}")
print(f"Bill with 12% tax: {calculate_bill(1000, tax=12):.2f}")"""
    },
    {
        "q_num": 23,
        "title": "Notice Board Message",
        "level": "Level 4 of 10: Default and keyword arguments",
        "subtopic": "Several defaults with keywords",
        "difficulty": "Intermediate",
        "xp": 45,
        "scenario": "A notice system sends messages from System by default, but can show the sender and an urgent flag.",
        "task": 'Define send_message(text, sender="System", urgent=False). If urgent is True, add [URGENT] at the start. Print the message in the form [SENDER] TEXT. Call it once with only the text and once with sender="Accounts" and urgent=True.',
        "sample_input": "",
        "expected_output": "[System] Server restart\n[URGENT] [Accounts] Fee due",
        "hint": "Build a prefix string first: '[URGENT] ' if urgent else ''.",
        "starter_code": """# [FR-23] Notice Board Message
# Level 4 of 10: Several defaults with keywords
def send_message(text, sender="System", urgent=False):
    pass

# TODO: Call send_message("Server restart") and send_message("Fee due", sender="Accounts", urgent=True)
""",
        "solution_code": """def send_message(text, sender="System", urgent=False):
    prefix = "[URGENT] " if urgent else ""
    print(f"{prefix}[{sender}] {text}")

send_message("Server restart")
send_message("Fee due", sender="Accounts", urgent=True)"""
    },
    {
        "q_num": 24,
        "title": "Create a Profile",
        "level": "Level 4 of 10: Default and keyword arguments",
        "subtopic": "Keyword arguments in any order",
        "difficulty": "Beginner",
        "xp": 40,
        "scenario": "A form stores a name and age. The city is Patna unless the user chooses a different one.",
        "task": 'Define create_profile(name, age, city="Patna") that prints Name: NAME | Age: AGE | City: CITY. Read the name and age, then call the function with age= and name= given as keywords (the city uses its default).',
        "sample_input": "Asha\n21",
        "expected_output": "Name: Asha | Age: 21 | City: Patna",
        "hint": "Keyword arguments let you list name and age in any order.",
        "starter_code": """# [FR-24] Create a Profile
# Level 4 of 10: Keyword arguments in any order
def create_profile(name, age, city="Patna"):
    pass

user_name = input().strip()
user_age = int(input())
# TODO: Call create_profile with keyword arguments age= and name=
""",
        "solution_code": """def create_profile(name, age, city="Patna"):
    print(f"Name: {name} | Age: {age} | City: {city}")

user_name = input().strip()
user_age = int(input())
create_profile(age=user_age, name=user_name)"""
    },

    # =========================================================================
    # Functions - Level 5: Scope and changing data (FR-25 to FR-28)
    # =========================================================================
    {
        "q_num": 25,
        "title": "Local versus Global",
        "level": "Level 5 of 10: Scope and changing data",
        "subtopic": "Local variables",
        "difficulty": "Intermediate",
        "xp": 45,
        "scenario": "A program has a variable total outside the function, and the function creates its own total.",
        "task": "Set total = 5 at the top. Define calculate() that sets its own total = 100 and prints Inside: followed by it. Call calculate(), then print Outside: followed by the outer total.",
        "sample_input": "",
        "expected_output": "Inside: 100\nOutside: 5",
        "hint": "Assignment inside the function creates a new local variable. It does not change the outer one.",
        "starter_code": """# [FR-25] Local versus Global
# Level 5 of 10: Local variables
total = 5

def calculate():
    pass

calculate()
print(f"Outside: {total}")
""",
        "solution_code": """total = 5

def calculate():
    total = 100
    print(f"Inside: {total}")

calculate()
print(f"Outside: {total}")"""
    },
    {
        "q_num": 26,
        "title": "Visitor Counter",
        "level": "Level 5 of 10: Scope and changing data",
        "subtopic": "The global keyword",
        "difficulty": "Intermediate",
        "xp": 45,
        "scenario": "A website counts visits. Every call to visit() should add one to the same counter.",
        "task": "Set counter = 0. Define visit() that uses the global keyword to add 1 to counter. Call it three times, then print Counter: followed by the value.",
        "sample_input": "",
        "expected_output": "Counter: 3",
        "hint": "Write global counter as the first line of the function before you change it.",
        "starter_code": """# [FR-26] Visitor Counter
# Level 5 of 10: The global keyword
counter = 0

def visit():
    pass

# TODO: Call visit() three times and print Counter: <counter>
""",
        "solution_code": """counter = 0

def visit():
    global counter
    counter += 1

visit()
visit()
visit()
print(f"Counter: {counter}")"""
    },
    {
        "q_num": 27,
        "title": "Add Items to a Cart",
        "level": "Level 5 of 10: Scope and changing data",
        "subtopic": "Changing a list inside a function",
        "difficulty": "Intermediate",
        "xp": 45,
        "scenario": "A shopping cart is a list. A function adds items to the cart that the main program owns.",
        "task": "Create an empty cart list. Define add_item(cart, item) that appends the item to the list. Read two item names, add both with the function, and print the cart.",
        "sample_input": "pen\nbook",
        "expected_output": "['pen', 'book']",
        "hint": "Lists change in place, so the function's append affects the same list the caller has.",
        "starter_code": """# [FR-27] Add Items to a Cart
# Level 5 of 10: Changing a list inside a function
def add_item(cart, item):
    pass

cart = []
item1 = input().strip()
item2 = input().strip()
# TODO: Add both items using add_item and print cart
""",
        "solution_code": """def add_item(cart, item):
    cart.append(item)

cart = []
item1 = input().strip()
item2 = input().strip()
add_item(cart, item1)
add_item(cart, item2)
print(cart)"""
    },
    {
        "q_num": 28,
        "title": "Sorted Copy",
        "level": "Level 5 of 10: Scope and changing data",
        "subtopic": "Returning a new list",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A teacher wants a sorted list of scores, but the original order of the scores must be kept for the record.",
        "task": "Define sorted_copy(values) that returns a new sorted list and leaves the original unchanged. Read numbers on one line, call the function, then print the original list and the sorted list.",
        "sample_input": "5 2 9",
        "expected_output": "Original: [5, 2, 9]\nSorted: [2, 5, 9]",
        "hint": "sorted(values) returns a new list. list.sort() would change the original, so avoid it here.",
        "starter_code": """# [FR-28] Sorted Copy
# Level 5 of 10: Returning a new list
def sorted_copy(values):
    pass

nums = list(map(int, input().split()))
# TODO: Call sorted_copy(nums) and print Original and Sorted lists
""",
        "solution_code": """def sorted_copy(values):
    return sorted(values)

nums = list(map(int, input().split()))
sorted_nums = sorted_copy(nums)
print(f"Original: {nums}")
print(f"Sorted: {sorted_nums}")"""
    },

    # =========================================================================
    # Recursion - Level 1 (Level 6): Base case and recursive call (FR-29 to FR-33)
    # =========================================================================
    {
        "q_num": 29,
        "title": "Countdown to Liftoff",
        "level": "Level 6 of 10: Recursion - Base case and recursive call",
        "subtopic": "Recursive countdown",
        "difficulty": "Beginner",
        "xp": 45,
        "scenario": "A rocket control program counts down by calling the same function with a smaller number each time.",
        "task": "Define countdown(n) recursively. If n is 0, print Liftoff! and stop. Otherwise print n and call countdown(n - 1). Read n and call the function.",
        "sample_input": "5",
        "expected_output": "5\n4\n3\n2\n1\nLiftoff!",
        "hint": "The base case is n == 0. The recursive call uses n - 1, which moves towards the base case.",
        "starter_code": """# [FR-29] Countdown to Liftoff
# Level 6 of 10: Recursion - Base case and recursive call
def countdown(n):
    pass

n = int(input())
countdown(n)
""",
        "solution_code": """def countdown(n):
    if n == 0:
        print("Liftoff!")
        return
    print(n)
    countdown(n - 1)

n = int(input())
countdown(n)"""
    },
    {
        "q_num": 30,
        "title": "Count Up",
        "level": "Level 6 of 10: Recursion - Base case and recursive call",
        "subtopic": "Recursion before and after printing",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A student compares printing before the recursive call with printing after it.",
        "task": "Define count_up(n) recursively: if n is 0 return. Otherwise call count_up(n - 1) first, then print n. Read n and call the function.",
        "sample_input": "4",
        "expected_output": "1\n2\n3\n4",
        "hint": "The print comes after the recursive call, so the smallest number is printed first.",
        "starter_code": """# [FR-30] Count Up
# Level 6 of 10: Recursion before and after printing
def count_up(n):
    pass

n = int(input())
count_up(n)
""",
        "solution_code": """def count_up(n):
    if n == 0:
        return
    count_up(n - 1)
    print(n)

n = int(input())
count_up(n)"""
    },
    {
        "q_num": 31,
        "title": "Sum from 1 to n",
        "level": "Level 6 of 10: Recursion - Base case and recursive call",
        "subtopic": "Recursive sum",
        "difficulty": "Beginner",
        "xp": 45,
        "scenario": "A teacher wants to add all numbers from 1 to n using a recursive function.",
        "task": "Define sum_to(n) that returns n + sum_to(n - 1), with base case sum_to(0) = 0. Read n and print the result.",
        "sample_input": "10",
        "expected_output": "55",
        "hint": "Each call adds n and asks for the sum of the smaller numbers.",
        "starter_code": """# [FR-31] Sum from 1 to n
# Level 6 of 10: Recursive sum
def sum_to(n):
    pass

n = int(input())
print(sum_to(n))
""",
        "solution_code": """def sum_to(n):
    if n <= 0:
        return 0
    return n + sum_to(n - 1)

n = int(input())
print(sum_to(n))"""
    },
    {
        "q_num": 32,
        "title": "Star Row",
        "level": "Level 6 of 10: Recursion - Base case and recursive call",
        "subtopic": "Printing without a new line",
        "difficulty": "Beginner",
        "xp": 45,
        "scenario": "A pattern printer draws one row of stars using recursion. Each call prints one star on the same line.",
        "task": 'Define print_stars(n) recursively. If n is 0, print an empty line and stop. Otherwise print * with end="" and call print_stars(n - 1). Read n and call the function.',
        "sample_input": "5",
        "expected_output": "*****",
        "hint": 'print("*", end="") keeps the cursor on the same line. The final print() moves to a new line.',
        "starter_code": """# [FR-32] Star Row
# Level 6 of 10: Printing without a new line
def print_stars(n):
    pass

n = int(input())
print_stars(n)
""",
        "solution_code": """def print_stars(n):
    if n == 0:
        print()
        return
    print("*", end="")
    print_stars(n - 1)

n = int(input())
print_stars(n)"""
    },
    {
        "q_num": 33,
        "title": "Halving Steps",
        "level": "Level 6 of 10: Recursion - Base case and recursive call",
        "subtopic": "Counting steps",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A game halves a number until it reaches 1. The program counts how many halvings are needed.",
        "task": "Define halvings(n): if n is 1 or less, return 0. Otherwise return 1 + halvings(n // 2). Read n and print Steps: followed by the count.",
        "sample_input": "20",
        "expected_output": "Steps: 4",
        "hint": "20 becomes 10, 5, 2 and then 1. That is four halvings.",
        "starter_code": """# [FR-33] Halving Steps
# Level 6 of 10: Counting steps
def halvings(n):
    pass

n = int(input())
print(f"Steps: {halvings(n)}")
""",
        "solution_code": """def halvings(n):
    if n <= 1:
        return 0
    return 1 + halvings(n // 2)

n = int(input())
print(f"Steps: {halvings(n)}")"""
    },

    # =========================================================================
    # Recursion - Level 2 (Level 7): Recursion with numbers (FR-34 to FR-38)
    # =========================================================================
    {
        "q_num": 34,
        "title": "Factorial",
        "level": "Level 7 of 10: Recursion with numbers",
        "subtopic": "Recursive factorial",
        "difficulty": "Beginner",
        "xp": 45,
        "scenario": "A probability class uses factorial to count the ways to arrange items.",
        "task": "Define factorial(n) recursively with base case factorial(1) = 1 (and 0 also returns 1). Read n and print the factorial.",
        "sample_input": "6",
        "expected_output": "720",
        "hint": "n! = n x (n - 1)!",
        "starter_code": """# [FR-34] Factorial
# Level 7 of 10: Recursion with numbers
def factorial(n):
    pass

n = int(input())
print(factorial(n))
""",
        "solution_code": """def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

n = int(input())
print(factorial(n))"""
    },
    {
        "q_num": 35,
        "title": "Power of a Number",
        "level": "Level 7 of 10: Recursion with numbers",
        "subtopic": "Recursive power",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A calculator computes base to the power exp without using the ** operator.",
        "task": "Define power(base, exp) recursively: if exp is 0 return 1, otherwise return base * power(base, exp - 1). Read base and exp, then print the result.",
        "sample_input": "3\n4",
        "expected_output": "81",
        "hint": "3 to the power 4 is 3 x (3 to the power 3).",
        "starter_code": """# [FR-35] Power of a Number
# Level 7 of 10: Recursive power
def power(base, exp):
    pass

base = int(input())
exp = int(input())
print(power(base, exp))
""",
        "solution_code": """def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

base = int(input())
exp = int(input())
print(power(base, exp))"""
    },
    {
        "q_num": 36,
        "title": "Sum of Digits",
        "level": "Level 7 of 10: Recursion with numbers",
        "subtopic": "Recursive digit sum",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A checksum adds the digits of a number. The last digit is found with % 10 and the rest with // 10.",
        "task": "Define sum_digits(n) recursively. If n is less than 10 return n. Otherwise return n % 10 + sum_digits(n // 10). Read n and print the sum.",
        "sample_input": "4095",
        "expected_output": "18",
        "hint": "4095 gives 5 + the sum of 409, and so on.",
        "starter_code": """# [FR-36] Sum of Digits
# Level 7 of 10: Recursive digit sum
def sum_digits(n):
    pass

n = int(input())
print(sum_digits(n))
""",
        "solution_code": """def sum_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_digits(n // 10)

n = int(input())
print(sum_digits(n))"""
    },
    {
        "q_num": 37,
        "title": "Count the Digits",
        "level": "Level 7 of 10: Recursion with numbers",
        "subtopic": "Recursive digit count",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A form checks how many digits a number has, using recursion instead of converting to text.",
        "task": "Define count_digits(n) recursively. If n is less than 10 return 1. Otherwise return 1 + count_digits(n // 10). Read n and print Digits: followed by the count.",
        "sample_input": "90210",
        "expected_output": "Digits: 5",
        "hint": "Each division by 10 removes one digit.",
        "starter_code": """# [FR-37] Count the Digits
# Level 7 of 10: Recursive digit count
def count_digits(n):
    pass

n = int(input())
print(f"Digits: {count_digits(n)}")
""",
        "solution_code": """def count_digits(n):
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

n = int(input())
print(f"Digits: {count_digits(n)}")"""
    },
    {
        "q_num": 38,
        "title": "Fibonacci",
        "level": "Level 7 of 10: Recursion with numbers",
        "subtopic": "Recursion that calls itself twice",
        "difficulty": "Intermediate",
        "xp": 55,
        "scenario": "A puzzle club uses the series 0, 1, 1, 2, 3, 5, 8, ... where each term is the sum of the two terms before it.",
        "task": "Define fib(n) recursively: if n is 0 or 1 return n, otherwise return fib(n - 1) + fib(n - 2). Read n and print fib(n) = followed by the value.",
        "sample_input": "10",
        "expected_output": "fib(10) = 55",
        "hint": "Here the function calls itself twice in one line. Use the base cases 0 and 1 first.",
        "starter_code": """# [FR-38] Fibonacci
# Level 7 of 10: Recursion that calls itself twice
def fib(n):
    pass

n = int(input())
print(f"fib({n}) = {fib(n)}")
""",
        "solution_code": """def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

n = int(input())
print(f"fib({n}) = {fib(n)}")"""
    },

    # =========================================================================
    # Recursion - Level 3 (Level 8): Recursion with strings (FR-39 to FR-42)
    # =========================================================================
    {
        "q_num": 39,
        "title": "Reverse a Word",
        "level": "Level 8 of 10: Recursion with strings",
        "subtopic": "Recursive string reversal",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A word game reverses a word by taking the last piece and moving the first letter to the end.",
        "task": "Define reverse_text(s) recursively. If the length is 1 or less return s. Otherwise return reverse_text(s[1:]) + s[0]. Read a word and print the reversed word.",
        "sample_input": "python",
        "expected_output": "nohtyp",
        "hint": "s[1:] is everything after the first letter. s[0] is the first letter.",
        "starter_code": """# [FR-39] Reverse a Word
# Level 8 of 10: Recursion with strings
def reverse_text(s):
    pass

word = input().strip()
print(reverse_text(word))
""",
        "solution_code": """def reverse_text(s):
    if len(s) <= 1:
        return s
    return reverse_text(s[1:]) + s[0]

word = input().strip()
print(reverse_text(word))"""
    },
    {
        "q_num": 40,
        "title": "Palindrome Checker",
        "level": "Level 8 of 10: Recursion with strings",
        "subtopic": "Recursive palindrome check",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A word is a palindrome when its first and last letters match and the middle part is also a palindrome.",
        "task": "Define is_pal(s) recursively. If the length is 0 or 1 return True. If the first and last letters differ return False. Otherwise return is_pal(s[1:-1]). Read a word in lower case and print Palindrome or Not a palindrome.",
        "sample_input": "level",
        "expected_output": "Palindrome",
        "hint": "s[1:-1] removes the first and last letters.",
        "starter_code": """# [FR-40] Palindrome Checker
# Level 8 of 10: Recursive palindrome check
def is_pal(s):
    pass

word = input().strip()
print("Palindrome" if is_pal(word) else "Not a palindrome")
""",
        "solution_code": """def is_pal(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_pal(s[1:-1])

word = input().strip()
print("Palindrome" if is_pal(word) else "Not a palindrome")"""
    },
    {
        "q_num": 41,
        "title": "Count Vowels",
        "level": "Level 8 of 10: Recursion with strings",
        "subtopic": "Recursive character counting",
        "difficulty": "Intermediate",
        "xp": 55,
        "scenario": "A reading tool counts vowels in a word by checking one character at a time through recursion.",
        "task": "Define count_vowels(s) recursively. If s is empty return 0. Otherwise add 1 if the first letter is a vowel (a, e, i, o, u, any case), and add count_vowels(s[1:]). Read a word and print Vowels: followed by the count.",
        "sample_input": "recursion",
        "expected_output": "Vowels: 4",
        "hint": "Check only the first character in each call, then pass the rest of the string on.",
        "starter_code": """# [FR-41] Count Vowels
# Level 8 of 10: Recursive character counting
def count_vowels(s):
    pass

word = input().strip()
print(f"Vowels: {count_vowels(word)}")
""",
        "solution_code": """def count_vowels(s):
    if not s:
        return 0
    is_v = 1 if s[0].lower() in "aeiou" else 0
    return is_v + count_vowels(s[1:])

word = input().strip()
print(f"Vowels: {count_vowels(word)}")"""
    },
    {
        "q_num": 42,
        "title": "Remove Spaces",
        "level": "Level 8 of 10: Recursion with strings",
        "subtopic": "Recursive string filtering",
        "difficulty": "Intermediate",
        "xp": 55,
        "scenario": "A username generator removes spaces from text by checking each character recursively.",
        "task": "Define remove_spaces(s) recursively. If s is empty return an empty string. Otherwise take the first character, and return the rest without spaces, adding the first character only when it is not a space. Read a line and print the result.",
        "sample_input": "a b c d",
        "expected_output": "abcd",
        "hint": "Keep the first character only when it is not a space, then add the cleaned rest.",
        "starter_code": """# [FR-42] Remove Spaces
# Level 8 of 10: Recursive string filtering
def remove_spaces(s):
    pass

line = input()
print(remove_spaces(line))
""",
        "solution_code": """def remove_spaces(s):
    if not s:
        return ""
    head = "" if s[0] == " " else s[0]
    return head + remove_spaces(s[1:])

line = input()
print(remove_spaces(line))"""
    },

    # =========================================================================
    # Recursion - Level 4 (Level 9): Recursion with lists and nested data (FR-43 to FR-46)
    # =========================================================================
    {
        "q_num": 43,
        "title": "Sum of a List",
        "level": "Level 9 of 10: Recursion with lists and nested data",
        "subtopic": "Recursive list sum",
        "difficulty": "Intermediate",
        "xp": 55,
        "scenario": "A class collects test scores and needs their total using recursion on the list.",
        "task": "Define sum_list(nums) recursively. If the list is empty return 0. Otherwise return nums[0] + sum_list(nums[1:]). Read numbers on one line, then print Sum: followed by the total.",
        "sample_input": "4 8 15 16 23 42",
        "expected_output": "Sum: 108",
        "hint": "nums[1:] gives the list without its first item.",
        "starter_code": """# [FR-43] Sum of a List
# Level 9 of 10: Recursion with lists and nested data
def sum_list(nums):
    pass

nums = list(map(int, input().split()))
print(f"Sum: {sum_list(nums)}")
""",
        "solution_code": """def sum_list(nums):
    if not nums:
        return 0
    return nums[0] + sum_list(nums[1:])

nums = list(map(int, input().split()))
print(f"Sum: {sum_list(nums)}")"""
    },
    {
        "q_num": 44,
        "title": "Largest Value",
        "level": "Level 9 of 10: Recursion with lists and nested data",
        "subtopic": "Recursive maximum",
        "difficulty": "Intermediate",
        "xp": 55,
        "scenario": "A sensor reading list needs its largest value found by comparing the first value with the largest of the rest.",
        "task": "Define max_list(nums) recursively. If there is only one item return it. Otherwise find rest_max = max_list(nums[1:]) and return the bigger of nums[0] and rest_max. Read numbers and print Largest: followed by the value.",
        "sample_input": "3 17 5 9",
        "expected_output": "Largest: 17",
        "hint": "Compare the first item with the answer for the rest of the list.",
        "starter_code": """# [FR-44] Largest Value
# Level 9 of 10: Recursive maximum
def max_list(nums):
    pass

nums = list(map(int, input().split()))
print(f"Largest: {max_list(nums)}")
""",
        "solution_code": """def max_list(nums):
    if len(nums) == 1:
        return nums[0]
    rest_max = max_list(nums[1:])
    return nums[0] if nums[0] > rest_max else rest_max

nums = list(map(int, input().split()))
print(f"Largest: {max_list(nums)}")"""
    },
    {
        "q_num": 45,
        "title": "Total of Nested Lists",
        "level": "Level 9 of 10: Recursion with lists and nested data",
        "subtopic": "Recursion on nested lists",
        "difficulty": "Hard",
        "xp": 70,
        "scenario": "A file system stores file sizes in folders inside folders. Some items are lists of sizes.",
        "task": "Define nested_sum(items) that loops over the items. If an item is a list, add nested_sum(item). Otherwise add the item. Use the data [1, [2, 3], [4, [5]]] and print Total: followed by the result.",
        "sample_input": "",
        "expected_output": "Total: 15",
        "hint": "isinstance(item, list) checks whether an item is a nested list.",
        "starter_code": """# [FR-45] Total of Nested Lists
# Level 9 of 10: Recursion on nested lists
def nested_sum(items):
    pass

data = [1, [2, 3], [4, [5]]]
print(f"Total: {nested_sum(data)}")
""",
        "solution_code": """def nested_sum(items):
    total = 0
    for item in items:
        if isinstance(item, list):
            total += nested_sum(item)
        else:
            total += item
    return total

data = [1, [2, 3], [4, [5]]]
print(f"Total: {nested_sum(data)}")"""
    },
    {
        "q_num": 46,
        "title": "Depth of Nested Lists",
        "level": "Level 9 of 10: Recursion with lists and nested data",
        "subtopic": "Measuring depth with recursion",
        "difficulty": "Hard",
        "xp": 75,
        "scenario": "A folder tree has folders inside folders. The depth is how many levels of folders go down.",
        "task": "Define depth(items) that returns 1 plus the largest depth of any nested list inside it. Use the data [1, [2, [3]]] and print Depth: followed by the result.",
        "sample_input": "",
        "expected_output": "Depth: 3",
        "hint": "Start with max_depth = 1. For each nested list, the depth is 1 + depth(item), and keep the largest.",
        "starter_code": """# [FR-46] Depth of Nested Lists
# Level 9 of 10: Measuring depth with recursion
def depth(items):
    pass

data = [1, [2, [3]]]
print(f"Depth: {depth(data)}")
""",
        "solution_code": """def depth(items):
    max_depth = 1
    for item in items:
        if isinstance(item, list):
            d = 1 + depth(item)
            if d > max_depth:
                max_depth = d
    return max_depth

data = [1, [2, [3]]]
print(f"Depth: {depth(data)}")"""
    },

    # =========================================================================
    # Recursion - Level 5 (Level 10): Classic recursion problems (FR-47 to FR-50)
    # =========================================================================
    {
        "q_num": 47,
        "title": "Greatest Common Divisor",
        "level": "Level 10 of 10: Classic recursion problems",
        "subtopic": "Euclid's algorithm with recursion",
        "difficulty": "Intermediate",
        "xp": 60,
        "scenario": "A tailor needs the longest piece length that fits both cloth rolls exactly. The GCD is found with Euclid's algorithm.",
        "task": "Define gcd(a, b) recursively: if b is 0 return a, otherwise return gcd(b, a % b). Read two numbers and print GCD: followed by the value.",
        "sample_input": "84\n36",
        "expected_output": "GCD: 12",
        "hint": "The remainder gets smaller at each step, so the recursion must end when the remainder is 0.",
        "starter_code": """# [FR-47] Greatest Common Divisor
# Level 10 of 10: Euclid's algorithm with recursion
def gcd(a, b):
    pass

a = int(input())
b = int(input())
print(f"GCD: {gcd(a, b)}")
""",
        "solution_code": """def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input())
b = int(input())
print(f"GCD: {gcd(a, b)}")"""
    },
    {
        "q_num": 48,
        "title": "Tower of Hanoi Moves",
        "level": "Level 10 of 10: Classic recursion problems",
        "subtopic": "Tower of Hanoi",
        "difficulty": "Hard",
        "xp": 80,
        "scenario": "A puzzle has disks stacked on rod A. Disks must move to rod C, using rod B, and a larger disk can never sit on a smaller one. The program prints every move.",
        "task": "Define hanoi(n, source, target, auxiliary). If n is 0 return. Otherwise move n-1 disks from source to auxiliary, print Move disk n from source to target, then move n-1 disks from auxiliary to target. Read n and call hanoi(n, 'A', 'C', 'B').",
        "sample_input": "3",
        "expected_output": "Move disk 1 from A to C\nMove disk 2 from A to B\nMove disk 1 from C to B\nMove disk 3 from A to C\nMove disk 1 from B to A\nMove disk 2 from B to C\nMove disk 1 from A to C",
        "hint": "Think of the smaller stack as a separate problem. Swap the roles of the rods in each recursive call.",
        "starter_code": """# [FR-48] Tower of Hanoi Moves
# Level 10 of 10: Tower of Hanoi
def hanoi(n, source, target, auxiliary):
    pass

n = int(input())
hanoi(n, 'A', 'C', 'B')
""",
        "solution_code": """def hanoi(n, source, target, auxiliary):
    if n == 0:
        return
    hanoi(n - 1, source, auxiliary, target)
    print(f"Move disk {n} from {source} to {target}")
    hanoi(n - 1, auxiliary, target, source)

n = int(input())
hanoi(n, 'A', 'C', 'B')"""
    },
    {
        "q_num": 49,
        "title": "Find a Number in a Sorted List",
        "level": "Level 10 of 10: Classic recursion problems",
        "subtopic": "Binary search with recursion",
        "difficulty": "Hard",
        "xp": 75,
        "scenario": "A phone book is sorted. Binary search checks the middle name and throws away half of the list at each step.",
        "task": "Use the sorted list [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]. Define binary_search(items, target, low, high) recursively. Return the index if found, or -1 if not. Read a target and print Found at index <idx>, or Not found.",
        "sample_input": "23",
        "expected_output": "Found at index 5",
        "hint": "Find the middle index with (low + high) // 2, then search only the half that could contain the target.",
        "starter_code": """# [FR-49] Find a Number in a Sorted List
# Level 10 of 10: Binary search with recursion
def binary_search(items, target, low, high):
    pass

items = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = int(input())
idx = binary_search(items, target, 0, len(items) - 1)
print(f"Found at index {idx}" if idx != -1 else "Not found")
""",
        "solution_code": """def binary_search(items, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if items[mid] == target:
        return mid
    elif items[mid] > target:
        return binary_search(items, target, low, mid - 1)
    else:
        return binary_search(items, target, mid + 1, high)

items = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target = int(input())
idx = binary_search(items, target, 0, len(items) - 1)
print(f"Found at index {idx}" if idx != -1 else "Not found")"""
    },
    {
        "q_num": 50,
        "title": "Decimal to Binary",
        "level": "Level 10 of 10: Classic recursion problems",
        "subtopic": "Repeated division with recursion",
        "difficulty": "Intermediate",
        "xp": 60,
        "scenario": "A computer stores numbers in binary (only 0 and 1). Repeated division by 2 gives the binary digits from the last to the first.",
        "task": "Define to_binary(n) recursively. If n is less than 2 return str(n). Otherwise return to_binary(n // 2) + str(n % 2). Read n and print Binary: followed by the result.",
        "sample_input": "13",
        "expected_output": "Binary: 1101",
        "hint": "The result of the smaller number comes first, then the remainder of n divided by 2.",
        "starter_code": """# [FR-50] Decimal to Binary
# Level 10 of 10: Repeated division with recursion
def to_binary(n):
    pass

n = int(input())
print(f"Binary: {to_binary(n)}")
""",
        "solution_code": """def to_binary(n):
    if n < 2:
        return str(n)
    return to_binary(n // 2) + str(n % 2)

n = int(input())
print(f"Binary: {to_binary(n)}")"""
    },
]
