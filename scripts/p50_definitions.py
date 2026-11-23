# scripts/p50_definitions.py
# Complete definitions for all 50 Practice Questions (Part A to Part F)

P50_QUESTIONS_RAW = [
    # =========================================================================
    # Part A: Operators, Expressions and Formatted Output (Q1 to Q5)
    # =========================================================================
    {
        "q_num": 1,
        "title": "Oxygen Reserve at Aryabhata-7",
        "part": "Part A: Operators, Expressions and Formatted Output",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "In a hypothetical space mission, the Aryabhata-7 station has C crew members. Each crew member consumes R litres of oxygen per day. The storage tank holds T litres of oxygen, and the next supply ship will arrive after D days. Mission control wants to know how many complete days the oxygen will last and whether the crew is safe until the supply ship arrives.",
        "task": "Find how many complete days the oxygen will last and the leftover litres. Then determine if the supply is enough for D days.",
        "constraints": "1 <= C, R <= 100; 1 <= T <= 100000; 1 <= D <= 365",
        "sample_input": "6\n4\n500\n20",
        "expected_output": "Oxygen lasts for 20 full days with 20 litres left over.\nStatus: Safe",
        "hint": "Daily consumption = C * R. Full days = T // daily_consumption. Leftover = T % daily_consumption. If T >= daily_consumption * D, Status is Safe; else shortage = daily_consumption * D - T.",
        "starter_code": """# [P50-001] Oxygen Reserve at Aryabhata-7
# C: Crew members, R: Litres/day/member, T: Total litres in tank, D: Days until supply ship
C = 6
R = 4
T = 500
D = 20

# Calculate full days, leftover litres, and safety status:
""",
        "solution_code": """C = 6
R = 4
T = 500
D = 20

daily = C * R
full_days = T // daily
leftover = T % daily
print(f"Oxygen lasts for {full_days} full days with {leftover} litres left over.")

needed = daily * D
if T >= needed:
    print("Status: Safe")
else:
    print(f"Status: Shortage of {needed - T} litres")"""
    },
    {
        "q_num": 2,
        "title": "Cross-Time-Zone Flight Arrival",
        "part": "Part A: Operators, Expressions and Formatted Output",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A fictional airline, SkyBharat, wants its app to display the local arrival time of a flight. The flight departs at a given local time (24-hour clock), flies for a given number of minutes, and lands in a city whose local time differs from the departure city by a given number of minutes (positive if ahead, negative if behind).",
        "task": "Display the local arrival time (HH:MM) and how many days the date has shifted using only // and %.",
        "constraints": "0 <= hour <= 23; 0 <= minute <= 59; 1 <= duration <= 1500; -720 <= difference <= 840. Use only // and % (no time module).",
        "sample_input": "22 45\n540\n330",
        "expected_output": "Arrival Time: 13:15\nDay Shift: +1 day(s)",
        "hint": "Convert departure to total minutes (hour*60 + min). Add duration and time difference. Shift = total // 1440. Remainder = total % 1440. Arrival hour = remainder // 60, min = remainder % 60.",
        "starter_code": """# [P50-002] Cross-Time-Zone Flight Arrival
# Departure time: 22 45, Duration: 540 minutes, Time difference: 330 minutes
dep_hour, dep_min = 22, 45
duration = 540
diff = 330

# Calculate arrival time and day shift using // and %:
""",
        "solution_code": """dep_hour, dep_min = 22, 45
duration = 540
diff = 330

total_mins = dep_hour * 60 + dep_min + duration + diff
day_shift = total_mins // 1440
rem_mins = total_mins % 1440
arr_hour = rem_mins // 60
arr_min = rem_mins % 60

print(f"Arrival Time: {arr_hour:02d}:{arr_min:02d}")
if day_shift == 0:
    print("Day Shift: Same Day")
elif day_shift > 0:
    print(f"Day Shift: +{day_shift} day(s)")
else:
    print(f"Day Shift: {day_shift} day(s)")"""
    },
    {
        "q_num": 3,
        "title": "Smart Farm Fertiliser Planner",
        "part": "Part A: Operators, Expressions and Formatted Output",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "On a hypothetical smart farm, a rectangular field must be treated with fertiliser. The recommended dose is a fixed number of grams per square metre. Fertiliser is sold only in full bags of a fixed weight, so the farmer must buy a whole number of bags.",
        "task": "Find the area, fertiliser needed (kg), number of bags to buy, total cost, and leftover fertiliser. Use arithmetic operators only (no math module, no if statement).",
        "constraints": "Area in sq m, doses in grams/sq m, bag weight in kg. Round all decimal values to 2 decimal places.",
        "sample_input": "40\n25\n120\n50\n800",
        "expected_output": "Area: 1000.00 sq m\nFertilizer Required: 120.00 kg\nBags Needed: 3\nTotal Cost: Rs. 2400.00\nLeftover Fertilizer: 30.00 kg",
        "hint": "Area = length * width. Required kg = (Area * grams_per_sq_m) / 1000. Bags = int(-(-required // bag_weight)). Total cost = bags * cost_per_bag. Leftover = (bags * bag_weight) - required.",
        "starter_code": """# [P50-003] Smart Farm Fertiliser Planner
length = 40
width = 25
grams_per_sq_m = 120
bag_weight = 50
cost_per_bag = 800

# Compute area, required kg, whole bags needed, total cost, leftover kg:
""",
        "solution_code": """length = 40
width = 25
grams_per_sq_m = 120
bag_weight = 50
cost_per_bag = 800

area = float(length * width)
req_kg = float(area * grams_per_sq_m / 1000)
# Ceiling division without math or if
bags = int(-(-req_kg // bag_weight))
total_cost = bags * cost_per_bag
leftover = (bags * bag_weight) - req_kg

print(f"Area: {area:.2f} sq m")
print(f"Fertilizer Required: {req_kg:.2f} kg")
print(f"Bags Needed: {bags}")
print(f"Total Cost: Rs. {total_cost:.2f}")
print(f"Leftover Fertilizer: {leftover:.2f} kg")"""
    },
    {
        "q_num": 4,
        "title": "Friends' Dinner Bill Splitter",
        "part": "Part A: Operators, Expressions and Formatted Output",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A group of friends at a restaurant receives a bill. A 5% service charge is added to the base amount, and then 18% GST is applied on (base amount + service charge). Each of the first (n-1) friends pays the largest whole-rupee amount not exceeding total / n, and the last friend pays whatever remains.",
        "task": "Calculate the service charge, GST, total bill, amount paid by each of the first (n-1) friends, and the last friend's share.",
        "constraints": "2 <= n <= 20; 1 <= base amount <= 100000. All values with two decimal places.",
        "sample_input": "2450\n5",
        "expected_output": "Service Charge: 122.50\nGST: 463.05\nTotal Bill: 3035.55\nEach of the first 4 friends pays: 607.00\nLast friend pays: 607.55",
        "hint": "service_charge = round(base * 0.05, 2). gst = round((base + service_charge) * 0.18, 2). total = base + service_charge + gst. first_share = float(int(total // n)). last_share = total - (first_share * (n - 1)).",
        "starter_code": """# [P50-004] Friends' Dinner Bill Splitter
base_amount = 2450.0
n = 5

# Calculate service charge, GST, total, and split amounts:
""",
        "solution_code": """base_amount = 2450.0
n = 5

sc = round(base_amount * 0.05, 2)
gst = round((base_amount + sc) * 0.18, 2)
total = round(base_amount + sc + gst, 2)
first_share = float(int(total // n))
last_share = round(total - (first_share * (n - 1)), 2)

print(f"Service Charge: {sc:.2f}")
print(f"GST: {gst:.2f}")
print(f"Total Bill: {total:.2f}")
print(f"Each of the first {n-1} friends pays: {first_share:.2f}")
print(f"Last friend pays: {last_share:.2f}")"""
    },
    {
        "q_num": 5,
        "title": "E-Wallet Cashback Engine",
        "part": "Part A: Operators, Expressions and Formatted Output",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A hypothetical e-wallet, PayNova, rewards every full block of Rs. 100 spent with Rs. 7 cashback, but the cashback per transaction is capped at Rs. 150. The leftover amount (less than Rs. 100) earns one bonus coin for every full Rs. 10.",
        "task": "Display the number of full blocks of 100, the cashback amount, and the bonus coins.",
        "constraints": "1 <= amount <= 1000000",
        "sample_input": "2350",
        "expected_output": "Full Blocks of Rs. 100: 23\nCashback: Rs. 150\nBonus Coins: 5",
        "hint": "blocks = amount // 100. cashback = min(blocks * 7, 150). leftover = amount % 100. coins = leftover // 10.",
        "starter_code": """# [P50-005] E-Wallet Cashback Engine
amount = 2350

# Calculate blocks, capped cashback, and bonus coins:
""",
        "solution_code": """amount = 2350

blocks = amount // 100
cashback = min(blocks * 7, 150)
leftover = amount % 100
coins = leftover // 10

print(f"Full Blocks of Rs. 100: {blocks}")
print(f"Cashback: Rs. {cashback}")
print(f"Bonus Coins: {coins}")"""
    },

    # =========================================================================
    # Part B: Decision Making and Nested Conditions (Q6 to Q12)
    # =========================================================================
    {
        "q_num": 6,
        "title": "Hospital Triage Desk",
        "part": "Part B: Decision Making and Nested Conditions",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "At a hypothetical hospital, a triage nurse decides where to send a patient using age, blood oxygen saturation (SpO2 %) and body temperature (°F). The rules are applied in this order: (1) Invalid Input if age < 0, SpO2 outside 0-100, or temp outside 90-110. (2) SpO2 below 90: ICU Admission. (3) SpO2 below 94 and (age >= 60 or temp >= 101): HDU Admission. (4) Temperature >= 100.4 or SpO2 < 94: General Ward. (5) Otherwise: Home Isolation.",
        "task": "Classify patient admission strictly following the triage order.",
        "constraints": "Apply the rules strictly in the order given.",
        "sample_input": "67\n92\n99.1",
        "expected_output": "HDU Admission",
        "hint": "Use an if-elif-else ladder in the exact precedence order given.",
        "starter_code": """# [P50-006] Hospital Triage Desk
age = 67
spo2 = 92
temp = 99.1

# Evaluate triage criteria in strict order:
""",
        "solution_code": """age = 67
spo2 = 92
temp = 99.1

if age < 0 or spo2 < 0 or spo2 > 100 or temp < 90 or temp > 110:
    print("Invalid Input")
elif spo2 < 90:
    print("ICU Admission")
elif spo2 < 94 and (age >= 60 or temp >= 101):
    print("HDU Admission")
elif temp >= 100.4 or spo2 < 94:
    print("General Ward")
else:
    print("Home Isolation")"""
    },
    {
        "q_num": 7,
        "title": "Smart Highway Challan System",
        "part": "Part B: Decision Making and Nested Conditions",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A smart-traffic system fines vehicles for overspeeding. Base speed limit: City 50 km/h, Highway 100 km/h, School 25 km/h. Trucks must travel 10 km/h below the zone limit. Base fine: excess <= 10 km/h is Rs. 500, excess 11-20 km/h is Rs. 1000, and excess > 20 km/h is Rs. 2000. Multipliers: 1.5 for Truck, 2 for School zone (both apply if both hold).",
        "task": "Display the speed limit, excess speed (0 if within limit), and the calculated fine (0 if no fine).",
        "constraints": "1 <= speed <= 250",
        "sample_input": "Truck\nHighway\n112",
        "expected_output": "Speed Limit: 90 km/h\nExcess Speed: 22 km/h\nFine: Rs. 3000",
        "hint": "Calculate effective limit. Excess = max(0, speed - limit). If excess > 0, find base fine and multiply by 1.5 for Truck and 2 for School.",
        "starter_code": """# [P50-007] Smart Highway Challan System
vehicle = 'Truck'
zone = 'Highway'
speed = 112

# Calculate speed limit, excess speed, and final fine:
""",
        "solution_code": """vehicle = 'Truck'
zone = 'Highway'
speed = 112

zone_limits = {'City': 50, 'Highway': 100, 'School': 25}
limit = zone_limits.get(zone, 50)
if vehicle == 'Truck':
    limit -= 10

excess = max(0, speed - limit)
fine = 0
if excess > 0:
    if excess <= 10:
        base_fine = 500
    elif excess <= 20:
        base_fine = 1000
    else:
        base_fine = 2000
    
    mult = 1.0
    if vehicle == 'Truck':
        mult *= 1.5
    if zone == 'School':
        mult *= 2.0
    fine = int(base_fine * mult)

print(f"Speed Limit: {limit} km/h")
print(f"Excess Speed: {excess} km/h")
print(f"Fine: Rs. {fine}")"""
    },
    {
        "q_num": 8,
        "title": "Airline Excess-Baggage Counter",
        "part": "Part B: Decision Making and Nested Conditions",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "AeroLink allows free baggage of 20 kg in Economy and 35 kg in Business class. Maximum accepted weight is 40 kg (Economy) and 60 kg (Business); heavier baggage is rejected. Excess weight is charged at Rs. 450/kg (Economy) or Rs. 300/kg (Business). If excess > 10 kg, a 20% surcharge is added. Finally, 5% GST is applied on (excess charge + surcharge).",
        "task": "Determine if baggage is rejected, has no excess, or calculate the full payable amount breakdown.",
        "constraints": "0 <= weight <= 100",
        "sample_input": "Economy\n34.5",
        "expected_output": "Excess Weight: 14.50 kg\nExcess Charge: Rs. 6525.00\nSurcharge: Rs. 1305.00\nGST: Rs. 391.50\nTotal Payable: Rs. 8221.50",
        "hint": "Check weight > max first. If weight <= free, print 'No excess baggage charges'. Otherwise compute excess, surcharge, GST, and total.",
        "starter_code": """# [P50-008] Airline Excess-Baggage Counter
travel_class = 'Economy'
weight = 34.5

# Calculate baggage charges according to airline rules:
""",
        "solution_code": """travel_class = 'Economy'
weight = 34.5

free_limit = 20 if travel_class == 'Economy' else 35
max_limit = 40 if travel_class == 'Economy' else 60
rate = 450 if travel_class == 'Economy' else 300

if weight > max_limit:
    print("Baggage Rejected: Weight limit exceeded")
elif weight <= free_limit:
    print("No excess baggage charges")
else:
    excess_wt = weight - free_limit
    excess_chg = excess_wt * rate
    surcharge = excess_chg * 0.20 if excess_wt > 10 else 0.0
    gst = (excess_chg + surcharge) * 0.05
    total = excess_chg + surcharge + gst
    print(f"Excess Weight: {excess_wt:.2f} kg")
    print(f"Excess Charge: Rs. {excess_chg:.2f}")
    print(f"Surcharge: Rs. {surcharge:.2f}")
    print(f"GST: Rs. {gst:.2f}")
    print(f"Total Payable: Rs. {total:.2f}")"""
    },
    {
        "q_num": 9,
        "title": "Himalayan Resort Billing",
        "part": "Part B: Decision Making and Nested Conditions",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A hill resort charges per night: Standard Rs. 2500, Deluxe Rs. 4000, Luxury Rs. 7000. Peak season adds 25% to room rate. Every guest beyond two adds Rs. 500 per night. Stays of 5-9 nights get 10% discount on room charges; 10+ nights get 20%. GST is 12% if tariff per night <= 7500, else 18%, applied on discounted amount.",
        "task": "Compute tariff per night, room charges, discount, GST, and net total payable.",
        "constraints": "1 <= nights <= 60; 1 <= guests <= 6",
        "sample_input": "Deluxe\n6\nPeak\n3",
        "expected_output": "Tariff per Night: Rs. 5500.00\nRoom Charges: Rs. 33000.00\nDiscount (10%): Rs. 3300.00\nGST (12%): Rs. 3564.00\nTotal Payable: Rs. 33264.00",
        "hint": "rate = base * 1.25 if Peak else base. tariff_per_night = rate + max(0, guests - 2) * 500. room_charges = tariff * nights. Apply length discount and then GST rate.",
        "starter_code": """# [P50-009] Himalayan Resort Billing
room_type = 'Deluxe'
nights = 6
season = 'Peak'
guests = 3

# Compute tariff, room charges, discount, GST, and total:
""",
        "solution_code": """room_type = 'Deluxe'
nights = 6
season = 'Peak'
guests = 3

base_rates = {'Standard': 2500, 'Deluxe': 4000, 'Luxury': 7000}
rate = base_rates[room_type]
if season == 'Peak':
    rate = rate * 1.25

tariff = rate + max(0, guests - 2) * 500
room_charges = tariff * nights

if nights >= 10:
    disc_pct = 20
elif nights >= 5:
    disc_pct = 10
else:
    disc_pct = 0

discount = room_charges * (disc_pct / 100)
after_disc = room_charges - discount

gst_pct = 12 if tariff <= 7500 else 18
gst = after_disc * (gst_pct / 100)
total = after_disc + gst

print(f"Tariff per Night: Rs. {tariff:.2f}")
print(f"Room Charges: Rs. {room_charges:.2f}")
print(f"Discount ({disc_pct}%): Rs. {discount:.2f}")
print(f"GST ({gst_pct}%): Rs. {gst:.2f}")
print(f"Total Payable: Rs. {total:.2f}")"""
    },
    {
        "q_num": 10,
        "title": "Tomorrow's Date Generator",
        "part": "Part B: Decision Making and Nested Conditions",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A calendar app must show tomorrow's date for any date entered by the user. Write a program that validates the date (including leap year rules) and prints the next date in DD-MM-YYYY format.",
        "task": "Validate day, month, and year. Print 'Invalid Date' if invalid, otherwise the next date as DD-MM-YYYY.",
        "constraints": "1 <= year <= 9999. Check leap year: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0).",
        "sample_input": "28 2 2024",
        "expected_output": "29-02-2024",
        "hint": "Check month 1-12 and day within days_in_month. Increment day; if day > days_in_month, set day=1 and increment month. If month > 12, set month=1 and increment year.",
        "starter_code": """# [P50-010] Tomorrow's Date Generator
day, month, year = 28, 2, 2024

# Validate date and print next date or 'Invalid Date':
""",
        "solution_code": """day, month, year = 28, 2, 2024

def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

days_in_months = [0, 31, 29 if is_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if month < 1 or month > 12 or day < 1 or day > days_in_months[month]:
    print("Invalid Date")
else:
    day += 1
    if day > days_in_months[month]:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    print(f"{day:02d}-{month:02d}-{year:04d}")"""
    },
    {
        "q_num": 11,
        "title": "Drone Delivery Clearance",
        "part": "Part B: Decision Making and Nested Conditions",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A drone delivery company calculates battery use % as 4 * distance(km) + 3 * payload(kg), multiplied by 1.3 if wind speed > 25 km/h. Checks in order: wind > 40 km/h -> Flight Cancelled: Unsafe wind; payload > 5 kg -> Flight Cancelled: Overweight payload; battery >= use + 10 -> Delivery Approved; battery >= use -> Delivery Risky: Battery reserve below 10%; else Flight Cancelled: Insufficient battery.",
        "task": "Print the flight decision in order, and for Approved/Risky also print Estimated Battery Use: <value>%.",
        "constraints": "Apply checks strictly in order. Round battery % to two decimal places.",
        "sample_input": "8\n2.5\n70\n30",
        "expected_output": "Delivery Approved\nEstimated Battery Use: 51.35%",
        "hint": "Check wind > 40 first, then payload > 5, then calculate estimated use and evaluate battery levels.",
        "starter_code": """# [P50-011] Drone Delivery Clearance
distance = 8.0
payload = 2.5
battery = 70.0
wind = 30.0

# Evaluate drone flight safety and clearance:
""",
        "solution_code": """distance = 8.0
payload = 2.5
battery = 70.0
wind = 30.0

if wind > 40:
    print("Flight Cancelled: Unsafe wind")
elif payload > 5:
    print("Flight Cancelled: Overweight payload")
else:
    use = 4 * distance + 3 * payload
    if wind > 25:
        use *= 1.3
    
    if battery >= use + 10:
        print("Delivery Approved")
        print(f"Estimated Battery Use: {use:.2f}%")
    elif battery >= use:
        print("Delivery Risky: Battery reserve below 10%")
        print(f"Estimated Battery Use: {use:.2f}%")
    else:
        print("Flight Cancelled: Insufficient battery")"""
    },
    {
        "q_num": 12,
        "title": "Merit-cum-Means Scholarship Committee",
        "part": "Part B: Decision Making and Nested Conditions",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A university awards scholarships: attendance < 75% -> Not Eligible: Low attendance. Else base scholarship: marks >= 90 -> 100%, 80 to <90 -> 60%, 70 to <80 -> 30%, <70% -> Not Eligible: Marks below 70%. If annual family income <= 3,00,000: add 10%. Sports: State adds 10%, National adds 20%. Final scholarship capped at 100%.",
        "task": "Determine scholarship percentage or print non-eligibility reason.",
        "constraints": "0 <= percentage <= 100; 0 <= attendance <= 100",
        "sample_input": "86.5\n82\n250000\nState",
        "expected_output": "Scholarship: 80%",
        "hint": "Check attendance < 75 first. Next check marks < 70. Otherwise add family income bonus and sports bonus, capped at 100%.",
        "starter_code": """# [P50-012] Merit-cum-Means Scholarship Committee
marks = 86.5
attendance = 82
income = 250000
sports = 'State'

# Determine scholarship percentage:
""",
        "solution_code": """marks = 86.5
attendance = 82
income = 250000
sports = 'State'

if attendance < 75:
    print("Not Eligible: Low attendance")
elif marks < 70:
    print("Not Eligible: Marks below 70%")
else:
    if marks >= 90:
        base = 100
    elif marks >= 80:
        base = 60
    else:
        base = 30
    
    if income <= 300000:
        base += 10
    
    if sports == 'State':
        base += 10
    elif sports == 'National':
        base += 20
        
    final = min(100, base)
    print(f"Scholarship: {final}%")"""
    },

    # =========================================================================
    # Part C: Loops, Patterns and Number Logic (Q13 to Q22)
    # =========================================================================
    {
        "q_num": 13,
        "title": "Piggy Bank Target Tracker",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A savings app lets a child set a target and records daily deposits until -1 is entered. The app reports total deposits count, total saved amount, largest deposit, and the deposit number on which the target was first reached/crossed.",
        "task": "Process deposits ending in -1 and report savings summary.",
        "constraints": "At least one deposit is entered before -1. 1 <= target <= 1000000.",
        "sample_input": "1000\n200\n150\n400\n50\n300\n-1",
        "expected_output": "Total Deposits: 5\nTotal Saved: Rs. 1100\nLargest Deposit: Rs. 400\nTarget reached on deposit number 5",
        "hint": "Maintain running sum, max deposit, and record the index when running sum >= target for the first time.",
        "starter_code": """# [P50-013] Piggy Bank Target Tracker
target = 1000
deposits = [200, 150, 400, 50, 300]

# Track total deposits, largest deposit, and target reached event:
""",
        "solution_code": """target = 1000
deposits = [200, 150, 400, 50, 300]

total_saved = 0
largest = 0
reached_idx = None

for i, d in enumerate(deposits, 1):
    total_saved += d
    if d > largest:
        largest = d
    if total_saved >= target and reached_idx is None:
        reached_idx = i

print(f"Total Deposits: {len(deposits)}")
print(f"Total Saved: Rs. {total_saved}")
print(f"Largest Deposit: Rs. {largest}")
if reached_idx is not None:
    print(f"Target reached on deposit number {reached_idx}")
else:
    print(f"Target not reached. Remaining: Rs. {target - total_saved}")"""
    },
    {
        "q_num": 14,
        "title": "Concert Stage Light Diamond",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A concert designer wants a numeric light-pattern diamond. For a given n, row i (1 <= i <= n) of the upper half has (n - i) leading spaces followed by digits 1 to i and then i-1 down to 1. The lower half repeats the rows in reverse order (without repeating the middle row).",
        "task": "Generate the 2n-1 rows diamond pattern with no trailing spaces.",
        "constraints": "1 <= n <= 9",
        "sample_input": "3",
        "expected_output": "  1\n 121\n12321\n 121\n  1",
        "hint": "For row i: spaces = ' ' * (n - i). numbers = ''.join(str(x) for x in range(1, i+1)) + ''.join(str(x) for x in range(i-1, 0, -1)).",
        "starter_code": """# [P50-014] Concert Stage Light Diamond
n = 3

# Generate the numeric diamond pattern:
""",
        "solution_code": """n = 3

rows = []
for i in range(1, n + 1):
    spaces = ' ' * (n - i)
    asc = ''.join(str(x) for x in range(1, i + 1))
    desc = ''.join(str(x) for x in range(i - 1, 0, -1))
    rows.append(spaces + asc + desc)

for i in range(n - 1, 0, -1):
    spaces = ' ' * (n - i)
    asc = ''.join(str(x) for x in range(1, i + 1))
    desc = ''.join(str(x) for x in range(i - 1, 0, -1))
    rows.append(spaces + asc + desc)

print('\\n'.join(rows))"""
    },
    {
        "q_num": 15,
        "title": "Treasure Vault of Perfect Keys",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "In a treasure-hunt game, a vault opens only with 'perfect' keys. A number is perfect if it equals the sum of its proper positive divisors (excluding the number itself). For example, 28 = 1 + 2 + 4 + 7 + 14.",
        "task": "Find all perfect numbers in the inclusive range [a, b].",
        "constraints": "1 <= a <= b <= 1000",
        "sample_input": "1 500",
        "expected_output": "Keys found: 6 28 496\nTotal keys: 3",
        "hint": "For each number x in range [a, b], find divisors up to x//2, sum them, and check if sum == x and x > 1.",
        "starter_code": """# [P50-015] Treasure Vault of Perfect Keys
a, b = 1, 500

# Find all perfect numbers in range [a, b]:
""",
        "solution_code": """a, b = 1, 500

perfect_keys = []
for num in range(max(2, a), b + 1):
    div_sum = sum(d for d in range(1, num // 2 + 1) if num % d == 0)
    if div_sum == num:
        perfect_keys.append(num)

if perfect_keys:
    print(f"Keys found: {' '.join(map(str, perfect_keys))}")
    print(f"Total keys: {len(perfect_keys)}")
else:
    print("No keys found")"""
    },
    {
        "q_num": 16,
        "title": "Epidemic Spread Simulator",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A health department models disease spread in a town of P people. Initially I people are infected. Every day, each infected person infects R new people, but total infected can never exceed P. The simulation runs for at most D days and stops early if everyone becomes infected.",
        "task": "Simulate daily infections and print early completion or final status.",
        "constraints": "1 <= I <= P <= 100000; 0 <= R <= 10; 1 <= D <= 30",
        "sample_input": "1000\n5\n2\n6",
        "expected_output": "Day 1: 15 infected\nDay 2: 45 infected\nDay 3: 135 infected\nDay 4: 405 infected\nDay 5: 1000 infected\nEntire population infected on day 5",
        "hint": "On each day k, newly infected = current * R. current = min(P, current + newly). If current == P, print entire population infected and stop.",
        "starter_code": """# [P50-016] Epidemic Spread Simulator
P = 1000
I = 5
R = 2
D = 6

# Simulate epidemic spread across D days:
""",
        "solution_code": """P = 1000
I = 5
R = 2
D = 6

current = I
finished_early = False

for day in range(1, D + 1):
    current = min(P, current + current * R)
    print(f"Day {day}: {current} infected")
    if current == P:
        print(f"Entire population infected on day {day}")
        finished_early = True
        break

if not finished_early:
    pct = (current / P) * 100
    print(f"Infected after {D} days: {current} ({pct:.1f}% of population)")"""
    },
    {
        "q_num": 17,
        "title": "Serial Number Digit Audit",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A factory prints numeric serial numbers on products. The quality team wants to know which digits repeat. Write a program that, using arithmetic operations (% and //) and a while loop, finds every digit that occurs more than once in the serial number without converting to a string.",
        "task": "Count repeated digits arithmetically and display counts in ascending digit order.",
        "constraints": "1 <= serial number <= 10^18. Do not convert the number to a string.",
        "sample_input": "4829104738",
        "expected_output": "4 appears 2 times\n8 appears 2 times",
        "hint": "Use an array of size 10 to store digit counts. Use `while n > 0: d = n % 10; count[d] += 1; n //= 10`.",
        "starter_code": """# [P50-017] Serial Number Digit Audit
serial = 4829104738

# Find repeated digits using % and // without converting to str:
""",
        "solution_code": """serial = 4829104738

counts = [0] * 10
temp = serial
while temp > 0:
    d = temp % 10
    counts[d] += 1
    temp //= 10

repeated = [(digit, count) for digit, count in enumerate(counts) if count > 1]
if repeated:
    for digit, count in repeated:
        print(f"{digit} appears {count} times")
else:
    print("All digits are unique")"""
    },
    {
        "q_num": 18,
        "title": "Mirror Prime Finder",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A cryptography club is searching for 'mirror primes': numbers that are prime and also read the same forwards and backwards (palindromes). Check the palindrome property by reversing digits arithmetically with a loop.",
        "task": "List all mirror primes in the inclusive range [a, b].",
        "constraints": "1 <= a <= b <= 100000. Reversing must be arithmetic.",
        "sample_input": "10 200",
        "expected_output": "Palindromic primes: 11 101 131 151 181 191\nCount: 6",
        "hint": "Check prime using loop up to int(sqrt(n)). Reverse arithmetically: rev = 0; while temp: rev = rev * 10 + temp % 10; temp //= 10.",
        "starter_code": """# [P50-018] Mirror Prime Finder
a, b = 10, 200

# Find palindromic primes using arithmetic reversing:
""",
        "solution_code": """a, b = 10, 200

def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0:
            return False
        d += 6
    return True

def is_pal(n):
    temp = n
    rev = 0
    while temp > 0:
        rev = rev * 10 + temp % 10
        temp //= 10
    return rev == n

pal_primes = [x for x in range(a, b + 1) if is_pal(x) and is_prime(x)]
if pal_primes:
    print(f"Palindromic primes: {' '.join(map(str, pal_primes))}")
    print(f"Count: {len(pal_primes)}")
else:
    print("No palindromic primes found")"""
    },
    {
        "q_num": 19,
        "title": "Physics Lab Series Calculator",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A physics lab approximates e^x using the first n terms of the series: 1 + x + x^2/2! + x^3/3! + ... + x^(n-1)/(n-1)!. Compute the approximation without math module or factorial function by building each term from the previous term in a loop.",
        "task": "Compute series sum of n terms to 4 decimal places.",
        "constraints": "-10 <= x <= 10; 1 <= n <= 30",
        "sample_input": "1\n5",
        "expected_output": "Sum of 5 terms: 2.7083",
        "hint": "term = 1.0; total = 1.0; For i in range(1, n): term = term * x / i; total += term.",
        "starter_code": """# [P50-019] Physics Lab Series Calculator
x = 1.0
n = 5

# Compute e^x approximation using n terms:
""",
        "solution_code": """x = 1.0
n = 5

term = 1.0
total = 1.0
for i in range(1, n):
    term = term * x / i
    total += term

print(f"Sum of {n} terms: {total:.4f}")"""
    },
    {
        "q_num": 20,
        "title": "Binary Signal Decoder",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A sensor sends a signal as a string of 0s and 1s. Validate it and print: decimal value, number of 1s, longest run of consecutive 1s, and number of transitions (positions where character differs from previous). Convert to decimal with a loop, not with int(s, 2).",
        "task": "Decode binary signal or print 'Invalid Signal'.",
        "constraints": "1 <= length <= 30",
        "sample_input": "1101110011",
        "expected_output": "Decimal Value: 883\nNumber of 1s: 7\nLongest Run of 1s: 3\nTransitions: 4",
        "hint": "Check all chars in '01'. Decimal: dec = 0; for ch in s: dec = dec * 2 + int(ch). Count transitions where s[i] != s[i-1].",
        "starter_code": """# [P50-020] Binary Signal Decoder
signal = '1101110011'

# Validate and decode binary signal:
""",
        "solution_code": """signal = '1101110011'

if not signal or any(ch not in '01' for ch in signal):
    print("Invalid Signal")
else:
    dec = 0
    ones = 0
    longest_run = 0
    curr_run = 0
    transitions = 0
    
    for i, ch in enumerate(signal):
        dec = dec * 2 + int(ch)
        if ch == '1':
            ones += 1
            curr_run += 1
            if curr_run > longest_run:
                longest_run = curr_run
        else:
            curr_run = 0
            
        if i > 0 and signal[i] != signal[i - 1]:
            transitions += 1
            
    print(f"Decimal Value: {dec}")
    print(f"Number of 1s: {ones}")
    print(f"Longest Run of 1s: {longest_run}")
    print(f"Transitions: {transitions}")"""
    },
    {
        "q_num": 21,
        "title": "Mall Parking Collection Report",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A mall charges parking: Bike Rs. 10/hr (day Rs. 80), Car Rs. 30/hr (day Rs. 250), Bus Rs. 80/hr (day Rs. 600). A vehicle is billed the lower of its hourly total and flat day-rate. For N vehicles, print each bill, total collection, and the first vehicle paying highest bill.",
        "task": "Print each vehicle bill, total collection, and highest bill vehicle.",
        "constraints": "1 <= N <= 50; 1 <= hours <= 48",
        "sample_input": "4\nCar 3\nBike 14\nBus 2\nCar 12",
        "expected_output": "Vehicle 1 (Car): Rs. 90\nVehicle 2 (Bike): Rs. 80\nVehicle 3 (Bus): Rs. 160\nVehicle 4 (Car): Rs. 250\nTotal Collection: Rs. 580\nHighest Bill: Vehicle 4",
        "hint": "Hourly and daily caps: Bike (10, 80), Car (30, 250), Bus (80, 600). bill = min(rate * hrs, cap).",
        "starter_code": """# [P50-021] Mall Parking Collection Report
records = [('Car', 3), ('Bike', 14), ('Bus', 2), ('Car', 12)]

# Compute bills, total collection, and highest bill:
""",
        "solution_code": """records = [('Car', 3), ('Bike', 14), ('Bus', 2), ('Car', 12)]

rates = {'Bike': (10, 80), 'Car': (30, 250), 'Bus': (80, 600)}

total = 0
max_bill = -1
max_v = 1

for i, (v_type, hrs) in enumerate(records, 1):
    hourly, cap = rates[v_type]
    bill = min(hourly * hrs, cap)
    total += bill
    if bill > max_bill:
        max_bill = bill
        max_v = i
    print(f"Vehicle {i} ({v_type}): Rs. {bill}")

print(f"Total Collection: Rs. {total}")
print(f"Highest Bill: Vehicle {max_v}")"""
    },
    {
        "q_num": 22,
        "title": "The Hailstone Experiment",
        "part": "Part C: Loops, Patterns and Number Logic",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A maths club studies the Collatz (hailstone) sequence starting from n: if even, divide by 2; if odd, multiply by 3 and add 1; stop when value reaches 1. Print the sequence, total steps taken, and maximum value reached.",
        "task": "Generate Collatz sequence and print sequence, steps, and max value.",
        "constraints": "1 <= n <= 100",
        "sample_input": "6",
        "expected_output": "6 3 10 5 16 8 4 2 1\nSteps: 8\nMaximum Value: 16",
        "hint": "Keep appending to list until n == 1. Steps = len(seq) - 1. Max value = max(seq).",
        "starter_code": """# [P50-022] The Hailstone Experiment
n = 6

# Generate Collatz sequence and statistics:
""",
        "solution_code": """n = 6

seq = [n]
curr = n
while curr != 1:
    if curr % 2 == 0:
        curr //= 2
    else:
        curr = curr * 3 + 1
    seq.append(curr)

print(' '.join(map(str, seq)))
print(f"Steps: {len(seq) - 1}")
print(f"Maximum Value: {max(seq)}")"""
    },

    # =========================================================================
    # Part D: String Handling (Q23 to Q31)
    # =========================================================================
    {
        "q_num": 23,
        "title": "Corporate Firewall Password Audit",
        "part": "Part D: String Handling",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A security portal validates passwords: (1) at least 8 characters, (2) an uppercase letter, (3) a lowercase letter, (4) a digit, and (5) a special character from !@#$%^&*. Spaces are not allowed. Report missing requirements and strength: Weak (0-2 met), Medium (3-4), Strong (all 5).",
        "task": "Audit password criteria, list missing items in order, and evaluate strength.",
        "constraints": "1 <= length <= 50",
        "sample_input": "rahul123",
        "expected_output": "Missing: an uppercase letter\nMissing: a special character (!@#$%^&*)\nStrength: Medium",
        "hint": "Check ' ' in pwd -> Invalid password: spaces are not allowed. Check each requirement in the specified order.",
        "starter_code": """# [P50-023] Corporate Firewall Password Audit
password = 'rahul123'

# Audit password and report missing criteria and strength:
""",
        "solution_code": """password = 'rahul123'

if ' ' in password:
    print("Invalid password: spaces are not allowed")
else:
    specials = set("!@#$%^&*")
    c1 = len(password) >= 8
    c2 = any(c.isupper() for c in password)
    c3 = any(c.islower() for c in password)
    c4 = any(c.isdigit() for c in password)
    c5 = any(c in specials for c in password)
    
    missing = []
    if not c1: missing.append("at least 8 characters")
    if not c2: missing.append("an uppercase letter")
    if not c3: missing.append("a lowercase letter")
    if not c4: missing.append("a digit")
    if not c5: missing.append("a special character (!@#$%^&*)")
    
    met_count = 5 - len(missing)
    if not missing:
        print("All criteria satisfied")
    else:
        for m in missing:
            print(f"Missing: {m}")
            
    if met_count <= 2:
        print("Strength: Weak")
    elif met_count <= 4:
        print("Strength: Medium")
    else:
        print("Strength: Strong")"""
    },
    {
        "q_num": 24,
        "title": "Secret Agent Rolling Cipher",
        "part": "Part D: String Handling",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A rolling cipher encodes text: using key k, the 1st letter is shifted by k, 2nd letter by k+1, 3rd by k+2, etc. Only letters count; spaces, digits, and punctuation are unshifted and do not advance shift. Shifts wrap around the alphabet and preserve case. Write a program to decode an encrypted message.",
        "task": "Decode rolling cipher text back to plain text.",
        "constraints": "1 <= length <= 200; 1 <= k <= 25",
        "sample_input": "Cwxfir ic Nlia!\n2",
        "expected_output": "Attack at Dawn!",
        "hint": "To decode, shift backward by (k + letter_index) % 26. Maintain a counter for letters processed so far.",
        "starter_code": """# [P50-024] Secret Agent Rolling Cipher
ciphertext = 'Cwxfir ic Nlia!'
k = 2

# Decode ciphertext by reversing rolling shift:
""",
        "solution_code": """ciphertext = 'Cwxfir ic Nlia!'
k = 2

res = []
letter_idx = 0

for ch in ciphertext:
    if ch.isalpha():
        shift = (k + letter_idx) % 26
        base = ord('A') if ch.isupper() else ord('a')
        dec_char = chr(base + (ord(ch) - base - shift) % 26)
        res.append(dec_char)
        letter_idx += 1
    else:
        res.append(ch)

print(''.join(res))"""
    },
    {
        "q_num": 25,
        "title": "Chat Shorthand Expander",
        "part": "Part D: String Handling",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A messaging app expands shorthand: u -> you, r -> are, gr8 -> great, pls -> please, thx -> thanks, b4 -> before, idk -> I do not know, brb -> be right back. Whole word matching, case-insensitive, preserves trailing punctuation (. , ! ?). If shorthand starts with uppercase, replacement's first letter must be uppercase.",
        "task": "Expand abbreviations while preserving trailing punctuation and title casing.",
        "constraints": "Words separated by spaces.",
        "sample_input": "Pls call me b4 u leave, thx!",
        "expected_output": "Please call me before you leave, thanks!",
        "hint": "Strip trailing punctuation, look up lowercase word in dict, capitalize if original was capitalized, and reattach punctuation.",
        "starter_code": """# [P50-025] Chat Shorthand Expander
message = 'Pls call me b4 u leave, thx!'

# Expand chat abbreviations:
""",
        "solution_code": """message = 'Pls call me b4 u leave, thx!'

shorthand = {
    'u': 'you',
    'r': 'are',
    'gr8': 'great',
    'pls': 'please',
    'thx': 'thanks',
    'b4': 'before',
    'idk': 'I do not know',
    'brb': 'be right back'
}

punct = set(".,!?")
words = message.split()
res = []

for w in words:
    p = ""
    while w and w[-1] in punct:
        p = w[-1] + p
        w = w[:-1]
    
    w_low = w.lower()
    if w_low in shorthand:
        rep = shorthand[w_low]
        if w and w[0].isupper():
            rep = rep[0].upper() + rep[1:]
        res.append(rep + p)
    else:
        res.append(w + p)

print(' '.join(res))"""
    },
    {
        "q_num": 26,
        "title": "Genome Lab Sequence Report",
        "part": "Part D: String Handling",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "Validate a DNA string: convert to uppercase, ensure only A, C, G, T. Report length, GC-content percentage, reverse complement (reversed string with A<->T, C<->G), and overlapping count of codon 'ATG'.",
        "task": "Print DNA report or 'Invalid DNA Sequence'.",
        "constraints": "1 <= length <= 100",
        "sample_input": "ATGCGATGCAATG",
        "expected_output": "Length: 13\nGC Content: 46.15%\nReverse Complement: CATTGCATCGCAT\nATG Count: 3",
        "hint": "Check all chars in 'ACGT'. GC content = (G+C)/len * 100. Overlapping ATG: sum(1 for i in range(len(s)-2) if s[i:i+3] == 'ATG').",
        "starter_code": """# [P50-026] Genome Lab Sequence Report
dna = 'ATGCGATGCAATG'

# Validate and generate DNA report:
""",
        "solution_code": """dna = 'ATGCGATGCAATG'.upper()

if not dna or any(c not in 'ACGT' for c in dna):
    print("Invalid DNA Sequence")
else:
    n = len(dna)
    gc_count = dna.count('G') + dna.count('C')
    gc_pct = (gc_count / n) * 100
    
    trans = str.maketrans('ACGT', 'TGCA')
    rev_comp = dna.translate(trans)[::-1]
    
    atg_count = sum(1 for i in range(n - 2) if dna[i:i+3] == 'ATG')
    
    print(f"Length: {n}")
    print(f"GC Content: {gc_pct:.2f}%")
    print(f"Reverse Complement: {rev_comp}")
    print(f"ATG Count: {atg_count}")"""
    },
    {
        "q_num": 27,
        "title": "Receipt Number Extractor",
        "part": "Part D: String Handling",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "An expense app scans text from a receipt and extracts every whole number embedded in it (a maximal sequence of consecutive digits, e.g. 'Room101' gives 101). Do not use the re module. Report numbers found, total sum, and largest number.",
        "task": "Extract numbers manually without regex.",
        "constraints": "1 <= length <= 200. No re module.",
        "sample_input": "Paid 250 for tea, 1200 for lunch and 75 for tip",
        "expected_output": "Numbers Found: 250, 1200, 75\nTotal: 1525\nLargest: 1200",
        "hint": "Iterate through characters, accumulating digits into a buffer string. On a non-digit, convert buffer to int if non-empty.",
        "starter_code": """# [P50-027] Receipt Number Extractor
text = 'Paid 250 for tea, 1200 for lunch and 75 for tip'

# Extract numbers without re module:
""",
        "solution_code": """text = 'Paid 250 for tea, 1200 for lunch and 75 for tip'

numbers = []
curr = ""
for ch in text:
    if ch.isdigit():
        curr += ch
    else:
        if curr:
            numbers.append(int(curr))
            curr = ""
if curr:
    numbers.append(int(curr))

if numbers:
    print(f"Numbers Found: {', '.join(map(str, numbers))}")
    print(f"Total: {sum(numbers)}")
    print(f"Largest: {max(numbers)}")
else:
    print("No numbers found")"""
    },
    {
        "q_num": 28,
        "title": "Anagram Detective",
        "part": "Part D: String Handling",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A detective agency checks if two clues are anagrams (ignoring spaces, punctuation, case). Also compute common letters: the sum over each letter of min(count1, count2).",
        "task": "Determine if two strings are anagrams and count common letters.",
        "constraints": "1 <= length <= 100",
        "sample_input": "Dormitory\nDirty room",
        "expected_output": "Anagrams\nCommon Letters: 9",
        "hint": "Filter only lowercase letters. Anagrams if sorted lists match. Common count = sum(min(c1[ch], c2[ch]) for ch in set).",
        "starter_code": """# [P50-028] Anagram Detective
clue1 = 'Dormitory'
clue2 = 'Dirty room'

# Check anagram property and count common letters:
""",
        "solution_code": """clue1 = 'Dormitory'
clue2 = 'Dirty room'

from collections import Counter
s1 = [c.lower() for c in clue1 if c.isalpha()]
s2 = [c.lower() for c in clue2 if c.isalpha()]

c1 = Counter(s1)
c2 = Counter(s2)

common = sum(min(c1[ch], c2[ch]) for ch in set(c1) | set(c2))
is_anagram = (c1 == c2)

print("Anagrams" if is_anagram else "Not Anagrams")
print(f"Common Letters: {common}")"""
    },
    {
        "q_num": 29,
        "title": "Ancient Library Roman Catalogue",
        "part": "Part D: String Handling",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A library has books numbered with Roman numerals. Convert a Roman numeral to an integer (I=1, V=5, X=10, L=50, C=100, D=500, M=1000). If smaller symbol appears before larger one, subtract it. If input contains any other character, print 'Invalid Roman Numeral'.",
        "task": "Convert Roman numeral or print invalid message.",
        "constraints": "1 <= length <= 15",
        "sample_input": "MCMXCIV",
        "expected_output": "Value: 1994",
        "hint": "Map symbols to values. If curr < next, subtract curr; else add curr.",
        "starter_code": """# [P50-029] Ancient Library Roman Catalogue
roman = 'MCMXCIV'

# Convert Roman numeral to integer value:
""",
        "solution_code": """roman = 'MCMXCIV'

vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

if not roman or any(ch not in vals for ch in roman):
    print("Invalid Roman Numeral")
else:
    total = 0
    n = len(roman)
    for i in range(n):
        curr = vals[roman[i]]
        if i + 1 < n and curr < vals[roman[i + 1]]:
            total -= curr
        else:
            total += curr
    print(f"Value: {total}")"""
    },
    {
        "q_num": 30,
        "title": "Treasure Map Mirror Code",
        "part": "Part D: String Handling",
        "difficulty": "Hard",
        "xp": 75,
        "scenario": "A treasure map hides its secret inside the longest palindromic substring of a lowercase string. If multiple substrings have the same maximum length, choose the one with the earliest start index.",
        "task": "Find the longest palindromic substring, its length, and 0-based starting index.",
        "constraints": "1 <= length <= 100",
        "sample_input": "forgeeksskeegfor",
        "expected_output": "Longest Palindrome: geeksskeeg\nLength: 10\nStarting Index: 3",
        "hint": "Check all substrings s[i:j]. If s[i:j] == s[i:j][::-1] and len > max_len, update result.",
        "starter_code": """# [P50-030] Treasure Map Mirror Code
code = 'forgeeksskeegfor'

# Find the earliest longest palindromic substring:
""",
        "solution_code": """code = 'forgeeksskeegfor'

best_sub = ""
best_idx = 0
n = len(code)

for i in range(n):
    for j in range(i + 1, n + 1):
        sub = code[i:j]
        if sub == sub[::-1]:
            if len(sub) > len(best_sub):
                best_sub = sub
                best_idx = i

print(f"Longest Palindrome: {best_sub}")
print(f"Length: {len(best_sub)}")
print(f"Starting Index: {best_idx}")"""
    },
    {
        "q_num": 31,
        "title": "Notice Board Word Wrapper",
        "part": "Part D: String Handling",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A digital notice board displays at most W characters per line. Arrange words into lines such that no word is split, words are separated by one space, and lines are packed greedily. If a single word is longer than W, place it alone on a line unchanged.",
        "task": "Wrap text to width W and print total lines formatted.",
        "constraints": "1 <= W <= 80",
        "sample_input": "20\nThe quick brown fox jumps over the lazy dog near the river bank",
        "expected_output": "The quick brown fox\njumps over the lazy\ndog near the river\nbank\nTotal Lines: 4",
        "hint": "Greedy packing: if curr_len + len(w) + 1 <= W, append to current line; else start new line.",
        "starter_code": """# [P50-031] Notice Board Word Wrapper
W = 20
sentence = 'The quick brown fox jumps over the lazy dog near the river bank'

# Wrap words to max width W:
""",
        "solution_code": """W = 20
sentence = 'The quick brown fox jumps over the lazy dog near the river bank'

words = sentence.split()
lines = []
curr_line = []
curr_len = 0

for w in words:
    if not curr_line:
        curr_line.append(w)
        curr_len = len(w)
    else:
        if curr_len + 1 + len(w) <= W:
            curr_line.append(w)
            curr_len += 1 + len(w)
        else:
            lines.append(' '.join(curr_line))
            curr_line = [w]
            curr_len = len(w)

if curr_line:
    lines.append(' '.join(curr_line))

for l in lines:
    print(l)
print(f"Total Lines: {len(lines)}")"""
    },

    # =========================================================================
    # Part E: Lists and Two-Dimensional Lists (Q32 to Q39)
    # =========================================================================
    {
        "q_num": 32,
        "title": "Garden Spiral Planting Plan",
        "part": "Part E: Lists and Two-Dimensional Lists",
        "difficulty": "Hard",
        "xp": 75,
        "scenario": "A landscape designer plants flowers in an n x n square bed in a clockwise spiral, starting from the top-left corner and moving right, down, left, and up, numbering plants 1 to n^2. Generate the plan using a 2D list.",
        "task": "Generate spiral matrix and print each number right-aligned in width 3.",
        "constraints": "1 <= n <= 10",
        "sample_input": "3",
        "expected_output": "  1  2  3\n  8  9  4\n  7  6  5",
        "hint": "Track top, bottom, left, right bounds. Fill while top <= bottom and left <= right.",
        "starter_code": """# [P50-032] Garden Spiral Planting Plan
n = 3

# Fill n x n spiral matrix and format output:
""",
        "solution_code": """n = 3

mat = [[0] * n for _ in range(n)]
top, bottom, left, right = 0, n - 1, 0, n - 1
val = 1

while top <= bottom and left <= right:
    for c in range(left, right + 1):
        mat[top][c] = val
        val += 1
    top += 1
    for r in range(top, bottom + 1):
        mat[r][right] = val
        val += 1
    right -= 1
    if top <= bottom:
        for c in range(right, left - 1, -1):
            mat[bottom][c] = val
            val += 1
        bottom -= 1
    if left <= right:
        for r in range(bottom, top - 1, -1):
            mat[r][left] = val
            val += 1
        left += 1

for row in mat:
    print(''.join(f"{x:3d}" for x in row))"""
    },
    {
        "q_num": 33,
        "title": "Warehouse Shelf Grid Audit",
        "part": "Part E: Lists and Two-Dimensional Lists",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A warehouse is an r x c grid of shelves storing box counts. Report: row totals, column totals, location of fullest shelf (first in row-major order if tied, 1-based), and number of shelves holding fewer boxes than threshold T.",
        "task": "Audit warehouse shelf matrix and print metrics.",
        "constraints": "1 <= r, c <= 10",
        "sample_input": "3 4\n12 5 30 8\n7 22 3 15\n18 9 11 40\n10",
        "expected_output": "Row totals: 55 47 78\nColumn totals: 37 36 44 63\nFullest shelf: 40 at (row 3, column 4)\nShelves below threshold: 5",
        "hint": "row_totals = [sum(row) for row in grid]. col_totals = [sum(grid[r][c] for r in range(R)) for c in range(C)].",
        "starter_code": """# [P50-033] Warehouse Shelf Grid Audit
r, c = 3, 4
grid = [
    [12, 5, 30, 8],
    [7, 22, 3, 15],
    [18, 9, 11, 40]
]
T = 10

# Compute row/col totals, fullest shelf, and below threshold count:
""",
        "solution_code": """r, c = 3, 4
grid = [
    [12, 5, 30, 8],
    [7, 22, 3, 15],
    [18, 9, 11, 40]
]
T = 10

row_totals = [sum(row) for row in grid]
col_totals = [sum(grid[i][j] for i in range(r)) for j in range(c)]

max_val = -1
max_pos = (1, 1)
below_t = 0

for i in range(r):
    for j in range(c):
        val = grid[i][j]
        if val > max_val:
            max_val = val
            max_pos = (i + 1, j + 1)
        if val < T:
            below_t += 1

print(f"Row totals: {' '.join(map(str, row_totals))}")
print(f"Column totals: {' '.join(map(str, col_totals))}")
print(f"Fullest shelf: {max_val} at (row {max_pos[0]}, column {max_pos[1]})")
print(f"Shelves below threshold: {below_t}")"""
    },
    {
        "q_num": 34,
        "title": "Lost Parcel Detective",
        "part": "Part E: Lists and Two-Dimensional Lists",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A courier hub scans n parcels that should carry IDs 1 to n. Due to a scanner glitch, one ID was scanned twice and one ID was never scanned. Find the duplicate ID and missing ID without using sets or dictionaries.",
        "task": "Find duplicate and missing ID using lists or arithmetic sums only.",
        "constraints": "2 <= n <= 1000. Exactly one duplicate and one missing. No sets or dicts.",
        "sample_input": "8\n3 1 4 6 2 8 4 7",
        "expected_output": "Duplicate: 4\nMissing: 5",
        "hint": "Count occurrences using a frequency list of size n+1: counts = [0]*(n+1).",
        "starter_code": """# [P50-034] Lost Parcel Detective
n = 8
parcels = [3, 1, 4, 6, 2, 8, 4, 7]

# Find duplicate and missing ID without sets/dicts:
""",
        "solution_code": """n = 8
parcels = [3, 1, 4, 6, 2, 8, 4, 7]

counts = [0] * (n + 1)
for x in parcels:
    counts[x] += 1

dup = -1
miss = -1
for i in range(1, n + 1):
    if counts[i] == 2:
        dup = i
    elif counts[i] == 0:
        miss = i

print(f"Duplicate: {dup}")
print(f"Missing: {miss}")"""
    },
    {
        "q_num": 35,
        "title": "Stock Trader's Best Deal",
        "part": "Part E: Lists and Two-Dimensional Lists",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A trader may buy on one day and sell on a later day (only once). Find best buy day, sell day, and maximum profit. If several choices give the same profit, choose the one with the earliest sell day, and then earliest buy day.",
        "task": "Identify optimal buy and sell days for maximum profit.",
        "constraints": "2 <= n <= 1000; days numbered from 1.",
        "sample_input": "7\n100 180 260 310 40 535 695",
        "expected_output": "Buy on day 5 at 40\nSell on day 7 at 695\nMaximum profit: 655",
        "hint": "Track max profit and compare pairs (buy_day, sell_day) with sell_day > buy_day.",
        "starter_code": """# [P50-035] Stock Trader's Best Deal
n = 7
prices = [100, 180, 260, 310, 40, 535, 695]

# Find best transaction or report no profitable transaction:
""",
        "solution_code": """n = 7
prices = [100, 180, 260, 310, 40, 535, 695]

best_profit = 0
best_deal = None

for sell_idx in range(1, n):
    for buy_idx in range(sell_idx):
        profit = prices[sell_idx] - prices[buy_idx]
        if profit > best_profit:
            best_profit = profit
            best_deal = (buy_idx + 1, prices[buy_idx], sell_idx + 1, prices[sell_idx])

if best_deal and best_profit > 0:
    b_day, b_pr, s_day, s_pr = best_deal
    print(f"Buy on day {b_day} at {b_pr}")
    print(f"Sell on day {s_day} at {s_pr}")
    print(f"Maximum profit: {best_profit}")
else:
    print("No profitable transaction possible.")"""
    },
    {
        "q_num": 36,
        "title": "Satellite Image Rotation",
        "part": "Part E: Lists and Two-Dimensional Lists",
        "difficulty": "Beginner",
        "xp": 30,
        "scenario": "A satellite sends an n x n square image as a grid of pixel values. Before display, rotate the grid 90 degrees clockwise.",
        "task": "Rotate n x n matrix 90 degrees clockwise.",
        "constraints": "1 <= n <= 10",
        "sample_input": "3\n1 2 3\n4 5 6\n7 8 9",
        "expected_output": "7 4 1\n8 5 2\n9 6 3",
        "hint": "Rotated row r is formed by column r of the original grid taken from bottom to top: grid[n-1-i][j].",
        "starter_code": """# [P50-036] Satellite Image Rotation
n = 3
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Rotate grid 90 degrees clockwise:
""",
        "solution_code": """n = 3
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = []
for col in range(n):
    rotated_row = [grid[row][col] for row in range(n - 1, -1, -1)]
    rotated.append(rotated_row)

for row in rotated:
    print(' '.join(map(str, row)))"""
    },
    {
        "q_num": 37,
        "title": "Esports Leaderboard Merger",
        "part": "Part E: Lists and Two-Dimensional Lists",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "Two esports servers each keep a leaderboard sorted highest to lowest. Merge them into one leaderboard (equal scores take element from 1st list before 2nd) comparing elements one by one; sort(), sorted(), max() are not allowed. Report top K scores, total players, and rank of score S (rank = 1 + count of scores strictly greater).",
        "task": "Two-pointer merge without built-in sorting.",
        "constraints": "1 <= K <= total players. No sort/sorted/max.",
        "sample_input": "980 870 870 640\n990 870 720 500\n5\n870",
        "expected_output": "Top 5 Scores: 990 980 870 870 870\nTotal Players: 8\nRank of 870: 3",
        "hint": "Use two pointers i and j. If A[i] >= B[j], append A[i] and i += 1; else append B[j] and j += 1. Rank = 1 + sum(1 for x in merged if x > S).",
        "starter_code": """# [P50-037] Esports Leaderboard Merger
server_A = [980, 870, 870, 640]
server_B = [990, 870, 720, 500]
K = 5
S = 870

# Merge leaderboards without sort() or sorted():
""",
        "solution_code": """server_A = [980, 870, 870, 640]
server_B = [990, 870, 720, 500]
K = 5
S = 870

merged = []
i = 0
j = 0
while i < len(server_A) and j < len(server_B):
    if server_A[i] >= server_B[j]:
        merged.append(server_A[i])
        i += 1
    else:
        merged.append(server_B[j])
        j += 1

while i < len(server_A):
    merged.append(server_A[i])
    i += 1

while j < len(server_B):
    merged.append(server_B[j])
    j += 1

print(f"Top {K} Scores: {' '.join(map(str, merged[:K]))}")
print(f"Total Players: {len(merged)}")

if S in merged:
    rank = 1 + sum(1 for x in merged if x > S)
    print(f"Rank of {S}: {rank}")
else:
    print(f"Score {S} not found")"""
    },
    {
        "q_num": 38,
        "title": "Solar Farm Best Stretch",
        "part": "Part E: Lists and Two-Dimensional Lists",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A solar farm records net energy (kWh) for n consecutive days (some negative). Find the contiguous stretch of days with the largest total energy. If multiple stretches tie, choose the earliest start day, and then the shortest length.",
        "task": "Find maximum subarray stretch with tie-breaking rules.",
        "constraints": "1 <= n <= 100",
        "sample_input": "9\n-2 1 -3 4 -1 2 1 -5 4",
        "expected_output": "Best Period: Day 4 to Day 7\nTotal Net Energy: 6",
        "hint": "Check all pairs (i, j). Maintain best sum, best start, best length.",
        "starter_code": """# [P50-038] Solar Farm Best Stretch
n = 9
energy = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Find best contiguous period:
""",
        "solution_code": """n = 9
energy = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

best_sum = -float('inf')
best_start = 0
best_end = 0
best_len = float('inf')

for i in range(n):
    curr_sum = 0
    for j in range(i, n):
        curr_sum += energy[j]
        l = j - i + 1
        if curr_sum > best_sum:
            best_sum = curr_sum
            best_start = i
            best_end = j
            best_len = l
        elif curr_sum == best_sum:
            if i < best_start:
                best_start = i
                best_end = j
                best_len = l
            elif i == best_start and l < best_len:
                best_end = j
                best_len = l

print(f"Best Period: Day {best_start + 1} to Day {best_end + 1}")
print(f"Total Net Energy: {best_sum}")"""
    },
    {
        "q_num": 39,
        "title": "The Elimination Game",
        "part": "Part E: Lists and Two-Dimensional Lists",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "In a reality show, n contestants numbered 1 to n stand in a circle. Counting starts from contestant 1 and every k-th contestant (counting current as 1) is eliminated; counting restarts from next contestant. Continue until one winner remains.",
        "task": "Simulate Josephus elimination circle and print order and winner.",
        "constraints": "2 <= n <= 100; 1 <= k <= 100",
        "sample_input": "7 3",
        "expected_output": "Elimination Order: 3 6 2 7 5 1\nWinner: 4",
        "hint": "Maintain circular index: idx = (idx + k - 1) % len(circle). pop contestant and record in order.",
        "starter_code": """# [P50-039] The Elimination Game
n, k = 7, 3

# Simulate elimination circle:
""",
        "solution_code": """n, k = 7, 3

circle = list(range(1, n + 1))
elim = []
idx = 0

while len(circle) > 1:
    idx = (idx + k - 1) % len(circle)
    elim.append(circle.pop(idx))

print(f"Elimination Order: {' '.join(map(str, elim))}")
print(f"Winner: {circle[0]}")"""
    },

    # =========================================================================
    # Part F: User-Defined Functions and Recursion (Q40 to Q50)
    # =========================================================================
    {
        "q_num": 40,
        "title": "Electricity Board Billing Function",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "An electricity board uses slabs: first 100 units @ Rs. 3.50/unit, next 100 units @ Rs. 5.00/unit, above 200 units @ Rs. 7.50/unit. Fixed charge Rs. 60. Senior citizens get 15% discount on energy charge only. Electricity duty of 6% is levied on (energy charge - discount + fixed charge). Write function calculate_bill(units, senior=False).",
        "task": "Implement calculate_bill function and display breakdown.",
        "constraints": "1 <= units <= 5000",
        "sample_input": "340\nRegular",
        "expected_output": "Energy Charge: Rs. 1900.00\nDiscount: Rs. 0.00\nFixed Charge: Rs. 60.00\nDuty: Rs. 117.60\nNet Payable: Rs. 2077.60",
        "hint": "Calculate energy charge across slabs (0-100, 101-200, >200). Discount = 0.15 * energy if senior else 0. Duty = 0.06 * (energy - disc + 60).",
        "starter_code": """# [P50-040] Electricity Board Billing Function
units = 340
category = 'Regular'

def calculate_bill(units, senior=False):
    # TODO: Implement function returning (energy, discount, fixed, duty, net)
    pass

# Call calculate_bill and format output:
""",
        "solution_code": """units = 340
category = 'Regular'

def calculate_bill(units, senior=False):
    if units <= 100:
        energy = units * 3.50
    elif units <= 200:
        energy = 100 * 3.50 + (units - 100) * 5.00
    else:
        energy = 100 * 3.50 + 100 * 5.00 + (units - 200) * 7.50
        
    discount = energy * 0.15 if senior else 0.0
    fixed = 60.00
    duty = (energy - discount + fixed) * 0.06
    net = energy - discount + fixed + duty
    return energy, discount, fixed, duty, net

energy, discount, fixed, duty, net = calculate_bill(units, senior=(category == 'Senior'))
print(f"Energy Charge: Rs. {energy:.2f}")
print(f"Discount: Rs. {discount:.2f}")
print(f"Fixed Charge: Rs. {fixed:.2f}")
print(f"Duty: Rs. {duty:.2f}")
print(f"Net Payable: Rs. {net:.2f}")"""
    },
    {
        "q_num": 41,
        "title": "Prime Toolkit for a Cryptography Class",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A cryptography class needs three helper functions: is_prime(n) returning True/False, next_prime(n) returning smallest prime > n, and prime_factors(n) returning prime factors of n in non-decreasing order.",
        "task": "Implement all 3 functions and test with input number.",
        "constraints": "2 <= n <= 100000",
        "sample_input": "84",
        "expected_output": "Prime: No\nNext prime: 89\nPrime factors: 2 x 2 x 3 x 7",
        "hint": "Check prime up to sqrt(n). In prime_factors, divide out 2 then odd factors d from 3 upwards.",
        "starter_code": """# [P50-041] Prime Toolkit for a Cryptography Class
n = 84

def is_prime(n):
    pass

def next_prime(n):
    pass

def prime_factors(n):
    pass

# Call functions and format output:
""",
        "solution_code": """n = 84

def is_prime(n):
    if n < 2: return False
    if n in (2, 3): return True
    if n % 2 == 0 or n % 3 == 0: return False
    d = 5
    while d * d <= n:
        if n % d == 0 or n % (d + 2) == 0: return False
        d += 6
    return True

def next_prime(n):
    cand = n + 1
    while not is_prime(cand):
        cand += 1
    return cand

def prime_factors(n):
    factors = []
    d = 2
    temp = n
    while d * d <= temp:
        while temp % d == 0:
            factors.append(d)
            temp //= d
        d += 1
    if temp > 1:
        factors.append(temp)
    return factors

print(f"Prime: {'Yes' if is_prime(n) else 'No'}")
print(f"Next prime: {next_prime(n)}")
factors = prime_factors(n)
print(f"Prime factors: {' x '.join(map(str, factors))}")"""
    },
    {
        "q_num": 42,
        "title": "Sensor Data Analyser",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A weather station sends n readings. Write function analyse(data) that returns five values: minimum, maximum, mean, median, and mode (if tie, mode is the smallest of them; median is average of two middle values if even). Do not use the statistics module.",
        "task": "Compute statistical metrics without statistics module.",
        "constraints": "1 <= n <= 100",
        "sample_input": "8\n4 9 4 7 1 9 4 6",
        "expected_output": "Minimum: 1\nMaximum: 9\nMean: 5.50\nMedian: 5.00\nMode: 4",
        "hint": "Sort data. Mean = sum/n. Median = s[n//2] if odd else (s[n//2-1]+s[n//2])/2. Mode = element with highest frequency, picking smallest on tie.",
        "starter_code": """# [P50-042] Sensor Data Analyser
n = 8
data = [4, 9, 4, 7, 1, 9, 4, 6]

def analyse(data):
    # Return (minimum, maximum, mean, median, mode)
    pass

# Run analysis and print formatted results:
""",
        "solution_code": """n = 8
data = [4, 9, 4, 7, 1, 9, 4, 6]

def analyse(data):
    s_data = sorted(data)
    d_min = s_data[0]
    d_max = s_data[-1]
    d_mean = sum(s_data) / len(s_data)
    
    m = len(s_data)
    if m % 2 == 1:
        d_median = float(s_data[m // 2])
    else:
        d_median = (s_data[m // 2 - 1] + s_data[m // 2]) / 2.0
        
    counts = {}
    for x in s_data:
        counts[x] = counts.get(x, 0) + 1
        
    max_freq = max(counts.values())
    modes = [k for k, v in counts.items() if v == max_freq]
    d_mode = min(modes)
    
    return d_min, d_max, d_mean, d_median, d_mode

mn, mx, mean, med, mode = analyse(data)
print(f"Minimum: {mn}")
print(f"Maximum: {mx}")
print(f"Mean: {mean:.2f}")
print(f"Median: {med:.2f}")
print(f"Mode: {mode}")"""
    },
    {
        "q_num": 43,
        "title": "Gymnastics Judging Panel",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "In a gymnastics event, final score drops single highest and lowest scores, averages the rest, and adds bonus. Write function final_score(*scores, bonus=0) returning -1 if fewer than 3 scores supplied.",
        "task": "Compute trimmed gymnastics score with arbitrary arguments.",
        "constraints": "1 <= judges <= 15",
        "sample_input": "8.5 9.0 7.5 9.5 8.0\n0.3",
        "expected_output": "Judges: 5\nDropped Scores: 7.5, 9.5\nFinal Score: 8.80",
        "hint": "If len(scores) < 3 return -1. Else dropped are min(scores) and max(scores). Sum remaining, divide by len-2, and add bonus.",
        "starter_code": """# [P50-043] Gymnastics Judging Panel
scores = [8.5, 9.0, 7.5, 9.5, 8.0]
bonus = 0.3

def final_score(*scores, bonus=0):
    pass

# Unpack scores and print judging results:
""",
        "solution_code": """scores = [8.5, 9.0, 7.5, 9.5, 8.0]
bonus = 0.3

def final_score(*scores, bonus=0):
    if len(scores) < 3:
        return -1, None, None
    s = sorted(scores)
    lowest = s[0]
    highest = s[-1]
    trimmed = s[1:-1]
    avg = sum(trimmed) / len(trimmed)
    return avg + bonus, lowest, highest

res, low, high = final_score(*scores, bonus=bonus)
if res == -1:
    print("At least 3 judges are required")
else:
    print(f"Judges: {len(scores)}")
    print(f"Dropped Scores: {low:.1f}, {high:.1f}")
    print(f"Final Score: {res:.2f}")"""
    },
    {
        "q_num": 44,
        "title": "Temple Tower Puzzle",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A temple has three pegs: A (source), B (helper), C (destination), with n discs on A. Discs move one at a time, never placing a larger disc on smaller. Write recursive function hanoi(n, source, helper, destination) printing every move and returning total moves made.",
        "task": "Implement recursive Tower of Hanoi.",
        "constraints": "1 <= n <= 5",
        "sample_input": "3",
        "expected_output": "Move disk 1 from A to C\nMove disk 2 from A to B\nMove disk 1 from C to B\nMove disk 3 from A to C\nMove disk 1 from B to A\nMove disk 2 from B to C\nMove disk 1 from A to C\nTotal Moves: 7",
        "hint": "hanoi(n-1, src, dst, hlp), move disk n from src to dst, hanoi(n-1, hlp, src, dst). Total moves = 2^n - 1.",
        "starter_code": """# [P50-044] Temple Tower Puzzle
n = 3

def hanoi(n, source, helper, destination):
    # Print moves and return total count
    pass

# Solve Tower of Hanoi:
""",
        "solution_code": """n = 3

def hanoi(n, source, helper, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return 1
    m1 = hanoi(n - 1, source, destination, helper)
    print(f"Move disk {n} from {source} to {destination}")
    m2 = hanoi(n - 1, helper, source, destination)
    return m1 + 1 + m2

total_moves = hanoi(n, 'A', 'B', 'C')
print(f"Total Moves: {total_moves}")"""
    },
    {
        "q_num": 45,
        "title": "Robot Staircase Paths",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A robot climbs a staircase of n steps and can climb 1, 2, or 3 steps at a time. Write recursive function ways(n) returning distinct ways to reach top (ways(0) = 1, negative steps = 0). Use global counter with global keyword to report how many times function was called in total.",
        "task": "Compute staircase paths and recursive calls counter.",
        "constraints": "0 <= n <= 15",
        "sample_input": "4",
        "expected_output": "Number of Ways: 7\nRecursive Calls: 25",
        "hint": "Increment global calls at start of function. If n < 0 return 0; if n == 0 return 1; return ways(n-1) + ways(n-2) + ways(n-3).",
        "starter_code": """# [P50-045] Robot Staircase Paths
n = 4

calls = 0
def ways(n):
    global calls
    calls += 1
    # Implement recursion
    pass

# Run ways(n) and report results:
""",
        "solution_code": """n = 4

calls = 0

def ways(n):
    global calls
    calls += 1
    if n < 0:
        return 0
    if n == 0:
        return 1
    return ways(n - 1) + ways(n - 2) + ways(n - 3)

ans = ways(n)
print(f"Number of Ways: {ans}")
print(f"Recursive Calls: {calls}")"""
    },
    {
        "q_num": 46,
        "title": "College Roll Number Search",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A college keeps roll numbers sorted. Write recursive function binary_search(arr, key, low, high) returning tuple (index, calls), where index is 0-based position (-1 if absent) and calls is function calls made including the first. Middle index mid = (low + high) // 2.",
        "task": "Implement recursive binary search returning index and call count.",
        "constraints": "1 <= n <= 100",
        "sample_input": "10\n101 105 110 118 125 131 140 152 160 175\n131",
        "expected_output": "Found at position 6\nCalls Made: 3",
        "hint": "If low > high return (-1, 1). mid = (low+high)//2. If arr[mid] == key return (mid, 1). Else recurse and add 1 to returned calls.",
        "starter_code": """# [P50-046] College Roll Number Search
n = 10
arr = [101, 105, 110, 118, 125, 131, 140, 152, 160, 175]
key = 131

def binary_search(arr, key, low, high):
    pass

# Search for roll number:
""",
        "solution_code": """n = 10
arr = [101, 105, 110, 118, 125, 131, 140, 152, 160, 175]
key = 131

def binary_search(arr, key, low, high):
    if low > high:
        return -1, 1
    mid = (low + high) // 2
    if arr[mid] == key:
        return mid, 1
    elif key < arr[mid]:
        idx, calls = binary_search(arr, key, low, mid - 1)
        return idx, calls + 1
    else:
        idx, calls = binary_search(arr, key, mid + 1, high)
        return idx, calls + 1

idx, calls = binary_search(arr, key, 0, n - 1)
if idx != -1:
    print(f"Found at position {idx + 1}")
else:
    print("Not Found")
print(f"Calls Made: {calls}")"""
    },
    {
        "q_num": 47,
        "title": "Sensor Noise Cleaner",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "Write two functions: clean_readings(data, low, high) which removes values outside [low, high] in-place and returns count removed; and normalized_copy(data) returning a new list where each x becomes (x - min)/(max - min) rounded to 2 decimals (0.00 if max == min).",
        "task": "Clean data in place and return normalized copy.",
        "constraints": "1 <= n <= 100",
        "sample_input": "8\n22 25 -999 27 24 1000 26 23\n20 30",
        "expected_output": "Removed: 2\nClean Readings: 22 25 27 24 26 23\nNormalized: 0.00 0.60 1.00 0.40 0.80 0.20",
        "hint": "In-place removal: iterate backwards or rebuild slice `data[:] = [x for x in data if low <= x <= high]`. Normalize using min/max of cleaned data.",
        "starter_code": """# [P50-047] Sensor Noise Cleaner
n = 8
data = [22, 25, -999, 27, 24, 1000, 26, 23]
low, high = 20, 30

def clean_readings(data, low, high):
    pass

def normalized_copy(data):
    pass

# Clean and normalize readings:
""",
        "solution_code": """n = 8
data = [22, 25, -999, 27, 24, 1000, 26, 23]
low, high = 20, 30

def clean_readings(data, low, high):
    orig_len = len(data)
    data[:] = [x for x in data if low <= x <= high]
    return orig_len - len(data)

def normalized_copy(data):
    if not data:
        return []
    mn = min(data)
    mx = max(data)
    if mn == mx:
        return [0.0] * len(data)
    return [round((x - mn) / (mx - mn), 2) for x in data]

removed = clean_readings(data, low, high)
norm = normalized_copy(data)

print(f"Removed: {removed}")
print(f"Clean Readings: {' '.join(map(str, data))}")
print(f"Normalized: {' '.join(f'{x:.2f}' for x in norm)}")"""
    },
    {
        "q_num": 48,
        "title": "HR Payroll Sorting with Lambda",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "An HR department stores records as [name, department, salary]. Using sorted() with lambda functions, print records: (i) sorted by name alphabetically, and (ii) sorted by department alphabetically and salary descending within department. Also write top_earners(records, n=3) returning names of top n highest-paid employees.",
        "task": "Perform multi-criteria lambda sorting and top earners retrieval.",
        "constraints": "3 <= N <= 20",
        "sample_input": "5\nMeera HR 45000\nArjun IT 72000\nZoya IT 68000\nKabir HR 52000\nAnita Finance 61000",
        "expected_output": "Sorted by Name:\nAnita - Finance - 61000\nArjun - IT - 72000\nKabir - HR - 52000\nMeera - HR - 45000\nZoya - IT - 68000\nSorted by Department and Salary:\nAnita - Finance - 61000\nKabir - HR - 52000\nMeera - HR - 45000\nArjun - IT - 72000\nZoya - IT - 68000\nTop 3 Earners: Arjun, Zoya, Anita",
        "hint": "Name sort: key=lambda x: x[0]. Dept & Salary: key=lambda x: (x[1], -x[2]). Top earners: sorted by salary desc.",
        "starter_code": """# [P50-048] HR Payroll Sorting with Lambda
records = [
    ['Meera', 'HR', 45000],
    ['Arjun', 'IT', 72000],
    ['Zoya', 'IT', 68000],
    ['Kabir', 'HR', 52000],
    ['Anita', 'Finance', 61000]
]

# Sort using lambda and find top earners:
""",
        "solution_code": """records = [
    ['Meera', 'HR', 45000],
    ['Arjun', 'IT', 72000],
    ['Zoya', 'IT', 68000],
    ['Kabir', 'HR', 52000],
    ['Anita', 'Finance', 61000]
]

def top_earners(recs, n=3):
    s = sorted(recs, key=lambda x: -x[2])
    return [r[0] for r in s[:n]]

by_name = sorted(records, key=lambda x: x[0])
print("Sorted by Name:")
for r in by_name:
    print(f"{r[0]} - {r[1]} - {r[2]}")

by_dept_sal = sorted(records, key=lambda x: (x[1], -x[2]))
print("Sorted by Department and Salary:")
for r in by_dept_sal:
    print(f"{r[0]} - {r[1]} - {r[2]}")

top3 = top_earners(records, 3)
print(f"Top 3 Earners: {', '.join(top3)}")"""
    },
    {
        "q_num": 49,
        "title": "Calendar Utility Library",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A planner app needs date utility functions: is_leap(year), days_in_month(month, year), day_of_year(day, month, year), and days_since_start(day, month, year) from 01-01-0001 (day 1). For two dates, print day-of-year of each date, absolute days between them, and in weeks and days format.",
        "task": "Build modular date utility library and compute elapsed time.",
        "constraints": "Valid dates between years 1 and 9999.",
        "sample_input": "15 8 2023\n26 1 2024",
        "expected_output": "Date 1: Day 227 of 2023\nDate 2: Day 26 of 2024\nDays Between: 164\nWeeks and Days: 23 weeks 3 days",
        "hint": "days_since_start sums full years days + day_of_year. Days between = abs(d1 - d2). Weeks = diff // 7, Days = diff % 7.",
        "starter_code": """# [P50-049] Calendar Utility Library
d1, m1, y1 = 15, 8, 2023
d2, m2, y2 = 26, 1, 2024

def is_leap(year):
    pass

def days_in_month(month, year):
    pass

def day_of_year(day, month, year):
    pass

def days_since_start(day, month, year):
    pass

# Compute day-of-year and difference:
""",
        "solution_code": """d1, m1, y1 = 15, 8, 2023
d2, m2, y2 = 26, 1, 2024

def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def days_in_month(month, year):
    days = [0, 31, 29 if is_leap(year) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return days[month]

def day_of_year(day, month, year):
    return sum(days_in_month(m, year) for m in range(1, month)) + day

def days_since_start(day, month, year):
    y = year - 1
    # Leap years up to y
    leaps = y // 4 - y // 100 + y // 400
    return y * 365 + leaps + day_of_year(day, month, year)

doy1 = day_of_year(d1, m1, y1)
doy2 = day_of_year(d2, m2, y2)

total_days1 = days_since_start(d1, m1, y1)
total_days2 = days_since_start(d2, m2, y2)
diff = abs(total_days1 - total_days2)

weeks = diff // 7
rem_days = diff % 7

print(f"Date 1: Day {doy1} of {y1}")
print(f"Date 2: Day {doy2} of {y2}")
print(f"Days Between: {diff}")
print(f"Weeks and Days: {weeks} weeks {rem_days} days")"""
    },
    {
        "q_num": 50,
        "title": "Digital Bank Transaction Processor",
        "part": "Part F: User-Defined Functions and Recursion",
        "difficulty": "Intermediate",
        "xp": 50,
        "scenario": "A digital bank starts with balance Rs. 5000. Write function process(balance, op, amount, withdrawals). Rules: op 'D' (deposit): amount > 0 (else Invalid amount); amount > 50000 not applied (Deposit flagged: KYC required); else Deposited <amount>. op 'W' (withdrawal): amount > 0 and % 100 == 0 (else Invalid amount); first 3 successful withdrawals free, afterwards fee Rs. 20; declined if balance - (amount + fee) < 500 (Declined: Insufficient balance); else Withdrew <amount> (add (fee 20) if fee charged). Other ops give Invalid operation.",
        "task": "Process transactions log and report final balance and withdrawal count.",
        "constraints": "1 <= N <= 30",
        "sample_input": "9\nD 2000\nW 1500\nW 2000\nW 3000\nD 5000\nW 1000\nD 60000\nX 100\nW 150",
        "expected_output": "Txn 1: Deposited 2000 | Balance: 7000\nTxn 2: Withdrew 1500 | Balance: 5500\nTxn 3: Withdrew 2000 | Balance: 3500\nTxn 4: Withdrew 3000 | Balance: 500\nTxn 5: Deposited 5000 | Balance: 5500\nTxn 6: Withdrew 1000 (fee 20) | Balance: 4480\nTxn 7: Deposit flagged: KYC required | Balance: 4480\nTxn 8: Invalid operation | Balance: 4480\nTxn 9: Invalid amount | Balance: 4480\nFinal Balance: 4480\nSuccessful Withdrawals: 4",
        "hint": "Check op. If D: check <= 0 (Invalid amount), > 50000 (KYC), else add. If W: check > 0 and % 100 == 0. Fee is 20 if withdrawals >= 3. Check balance - amount - fee >= 500.",
        "starter_code": """# [P50-050] Digital Bank Transaction Processor
balance = 5000
transactions = [
    ('D', 2000),
    ('W', 1500),
    ('W', 2000),
    ('W', 3000),
    ('D', 5000),
    ('W', 1000),
    ('D', 60000),
    ('X', 100),
    ('W', 150)
]

def process(balance, op, amount, withdrawals):
    # Returns (updated_balance, message, updated_withdrawals)
    pass

# Execute transactions log:
""",
        "solution_code": """balance = 5000
transactions = [
    ('D', 2000),
    ('W', 1500),
    ('W', 2000),
    ('W', 3000),
    ('D', 5000),
    ('W', 1000),
    ('D', 60000),
    ('X', 100),
    ('W', 150)
]

def process(balance, op, amount, withdrawals):
    if op == 'D':
        if amount <= 0:
            return balance, "Invalid amount", withdrawals
        if amount > 50000:
            return balance, "Deposit flagged: KYC required", withdrawals
        return balance + amount, f"Deposited {amount}", withdrawals
    elif op == 'W':
        if amount <= 0 or amount % 100 != 0:
            return balance, "Invalid amount", withdrawals
        fee = 20 if withdrawals >= 3 else 0
        if balance - (amount + fee) < 500:
            return balance, "Declined: Insufficient balance", withdrawals
        new_bal = balance - (amount + fee)
        fee_str = " (fee 20)" if fee > 0 else ""
        return new_bal, f"Withdrew {amount}{fee_str}", withdrawals + 1
    else:
        return balance, "Invalid operation", withdrawals

withdrawals = 0
for i, (op, amt) in enumerate(transactions, 1):
    balance, msg, withdrawals = process(balance, op, amt, withdrawals)
    print(f"Txn {i}: {msg} | Balance: {balance}")

print(f"Final Balance: {balance}")
print(f"Successful Withdrawals: {withdrawals}")"""
    }
]
