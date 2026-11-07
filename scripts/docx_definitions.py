# DOCX Semester Assignment Questions (Q1 to Q45) definitions

DOCX_DETAILS = {
    "Q1": {
        "inp": "2000\n2500\n1000",
        "starter": "consultation = 2000\nmedicine = 2500\nlab_test = 1000\n# Calculate total bill and apply 5% discount if total exceeds 5000:\n",
        "solution": "consultation = 2000\nmedicine = 2500\nlab_test = 1000\ntotal = consultation + medicine + lab_test\ndiscount = total * 0.05 if total > 5000 else 0\nnet_bill = total - discount\nprint(f\"Total bill: Rs {total:.2f}\")\nprint(f\"Discount: Rs {discount:.2f}\")\nprint(f\"Net payable: Rs {net_bill:.2f}\")",
        "out": "Total bill: Rs 5500.00\nDiscount: Rs 275.00\nNet payable: Rs 5225.00",
        "hint": "Add the three charges. If total > 5000, discount = total * 0.05."
    },
    "Q2": {
        "inp": "120",
        "starter": "units = 120\n# Calculate water bill based on slabs (first 50 @ 1, next 50 @ 2, above 100 @ 3):\n",
        "solution": "units = 120\nif units <= 50:\n    bill = units * 1\nelif units <= 100:\n    bill = 50 * 1 + (units - 50) * 2\nelse:\n    bill = 50 * 1 + 50 * 2 + (units - 100) * 3\nprint(f\"Water consumption: {units} units\")\nprint(f\"Total bill: Rs {bill:.2f}\")",
        "out": "Water consumption: 120 units\nTotal bill: Rs 210.00",
        "hint": "Use if-elif-else slabs: first 50 at Rs 1, next 50 at Rs 2, remainder at Rs 3."
    },
    "Q3": {
        "inp": "88",
        "starter": "marks = 88\n# Display scholarship percentage based on marks:\n",
        "solution": "marks = 88\nif marks >= 95:\n    scholarship = \"100%\"\nelif marks >= 85:\n    scholarship = \"75%\"\nelif marks >= 75:\n    scholarship = \"50%\"\nelse:\n    scholarship = \"No scholarship\"\nprint(f\"Marks: {marks}\")\nprint(f\"Scholarship: {scholarship}\")",
        "out": "Marks: 88\nScholarship: 75%",
        "hint": "Check marks >= 95 (100%), >= 85 (75%), >= 75 (50%), else None."
    },
    "Q4": {
        "inp": "18",
        "starter": "distance = 18\n# Calculate cab fare: Rs 50 for first 5km, Rs 12/km for next 10km, Rs 10/km beyond 15km:\n",
        "solution": "distance = 18\nif distance <= 5:\n    fare = 50\nelif distance <= 15:\n    fare = 50 + (distance - 5) * 12\nelse:\n    fare = 50 + 10 * 12 + (distance - 15) * 10\nprint(f\"Distance: {distance} km\")\nprint(f\"Total fare: Rs {fare:.2f}\")",
        "out": "Distance: 18 km\nTotal fare: Rs 200.00",
        "hint": "Calculate fare in stages: first 5km (50), next 10km (12/km), extra (10/km)."
    },
    "Q5": {
        "inp": "2.4",
        "starter": "daily_limit = 2.0\ndata_consumed = 2.4\n# Calculate remaining data or additional data consumed:\n",
        "solution": "daily_limit = 2.0\ndata_consumed = 2.4\nif data_consumed <= daily_limit:\n    remaining = daily_limit - data_consumed\n    print(f\"Data remaining: {remaining:.2f} GB\")\nelse:\n    extra = data_consumed - daily_limit\n    print(f\"Data limit exceeded! Additional consumed: {extra:.2f} GB\")",
        "out": "Data limit exceeded! Additional consumed: 0.40 GB",
        "hint": "Compare data consumed with 2.0 GB limit."
    },
    "Q6": {
        "inp": "general\n3",
        "starter": "ticket_type = 'general'\nquantity = 3\n# Ticket prices: platform=10, general=50, reserved=150. Calculate total:\n",
        "solution": "ticket_type = 'general'\nquantity = 3\nrates = {'platform': 10, 'general': 50, 'reserved': 150}\nrate = rates.get(ticket_type, 0)\ntotal = rate * quantity\nprint(f\"Ticket type: {ticket_type.capitalize()}\")\nprint(f\"Quantity: {quantity}\")\nprint(f\"Total cost: Rs {total}\")",
        "out": "Ticket type: General\nQuantity: 3\nTotal cost: Rs 150",
        "hint": "Use a dictionary or if-elif to look up ticket rates."
    },
    "Q7": {
        "inp": "65 58 72 60 55 80 62 59 70 64",
        "starter": "speeds = [65, 58, 72, 60, 55, 80, 62, 59, 70, 64]\nspeed_limit = 60\n# Count vehicles exceeding permitted speed of 60 km/h:\n",
        "solution": "speeds = [65, 58, 72, 60, 55, 80, 62, 59, 70, 64]\nspeed_limit = 60\noverspeeding = sum(1 for s in speeds if s > speed_limit)\nprint(f\"Total vehicles inspected: {len(speeds)}\")\nprint(f\"Vehicles overspeeding (> {speed_limit} km/h): {overspeeding}\")",
        "out": "Total vehicles inspected: 10\nVehicles overspeeding (> 60 km/h): 6",
        "hint": "Count speeds strictly greater than 60."
    },
    "Q8": {
        "inp": "500 750 400 600 350",
        "starter": "intake_log = [500, 750, 400, 600, 350]\n# Calculate total water consumed and check if minimum 2000 ml target met:\n",
        "solution": "intake_log = [500, 750, 400, 600, 350]\ntotal_ml = sum(intake_log)\nprint(f\"Total water consumed: {total_ml} ml\")\nif total_ml >= 2000:\n    print(\"Target achieved: Daily hydration goal completed!\")\nelse:\n    print(f\"Target not met: Need {2000 - total_ml} ml more.\")",
        "out": "Total water consumed: 2600 ml\nTarget achieved: Daily hydration goal completed!",
        "hint": "Sum the intakes and compare against 2000 ml."
    },
    "Q9": {
        "inp": "2\n7",
        "starter": "current_floor = 2\ndesired_floor = 7\n# Validate floors (0-10) and determine direction (Up, Down, Same floor):\n",
        "solution": "current_floor = 2\ndesired_floor = 7\nif not (0 <= current_floor <= 10 and 0 <= desired_floor <= 10):\n    print(\"Invalid floor entered\")\nelif desired_floor > current_floor:\n    print(f\"Elevator moving UP from floor {current_floor} to floor {desired_floor}\")\nelif desired_floor < current_floor:\n    print(f\"Elevator moving DOWN from floor {current_floor} to floor {desired_floor}\")\nelse:\n    print(\"Already on desired floor\")",
        "out": "Elevator moving UP from floor 2 to floor 7",
        "hint": "Compare desired_floor with current_floor."
    },
    "Q10": {
        "inp": "0 1 0 0 1 0 0 1 0 0 0 1 0 0 0",
        "starter": "inspections = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]\n# Count defective (1) and non-defective (0) products:\n",
        "solution": "inspections = [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0]\ndefective = sum(1 for item in inspections if item == 1)\nnon_defective = len(inspections) - defective\nprint(f\"Defective products: {defective}\")\nprint(f\"Non-defective products: {non_defective}\")",
        "out": "Defective products: 4\nNon-defective products: 11",
        "hint": "Count 1s and 0s in the list."
    },
    "Q11": {
        "inp": "DL01A1234",
        "starter": "vehicles = ['KA05C1111', 'DL01A1234', 'MH02B9999', 'UP16Z5555', 'TN09D4321']\nsearch_num = 'DL01A1234'\n# Search for registration number in list:\n",
        "solution": "vehicles = ['KA05C1111', 'DL01A1234', 'MH02B9999', 'UP16Z5555', 'TN09D4321']\nsearch_num = 'DL01A1234'\nif search_num in vehicles:\n    idx = vehicles.index(search_num) + 1\n    print(f\"Vehicle {search_num} found at position {idx}\")\nelse:\n    print(\"Vehicle not found\")",
        "out": "Vehicle DL01A1234 found at position 2",
        "hint": "Use 'in' keyword and list.index()."
    },
    "Q12": {
        "inp": "45 12 8 60 4 25 10 3",
        "starter": "stock = [45, 12, 8, 60, 4, 25, 10, 3]\nthreshold = 10\n# Find products with stock below threshold:\n",
        "solution": "stock = [45, 12, 8, 60, 4, 25, 10, 3]\nthreshold = 10\nlow_stock = [(i+1, qty) for i, qty in enumerate(stock) if qty < threshold]\nprint(f\"Low stock items count: {len(low_stock)}\")\nfor prod_id, qty in low_stock:\n    print(f\"Product {prod_id}: {qty} units\")",
        "out": "Low stock items count: 3\nProduct 3: 8 units\nProduct 5: 4 units\nProduct 8: 3 units",
        "hint": "Enumerate the stock list and filter items < threshold."
    },
    "Q13": {
        "inp": "student@university.edu",
        "starter": "email = 'student@university.edu'\n# Validate that email contains '@' and '.' after '@':\n",
        "solution": "email = 'student@university.edu'\nif '@' in email and '.' in email[email.find('@'):]:\n    print(\"Valid email address\")\nelse:\n    print(\"Invalid email address\")",
        "out": "Valid email address",
        "hint": "Check for '@' in string and '.' appearing after '@'."
    },
    "Q14": {
        "inp": "4 5 3 4 5 2 4 5 3 5",
        "starter": "ratings = [4, 5, 3, 4, 5, 2, 4, 5, 3, 5]\n# Calculate average rating, highest rating, and 5-star count:\n",
        "solution": "ratings = [4, 5, 3, 4, 5, 2, 4, 5, 3, 5]\navg_rating = sum(ratings) / len(ratings)\nfive_stars = ratings.count(5)\nprint(f\"Average rating: {avg_rating:.1f}\")\nprint(f\"Highest rating: {max(ratings)}\")\nprint(f\"5-star ratings count: {five_stars}\")",
        "out": "Average rating: 4.0\nHighest rating: 5\n5-star ratings count: 4",
        "hint": "Use sum/len for average, max(), and list.count(5)."
    },
    "Q15": {
        "inp": "Python Programming is Essential",
        "starter": "sentence = 'Python Programming is Essential'\n# Display total characters, vowels count, and consonants count:\n",
        "solution": "sentence = 'Python Programming is Essential'\nvowels = sum(1 for ch in sentence.lower() if ch in 'aeiou')\nconsonants = sum(1 for ch in sentence.lower() if ch.isalpha() and ch not in 'aeiou')\nprint(f\"Total characters: {len(sentence)}\")\nprint(f\"Vowels: {vowels}\")\nprint(f\"Consonants: {consonants}\")",
        "out": "Total characters: 31\nVowels: 9\nConsonants: 19",
        "hint": "Check isalpha() and whether letter is in 'aeiou'."
    },
    "Q16": {
        "inp": "8374",
        "starter": "code = 8374\n# Calculate number of digits, sum of digits, and reverse of the number:\n",
        "solution": "code = 8374\ns = str(code)\ncount = len(s)\ntotal = sum(int(d) for d in s)\nrev = s[::-1]\nprint(f\"Digit count: {count}\")\nprint(f\"Digit sum: {total}\")\nprint(f\"Reversed code: {rev}\")",
        "out": "Digit count: 4\nDigit sum: 22\nReversed code: 4738",
        "hint": "Convert to string to count, sum, and reverse."
    },
    "Q17": {
        "inp": "144",
        "starter": "number = 144\n# Check if number is a perfect square:\n",
        "solution": "import math\nnumber = 144\nroot = math.isqrt(number)\nif root * root == number:\n    print(f\"Access granted: {number} is a perfect square (root = {root})\")\nelse:\n    print(f\"Access denied: {number} is not a perfect square\")",
        "out": "Access granted: 144 is a perfect square (root = 12)",
        "hint": "Use math.isqrt(n) and verify root * root == n."
    },
    "Q18": {
        "inp": "10000\n5\n3",
        "starter": "initial_pop = 10000\ngrowth_rate = 5\nyears = 3\n# Calculate population growth year by year:\n",
        "solution": "pop = 10000\nrate = 0.05\nfor yr in range(1, 4):\n    pop = pop + pop * rate\n    print(f\"Year {yr}: {int(pop)}\")",
        "out": "Year 1: 10500\nYear 2: 11025\nYear 3: 11576",
        "hint": "Compound population year by year."
    },
    "Q19": {
        "inp": "45000",
        "starter": "def calculate_pf(basic_salary):\n    # Return 12% PF contribution\n    pass\n\nsalary = 45000\n",
        "solution": "def calculate_pf(basic_salary):\n    return basic_salary * 0.12\n\nsalary = 45000\npf = calculate_pf(salary)\nprint(f\"Basic salary: Rs {salary:.2f}\")\nprint(f\"PF contribution (12%): Rs {pf:.2f}\")",
        "out": "Basic salary: Rs 45000.00\nPF contribution (12%): Rs 5400.00",
        "hint": "Define calculate_pf(basic_salary) returning basic_salary * 0.12."
    },
    "Q20": {
        "inp": "800000",
        "starter": "def calculate_premium(vehicle_price):\n    # Return 3% insurance premium\n    pass\n\nprice = 800000\n",
        "solution": "def calculate_premium(vehicle_price):\n    return vehicle_price * 0.03\n\nprice = 800000\npremium = calculate_premium(price)\nprint(f\"Vehicle price: Rs {price:.2f}\")\nprint(f\"Insurance premium (3%): Rs {premium:.2f}\")",
        "out": "Vehicle price: Rs 800000.00\nInsurance premium (3%): Rs 24000.00",
        "hint": "Return vehicle_price * 0.03."
    },
    "Q21": {
        "inp": "500\n120",
        "starter": "def check_book(total_books, issued_books):\n    # Return available books\n    pass\n\ntotal = 500\nissued = 120\n",
        "solution": "def check_book(total_books, issued_books):\n    return total_books - issued_books\n\ntotal = 500\nissued = 120\navailable = check_book(total, issued)\nprint(f\"Total books: {total}\")\nprint(f\"Issued books: {issued}\")\nprint(f\"Available books: {available}\")",
        "out": "Total books: 500\nIssued books: 120\nAvailable books: 380",
        "hint": "Subtract issued_books from total_books."
    },
    "Q22": {
        "inp": "8300\n100",
        "starter": "def inr_to_usd(inr, rate=83.0):\n    pass\n\ndef usd_to_inr(usd, rate=83.0):\n    pass\n",
        "solution": "def inr_to_usd(inr, rate=83.0):\n    return inr / rate\n\ndef usd_to_inr(usd, rate=83.0):\n    return usd * rate\n\nprint(f\"Rs 8300 in USD: ${inr_to_usd(8300):.2f}\")\nprint(f\"$100 in INR: Rs {usd_to_inr(100):.2f}\")",
        "out": "Rs 8300 in USD: $100.00\n$100 in INR: Rs 8300.00",
        "hint": "Divide INR by exchange rate for USD; multiply USD by rate for INR."
    },
    "Q23": {
        "inp": "circle 7",
        "starter": "import math\ndef area_circle(r): pass\ndef area_rectangle(l, w): pass\ndef area_triangle(b, h): pass\n",
        "solution": "import math\ndef area_circle(r):\n    return math.pi * r * r\n\nradius = 7\nprint(f\"Circle area (r={radius}): {area_circle(radius):.2f}\")",
        "out": "Circle area (r=7): 153.94",
        "hint": "Use math.pi * r * r for circle."
    },
    "Q24": {
        "inp": "28",
        "starter": "age = 28\n# Categorize applicant: <18 Not eligible, 18-30 Category A, 31-50 Category B, >50 Category C:\n",
        "solution": "age = 28\nif age < 18:\n    cat = \"Not eligible\"\nelif age <= 30:\n    cat = \"Category A\"\nelif age <= 50:\n    cat = \"Category B\"\nelse:\n    cat = \"Category C\"\nprint(f\"Age: {age}\")\nprint(f\"Eligibility: {cat}\")",
        "out": "Age: 28\nEligibility: Category A",
        "hint": "Use if-elif-else on age boundaries."
    },
    "Q25": {
        "inp": "100\n15 4 8 2",
        "starter": "capacity = 100\nentries = 15\nexits = 4\n# Calculate available parking slots:\n",
        "solution": "capacity = 100\noccupied = 15 - 4\navailable = capacity - occupied\nprint(f\"Total capacity: {capacity}\")\nprint(f\"Current occupancy: {occupied}\")\nprint(f\"Available slots: {available}\")",
        "out": "Total capacity: 100\nCurrent occupancy: 11\nAvailable slots: 89",
        "hint": "Available = capacity - (entries - exits)."
    },
    "Q26": {
        "inp": "250 180 320 90 410",
        "starter": "calories = [250, 180, 320, 90, 410]\n# Calculate total calories and highest calorie item:\n",
        "solution": "calories = [250, 180, 320, 90, 410]\nprint(f\"Total calorie intake: {sum(calories)} kcal\")\nprint(f\"Highest calorie item: {max(calories)} kcal\")",
        "out": "Total calorie intake: 1250 kcal\nHighest calorie item: 410 kcal",
        "hint": "Use sum() and max()."
    },
    "Q27": {
        "inp": "300 450 350",
        "starter": "max_capacity = 1000\nwater_added = [300, 450, 350]\n# Monitor tank filling until full or overflow:\n",
        "solution": "current = 0\nmax_capacity = 1000\nfor qty in [300, 450, 350]:\n    if current + qty > max_capacity:\n        print(f\"Overflow warning! Cannot add {qty} L\")\n        break\n    current += qty\n    print(f\"Added {qty} L. Current level: {current} / {max_capacity} L\")",
        "out": "Added 300 L. Current level: 300 / 1000 L\nAdded 450 L. Current level: 750 / 1000 L\nOverflow warning! Cannot add 350 L",
        "hint": "Check if current + qty exceeds max capacity."
    },
    "Q28": {
        "inp": "1111 2222 4567",
        "starter": "attempts = ['1111', '2222', '4567']\ncorrect_pin = '4567'\n# Authenticate PIN with max 3 attempts:\n",
        "solution": "correct_pin = '4567'\nfor attempt in ['1111', '2222', '4567']:\n    if attempt == correct_pin:\n        print(\"PIN verified: Access granted\")\n        break\n    else:\n        print(f\"Incorrect PIN: {attempt}\")",
        "out": "Incorrect PIN: 1111\nIncorrect PIN: 2222\nPIN verified: Access granted",
        "hint": "Break loop when correct_pin is entered."
    },
    "Q29": {
        "inp": "12.5 14.0 11.8 15.2 13.0 16.5 10.0",
        "starter": "daily_units = [12.5, 14.0, 11.8, 15.2, 13.0, 16.5, 10.0]\n# Calculate total and average electricity consumption for 7 days:\n",
        "solution": "daily_units = [12.5, 14.0, 11.8, 15.2, 13.0, 16.5, 10.0]\ntotal = sum(daily_units)\navg = total / len(daily_units)\nprint(f\"7-day total consumption: {total:.2f} units\")\nprint(f\"Daily average: {avg:.2f} units\")",
        "out": "7-day total consumption: 93.00 units\nDaily average: 13.29 units",
        "hint": "Calculate sum and average."
    },
    "Q30": {
        "inp": "student 3",
        "starter": "rates = {'student': 200, 'faculty': 500, 'professional': 1000}\ncategory = 'student'\ncount = 3\n# Calculate registration fee:\n",
        "solution": "rates = {'student': 200, 'faculty': 500, 'professional': 1000}\ncategory = 'student'\ncount = 3\ntotal = rates[category] * count\nprint(f\"Registration category: {category.capitalize()}\")\nprint(f\"Attendees: {count}\")\nprint(f\"Total registration fee: Rs {total}\")",
        "out": "Registration category: Student\nAttendees: 3\nTotal registration fee: Rs 600",
        "hint": "Multiply attendees by category fee."
    },
    "Q31": {
        "inp": "(no input needed)",
        "starter": "def display_welcome():\n    # Display welcome message for Python students\n    pass\n\ndisplay_welcome()\n",
        "solution": "def display_welcome():\n    print(\"Welcome to Python Programming Course!\")\n    print(\"Build real-world coding skills with ElysiaCode.\")\n\ndisplay_welcome()",
        "out": "Welcome to Python Programming Course!\nBuild real-world coding skills with ElysiaCode.",
        "hint": "Define a function with no parameters and call it."
    },
    "Q32": {
        "inp": "5 40",
        "starter": "def calculate_cost(quantity, price):\n    # Display total cost without returning\n    pass\n\ncalculate_cost(5, 40)\n",
        "solution": "def calculate_cost(quantity, price):\n    total = quantity * price\n    print(f\"Total cost for {quantity} notebooks at Rs {price}: Rs {total}\")\n\ncalculate_cost(5, 40)",
        "out": "Total cost for 5 notebooks at Rs 40: Rs 200",
        "hint": "Multiply arguments and print inside the function."
    },
    "Q33": {
        "inp": "9",
        "starter": "def find_square(number):\n    # Return the square of number\n    pass\n\nnum = 9\n",
        "solution": "def find_square(number):\n    return number * number\n\nnum = 9\nprint(f\"Square of {num} is {find_square(num)}\")",
        "out": "Square of 9 is 81",
        "hint": "Return number * number."
    },
    "Q34": {
        "inp": "4 2500 1200",
        "starter": "def trip_cost(days, hotel_per_day, travel_charges):\n    # Calculate total trip cost\n    pass\n\nprint(f\"Total trip cost: Rs {trip_cost(4, 2500, 1200)}\")\n",
        "solution": "def trip_cost(days, hotel_per_day, travel_charges):\n    return days * hotel_per_day + travel_charges\n\nprint(f\"Total trip cost: Rs {trip_cost(4, 2500, 1200)}\")",
        "out": "Total trip cost: Rs 11200",
        "hint": "Formula: days * hotel_per_day + travel_charges."
    },
    "Q35": {
        "inp": "Aarav 101 BCA",
        "starter": "def display_student(name, roll_no, course):\n    # Display student details using keyword arguments\n    pass\n\ndisplay_student(roll_no=101, name='Aarav', course='BCA')\n",
        "solution": "def display_student(name, roll_no, course):\n    print(f\"Roll No: {roll_no} | Name: {name} | Course: {course}\")\n\ndisplay_student(roll_no=101, name='Aarav', course='BCA')",
        "out": "Roll No: 101 | Name: Aarav | Course: BCA",
        "hint": "Pass arguments by name using keyword syntax."
    },
    "Q36": {
        "inp": "5",
        "starter": "def calculate_delivery(weight, rate=50):\n    # Calculate delivery fee with default rate 50\n    pass\n\nprint(f\"Default delivery: Rs {calculate_delivery(5)}\")\nprint(f\"Express delivery: Rs {calculate_delivery(5, rate=80)}\")\n",
        "solution": "def calculate_delivery(weight, rate=50):\n    return weight * rate\n\nprint(f\"Default delivery: Rs {calculate_delivery(5)}\")\nprint(f\"Express delivery: Rs {calculate_delivery(5, rate=80)}\")",
        "out": "Default delivery: Rs 250\nExpress delivery: Rs 400",
        "hint": "Use rate=50 in parameter list."
    },
    "Q37": {
        "inp": "85 92 78",
        "starter": "def analyse_scores(a, b, c):\n    # Return total, average, and highest score\n    pass\n\nt, avg, h = analyse_scores(85, 92, 78)\nprint(f\"Total: {t}, Average: {avg:.2f}, Highest: {h}\")\n",
        "solution": "def analyse_scores(a, b, c):\n    scores = [a, b, c]\n    return sum(scores), sum(scores) / 3, max(scores)\n\nt, avg, h = analyse_scores(85, 92, 78)\nprint(f\"Total: {t}, Average: {avg:.2f}, Highest: {h}\")",
        "out": "Total: 255, Average: 85.00, Highest: 92",
        "hint": "Return tuple of values separated by commas."
    },
    "Q38": {
        "inp": "1500 2500",
        "starter": "total_sales = 0\ndef add_sale(amount):\n    # Modify global total_sales using 'global' keyword\n    pass\n\nadd_sale(1500)\nadd_sale(2500)\nprint(f\"Total sales: Rs {total_sales}\")\n",
        "solution": "total_sales = 0\ndef add_sale(amount):\n    global total_sales\n    total_sales += amount\n\nadd_sale(1500)\nadd_sale(2500)\nprint(f\"Total sales: Rs {total_sales}\")",
        "out": "Total sales: Rs 4000",
        "hint": "Use 'global total_sales' inside the function."
    },
    "Q39": {
        "inp": "80 85 90",
        "starter": "def calculate_total(m1, m2, m3): pass\ndef calculate_percentage(m1, m2, m3): pass\n\nprint(f\"Percentage: {calculate_percentage(80, 85, 90):.2f}%\")\n",
        "solution": "def calculate_total(m1, m2, m3):\n    return m1 + m2 + m3\n\ndef calculate_percentage(m1, m2, m3):\n    total = calculate_total(m1, m2, m3)\n    return (total / 300) * 100\n\nprint(f\"Total Marks: {calculate_total(80, 85, 90)} / 300\")\nprint(f\"Percentage: {calculate_percentage(80, 85, 90):.2f}%\")",
        "out": "Total Marks: 255 / 300\nPercentage: 85.00%",
        "hint": "Call calculate_total inside calculate_percentage."
    },
    "Q40": {
        "inp": "20 5",
        "starter": "def add(a, b): return a + b\ndef subtract(a, b): return a - b\ndef multiply(a, b): return a * b\ndef divide(a, b): return a / b if b != 0 else 'Error'\n",
        "solution": "def add(a, b): return a + b\ndef subtract(a, b): return a - b\ndef multiply(a, b): return a * b\ndef divide(a, b): return a / b if b != 0 else 'Error'\n\na, b = 20, 5\nprint(f\"Add: {add(a, b)}\")\nprint(f\"Subtract: {subtract(a, b)}\")\nprint(f\"Multiply: {multiply(a, b)}\")\nprint(f\"Divide: {divide(a, b)}\")",
        "out": "Add: 25\nSubtract: 15\nMultiply: 100\nDivide: 4.0",
        "hint": "Define separate arithmetic functions."
    },
    "Q41": {
        "inp": "5",
        "starter": "def factorial(n):\n    # Calculate factorial recursively\n    pass\n\nprint(f\"5! = {factorial(5)}\")\n",
        "solution": "def factorial(n):\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)\n\nprint(f\"5! = {factorial(5)}\")",
        "out": "5! = 120",
        "hint": "Base case: n <= 1 return 1, recursive step n * factorial(n - 1)."
    },
    "Q42": {
        "inp": "10",
        "starter": "def sum_n(n):\n    # Calculate sum from 1 to n recursively\n    pass\n\nprint(f\"Sum 1 to 10 = {sum_n(10)}\")\n",
        "solution": "def sum_n(n):\n    if n <= 1:\n        return n\n    return n + sum_n(n - 1)\n\nprint(f\"Sum 1 to 10 = {sum_n(10)}\")",
        "out": "Sum 1 to 10 = 55",
        "hint": "Base case: n <= 1 return n, recursive step n + sum_n(n - 1)."
    },
    "Q43": {
        "inp": "27",
        "starter": "def check_even_odd(number):\n    # Return 'Even' if divisible by 2, else 'Odd'\n    pass\n\nprint(check_even_odd(27))\n",
        "solution": "def check_even_odd(number):\n    return 'Even' if number % 2 == 0 else 'Odd'\n\nprint(f\"27 is {check_even_odd(27)}\")",
        "out": "27 is Odd",
        "hint": "Check number % 2 == 0."
    },
    "Q44": {
        "inp": "45 89 23",
        "starter": "def largest(a, b, c):\n    # Return largest without using max()\n    pass\n\nprint(f\"Largest: {largest(45, 89, 23)}\")\n",
        "solution": "def largest(a, b, c):\n    if a >= b and a >= c:\n        return a\n    elif b >= a and b >= c:\n        return b\n    return c\n\nprint(f\"Largest: {largest(45, 89, 23)}\")",
        "out": "Largest: 89",
        "hint": "Use if-elif comparisons without using max()."
    },
    "Q45": {
        "inp": "80 65",
        "starter": "def attendance_status(classes_held, classes_attended):\n    # Return attendance percentage and eligibility (>= 75%)\n    pass\n\nattendance_status(80, 65)\n",
        "solution": "def attendance_status(classes_held, classes_attended):\n    pct = (classes_attended / classes_held) * 100\n    status = \"Eligible\" if pct >= 75 else \"Not Eligible\"\n    print(f\"Classes: {classes_attended}/{classes_held}\")\n    print(f\"Attendance: {pct:.2f}%\")\n    print(f\"Exam Status: {status}\")\n\nattendance_status(80, 65)",
        "out": "Classes: 65/80\nAttendance: 81.25%\nExam Status: Eligible",
        "hint": "Percentage = (classes_attended / classes_held) * 100; check >= 75%."
    }
}
print("DOCX 45 definitions loaded cleanly.")
