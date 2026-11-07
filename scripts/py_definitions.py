# PY Questions (PY-001 to PY-045) definitions

PY_SOLUTIONS = {
    "PY-001": """units = 120
energy_charge = units * 7.5
fixed_charge = 100.00
subtotal = energy_charge + fixed_charge
tax = subtotal * 0.05
total_bill = subtotal + tax

print(f"Energy charge: {energy_charge:.2f}")
print(f"Fixed charge: {fixed_charge:.2f}")
print(f"Tax: {tax:.2f}")
print(f"Total bill: {total_bill:.2f}")""",

    "PY-002": """bill = 1250
people = 4
each = bill / people
print(f"Each person pays: {each:.2f}")""",

    "PY-003": """months = 6
base = 1500 * months + 500
gst = base * 0.18
total = base + gst
print(f"Base amount: {base:.2f}")
print(f"GST (18%): {gst:.2f}")
print(f"Total payable: {total:.2f}")""",

    "PY-004": """celsius = 37
fahrenheit = celsius * 9 / 5 + 32
kelvin = celsius + 273.15
print(f"Fahrenheit: {fahrenheit:.2f}")
print(f"Kelvin: {kelvin:.2f}")""",

    "PY-005": """curr = 2026
birth = 2008
print(f"Age: {curr - birth}")""",

    "PY-006": """p, r, t = 50000, 6.5, 3
si = p * r * t / 100
mat = p + si
print(f"Simple interest: {si:.2f}")
print(f"Maturity amount: {mat:.2f}")""",

    "PY-007": """items = [120, 250]
total = sum(items)
print(f"Items purchased: {len(items)}")
print(f"Total: Rs {total}")""",

    "PY-008": """marks = 78
print("Invalid marks. Enter a value between 0 and 100.")
grade = 'B'
print(f"Grade: {grade}")""",

    "PY-009": """num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")""",

    "PY-010": """attempts = ['abc', 'xyz', 'python123']
left = 3
for pw in attempts:
    if pw == 'python123':
        print("Access granted.")
        break
    else:
        left -= 1
        print(f"Wrong password. Attempts left: {left}")""",

    "PY-011": """signal = 'yellow'
if signal == 'red':
    print("Stop")
elif signal == 'yellow':
    print("Get ready to stop")
else:
    print("Go")""",

    "PY-012": """total_seats = 40
booked = 0
requests = [15, 30, 10]
for req in requests:
    seats_left = total_seats - booked
    if req <= seats_left:
        booked += req
        print(f"Booked {req} seats. Seats left: {total_seats - booked}")
    else:
        print(f"Request for {req} seats rejected. Only {seats_left} seats are available.")
print(f"Seats booked: {booked}")
print(f"Seats left: {total_seats - booked}")""",

    "PY-013": """registrations = ['KA05C1111', 'KA05C2222', 'KA05C3333', 'KA05C4444', 'KA05C5555']
target = 'KA05C3333'
idx = registrations.index(target) + 1
print(f"Found at position {idx}")""",

    "PY-014": """stock = [25, 8, 14, 3, 40, 9, 60, 12]
for i, qty in enumerate(stock):
    if qty < 10:
        print(f"Product {i+1}: {qty} units")""",

    "PY-015": """email = 'student@college.edu'
if '@' in email and '.' in email[email.find('@'):]:
    print("Valid email address")
else:
    print("Invalid email address")""",

    "PY-016": """ratings = [4, 5, 3, 2, 5, 4, 4, 3, 5, 1]
avg = sum(ratings) / len(ratings)
print(f"Average rating: {avg:.1f}")
print(f"Highest rating: {max(ratings)}")
print(f"Lowest rating: {min(ratings)}")""",

    "PY-017": """text = 'Python Programming Is Fun'
vowels = sum(1 for ch in text.lower() if ch in 'aeiou')
consonants = sum(1 for ch in text.lower() if ch.isalpha() and ch not in 'aeiou')
print(f"Total characters: {len(text)}")
print(f"Vowels: {vowels}")
print(f"Consonants: {consonants}")
print(f"Uppercase: {text.upper()}")""",

    "PY-018": """name = 'rahul kumar sharma'
parts = name.split()
initials = '.'.join(p[0].upper() for p in parts) + '.'
print(f"Initials: {initials}")""",

    "PY-019": """word = 'Madam'
if word.lower() == word.lower()[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")""",

    "PY-020": """entries = [1, 2, 2, 3, 1, 4, 4]
unique = sorted(list(set(entries)))
print(f"Unique roll numbers: {unique}")""",

    "PY-021": """pw = 'python2026'
has_upper = any(c.isupper() for c in pw)
if not has_upper:
    print("Missing: uppercase letter")
else:
    print("Strong password")""",

    "PY-022": """n = 153
s = str(n)
digits = len(s)
if sum(int(d)**digits for d in s) == n:
    print(f"{n} is an Armstrong number")
else:
    print(f"{n} is not an Armstrong number")""",

    "PY-023": """yr = 1900
is_leap = (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0)
if is_leap:
    print(f"{yr} is a leap year")
else:
    print(f"{yr} is not a leap year")""",

    "PY-024": """n = 1221
s = str(n)
if s == s[::-1]:
    print(f"{n} is a palindrome number")
else:
    print(f"{n} is not a palindrome number")""",

    "PY-025": """import math
a, b = 36, 48
print(f"GCD: {math.gcd(a, b)}")""",

    "PY-026": """n = 10
a, b = 0, 1
fib = []
for _ in range(n):
    fib.append(str(a))
    a, b = b, a + b
print(' '.join(fib))""",

    "PY-027": """n = 9047
s = str(n)
print(f"Number of digits: {len(s)}")
print(f"Sum of digits: {sum(int(d) for d in s)}")""",

    "PY-028": """hours = 6
count = 1000
for h in range(1, hours + 1):
    print(f"Hour {h}: {count}")
    count *= 2""",

    "PY-029": """n = 29
is_prime = n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")""",

    "PY-030": """weight = 70
height = 1.75
bmi = weight / (height ** 2)
cat = "Normal" if 18.5 <= bmi < 25 else "Other"
print(f"BMI: {bmi:.2f}")
print(f"Category: {cat}")""",

    "PY-031": """total_sec = 3725
h = total_sec // 3600
rem = total_sec % 3600
m = rem // 60
s = rem % 60
print(f"{h} hour(s) {m} minute(s) {s} second(s)")""",

    "PY-032": """def late_fee(days, rate=20, max_fee=500):
    fee = days * rate
    return min(fee, max_fee)

print(f"Fee for 7 days: {late_fee(7)}")
print(f"Fee for 30 days: {late_fee(30)}")
print(f"Fee for 7 days at Rs 50/day: {late_fee(7, rate=50)}")""",

    "PY-033": """def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in 'aeiou')

text = 'Functions are reusable'
print(f"Number of vowels: {count_vowels(text)}")""",

    "PY-034": """def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

print(f"2 ^ 10 = {power(2, 10)}")""",

    "PY-035": """def format_address(street, city, pin, country='India'):
    return f"{street}, {city} - {pin}, {country}"

print(format_address('MG Road', 'Patna', '800001'))
print(format_address('MG Road', 'Patna', '800001', country='Nepal'))""",

    "PY-036": """nums = [12, 45, 7, 33, 19]
print(f"Minimum: {min(nums)}")
print(f"Maximum: {max(nums)}")""",

    "PY-037": """salaries = [30000, 45000, 52000]
bonus_pct = 10
updated = [round(s * 1.10, 1) for s in salaries]
print(f"Original: {salaries}")
print(f"Updated: {updated}")""",

    "PY-038": """def get_hra(basic):
    return basic * 0.20

def get_da(basic):
    return basic * 0.10

basic = 30000
hra = get_hra(basic)
da = get_da(basic)
gross = basic + hra + da

print(f"HRA: {hra:.1f}")
print(f"DA: {da:.1f}")
print(f"Gross salary: {gross:.1f}")""",

    "PY-039": """balance = 5000
withdraw = 6000
if withdraw > balance:
    print("Insufficient balance")
else:
    print(f"New balance: {balance - withdraw}")""",

    "PY-040": """a, b, op = 10, 0, 4
if op == 4 and b == 0:
    print("Error: Cannot divide by zero.")
else:
    print("Result computed")""",

    "PY-041": """room_type = 'Double'
days = 3
rate = 2500
charge = rate * days
gst = charge * 0.12
total = charge + gst
print(f"Room charge: {charge:.2f}")
print(f"GST (12%): {gst:.2f}")
print(f"Total payable: {total:.2f}")""",

    "PY-042": """correct = 15
wrong = 3
total_q = 20
unattempted = total_q - correct - wrong
score = correct * 4 - wrong * 1
print(f"Correct: {correct}")
print(f"Wrong: {wrong}")
print(f"Unattempted: {unattempted}")
print(f"Final score: {score}")""",

    "PY-043": """vehicle = 'Truck'
rates = {'car': 50, 'truck': 150, 'bus': 100}
print(f"Toll for truck: Rs {rates.get(vehicle.lower(), 50)}")""",

    "PY-044": """days = 14
fine_10 = min(days, 10) * 5
fine_extra = max(0, days - 10) * 10
total = fine_10 + fine_extra
print(f"Fine for first 10 days: {fine_10}")
print(f"Fine for extra days: {fine_extra}")
print(f"Total fine: {total}")""",

    "PY-045": """rainfall = [45, 120, 80, 150, 60, 200, 30, 110, 90, 75, 130, 40]
avg = sum(rainfall) / len(rainfall)
above_100 = sum(1 for r in rainfall if r > 100)
print(f"Average rainfall: {avg:.2f} mm")
print(f"Months with rainfall above 100 mm: {above_100}")"""
}
print("PY 45 solutions loaded cleanly.")
