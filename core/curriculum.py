"""
Elysia Code: Bilingual Curriculum Database
Rich, hands-on syllabus for Python and HTML/CSS tracks.
Each topic includes:
- Intuition & Real-World Analogy (English & Hinglish)
- Industry & College Usage
- 🚨 Common Beginner Mistakes & Anti-Patterns ("What NOT to do")
- Hands-on Coding Challenge with Automated Test Cases
- Top 3 University Viva Questions with Scoring Answers
- Stepped Memory Trace for the 3D Variable Visualizer
"""

from typing import Dict, Any, List
from core.curriculum_builder import PARTS_REGISTRY, get_all_chapters

def get_python_curriculum_tree() -> List[Dict[str, Any]]:
    """Returns the authoritative 7-part, 26-chapter, 140-subtopic curriculum tree."""
    return get_all_chapters()

def get_curriculum_parts() -> List[Dict[str, Any]]:
    """Returns the 7 parts with embedded chapters and descriptions."""
    return PARTS_REGISTRY

CURRICULUM_DATA: Dict[str, Dict[str, Any]] = {

    "python": {
        "title": "Python 3 Core & Lab Mastery",
        "description_en": "From zero programming experience to acing college labs, assignments, and practical vivas.",
        "description_hi": "Bina kisi coding background ke Python seekho, college ke labs aur viva me top karo.",
        "topics": [
            {
                "id": "py_variables",
                "title": "Variables & Data Types",
                "icon": "📦",
                "tag": "Basics",
                "duration": "8 mins",
                "intro_en": "A variable is like a labeled storage box in your computer's memory. You don't need to declare its type in Python; Python automatically figures out whether you are storing an integer, decimal (float), text (string), or boolean.",
                "intro_hi": "Variable ko samajh lo ek labeled dabba. Tum market se dabba laate ho aur uspe sticker laga dete ho 'Chini' ya 'Chai Patti'. Python me type declare karne ka jhanjhat nahi hota, Python khud samajh jata hai ki number hai, decimal hai, ya text.",
                "use_case_en": "Calculating monthly hostel mess dues, tracking student CGPA, or storing user credentials in web applications.",
                "use_case_hi": "Hostel mess ka bill calculate karna, attendance percentage store karna, ya user ka naam aur roll number save karna.",
                "common_mistakes": [
                    {
                        "mistake": "Adding string and integer directly: age = 20; print('My age is ' + age)",
                        "why_it_fails_en": "Python cannot concatenate text with numbers directly. This throws TypeError: can only concatenate str (not 'int') to str.",
                        "why_it_fails_hi": "Python text aur number ko bina convert kiye jod nahi sakta. Chai me namak nahi daal sakte! str(age) lagana padega ya f-string use karo.",
                        "fix": "print(f'My age is {age}') or print('My age is ' + str(age))"
                    },
                    {
                        "mistake": "Variable names starting with numbers or spaces: 1st_student = 'Aman'",
                        "why_it_fails_en": "Variables must start with a letter or underscore. Starting with a number throws a SyntaxError.",
                        "why_it_fails_hi": "Variable ka naam hamesha letter ya underscore se shuru hona chahiye, number ya space se nahi.",
                        "fix": "student_1 = 'Aman' or first_student = 'Aman'"
                    }
                ],
                "starter_code": "# Problem: Calculate the remaining budget\n# Given total budget = 500 and spent = 180\n# Store remaining in 'remaining' and print: 'Remaining budget: X'\n\ntotal_budget = 500\nspent = 180\n\n# Your code here:\n",
                "solution_code": "total_budget = 500\nspent = 180\nremaining = total_budget - spent\nprint(f'Remaining budget: {remaining}')",
                "test_cases": [
                    {"expected_output": "Remaining budget: 320"}
                ],
                "viva_questions": [
                    {
                        "question": "Is Python statically typed or dynamically typed? Explain.",
                        "answer_en": "Python is dynamically typed because variable types are checked and assigned at runtime, so you don't declare types explicitly.",
                        "answer_hi": "Python dynamically typed hai kyunki variable ka type run hone ke time decide hota hai, pehle se int x declare karne ki zarurat nahi hoti."
                    },
                    {
                        "question": "What is the difference between mutable and immutable data types?",
                        "answer_en": "Immutable types (int, float, str, tuple) cannot be modified after creation. Mutable types (list, dict, set) can be updated in-place.",
                        "answer_hi": "Immutable types (numbers, string, tuple) ek baar banne ke baad change nahi ho sakte. Mutable types (list, dictionary) me items add ya update kar sakte ho."
                    }
                ],
                "memory_trace": [
                    {"step": 1, "line": 1, "vars": {"total_budget": 500}},
                    {"step": 2, "line": 2, "vars": {"total_budget": 500, "spent": 180}},
                    {"step": 3, "line": 3, "vars": {"total_budget": 500, "spent": 180, "remaining": 320}}
                ]
            },
            {
                "id": "py_conditionals",
                "title": "If-Else & Attendance Criteria",
                "icon": "⚖️",
                "tag": "Decision Making",
                "duration": "10 mins",
                "intro_en": "Conditionals allow your program to make decisions based on rules. If a condition evaluates to True, one block of code runs; otherwise, the alternative executes.",
                "intro_hi": "Conditionals ka matlab hai shart! Jaise college gate par security guard dekhta hai: 'Agar ID card hai to entry, warna wapis jao'. Python me if, elif, aur else yehi kaam karte hain.",
                "use_case_en": "Checking if student attendance is >= 75% to determine exam eligibility, grading systems, and payment approval.",
                "use_case_hi": "College me 75% attendance check karna ki exam me baithne milega ya detain hoge, grade calculate karna (A, B, C).",
                "common_mistakes": [
                    {
                        "mistake": "Using single '=' instead of '==' in conditions: if attendance = 75:",
                        "why_it_fails_en": "Single '=' is assignment (assigning a value), while '==' is equality comparison. This causes a SyntaxError: invalid syntax.",
                        "why_it_fails_hi": "Single '=' ka matlab hota hai dabba bharna (assign karna). Compare karne ke liye hamesha double '==' lagao!",
                        "fix": "if attendance == 75:"
                    },
                    {
                        "mistake": "Forgetting the colon ':' at the end of the if statement: if score >= 50",
                        "why_it_fails_en": "Python requires a colon at the end of every header line before an indented block.",
                        "why_it_fails_hi": "Python me if, for, def ke aakhri me colon ':' lagana mandatory hai, warna compiler ro padega.",
                        "fix": "if score >= 50:"
                    }
                ],
                "starter_code": "# Problem: Check college exam eligibility\n# If attendance >= 75: print 'Eligible for Exam'\n# Else: print 'Detained - Attend Extra Classes'\n\nattendance = 82\n\n# Your code here:\n",
                "solution_code": "attendance = 82\nif attendance >= 75:\n    print('Eligible for Exam')\nelse:\n    print('Detained - Attend Extra Classes')",
                "test_cases": [
                    {"expected_output": "Eligible for Exam"}
                ],
                "viva_questions": [
                    {
                        "question": "What is the difference between '==' and 'is' in Python?",
                        "answer_en": "'==' checks if the values are equal. 'is' checks if both variables refer to the exact same object in memory (identity check).",
                        "answer_hi": "'==' check karta hai ki dono taraf ki value barabar hai ya nahi. Jabki 'is' check karta hai ki dono memory me same address par hain ya nahi."
                    },
                    {
                        "question": "Why does indentation matter in Python compared to C/C++ or Java?",
                        "answer_en": "Python uses indentation (whitespace) instead of curly braces {} to define code blocks and scope.",
                        "answer_hi": "C ya Java me curly braces {} lagte the block batane ke liye, Python me spacing (indentation) se hi Python ko pata chalta hai ki kaunsa code kiske andar hai."
                    }
                ],
                "memory_trace": [
                    {"step": 1, "line": 1, "vars": {"attendance": 82}},
                    {"step": 2, "line": 2, "vars": {"attendance": 82, "condition": "82 >= 75 (True)"}},
                    {"step": 3, "line": 3, "vars": {"action": "Printed 'Eligible for Exam'"}}
                ]
            },
            {
                "id": "py_loops",
                "title": "Loops (For, While & Range)",
                "icon": "🔄",
                "tag": "Repetition",
                "duration": "12 mins",
                "intro_en": "Loops allow you to repeat a task without copy-pasting code. A 'for' loop iterates over a sequence (like a list or range), while a 'while' loop repeats as long as a condition holds true.",
                "intro_hi": "Loop ka matlab hai chakkar! Socho tumhe 50 dosto ko invitation message bhejna hai. Ek-ek karke type karoge to haath thak jayega. Loop se computer 50 baar khud kaam kar deta hai.",
                "use_case_en": "Iterating over database records, calculating factorial/summation in labs, scanning files, batch processing.",
                "use_case_hi": "Class ke 60 bacho ka total marks calculate karna, lab assignment me 1 se N tak sum nikalna, tables print karna.",
                "common_mistakes": [
                    {
                        "mistake": "Infinite while loop: while count < 5: print(count) (forgetting count += 1)",
                        "why_it_fails_en": "If you never update the loop variable, the condition stays True forever, hanging the computer or freezing the browser.",
                        "why_it_fails_hi": "Agar condition badloge nahi to loop zindagi bhar chalta rahega aur browser freeze ho jayega. Hamesha counter badhao (i += 1).",
                        "fix": "while count < 5:\n    print(count)\n    count += 1"
                    },
                    {
                        "mistake": "Misunderstanding range(stop): Thinking range(5) includes 5",
                        "why_it_fails_en": "In Python, range(n) generates numbers from 0 up to n-1 (stop value is excluded).",
                        "why_it_fails_hi": "Python me range(5) 0 se 4 tak hi jata hai, 5 include nahi hota! Agar 1 se 5 chahiye to range(1, 6) likho.",
                        "fix": "for i in range(1, 6):"
                    }
                ],
                "starter_code": "# Problem: Print the sum of first 5 natural numbers (1 + 2 + 3 + 4 + 5 = 15)\n# Store the answer in 'total' and print: 'Sum is: X'\n\ntotal = 0\n# Use a for loop to calculate the sum:\n",
                "solution_code": "total = 0\nfor i in range(1, 6):\n    total += i\nprint(f'Sum is: {total}')",
                "test_cases": [
                    {"expected_output": "Sum is: 15"}
                ],
                "viva_questions": [
                    {
                        "question": "What is the difference between break, continue, and pass in Python?",
                        "answer_en": "'break' exits the loop immediately. 'continue' skips to the next iteration. 'pass' is a null statement placeholder that does nothing.",
                        "answer_hi": "'break' loop ko turant tod ke bahar nikal deta hai. 'continue' is current round ko chhod ke agle round par chala jata hai. 'pass' ek khaali placeholder hai jisse error na aaye."
                    },
                    {
                        "question": "Does Python support a 'do-while' loop?",
                        "answer_en": "No, Python does not have a native 'do-while' loop, but it can be simulated using 'while True:' with a conditional 'break'.",
                        "answer_hi": "Nahi, Python me 'do-while' loop nahi hota. Par hum while True: likh kar andar if condition: break laga ke same cheez bana sakte hain."
                    }
                ],
                "memory_trace": [
                    {"step": 1, "line": 1, "vars": {"total": 0}},
                    {"step": 2, "line": 2, "vars": {"total": 1, "i": 1}},
                    {"step": 3, "line": 2, "vars": {"total": 3, "i": 2}},
                    {"step": 4, "line": 2, "vars": {"total": 6, "i": 3}},
                    {"step": 5, "line": 2, "vars": {"total": 10, "i": 4}},
                    {"step": 6, "line": 2, "vars": {"total": 15, "i": 5}}
                ]
            },
            {
                "id": "py_lists",
                "title": "Lists & Slicing",
                "icon": "📜",
                "tag": "Data Structures",
                "duration": "14 mins",
                "intro_en": "A list is an ordered, mutable sequence of elements enclosed in square brackets []. You can store different data types together and access elements using zero-based indices.",
                "intro_hi": "List ek grocery list ya canteen menu ki tarah hai jisme sequence me items likhe hote hain. Bracket [] use hota hai aur counting hamesha 0 se shuru hoti hai (0th item, 1st item).",
                "use_case_en": "Maintaining student lists, tracking marks, shopping carts, time-series data.",
                "use_case_hi": "Hostel room ke 4 roommates ke marks store karna, Swiggy cart me items add/remove karna.",
                "common_mistakes": [
                    {
                        "mistake": "IndexError: accessing an index that doesn't exist: arr = [10, 20]; print(arr[2])",
                        "why_it_fails_en": "List indices start at 0. A 2-element list only has indices 0 and 1. Accessing index 2 raises IndexError: list index out of range.",
                        "why_it_fails_hi": "Dabba sirf 2 samoso ka hai (index 0 aur 1). Tu maang raha hai index 2 jo hai hi nahi! Hamesha len(arr)-1 tak hi access karo.",
                        "fix": "print(arr[1]) # last element"
                    },
                    {
                        "mistake": "Modifying a list while iterating directly over it using for item in arr: arr.remove(item)",
                        "why_it_fails_en": "Modifying the list structure while iterating causes elements to be skipped because the internal iterator index shifts.",
                        "why_it_fails_hi": "Loop ke andar hi list se element delete karoge to index hil jata hai aur agla item skip ho jata hai. Hamesha copy par loop lagao: arr[:].",
                        "fix": "for item in arr[:]: # iterate over slice copy"
                    }
                ],
                "starter_code": "# Problem: Reverse the given marks list using slicing and print the highest mark\n# marks = [45, 88, 92, 67, 78]\n# Store reversed list in 'rev_marks' and max mark in 'top_mark'\n\nmarks = [45, 88, 92, 67, 78]\n\n# Your code here:\n",
                "solution_code": "marks = [45, 88, 92, 67, 78]\nrev_marks = marks[::-1]\ntop_mark = max(marks)\nprint(f'Reversed: {rev_marks}')\nprint(f'Top mark: {top_mark}')",
                "test_cases": [
                    {"expected_output": "Reversed: [78, 67, 92, 88, 45]\nTop mark: 92"}
                ],
                "viva_questions": [
                    {
                        "question": "What is the difference between a Python List and an Array in C?",
                        "answer_en": "A C array has a fixed size and must hold identical data types. A Python list is dynamic (resizes automatically) and can hold heterogeneous elements.",
                        "answer_hi": "C array fixed size ka hota hai aur usme sirf ek hi type ka data aa sakta hai (jaise sab int). Python list dynamic hoti hai aur usme int, string, float sab mix ho sakte hain."
                    },
                    {
                        "question": "What does list slicing [::-1] do and what is its time complexity?",
                        "answer_en": "[::-1] creates a reversed shallow copy of the list. Its time complexity is O(n) because it copies all n elements in reverse order.",
                        "answer_hi": "[::-1] puri list ko ulta (reverse) karke nayi list bana deta hai. Iska time complexity O(n) hota hai kyunki n elements copy hote hain."
                    }
                ],
                "memory_trace": [
                    {"step": 1, "line": 1, "vars": {"marks": [45, 88, 92, 67, 78]}},
                    {"step": 2, "line": 2, "vars": {"rev_marks": [78, 67, 92, 88, 45]}},
                    {"step": 3, "line": 3, "vars": {"top_mark": 92}}
                ]
            },
            {
                "id": "py_functions",
                "title": "Functions & Modularity",
                "icon": "⚡",
                "tag": "Logic Reusability",
                "duration": "15 mins",
                "intro_en": "A function is a reusable block of code that performs a specific task. You define it once using def, pass inputs (parameters), and return a result with return.",
                "intro_hi": "Function ko samajh lo ek vending machine! Tum machine me coin (argument/input) daalte ho, andar processing hoti hai, aur wo chips ka packet (return value) bahar phek deta hai. Ek baar machine bana li, ab 100 baar use karo.",
                "use_case_en": "Calculating SGPA/CGPA, authentication checks, mathematical formulas, building modular clean code for lab evaluations.",
                "use_case_hi": "Marks daal ke SGPA nikalne ka formula, recurring discount calculation, lab practical me modular code dikhana jisse teacher full marks de.",
                "common_mistakes": [
                    {
                        "mistake": "Confusing print() with return: def add(a, b): print(a + b) then doing res = add(2, 3) + 5",
                        "why_it_fails_en": "A function without a return statement implicitly returns None. Trying to do arithmetic on None throws TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'.",
                        "why_it_fails_hi": "print() sirf screen pe show karta hai, value wapis nahi deta! Agle calculation ke liye hamesha return use karo, warna Python None return karega.",
                        "fix": "def add(a, b):\n    return a + b"
                    },
                    {
                        "mistake": "Calling a function before defining it in the file.",
                        "why_it_fails_en": "Python is interpreted line-by-line. Calling a function before its def throws NameError: name 'func' is not defined.",
                        "why_it_fails_hi": "Python upar se niche line-by-line chalta hai. Pehle function define karo, uske baad hi use call kar sakte ho.",
                        "fix": "Define 'def my_func():' before calling 'my_func()'"
                    }
                ],
                "starter_code": "# Problem: Write a function 'calculate_cgpa(marks_list)'\n# It takes a list of marks (out of 100) and returns the average / 10\n# Test with marks = [80, 90, 70]\n\ndef calculate_cgpa(marks_list):\n    # Your code here\n    pass\n\nmarks = [80, 90, 70]\nresult = calculate_cgpa(marks)\nprint(f'Calculated CGPA: {result}')\n",
                "solution_code": "def calculate_cgpa(marks_list):\n    avg = sum(marks_list) / len(marks_list)\n    return avg / 10\n\nmarks = [80, 90, 70]\nresult = calculate_cgpa(marks)\nprint(f'Calculated CGPA: {result}')",
                "test_cases": [
                    {"expected_output": "Calculated CGPA: 8.0"}
                ],
                "viva_questions": [
                    {
                        "question": "What is the difference between parameters and arguments?",
                        "answer_en": "Parameters are the variable names listed in the function definition. Arguments are the actual values passed to the function when it is called.",
                        "answer_hi": "Parameters wo hote hain jo function define karte waqt bracket me likhte hain (e.g. def add(a, b)). Arguments wo actual values hain jo call karte waqt bhejte hain (add(5, 10))."
                    },
                    {
                        "question": "What does *args and **kwargs mean in Python?",
                        "answer_en": "*args allows a function to accept any number of positional arguments as a tuple. **kwargs allows arbitrary keyword arguments as a dictionary.",
                        "answer_hi": "*args se hum function me kitne bhi positional arguments bhej sakte hain (tuple ban jata hai). **kwargs se key-value pairs bhej sakte hain (dictionary ban jati hai)."
                    }
                ],
                "memory_trace": [
                    {"step": 1, "line": 1, "vars": {"function_defined": "calculate_cgpa"}},
                    {"step": 2, "line": 5, "vars": {"marks": [80, 90, 70]}},
                    {"step": 3, "line": 6, "vars": {"inside_func": True, "marks_list": [80, 90, 70], "sum": 240, "len": 3, "avg": 80.0}},
                    {"step": 4, "line": 7, "vars": {"result": 8.0}}
                ]
            }
        ]
    },
    "html": {
        "title": "HTML5 & Modern Web Foundation",
        "description_en": "Master the skeleton of the web, semantic tags, forms, tables, and CSS layout foundations.",
        "description_hi": "Internet ki bhasha seekho: HTML tags, forms, tables aur styling jisse live websites banti hain.",
        "topics": [
            {
                "id": "html_tags",
                "title": "HTML Structure & Essential Tags",
                "icon": "🏗️",
                "tag": "Web Skeleton",
                "duration": "8 mins",
                "intro_en": "HTML (HyperText Markup Language) is the backbone of any website. It uses tags enclosed in angle brackets <tag> to tell the browser how to structure text, headings, paragraphs, and images.",
                "intro_hi": "HTML web page ka kankaal (skeleton) hai. Jaise insaan ki body me pehle haddiyan banti hain fir skin aati hai, waise hi pehle HTML se content ki haddi banti hai aur CSS se makeup hota hai.",
                "use_case_en": "Building portfolio landing pages, article layouts, college fest websites, and web apps.",
                "use_case_hi": "Apna khud ka resume website banana, college fest ka page design karna, e-commerce product pages.",
                "common_mistakes": [
                    {
                        "mistake": "Using multiple <h1> tags on a single page for styling purposes.",
                        "why_it_fails_en": "A web page should have only one <h1> representing the main topic for SEO and accessibility. Use <h2>, <h3> or CSS for font sizes.",
                        "why_it_fails_hi": "Ek page pe sirf ek hi main <h1> title hona chahiye SEO aur standard ke hisaab se. Chhote title ke liye <h2> ya <h3> use karo.",
                        "fix": "Use one <h1> for the primary header, and <h2>/<h3> for subheadings."
                    },
                    {
                        "mistake": "Trying to close self-closing tags like <img></img> or <br></br>",
                        "why_it_fails_en": "<img>, <br>, and <hr> are void elements (self-closing). They do not contain inner text and do not require closing tags.",
                        "why_it_fails_hi": "<img> aur <br> void tags hain, inme koi text andar nahi hota. Inhe </img> karke band karne ki koi zarurat nahi hoti.",
                        "fix": "<img src='photo.jpg' alt='Photo'> or <br>"
                    }
                ],
                "starter_code": "<!-- Problem: Create a College Fest Welcome Card -->\n<!-- Add an <h1> with text 'TechFest 2026', an <h2> with 'The Ultimate Coding Arena' -->\n<!-- And a paragraph <p> with 'Join over 500 hackers this weekend!' -->\n\n<div class=\"fest-card\">\n  <!-- Your code here -->\n</div>\n",
                "solution_code": "<div class=\"fest-card\">\n  <h1>TechFest 2026</h1>\n  <h2>The Ultimate Coding Arena</h2>\n  <p>Join over 500 hackers this weekend!</p>\n</div>",
                "test_cases": [
                    {"expected_html_elements": ["h1", "h2", "p"]}
                ],
                "viva_questions": [
                    {
                        "question": "What is the difference between HTML elements and HTML tags?",
                        "answer_en": "A tag is the opening or closing syntax (e.g. <p> or </p>). An element comprises the opening tag, content, and closing tag as a whole unit.",
                        "answer_hi": "Tag sirf opening ya closing bracket hota hai jaise <p>. Element pura package hota hai jisme opening tag, beech ka text, aur closing tag sab shamil hota hai."
                    },
                    {
                        "question": "What does <!DOCTYPE html> do?",
                        "answer_en": "It tells the web browser that the document is written in modern HTML5 standards, preventing the browser from rendering in 'quirks mode'.",
                        "answer_hi": "Ye browser ko batata hai ki page modern HTML5 me likha hai, taaki browser purane buggy mode (quirks mode) me na chale."
                    }
                ]
            },
            {
                "id": "html_forms",
                "title": "Forms & User Inputs",
                "icon": "📝",
                "tag": "Interactivity",
                "duration": "12 mins",
                "intro_en": "Forms allow websites to collect user data like login credentials, feedback, registrations, and payment details using input elements, dropdowns, and buttons.",
                "intro_hi": "Form wo jagah hai jahan user apni details bharta hai — jaise Instagram sign up page, college admission form, ya Swiggy address box. <form>, <input>, aur <button> se ye banta hai.",
                "use_case_en": "College event registration, student login portals, survey questionnaires, checkout flows.",
                "use_case_hi": "College fest registration form, library book issue portal, student attendance feedback form.",
                "common_mistakes": [
                    {
                        "mistake": "Missing the 'name' attribute on <input> tags.",
                        "why_it_fails_en": "Without the 'name' attribute, form data will NOT be included in the submission payload sent to the backend server.",
                        "why_it_fails_hi": "Agar input tag me name attribute nahi doge, to server ko pata hi nahi chalega ki kis field ka data aya hai aur backend me blank jayega.",
                        "fix": "<input type='text' name='username' placeholder='Enter username'>"
                    },
                    {
                        "mistake": "Not connecting <label> with <input> using for and id.",
                        "why_it_fails_en": "Connecting label 'for' with input 'id' improves accessibility and allows users to click the text label to focus the input box.",
                        "why_it_fails_hi": "Label me for='email' aur input me id='email' lagane se text par click karte hi input box select ho jata hai. Ye best practice hai!",
                        "fix": "<label for='email'>Email:</label><input type='email' id='email' name='email'>"
                    }
                ],
                "starter_code": "<!-- Problem: Build a Student Hackathon Registration Form -->\n<!-- Create a <form> with: -->\n<!-- 1. An input of type 'text' with name='student_name' and placeholder='Full Name' -->\n<!-- 2. An input of type 'email' with name='student_email' and placeholder='College Email' -->\n<!-- 3. A <button type='submit'>Register Now</button> -->\n\n<form>\n  <!-- Your code here -->\n</form>\n",
                "solution_code": "<form>\n  <input type=\"text\" name=\"student_name\" placeholder=\"Full Name\">\n  <input type=\"email\" name=\"student_email\" placeholder=\"College Email\">\n  <button type=\"submit\">Register Now</button>\n</form>",
                "test_cases": [
                    {"expected_html_elements": ["form", "input", "button"]}
                ],
                "viva_questions": [
                    {
                        "question": "What is the difference between GET and POST methods in HTML forms?",
                        "answer_en": "GET appends form data to the URL query string (visible and cached, good for searches). POST sends data inside the HTTP request body (secure and suitable for sensitive data like passwords).",
                        "answer_hi": "GET method data ko URL me chipka ke bhejta hai (sabko dikhta hai, jaise Google search). POST method data ko body ke andar chhipa ke bhejta hai (passwords aur form ke liye safe)."
                    },
                    {
                        "question": "What is the purpose of semantic HTML tags like <nav>, <article>, <section>, and <footer>?",
                        "answer_en": "Semantic tags clearly describe their meaning to both browser and developer, improving SEO, accessibility (screen readers), and code maintainability.",
                        "answer_hi": "Semantic tags ka matlab hota hai aise tags jinka naam sunke hi pata chale ki andar kya hai (jaise <nav>, <footer>), sirf <div> use karne se SEO aur accessibility kharab hoti hai."
                    }
                ]
            }
        ]
    }
}
