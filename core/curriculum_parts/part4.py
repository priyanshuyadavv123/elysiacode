"""
Part 4: Working Smart, Not Hard (Functions & Modularity)
Chapters 12, 13, and 14 with exact syllabus titles and subtopics.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 12: Building Your Own Tools (Functions)
    # =========================================================================
    {
        "id": "ch12_functions",
        "part_number": 4,
        "part_title": "PART 4: WORKING SMART, NOT HARD (FUNCTIONS & MODULARITY)",
        "chapter_number": 12,
        "title": "Chapter 12: Building Your Own Tools (Functions)",
        "subtitle_en": "Reusability, def keyword, parameters vs arguments, return vs print, and argument binding",
        "subtitle_hi": "Functions banana: def keyword, parameters vs arguments, return vs print aur default values",
        "icon": "🛠️",
        "estimated_time": "35 mins",
        "prerequisites_en": "Parts 1, 2, and 3 (Variables, loops, conditionals, data structures).",
        "prerequisites_hi": "Part 1, 2, 3 (Variables, loops, if-else, data structures).",
        "learning_objectives_en": [
            "Understand the reusable recipe mental model of functions",
            "Define functions with def and execute them by calling ()",
            "Distinguish parameters (placeholders) from arguments (actual inputs)",
            "Master the difference between return (value output) and print (terminal display)",
            "Use default parameters and contrast positional vs keyword arguments"
        ],
        "learning_objectives_hi": [
            "Function ka reusable recipe mental model seekho",
            "def se function banana aur () laga kar call karna",
            "Parameters (names) aur Arguments (values) ka critical farak",
            "return (value wapas aana) vs print (screen pe dikhana) ka difference",
            "Default parameters aur positional vs keyword arguments"
        ],
        "recap_en": "You mastered function architecture: definition, invocation, argument mapping, return values vs side-effect printing, and default parameter styling.",
        "recap_hi": "Aapne functions ka creation, execution, parameters vs arguments, return keyword aur default values master ki.",
        "subtopics": [
            {
                "id": "ch12_sub1_what_is_a_function",
                "title": "What is a function? (The \"recipe\" concept)",
                "title_hi": "Function kya hota hai? (\"Recipe\" Concept)",
                "icon": "📜",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A function is a reusable, named block of code that performs a specific action. You define the instructions ONCE, and can call it thousands of times from anywhere in your codebase.",
                "what_is_it_hi": "Function ek baar likha gaya reusable code block hota hai. Aap recipe ek baar likhte ho, aur jab bhi zaroorat ho bas function ka naam pukaar kar use chala sakte ho.",
                "why_need_it_en": "Without functions, calculating sales tax across 50 checkout pages requires copying the same 10 lines of math everywhere. If tax changes, you have to find and update all 50 places!",
                "why_need_it_hi": "Bina function ke har jagah same code copy-paste karna padta. Function banane se sirf ek jagah change karo, poori app me update ho jata hai.",
                "how_to_use_en": "Define once with def name():, call anytime with name().",
                "how_to_use_hi": "def se banao, naam() se call karo.",
                "syntax": "# Define the recipe:\ndef brew_coffee():\n    print(\"Boiling water...\")\n    print(\"Adding coffee...\")\n    print(\"Coffee ready!\")\n\n# Call the recipe whenever needed:\nbrew_coffee()",
                "rules_en": [
                    "A function DOES NOTHING until you explicitly CALL it.",
                    "Defining a function loads its bytecode into memory; calling it executes the body.",
                    "Follow the Single Responsibility Principle: a function should do ONE thing well."
                ],
                "rules_hi": [
                    "Jab tak aap function ko CALL nahi karte, wo kuch nahi karta.",
                    "Function define karne se memory me save hota hai, call karne par chalta hai.",
                    "Ek function ko ek hi kaam achhe se karna chahiye."
                ],
                "analogy_en": "A recipe card for making Chai: having the recipe in your drawer doesn't make tea. Only when you FOLLOW the recipe (call the function) do you get a hot cup of tea.",
                "analogy_hi": "Chai banane ki recipe card jaisi — card kitchen me rakhne se chai nahi banti. Jab aap recipe execute karte ho (function call), tab chai milti hai.",
                "common_mistakes": [
                    {
                        "mistake": "Writing the function definition and wondering why nothing prints to terminal.",
                        "why_it_fails_en": "You only defined the recipe; you forgot to CALL it with parentheses ()!",
                        "why_it_fails_hi": "Function sirf banaya, call karna bhool gaye.",
                        "fix": "Always invoke the function: my_function()."
                    }
                ],
                "example_1": {
                    "title": "Defining and Calling a Function",
                    "title_hi": "Function banana aur run karna",
                    "code": "def show_banner():\n    print('=== SYSTEM ONLINE ===')\n    print('Status: 100% Operational')\n\nshow_banner()  # Execution trigger",
                    "expected_output": "=== SYSTEM ONLINE ===\nStatus: 100% Operational",
                    "explanation_en": "show_banner() invokes the pre-defined sequence of instructions.",
                    "explanation_hi": "show_banner() pehle se save instructions ko run karta hai."
                },
                "example_2": {
                    "title": "Reusing Functions Multiple Times",
                    "title_hi": "Function ko baar baar reuse karna",
                    "code": "def cheer():\n    print('Elysia Code!')\n\nfor _ in range(2):\n    cheer()",
                    "expected_output": "Elysia Code!\nElysia Code!",
                    "explanation_en": "The function is called twice without duplicate logic.",
                    "explanation_hi": "Loop ke andar do baar same function call hota hai."
                },
                "challenge": {
                    "prompt_en": "Define a function announce() that prints 'Event Started!'. Call it once.",
                    "prompt_hi": "announce() function banao jo 'Event Started!' print kare. Use ek baar call karo.",
                    "starter_code": "# Define and call announce():\n",
                    "expected_output": "Event Started!",
                    "solution_code": "def announce():\n    print('Event Started!')\n\nannounce()",
                    "solution_explanation_en": "Defines announce() with def and calls announce().",
                    "solution_explanation_hi": "def announce() bana kar announce() call karta hai.",
                    "hints": ["def announce():\\n    print('Event Started!')\\nannounce()"],
                    "ego_roast_hi": "Function call ke brackets () bhool gaye kya?",
                    "ego_cheer_hi": "Reusable function tool created! 🛠️"
                }
            },
            {
                "id": "ch12_sub2_defining_with_def",
                "title": "Defining a function using def",
                "title_hi": "def keyword se function define karna",
                "icon": "✍️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "'def' is a Python keyword that stands for 'define'. It signals to the Python interpreter that a new function header is beginning.",
                "what_is_it_hi": "'def' Python ka keyword hai jiska matlab hai 'define karna'. Ye interpreter ko batata hai ki yahan se naya function shuru ho raha hai.",
                "why_need_it_en": "Without a dedicated keyword, the parser cannot distinguish a function declaration from a variable assignment or function call.",
                "why_need_it_hi": "def ke bina Python ko samajh nahi aayega ki aap naya function bana rahe ho ya purana call kar rahe ho.",
                "how_to_use_en": "def function_name(parameters): followed by an indented 4-space body.",
                "how_to_use_hi": "def function_name(): ke baad colon lagao aur 4 spaces aage code likho.",
                "syntax": "def calculate_tax():\n    # 4 spaces indentation\n    rate = 0.18\n    print(f\"Active GST rate: {rate * 100}%\")",
                "rules_en": [
                    "The function name follows standard snake_case naming rules (same as variables).",
                    "A colon (:) is MANDATORY at the end of the def line.",
                    "Parentheses () are mandatory, even if the function accepts zero parameters.",
                    "The function body must be indented by 4 spaces."
                ],
                "rules_hi": [
                    "Function name hamesha snake_case me hona chahiye (calculate_bill).",
                    "def line ke aakhri me colon (:) lagana mandatory hai.",
                    "Gol brackets () zaroori hain chahe koi input na ho.",
                    "Function ke andar ka code 4 spaces aage hona chahiye."
                ],
                "analogy_en": "Like naming a new button on a machine control panel: you label the button 'Eject' (def eject()) before anyone can press it.",
                "analogy_hi": "Remote control par naya button install karne jaisa — pehle uspe 'Power' likha (def), tabhi use daba sakte ho.",
                "common_mistakes": [
                    {
                        "mistake": "Forgetting parentheses in def: def my_func: print('Hi')",
                        "why_it_fails_en": "SyntaxError: invalid syntax. Parentheses () are mandatory in def.",
                        "why_it_fails_hi": "Bina brackets ke Python SyntaxError de dega.",
                        "fix": "Always include parentheses: def my_func():"
                    }
                ],
                "example_1": {
                    "title": "Function Definition Structure",
                    "title_hi": "Function definition ka saaf structure",
                    "code": "def boot_server():\n    print('Server port: 8080')\n    print('Server status: RUNNING')\n\nboot_server()",
                    "expected_output": "Server port: 8080\nServer status: RUNNING",
                    "explanation_en": "Standard def statement executing two indented print statements.",
                    "explanation_hi": "Standard def structure do print statements chalaata hai."
                },
                "example_2": {
                    "title": "Local Variables Inside Def",
                    "title_hi": "Function ke andar local variables",
                    "code": "def calculate_speed():\n    dist = 100\n    time = 2\n    print('Speed:', dist / time, 'km/h')\n\ncalculate_speed()",
                    "expected_output": "Speed: 50.0 km/h",
                    "explanation_en": "dist and time are local variables scoped inside calculate_speed().",
                    "explanation_hi": "dist aur time function ke andar ke local variables hain."
                },
                "challenge": {
                    "prompt_en": "Define a function ping() with def that prints: Pong!",
                    "prompt_hi": "def se ping() function banao jo print kare: Pong! Fir ping() call karo.",
                    "starter_code": "# Define and call ping():\n",
                    "expected_output": "Pong!",
                    "solution_code": "def ping():\n    print('Pong!')\n\nping()",
                    "solution_explanation_en": "Standard definition and invocation of ping().",
                    "solution_explanation_hi": "ping() bana kar use call karta hai.",
                    "hints": ["def ping():\\n    print('Pong!')\\nping()"],
                    "ego_roast_hi": "def ke aage colon (:) lagana bhool gaye?",
                    "ego_cheer_hi": "def statement syntax verified! ✍️"
                }
            },
            {
                "id": "ch12_sub3_calling_a_function",
                "title": "Calling a function to make it run",
                "title_hi": "Function ko call karke execute karna",
                "icon": "📞",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Calling (or invoking) a function means executing its code by typing the function's name followed by parentheses: function_name().",
                "what_is_it_hi": "Function ko call karna matlab uska naam likh kar aage brackets lagana: function_name(). Bina brackets ke function run nahi hota!",
                "why_need_it_en": "Writing just the name without parentheses (e.g. print) passes the function object itself, rather than running it.",
                "why_need_it_hi": "Agar brackets nahi lagaoge to function execute nahi hoga, balki uska memory address dikhega.",
                "how_to_use_en": "Type func() to execute. To pass it as a reference, use func without ().",
                "how_to_use_hi": "Run karne ke liye func() likho.",
                "syntax": "# Calling function:\nmy_func()",
                "rules_en": [
                    "Parentheses () are the EXECUTION OPERATOR in Python.",
                    "Without (), my_func is just a function object reference: <function my_func at 0x...>",
                    "Calling a function transfers execution control to the function body, then returns control to the caller."
                ],
                "rules_hi": [
                    "Brackets () Python me execution ka trigger hote hain.",
                    "Bina brackets ke function execute nahi hota, bas uska reference pass hota hai.",
                    "Call karne par control function ke andar jaata hai aur khatam hone par wapas aata hai."
                ],
                "analogy_en": "The function name is a light switch. Adding parentheses () is your finger physically flipping the switch up to turn the light ON.",
                "analogy_hi": "Function ka naam switch hai, aur brackets () ungli se switch ko press karna hai. Bina press kiye light nahi jalegi.",
                "common_mistakes": [
                    {
                        "mistake": "Writing greet without parentheses and wondering why nothing happened.",
                        "why_it_fails_en": "greet is merely the function object; it never executed.",
                        "why_it_fails_hi": "Bina () ke function trigger hi nahi hota.",
                        "fix": "Always append parentheses to execute: greet()."
                    }
                ],
                "example_1": {
                    "title": "Executing with Parentheses",
                    "title_hi": "() se execution trigger",
                    "code": "def play_sound():\n    print('Ding! 🔔')\n\nplay_sound()",
                    "expected_output": "Ding! 🔔",
                    "explanation_en": "Parentheses () execute the play_sound routine.",
                    "explanation_hi": "play_sound() call hone par print statement chalta hai."
                },
                "example_2": {
                    "title": "Name vs Invocation",
                    "title_hi": "Function name vs Function call ka farak",
                    "code": "def sample():\n    return 'done'\n\nprint('Without ():', type(sample).__name__)\nprint('With ():', sample())",
                    "expected_output": "Without (): function\nWith (): done",
                    "explanation_en": "Without () it is a function object; with () it executes and returns 'done'.",
                    "explanation_hi": "Bina () ke wo function object hai, () ke sath wo execute hoke 'done' deta hai."
                },
                "challenge": {
                    "prompt_en": "Define action() that prints 'Action Executed!'. Call action().",
                    "prompt_hi": "action() define karo jo 'Action Executed!' print kare. Use call karo.",
                    "starter_code": "# Define and call action:\n",
                    "expected_output": "Action Executed!",
                    "solution_code": "def action():\n    print('Action Executed!')\n\naction()",
                    "solution_explanation_en": "Invokes action() using parentheses.",
                    "solution_explanation_hi": "action() call karke message print karta hai.",
                    "hints": ["action()"],
                    "ego_roast_hi": "action() ke aage brackets lagana bhool gaye?",
                    "ego_cheer_hi": "Function execution confirmed! 📞"
                }
            },
            {
                "id": "ch12_sub4_arguments_parameters",
                "title": "Passing information in: Arguments and Parameters",
                "title_hi": "Information bhejna: Arguments aur Parameters ka farak",
                "icon": "📥",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "PARAMETERS are the variable names listed in the function definition (the blueprint placeholders). ARGUMENTS are the actual real values passed into the function when you call it.",
                "what_is_it_hi": "PARAMETERS wo variable names hain jo function banate waqt header me likhe jaate hain (jaise def greet(name): me 'name' parameter hai). ARGUMENTS wo actual values hain jo call karte waqt pass ki jaati hain (jaise greet('Alex') me 'Alex' argument hai).",
                "why_need_it_en": "It makes functions universal and dynamic! A single greet(user) function can personalize greetings for 100,000 different users.",
                "why_need_it_hi": "Isse function dynamic ban jata hai: ek hi greet(name) function se 10,000 alag users ko unke naam se welcome kiya ja sakta hai.",
                "how_to_use_en": "def add(a, b): return a + b -> add(5, 10).",
                "how_to_use_hi": "def add(a, b): return a + b -> add(5, 10).",
                "syntax": "# 'name' and 'age' are PARAMETERS (Placeholders):\ndef greet_user(name, age):\n    print(f\"Hello {name}, you are {age} years old!\")\n\n# \"Alex\" and 20 are ARGUMENTS (Actual Values):\ngreet_user(\"Alex\", 20)",
                "rules_en": [
                    "CRITICAL INTERVIEW LAW: Parameter = Variable in function definition. Argument = Actual value in function call.",
                    "The number of arguments passed must match the number of expected parameters (unless defaults are provided).",
                    "Arguments are passed by assignment (object references are bound to parameter names)."
                ],
                "rules_hi": [
                    "INTERVIEW NIYAM: Parameter = Function banate waqt ka variable naam. Argument = Call karte waqt di gayi actual value.",
                    "Jitne parameters hain, utne arguments dena zaroori hai (agar default na ho).",
                    "Python me arguments 'pass by object reference' hote hain."
                ],
                "analogy_en": "A coin-operated vending machine: The coin slot shape is the PARAMETER (expects a coin). The actual 5-rupee coin you drop in is the ARGUMENT.",
                "analogy_hi": "Vending machine ka coin slot PARAMETER hai (jo sikka maangta hai). Aapki jeb se nikla 5 rupaye ka sikka ARGUMENT hai.",
                "common_mistakes": [
                    {
                        "mistake": "Calling a 2-parameter function with only 1 argument: add(5)",
                        "why_it_fails_en": "TypeError: add() missing 1 required positional argument: 'b'.",
                        "why_it_fails_hi": "Function 2 cheezein maang raha tha aur aapne sirf 1 di.",
                        "fix": "Provide all required arguments: add(5, 10)."
                    }
                ],
                "example_1": {
                    "title": "Parameters Receiving Arguments",
                    "title_hi": "Dynamic personalized function",
                    "code": "def personalize_welcome(name, course):\n    print(f'Welcome {name} to {course}!')\n\npersonalize_welcome('Aman', 'Python Mastery')",
                    "expected_output": "Welcome Aman to Python Mastery!",
                    "explanation_en": "Parameters 'name' and 'course' receive arguments 'Aman' and 'Python Mastery'.",
                    "explanation_hi": "Parameters me actual arguments pass ho kar print hote hain."
                },
                "example_2": {
                    "title": "Math Function with Multiple Inputs",
                    "title_hi": "Do numbers ko multiply karne wala function",
                    "code": "def multiply(x, y):\n    print(f'{x} * {y} = {x * y}')\n\nmultiply(6, 7)",
                    "expected_output": "6 * 7 = 42",
                    "explanation_en": "x=6, y=7 are bound and multiplied.",
                    "explanation_hi": "6 aur 7 multiply hoke 42 print hota hai."
                },
                "challenge": {
                    "prompt_en": "Define square(n) that prints: Square of n is n*n. Call square(5).",
                    "prompt_hi": "square(n) define karo jo print kare: Square of 5 is 25. square(5) call karo.",
                    "starter_code": "# Define and call square(5):\n",
                    "expected_output": "Square of 5 is 25",
                    "solution_code": "def square(n):\n    print(f'Square of {n} is {n * n}')\n\nsquare(5)",
                    "solution_explanation_en": "Parameter n receives argument 5 and prints 25.",
                    "solution_explanation_hi": "Parameter n me 5 jata hai aur square 25 print hota hai.",
                    "hints": ["def square(n):\\n    print(f'Square of {n} is {n * n}')"],
                    "ego_roast_hi": "Parameter pass karna bhool gaye?",
                    "ego_cheer_hi": "Parameters vs arguments mastered! 📥"
                }
            },
            {
                "id": "ch12_sub5_return_vs_print",
                "title": "Giving information back: The return keyword (vs. print)",
                "title_hi": "Information wapas dena: return keyword vs print ka farak",
                "icon": "↩️",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "'return' hands a calculated value BACK to whoever called the function so it can be stored in a variable, used in further math, or passed to other functions. 'print()' merely writes text to the terminal screen and gives NOTHING back (it returns None!).",
                "what_is_it_hi": "'return' function ke calculation ka result WAPAS US JAGAH BHEJTA HAI jahan se function call hua tha, taaki aap use variable me store kar sako ya aage math me use kar sako. 'print()' sirf screen par text dikhata hai aur WAPAS KUCH NAHI DETA (None return karta hai!).",
                "why_need_it_en": "If a function computes user tax, you can't subtract the tax from their salary if the function only printed it to the screen! You must RETURN it so your code can use the number.",
                "why_need_it_hi": "Agar tax calculate karne wala function sirf print karega, to salary me se tax minus kaise karoge? Math aage badhane ke liye 'return' zaroori hai.",
                "how_to_use_en": "def add(a, b): return a + b -> total = add(10, 20).",
                "how_to_use_hi": "def add(a, b): return a + b -> result = add(5, 5).",
                "syntax": "# ❌ ONLY PRINTS (Returns None):\ndef calc_print(a, b):\n    print(a + b)\n\n# ✅ RETURNS VALUE (Usable in further code):\ndef calc_return(a, b):\n    return a + b\n\nval = calc_return(10, 20)  # val is 30\nfinal = val * 2            # 60",
                "rules_en": [
                    "CRITICAL LAW: A function without an explicit 'return' statement returns 'None' by default.",
                    "'return' immediately TERMINATES the function — any lines after 'return' inside that function are unreachable dead code.",
                    "You can return multiple values: 'return x, y' (returns a tuple)."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: Agar function me 'return' nahi likha to wo chupke se 'None' return karta hai.",
                    "'return' aate hi function turant ruk jata hai. Uske neeche ki lines kabhi nahi chalti.",
                    "'return a, b' likhne par Python dono ko tuple me pack karke return karta hai."
                ],
                "analogy_en": "print() is a chef shouting 'Your pasta is ready!' out the kitchen window. return is the waiter actually placing the plate of pasta on your table so you can eat it.",
                "analogy_hi": "print() chef ka chilana hai: 'Khana ready hai!' (sirf aawaaz aayi). return waiter ka sach me khane ki thali aapke table par laakar rakhna hai jise aap kha sakte ho.",
                "common_mistakes": [
                    {
                        "mistake": "Assigning from a printing function: res = add(5, 5) where add() uses print(a+b).",
                        "why_it_fails_en": "res will be None! Trying res * 2 crashes with TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'.",
                        "why_it_fails_hi": "print() None deta hai, to res me None store hoga aur aage multiply karne par crash ho jayega.",
                        "fix": "Use return a + b inside the function."
                    }
                ],
                "example_1": {
                    "title": "Return vs Print in Chained Math",
                    "title_hi": "return ki value ko aage use karna",
                    "code": "def add_tax(price):\n    return price * 1.18\n\nbill = add_tax(100)\nprint('Total Bill with 18% tax:', bill)\nprint('Half of bill:', bill / 2)",
                    "expected_output": "Total Bill with 18% tax: 118.0\nHalf of bill: 59.0",
                    "explanation_en": "Because add_tax returned 118.0, bill can be further divided by 2.",
                    "explanation_hi": "return ki wajah se bill 118.0 mila aur aage 2 se divide ho paya."
                },
                "example_2": {
                    "title": "Return Terminates Function Immediately",
                    "title_hi": "return aate hi function ka rukna",
                    "code": "def check_pass(marks):\n    if marks >= 40:\n        return 'Passed'\n    return 'Failed'  # Acts like else!\n\nprint('Score 75:', check_pass(75))\nprint('Score 30:', check_pass(30))",
                    "expected_output": "Score 75: Passed\nScore 30: Failed",
                    "explanation_en": "As soon as return executes, the function exits immediately.",
                    "explanation_hi": "return chalte hi function se turant exit ho jata hai."
                },
                "challenge": {
                    "prompt_en": "Write double(x) that returns x * 2. Store ans = double(25) and print: Doubled: 50",
                    "prompt_hi": "double(x) banao jo return x * 2 kare. ans = double(25) karke print karo: Doubled: 50",
                    "starter_code": "# Define double(x) with return:\n",
                    "expected_output": "Doubled: 50",
                    "solution_code": "def double(x):\n    return x * 2\n\nans = double(25)\nprint(f'Doubled: {ans}')",
                    "solution_explanation_en": "double(25) returns 50, which is stored in ans and printed.",
                    "solution_explanation_hi": "double(25) 50 return karta hai jo ans me store hoke print hota hai.",
                    "hints": ["def double(x):\\n    return x * 2"],
                    "ego_roast_hi": "return ki jagah print to nahi likh diya?",
                    "ego_cheer_hi": "return keyword mastery unlocked! ↩️"
                }
            },
            {
                "id": "ch12_sub6_default_parameters",
                "title": "Default parameters (Making arguments optional)",
                "title_hi": "Default parameters (Arguments ko optional banana)",
                "icon": "⚙️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Default parameters let you assign a fallback value to a parameter in the function definition: def greet(name='Guest'):. If the caller provides an argument, it uses the provided value; if omitted, it smoothly falls back to the default.",
                "what_is_it_hi": "Default parameters se aap kisi parameter ko optional bana sakte ho: def greet(name='Guest'):. Agar user argument dega to uski value use hogi; agar nahi dega to default fallback 'Guest' use ho jayega.",
                "why_need_it_en": "Like print(sep=' ', end='\\n'): Python has thousands of built-in functions with defaults so you only specify arguments when you want to customize them.",
                "why_need_it_hi": "print(sep=' ', end='\\n') me defaults hote hain. Defaults hone se har baar saari details type nahi karni padti.",
                "how_to_use_en": "def power(base, exp=2): return base ** exp.",
                "how_to_use_hi": "def func(x, factor=1): return x * factor.",
                "syntax": "def send_email(to, subject=\"No Subject\", priority=\"Normal\"):\n    print(f\"Sending to {to} | Sub: {subject} | Priority: {priority}\")",
                "rules_en": [
                    "CRITICAL SYNTAX LAW: Non-default parameters CANNOT follow default parameters! def func(a=1, b): is illegal (SyntaxError).",
                    "Default parameters must always appear AFTER all positional parameters: def func(b, a=1): is valid.",
                    "NEVER use mutable default arguments (like def f(items=[]):)! Use def f(items=None): items = items or []."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: Default parameters hamesha AAKHRI me hone chahiye. def f(a=1, b) strictly ILLEGAL hai.",
                    "Mutable default (jaise items=[]) kabhi mat lagao, items=None lagao.",
                    "Optional parameters ko hamesha right side me rakha jata hai."
                ],
                "analogy_en": "Ordering coffee: The default is dairy milk and 1 sugar. You only specify 'almond milk and zero sugar' if you want to override the default.",
                "analogy_hi": "Restaurant me thali order karna: Default me roti aur daal aati hi hai. Agar alag se naan chahiye tabhi bolna padta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Placing non-default parameter after default parameter: def greet(msg='Hello', name):",
                        "why_it_fails_en": "SyntaxError: non-default argument follows default argument.",
                        "why_it_fails_hi": "Default parameter pehle aur required parameter baad me nahi aa sakta.",
                        "fix": "Reorder parameters: def greet(name, msg='Hello'):"
                    }
                ],
                "example_1": {
                    "title": "Function with Optional Default Argument",
                    "title_hi": "Default parameter ka live use",
                    "code": "def calculate_power(base, exp=2):\n    return base ** exp\n\nprint('Default squared (5):', calculate_power(5))\nprint('Custom cubed (5, 3):', calculate_power(5, 3))",
                    "expected_output": "Default squared (5): 25\nCustom cubed (5, 3): 125",
                    "explanation_en": "Uses default exp=2 when omitted, but overrides it when 3 is passed.",
                    "explanation_hi": "Chhodne par default 2 leta hai, dene par 3 use karta hai."
                },
                "example_2": {
                    "title": "Multiple Defaults for Configuration",
                    "title_hi": "Multiple default parameters",
                    "code": "def create_box(width=10, height=10):\n    return f'{width}x{height}'\n\nprint('Default box:', create_box())\nprint('Custom width:', create_box(50))",
                    "expected_output": "Default box: 10x10\nCustom width: 50x10",
                    "explanation_en": "Both parameters have defaults and can be partially or fully overridden.",
                    "explanation_hi": "Dono parameters ke defaults hain jinhe customize kiya ja sakta hai."
                },
                "challenge": {
                    "prompt_en": "Define greet(name, greeting='Hello'). Calling greet('Alex') prints 'Hello, Alex!'. Calling greet('Alex', 'Hi') prints 'Hi, Alex!'. Test with greet('Alex').",
                    "prompt_hi": "greet(name, greeting='Hello') define karo jo print kare: Hello, Alex! greet('Alex') call karo.",
                    "starter_code": "# Define greet with default greeting:\n",
                    "expected_output": "Hello, Alex!",
                    "solution_code": "def greet(name, greeting='Hello'):\n    print(f'{greeting}, {name}!')\n\ngreet('Alex')",
                    "solution_explanation_en": "Uses default 'Hello' when second argument is omitted.",
                    "solution_explanation_hi": "Default 'Hello' use karke 'Hello, Alex!' print karta hai.",
                    "hints": ["def greet(name, greeting='Hello'):\\n    print(f'{greeting}, {name}!')"],
                    "ego_roast_hi": "Default parameter aakhri me lagana bhool gaye?",
                    "ego_cheer_hi": "Default parameters configured cleanly! ⚙️"
                }
            },
            {
                "id": "ch12_sub7_positional_vs_keyword",
                "title": "Positional vs. Keyword arguments",
                "title_hi": "Positional vs. Keyword arguments",
                "icon": "🎯",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "POSITIONAL arguments are passed in exact order based on parameter positions. KEYWORD (named) arguments explicitly specify the parameter name during invocation (e.g. func(age=20, name='Alex')), allowing arguments to be passed in ANY order!",
                "what_is_it_hi": "POSITIONAL arguments order (position) ke hisab se pass hote hain. KEYWORD arguments me aap parameter ka naam likh kar value dete ho (age=20, name='Alex'), jisse order ka koi chakkar nahi rehta aur code bohot readable banta hai!",
                "why_need_it_en": "When a function has 6 configuration parameters, keyword arguments prevent bugs like accidentally passing email where username was expected.",
                "why_need_it_hi": "Jab function me 5-6 parameters hote hain to keyword arguments se galti se galat dabba bharne ka risk khatam ho jata hai.",
                "how_to_use_en": "Positional: send('A', 'B'). Keyword: send(sender='A', recipient='B').",
                "how_to_use_hi": "Keyword call: transfer(amount=500, to_account='1234').",
                "syntax": "def create_user(username, email, role=\"member\"):\n    pass\n\n# Positional:\ncreate_user(\"alex\", \"alex@test.com\")\n# Keyword (Order does not matter!):\ncreate_user(email=\"alex@test.com\", username=\"alex\")",
                "rules_en": [
                    "Positional arguments MUST always precede keyword arguments in a call: func(10, y=20) is valid; func(x=10, 20) is a SyntaxError.",
                    "Keyword arguments make function calls self-documenting.",
                    "You cannot provide multiple values for the same parameter."
                ],
                "rules_hi": [
                    "Positional arguments hamesha keyword arguments se PEHLE aane chahiye. func(x=10, 20) galat hai.",
                    "Keyword arguments se code self-documenting ban jata hai.",
                    "Ek hi parameter ko do baar value nahi de sakte."
                ],
                "analogy_en": "Positional is a physical envelope: Name must be on line 1, Street on line 2, Pincode on line 3. Keyword is a form with labeled boxes: you can fill Box 'Pincode' before Box 'Name'.",
                "analogy_hi": "Positional line me khade hone jaisa hai. Keyword form me labeled boxes bharne jaisa hai — pehle phone number likho ya pehle naam, sab sahi dabbe me jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Passing a positional argument after a keyword argument: func(a=5, 10)",
                        "why_it_fails_en": "SyntaxError: positional argument follows keyword argument.",
                        "why_it_fails_hi": "Keyword argument ke baad bina naam ka positional argument nahi aa sakta.",
                        "fix": "Put all positional arguments first: func(10, a=5)."
                    }
                ],
                "example_1": {
                    "title": "Flexible Order with Keyword Arguments",
                    "title_hi": "Bina order ki chinta ke keyword arguments",
                    "code": "def describe_pet(animal_type, pet_name):\n    print(f'I have a {animal_type} named {pet_name}.')\n\n# Calling with flipped order using keywords\ndescribe_pet(pet_name='Harry', animal_type='Hamster')",
                    "expected_output": "I have a Hamster named Harry.",
                    "explanation_en": "Keyword arguments bind correctly regardless of argument order.",
                    "explanation_hi": "Keywords use karne par order aage-peeche hone se koi farak nahi padta."
                },
                "example_2": {
                    "title": "Mixing Positional and Keyword Arguments",
                    "title_hi": "Positional aur Keyword mix karna",
                    "code": "def order_pizza(size, crust='Thin', cheese='Mozzarella'):\n    print(f'Pizza: {size} | Crust: {crust} | Cheese: {cheese}')\n\n# 1 positional, 1 keyword\norder_pizza('Large', cheese='Cheddar')",
                    "expected_output": "Pizza: Large | Crust: Thin | Cheese: Cheddar",
                    "explanation_en": "'Large' is positional for size; cheese='Cheddar' overrides default cheese keyword.",
                    "explanation_hi": "Pehla positional hai, doosra specific keyword argument hai."
                },
                "challenge": {
                    "prompt_en": "Call profile(name='Alex', role='Dev') using keyword arguments for def profile(name, role): print(f'{name}: {role}').",
                    "prompt_hi": "def profile(name, role): print(f'{name}: {role}') ko keyword arguments name='Alex', role='Dev' se call karo.",
                    "starter_code": "def profile(name, role):\n    print(f'{name}: {role}')\n\n# Call with keyword arguments:\n",
                    "expected_output": "Alex: Dev",
                    "solution_code": "def profile(name, role):\n    print(f'{name}: {role}')\n\nprofile(name='Alex', role='Dev')",
                    "solution_explanation_en": "Calls profile using explicit keyword arguments.",
                    "solution_explanation_hi": "Keyword arguments se profile call karta hai.",
                    "hints": ["profile(name='Alex', role='Dev')"],
                    "ego_roast_hi": "Keyword arguments likhna bhool gaye?",
                    "ego_cheer_hi": "Argument binding mastery unlocked! 🎯"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 13: Advanced Function Magic
    # =========================================================================
    {
        "id": "ch13_advanced_functions",
        "part_number": 4,
        "part_title": "PART 4: WORKING SMART, NOT HARD (FUNCTIONS & MODULARITY)",
        "chapter_number": 13,
        "title": "Chapter 13: Advanced Function Magic",
        "subtitle_en": "Local vs Global scope, variable *args and **kwargs, docstrings, lambdas, map, filter, and zip",
        "subtitle_hi": "Scope: Local vs Global, *args aur **kwargs, docstrings, lambda functions, map, filter aur zip",
        "icon": "✨",
        "estimated_time": "40 mins",
        "prerequisites_en": "Chapter 12 (Functions, return, parameters).",
        "prerequisites_hi": "Chapter 12 (Functions, return aur parameters).",
        "learning_objectives_en": [
            "Master variable scope (LEGB: Local, Enclosing, Global, Built-in) and the global keyword",
            "Handle arbitrary arguments with *args (tuples) and **kwargs (dictionaries)",
            "Write production-grade docstrings complying with PEP 257",
            "Write single-line anonymous lambda functions",
            "Process functional pipelines using map(), filter(), and zip()"
        ],
        "learning_objectives_hi": [
            "Variable scope (Local vs Global) aur LEGB rule samjho",
            "*args (tuple) aur **kwargs (dict) se flexible functions banana",
            "Professional docstrings likhna",
            "One-line lambda functions likhna",
            "map(), filter(), aur zip() se functional data processing"
        ],
        "recap_en": "You mastered advanced functions: variable scoping boundaries, variable argument packing (*args/**kwargs), documentation standards, inline lambdas, and functional iteration tools.",
        "recap_hi": "Aapne scope boundaries, *args aur **kwargs, docstrings, lambdas aur map/filter/zip master kiye.",
        "subtopics": [
            {
                "id": "ch13_sub1_scope_local_global",
                "title": "Understanding Scope: Local vs. Global variables",
                "title_hi": "Scope ko samajhna: Local vs. Global variables",
                "icon": "🌐",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "SCOPE determines where a variable is accessible in your code. Variables created INSIDE a function are LOCAL (born when the function runs, destroyed when it finishes). Variables created OUTSIDE all functions at the top level are GLOBAL (accessible everywhere).",
                "what_is_it_hi": "SCOPE ka matlab hota hai variable ki pahochn (visibility). Function ke ANDAR banaya gaya variable LOCAL hota hai (function khatam hote hi memory se gayab). Function ke BAHAR banaya gaya variable GLOBAL hota hai (poori file me kahin se bhi padh sakte ho).",
                "why_need_it_en": "Encapsulation: Functions shouldn't accidentally tamper with variables in other functions. Local scope keeps variables safe inside their own playground.",
                "why_need_it_hi": "Encapsulation: Ek function ka variable doosre function ke variable me ghus kar code kharab na kare, isliye local scope zaroori hai.",
                "how_to_use_en": "To modify a global variable inside a function, explicitly declare 'global my_var'.",
                "how_to_use_hi": "Global variable ko function ke andar modify karne ke liye 'global var_name' likhna padta hai.",
                "syntax": "x = 10  # GLOBAL variable\n\ndef my_func():\n    y = 5  # LOCAL variable (invisible outside!)\n    print(x + y)\n\n# print(y)  # ERROR: NameError: name 'y' is not defined",
                "rules_en": [
                    "LEGB Rule for variable resolution: Local -> Enclosing -> Global -> Built-in.",
                    "A function can READ global variables freely.",
                    "If a function tries to WRITE/ASSIGN to a variable name without the 'global' keyword, Python creates a NEW local variable with that name.",
                    "UnboundLocalError occurs if you read a variable before assigning to it locally."
                ],
                "rules_hi": [
                    "LEGB Niyam: Python pehle Local me dhoondta hai, fir Enclosing, fir Global, fir Built-in me.",
                    "Function global variable ko READ aasaani se kar sakta hai.",
                    "Agar bina 'global' likhe assign karoge to Python use naya local variable maan lega.",
                    "Best practice: 'global' keyword kam se kam use karo, arguments aur return use karo."
                ],
                "analogy_en": "A personal diary inside your bedroom (local variable: only you can read it) vs a national billboard on the highway (global variable: everyone in the country can read it).",
                "analogy_hi": "Apne kamre ki personal diary (Local: sirf aapke kamre me) vs road par laga hoarding banner (Global: poora shahar dekh sakta hai).",
                "common_mistakes": [
                    {
                        "mistake": "Trying to modify global counter without global keyword: counter += 1 inside function.",
                        "why_it_fails_en": "UnboundLocalError: cannot access local variable 'counter' where it is not associated with a value.",
                        "why_it_fails_hi": "Python use local variable samajhta hai aur shuru me value na hone par crash ho jata hai.",
                        "fix": "Add 'global counter' at the top of the function, or better, pass and return it."
                    }
                ],
                "example_1": {
                    "title": "Local vs Global Scope Demonstration",
                    "title_hi": "Local aur Global scope ka farak",
                    "code": "app_name = 'Elysia'  # Global\n\ndef run():\n    session_id = 'XYZ-123'  # Local\n    print('Inside run():', app_name, session_id)\n\nrun()\nprint('Outside run():', app_name)",
                    "expected_output": "Inside run(): Elysia XYZ-123\nOutside run(): Elysia",
                    "explanation_en": "app_name is visible everywhere; session_id exists only within run().",
                    "explanation_hi": "app_name har jagah dikhta hai; session_id sirf run() ke andar zinda rehta hai."
                },
                "example_2": {
                    "title": "Using the global Keyword",
                    "title_hi": "global keyword se value modify karna",
                    "code": "score = 0\n\ndef add_points(pts):\n    global score\n    score += pts\n\nadd_points(50)\nprint('Updated Global Score:', score)",
                    "expected_output": "Updated Global Score: 50",
                    "explanation_en": "global score explicitly informs Python to modify the module-level variable.",
                    "explanation_hi": "global score se module-level variable update hota hai."
                },
                "challenge": {
                    "prompt_en": "Declare global total = 10. Inside add_five(), use global total and add 5. Call add_five() and print: Total: 15",
                    "prompt_hi": "total = 10 declare karo. add_five() me global total use karke 5 jodo. Function call karke print karo: Total: 15",
                    "starter_code": "total = 10\ndef add_five():\n    # Use global total and add 5:\n    pass\n",
                    "expected_output": "Total: 15",
                    "solution_code": "total = 10\ndef add_five():\n    global total\n    total += 5\n\nadd_five()\nprint(f'Total: {total}')",
                    "solution_explanation_en": "Modifies global total via global keyword.",
                    "solution_explanation_hi": "global keyword se total ko 15 banata hai.",
                    "hints": ["global total\\ntotal += 5"],
                    "ego_roast_hi": "global keyword lagana bhool gaye?",
                    "ego_cheer_hi": "LEGB scope hierarchy mastered! 🌐"
                }
            },
            {
                "id": "ch13_sub2_args_and_kwargs",
                "title": "Handling unknown amounts of data: *args and **kwargs",
                "title_hi": "Anjaan amount ka data handle karna: *args aur **kwargs",
                "icon": "📦",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "*args lets a function accept ANY number of positional arguments (packed into a TUPLE). **kwargs lets a function accept ANY number of keyword arguments (packed into a DICTIONARY).",
                "what_is_it_hi": "*args function ko kitne bhi POSITIONAL arguments lene ki azaadi deta hai (saare arguments ek TUPLE me pack ho jaate hain). **kwargs kitne bhi KEYWORD arguments lene deta hai (saare ek DICTIONARY me pack ho jaate hain).",
                "why_need_it_en": "Built-ins like print(*args) accept 1 item or 100 items! Decorators and web frameworks (Django/Flask) use *args, **kwargs to wrap any arbitrary function cleanly.",
                "why_need_it_hi": "print() function dekha hai? Chahe 1 item do ya 20 items, print sab chala deta hai. Wahi taakat *args aur **kwargs ki hai.",
                "how_to_use_en": "def func(*args, **kwargs): for a in args: ... for k, v in kwargs.items(): ...",
                "how_to_use_hi": "def func(*args, **kwargs): args tuple hai aur kwargs dictionary hai.",
                "syntax": "def super_function(*args, **kwargs):\n    print(\"Positional tuple:\", args)\n    print(\"Keyword dict:\", kwargs)\n\nsuper_function(1, 2, 3, name=\"Alex\", role=\"Admin\")",
                "rules_en": [
                    "The names 'args' and 'kwargs' are conventions; the ASTERISKS (* and **) are the actual magic syntax.",
                    "*args bundles positional arguments into a tuple.",
                    "**kwargs bundles keyword arguments into a dictionary.",
                    "Standard parameter order: def func(required, *args, default=0, **kwargs):"
                ],
                "rules_hi": [
                    "Naam kuch bhi ho sakta hai (*nums), lekin ASTERISK (* aur **) syntax mandatory hai.",
                    "*args saare positional inputs ko TUPLE me pack karta hai.",
                    "**kwargs saare key=value inputs ko DICTIONARY me pack karta hai.",
                    "Order: required pehle, fir *args, fir defaults, fir **kwargs."
                ],
                "analogy_en": "*args is a big backpack where you toss in any number of loose balls. **kwargs is a labeled filing box where you toss in labeled files.",
                "analogy_hi": "*args ek bada jhola hai jisme bina ginti ke jitne chahe samose daal lo. **kwargs ek labeled dabba hai jisme sticker laga kar saman daala jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Placing *args after **kwargs: def f(**kwargs, *args):",
                        "why_it_fails_en": "SyntaxError: invalid syntax. *args MUST always precede **kwargs.",
                        "why_it_fails_hi": "**kwargs hamesha sabse aakhri me aata hai.",
                        "fix": "Always use: def f(*args, **kwargs):"
                    }
                ],
                "example_1": {
                    "title": "Flexible Sum Function with *args",
                    "title_hi": "*args se universal sum function",
                    "code": "def add_all(*numbers):\n    return sum(numbers)\n\nprint('Sum of 2 items:', add_all(10, 20))\nprint('Sum of 4 items:', add_all(1, 2, 3, 4))",
                    "expected_output": "Sum of 2 items: 30\nSum of 4 items: 10",
                    "explanation_en": "add_all accepts any number of integers and sums them seamlessly.",
                    "explanation_hi": "add_all me chahe 2 number pass karo ya 4, sabka sum nikal jata hai."
                },
                "example_2": {
                    "title": "Configuration Builder with **kwargs",
                    "title_hi": "**kwargs se profile builder",
                    "code": "def build_profile(**details):\n    for key, val in details.items():\n        print(f'{key}: {val}')\n\nbuild_profile(user='Alex', status='Active')",
                    "expected_output": "user: Alex\nstatus: Active",
                    "explanation_en": "kwargs captures arbitrary keyword arguments as a dictionary.",
                    "explanation_hi": "kwargs saare key-value pairs ko dictionary me lekar loop chalaata hai."
                },
                "challenge": {
                    "prompt_en": "Define product_all(*nums) that multiplies all passed numbers. Call product_all(2, 3, 4) and print: Product: 24",
                    "prompt_hi": "product_all(*nums) banao jo saare numbers multiply kare. product_all(2, 3, 4) call karke print karo: Product: 24",
                    "starter_code": "# Define product_all(*nums):\n",
                    "expected_output": "Product: 24",
                    "solution_code": "def product_all(*nums):\n    res = 1\n    for n in nums:\n        res *= n\n    return res\n\nans = product_all(2, 3, 4)\nprint(f'Product: {ans}')",
                    "solution_explanation_en": "Iterates over *nums tuple and calculates total product.",
                    "solution_explanation_hi": "*nums ke numbers ko multiply karke product print karta hai.",
                    "hints": ["for n in nums: res *= n"],
                    "ego_roast_hi": "*nums par loop chalana bhool gaye?",
                    "ego_cheer_hi": "Variable argument packing unlocked! 📦"
                }
            },
            {
                "id": "ch13_sub3_docstrings",
                "title": "Writing documentation for your functions (Docstrings)",
                "title_hi": "Functions ki documentation likhna (Docstrings)",
                "icon": "📖",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A docstring (documentation string) is a multi-line string (\"\"\"...\"\"\") placed as the very first statement inside a function, class, or module. Python binds it to the function's __doc__ attribute and powers the interactive help() system.",
                "what_is_it_hi": "Docstring function ke andar sabse pehli line par likhi gayi triple-quoted string (\"\"\") hoti hai. Python ise function ke __doc__ attribute me save karta hai aur jab koi help(my_func) chalata hai to yahi documentation dikhti hai.",
                "why_need_it_en": "When team members hover over your function in VS Code, the docstring pops up as the official API manual showing what arguments are expected and what is returned.",
                "why_need_it_hi": "VS Code me jab koi aapke function par mouse le jata hai to ye docstring use batati hai ki function kya karta hai aur kya return karega.",
                "how_to_use_en": "Write triple quotes right under def. Document Parameters and Returns.",
                "how_to_use_hi": "def ke theek neeche triple quotes lagao.",
                "syntax": "def calculate_interest(principal, rate, years):\n    \"\"\"\n    Calculate simple interest for a loan.\n\n    Args:\n        principal (float): Initial loan amount\n        rate (float): Annual interest percentage\n        years (int): Duration in years\n\n    Returns:\n        float: Total computed interest\n    \"\"\"\n    return (principal * rate * years) / 100",
                "rules_en": [
                    "PEP 257 Standard: First line should be a concise summary ending with a period.",
                    "Accessed at runtime via func.__doc__ or help(func).",
                    "Docstrings are permanent metadata, whereas comments (#) are stripped out during bytecode compilation."
                ],
                "rules_hi": [
                    "PEP 257 Niyam: Pehli line ek saaf summary honi chahiye.",
                    "Code me func.__doc__ ya help(func) se read kiya ja sakta hai.",
                    "Comments (#) bytecode me delete ho jaate hain, lekin Docstring memory me safe rehti hai."
                ],
                "analogy_en": "A medicine bottle label: It tells the pharmacist the dosage (parameters), effect (description), and expiration date (metadata).",
                "analogy_hi": "Dawai ki shishi par laga label — kitni boond leni hai (parameters), kya asar hoga (returns).",
                "common_mistakes": [
                    {
                        "mistake": "Placing the docstring after the first line of code inside the function.",
                        "why_it_fails_en": "It becomes a regular unused string literal and is NOT bound to __doc__.",
                        "why_it_fails_hi": "Docstring function ki sabse pehli line honi chahiye, warna wo normal string ban kar ignore ho jayegi.",
                        "fix": "Always place docstrings immediately under the 'def' line."
                    }
                ],
                "example_1": {
                    "title": "Accessing __doc__ Attribute Programmatically",
                    "title_hi": "__doc__ attribute se documentation padhna",
                    "code": "def add(a, b):\n    \"\"\"Return the mathematical sum of a and b.\"\"\"\n    return a + b\n\nprint('Docstring:', add.__doc__)",
                    "expected_output": "Docstring: Return the mathematical sum of a and b.",
                    "explanation_en": "add.__doc__ extracts the runtime documentation cleanly.",
                    "explanation_hi": "add.__doc__ se function ki saved documentation print hoti hai."
                },
                "example_2": {
                    "title": "Multiline Google-Style Docstring",
                    "title_hi": "Professional multiline docstring",
                    "code": "def greet(name):\n    \"\"\"\n    Greet a user warmly.\n    Args: name (str)\n    \"\"\"\n    return f'Hello, {name}'\n\nprint('Clean extraction:', 'Greet a user' in greet.__doc__)",
                    "expected_output": "Clean extraction: True",
                    "explanation_en": "Confirms presence of structured documentation.",
                    "explanation_hi": "Structured documentation ki presence verify karta hai."
                },
                "challenge": {
                    "prompt_en": "Define a function cube(n) with docstring 'Return cube of n.' and print cube.__doc__.",
                    "prompt_hi": "cube(n) function banao jisme docstring ho 'Return cube of n.' aur print karo cube.__doc__.",
                    "starter_code": "# Define cube with docstring:\n",
                    "expected_output": "Return cube of n.",
                    "solution_code": "def cube(n):\n    \"\"\"Return cube of n.\"\"\"\n    return n ** 3\n\nprint(cube.__doc__)",
                    "solution_explanation_en": "Extracts docstring from cube.__doc__.",
                    "solution_explanation_hi": "cube.__doc__ se docstring print karta hai.",
                    "hints": ["def cube(n):\\n    \"\"\"Return cube of n.\"\"\"\\n    return n ** 3"],
                    "ego_roast_hi": "Triple quotes docstring lagana bhool gaye?",
                    "ego_cheer_hi": "Professional API documentation authored! 📖"
                }
            },
            {
                "id": "ch13_sub4_lambda_functions",
                "title": "One-line mini functions (Lambda functions)",
                "title_hi": "One-line mini functions (Lambda functions)",
                "icon": "⚡",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A lambda function is a small, anonymous (unnamed) single-line function defined with the 'lambda' keyword: lambda arguments: expression. It automatically returns the result of the expression without needing a 'return' keyword.",
                "what_is_it_hi": "Lambda function ek chhota sa bina naam ka 1-line function hota hai jo 'lambda' keyword se banta hai: lambda arguments: expression. Isme 'return' likhne ki zarurat nahi hoti, ye expression ka result apne aap return karta hai.",
                "why_need_it_en": "Throwaway helper functions: sorting lists by a custom sub-key (sorted(users, key=lambda u: u['age'])), or inline callbacks.",
                "why_need_it_hi": "Jab sirf ek line ke chhota sa function chahiye ho jise poori file me dobara kabhi use nahi karna (jaise custom sorting).",
                "how_to_use_en": "sq = lambda x: x ** 2 -> sq(5) returns 25.",
                "how_to_use_hi": "add = lambda a, b: a + b -> add(3, 4).",
                "syntax": "# Traditional function:\ndef double(x):\n    return x * 2\n\n# Equivalent Lambda one-liner:\ndouble_lambda = lambda x: x * 2",
                "rules_en": [
                    "Lambdas can take any number of arguments, but can contain ONLY ONE single expression.",
                    "No statements (like if/else blocks, loops, or assignments) are allowed inside lambdas (only ternary if: x if c else y).",
                    "Do NOT use the 'return' keyword inside a lambda (the expression is returned automatically).",
                    "PEP 8 recommendation: if you are assigning a lambda to a variable name, use 'def' instead."
                ],
                "rules_hi": [
                    "Lambda me kitne bhi arguments ho sakte hain lekin sirf EK expression ho sakti hai.",
                    "Lambda ke andar loops ya multiline statements allow nahi hote.",
                    "Lambda me 'return' keyword nahi likha jata, wo automatically return karta hai.",
                    "PEP 8 ke mutabiq agar function ko naam dena hai to 'def' use karo."
                ],
                "analogy_en": "A disposable paper cup: you use it once for a quick sip of water at a dispenser and throw it away, rather than bringing out fine ceramic china.",
                "analogy_hi": "Use-and-throw paper cup jaisa — ek baar paani piya aur phenk diya, bartan dhone ki headache nahi.",
                "common_mistakes": [
                    {
                        "mistake": "Writing 'return' inside a lambda: lambda x: return x * 2",
                        "why_it_fails_en": "SyntaxError: invalid syntax. return is implicit in lambdas.",
                        "why_it_fails_hi": "Lambda me return likhne par SyntaxError aata hai.",
                        "fix": "Remove 'return': lambda x: x * 2."
                    }
                ],
                "example_1": {
                    "title": "Sorting a List of Tuples by Second Element",
                    "title_hi": "Second element se sorting lambda use karke",
                    "code": "students = [('Rohan', 85), ('Aman', 95), ('Pooja', 78)]\n# Sort by marks (index 1)\nstudents.sort(key=lambda s: s[1], reverse=True)\nprint('Leaderboard:', students)",
                    "expected_output": "Leaderboard: [('Aman', 95), ('Rohan', 85), ('Pooja', 78)]",
                    "explanation_en": "lambda s: s[1] extracts the mark from each tuple as the sorting key.",
                    "explanation_hi": "lambda s: s[1] har tuple ka marks nikaal kar descending sort karata hai."
                },
                "example_2": {
                    "title": "Ternary Conditional Inside Lambda",
                    "title_hi": "Ternary if-else lambda ke andar",
                    "code": "check_adult = lambda age: 'Adult' if age >= 18 else 'Minor'\nprint('Age 20 is:', check_adult(20))\nprint('Age 15 is:', check_adult(15))",
                    "expected_output": "Age 20 is: Adult\nAge 15 is: Minor",
                    "explanation_en": "Evaluates conditional expression inline.",
                    "explanation_hi": "Inline conditional expression evaluate karta hai."
                },
                "challenge": {
                    "prompt_en": "Create a lambda multiply = lambda a, b: a * b. Print multiply(4, 5): 20",
                    "prompt_hi": "multiply = lambda a, b: a * b banao aur multiply(4, 5) print karo: 20",
                    "starter_code": "# Create and call lambda:\n",
                    "expected_output": "20",
                    "solution_code": "multiply = lambda a, b: a * b\nprint(multiply(4, 5))",
                    "solution_explanation_en": "Executes lambda with arguments 4 and 5.",
                    "solution_explanation_hi": "Lambda multiply karke 20 deta hai.",
                    "hints": ["multiply = lambda a, b: a * b\\nprint(multiply(4, 5))"],
                    "ego_roast_hi": "lambda syntax bhool gaye?",
                    "ego_cheer_hi": "One-line anonymous lambda mastered! ⚡"
                }
            },
            {
                "id": "ch13_sub5_map_filter_zip",
                "title": "Applying functions to lists: map(), filter(), and zip()",
                "title_hi": "Lists par functions apply karna: map(), filter(), aur zip()",
                "icon": "⚙️",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Functional programming trios: map(func, iter) applies a transformation function to EVERY element; filter(func, iter) keeps only elements where func returns True; zip(iter1, iter2) stitches elements from two collections together into pairs like a zipper.",
                "what_is_it_hi": "Python ke 3 functional superpowers: map() list ke HAR ITEM par function chalaata hai; filter() sirf un items ko RAKHTA HAI jo True pass hote hain; zip() do alag lists ko chain (zipper) ki tarah aapas me jod deta hai.",
                "why_need_it_en": "Data pipelines: converting string prices to floats (map), removing inactive users (filter), and pairing student names with roll numbers (zip).",
                "why_need_it_hi": "Strings ko numbers me badalna (map), pass students ko filter karna (filter), names aur roll numbers ko jodi me banana (zip).",
                "how_to_use_en": "list(map(int, ['1', '2'])), list(filter(lambda x: x > 0, nums)), list(zip(names, scores)).",
                "how_to_use_hi": "list(map(str.upper, names)), list(filter(lambda x: x % 2 == 0, nums)), list(zip(a, b)).",
                "syntax": "# map:\ndoubled = list(map(lambda x: x * 2, [1, 2, 3]))  # [2, 4, 6]\n# filter:\nevens = list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4])) # [2, 4]\n# zip:\npaired = list(zip([\"A\", \"B\"], [10, 20])) # [('A', 10), ('B', 20)]",
                "rules_en": [
                    "map() and filter() return lazy iterators! You must wrap with list() to see the concrete list result.",
                    "zip() stops at the length of the SHORTEST iterable (to prevent out-of-bounds mismatches).",
                    "zip(*paired) unzips paired tuples back into two separate collections."
                ],
                "rules_hi": [
                    "map() aur filter() lazy iterators return karte hain, list dekhne ke liye list() me wrap karna padta hai.",
                    "zip() sabse chhoti list ki length par ruk jata hai.",
                    "zip(*paired) do lists ko wapas alag-alag un-zip kar deta hai."
                ],
                "analogy_en": "map is an assembly line painter spraying red on every toy. filter is a quality-control inspector throwing away broken toys. zip is a jacket zipper interlocking teeth from left and right.",
                "analogy_hi": "map assembly line worker hai jo har item par paint karta hai. filter inspector hai jo kharab items ko filter karta hai. zip jacket ki chain hai jo dono sides ko jodti hai.",
                "common_mistakes": [
                    {
                        "mistake": "Printing map directly: print(map(int, ['1', '2']))",
                        "why_it_fails_en": "Outputs <map object at 0x...>. map is a lazy generator iterator.",
                        "why_it_fails_hi": "map lazy iterator hota hai, direct print karne par memory address dikhta hai.",
                        "fix": "Cast to list: print(list(map(int, ['1', '2'])))."
                    }
                ],
                "example_1": {
                    "title": "Map and Filter in Action",
                    "title_hi": "map aur filter ka use",
                    "code": "nums = [1, 2, 3, 4, 5]\n# Double all numbers\ndoubles = list(map(lambda x: x * 2, nums))\n# Filter evens only\nevens = list(filter(lambda x: x % 2 == 0, nums))\nprint('Doubles (map):', doubles)\nprint('Evens (filter):', evens)",
                    "expected_output": "Doubles (map): [2, 4, 6, 8, 10]\nEvens (filter): [2, 4]",
                    "explanation_en": "map transforms every number; filter retains only even numbers.",
                    "explanation_hi": "map ne har number ko double kiya; filter ne sirf even numbers rakhe."
                },
                "example_2": {
                    "title": "Pairing Data with zip()",
                    "title_hi": "zip() se names aur marks jodna",
                    "code": "names = ['Alice', 'Bob']\nmarks = [95, 85]\nreport = list(zip(names, marks))\nprint('Paired report card:', report)",
                    "expected_output": "Paired report card: [('Alice', 95), ('Bob', 85)]",
                    "explanation_en": "Pairs corresponding indices into tuples.",
                    "explanation_hi": "Dono lists ko aapas me pair karke tuples banata hai."
                },
                "challenge": {
                    "prompt_en": "Given words = ['a', 'b', 'c'], use list(map(str.upper, words)) and print: ['A', 'B', 'C']",
                    "prompt_hi": "words = ['a', 'b', 'c'] par list(map(str.upper, words)) chala kar print karo: ['A', 'B', 'C']",
                    "starter_code": "words = ['a', 'b', 'c']\n# Use map with str.upper and print:\n",
                    "expected_output": "['A', 'B', 'C']",
                    "solution_code": "words = ['a', 'b', 'c']\nprint(list(map(str.upper, words)))",
                    "solution_explanation_en": "Maps str.upper over every item and converts to list.",
                    "solution_explanation_hi": "str.upper map karke uppercase list print karta hai.",
                    "hints": ["list(map(str.upper, words))"],
                    "ego_roast_hi": "map() ko list() me wrap karna bhool gaye?",
                    "ego_cheer_hi": "Functional programming pipeline mastered! ⚙️"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 14: Borrowing Code (Modules and Packages)
    # =========================================================================
    {
        "id": "ch14_modules_packages",
        "part_number": 4,
        "part_title": "PART 4: WORKING SMART, NOT HARD (FUNCTIONS & MODULARITY)",
        "chapter_number": 14,
        "title": "Chapter 14: Borrowing Code (Modules and Packages)",
        "subtitle_en": "Code reuse, import syntax, standard library (math, random, time, os), and pip package manager",
        "subtitle_hi": "Code reuse, import syntax, standard library (math, random, os) aur pip package manager",
        "icon": "📦",
        "estimated_time": "35 mins",
        "prerequisites_en": "Chapters 12 & 13 (Functions).",
        "prerequisites_hi": "Chapter 12 aur 13 (Functions).",
        "learning_objectives_en": [
            "Understand modules as reusable .py code files",
            "Master import syntax variations (import, from ... import ..., as nickname)",
            "Explore Python's built-in 'batteries included' Standard Library (math, random, time, os)",
            "Understand third-party package management via pip and PyPI"
        ],
        "learning_objectives_hi": [
            "Modules ka concept samjho (.py files reuse karna)",
            "import syntax ke alag-alag forms (import, from, as)",
            "Python ki 'batteries included' Standard Library (math, random, os)",
            "pip aur PyPI se third-party packages install karna"
        ],
        "recap_en": "You mastered modular Python: importing modules, aliasing, using the standard library, and package management with pip.",
        "recap_hi": "Aapne code modularity, import statements, standard library aur pip package ecosystem master kiya.",
        "subtopics": [
            {
                "id": "ch14_sub1_what_is_a_module",
                "title": "What is a module? (Reusing code from other files)",
                "title_hi": "Module kya hota hai? (Doosri files se code reuse karna)",
                "icon": "📁",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A module is simply a Python file (.py) containing functions, classes, and variables. Any .py file you save can instantly be imported into any other .py file using the 'import' statement.",
                "what_is_it_hi": "Module bas ek simple Python file (.py) hoti hai jisme functions aur variables likhe hote hain. Aapki banayi hui koi bhi .py file doosri file me 'import' karke reuse ki ja sakti hai.",
                "why_need_it_en": "Modularity: A 10,000-line monolithic script is a nightmare to maintain. Splitting code into database.py, auth.py, and routes.py keeps software organized and testable.",
                "why_need_it_hi": "Agar saara code ek hi 10,000 line ki file me likhoge to dimaag kharab ho jayega. Code ko auth.py, db.py alag files me baant kar import karna best practice hai.",
                "how_to_use_en": "Save helper.py with def greet(): pass. In main.py, type: import helper; helper.greet().",
                "how_to_use_hi": "helper.py banao, main.py me import helper likh kar use karo.",
                "syntax": "# In math_tools.py:\ndef square(n): return n * n\n\n# In main.py:\nimport math_tools\nprint(math_tools.square(5))",
                "rules_en": [
                    "A module is executed the FIRST time it is imported.",
                    "Python searches for modules in sys.path: current directory first, then installed site-packages, then standard library.",
                    "Avoid circular imports (file A imports B while B imports A)."
                ],
                "rules_hi": [
                    "Pehli baar import hone par module ka code execute hota hai.",
                    "Python pehle current folder me dhoondta hai, fir standard library me.",
                    "Circular import (A imports B aur B imports A) se bacho."
                ],
                "analogy_en": "A toolkit with modular compartments: instead of carrying a massive 50kg steel toolbox everywhere, you grab just the screwdriver box when needed.",
                "analogy_hi": "Toolkit ke alag-alag dabbe: plumbing ka dabba alag, electrical ka alag. Jab jo chahiye bas wahi dabba import karo.",
                "common_mistakes": [
                    {
                        "mistake": "Naming your file the same as a standard library module: saving your script as 'math.py' or 'random.py'.",
                        "why_it_fails_en": "Python imports your local empty math.py instead of the real math library, causing AttributeError: module 'math' has no attribute 'sqrt'!",
                        "why_it_fails_hi": "Apni file ka naam 'math.py' rakh diya to Python official math library load hi nahi karega aur crash ho jayega.",
                        "fix": "Never name your files after Python built-in modules."
                    }
                ],
                "example_1": {
                    "title": "Inspecting Module Properties",
                    "title_hi": "Module ka naam aur file location",
                    "code": "import sys\nprint('sys module name:', sys.__name__)\nprint('Module type:', type(sys).__name__)",
                    "expected_output": "sys module name: sys\nModule type: module",
                    "explanation_en": "sys is a built-in module object loaded in memory.",
                    "explanation_hi": "sys ek real module object hai jo memory me load hota hai."
                },
                "example_2": {
                    "title": "Namespace Isolation",
                    "title_hi": "Namespace collision se bachna",
                    "code": "import math\npi = 3  # Local variable\nprint('Local pi:', pi)\nprint('Module math.pi:', round(math.pi, 4))",
                    "expected_output": "Local pi: 3\nModule math.pi: 3.1416",
                    "explanation_en": "math.pi and local pi live in separate isolated namespaces.",
                    "explanation_hi": "math.pi aur local pi do alag namespaces me rehte hain bina ladai ke."
                },
                "challenge": {
                    "prompt_en": "Import the sys module and print its active platform: print('Platform:', sys.platform is not None)",
                    "prompt_hi": "sys module import karke print karo: Platform: True",
                    "starter_code": "# Import sys and print:\n",
                    "expected_output": "Platform: True",
                    "solution_code": "import sys\nprint(f'Platform: {sys.platform is not None}')",
                    "solution_explanation_en": "Imports sys and verifies sys.platform.",
                    "solution_explanation_hi": "sys import karke platform check karta hai.",
                    "hints": ["import sys\\nprint(f'Platform: {sys.platform is not None}')"],
                    "ego_roast_hi": "import sys likhna bhool gaye?",
                    "ego_cheer_hi": "Module architecture validated! 📁"
                }
            },
            {
                "id": "ch14_sub2_import_whole_module",
                "title": "Importing whole modules (import math)",
                "title_hi": "Poora module import karna (import math)",
                "icon": "📦",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "'import module_name' loads the entire module and places its name into your local scope as a namespace. To use any function or constant from it, prefix with the module name: math.sqrt(16) or math.pi.",
                "what_is_it_hi": "'import math' poora module load karta hai. Uske functions use karne ke liye module ka naam aage lagana padta hai: math.sqrt(25) ya math.pi.",
                "why_need_it_en": "Namespace Safety: Prefixing math.sqrt makes it crystal clear where the function came from, preventing name collisions with functions you wrote.",
                "why_need_it_hi": "Isse pata rehta hai ki ye function math module se aaya hai, aapke code se nahi.",
                "how_to_use_en": "import math; result = math.sqrt(25).",
                "how_to_use_hi": "import math; ans = math.sqrt(25).",
                "syntax": "import math\n\nroot = math.sqrt(49)    # 7.0\nfloored = math.floor(4.9) # 4",
                "rules_en": [
                    "Everything inside the module must be accessed using the dot operator: module.function().",
                    "Imports should be placed at the very top of your file (PEP 8 standard).",
                    "Multiple imports should be on separate lines (import math \\n import sys)."
                ],
                "rules_hi": [
                    "Functions use karne ke liye dot lagana padta hai: module.func().",
                    "Hamesha file ke sabse upar imports likho (PEP 8).",
                    "Har import ko alag line par likho."
                ],
                "analogy_en": "Buying an entire Swiss Army Knife: to use the scissors, you pull them out from the knife body (knife.scissors).",
                "analogy_hi": "Poora Swiss Army knife khareedne jaisa — scissor nikaalni hai to knife.scissor bolte ho.",
                "common_mistakes": [
                    {
                        "mistake": "Calling sqrt(16) after writing 'import math'.",
                        "why_it_fails_en": "NameError: name 'sqrt' is not defined. You imported math, not bare sqrt.",
                        "why_it_fails_hi": "Prefix lagana bhool gaye. Python ko sqrt seedhe nahi dikhta.",
                        "fix": "Call math.sqrt(16)."
                    }
                ],
                "example_1": {
                    "title": "Using the Built-in math Module",
                    "title_hi": "math module ke functions",
                    "code": "import math\nprint('Square root of 64:', math.sqrt(64))\nprint('Ceiling of 4.1:', math.ceil(4.1))\nprint('Floor of 4.9:', math.floor(4.9))",
                    "expected_output": "Square root of 64: 8.0\nCeiling of 4.1: 5\nFloor of 4.9: 4",
                    "explanation_en": "Calls math.sqrt, math.ceil, and math.floor cleanly.",
                    "explanation_hi": "Square root (8.0), ceiling (5), aur floor (4) calculate karta hai."
                },
                "example_2": {
                    "title": "Constants Inside math",
                    "title_hi": "math module ke constants",
                    "code": "import math\nprint('Pi constant:', round(math.pi, 2))\nprint('Euler constant:', round(math.e, 2))",
                    "expected_output": "Pi constant: 3.14\nEuler constant: 2.72",
                    "explanation_en": "Accesses math constants pi and e.",
                    "explanation_hi": "math ke constants pi aur e read karta hai."
                },
                "challenge": {
                    "prompt_en": "Import math and calculate square root of 81 using math.sqrt(81). Print: Root: 9.0",
                    "prompt_hi": "math import karo aur math.sqrt(81) nikaal kar print karo: Root: 9.0",
                    "starter_code": "# Import math and calculate sqrt:\n",
                    "expected_output": "Root: 9.0",
                    "solution_code": "import math\nprint(f'Root: {math.sqrt(81)}')",
                    "solution_explanation_en": "Uses math.sqrt(81) to get 9.0.",
                    "solution_explanation_hi": "math.sqrt(81) se 9.0 print karta hai.",
                    "hints": ["import math\\nprint(f'Root: {math.sqrt(81)}')"],
                    "ego_roast_hi": "math.sqrt call karna bhool gaye?",
                    "ego_cheer_hi": "Whole module import verified! 📦"
                }
            },
            {
                "id": "ch14_sub3_import_specific_parts",
                "title": "Importing specific parts (from random import randint)",
                "title_hi": "Specific parts import karna (from random import randint)",
                "icon": "🎯",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "'from module import symbol' imports ONLY the specified function, class, or constant directly into your local namespace. You can call it directly without typing the module prefix: randint(1, 6) instead of random.randint(1, 6).",
                "what_is_it_hi": "'from module import function' se aap poora module lene ke bajaye sirf wahi EK specific cheez nikaalte ho jo chahiye. Isse prefix lagane ki zarurat nahi padti: seedhe randint(1, 6) likh sakte ho.",
                "why_need_it_en": "Conciseness: If you use a function 50 times in a script, typing sqrt(x) is cleaner than math.sqrt(x).",
                "why_need_it_hi": "Agar koi function baar baar use ho raha hai to baar baar module. lagane se bachata hai.",
                "how_to_use_en": "from math import sqrt, pi -> print(sqrt(25)).",
                "how_to_use_hi": "from math import sqrt, pi -> print(sqrt(25)).",
                "syntax": "from random import randint, choice\n\nroll = randint(1, 6)  # Direct call without 'random.' prefix!\npick = choice([\"A\", \"B\", \"C\"])",
                "rules_en": [
                    "You can import multiple specific symbols separated by commas: from math import sqrt, ceil, floor.",
                    "AVOID wildcard imports: 'from math import *' pollutes your local scope and overwrites existing variable names.",
                    "The imported symbol becomes a direct member of the current file's namespace."
                ],
                "rules_hi": [
                    "Comma laga kar multiple specific cheezein import kar sakte ho.",
                    "Wildcard 'from math import *' STRICTLY AVOID karo kyunki ye namespace kharab kar deta hai.",
                    "Imported function seedhe call ho sakta hai bina prefix ke."
                ],
                "analogy_en": "Instead of bringing the entire toolbox to the roof, you take just the 10mm wrench out of the box and put it in your pocket.",
                "analogy_hi": "Poora tool dabba chhat par le jaane ke bajaye sirf zaroori paana (wrench) nikaal kar jeb me rakh lena.",
                "common_mistakes": [
                    {
                        "mistake": "Using 'from module import *' (wildcard import).",
                        "why_it_fails_en": "Pollutes the global namespace with hundreds of unknown names, leading to silent variable collisions.",
                        "why_it_fails_hi": "Hazaaron unknown functions local namespace me ghus jaate hain aur bugs laate hain.",
                        "fix": "Always import specific names explicitly: from module import specific_func."
                    }
                ],
                "example_1": {
                    "title": "Direct Invocation with from-import",
                    "title_hi": "Direct call without prefix",
                    "code": "from math import sqrt, pi\nprint('Direct sqrt:', sqrt(100))\nprint('Direct pi:', round(pi, 2))",
                    "expected_output": "Direct sqrt: 10.0\nDirect pi: 3.14",
                    "explanation_en": "sqrt and pi are called directly without 'math.' prefix.",
                    "explanation_hi": "Bina 'math.' likhe seedhe sqrt aur pi call karta hai."
                },
                "example_2": {
                    "title": "Random Dice Roll Simulation",
                    "title_hi": "Dice roll simulation randint se",
                    "code": "from random import randint\n# Dice roll between 1 and 6\nroll = randint(1, 6)\nprint('Dice roll between 1 and 6:', 1 <= roll <= 6)",
                    "expected_output": "Dice roll between 1 and 6: True",
                    "explanation_en": "randint(1, 6) produces an integer in range [1, 6] inclusive.",
                    "explanation_hi": "randint(1, 6) 1 se 6 ke beech ka number generate karta hai."
                },
                "challenge": {
                    "prompt_en": "Use 'from math import ceil' to round 7.2 up and print: Ceil: 8",
                    "prompt_hi": "'from math import ceil' use karke ceil(7.2) nikaalo aur print karo: Ceil: 8",
                    "starter_code": "# Use from-import for ceil:\n",
                    "expected_output": "Ceil: 8",
                    "solution_code": "from math import ceil\nprint(f'Ceil: {ceil(7.2)}')",
                    "solution_explanation_en": "Imports ceil and calls ceil(7.2) = 8.",
                    "solution_explanation_hi": "ceil(7.2) 8 return karta hai.",
                    "hints": ["from math import ceil\\nprint(f'Ceil: {ceil(7.2)}')"],
                    "ego_roast_hi": "from ... import ... syntax bhool gaye?",
                    "ego_cheer_hi": "Selective symbol import verified! 🎯"
                }
            },
            {
                "id": "ch14_sub4_aliasing_modules",
                "title": "Giving modules nicknames (import datetime as dt)",
                "title_hi": "Modules ko nicknames dena (import datetime as dt)",
                "icon": "🏷️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The 'as' keyword lets you assign an alias (short nickname) to an imported module or function. This saves typing and adheres to standard community conventions.",
                "what_is_it_hi": "'as' keyword se aap kisi lambe module ko chhota nickname de dete ho. Jaise 'import datetime as dt' ya Data Science me 'import numpy as np'.",
                "why_need_it_en": "Typing datetime.datetime.now() is verbose; dt.datetime.now() is clean. Universal industry standards: import pandas as pd, import numpy as np, import matplotlib.pyplot as plt.",
                "why_need_it_hi": "Lamba naam baar baar type karne se bachata hai aur industry ke standard conventions follow karta hai (np, pd, dt).",
                "how_to_use_en": "import module as alias -> import datetime as dt.",
                "how_to_use_hi": "import datetime as dt.",
                "syntax": "import datetime as dt\nimport math as m\n\nval = m.sqrt(25)  # Uses short alias 'm'",
                "rules_en": [
                    "Once you alias a module, you MUST use the alias! The original name is no longer accessible in that scope.",
                    "Follow established community aliases (np, pd, plt, tf, dt). Avoid random obscure abbreviations.",
                    "You can also alias specific functions: from math import factorial as fact."
                ],
                "rules_hi": [
                    "Nickname dene ke baad original naam se call nahi kar sakte, nickname hi use karna padega.",
                    "Industry ke standard nicknames hi use karo (np, pd, dt).",
                    "Functions ko bhi nickname de sakte ho: from math import sqrt as s."
                ],
                "analogy_en": "Calling your friend 'Alexander' by his short nickname 'Alex'. Everyone knows who you mean, and it takes 3x less time to say.",
                "analogy_hi": "Dost ka official lamba naam 'Priyanshu' hone par use 'Prince' bolna — sabko pata hai kiski baat ho rahi hai.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to use the original module name after aliasing: import math as m; print(math.sqrt(4))",
                        "why_it_fails_en": "NameError: name 'math' is not defined. The alias 'm' replaced 'math' in local scope.",
                        "why_it_fails_hi": "Nickname 'm' ban gaya hai to 'math' ab exist hi nahi karta.",
                        "fix": "Use the alias: m.sqrt(4)."
                    }
                ],
                "example_1": {
                    "title": "Aliasing the Datetime Module",
                    "title_hi": "datetime ko dt nickname dena",
                    "code": "import datetime as dt\nnow = dt.date(2026, 10, 12)\nprint('Formatted Date via dt alias:', now)",
                    "expected_output": "Formatted Date via dt alias: 2026-10-12",
                    "explanation_en": "Accesses datetime via short alias dt.",
                    "explanation_hi": "dt alias use karke date format karta hai."
                },
                "example_2": {
                    "title": "Aliasing Specific Functions to Resolve Conflicts",
                    "title_hi": "Name conflict solve karne ke liye alias",
                    "code": "from math import sqrt as square_root\nprint('Calculated via alias:', square_root(36))",
                    "expected_output": "Calculated via alias: 6.0",
                    "explanation_en": "Renames sqrt to square_root locally.",
                    "explanation_hi": "sqrt ko square_root naam se alias kiya."
                },
                "challenge": {
                    "prompt_en": "Import math as m, calculate m.floor(9.8), and print: Floored: 9",
                    "prompt_hi": "math as m import karo aur m.floor(9.8) nikaal kar print karo: Floored: 9",
                    "starter_code": "# Import with alias and print:\n",
                    "expected_output": "Floored: 9",
                    "solution_code": "import math as m\nprint(f'Floored: {m.floor(9.8)}')",
                    "solution_explanation_en": "Uses 'as m' alias to call m.floor(9.8).",
                    "solution_explanation_hi": "m.floor(9.8) call karke print karta hai.",
                    "hints": ["import math as m\\nprint(f'Floored: {m.floor(9.8)}')"],
                    "ego_roast_hi": "as m lagana bhool gaye?",
                    "ego_cheer_hi": "Module aliasing verified! 🏷️"
                }
            },
            {
                "id": "ch14_sub5_standard_library",
                "title": "Exploring Python's built-in Standard Library (math, random, time, os)",
                "title_hi": "Python ki built-in Standard Library (math, random, time, os)",
                "icon": "🔋",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Python's philosophy is 'Batteries Included'. The official runtime ships with over 200 powerful built-in modules ready to use with zero downloads: math, random, time, os, sys, json, csv, re, sqlite3, and more.",
                "what_is_it_hi": "Python ka famous nara hai 'Batteries Included' — iska matlab bina kuch alag se download kiye Python ke sath 200 se zyada powerful libraries free milti hain: math, random, time, os, sys, json, csv sab built-in hain!",
                "why_need_it_en": "You don't need third-party packages to manipulate files (os), format timestamps (time), roll dice (random), or parse JSON web data (json).",
                "why_need_it_hi": "Files read karna (os), timer lagana (time), lottery number nikaalna (random), web data parse karna (json) — sab pehle se ready hai.",
                "how_to_use_en": "Just write 'import time' or 'import os' anywhere; no pip install needed.",
                "how_to_use_hi": "Direct 'import os' ya 'import time' likho.",
                "syntax": "import math    # Advanced trigonometry, logs, sqrt\nimport random  # Random numbers, shuffling, sampling\nimport time    # Timestamps, delays, benchmarking\nimport os      # File paths, directories, environment vars",
                "rules_en": [
                    "Standard library modules require NO internet connection or pip commands.",
                    "They are rigorously tested, backwards-compatible, and written in C for performance.",
                    "Consult official docs at docs.python.org/3/library/."
                ],
                "rules_hi": [
                    "Standard library ke liye internet ya pip install ki zarurat nahi hoti.",
                    "Ye C language me likhe hote hain isliye superfast aur secure hote hain.",
                    "Official Python documentation me sabka pura guide maujood hai."
                ],
                "analogy_en": "Buying a smartphone that comes with a built-in camera, calculator, clock, and file manager right out of the factory box.",
                "analogy_hi": "Naya smartphone lene jaisa — camera, calculator, clock aur notes app pehle se factory installed milti hain.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to run 'pip install math' or 'pip install random'.",
                        "why_it_fails_en": "Fails because standard library modules are already built into the core Python interpreter.",
                        "why_it_fails_hi": "Built-in cheezon ko pip install karne ki zarurat nahi hoti.",
                        "fix": "Just write 'import math' directly."
                    }
                ],
                "example_1": {
                    "title": "Random Sampling and Shuffling",
                    "title_hi": "Random choices aur shuffling",
                    "code": "import random\ncards = ['Ace', 'King', 'Queen']\npicked = random.choice(cards)\nprint('Random card picked is valid:', picked in cards)",
                    "expected_output": "Random card picked is valid: True",
                    "explanation_en": "random.choice picks a random element from the list.",
                    "explanation_hi": "random.choice list me se random card select karta hai."
                },
                "example_2": {
                    "title": "Time and OS Inspection",
                    "title_hi": "Time formatting aur path separator",
                    "code": "import time\nimport os\nprint('Path separator on OS:', repr(os.sep))\nprint('Time epoch is active:', time.time() > 0)",
                    "expected_output": "Path separator on OS: '/'\nTime epoch is active: True",
                    "explanation_en": "os.sep gives the OS path separator ('/' on Unix, '\\\\' on Windows).",
                    "explanation_hi": "os.sep operating system ka path separator batata hai."
                },
                "challenge": {
                    "prompt_en": "Import os and print whether os.name exists: OS active: True",
                    "prompt_hi": "os import karke print karo: OS active: True",
                    "starter_code": "# Import os and print:\n",
                    "expected_output": "OS active: True",
                    "solution_code": "import os\nprint(f'OS active: {os.name is not None}')",
                    "solution_explanation_en": "Checks os.name validity.",
                    "solution_explanation_hi": "os module se operating system check karta hai.",
                    "hints": ["import os\\nprint(f'OS active: {os.name is not None}')"],
                    "ego_roast_hi": "os module import karna bhool gaye?",
                    "ego_cheer_hi": "Standard library exploration verified! 🔋"
                }
            },
            {
                "id": "ch14_sub6_pip_packages",
                "title": "Installing third-party code using pip (The Python Package Index)",
                "title_hi": "pip se third-party packages install karna (PyPI)",
                "icon": "🌐",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "'pip' (Pip Installs Packages) is the official package manager for Python. It connects to PyPI (Python Package Index — pypi.org), an online warehouse of over 500,000 open-source libraries (like requests, numpy, pandas, flask, fastapi).",
                "what_is_it_hi": "'pip' Python ka official package manager hai. Ye PyPI (Python Package Index) se connect karta hai jahan duniya bhar ke coders ne 5,00,000 se zyada open-source libraries (jaise requests, pandas, flask) daal rakhi hain.",
                "why_need_it_en": "Why reinvent the wheel? To make HTTP requests to web servers, send WhatsApp messages, or build machine learning models, one command 'pip install requests' gives you instant superpowers.",
                "why_need_it_hi": "Duniya bhar ke super-engineers ka banaya hua code aap sirf 1 command 'pip install package_name' likh kar apne project me use kar sakte ho.",
                "how_to_use_en": "In terminal: pip install requests. To save dependencies: pip freeze > requirements.txt.",
                "how_to_use_hi": "Terminal me likho: pip install package_name. Requirements file ke liye: pip freeze > requirements.txt.",
                "syntax": "# In terminal (NOT in python code!):\npip install requests\npip install numpy pandas\npip list\npip uninstall requests",
                "rules_en": [
                    "CRITICAL LAW: 'pip install' is run in your TERMINAL/BASH command prompt, NEVER inside a Python script!",
                    "requirements.txt lists your project's dependencies: install all with 'pip install -r requirements.txt'.",
                    "Always use Virtual Environments (venv) to prevent dependency conflicts between projects."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: 'pip install' TERMINAL me likha jata hai, Python code ke andar nahi!",
                    "requirements.txt file se doosre developers 'pip install -r requirements.txt' karke sab kuch install kar sakte hain.",
                    "Hamesha Virtual Environment (venv) me install karo taaki computer ke doosre projects kharab na hon."
                ],
                "analogy_en": "PyPI is the Google Play Store or iOS App Store for Python code. pip is the 'Install App' button on your phone.",
                "analogy_hi": "PyPI Python ka Play Store hai. Aur pip 'Install' button hai jo 1 click me naya app download kar deta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Typing 'pip install requests' directly inside a Python file or interactive Python shell.",
                        "why_it_fails_en": "SyntaxError: invalid syntax. The Python interpreter does not understand shell commands.",
                        "why_it_fails_hi": "Python interpreter shell commands nahi samajhta, syntax error de dega.",
                        "fix": "Run pip in your system Command Prompt, PowerShell, or macOS Terminal."
                    }
                ],
                "example_1": {
                    "title": "Simulating Dependency Management",
                    "title_hi": "requirements.txt format",
                    "code": "reqs = ['requests>=2.31.0', 'fastapi>=0.100.0']\nprint('Generated requirements.txt content:')\nfor r in reqs:\n    print(r)",
                    "expected_output": "Generated requirements.txt content:\nrequests>=2.31.0\nfastapi>=0.100.0",
                    "explanation_en": "Shows the standard pip freeze requirements.txt structure.",
                    "explanation_hi": "requirements.txt ka standard format dikhata hai."
                },
                "example_2": {
                    "title": "Checking Installed Modules via Sys",
                    "title_hi": "Loaded modules check karna",
                    "code": "import sys\nprint('Modules system active:', 'sys' in sys.modules)",
                    "expected_output": "Modules system active: True",
                    "explanation_en": "sys.modules caches all loaded packages.",
                    "explanation_hi": "sys.modules me saare installed aur loaded modules rehte hain."
                },
                "challenge": {
                    "prompt_en": "Print the standard command used to install packages from a requirements file: pip install -r requirements.txt",
                    "prompt_hi": "requirements file se install karne ki standard command print karo: pip install -r requirements.txt",
                    "starter_code": "# Print pip install command:\n",
                    "expected_output": "pip install -r requirements.txt",
                    "solution_code": "print('pip install -r requirements.txt')",
                    "solution_explanation_en": "Outputs the canonical pip command.",
                    "solution_explanation_hi": "Standard pip command print karta hai.",
                    "hints": ["print('pip install -r requirements.txt')"],
                    "ego_roast_hi": "pip command yaad nahi?",
                    "ego_cheer_hi": "PART 4 FUNCTIONS & MODULARITY COMPLETED! 🏆 Professional Code Architect!"
                }
            }
        ]
    }
]
