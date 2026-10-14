"""
Elysia School: Dynamic Question Bank Engine
Generates customized problem sets by subject, topic, difficulty, and count.
Includes real-world college scenarios, test cases, and bilingual hints.
"""

from typing import List, Dict, Any
import random

QUESTIONS_DATABASE = [
    # =========================================================================
    # PYTHON QUESTIONS
    # =========================================================================

    # --- Python: Variables & Math (py_variables) ---
    {
        "id": "py_q_1",
        "subject": "python",
        "topic": "py_variables",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Hostel Swiggy Bill Splitter",
        "title_hi": "Hostel Swiggy Bill Splitter",
        "desc_en": "You and your 3 roommates (total 4 people) ordered food worth 840 rupees. There is an additional delivery fee of 40 rupees and a 50 rupee coupon discount. Write code to compute each person's exact share in a variable named 'each_share', and print: 'Each roommate pays: X'",
        "desc_hi": "Tu aur tere 3 roommates (total 4 log) ne 840 ka khana mangwaya. 40 rupaye delivery fee lagi aur 50 rupaye ka discount mila. Calculate karo ki har dost ko kitna dena padega variable 'each_share' me, aur print karo: 'Each roommate pays: X'",
        "starter_code": "total_food = 840\ndelivery_fee = 40\ndiscount = 50\ntotal_people = 4\n\n# Calculate each_share and print:\n",
        "solution_code": "total_food = 840\ndelivery_fee = 40\ndiscount = 50\ntotal_people = 4\nnet_bill = total_food + delivery_fee - discount\neach_share = net_bill / total_people\nprint(f'Each roommate pays: {each_share}')",
        "expected_output": "Each roommate pays: 207.5",
        "hint_en": "Formula: (total_food + delivery_fee - discount) / total_people",
        "hint_hi": "Pehle net bill nikalo: (840 + 40 - 50), fir 4 se divide kardo."
    },
    {
        "id": "py_q_2",
        "subject": "python",
        "topic": "py_variables",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Temperature Converter (Celsius to Fahrenheit)",
        "title_hi": "Celsius to Fahrenheit Converter",
        "desc_en": "Given temperature 'celsius = 37', convert it to Fahrenheit using formula F = (C * 9/5) + 32. Store in 'fahrenheit' and print: 'Temperature in F: X'",
        "desc_hi": "Temperature 'celsius = 37' diya hai. Use formula F = (C * 9/5) + 32 se convert karo. 'fahrenheit' variable me store karke print karo: 'Temperature in F: X'",
        "starter_code": "celsius = 37\n# Write conversion here:\n",
        "solution_code": "celsius = 37\nfahrenheit = (celsius * 9/5) + 32\nprint(f'Temperature in F: {fahrenheit}')",
        "expected_output": "Temperature in F: 98.6",
        "hint_en": "Remember operator precedence or use parentheses: (celsius * 9/5) + 32",
        "hint_hi": "BODMAS rule ka dhyan rakhna, bracket lagao: (celsius * 9/5) + 32"
    },
    {
        "id": "py_q_8",
        "subject": "python",
        "topic": "py_variables",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Simple Interest & Total Maturity",
        "title_hi": "Simple Interest aur Total Maturity",
        "desc_en": "Given principal P = 12000, annual rate R = 7.5%, and time T = 2 years. Compute simple interest SI = (P * R * T) / 100 and total amount = P + SI. Print on separate lines: 'Interest: 1800.0' and 'Total: 13800.0'.",
        "desc_hi": "Principal P = 12000, rate R = 7.5%, time T = 2 years diya hai. Simple interest SI = (P * R * T) / 100 aur total = P + SI calculate karo. Do lines me print karo: 'Interest: 1800.0' aur 'Total: 13800.0'.",
        "starter_code": "P = 12000\nR = 7.5\nT = 2\n# Calculate SI and Total:\n",
        "solution_code": "P = 12000\nR = 7.5\nT = 2\nSI = (P * R * T) / 100\ntotal = P + SI\nprint(f'Interest: {SI}')\nprint(f'Total: {total}')",
        "expected_output": "Interest: 1800.0\nTotal: 13800.0",
        "hint_en": "Use SI = (P * R * T) / 100 and total = P + SI.",
        "hint_hi": "SI = (P * R * T) / 100 formula lagao aur dono values print karo."
    },
    {
        "id": "py_q_9",
        "subject": "python",
        "topic": "py_variables",
        "difficulty": "Tricky",
        "xp": 75,
        "title_en": "Swap Variables Without Temporary Variable",
        "title_hi": "Bina Third Variable Ke Swap Karo",
        "desc_en": "Given a = 45 and b = 90. Swap both numbers using Python tuple packing/unpacking without a temporary variable. Print 'a = 90, b = 45'.",
        "desc_hi": "a = 45 aur b = 90 diya hai. Python tuple packing/unpacking se dono values swap karo bina kisi extra variable ke. Print karo: 'a = 90, b = 45'.",
        "starter_code": "a = 45\nb = 90\n# Swap in one line without temp:\n",
        "solution_code": "a = 45\nb = 90\na, b = b, a\nprint(f'a = {a}, b = {b}')",
        "expected_output": "a = 90, b = 45",
        "hint_en": "Python supports multiple assignment: `a, b = b, a`.",
        "hint_hi": "Python me ek line me swap hota hai: `a, b = b, a`."
    },

    # --- Python: Conditionals (py_conditionals) ---
    {
        "id": "py_q_3",
        "subject": "python",
        "topic": "py_conditionals",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "75% Attendance Detainee Checker",
        "title_hi": "75% Attendance Detainee Checker",
        "desc_en": "Given 'total_classes = 60' and 'attended = 42'. Calculate attendance percentage. If percentage >= 75, print 'Status: Eligible', otherwise print 'Status: Detained'.",
        "desc_hi": "'total_classes = 60' aur 'attended = 42' diya hai. Attendance percentage calculate karo. Agar >= 75 hai to print karo 'Status: Eligible', warna 'Status: Detained'.",
        "starter_code": "total_classes = 60\nattended = 42\n\n# Your code here:\n",
        "solution_code": "total_classes = 60\nattended = 42\npercentage = (attended / total_classes) * 100\nif percentage >= 75:\n    print('Status: Eligible')\nelse:\n    print('Status: Detained')",
        "expected_output": "Status: Detained",
        "hint_en": "42 / 60 * 100 is 70%, which is strictly less than 75%.",
        "hint_hi": "42 / 60 * 100 = 70% banta hai jo 75 se kam hai, isliye Detained aana chahiye."
    },
    {
        "id": "py_q_4",
        "subject": "python",
        "topic": "py_conditionals",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "College Lab Grade Evaluator",
        "title_hi": "College Lab Grade Evaluator",
        "desc_en": "Given student 'marks = 86'. If marks >= 90: 'Grade: O' (Outstanding), elif marks >= 80: 'Grade: A+', elif marks >= 70: 'Grade: A', else: 'Grade: B'. Print the grade line.",
        "desc_hi": "'marks = 86' ke liye grading system banao. Agar >= 90: 'Grade: O', >= 80: 'Grade: A+', >= 70: 'Grade: A', warna: 'Grade: B'.",
        "starter_code": "marks = 86\n# Write if-elif-else ladder:\n",
        "solution_code": "marks = 86\nif marks >= 90:\n    print('Grade: O')\nelif marks >= 80:\n    print('Grade: A+')\nelif marks >= 70:\n    print('Grade: A')\nelse:\n    print('Grade: B')",
        "expected_output": "Grade: A+",
        "hint_en": "Use if followed by elif and finally else.",
        "hint_hi": "Pehle if check hoga, fir elif 80 wala true ho jayega aur 'Grade: A+' print hoga."
    },
    {
        "id": "py_q_10",
        "subject": "python",
        "topic": "py_conditionals",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Leap Year Validator",
        "title_hi": "Leap Year Checker",
        "desc_en": "Given year = 2024. A year is a leap year if it is divisible by 4 and not divisible by 100, OR it is divisible by 400. Print '2024 is a Leap Year' if true, else '2024 is Not a Leap Year'.",
        "desc_hi": "year = 2024 diya hai. Leap year check karo ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0). Print karo: '2024 is a Leap Year'.",
        "starter_code": "year = 2024\n# Check leap year condition:\n",
        "solution_code": "year = 2024\nif (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n    print(f'{year} is a Leap Year')\nelse:\n    print(f'{year} is Not a Leap Year')",
        "expected_output": "2024 is a Leap Year",
        "hint_en": "Combine conditions: `(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)`.",
        "hint_hi": "Dhyan rahe century years (100) leap year nahi hote jab tak 400 se divisible na hon."
    },
    {
        "id": "py_q_11",
        "subject": "python",
        "topic": "py_conditionals",
        "difficulty": "Tricky",
        "xp": 75,
        "title_en": "Campus Canteen Slab Discounts",
        "title_hi": "Canteen Bill Discount Slabs",
        "desc_en": "Given bill = 650. Slabs: bill > 1000 gives 20% discount; bill > 500 gives 10% discount; otherwise 0%. Compute and print 'Final Bill: 585.0'.",
        "desc_hi": "bill = 650 diya hai. Agar bill > 1000 to 20% discount, agar > 500 to 10% discount, warna 0%. Print karo: 'Final Bill: 585.0'.",
        "starter_code": "bill = 650\n# Apply slab discount:\n",
        "solution_code": "bill = 650\nif bill > 1000:\n    discount = 0.20\nelif bill > 500:\n    discount = 0.10\nelse:\n    discount = 0.0\nfinal_bill = bill - (bill * discount)\nprint(f'Final Bill: {final_bill}')",
        "expected_output": "Final Bill: 585.0",
        "hint_en": "650 is greater than 500, so discount is 10% (65.0). 650 - 65 = 585.0.",
        "hint_hi": "650 par 10% discount (65 rupaye) katega, to final bill 585.0 banega."
    },

    # --- Python: Loops (py_loops) ---
    {
        "id": "py_q_5",
        "subject": "python",
        "topic": "py_loops",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Multiplication Table Generator",
        "title_hi": "Multiplication Table Generator",
        "desc_en": "Given 'n = 7', print the multiplication table from 1 to 5 in the format '7 x 1 = 7', '7 x 2 = 14', etc. (one per line).",
        "desc_hi": "'n = 7' ke liye 1 se 5 tak ki table print karo format: '7 x 1 = 7', '7 x 2 = 14', etc. ek-ek line me.",
        "starter_code": "n = 7\n# Use a loop from 1 to 5:\n",
        "solution_code": "n = 7\nfor i in range(1, 6):\n    print(f'{n} x {i} = {n * i}')",
        "expected_output": "7 x 1 = 7\n7 x 2 = 14\n7 x 3 = 21\n7 x 4 = 28\n7 x 5 = 35",
        "hint_en": "range(1, 6) will loop from 1 to 5.",
        "hint_hi": "range(1, 6) lagao taaki loop 1 se 5 tak chale."
    },
    {
        "id": "py_q_6",
        "subject": "python",
        "topic": "py_loops",
        "difficulty": "Tricky",
        "xp": 75,
        "title_en": "Even Numbers Filter & Sum",
        "title_hi": "Even Numbers Filter & Sum",
        "desc_en": "Given numbers from 1 to 10. Compute the sum of only the even numbers and print: 'Sum of evens: X'",
        "desc_hi": "1 se 10 tak ke numbers me se sirf EVEN (sam) numbers ka sum calculate karo aur print karo: 'Sum of evens: X'",
        "starter_code": "total_even = 0\n# Loop from 1 to 10 and add if i % 2 == 0:\n",
        "solution_code": "total_even = 0\nfor i in range(1, 11):\n    if i % 2 == 0:\n        total_even += i\nprint(f'Sum of evens: {total_even}')",
        "expected_output": "Sum of evens: 30",
        "hint_en": "Evens are 2 + 4 + 6 + 8 + 10 = 30.",
        "hint_hi": "2 + 4 + 6 + 8 + 10 jodoge to 30 aayega. `i % 2 == 0` se even check hota hai."
    },
    {
        "id": "py_q_12",
        "subject": "python",
        "topic": "py_loops",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Number Reversal & Palindrome Checker",
        "title_hi": "Number Reverse aur Palindrome Checker",
        "desc_en": "Given num = 12321. Check if the reversed number is equal to original number. If equal, print '12321 is a Palindrome', else '12321 is Not a Palindrome'.",
        "desc_hi": "num = 12321 diya hai. Check karo ki ulta karne par bhi same number rehta hai ya nahi. Print karo: '12321 is a Palindrome'.",
        "starter_code": "num = 12321\n# Reverse and check palindrome:\n",
        "solution_code": "num = 12321\ns = str(num)\nif s == s[::-1]:\n    print(f'{num} is a Palindrome')\nelse:\n    print(f'{num} is Not a Palindrome')",
        "expected_output": "12321 is a Palindrome",
        "hint_en": "Convert integer to string and use string slicing `s[::-1]` to reverse.",
        "hint_hi": "String me convert karke `s[::-1]` se ulta kar sakte ho."
    },
    {
        "id": "py_q_13",
        "subject": "python",
        "topic": "py_loops",
        "difficulty": "Tricky",
        "xp": 75,
        "title_en": "Right-Angled Star Triangle Pattern",
        "title_hi": "Right-Angled Star Triangle Pattern",
        "desc_en": "Given rows = 4. Using a loop, print a right-angled triangle pattern from 1 star to 4 stars.",
        "desc_hi": "rows = 4 diya hai. Loop use karke 1 se lekar 4 stars tak ka triangle print karo.",
        "starter_code": "rows = 4\n# Loop and print asterisks:\n",
        "solution_code": "rows = 4\nfor i in range(1, rows + 1):\n    print('*' * i)",
        "expected_output": "*\n**\n***\n****",
        "hint_en": "In Python, multiplying a string repeats it: `print('*' * i)`.",
        "hint_hi": "Python me `'*' * i` karne se string utni baar repeat ho jaati hai."
    },

    # --- Python: Lists (py_lists) ---
    {
        "id": "py_q_7",
        "subject": "python",
        "topic": "py_lists",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Find Second Highest Marks",
        "title_hi": "Find Second Highest Marks",
        "desc_en": "Given a list of marks: `marks = [45, 92, 88, 76, 95]`. Find the second highest mark and print: 'Second topper: X'",
        "desc_hi": "Marks list: `marks = [45, 92, 88, 76, 95]`. Isme se second highest mark dhoondo aur print karo: 'Second topper: X'",
        "starter_code": "marks = [45, 92, 88, 76, 95]\n# Sort or remove max to find second highest:\n",
        "solution_code": "marks = [45, 92, 88, 76, 95]\nmarks.sort()\nsecond_topper = marks[-2]\nprint(f'Second topper: {second_topper}')",
        "expected_output": "Second topper: 92",
        "hint_en": "Sort the list with `marks.sort()` and take `marks[-2]`.",
        "hint_hi": "List ko sort karo, last wala highest hoga aur second last (-2) second highest hoga."
    },
    {
        "id": "py_q_14",
        "subject": "python",
        "topic": "py_lists",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Remove Duplicates Preserving Order",
        "title_hi": "List Duplicates Remove Karo",
        "desc_en": "Given items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]. Create a new list containing unique items while preserving their original first-seen order. Print 'Unique: [3, 1, 4, 5, 9, 2, 6]'.",
        "desc_hi": "items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3] diya hai. Duplicate elements hatao lekin unka original order barkarar rakho. Print karo: 'Unique: [3, 1, 4, 5, 9, 2, 6]'.",
        "starter_code": "items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\n# Remove duplicates preserving order:\n",
        "solution_code": "items = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]\nunique = []\nfor x in items:\n    if x not in unique:\n        unique.append(x)\nprint(f'Unique: {unique}')",
        "expected_output": "Unique: [3, 1, 4, 5, 9, 2, 6]",
        "hint_en": "Iterate over items and append to a new list only if not already present.",
        "hint_hi": "Ek nayi list banao aur loop chala kar check karo `if x not in unique:`."
    },
    {
        "id": "py_q_15",
        "subject": "python",
        "topic": "py_lists",
        "difficulty": "Tricky",
        "xp": 75,
        "title_en": "2D Matrix Diagonal Sum",
        "title_hi": "Matrix Diagonal Elements Ka Sum",
        "desc_en": "Given a 3x3 matrix: `matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]`. Calculate the sum of the primary diagonal elements (1 + 5 + 9). Print 'Primary Diagonal Sum: 15'.",
        "desc_hi": "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] diya hai. Primary diagonal elements (1 + 5 + 9) ka sum nikalo aur print karo: 'Primary Diagonal Sum: 15'.",
        "starter_code": "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\n# Compute diagonal sum:\n",
        "solution_code": "matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]\ndiag_sum = sum(matrix[i][i] for i in range(len(matrix)))\nprint(f'Primary Diagonal Sum: {diag_sum}')",
        "expected_output": "Primary Diagonal Sum: 15",
        "hint_en": "Diagonal elements satisfy row == column index: `matrix[i][i]`.",
        "hint_hi": "Diagonal element index i == j hota hai: `matrix[i][i]`."
    },

    # --- Python: Tuples (py_tuples) ---
    {
        "id": "py_q_16",
        "subject": "python",
        "topic": "py_tuples",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Coordinate Distance with Tuple Unpacking",
        "title_hi": "Tuple Coordinates Unpack Karo",
        "desc_en": "Given point1 = (0, 0) and point2 = (3, 4). Unpack both tuples and calculate Euclidean distance using formula sqrt((x2-x1)**2 + (y2-y1)**2). Print 'Distance: 5.0'.",
        "desc_hi": "point1 = (0, 0) aur point2 = (3, 4) diya hai. Unpack karke Euclidean distance nikalo. Print karo: 'Distance: 5.0'.",
        "starter_code": "point1 = (0, 0)\npoint2 = (3, 4)\n# Unpack and calculate distance:\n",
        "solution_code": "point1 = (0, 0)\npoint2 = (3, 4)\nx1, y1 = point1\nx2, y2 = point2\ndist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5\nprint(f'Distance: {dist}')",
        "expected_output": "Distance: 5.0",
        "hint_en": "Unpack using `x1, y1 = point1` and `dist = ((x2-x1)**2 + (y2-y1)**2)**0.5`.",
        "hint_hi": "Tuple unpack karo aur distance formula `** 0.5` use karke square root nikalo."
    },
    {
        "id": "py_q_17",
        "subject": "python",
        "topic": "py_tuples",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Top 3 Semester Scores with Tuples",
        "title_hi": "Tuple Slicing & Min-Max",
        "desc_en": "Given tuple `scores = (88, 95, 72, 99, 84, 91)`. Sort the scores in descending order and extract the top 3 highest scores into a new tuple. Print 'Top 3: (99, 95, 91)'.",
        "desc_hi": "scores = (88, 95, 72, 99, 84, 91) diya hai. Highest se lowest order me sort karke top 3 scores ka naya tuple banao. Print karo: 'Top 3: (99, 95, 91)'.",
        "starter_code": "scores = (88, 95, 72, 99, 84, 91)\n# Extract top 3 into tuple:\n",
        "solution_code": "scores = (88, 95, 72, 99, 84, 91)\ntop_3 = tuple(sorted(scores, reverse=True)[:3])\nprint(f'Top 3: {top_3}')",
        "expected_output": "Top 3: (99, 95, 91)",
        "hint_en": "Use `sorted(scores, reverse=True)[:3]` and convert back with `tuple()`.",
        "hint_hi": "`sorted(..., reverse=True)` se sort karo aur fir slice `[:3]` lekar `tuple()` me daal do."
    },

    # --- Python: Dictionaries (py_dicts) ---
    {
        "id": "py_q_18",
        "subject": "python",
        "topic": "py_dicts",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Word Frequency Counter",
        "title_hi": "Dictionary Word Count",
        "desc_en": "Given `text = 'python is fun and python is powerful'`. Count word occurrences using a dictionary. Print counts of 'is' and 'python' on separate lines: 'is: 2' and 'python: 2'.",
        "desc_hi": "text = 'python is fun and python is powerful' diya hai. Har word ka count dictionary me rakho. 'is: 2' aur 'python: 2' print karo.",
        "starter_code": "text = 'python is fun and python is powerful'\n# Count word frequencies:\n",
        "solution_code": "text = 'python is fun and python is powerful'\ncounts = {}\nfor w in text.split():\n    counts[w] = counts.get(w, 0) + 1\nprint(f'is: {counts[\"is\"]}')\nprint(f'python: {counts[\"python\"]}')",
        "expected_output": "is: 2\npython: 2",
        "hint_en": "Use `counts.get(w, 0) + 1` inside a loop over `text.split()`.",
        "hint_hi": "`text.split()` se words nikalo aur `counts.get(w, 0) + 1` se counter update karo."
    },
    {
        "id": "py_q_19",
        "subject": "python",
        "topic": "py_dicts",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Roll Number to Name Inverted Lookup",
        "title_hi": "Dictionary Invert Karo",
        "desc_en": "Given `students = {'Alice': 101, 'Bob': 102, 'Charlie': 103}`. Invert it to map roll number to student name. Lookup roll number 102 and print: 'Roll 102 belongs to Bob'.",
        "desc_hi": "students = {'Alice': 101, 'Bob': 102, 'Charlie': 103} diya hai. Isko invert karo taaki roll number se naam mile. Roll 102 lookup karke print karo: 'Roll 102 belongs to Bob'.",
        "starter_code": "students = {'Alice': 101, 'Bob': 102, 'Charlie': 103}\n# Invert dictionary and lookup 102:\n",
        "solution_code": "students = {'Alice': 101, 'Bob': 102, 'Charlie': 103}\nby_roll = {roll: name for name, roll in students.items()}\nprint(f'Roll 102 belongs to {by_roll[102]}')",
        "expected_output": "Roll 102 belongs to Bob",
        "hint_en": "Dictionary comprehension: `{roll: name for name, roll in students.items()}`.",
        "hint_hi": "Dict comprehension use karo: `{v: k for k, v in students.items()}`."
    },
    {
        "id": "py_q_20",
        "subject": "python",
        "topic": "py_dicts",
        "difficulty": "Tricky",
        "xp": 75,
        "title_en": "Gradebook Student Average Calculator",
        "title_hi": "Nested Dictionary Average Marks",
        "desc_en": "Given `grades = {'Rahul': [80, 85, 90], 'Priya': [90, 95, 92], 'Aman': [70, 75, 80]}`. Compute Priya's average marks rounded to 2 decimal places. Print 'Priya average: 92.33'.",
        "desc_hi": "grades = {'Rahul': [80, 85, 90], 'Priya': [90, 95, 92], 'Aman': [70, 75, 80]} diya hai. Priya ka average marks 2 decimal tak round karke print karo: 'Priya average: 92.33'.",
        "starter_code": "grades = {'Rahul': [80, 85, 90], 'Priya': [90, 95, 92], 'Aman': [70, 75, 80]}\n# Calculate Priya's average:\n",
        "solution_code": "grades = {'Rahul': [80, 85, 90], 'Priya': [90, 95, 92], 'Aman': [70, 75, 80]}\npriya_avg = sum(grades['Priya']) / len(grades['Priya'])\nprint(f'Priya average: {priya_avg:.2f}')",
        "expected_output": "Priya average: 92.33",
        "hint_en": "Access Priya's list using `grades['Priya']` and format with `:.2f`.",
        "hint_hi": "`sum(grades['Priya']) / len(grades['Priya'])` karo aur `:.2f` se 2 decimal places format karo."
    },

    # --- Python: Sets (py_sets) ---
    {
        "id": "py_q_21",
        "subject": "python",
        "topic": "py_sets",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Mutual Friends Finder",
        "title_hi": "Dono Dosto Ke Common Friends",
        "desc_en": "Given `rohan_friends = {'Amit', 'Sneha', 'Vikram', 'Pooja'}` and `kabir_friends = {'Vikram', 'Neha', 'Pooja', 'Rahul'}`. Find common friends using set intersection (&). Sort alphabetically and print: \"Mutual Friends: ['Pooja', 'Vikram']\".",
        "desc_hi": "rohan_friends aur kabir_friends sets diye hain. Set intersection (&) se common friends dhoondo, alphabetically sort karo aur print karo: \"Mutual Friends: ['Pooja', 'Vikram']\".",
        "starter_code": "rohan_friends = {'Amit', 'Sneha', 'Vikram', 'Pooja'}\nkabir_friends = {'Vikram', 'Neha', 'Pooja', 'Rahul'}\n# Find intersection and sort:\n",
        "solution_code": "rohan_friends = {'Amit', 'Sneha', 'Vikram', 'Pooja'}\nkabir_friends = {'Vikram', 'Neha', 'Pooja', 'Rahul'}\nmutual = sorted(list(rohan_friends & kabir_friends))\nprint(f'Mutual Friends: {mutual}')",
        "expected_output": "Mutual Friends: ['Pooja', 'Vikram']",
        "hint_en": "Set intersection operator is `&`.",
        "hint_hi": "`rohan_friends & kabir_friends` karke `sorted()` function me pass karo."
    },
    {
        "id": "py_q_22",
        "subject": "python",
        "topic": "py_sets",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Exclusive Tech Stack Comparison",
        "title_hi": "Symmetric Difference of Sets",
        "desc_en": "Given `stack_a = {'Python', 'Django', 'PostgreSQL', 'Docker'}` and `stack_b = {'Python', 'FastAPI', 'PostgreSQL', 'Redis'}`. Find technologies that belong to exactly one stack (symmetric difference ^). Sort alphabetically and print: \"Exclusive tech: ['Django', 'Docker', 'FastAPI', 'Redis']\".",
        "desc_hi": "stack_a aur stack_b sets diye hain. Jo tech sirf ek me ho (symmetric difference ^) unhe nikalo, sort karo aur print karo: \"Exclusive tech: ['Django', 'Docker', 'FastAPI', 'Redis']\".",
        "starter_code": "stack_a = {'Python', 'Django', 'PostgreSQL', 'Docker'}\nstack_b = {'Python', 'FastAPI', 'PostgreSQL', 'Redis'}\n# Find symmetric difference:\n",
        "solution_code": "stack_a = {'Python', 'Django', 'PostgreSQL', 'Docker'}\nstack_b = {'Python', 'FastAPI', 'PostgreSQL', 'Redis'}\nexclusive = sorted(list(stack_a ^ stack_b))\nprint(f'Exclusive tech: {exclusive}')",
        "expected_output": "Exclusive tech: ['Django', 'Docker', 'FastAPI', 'Redis']",
        "hint_en": "Use the symmetric difference operator `^`.",
        "hint_hi": "`stack_a ^ stack_b` se dono ke non-common elements milte hain."
    },

    # --- Python: Functions (py_functions) ---
    {
        "id": "py_q_23",
        "subject": "python",
        "topic": "py_functions",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Factorial Function Calculator",
        "title_hi": "Factorial Function Banao",
        "desc_en": "Write a function `def factorial(n):` that computes the factorial of n. Call it with n = 5 and print: 'Factorial of 5: 120'.",
        "desc_hi": "Ek function `def factorial(n):` banao jo n ka factorial calculate kare. n = 5 ke sath call karke print karo: 'Factorial of 5: 120'.",
        "starter_code": "def factorial(n):\n    # Return factorial\n    pass\n\n# Call and print for n=5:\n",
        "solution_code": "def factorial(n):\n    ans = 1\n    for i in range(1, n + 1):\n        ans *= i\n    return ans\n\nprint(f'Factorial of 5: {factorial(5)}')",
        "expected_output": "Factorial of 5: 120",
        "hint_en": "Initialize ans = 1, loop 1 to n, multiply each step, and return ans.",
        "hint_hi": "1 se n tak loop chalakar multiply karte jao aur answer return karo."
    },
    {
        "id": "py_q_24",
        "subject": "python",
        "topic": "py_functions",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Prime Number Checker Function",
        "title_hi": "Prime Number Function",
        "desc_en": "Write a function `def is_prime(n):` returning True if n is prime, else False. Check n = 29 and print: '29 is prime: True'.",
        "desc_hi": "Function `def is_prime(n):` banao jo check kare ki number prime hai ya nahi. n = 29 test karke print karo: '29 is prime: True'.",
        "starter_code": "def is_prime(n):\n    # Return boolean:\n    pass\n\n# Test with 29:\n",
        "solution_code": "def is_prime(n):\n    if n < 2:\n        return False\n    for i in range(2, int(n ** 0.5) + 1):\n        if n % i == 0:\n            return False\n    return True\n\nprint(f'29 is prime: {is_prime(29)}')",
        "expected_output": "29 is prime: True",
        "hint_en": "A prime number has no divisors between 2 and sqrt(n).",
        "hint_hi": "2 se lekar sqrt(n) tak check karo, agar kisi se divisible nahi hua to Prime hai."
    },
    {
        "id": "py_q_25",
        "subject": "python",
        "topic": "py_functions",
        "difficulty": "Tricky",
        "xp": 75,
        "title_en": "Flexible Bill Calculator with *args",
        "title_hi": "*args Se Flexible Bill Calculate Karo",
        "desc_en": "Write a function `def calculate_bill(*item_prices, tax_percent=5):` that sums all item prices and adds tax percentage. Call with prices 100, 250, 450 and default tax. Print: 'Total Bill: 840.0'.",
        "desc_hi": "Ek function `def calculate_bill(*item_prices, tax_percent=5):` banao jo saare items ka sum kare aur tax jod de. Call karo (100, 250, 450) ke sath aur print karo: 'Total Bill: 840.0'.",
        "starter_code": "def calculate_bill(*item_prices, tax_percent=5):\n    # Sum items and apply tax\n    pass\n\n# Call with 100, 250, 450:\n",
        "solution_code": "def calculate_bill(*item_prices, tax_percent=5):\n    subtotal = sum(item_prices)\n    total = subtotal + (subtotal * tax_percent / 100)\n    return total\n\nprint(f'Total Bill: {calculate_bill(100, 250, 450)}')",
        "expected_output": "Total Bill: 840.0",
        "hint_en": "*args collects all positional arguments into a tuple. `sum(item_prices)` calculates subtotal.",
        "hint_hi": "`*item_prices` se tuple banega, `sum()` karke tax (5%) add kardo."
    },

    # --- Python: Strings (py_strings) ---
    {
        "id": "py_q_26",
        "subject": "python",
        "topic": "py_strings",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Count Vowels in Sentence",
        "title_hi": "Sentence Me Vowels Count Karo",
        "desc_en": "Given `sentence = 'Artificial Intelligence in Python'`. Count how many vowels (a, e, i, o, u case-insensitive) are in the sentence. Print: 'Total Vowels: 12'.",
        "desc_hi": "sentence = 'Artificial Intelligence in Python' diya hai. Isme kul kitne vowels hain count karo aur print karo: 'Total Vowels: 12'.",
        "starter_code": "sentence = 'Artificial Intelligence in Python'\n# Count vowels:\n",
        "solution_code": "sentence = 'Artificial Intelligence in Python'\nvowels = 'aeiouAEIOU'\ncount = sum(1 for ch in sentence if ch in vowels)\nprint(f'Total Vowels: {count}')",
        "expected_output": "Total Vowels: 12",
        "hint_en": "Check each character: `ch in 'aeiouAEIOU'`.",
        "hint_hi": "Loop lagakar check karo `if ch.lower() in 'aeiou'` aur counter badhao."
    },
    {
        "id": "py_q_27",
        "subject": "python",
        "topic": "py_strings",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Clean and Capitalize Full Name",
        "title_hi": "User Name Ko Clean & Format Karo",
        "desc_en": "Given raw dirty input `raw_name = '   eLySiA   cOdE   '`. Strip surrounding spaces, reduce multiple inner spaces to a single space, and capitalize each word in Title Case. Print: 'Formatted Name: Elysia Code'.",
        "desc_hi": "raw_name = '   eLySiA   cOdE   ' diya hai. Extra spaces hatao aur proper Title Case me format karke print karo: 'Formatted Name: Elysia Code'.",
        "starter_code": "raw_name = '   eLySiA   cOdE   '\n# Clean and format:\n",
        "solution_code": "raw_name = '   eLySiA   cOdE   '\nformatted = ' '.join(raw_name.split()).title()\nprint(f'Formatted Name: {formatted}')",
        "expected_output": "Formatted Name: Elysia Code",
        "hint_en": "`' '.join(raw_name.split()).title()` removes extra whitespace and title-cases.",
        "hint_hi": "`raw_name.split()` saari faltu spaces hata deta hai, fir `' '.join()` aur `.title()` lagao."
    },
    {
        "id": "py_q_28",
        "subject": "python",
        "topic": "py_strings",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Anagram String Checker",
        "title_hi": "Anagram String Checker",
        "desc_en": "Given `word1 = 'listen'` and `word2 = 'silent'`. Check if both words are anagrams (same characters rearranged). Print: 'Anagram check: True'.",
        "desc_hi": "word1 = 'listen' aur word2 = 'silent' diya hai. Check karo ki kya dono anagram hain. Print karo: 'Anagram check: True'.",
        "starter_code": "word1 = 'listen'\nword2 = 'silent'\n# Check if sorted characters match:\n",
        "solution_code": "word1 = 'listen'\nword2 = 'silent'\nis_anagram = sorted(word1.lower()) == sorted(word2.lower())\nprint(f'Anagram check: {is_anagram}')",
        "expected_output": "Anagram check: True",
        "hint_en": "Two words are anagrams if `sorted(word1) == sorted(word2)`.",
        "hint_hi": "Dono words ko `sorted()` karke compare karlo."
    },

    # --- Python: Object-Oriented Programming (py_oop) ---
    {
        "id": "py_q_29",
        "subject": "python",
        "topic": "py_oop",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "BankAccount Class with Transactions",
        "title_hi": "BankAccount Class Banao",
        "desc_en": "Create a class `BankAccount` with `__init__(self, owner, balance=0)`, `deposit(self, amount)`, and `withdraw(self, amount)`. Initialize with owner 'Sameer' and balance 1000. Deposit 500, withdraw 300, and print: 'Sameer balance: 1200'.",
        "desc_hi": "Class `BankAccount` banao jisme owner aur balance ho. Deposit(500) aur withdraw(300) call karke print karo: 'Sameer balance: 1200'.",
        "starter_code": "class BankAccount:\n    # Implement methods\n    pass\n\n# Test instance with Sameer, 1000:\n",
        "solution_code": "class BankAccount:\n    def __init__(self, owner, balance=0):\n        self.owner = owner\n        self.balance = balance\n\n    def deposit(self, amount):\n        self.balance += amount\n\n    def withdraw(self, amount):\n        if amount <= self.balance:\n            self.balance -= amount\n\nacc = BankAccount('Sameer', 1000)\nacc.deposit(500)\nacc.withdraw(300)\nprint(f'{acc.owner} balance: {acc.balance}')",
        "expected_output": "Sameer balance: 1200",
        "hint_en": "Define methods on self: `self.balance += amount` and `self.balance -= amount`.",
        "hint_hi": "Class ke andar `__init__`, `deposit` aur `withdraw` methods likho."
    },
    {
        "id": "py_q_30",
        "subject": "python",
        "topic": "py_oop",
        "difficulty": "Tricky",
        "xp": 75,
        "title_en": "Student & MeritScholarship Inheritance",
        "title_hi": "Inheritance & Super() Implementation",
        "desc_en": "Create base class `Student(name, cgpa)` and subclass `ScholarshipStudent(name, cgpa, scholarship_pct)`. Add method `get_details()` returning `'{name} - CGPA: {cgpa} - Scholarship: {scholarship_pct}%'`. Instantiate with ('Aanya', 9.6, 50) and print output.",
        "desc_hi": "Base class `Student` aur child class `ScholarshipStudent` banao using `super()`. 'Aanya', 9.6, 50 ke sath object banakar details print karo: 'Aanya - CGPA: 9.6 - Scholarship: 50%'.",
        "starter_code": "class Student:\n    def __init__(self, name, cgpa):\n        self.name = name\n        self.cgpa = cgpa\n\nclass ScholarshipStudent(Student):\n    # Extend with scholarship_pct using super():\n    pass\n\n# Instantiate and print:\n",
        "solution_code": "class Student:\n    def __init__(self, name, cgpa):\n        self.name = name\n        self.cgpa = cgpa\n\nclass ScholarshipStudent(Student):\n    def __init__(self, name, cgpa, scholarship_pct):\n        super().__init__(name, cgpa)\n        self.scholarship_pct = scholarship_pct\n\n    def get_details(self):\n        return f'{self.name} - CGPA: {self.cgpa} - Scholarship: {self.scholarship_pct}%'\n\ns = ScholarshipStudent('Aanya', 9.6, 50)\nprint(s.get_details())",
        "expected_output": "Aanya - CGPA: 9.6 - Scholarship: 50%",
        "hint_en": "Call `super().__init__(name, cgpa)` in the child constructor.",
        "hint_hi": "Child class me `super().__init__(name, cgpa)` call karna mat bhoolna."
    },

    # --- Python: Exception Handling (py_exceptions) ---
    {
        "id": "py_q_31",
        "subject": "python",
        "topic": "py_exceptions",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Safe Division with Error Handling",
        "title_hi": "ZeroDivisionError Handle Karo",
        "desc_en": "Write a function `safe_divide(a, b)` that divides a by b. If b is 0, handle `ZeroDivisionError` and return 'Cannot divide by zero'. Call with (10, 0) and (10, 2), printing each result on separate lines.",
        "desc_hi": "Function `safe_divide(a, b)` banao. Agar b zero ho to `ZeroDivisionError` handle karke 'Cannot divide by zero' return karo. (10, 0) aur (10, 2) print karo.",
        "starter_code": "def safe_divide(a, b):\n    # Use try-except:\n    pass\n\nprint(safe_divide(10, 0))\nprint(safe_divide(10, 2))\n",
        "solution_code": "def safe_divide(a, b):\n    try:\n        return a / b\n    except ZeroDivisionError:\n        return 'Cannot divide by zero'\n\nprint(safe_divide(10, 0))\nprint(safe_divide(10, 2))",
        "expected_output": "Cannot divide by zero\n5.0",
        "hint_en": "Wrap division in `try:` and catch with `except ZeroDivisionError:`.",
        "hint_hi": "`try:` ke andar divide karo aur `except ZeroDivisionError:` me error message return karo."
    },
    {
        "id": "py_q_32",
        "subject": "python",
        "topic": "py_exceptions",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Custom InvalidAge Exception",
        "title_hi": "Custom Exception Raise Karo",
        "desc_en": "Define a custom exception `class InvalidAgeError(Exception): pass`. Write function `check_voting_age(age)` that raises `InvalidAgeError('Under 18 not allowed')` if age < 18, else returns 'Eligible'. In a try-except block, check age = 16 and catch the error to print: 'Caught: Under 18 not allowed'.",
        "desc_hi": "Custom exception `InvalidAgeError` define karo. Agar age < 18 ho to use raise karo. age = 16 ke sath catch karke print karo: 'Caught: Under 18 not allowed'.",
        "starter_code": "class InvalidAgeError(Exception):\n    pass\n\ndef check_voting_age(age):\n    # Raise if < 18\n    pass\n\n# Catch and print:\n",
        "solution_code": "class InvalidAgeError(Exception):\n    pass\n\ndef check_voting_age(age):\n    if age < 18:\n        raise InvalidAgeError('Under 18 not allowed')\n    return 'Eligible'\n\ntry:\n    check_voting_age(16)\nexcept InvalidAgeError as e:\n    print(f'Caught: {e}')",
        "expected_output": "Caught: Under 18 not allowed",
        "hint_en": "Use `raise InvalidAgeError('...')` and catch with `except InvalidAgeError as e:`.",
        "hint_hi": "`raise InvalidAgeError(...)` likho aur `except InvalidAgeError as e:` se catch karke `{e}` print karo."
    },

    # --- Python: File Handling & Parsing (py_files) ---
    {
        "id": "py_q_33",
        "subject": "python",
        "topic": "py_files",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Server Access Log Line Parser",
        "title_hi": "Log File Line Parse Karo",
        "desc_en": "Given raw log line: `log_line = '2026-10-12 14:32:10 [INFO] User admin logged in from IP 192.168.1.1'`. Extract the level inside brackets and the IP address. Print: 'Level: INFO, IP: 192.168.1.1'.",
        "desc_hi": "log_line = '2026-10-12 14:32:10 [INFO] User admin logged in from IP 192.168.1.1' diya hai. Level aur IP extract karke print karo: 'Level: INFO, IP: 192.168.1.1'.",
        "starter_code": "log_line = '2026-10-12 14:32:10 [INFO] User admin logged in from IP 192.168.1.1'\n# Extract level and IP:\n",
        "solution_code": "log_line = '2026-10-12 14:32:10 [INFO] User admin logged in from IP 192.168.1.1'\nparts = log_line.split()\nlevel = parts[2].strip('[]')\nip = parts[-1]\nprint(f'Level: {level}, IP: {ip}')",
        "expected_output": "Level: INFO, IP: 192.168.1.1",
        "hint_en": "Split the line: parts[2] has '[INFO]' and parts[-1] has the IP.",
        "hint_hi": "`log_line.split()` se words nikalo, `[INFO]`.strip('[]') se level aur last element se IP milega."
    },
    {
        "id": "py_q_34",
        "subject": "python",
        "topic": "py_files",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "CSV Student Record Line Formatter",
        "title_hi": "CSV Data Parse Karo",
        "desc_en": "Given CSV rows: `csv_data = 'Roll,Name,Marks\\n101,Rohan,85\\n102,Simran,92'`. Split the lines, parse each row, and calculate the total marks of all students (85 + 92 = 177). Print: 'Total Student Marks: 177'.",
        "desc_hi": "csv_data diya hai. Lines split karke header skip karo aur saare students ke marks ka total calculate karo. Print karo: 'Total Student Marks: 177'.",
        "starter_code": "csv_data = 'Roll,Name,Marks\\n101,Rohan,85\\n102,Simran,92'\n# Parse CSV and sum marks:\n",
        "solution_code": "csv_data = 'Roll,Name,Marks\\n101,Rohan,85\\n102,Simran,92'\nlines = csv_data.strip().split('\\n')\ntotal_marks = 0\nfor line in lines[1:]:\n    roll, name, marks = line.split(',')\n    total_marks += int(marks)\nprint(f'Total Student Marks: {total_marks}')",
        "expected_output": "Total Student Marks: 177",
        "hint_en": "Skip the header using `lines[1:]` and convert marks with `int(marks)`.",
        "hint_hi": "Header line ko skip karo `lines[1:]`, comma `,` par split karke marks ko `int()` me badlo."
    },

    # =========================================================================
    # HTML & CSS QUESTIONS
    # =========================================================================

    # --- HTML: Semantic Tags & Structure (html_tags) ---
    {
        "id": "html_q_1",
        "subject": "html",
        "topic": "html_tags",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Profile Badge Card",
        "title_hi": "Profile Badge Card",
        "desc_en": "Create a card with a main heading `<h1>Alex Doe</h1>`, a subtitle `<p>Computer Science Undergrad</p>`, and an unordered list `<ul>` with 2 skills: `<li>Python</li>` and `<li>HTML5</li>`.",
        "desc_hi": "Ek card banao jisme heading `<h1>Alex Doe</h1>`, paragraph `<p>Computer Science Undergrad</p>`, aur unordered list `<ul>` ho jisme do items `<li>Python</li>` aur `<li>HTML5</li>` hon.",
        "starter_code": "<div class=\"profile-card\">\n  <!-- Add h1, p, and ul with 2 li tags here -->\n</div>\n",
        "solution_code": "<div class=\"profile-card\">\n  <h1>Alex Doe</h1>\n  <p>Computer Science Undergrad</p>\n  <ul>\n    <li>Python</li>\n    <li>HTML5</li>\n  </ul>\n</div>",
        "expected_html_elements": ["h1", "p", "ul", "li"],
        "hint_en": "Wrap the skills inside <ul> and individual skills inside <li>.",
        "hint_hi": "List ke liye `<ul>` banao aur uske andar do `<li>` tags daalo."
    },
    {
        "id": "html_q_5",
        "subject": "html",
        "topic": "html_tags",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Semantic Site Navigation Header",
        "title_hi": "Semantic Navbar Header Banao",
        "desc_en": "Build a semantic website navigation header using `<header>`, `<nav>`, and an unordered list `<ul>` with 3 navigation links `<a>` ('Home', 'Learn', 'Contact').",
        "desc_hi": "Semantic header `<header>`, `<nav>`, `<ul>`, `<li>` aur `<a>` tags use karke 3 links wala navbar banao.",
        "starter_code": "<!-- Create semantic header, nav, ul, li, and a links -->\n",
        "solution_code": "<header>\n  <nav>\n    <ul>\n      <li><a href=\"#home\">Home</a></li>\n      <li><a href=\"#learn\">Learn</a></li>\n      <li><a href=\"#contact\">Contact</a></li>\n    </ul>\n  </nav>\n</header>",
        "expected_html_elements": ["header", "nav", "ul", "li", "a"],
        "hint_en": "Nest tags: <header> -> <nav> -> <ul> -> <li> -> <a>.",
        "hint_hi": "<header> ke andar <nav>, uske andar <ul> aur <li> me <a> tags daalo."
    },
    {
        "id": "html_q_8",
        "subject": "html",
        "topic": "html_tags",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Semantic Blog Post Layout",
        "title_hi": "Semantic Article & Footer Layout",
        "desc_en": "Create a semantic blog post layout using `<article>`, `<section>`, `<h2>Title</h2>`, `<p>Body text</p>`, and `<footer>Written by Elysia</footer>`.",
        "desc_hi": "Blog post ke liye semantic tags `<article>`, `<section>`, `<h2>`, `<p>`, aur `<footer>` use karke layout taiyar karo.",
        "starter_code": "<!-- Add article, section, h2, p, and footer -->\n",
        "solution_code": "<article>\n  <section>\n    <h2>Learning Modern Web Development</h2>\n    <p>Semantic tags improve accessibility and SEO for web applications.</p>\n  </section>\n  <footer>Written by Elysia</footer>\n</article>",
        "expected_html_elements": ["article", "section", "h2", "p", "footer"],
        "hint_en": "Place <section> with <h2> and <p> inside <article>, followed by <footer>.",
        "hint_hi": "<article> ke andar <section> aur <footer> banao."
    },
    {
        "id": "html_q_10",
        "subject": "html",
        "topic": "html_tags",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Native Interactive FAQ Accordion",
        "title_hi": "Details and Summary FAQ",
        "desc_en": "Create an interactive native accordion using `<details>` and `<summary>` containing a question heading in summary and answer in a `<p>` tag.",
        "desc_hi": "Bina JavaScript ke interactive FAQ accordion banao using `<details>`, `<summary>` aur `<p>` tags.",
        "starter_code": "<!-- Create details and summary accordion with p tag -->\n",
        "solution_code": "<details>\n  <summary>What is Python?</summary>\n  <p>Python is a high-level, interpreted programming language with easy syntax.</p>\n</details>",
        "expected_html_elements": ["details", "summary", "p"],
        "hint_en": "<summary> goes inside <details> as the clickable toggle title.",
        "hint_hi": "<details> ke andar pehla element <summary> hota hai, uske baad <p> content."
    },

    # --- HTML: Forms & User Inputs (html_forms) ---
    {
        "id": "html_q_2",
        "subject": "html",
        "topic": "html_forms",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "College Fest Ticket Booking Form",
        "title_hi": "College Fest Ticket Booking Form",
        "desc_en": "Create a form with an input for student name (type='text', name='name'), an input for tickets quantity (type='number', name='tickets', min='1', max='5'), and a submit button with text 'Book Passes'.",
        "desc_hi": "Ek booking form banao jisme student name input ho (type='text', name='name'), tickets quantity input ho (type='number', name='tickets', min='1', max='5'), aur submit button ho jiska text 'Book Passes' ho.",
        "starter_code": "<form action=\"/book\" method=\"POST\">\n  <!-- Add text input, number input, and submit button -->\n</form>\n",
        "solution_code": "<form action=\"/book\" method=\"POST\">\n  <input type=\"text\" name=\"name\" placeholder=\"Your Name\" required>\n  <input type=\"number\" name=\"tickets\" min=\"1\" max=\"5\" value=\"1\">\n  <button type=\"submit\">Book Passes</button>\n</form>",
        "expected_html_elements": ["form", "input", "button"],
        "hint_en": "Ensure you have two <input> tags and one <button type='submit'>.",
        "hint_hi": "Do `<input>` tags daalo aur ek `<button type='submit'>` button banao."
    },
    {
        "id": "html_q_6",
        "subject": "html",
        "topic": "html_forms",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Student Feedback Form with Radio & Select",
        "title_hi": "Feedback Form with Radio & Dropdown",
        "desc_en": "Create a `<form>` containing a `<select>` dropdown with 2 `<option>` elements, a radio input `<input type='radio'>` for rating, and a `<button>` submit.",
        "desc_hi": "Ek `<form>` banao jisme `<select>` dropdown (2 `<option>` ke sath), radio `<input type='radio'>` aur ek `<button>` submit ho.",
        "starter_code": "<form>\n  <!-- Add select with options, radio input, and submit button -->\n</form>\n",
        "solution_code": "<form>\n  <select name=\"subject\">\n    <option value=\"py\">Python</option>\n    <option value=\"html\">HTML5</option>\n  </select>\n  <label>\n    <input type=\"radio\" name=\"rating\" value=\"5\"> Excellent\n  </label>\n  <button type=\"submit\">Submit Feedback</button>\n</form>",
        "expected_html_elements": ["form", "select", "option", "input", "button"],
        "hint_en": "Inside <form>, include <select>, <option>, <input type='radio'>, and <button>.",
        "hint_hi": "<form> ke andar dropdown ke liye <select> aur options daalo, sath me radio button aur submit button."
    },

    # --- HTML: Tables & Data Grids (html_tables) ---
    {
        "id": "html_q_3",
        "subject": "html",
        "topic": "html_tables",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "College Timetable Schedule Table",
        "title_hi": "College Timetable Table Banao",
        "desc_en": "Create an HTML table with `<table>`, `<thead>`, `<tbody>`, rows `<tr>`, header cells `<th>` ('Day', 'Subject', 'Time'), and at least 2 data rows with `<td>` cells.",
        "desc_hi": "HTML table banao with `<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, aur `<td>` tags.",
        "starter_code": "<!-- Build a schedule table with table, thead, tbody, tr, th, td -->\n",
        "solution_code": "<table>\n  <thead>\n    <tr>\n      <th>Day</th>\n      <th>Subject</th>\n      <th>Time</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Monday</td>\n      <td>Python Lab</td>\n      <td>10:00 AM</td>\n    </tr>\n    <tr>\n      <td>Tuesday</td>\n      <td>Web Dev</td>\n      <td>02:00 PM</td>\n    </tr>\n  </tbody>\n</table>",
        "expected_html_elements": ["table", "thead", "tbody", "tr", "th", "td"],
        "hint_en": "Remember: <th> is for headers in <thead>, <td> is for data cells in <tbody>.",
        "hint_hi": "Header cells ke liye `<th>` aur normal cells ke liye `<td>` tag lagao."
    },
    {
        "id": "html_q_9",
        "subject": "html",
        "topic": "html_tables",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Student Marks Report Card Table",
        "title_hi": "Marksheet Table with tfoot",
        "desc_en": "Create an HTML table with `<table>`, `<thead>`, `<tbody>`, and `<tfoot>` showing total marks in `<tfoot>`.",
        "desc_hi": "Report card table banao jisme `<table>`, `<thead>`, `<tbody>`, `<tfoot>`, `<tr>`, `th` aur `<td>` shamil hon.",
        "starter_code": "<!-- Build table with thead, tbody, tfoot, tr, td -->\n",
        "solution_code": "<table>\n  <thead>\n    <tr><th>Subject</th><th>Marks</th></tr>\n  </thead>\n  <tbody>\n    <tr><td>Python</td><td>95</td></tr>\n  </tbody>\n  <tfoot>\n    <tr><td>Total</td><td>95</td></tr>\n  </tfoot>\n</table>",
        "expected_html_elements": ["table", "thead", "tbody", "tfoot", "tr", "th", "td"],
        "hint_en": "Include all structural sections: thead, tbody, and tfoot.",
        "hint_hi": "Table ke teeno parts daalo: thead, tbody aur tfoot."
    },

    # --- HTML: Media, Images & Audio (html_media) ---
    {
        "id": "html_q_4",
        "subject": "html",
        "topic": "html_media",
        "difficulty": "Beginner",
        "xp": 30,
        "title_en": "Responsive Media Card (Image & Audio)",
        "title_hi": "Image aur Audio Tag Card",
        "desc_en": "Create a media card containing a `<div>`, an `<img>` tag with `src='avatar.png'` and `alt='User Avatar'`, and an `<audio>` tag with `controls` attribute.",
        "desc_hi": "Ek media card `<div>` banao jisme `<img>` (src aur alt attribute ke sath) aur `<audio controls>` tag ho.",
        "starter_code": "<div class=\"media-card\">\n  <!-- Add img with src/alt, and audio with controls -->\n</div>\n",
        "solution_code": "<div class=\"media-card\">\n  <img src=\"avatar.png\" alt=\"User Avatar\">\n  <audio controls src=\"podcast.mp3\"></audio>\n</div>",
        "expected_html_elements": ["div", "img", "audio"],
        "hint_en": "Use `<img src=\"...\" alt=\"...\">` and `<audio controls src=\"...\"></audio>`.",
        "hint_hi": "`<img>` me src aur alt attributes daalo, aur `<audio>` me controls attribute zaroori hai."
    },

    # --- HTML / CSS: Styling & Layouts (css_basics) ---
    {
        "id": "html_q_7",
        "subject": "html",
        "topic": "css_basics",
        "difficulty": "Intermediate",
        "xp": 50,
        "title_en": "Product Pricing Tier Card with Embedded CSS",
        "title_hi": "Pricing Card with <style> Tags",
        "desc_en": "Create a pricing card with a `<style>` block defining `.pricing-box { display: flex; }`, and a container `<div class='pricing-box'>` containing an `<h2>Tier Pro</h2>` and `<button>Subscribe</button>`.",
        "desc_hi": "Ek pricing card banao jisme `<style>` tag ho, container `<div class='pricing-box'>`, `<h2>` title aur `<button>` button ho.",
        "starter_code": "<!-- Add style tag with .pricing-box, div, h2, and button -->\n",
        "solution_code": "<style>\n  .pricing-box { display: flex; flex-direction: column; padding: 20px; }\n</style>\n<div class=\"pricing-box\">\n  <h2>Tier Pro</h2>\n  <button>Subscribe</button>\n</div>",
        "expected_html_elements": ["style", "div", "h2", "button"],
        "hint_en": "Define CSS inside <style> and apply it to a <div> containing <h2> and <button>.",
        "hint_hi": "<style> tag ke andar CSS likho aur <div> ke andar <h2> aur <button> daalo."
    }
]

import functools


@functools.lru_cache(maxsize=256)
def _get_filtered_tuple(subject: str, topic: str, difficulty: str) -> tuple:
    filtered = [q for q in QUESTIONS_DATABASE if q["subject"].lower() == subject.lower()]
    if topic and topic.lower() != "all":
        filtered = [q for q in filtered if q["topic"].lower() == topic.lower()]
    if difficulty and difficulty.lower() != "all":
        filtered = [q for q in filtered if q["difficulty"].lower() == difficulty.lower()]
    return tuple(filtered)


def get_questions(subject: str = "python", topic: str = "all", difficulty: str = "all", count: int = 5) -> List[Dict[str, Any]]:
    """Filters questions according to user's criteria with LRU caching."""
    cached_list = list(_get_filtered_tuple(str(subject or "python"), str(topic or "all"), str(difficulty or "all")))
    if len(cached_list) <= count:
        return cached_list
    return random.sample(cached_list, count)
