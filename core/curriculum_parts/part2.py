"""
Part 2: Making Decisions and Repeating Actions
Chapters 6 and 7 with exact syllabus titles, subtopics, and mini-projects.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 6: The Crossroads (Control Flow)
    # =========================================================================
    {
        "id": "ch6_control_flow",
        "part_number": 2,
        "part_title": "PART 2: MAKING DECISIONS AND REPEATING ACTIONS",
        "chapter_number": 6,
        "title": "Chapter 6: The Crossroads (Control Flow)",
        "subtitle_en": "Guide code execution with if, elif, else, indentation laws, nested conditions, and an adventure game",
        "subtitle_hi": "Code ka rasta chunna: if, elif, else, indentation ke niyam aur adventure game",
        "icon": "🔀",
        "estimated_time": "40 mins",
        "prerequisites_en": "Part 1 (Variables, data types, and comparison operators).",
        "prerequisites_hi": "Part 1 (Variables, data types aur comparison operators).",
        "learning_objectives_en": [
            "Understand linear sequential execution (top to bottom)",
            "Master if, elif, and else branching logic",
            "Conquer indentation rules (4 spaces, avoiding tab/space mixing)",
            "Build nested decision matrices (conditions inside conditions)",
            "Build Mini-Project: A Choose-Your-Own-Adventure Text Game"
        ],
        "learning_objectives_hi": [
            "Sequential code flow samjho (upar se neeche)",
            "if, elif, aur else branches master karo",
            "Indentation rules (4 spaces) seekho taaki IndentationError na aaye",
            "Nested if conditions banao",
            "Mini-Project: Choose-Your-Own-Adventure Game complete karo"
        ],
        "recap_en": "You mastered conditional branching with if, elif, else, conquered indentation laws, implemented nested decisions, and built an interactive choose-your-own-adventure game.",
        "recap_hi": "Aapne if, elif, else decision making, indentation rules aur apna adventure game banaya.",
        "subtopics": [
            {
                "id": "ch6_sub1_flow_of_code",
                "title": "Understanding the flow of code (top to bottom)",
                "title_hi": "Code ka flow samajhna (upar se neeche)",
                "icon": "⬇️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Sequential execution means Python reads and executes code line-by-line from top to bottom, one statement at a time. Control flow statements (if, while, for) allow code to branch, skip, or repeat sections.",
                "what_is_it_hi": "Sequential execution ka matlab hai ki computer pehli line se shuru karke aakhri line tak ek-ek line order me chalaata hai. Control flow statements raste me mod (diversion) laate hain.",
                "why_need_it_en": "Real software isn't just a static script; it must take different paths depending on whether a user is logged in, a sensor is active, or an account has funds.",
                "why_need_it_hi": "Real software alag-alag situations me alag rasta leta hai — jaise agar balance hai to cash do, warna 'Insufficient Balance' bolo.",
                "how_to_use_en": "Code runs sequentially until an 'if' evaluates a condition to True or False.",
                "how_to_use_hi": "Lines sequentially chalti hain jab tak if condition diversion na bana de.",
                "syntax": "# Linear Flow:\nprint(\"Step 1\")\nprint(\"Step 2\")\nprint(\"Step 3\")",
                "rules_en": [
                    "Python never skips a line unless commanded by control flow (if/else/return/break).",
                    "A crash on line 5 halts the program immediately — lines 6+ never execute.",
                    "Variables must be declared before they are read lower down in the file."
                ],
                "rules_hi": [
                    "Python bina kisi control flow order ke koi line skip nahi karta.",
                    "Agar line 5 par crash hua to line 6 chalne ka sawaal hi nahi banta.",
                    "Variable ko pehle banana padta hai, tabhi neeche padha ja sakta hai."
                ],
                "analogy_en": "Like water flowing down a mountain stream: gravity pulls it straight down until it reaches a dam or fork in the river.",
                "analogy_hi": "Pahad se behti hui nadi jaisi — seedhe neeche behti hai jab tak aage do nahar me baantne wala baandh na aa jaye.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to read a variable before it is assigned in the file order.",
                        "why_it_fails_en": "NameError: name 'x' is not defined. Python hasn't reached the assignment line yet.",
                        "why_it_fails_hi": "Neeche banaya aur upar use kar liya to Python crash ho jayega.",
                        "fix": "Always place variable definitions above the lines that consume them."
                    }
                ],
                "example_1": {
                    "title": "Strict Sequential Execution",
                    "title_hi": "Line by line chalna",
                    "code": "print('1. Engine Started')\nprint('2. Fuel Checked')\nprint('3. Takeoff Cleared')",
                    "expected_output": "1. Engine Started\n2. Fuel Checked\n3. Takeoff Cleared",
                    "explanation_en": "Demonstrates the guaranteed sequential execution order.",
                    "explanation_hi": "Guaranteed top-to-bottom sequence dikhata hai."
                },
                "example_2": {
                    "title": "Variable State Mutation in Sequence",
                    "title_hi": "Flow me variable badalna",
                    "code": "status = 'Pending'\nprint('Initial:', status)\nstatus = 'Approved'\nprint('Updated:', status)",
                    "expected_output": "Initial: Pending\nUpdated: Approved",
                    "explanation_en": "Shows how the state of a variable evolves line-by-line.",
                    "explanation_hi": "Dikhata hai ki variable ka state flow ke sath kaise badalta hai."
                },
                "challenge": {
                    "prompt_en": "Print three sequential steps: Step A, then Step B, then Step C on three separate lines.",
                    "prompt_hi": "Teen steps alag-alag lines par print karo: Step A, Step B, Step C.",
                    "starter_code": "# Print steps A, B, and C in order:\n",
                    "expected_output": "Step A\nStep B\nStep C",
                    "solution_code": "print('Step A')\nprint('Step B')\nprint('Step C')",
                    "solution_explanation_en": "Three sequential print statements execute top to bottom.",
                    "solution_explanation_hi": "Teen prints sequentially chalte hain.",
                    "hints": ["print('Step A')\\nprint('Step B')\\nprint('Step C')"],
                    "ego_roast_hi": "3 print line likhna bhool gaye?",
                    "ego_cheer_hi": "Sequential execution verified! ⬇️"
                }
            },
            {
                "id": "ch6_sub2_if_statement",
                "title": "Making a choice: The if statement",
                "title_hi": "Faisla lena: The if statement",
                "icon": "❓",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The 'if' statement tests a boolean condition. If the condition is True, Python executes the indented block of code underneath. If False, Python skips the indented block completely.",
                "what_is_it_hi": "'if' statement condition check karta hai. Agar condition True hai to andar ghus kar indented code chalata hai. Agar False hai to us pure block ko skip kar deta hai.",
                "why_need_it_en": "Software needs brains: If speed > limit, trigger camera; if battery < 10%, show low power warning.",
                "why_need_it_hi": "Bina if ke computer dimaag use nahi kar sakta: Agar battery < 10% hai to warning dikhao.",
                "how_to_use_en": "if condition: followed by an indented block (4 spaces). Note the MANDATORY colon (:).",
                "how_to_use_hi": "if condition: ke baad agli line me 4 spaces aage badha kar code likho. Colon (:) lagana mandatory hai.",
                "syntax": "if condition:\n    # Indented code block runs only if condition is True\n    do_something()",
                "rules_en": [
                    "A colon (:) is MANDATORY at the end of the if line.",
                    "The body of the if MUST be indented (standard is 4 spaces).",
                    "Non-zero numbers, non-empty strings and lists evaluate as truthy in if conditions."
                ],
                "rules_hi": [
                    "if line ke aakhri me colon (:) lagana mandatory hai.",
                    "if ke andar ka code 4 spaces indent hona zaroori hai.",
                    "Khali text ('') ya 0 False maane jaate hain, baaki sab True."
                ],
                "analogy_en": "A security bouncer at a club door: 'If you have a VIP badge, you may enter; otherwise, stay outside.'",
                "analogy_hi": "Club ke bouncer jaisa: 'Agar entry pass hai to andar jao; nahi hai to aage badho.'",
                "common_mistakes": [
                    {
                        "mistake": "Forgetting the colon at the end of the if statement: if age >= 18",
                        "why_it_fails_en": "SyntaxError: expected ':' at the end of line.",
                        "why_it_fails_hi": "Python me colon bhoolte hi syntax error aa jata hai.",
                        "fix": "Always place a colon at the end: if age >= 18:"
                    }
                ],
                "example_1": {
                    "title": "Basic If Gate",
                    "title_hi": "Simple if statement",
                    "code": "temperature = 35\nif temperature > 30:\n    print('Heat alert: Stay hydrated!')\nprint('Weather check complete.')",
                    "expected_output": "Heat alert: Stay hydrated!\nWeather check complete.",
                    "explanation_en": "Since 35 > 30 is True, the alert runs. The final unindented line runs regardless.",
                    "explanation_hi": "35 > 30 True hai to alert print hua. Aakhri line bina indent wali hamesha chalti hai."
                },
                "example_2": {
                    "title": "Skipped Block When False",
                    "title_hi": "Condition False hone par skip hona",
                    "code": "logged_in = False\nif logged_in:\n    print('Welcome to your secret vault!')\nprint('System standing by.')",
                    "expected_output": "System standing by.",
                    "explanation_en": "Since logged_in is False, the indented vault message is skipped completely.",
                    "explanation_hi": "logged_in False hone ki wajah se indented block poora skip ho gaya."
                },
                "challenge": {
                    "prompt_en": "Set score = 90. If score >= 80, print: Honors Student",
                    "prompt_hi": "score = 90 rakho. Agar score >= 80 hai to print karo: Honors Student",
                    "starter_code": "score = 90\n# Write your if block:\n",
                    "expected_output": "Honors Student",
                    "solution_code": "score = 90\nif score >= 80:\n    print('Honors Student')",
                    "solution_explanation_en": "Checks score >= 80 and executes the indented print statement.",
                    "solution_explanation_hi": "score >= 80 check karke indented print chalata hai.",
                    "hints": ["if score >= 80:\\n    print('Honors Student')"],
                    "ego_roast_hi": "Colon (:) lagana bhool gaye kya?",
                    "ego_cheer_hi": "If gate unlocked! 🎯"
                }
            },
            {
                "id": "ch6_sub3_else_statement",
                "title": "Providing an alternative: The else statement",
                "title_hi": "Alternative dena: The else statement",
                "icon": "↔️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The 'else' block provides the alternative backup branch. It executes ONLY when the 'if' condition evaluates to False.",
                "what_is_it_hi": "'else' wo backup rasta hai jo tab chalta hai jab 'if' wali condition fail (False) ho jaati hai.",
                "why_need_it_en": "Programs need fallback plans: If card has money -> approve transaction; ELSE -> decline transaction.",
                "why_need_it_hi": "Fallback zaroori hota hai: Agar balance hai to payment karo, ELSE decline karo.",
                "how_to_use_en": "else: followed by colon and indented code. An else block NEVER takes its own condition.",
                "how_to_use_hi": "else: likho colon ke sath. Yaad rakho: else ke aage koi condition nahi lagti!",
                "syntax": "if condition:\n    do_when_true()\nelse:\n    do_when_false()",
                "rules_en": [
                    "An else statement cannot exist on its own; it must follow an if (or elif).",
                    "else NEVER has a condition (writing 'else x > 5:' is a SyntaxError).",
                    "Exactly one of the two blocks will execute — never both, never neither."
                ],
                "rules_hi": [
                    "else akele nahi aa sakta, uske pehle if hona zaroori hai.",
                    "else ke aage koi condition nahi likhte ('else x > 5' galat hai).",
                    "Dono me se koi EK hi block chalega — ya to if ya fir else."
                ],
                "analogy_en": "A coin flip: If heads, Team A bats; else (it's tails), Team B bats.",
                "analogy_hi": "Cricket match ka toss: Agar heads aya to batting, else bowling.",
                "common_mistakes": [
                    {
                        "mistake": "Adding a condition to else: else age < 18:",
                        "why_it_fails_en": "SyntaxError: invalid syntax. else is the catch-all; it takes no condition.",
                        "why_it_fails_hi": "else ke aage condition lagane par syntax error aayega. Condition ke liye 'elif' use hota hai.",
                        "fix": "Use elif if you have a condition, or just 'else:'."
                    }
                ],
                "example_1": {
                    "title": "Pass / Fail Decision Tree",
                    "title_hi": "Pass ya Fail ka faisla",
                    "code": "marks = 32\nif marks >= 40:\n    print('Status: Passed')\nelse:\n    print('Status: Needs Improvement')",
                    "expected_output": "Status: Needs Improvement",
                    "explanation_en": "Since 32 >= 40 is False, the if block is skipped and the else block executes.",
                    "explanation_hi": "32 >= 40 False hua to else block chal gaya."
                },
                "example_2": {
                    "title": "Even / Odd Number Classifier",
                    "title_hi": "Even ya Odd number check",
                    "code": "num = 7\nif num % 2 == 0:\n    print(f'{num} is Even')\nelse:\n    print(f'{num} is Odd')",
                    "expected_output": "7 is Odd",
                    "explanation_en": "7 % 2 is 1 (not 0), so the else block correctly identifies 7 as Odd.",
                    "explanation_hi": "7 % 2 remainder 1 deta hai to else block 7 ko Odd bata deta hai."
                },
                "challenge": {
                    "prompt_en": "Set battery = 15. If battery > 20, print: Battery OK; else print: Low Battery Warning",
                    "prompt_hi": "battery = 15 rakho. Agar battery > 20 hai to print karo 'Battery OK', warna print karo: Low Battery Warning",
                    "starter_code": "battery = 15\n# Write if-else block:\n",
                    "expected_output": "Low Battery Warning",
                    "solution_code": "battery = 15\nif battery > 20:\n    print('Battery OK')\nelse:\n    print('Low Battery Warning')",
                    "solution_explanation_en": "Since 15 > 20 is False, the else block executes.",
                    "solution_explanation_hi": "15 > 20 False hone par else block chalta hai.",
                    "hints": ["if battery > 20:\\n    ...\\nelse:\\n    ..."],
                    "ego_roast_hi": "else block likhna itna mushkil lag raha hai?",
                    "ego_cheer_hi": "Binary branching master! ↔️"
                }
            },
            {
                "id": "ch6_sub4_elif_statement",
                "title": "Multiple choices: The elif statement",
                "title_hi": "Multiple choices: The elif statement",
                "icon": "🪜",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "'elif' stands for 'else if'. It lets you test multiple mutually exclusive conditions in sequence. Python checks from top to bottom and runs ONLY the first condition that evaluates to True, skipping all remaining ones.",
                "what_is_it_hi": "'elif' ka matlab hota hai 'else if'. Jab 2 se zyada choices hon (jaise Grade A, B, C, D ya Fail), tab elif use hota hai. Python upar se check karta hai aur jaise hi pehla True milta hai, use chala kar baaki sab skip kar deta hai.",
                "why_need_it_en": "Real life has multi-tiered rules: grading scales (90+ A, 80+ B, 70+ C), traffic lights (Red, Yellow, Green), or user roles (Admin, Moderator, Member, Guest).",
                "why_need_it_hi": "Grading scale, traffic signals (Red, Yellow, Green), user roles — in sabme 2 se zyada raste hote hain.",
                "how_to_use_en": "if condition1: ... elif condition2: ... elif condition3: ... else: ...",
                "how_to_use_hi": "if cond1: ... elif cond2: ... elif cond3: ... else: ...",
                "syntax": "if score >= 90:\n    grade = \"A\"\nelif score >= 80:\n    grade = \"B\"\nelif score >= 70:\n    grade = \"C\"\nelse:\n    grade = \"F\"",
                "rules_en": [
                    "You can chain as many elif blocks as you want (1 to 100+).",
                    "Order matters! Once one branch is satisfied, Python exits the entire if-elif chain.",
                    "The optional else at the end acts as the catch-all if none of the if/elif conditions match."
                ],
                "rules_hi": [
                    "Aap jitne chahe utne elif blocks laga sakte ho.",
                    "Order sabse zaroori hai! Pehla True milte hi baaki saare elif skip ho jaate hain.",
                    "Aakhri else catch-all hota hai agar koi bhi condition match na ho."
                ],
                "analogy_en": "A traffic signal: If Red, stop; elif Yellow, prepare; elif Green, go; else, signal is broken.",
                "analogy_hi": "Traffic light jaisa: Agar Red hai to ruko; elif Yellow hai to slow ho; elif Green hai to chalo; else signal kharab hai.",
                "common_mistakes": [
                    {
                        "mistake": "Wrong order in elif range checks: if score >= 60: D; elif score >= 90: A",
                        "why_it_fails_en": "A score of 95 will match the first check (>= 60) and get D! The >= 90 branch is never reached.",
                        "why_it_fails_hi": "Upar chhota number rakh diya to 95 wala student bhi D grade pa jayega!",
                        "fix": "Always order conditions from most restrictive to least restrictive (90 -> 80 -> 70)."
                    }
                ],
                "example_1": {
                    "title": "College Grading System",
                    "title_hi": "Marks se Grade nikaalna",
                    "code": "marks = 85\nif marks >= 90:\n    grade = 'A'\nelif marks >= 80:\n    grade = 'B'\nelif marks >= 70:\n    grade = 'C'\nelse:\n    grade = 'F'\nprint(f'Marks: {marks} -> Grade: {grade}')",
                    "expected_output": "Marks: 85 -> Grade: B",
                    "explanation_en": "85 is not >= 90, but matches >= 80, so grade 'B' is assigned and the rest skipped.",
                    "explanation_hi": "85 >= 90 False hua, lekin >= 80 True ho gaya to Grade B mil gaya."
                },
                "example_2": {
                    "title": "Traffic Light Decision System",
                    "title_hi": "Traffic signal state",
                    "code": "signal = 'Yellow'\nif signal == 'Red':\n    action = 'STOP'\nelif signal == 'Yellow':\n    action = 'SLOW DOWN'\nelif signal == 'Green':\n    action = 'GO'\nelse:\n    action = 'CAUTION'\nprint('Driver Action:', action)",
                    "expected_output": "Driver Action: SLOW DOWN",
                    "explanation_en": "Matches the Yellow condition and executes the corresponding action.",
                    "explanation_hi": "Yellow condition match hoke SLOW DOWN print karta hai."
                },
                "challenge": {
                    "prompt_en": "Set temp = 25. If temp > 30 print 'Hot', elif temp >= 20 print 'Pleasant', else print 'Cold'.",
                    "prompt_hi": "temp = 25 rakho. Agar temp > 30 print 'Hot', elif temp >= 20 print 'Pleasant', else print 'Cold'.",
                    "starter_code": "temp = 25\n# Write if-elif-else logic:\n",
                    "expected_output": "Pleasant",
                    "solution_code": "temp = 25\nif temp > 30:\n    print('Hot')\nelif temp >= 20:\n    print('Pleasant')\nelse:\n    print('Cold')",
                    "solution_explanation_en": "25 is not > 30, but is >= 20, so 'Pleasant' prints.",
                    "solution_explanation_hi": "25 >= 20 True hota hai to 'Pleasant' print hota hai.",
                    "hints": ["Check temp >= 20 in the elif block."],
                    "ego_roast_hi": "elif lagane me kya confusion hai?",
                    "ego_cheer_hi": "Multi-way branch conquered! 🪜"
                }
            },
            {
                "id": "ch6_sub5_indentation_rules",
                "title": "Indentation rules in Python (The most common beginner mistake)",
                "title_hi": "Python me Indentation ke niyam (Beginners ki sabse aam galti)",
                "icon": "📐",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "In C++, Java, and JavaScript, curly braces {} define code blocks. In Python, WHITESPACE INDENTATION defines code blocks! Standard indentation is strictly 4 spaces per nesting level.",
                "what_is_it_hi": "C++, Java aur JS me curly braces {} se block banta hai. Python me SPACES (indentation) se block banta hai! Standard rule hai: har level ke liye exact 4 spaces.",
                "why_need_it_en": "Indentation forces all Python developers worldwide to write uniformly formatted, clean, and beautiful code without debates over brace styles.",
                "why_need_it_hi": "Isse har Python coder ka code clean aur sundar dikhta hai, bina faltu curly braces ke.",
                "how_to_use_en": "Press the Tab key (configured in your editor as 4 spaces) after any line ending with a colon (:).",
                "how_to_use_hi": "Colon (:) ke baad Enter dabate hi editor apne aap 4 spaces aage kar deta hai.",
                "syntax": "if is_ready:\n    # 4 spaces indentation\n    statement_1\n    statement_2\n# Back to 0 spaces (outside block)\noutside_statement",
                "rules_en": [
                    "PEP 8 LAW: Use exactly 4 SPACES per indentation level (never mix Tabs and Spaces).",
                    "All statements inside the same block MUST align at the EXACT same indentation depth.",
                    "IndentationError: unexpected indent occurs if an unindented line has random spaces.",
                    "IndentationError: unindent does not match any outer indentation level occurs when misalignment happens."
                ],
                "rules_hi": [
                    "PEP 8 NIYAM: Hamesha exact 4 SPACES use karo (Tabs aur Spaces mix mat karo).",
                    "Ek block ke andar ki saari lines ek dum barabar seedh me honi chahiye.",
                    "Bina wajah aage space dene par IndentationError aayega."
                ],
                "analogy_en": "Indentation is like an outline or bullet-point hierarchy in a book: sub-points are pushed in under the main heading.",
                "analogy_hi": "Kitaab ke bullet points jaisa: main heading bahar hoti hai, aur uske sub-points thoda andar ki taraf push kiye hote hain.",
                "common_mistakes": [
                    {
                        "mistake": "Mixing Tabs and Spaces in the same file.",
                        "why_it_fails_en": "TabError: inconsistent use of tabs and spaces in indentation.",
                        "why_it_fails_hi": "Ek line me tab dabaya aur doosri me spaces diye to Python TabError phek dega.",
                        "fix": "Configure your editor to 'Convert Tabs to Spaces'."
                    }
                ],
                "example_1": {
                    "title": "Clean 4-Space Indented Block",
                    "title_hi": "Sahi Indentation Alignment",
                    "code": "status = 'ready'\nif status == 'ready':\n    print('Step 1: Aligned')\n    print('Step 2: Aligned')\nprint('Step 3: Outside block')",
                    "expected_output": "Step 1: Aligned\nStep 2: Aligned\nStep 3: Outside block",
                    "explanation_en": "Steps 1 and 2 are inside the if block; Step 3 is outside.",
                    "explanation_hi": "Steps 1 aur 2 if ke andar hain; Step 3 bahar hai."
                },
                "example_2": {
                    "title": "Multi-Level Indentation",
                    "title_hi": "Nested blocks ki indentation (4 spaces fir 8 spaces)",
                    "code": "logged_in = True\nis_admin = True\nif logged_in:\n    print('Level 1: Logged in (4 spaces)')\n    if is_admin:\n        print('Level 2: Admin Verified (8 spaces)')",
                    "expected_output": "Level 1: Logged in (4 spaces)\nLevel 2: Admin Verified (8 spaces)",
                    "explanation_en": "Shows progression from 4 spaces to 8 spaces in nested blocks.",
                    "explanation_hi": "Pehle block me 4 spaces aur uske andar wale block me 8 spaces."
                },
                "challenge": {
                    "prompt_en": "Fix indentation: Set verified = True. Inside if verified:, print 'Access Approved' then 'Welcome User'.",
                    "prompt_hi": "Indentation sahi karke verified = True ke andar 'Access Approved' aur 'Welcome User' print karo.",
                    "starter_code": "verified = True\nif verified:\n    print('Access Approved')\n    print('Welcome User')",
                    "expected_output": "Access Approved\nWelcome User",
                    "solution_code": "verified = True\nif verified:\n    print('Access Approved')\n    print('Welcome User')",
                    "solution_explanation_en": "Both print statements align perfectly at 4 spaces.",
                    "solution_explanation_hi": "Dono prints 4 spaces par barabar align hain.",
                    "hints": ["Ensure 4 spaces on both lines inside the if block."],
                    "ego_roast_hi": "Spaces ginna nahi aata kya?",
                    "ego_cheer_hi": "Indentation perfection achieved! 📐"
                }
            },
            {
                "id": "ch6_sub6_nested_if",
                "title": "Nested if statements (Conditions inside conditions)",
                "title_hi": "Nested if statements (Conditions ke andar conditions)",
                "icon": "📦",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A nested if statement is an 'if' placed inside the indented body of another 'if'. The inner condition is evaluated ONLY if the outer condition has already passed.",
                "what_is_it_hi": "Nested if ka matlab hota hai ek 'if' ke pet ke andar doosra 'if'. Andar wala if tabhi check hota hai jab bahar wala if pehle se True ho chuka ho.",
                "why_need_it_en": "Hierarchical screening: 1. Is user logged in? -> 2. Does user have premium subscription? -> 3. Is video in 4K resolution?",
                "why_need_it_hi": "Step-by-step checks: 1. Kya account active hai? -> 2. Kya ATM PIN sahi hai? -> 3. Kya account me paise hain?",
                "how_to_use_en": "Indent by 4 spaces for the outer block, and by 8 spaces for the inner block.",
                "how_to_use_hi": "Bahar wale ke liye 4 spaces aur andar wale if ke liye 8 spaces aage badho.",
                "syntax": "if outer_condition:\n    # 4 spaces\n    if inner_condition:\n        # 8 spaces\n        do_nested_action()",
                "rules_en": [
                    "Inner conditions only run if the parent condition evaluated to True.",
                    "Each nesting level adds 4 more spaces of indentation (4 -> 8 -> 12).",
                    "Do not nest deeper than 3 levels (refactor using logical 'and' or functions to keep code readable)."
                ],
                "rules_hi": [
                    "Andar wala condition tabhi chalega jab parent True ho.",
                    "Har level par 4 spaces aur add ho jaate hain (4 -> 8 -> 12).",
                    "3 level se zyada gehra nested if mat banao, 'and' operator use karo."
                ],
                "analogy_en": "Passing through airport security: Gate 1 checks your ticket. ONLY if Gate 1 clears do you reach Gate 2 for luggage scanning.",
                "analogy_hi": "Airport checking: Gate 1 par ticket dikhaya (Outer If). Ticket sahi hone par hi Gate 2 par luggage scan hota hai (Inner If).",
                "common_mistakes": [
                    {
                        "mistake": "Over-nesting when a simple 'and' operator would be 10x cleaner.",
                        "why_it_fails_en": "Creates the dreaded 'Arrow Anti-Pattern' where code drifts far to the right.",
                        "why_it_fails_hi": "Code itna right shift ho jata hai ki padhna mushkil ho jata hai.",
                        "fix": "Flatten with logical and: if a and b:"
                    }
                ],
                "example_1": {
                    "title": "ATM Withdrawal Nested Check",
                    "title_hi": "ATM transaction ka nested check",
                    "code": "card_valid = True\npin_correct = True\nbalance = 500\n\nif card_valid:\n    if pin_correct:\n        print('PIN Verified: Access granted.')\n    else:\n        print('Wrong PIN!')\nelse:\n    print('Invalid Card!')",
                    "expected_output": "PIN Verified: Access granted.",
                    "explanation_en": "Both outer card check and inner PIN check evaluate to True.",
                    "explanation_hi": "Card check aur PIN check dono True pass hote hain."
                },
                "example_2": {
                    "title": "Nested Age and License Verification",
                    "title_hi": "Driving license verification",
                    "code": "age = 19\nhas_license = False\nif age >= 18:\n    if has_license:\n        print('Permitted to drive.')\n    else:\n        print('Adult, but license is missing.')",
                    "expected_output": "Adult, but license is missing.",
                    "explanation_en": "Passes the outer age gate, but fails the inner license check.",
                    "explanation_hi": "Age 18 pass hui lekin license na hone par inner else chala."
                },
                "challenge": {
                    "prompt_en": "Write nested if: is_member = True, balance = 100. If is_member: if balance >= 50: print('Purchase Approved')",
                    "prompt_hi": "Nested if likho: is_member = True aur balance = 100. Agar is_member aur balance >= 50 to print karo: Purchase Approved",
                    "starter_code": "is_member = True\nbalance = 100\n# Write nested if:\n",
                    "expected_output": "Purchase Approved",
                    "solution_code": "is_member = True\nbalance = 100\nif is_member:\n    if balance >= 50:\n        print('Purchase Approved')",
                    "solution_explanation_en": "Outer condition is_member is True; inner condition balance >= 50 is True, printing the approved message.",
                    "solution_explanation_hi": "Dono checks pass hoke message print karte hain.",
                    "hints": ["Indent the inner if by 4 spaces and its print by 8 spaces."],
                    "ego_roast_hi": "Nested if ki spacing galat kar di kya?",
                    "ego_cheer_hi": "Nested matrix decision unlocked! 📦"
                }
            },
            {
                "id": "ch6_sub7_mini_project_adventure_game",
                "title": "Mini-Project: A Choose-Your-Own-Adventure Text Game",
                "title_hi": "Mini-Project: Choose-Your-Own-Adventure Text Game",
                "icon": "🏰",
                "is_mini_project": True,
                "duration": "15 mins",
                "xp": 150,
                "what_is_it_en": "An interactive, branching RPG story game where the player makes life-or-death choices (left path vs right path, fight vs sneak). The storyline forks dynamically using nested if, elif, and else logic.",
                "what_is_it_hi": "Ek interactive RPG text game jisme player rasta chunta hai (left ya right, fight ya sneak). Story player ke decisions ke hisab se nested if, elif aur else se alag-alag branches par jaati hai.",
                "why_need_it_en": "It teaches complex branching decision trees, state validation, and fallback error handling in a fun, game-design context.",
                "why_need_it_hi": "Game design se conditionals, state management aur branching logic ka practical use samajh aata hai.",
                "how_to_use_en": "Evaluate player input choices with if/elif/else to trigger unique storylines and endings.",
                "how_to_use_hi": "Player ke choice variable ko if/elif/else se evaluate karke alag story endings dikhao.",
                "syntax": "# Branching Storyline Architecture:\nchoice1 = \"left\"\nif choice1 == \"left\":\n    # Cave storyline\n    choice2 = \"open\"\n    if choice2 == \"open\":\n        print(\"Treasure Found!\")\nelse:\n    # Forest storyline\n    print(\"Lost in forest!\")",
                "rules_en": [
                    "Handle case sensitivity using .lower() on choices.",
                    "Every branch must have clear narrative feedback.",
                    "Include fallback 'else' blocks for invalid moves."
                ],
                "rules_hi": [
                    "Choice text ko .lower() se compare karo taaki case ka issue na ho.",
                    "Har raste par player ko clear kahani sunao.",
                    "Galat input ke liye fallback else block zaroor rakho."
                ],
                "analogy_en": "A choose-your-own-adventure book where page 10 says: 'If you want to enter the castle, turn to page 25; if you want to swim across the moat, turn to page 40.'",
                "analogy_hi": "Bachpan ki comic book jaisi — 'Agar gufa me jaana hai to page 12 par jao, agar pahad chadhna hai to page 20 par jao.'",
                "common_mistakes": [
                    {
                        "mistake": "Forgetting else blocks for unexpected user choices.",
                        "why_it_fails_en": "If player types 'jump' instead of 'left', the game silently dies with no output.",
                        "why_it_fails_hi": "Agar user ne galat choice daal di to game bina kuch bole khatam ho jayegi.",
                        "fix": "Always provide an else: print('Invalid choice! You trip and stumble.')"
                    }
                ],
                "example_1": {
                    "title": "Complete Adventure Game Engine",
                    "title_hi": "Adventure Game ka complete engine",
                    "code": "# =========================================\n# MINI-PROJECT: DUNGEON OF ELYSIA\n# =========================================\npath = 'left'\naction = 'open'\n\nprint('🏰 You stand at the entrance of the Dungeon.')\nif path == 'left':\n    print('You walked into the Vault.')\n    if action == 'open':\n        print('🏆 VICTORY: You found the Golden Chalice!')\n    else:\n        print('You walked past the chest and found nothing.')\nelif path == 'right':\n    print('🐉 DANGER: A sleeping dragon blocks your path!')\nelse:\n    print('You hesitated and turned back home.')",
                    "expected_output": "🏰 You stand at the entrance of the Dungeon.\nYou walked into the Vault.\n🏆 VICTORY: You found the Golden Chalice!",
                    "explanation_en": "Path 'left' enters the vault branch; action 'open' triggers the victory branch.",
                    "explanation_hi": "Path 'left' hone par vault khula aur action 'open' hone par victory message aya."
                },
                "example_2": {
                    "title": "Alternative Dragon Path",
                    "title_hi": "Dragon wala alternative path",
                    "code": "path = 'right'\nif path == 'left':\n    print('Safe passage.')\nelif path == 'right':\n    print('🐉 A dragon breathes fire! Game Over.')\nelse:\n    print('Unknown path.')",
                    "expected_output": "🐉 A dragon breathes fire! Game Over.",
                    "explanation_en": "Takes the alternative dragon branch cleanly.",
                    "explanation_hi": "Dragon wale alternative raste ko run karta hai."
                },
                "challenge": {
                    "prompt_en": "Build a mini adventure game: choice = 'left'. If choice == 'left' print 'Treasure Room'; elif choice == 'right' print 'Dragon Pit'; else print 'Lost'",
                    "prompt_hi": "choice = 'left' rakho. Agar 'left' hai to print karo 'Treasure Room'; elif 'right' hai to print karo 'Dragon Pit'; else print karo 'Lost'",
                    "starter_code": "choice = 'left'\n# Build adventure branch:\n",
                    "expected_output": "Treasure Room",
                    "solution_code": "choice = 'left'\nif choice == 'left':\n    print('Treasure Room')\nelif choice == 'right':\n    print('Dragon Pit')\nelse:\n    print('Lost')",
                    "solution_explanation_en": "choice == 'left' evaluates to True, printing 'Treasure Room'.",
                    "solution_explanation_hi": "choice == 'left' match hoke 'Treasure Room' print karta hai.",
                    "hints": ["if choice == 'left':\\n    print('Treasure Room')"],
                    "ego_roast_hi": "Adventure game me rasta bhool gaye?",
                    "ego_cheer_hi": "BOOM! 💥 MINI-PROJECT 2 COMPLETED! You built a branching RPG game! 🏆"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 7: Doing Things Over and Over (Loops)
    # =========================================================================
    {
        "id": "ch7_loops",
        "part_number": 2,
        "part_title": "PART 2: MAKING DECISIONS AND REPEATING ACTIONS",
        "chapter_number": 7,
        "title": "Chapter 7: Doing Things Over and Over (Loops)",
        "subtitle_en": "While loops, for loops, avoiding infinite loops, range(), break, continue, pass, nested loops, and a password guesser game",
        "subtitle_hi": "While loop, for loop, infinite loops se bachna, range(), break, continue, pass, nested loops aur password game",
        "icon": "🔁",
        "estimated_time": "45 mins",
        "prerequisites_en": "Chapters 1 to 6 (Variables, comparisons, and if-else control flow).",
        "prerequisites_hi": "Chapter 1 se 6 tak (Variables, comparisons aur if-else).",
        "learning_objectives_en": [
            "Understand why loops are the core of computing automation",
            "Master while loops and how to prevent infinite freezes",
            "Master for loops and range(start, stop, step)",
            "Control loops precisely with break and continue",
            "Use pass as syntactic placeholder",
            "Construct nested 2D loops",
            "Build Mini-Project: A Password Guesser Game"
        ],
        "learning_objectives_hi": [
            "Loops automation ki jaan kyun hain samjho",
            "While loop seekho aur infinite loop se bachna",
            "For loop aur range(start, stop, step) master karo",
            "break aur continue se loops ko control karna",
            "pass statement ka sahi use",
            "Nested loops (loops ke andar loops) banana",
            "Mini-Project: Password Guesser Game complete karna"
        ],
        "recap_en": "You mastered repetition in Python: while loops, avoiding runaway infinite loops, for-in iteration, range sequence generation, break/continue interrupts, pass placeholders, nested matrices, and built a password guesser game.",
        "recap_hi": "Aapne while loop, for loop, range(), break/continue, nested loops aur apna password guesser game banaya.",
        "subtopics": [
            {
                "id": "ch7_sub1_what_is_a_loop",
                "title": "What is a loop and why do we need them?",
                "title_hi": "Loop kya hota hai aur iski zaroorat kyun hai?",
                "icon": "🔄",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A loop is a control structure that repeats a block of code multiple times automatically until a stopping condition is reached.",
                "what_is_it_hi": "Loop ek aisi programming superpower hai jo kisi bhi code block ko baar baar repeat karti hai jab tak rukne ki condition na aa jaye.",
                "why_need_it_en": "Without loops, printing 1,000 invoices would require copy-pasting 1,000 print lines! A loop does it in 2 lines.",
                "why_need_it_hi": "Bina loop ke 1000 baar student ka naam print karne ke liye 1000 lines likhni padti. Loop sirf 2 lines me wahi kaam kar deta hai.",
                "how_to_use_en": "Use a 'for' loop when you know the collection or count. Use a 'while' loop when repeating until an unknown event occurs.",
                "how_to_use_hi": "Ginti pata ho to 'for' loop lagao. Kisi condition ke khatam hone tak chalana ho to 'while' loop lagao.",
                "syntax": "# Without loop: 5 lines of tedious repetition\n# With loop: 2 elegant lines\nfor i in range(5):\n    print(\"Automated iteration\", i)",
                "rules_en": [
                    "DRY Principle: Don't Repeat Yourself — if you copy-paste code 3 times, you need a loop.",
                    "Loops drastically reduce code size and bug surface area.",
                    "Every loop must have a clear mechanism to eventually terminate."
                ],
                "rules_hi": [
                    "DRY Niyam: Don't Repeat Yourself — agar same code baar baar copy-paste kar rahe ho to loop lagao.",
                    "Loops se code chhota aur bugs kam hote hain.",
                    "Har loop me band hone ka rasta hona mandatory hai."
                ],
                "analogy_en": "A Ferris wheel or clock hand: it rotates repeatedly, ticking through every minute until time runs out.",
                "analogy_hi": "Ghadhi ki sui jaisi — ghoomti rehti hai lagataar, har second ko repeat karti hai.",
                "common_mistakes": [
                    {
                        "mistake": "Copy-pasting identical print lines 10 times instead of using a loop.",
                        "why_it_fails_en": "Brittle, amateur code that cannot adapt dynamically when count changes.",
                        "why_it_fails_hi": "10 baar copy-paste karne se code ganda ho jata hai aur edit karna mushkil hota hai.",
                        "fix": "Use a loop: for _ in range(10): print('Hello')."
                    }
                ],
                "example_1": {
                    "title": "Repetition Made Effortless",
                    "title_hi": "Bina copy-paste ke 3 baar print",
                    "code": "for i in range(3):\n    print(f'Repetition #{i + 1}')",
                    "expected_output": "Repetition #1\nRepetition #2\nRepetition #3",
                    "explanation_en": "Executes the print statement 3 times without duplicating code.",
                    "explanation_hi": "Bina code copy kiye 3 baar print karta hai."
                },
                "example_2": {
                    "title": "Iterating Over String Letters",
                    "title_hi": "Text ke har letter par loop",
                    "code": "word = 'AI'\nfor char in word:\n    print('Character:', char)",
                    "expected_output": "Character: A\nCharacter: I",
                    "explanation_en": "Steps through each individual character of the string.",
                    "explanation_hi": "String ke ek-ek letter par chal kar use print karta hai."
                },
                "challenge": {
                    "prompt_en": "Run a loop 3 times printing: Loop active",
                    "prompt_hi": "3 baar loop chala kar print karo: Loop active",
                    "starter_code": "# Run a loop 3 times:\n",
                    "expected_output": "Loop active\nLoop active\nLoop active",
                    "solution_code": "for _ in range(3):\n    print('Loop active')",
                    "solution_explanation_en": "Runs range(3) and outputs 'Loop active' three times.",
                    "solution_explanation_hi": "range(3) se 3 baar print hota hai.",
                    "hints": ["for _ in range(3):\\n    print('Loop active')"],
                    "ego_roast_hi": "3 baar loop chalana bhool gaye?",
                    "ego_cheer_hi": "Repetition automation verified! 🔄"
                }
            },
            {
                "id": "ch7_sub2_while_loop",
                "title": "The while loop: Looping until a condition is false",
                "title_hi": "The while loop: Condition False hone tak chalna",
                "icon": "⏳",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A 'while' loop continues executing its indented body as long as its condition remains True. Before every single turn, Python re-checks the condition: if True, it runs again; if False, the loop ends.",
                "what_is_it_hi": "while loop tab tak chalta rehta hai jab tak uski condition True bani rehti hai. Har turn se pehle Python condition dobara check karta hai. Jaise hi False hua, loop ruk jata hai.",
                "why_need_it_en": "When you don't know in advance how many turns are needed: e.g. Keep playing while player has lives; keep asking while password is wrong.",
                "why_need_it_hi": "Jab pehle se pata na ho ki kitni baar chalana hai: jaise jab tak user galat password daalta rahe tab tak dobara poocho.",
                "how_to_use_en": "while condition: followed by indented body, and CRITICALLY: update the variable inside!",
                "how_to_use_hi": "while condition: ke andar code likho aur variable ko update zaroor karo (i += 1).",
                "syntax": "count = 1\nwhile count <= 5:\n    print(count)\n    count += 1  # Crucial update step!",
                "rules_en": [
                    "A while loop must have an initialization (before the loop), condition (in the while line), and update (inside the body).",
                    "If the condition is initially False, the body will run ZERO times.",
                    "Failing to update the condition variable causes an INFINITE LOOP."
                ],
                "rules_hi": [
                    "while loop me 3 cheezein zaroori hain: shuruat (start), condition (check), aur badlav (update: i += 1).",
                    "Agar condition shuru me hi False hai to loop 0 baar chalega.",
                    "Agar variable update nahi kiya to loop kabhi nahi rukega (infinite loop)."
                ],
                "analogy_en": "Drinking water from a glass: While the glass is not empty, take another sip. Once empty, stop.",
                "analogy_hi": "Chai peene jaisa: Jab tak cup me chai bachi hai (condition True), tab tak ghoont lo. Cup khali hote hi ruk jao.",
                "common_mistakes": [
                    {
                        "mistake": "Forgetting the counter increment (e.g. i += 1) inside while loop.",
                        "why_it_fails_en": "The condition stays permanently True, freezing your CPU in an infinite loop.",
                        "why_it_fails_hi": "i ki value wahi reh jaati hai aur computer freeze ho jata hai.",
                        "fix": "Always increment or modify the loop variable inside the body."
                    }
                ],
                "example_1": {
                    "title": "Counting from 1 to 3 with While",
                    "title_hi": "1 se 3 tak ginti while loop se",
                    "code": "num = 1\nwhile num <= 3:\n    print('Count:', num)\n    num += 1\nprint('Loop finished!')",
                    "expected_output": "Count: 1\nCount: 2\nCount: 3\nLoop finished!",
                    "explanation_en": "Increments num each turn until num = 4, which breaks the loop.",
                    "explanation_hi": "Har turn me num 1 badhta hai, 4 hote hi loop khatam."
                },
                "example_2": {
                    "title": "Rocket Countdown Timer",
                    "title_hi": "Rocket launch countdown",
                    "code": "countdown = 3\nwhile countdown > 0:\n    print(f'T-minus {countdown}...')\n    countdown -= 1\nprint('🚀 BLAST OFF!')",
                    "expected_output": "T-minus 3...\nT-minus 2...\nT-minus 1...\n🚀 BLAST OFF!",
                    "explanation_en": "Decrements from 3 to 1 before blastoff.",
                    "explanation_hi": "3 se 1 tak reverse ginti karta hai fir blastoff bolta hai."
                },
                "challenge": {
                    "prompt_en": "Use a while loop to print numbers 1 and 2, then print 'Done'.",
                    "prompt_hi": "while loop use karke 1 aur 2 print karo, fir 'Done' print karo.",
                    "starter_code": "i = 1\n# Write while loop:\n",
                    "expected_output": "1\n2\nDone",
                    "solution_code": "i = 1\nwhile i <= 2:\n    print(i)\n    i += 1\nprint('Done')",
                    "solution_explanation_en": "Prints 1 and 2, increments i, and exits.",
                    "solution_explanation_hi": "1 aur 2 print karke bahar aakar Done print karta hai.",
                    "hints": ["while i <= 2:\\n    print(i)\\n    i += 1"],
                    "ego_roast_hi": "i += 1 lagana bhool gaye?",
                    "ego_cheer_hi": "While loop condition verified! ⏳"
                }
            },
            {
                "id": "ch7_sub3_infinite_loops",
                "title": "Avoiding the dreaded \"Infinite Loop\"",
                "title_hi": "Khatarnaak \"Infinite Loop\" se bachna",
                "icon": "♾️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "An infinite loop occurs when a loop's stopping condition is NEVER reached, causing the program to repeat forever, maxing out CPU usage and freezing the application.",
                "what_is_it_hi": "Infinite loop wo bala hai jahan rukne ki condition kabhi aati hi nahi! Computer 100% CPU use karke ghoomta rehta hai aur screen freeze ho jaati hai.",
                "why_need_it_en": "Every beginner experiences an infinite loop. Understanding why they happen and how to terminate them with Ctrl+C or kill signals is essential.",
                "why_need_it_hi": "Har coder se shuruat me infinite loop banta hai. Isse bachna aur Ctrl+C se program rokna aana zaroori hai.",
                "how_to_use_en": "Ensure every while loop has a progression step towards False, or an explicit safety limit: if steps > 1000: break.",
                "how_to_use_hi": "Ensure karo ki variable badh raha hai, aur emergency break lagao agar limit cross ho.",
                "syntax": "# DANGEROUS INFINITE LOOP:\n# while True:\n#     print(\"Help, I cannot stop!\")\n\n# SAFE LOOP WITH GUARANTEED TERMINATION:\nsteps = 0\nwhile steps < 5:\n    steps += 1",
                "rules_en": [
                    "Never write 'while True:' without an explicit 'break' statement inside.",
                    "Pressing Ctrl+C in terminal sends KeyboardInterrupt to kill an infinite loop.",
                    "Always verify that your counter step actually moves closer to the exit condition."
                ],
                "rules_hi": [
                    "Bina 'break' ke 'while True:' kabhi mat likho.",
                    "Terminal me Ctrl+C dabane se infinite loop ruk jata hai (KeyboardInterrupt).",
                    "Hamesha check karo ki counter aage badh raha hai ya nahi."
                ],
                "analogy_en": "Being stuck on an infinite roundabout in a car where every exit is blocked with barricades.",
                "analogy_hi": "Gol-chakkar (roundabout) me phans jaane jaisa jahan koi bhi exit road khula hi na ho aur gaadi ghoomti rahe.",
                "common_mistakes": [
                    {
                        "mistake": "Decrementing instead of incrementing: i = 1; while i > 0: i += 1",
                        "why_it_fails_en": "i starts at 1 and increases forever (1, 2, 3...), so i > 0 is permanently True!",
                        "why_it_fails_hi": "i hamesha 0 se bada hi rahega to loop kabhi rukega hi nahi.",
                        "fix": "Ensure the comparison bounds match the direction of modification."
                    }
                ],
                "example_1": {
                    "title": "Safely Breaking an Infinite Pattern",
                    "title_hi": "Emergency break se safe loop",
                    "code": "turns = 0\nwhile True:\n    turns += 1\n    if turns >= 3:\n        print('Emergency exit triggered at turn:', turns)\n        break",
                    "expected_output": "Emergency exit triggered at turn: 3",
                    "explanation_en": "Uses an explicit break condition to guarantee termination.",
                    "explanation_hi": "break statement lagakar infinite loop ko 3 turn ke baad rok deta hai."
                },
                "example_2": {
                    "title": "Safety Counter Pattern",
                    "title_hi": "Safety counter pattern",
                    "code": "safety_cap = 5\ncount = 0\nwhile count < safety_cap:\n    count += 1\nprint('Safe exit reached. Total steps:', count)",
                    "expected_output": "Safe exit reached. Total steps: 5",
                    "explanation_en": "Strict safety cap ensures loop exits at count = 5.",
                    "explanation_hi": "Safety cap lagakar loop ko safe rakhta hai."
                },
                "challenge": {
                    "prompt_en": "Demonstrate a safe loop with a break: run while True, increment n = 0 by 1, if n == 2: break. Print: Stopped safely at 2",
                    "prompt_hi": "while True me n = 0 ko badhao, jab n == 2 ho to break karo aur print karo: Stopped safely at 2",
                    "starter_code": "n = 0\nwhile True:\n    n += 1\n    # Add break check:\n",
                    "expected_output": "Stopped safely at 2",
                    "solution_code": "n = 0\nwhile True:\n    n += 1\n    if n == 2:\n        break\nprint(f'Stopped safely at {n}')",
                    "solution_explanation_en": "Safely breaks the while True loop at n == 2.",
                    "solution_explanation_hi": "n == 2 hote hi break lag jata hai aur message print hota hai.",
                    "hints": ["if n == 2:\\n    break"],
                    "ego_roast_hi": "break statement lagana bhool gaye?",
                    "ego_cheer_hi": "Infinite loop disaster averted! ♾️"
                }
            },
            {
                "id": "ch7_sub4_for_loop",
                "title": "The for loop: Stepping through items",
                "title_hi": "The for loop: Items par ek-ek karke chalna",
                "icon": "🚶",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A 'for' loop in Python is a 'for-each' iterator. It steps sequentially through every element of an iterable collection (list, string, tuple, dictionary, range) from start to finish.",
                "what_is_it_hi": "Python ka for loop 'for-each' loop hota hai. Ye kisi bhi collection (list, string, dictionary) ke har ek item par ek-ek karke chalta hai jab tak aakhri item na aa jaye.",
                "why_need_it_en": "Processing lists of students, sending emails to customers, and transforming data points are all powered by for loops.",
                "why_need_it_hi": "Students ki list process karna, sabhi users ko notification bhejna — ye sab for loop se hota hai.",
                "how_to_use_en": "for item in collection: followed by indented body.",
                "how_to_use_hi": "for item in list: likho aur andar code likho.",
                "syntax": "for element in iterable_collection:\n    process(element)",
                "rules_en": [
                    "The loop variable ('item') is automatically updated to the next element on every turn.",
                    "A for loop terminates automatically when the collection has no more items (zero risk of infinite loop!).",
                    "The original collection is NOT modified by merely looping over it."
                ],
                "rules_hi": [
                    "Har turn par variable me agla item apne aap aa jata hai.",
                    "Saare items khatam hote hi loop automatically ruk jata hai (infinite loop ka zero risk!).",
                    "Sirf loop chalane se original list modify nahi hoti."
                ],
                "analogy_en": "A postal worker going down a street, putting a letter in mailbox #1, then #2, then #3, until reaching the end of the block.",
                "analogy_hi": "Postman jaisa jo har ghar ke letterbox me ek-ek chitthi daalta hua gali ke aakhri ghar tak jaata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Naming the loop variable the exact same name as the collection: for items in items:",
                        "why_it_fails_en": "Shadows the collection, causing confusion and bugs.",
                        "why_it_fails_hi": "List aur single item ka naam same rakhne se confusion ho jata hai.",
                        "fix": "Use plural for collection and singular for item: for item in items: or for student in students:"
                    }
                ],
                "example_1": {
                    "title": "Iterating Over a List of Strings",
                    "title_hi": "Names ki list par loop",
                    "code": "heroes = ['Ironman', 'Batman', 'Spiderman']\nfor hero in heroes:\n    print('Hero:', hero)",
                    "expected_output": "Hero: Ironman\nHero: Batman\nHero: Spiderman",
                    "explanation_en": "Loops over all 3 heroes in order.",
                    "explanation_hi": "Teeno heroes par sequentially loop chalaata hai."
                },
                "example_2": {
                    "title": "Summing Numbers with a For Loop",
                    "title_hi": "Numbers ka total jod nikaalna",
                    "code": "prices = [10, 20, 30]\ntotal = 0\nfor p in prices:\n    total += p\nprint('Total Bill:', total)",
                    "expected_output": "Total Bill: 60",
                    "explanation_en": "Accumulates the sum of all price elements in the list.",
                    "explanation_hi": "List ke sabhi numbers ko jodkar total 60 banata hai."
                },
                "challenge": {
                    "prompt_en": "Loop over ['Red', 'Green', 'Blue'] and print each with prefix 'Color: '.",
                    "prompt_hi": "['Red', 'Green', 'Blue'] par loop chala kar har ek ke aage 'Color: ' laga kar print karo.",
                    "starter_code": "colors = ['Red', 'Green', 'Blue']\n# Write for loop:\n",
                    "expected_output": "Color: Red\nColor: Green\nColor: Blue",
                    "solution_code": "colors = ['Red', 'Green', 'Blue']\nfor c in colors:\n    print(f'Color: {c}')",
                    "solution_explanation_en": "Iterates through each color and prints it with the prefix.",
                    "solution_explanation_hi": "Har color ko prefix ke sath print karta hai.",
                    "hints": ["for c in colors:\\n    print(f'Color: {c}')"],
                    "ego_roast_hi": "for loop likhna bhool gaye?",
                    "ego_cheer_hi": "Collection iteration master! 🚶"
                }
            },
            {
                "id": "ch7_sub5_range_function",
                "title": "Using the range() function to count",
                "title_hi": "Ginti gin-ne ke liye range() function",
                "icon": "🔢",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The range() function generates an immutable sequence of numbers on demand without storing them all in memory. It accepts up to three arguments: range(start, stop, step).",
                "what_is_it_hi": "range() function numbers ki sequence generate karta hai. Isme 3 arguments hote hain: range(start, stop, step). Sabse important rule: stop number HAMESHA EXCLUSIVE (chhoota hua) hota hai!",
                "why_need_it_en": "To run a loop an exact number of times (e.g. 100 times), or count by 2s (even numbers), or count backwards (10 down to 1).",
                "why_need_it_hi": "Kisi loop ko exact 10 baar chalana ho, ya table 2, 4, 6, 8 print karna ho, ya ulta 10 se 1 ginn-na ho — range() use hota hai.",
                "how_to_use_en": "range(5) -> 0 to 4. range(1, 6) -> 1 to 5. range(0, 10, 2) -> 0, 2, 4, 6, 8.",
                "how_to_use_hi": "range(5) deta hai 0 se 4 tak. range(1, 6) deta hai 1 se 5 tak. range(0, 10, 2) deta hai 0, 2, 4, 6, 8.",
                "syntax": "# 1 arg: stop (starts at 0)\nrange(5)          # 0, 1, 2, 3, 4\n# 2 args: start, stop\nrange(2, 6)       # 2, 3, 4, 5\n# 3 args: start, stop, step\nrange(1, 10, 2)   # 1, 3, 5, 7, 9 (odds)\nrange(5, 0, -1)   # 5, 4, 3, 2, 1 (countdown)",
                "rules_en": [
                    "CRITICAL LAW: The 'stop' parameter is EXCLUSIVE. range(1, 5) stops BEFORE 5 (generates 1, 2, 3, 4).",
                    "Default start is 0; default step is 1.",
                    "Negative step allows reverse counting: range(5, 0, -1)."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: stop number HAMESHA chhoot jata hai. range(1, 5) me 5 nahi aayega (sirf 1, 2, 3, 4).",
                    "Agar start nahi doge to 0 se shuru hoga, step default 1 hota hai.",
                    "Negative step (-1) se ulti ginti hoti hai."
                ],
                "analogy_en": "Like setting a stopwatch to beep at second 1, 2, 3, 4, and stop right as second 5 begins.",
                "analogy_hi": "Metro station ke platform jaisa — train 1 se 4 station rukti hai, 5ve par rukti nahi cross ho jaati hai.",
                "common_mistakes": [
                    {
                        "mistake": "Expecting range(1, 10) to include 10.",
                        "why_it_fails_en": "range stops strictly at stop - 1. It yields numbers up to 9 only.",
                        "why_it_fails_hi": "range(1, 10) sirf 9 tak jaata hai, 10 kabhi include nahi hota.",
                        "fix": "To include 10, set stop to 11: range(1, 11)."
                    }
                ],
                "example_1": {
                    "title": "Start, Stop, and Step in Range",
                    "title_hi": "2 ki table range(2, 11, 2) se",
                    "code": "print('Even numbers up to 10:')\nfor n in range(2, 11, 2):\n    print(n, end=' ')\nprint()",
                    "expected_output": "Even numbers up to 10:\n2 4 6 8 10 ",
                    "explanation_en": "Starts at 2, steps by 2, stops before 11, printing 2 4 6 8 10.",
                    "explanation_hi": "2 se shuru hoke 2 ke step se 10 tak print karta hai."
                },
                "example_2": {
                    "title": "Counting Down Backwards",
                    "title_hi": "Ulti ginti range(3, 0, -1)",
                    "code": "for count in range(3, 0, -1):\n    print(count, end=' ')\nprint('GO!')",
                    "expected_output": "3 2 1 GO!",
                    "explanation_en": "Negative step counts downwards: 3, 2, 1.",
                    "explanation_hi": "Negative step se ulti ginti hoti hai."
                },
                "challenge": {
                    "prompt_en": "Print numbers 1 to 3 separated by spaces using range(1, 4): 1 2 3",
                    "prompt_hi": "range(1, 4) use karke 1 2 3 ek line me print karo: 1 2 3",
                    "starter_code": "# Use for loop with range(1, 4):\n",
                    "expected_output": "1 2 3",
                    "solution_code": "for i in range(1, 4):\n    print(i, end=' ' if i < 3 else '')\nprint()",
                    "solution_explanation_en": "Prints 1 2 3 on a single line.",
                    "solution_explanation_hi": "range(1, 4) se 1 2 3 print karta hai.",
                    "hints": ["range(1, 4) gives 1, 2, 3."],
                    "ego_roast_hi": "range ka stop exclusive hota hai, bhool gaye?",
                    "ego_cheer_hi": "Range sequence master! 🔢"
                }
            },
            {
                "id": "ch7_sub6_break_and_continue",
                "title": "Controlling the loop: break (stopping early) and continue (skipping a turn)",
                "title_hi": "Loop control: break (jaldi rokna) aur continue (turn skip karna)",
                "icon": "🛑",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "'break' abruptly halts and terminates the loop completely, jumping to the code outside. 'continue' immediately skips the REST of the current iteration and jumps straight to the next turn of the loop.",
                "what_is_it_hi": "'break' loop ko turant poori tarah tod kar bahar nikaal deta hai. 'continue' sirf CURRENT turn ka bacha hua hissa chhod kar agli turn par jump kar jaata hai.",
                "why_need_it_en": "Search algorithms: once an item is found, 'break' prevents checking the remaining 10,000 items! Data filters: if item is corrupted, 'continue' skips to the next valid record.",
                "why_need_it_hi": "Agar 10,000 me se roll number mil gaya to 'break' baaki ke checks rokt hai. Agar koi data galat hai to 'continue' use skip karke agle data par jata hai.",
                "how_to_use_en": "Place inside an if statement within the loop: if item == target: break.",
                "how_to_use_hi": "Loop ke andar if lagao: if x == 3: continue.",
                "syntax": "# Break example:\nfor x in range(10):\n    if x == 5:\n        break  # Loop ends immediately\n\n# Continue example:\nfor x in range(5):\n    if x == 2:\n        continue  # Skips only 2\n    print(x)",
                "rules_en": [
                    "break exits the entire loop immediately.",
                    "continue skips the rest of the current turn and proceeds to the next iteration.",
                    "In nested loops, break only exits the INNERMOST loop enclosing it."
                ],
                "rules_hi": [
                    "break loop ko turant khatam kar deta hai.",
                    "continue sirf is turn ko skip karke agle round me jata hai.",
                    "Nested loop me break sirf usi loop ko todta hai jiske andar wo likha hai."
                ],
                "analogy_en": "'break' is pulling the emergency brake on a train (the entire journey stops). 'continue' is a speed-breaker bump: you slow down and skip one gear, but keep driving.",
                "analogy_hi": "'break' emergency brake jaisa hai (gaadi poori ruk gayi). 'continue' traffic jam me ek chhota pothole skip karne jaisa hai.",
                "common_mistakes": [
                    {
                        "mistake": "Confusing break and continue.",
                        "why_it_fails_en": "Using break when you intended continue kills the entire loop prematurely.",
                        "why_it_fails_hi": "continue ki jagah break lagane se loop beech me hi mar jata hai.",
                        "fix": "Remember: break = TERMINATE. continue = SKIP TO NEXT."
                    }
                ],
                "example_1": {
                    "title": "Search and Break Early",
                    "title_hi": "Milte hi break lagana",
                    "code": "names = ['Aman', 'Rohan', 'Sara', 'Pooja']\nfor n in names:\n    if n == 'Rohan':\n        print('Found Rohan! Stopping search.')\n        break\n    print('Checking:', n)",
                    "expected_output": "Checking: Aman\nFound Rohan! Stopping search.",
                    "explanation_en": "Stops immediately upon finding 'Rohan', never checking Sara or Pooja.",
                    "explanation_hi": "Rohan milte hi break lag gaya, aage ke naam check nahi hue."
                },
                "example_2": {
                    "title": "Skip Evens with Continue",
                    "title_hi": "Continue se even numbers skip karna",
                    "code": "for num in range(1, 6):\n    if num % 2 == 0:\n        continue  # Skip evens\n    print('Odd number:', num)",
                    "expected_output": "Odd number: 1\nOdd number: 3\nOdd number: 5",
                    "explanation_en": "continue skips the print statement when num is even.",
                    "explanation_hi": "Jab num even hota hai to continue agli turn par jump kar deta hai."
                },
                "challenge": {
                    "prompt_en": "Loop through range(1, 6). If number is 3, skip it using continue. Print the remaining numbers.",
                    "prompt_hi": "range(1, 6) par loop chalao. Agar number 3 ho to continue se skip karo. Baaki numbers print karo.",
                    "starter_code": "for i in range(1, 6):\n    # Skip 3 and print:\n",
                    "expected_output": "1\n2\n4\n5",
                    "solution_code": "for i in range(1, 6):\n    if i == 3:\n        continue\n    print(i)",
                    "solution_explanation_en": "Skips 3 and outputs 1, 2, 4, 5.",
                    "solution_explanation_hi": "3 ko skip karke 1, 2, 4, 5 print karta hai.",
                    "hints": ["if i == 3: continue"],
                    "ego_roast_hi": "continue lagana bhool gaye kya?",
                    "ego_cheer_hi": "Loop interception mastered! 🛑"
                }
            },
            {
                "id": "ch7_sub7_pass_statement",
                "title": "The pass statement (Placeholder code)",
                "title_hi": "The pass statement (Placeholder code)",
                "icon": "⏳",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The 'pass' statement is a null operation (no-op). When executed, absolutely nothing happens. It is used as a syntactic placeholder in loops, functions, and classes where Python grammar requires an indented statement but you aren't ready to write the logic yet.",
                "what_is_it_hi": "'pass' ka matlab hota hai 'kuch mat karo' (no-op). Jab aapko code ka structure banana ho lekin andar ki logic baad me likhni ho, to Python khali block allow nahi karta. Wahan 'pass' likhte hain.",
                "why_need_it_en": "In Python, leaving an empty block after a colon throws an IndentationError. 'pass' satisfies the compiler without doing anything.",
                "why_need_it_hi": "Python me colon ke baad agar khali chhod doge to IndentationError aayega. 'pass' likhne se error nahi aata.",
                "how_to_use_en": "def todo_later(): pass or if condition: pass.",
                "how_to_use_hi": "if condition: pass ya for i in range(10): pass.",
                "syntax": "if is_vip:\n    pass  # TODO: Implement VIP perks later\nelse:\n    print(\"Standard flow\")",
                "rules_en": [
                    "pass does nothing at runtime.",
                    "It prevents IndentationError: expected an indented block.",
                    "Commonly used when stubbing out new architectures or empty exception handlers."
                ],
                "rules_hi": [
                    "pass run hone par kuch nahi karta.",
                    "Ye expected indented block wale error se bachata hai.",
                    "New features ka blueprint banate waqt use hota hai."
                ],
                "analogy_en": "Like putting a 'Under Construction' yellow caution tape on a room door until the interior decorators arrive.",
                "analogy_hi": "Naye building par 'Kaam Chalu Hai' ka board lagane jaisa taaki koi andar na ghuse.",
                "common_mistakes": [
                    {
                        "mistake": "Leaving a function or if block completely blank: if True:",
                        "why_it_fails_en": "IndentationError: expected an indented block after 'if' statement.",
                        "why_it_fails_hi": "Colon ke baad khali chhodne par Python crash ho jata hai.",
                        "fix": "Add 'pass' inside the empty block."
                    }
                ],
                "example_1": {
                    "title": "Pass as Architectural Stub",
                    "title_hi": "Placeholder ke roop me pass",
                    "code": "for i in range(3):\n    if i == 1:\n        pass  # Will handle special case later\n    else:\n        print('Handled index:', i)",
                    "expected_output": "Handled index: 0\nHandled index: 2",
                    "explanation_en": "Index 1 executes pass without error; indices 0 and 2 print.",
                    "explanation_hi": "Index 1 par pass chal kar aage badh jata hai bina crash huye."
                },
                "example_2": {
                    "title": "Stubbing a Future Function",
                    "title_hi": "Future function ka blueprint",
                    "code": "def calculate_ai_prediction():\n    pass  # Coming in v2.0\n\nprint('Blueprint loaded cleanly without syntax errors.')",
                    "expected_output": "Blueprint loaded cleanly without syntax errors.",
                    "explanation_en": "pass allows empty function definitions to parse cleanly.",
                    "explanation_hi": "pass ki wajah se khali function bina syntax error ke load hota hai."
                },
                "challenge": {
                    "prompt_en": "Write an if True block with pass inside, then print: Pass executed successfully",
                    "prompt_hi": "if True: ke andar pass likho, fir print karo: Pass executed successfully",
                    "starter_code": "# Use pass inside if block:\n",
                    "expected_output": "Pass executed successfully",
                    "solution_code": "if True:\n    pass\nprint('Pass executed successfully')",
                    "solution_explanation_en": "pass satisfies indentation requirement.",
                    "solution_explanation_hi": "pass indentation error se bachata hai.",
                    "hints": ["if True:\\n    pass"],
                    "ego_roast_hi": "pass likhna bhi bhool gaye?",
                    "ego_cheer_hi": "No-op placeholder verified! ⏳"
                }
            },
            {
                "id": "ch7_sub8_nested_loops",
                "title": "Nested loops (Loops inside loops)",
                "title_hi": "Nested loops (Loops ke andar loops)",
                "icon": "🔄",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "A nested loop is a loop located inside the body of another loop. For every SINGLE turn of the outer loop, the inner loop runs through ALL of its turns from start to finish.",
                "what_is_it_hi": "Nested loop ka matlab hota hai loop ke andar ek aur loop. Bahar wale loop ke HAR EK turn ke liye andar wala loop APNE SAARE turns poore karta hai.",
                "why_need_it_en": "2D data structures: grids, chessboards (8x8), spreadsheets (rows and columns), image pixels (width x height), and multiplication tables.",
                "why_need_it_hi": "Chessboard (8x8), Excel rows aur columns, image ke pixels, math tables — in sabme rows aur columns ke liye do loops lagte hain.",
                "how_to_use_en": "for row in range(3): for col in range(3):",
                "how_to_use_hi": "for r in range(3): for c in range(3):",
                "syntax": "for row in range(3):\n    for col in range(3):\n        print(f\"({row}, {col})\", end=\" \")\n    print()  # New line after every row",
                "rules_en": [
                    "Total operations = (outer loop iterations) * (inner loop iterations). A 100 x 100 loop runs 10,000 times!",
                    "Inner loop must be indented 4 spaces further than the outer loop.",
                    "Be careful with variable naming: do not use the same counter name for both loops (e.g. use 'i' and 'j', or 'r' and 'c')."
                ],
                "rules_hi": [
                    "Total turns = outer * inner. 10 * 10 loop 100 baar chalega!",
                    "Andar wale loop ko 4 spaces aur aage indent karna padta hai.",
                    "Dono loop ke variable names alag hone chahiye (i aur j, ya r aur c)."
                ],
                "analogy_en": "A clock: the minute hand must complete 60 full turns for the hour hand to tick just ONCE.",
                "analogy_hi": "Ghadhi jaisi: minute wali sui poore 60 chakkar kaat-ti hai tab jakar ghante wali sui sirf 1 step aage badhti hai.",
                "common_mistakes": [
                    {
                        "mistake": "Reusing the same variable name in outer and inner loops: for i in range(3): for i in range(3):",
                        "why_it_fails_en": "The inner loop clobbers and overwrites the outer loop's counter variable.",
                        "why_it_fails_hi": "Dono me same variable rakhne se counter value kharab ho jaati hai.",
                        "fix": "Always use distinct variable names: for i in range(3): for j in range(3):"
                    }
                ],
                "example_1": {
                    "title": "Printing a 2D Star Grid (3x3)",
                    "title_hi": "3x3 Stars ka Grid banana",
                    "code": "for row in range(3):\n    for col in range(3):\n        print('*', end=' ')\n    print()  # Newline after each row",
                    "expected_output": "* * * \n* * * \n* * * ",
                    "explanation_en": "Outer loop controls rows; inner loop prints 3 stars per row.",
                    "explanation_hi": "Bahar wala loop rows banata hai, andar wala har row me 3 stars print karta hai."
                },
                "example_2": {
                    "title": "Pair Combinations Matrix",
                    "title_hi": "Pairs combination matrix",
                    "code": "sizes = ['S', 'M']\ncolors = ['Red', 'Blue']\nfor s in sizes:\n    for c in colors:\n        print(f'{s}-{c}', end=' ')\nprint()",
                    "expected_output": "S-Red S-Blue M-Red M-Blue ",
                    "explanation_en": "Combines 2 sizes with 2 colors to output all 4 combinations.",
                    "explanation_hi": "Sizes aur colors ke saare possible pairs generate karta hai."
                },
                "challenge": {
                    "prompt_en": "Print a 2x2 coordinate grid: (0,0) (0,1) on line 1, and (1,0) (1,1) on line 2.",
                    "prompt_hi": "2x2 coordinates print karo: pehli line par (0,0) (0,1) aur doosri line par (1,0) (1,1)",
                    "starter_code": "# Nested loops for 2x2 grid:\n",
                    "expected_output": "(0,0) (0,1)\n(1,0) (1,1)",
                    "solution_code": "for r in range(2):\n    row_str = ' '.join(f'({r},{c})' for c in range(2))\n    print(row_str)",
                    "solution_explanation_en": "Generates 2 rows of coordinates.",
                    "solution_explanation_hi": "2 rows me coordinates print karta hai.",
                    "hints": ["Outer loop r in range(2), inner loop c in range(2)."],
                    "ego_roast_hi": "Matrix coordinates me ghoom gaye?",
                    "ego_cheer_hi": "2D multidimensional looping conquered! 🔄"
                }
            },
            {
                "id": "ch7_sub9_mini_project_password_guesser",
                "title": "Mini-Project: A Password Guesser Game",
                "title_hi": "Mini-Project: Password Guesser Game",
                "icon": "🔐",
                "is_mini_project": True,
                "duration": "15 mins",
                "xp": 150,
                "what_is_it_en": "A complete, functioning terminal security game where the user has a limited number of attempts to crack a secret password. The game uses while loops, attempts tracking, break on success, and lockout detection.",
                "what_is_it_hi": "Ek complete functioning security game jisme limited attempts (jaise 3 mauke) milte hain secret password crack karne ke. while loop, attempts counter, break aur lockout logic use hota hai.",
                "why_need_it_en": "Synthesizes loops, conditionals, state counters, break statements, and user feedback into a real-world cybersecurity application.",
                "why_need_it_hi": "Real-world cybersecurity (ATM PIN lock, account lockout) me yahi exact while-loop logic use hota hai.",
                "how_to_use_en": "Track attempts with while attempts < max_attempts:, check if guess == secret:, break on success.",
                "how_to_use_hi": "attempts count karo while loop me, match hone par break karo.",
                "syntax": "# Password Guesser Engine:\nsecret = \"elysia\"\nattempts = 0\nmax_attempts = 3\nwhile attempts < max_attempts:\n    attempts += 1\n    if guess == secret:\n        print(\"Unlocked!\")\n        break\nelse:\n    print(\"Account Locked!\")",
                "rules_en": [
                    "Increment attempt counter on every iteration.",
                    "Break immediately when secret is matched.",
                    "Trigger lockout warning if maximum attempts are exhausted."
                ],
                "rules_hi": [
                    "Har guess par attempts counter badhao.",
                    "Sahi password milte hi break laga kar unlock karo.",
                    "Attempts khatam hone par account lock alert dikhao."
                ],
                "analogy_en": "An iPhone that allows 5 PIN attempts before locking you out for 15 minutes.",
                "analogy_hi": "iPhone PIN lock jaisa — 3 baar galat PIN dala to screen lock ho jaati hai.",
                "common_mistakes": [
                    {
                        "mistake": "Not breaking when the password is correct, continuing to ask for more guesses.",
                        "why_it_fails_en": "Frustrates the user by asking for input even after they won.",
                        "why_it_fails_hi": "Jeetne ke baad bhi loop chalta rahega agar break nahi lagaya.",
                        "fix": "Always execute 'break' immediately after a winning guess."
                    }
                ],
                "example_1": {
                    "title": "Complete Password Guesser Simulation",
                    "title_hi": "Password Guesser ka simulation",
                    "code": "# =========================================\n# MINI-PROJECT: CYBER SECURITY PIN CRACKER\n# =========================================\nsecret_pin = '4455'\nguesses = ['1234', '4455']  # Simulated inputs\nmax_tries = 3\nattempt = 0\nunlocked = False\n\nfor g in guesses:\n    attempt += 1\n    print(f'Attempt {attempt}: Trying PIN {g}...')\n    if g == secret_pin:\n        print('🔓 ACCESS GRANTED! System Unlocked.')\n        unlocked = True\n        break\n    else:\n        print('❌ INCORRECT PIN.')\n\nif not unlocked:\n    print('🚨 SECURITY LOCKOUT ACTIVATED!')",
                    "expected_output": "Attempt 1: Trying PIN 1234...\n❌ INCORRECT PIN.\nAttempt 2: Trying PIN 4455...\n🔓 ACCESS GRANTED! System Unlocked.",
                    "explanation_en": "Fails on attempt 1, succeeds on attempt 2, breaks cleanly before attempt 3.",
                    "explanation_hi": "Pehle attempt par fail hua, doosre par sahi pin milte hi unlock ho gaya."
                },
                "example_2": {
                    "title": "Account Lockout Scenario",
                    "title_hi": "Lockout scenario jab saare attempts khatam ho jayein",
                    "code": "attempts_left = 1\nif attempts_left == 1:\n    print('⚠️ WARNING: 1 attempt remaining before lockout!')",
                    "expected_output": "⚠️ WARNING: 1 attempt remaining before lockout!",
                    "explanation_en": "Displays security warning threshold.",
                    "explanation_hi": "Security threshold warning display karta hai."
                },
                "challenge": {
                    "prompt_en": "Simulate PIN guesser: secret = '1234', guess = '1234'. If guess == secret, print: Unlocked in 1 try!",
                    "prompt_hi": "PIN guesser: secret = '1234', guess = '1234'. Agar match ho to print karo: Unlocked in 1 try!",
                    "starter_code": "secret = '1234'\nguess = '1234'\n# Check guess and print:\n",
                    "expected_output": "Unlocked in 1 try!",
                    "solution_code": "secret = '1234'\nguess = '1234'\nif guess == secret:\n    print('Unlocked in 1 try!')",
                    "solution_explanation_en": "Checks match and outputs successful unlock confirmation.",
                    "solution_explanation_hi": "PIN match karke unlock message print karta hai.",
                    "hints": ["if guess == secret: print('Unlocked in 1 try!')"],
                    "ego_roast_hi": "PIN verify karna nahi aa raha?",
                    "ego_cheer_hi": "BOOM! 💥 MINI-PROJECT 3 COMPLETED! Security password cracker verified! 🏆"
                }
            }
        ]
    }
]
