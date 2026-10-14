/**
 * Pre-bundled Visual Python Handbook Data
 * Enables instant, offline, zero-latency rendering!
 */
window.HANDBOOK_CHAPTERS = [
  {
    "id": "ch1_intro",
    "number": 1,
    "title": "Introduction to Python",
    "badge": "Core Foundation",
    "slides": [
      {
        "id": "prog_lang",
        "title": "Programming Languages",
        "concept": "We use programming languages to give computers clear, executable instructions.",
        "analogy_en": "Think of programming as giving a recipe to a chef. If you say 'cook food', the chef is confused. But if you say 'take 2 eggs, boil for 5 minutes', the chef executes exactly.",
        "analogy_hi": "Computer ek dumb robot hai! Agar tum usse bologe '5 aur 5 jod do', to wo confuse ho jayega. Par agar Python me likhoge `print(5 + 5)`, to wo turant execute karke `10` dega.",
        "visual_type": "flow_diagram",
        "code": "print(5 + 5)  # Output: 10",
        "notes_en": [
          "Computers only understand 0s and 1s (binary).",
          "Programming languages bridge the gap between human language and computer machine code."
        ],
        "notes_hi": [
          "Computer sirf 0 aur 1 (binary) samajhta hai.",
          "Programming language insaan ki bhasha aur computer ke beech ka bridge hai."
        ],
        "when_to_use_en": "Whenever you want to automate repetitive calculations, process data, or build software.",
        "when_to_use_hi": "Jab bhi tumhe manual kaam automate karna ho ya software banana ho."
      },
      {
        "id": "levels_of_lang",
        "title": "Levels of Programming Languages",
        "concept": "From Human Natural Language down to Binary Machine Code.",
        "analogy_en": "Natural Language (English/Hindi) is for humans. High-level languages (Python, JS) are human-friendly. Low-level (Assembly, C) give hardware control. Machine language (0s and 1s) is what CPU directly executes.",
        "analogy_hi": "English/Hindi insano ke liye hai. Python high-level hai (padhne me asaan). Assembly low-level hardware ke paas hai. Machine code (010101) computer ka asli brain hai.",
        "visual_type": "level_stack",
        "code": "# Python High-Level Code:\nif score >= 90:\n    print('Outstanding')",
        "notes_en": [
          "Natural Language: Communication between humans.",
          "High-Level Language (Python): Easy to read, write, and maintain.",
          "Low-Level Language (Assembly): Closer to hardware registers and memory.",
          "Machine Language: Binary 0s and 1s executed directly by the CPU."
        ],
        "notes_hi": [
          "Natural Language: Hum aapas me baat karte hain.",
          "High-Level (Python): English jaisa padhne me aasan.",
          "Low-Level (Assembly): Hardware aur chip ke bohot kareeb.",
          "Machine Code: 0 aur 1 jo seedha processor run karta hai."
        ]
      },
      {
        "id": "how_python_runs",
        "title": "How Python Runs (Behind the Scenes)",
        "concept": "Source Code (.py) -> Compilation to Bytecode (.pyc) -> Python Virtual Machine (PVM) -> Machine Code (CPU).",
        "analogy_en": "You write English-like code (.py). Python's compiler converts it into an optimized intermediate Bytecode (.pyc). The Python Virtual Machine (PVM) reads this bytecode and translates it into CPU machine instructions.",
        "analogy_hi": "Pehle tum `.py` file me code likhte ho. Python ka compiler use `.pyc` (bytecode) banata hai. Fir Python Virtual Machine (PVM) us bytecode ko CPU ke samajhne layak machine code me convert karti hai.",
        "visual_type": "pipeline",
        "code": "# Run in terminal:\n# python app.py\n# Generates __pycache__/app.cpython-311.pyc",
        "notes_en": [
          "1. Source Code: Human-readable code written in .py files.",
          "2. Compilation to Bytecode: Python converts code to .pyc (lower-level instructions).",
          "3. Python Virtual Machine (PVM): Reads bytecode and translates it for the host OS/CPU.",
          "4. Machine Code: CPU executes the final binary instructions."
        ],
        "notes_hi": [
          "1. Source Code: Jo code tum likhte ho (.py).",
          "2. Bytecode: Python ka internal intermediate code (.pyc).",
          "3. PVM: Bytecode ko OS aur computer ke hisaab se execute karta hai.",
          "4. Machine Code: Final execution jo CPU par hoti hai."
        ]
      },
      {
        "id": "why_learn_python",
        "title": "Why Learn Python?",
        "concept": "1. Powerful yet Simple  2. Used Everywhere  3. Leading in AI  4. Huge Community  5. High in Demand.",
        "analogy_en": "Writing 'Hello World' in C takes 6 lines of code. In Java it takes 5 lines. In Python it takes exactly 1 line: `print('Hello World')`.",
        "analogy_hi": "C ya Java me Hello World likhne ke liye class, main method aur curly braces lagte hain. Python me sirf ek line: `print('Hello World')`! Kam code, zyada kaam.",
        "visual_type": "features_grid",
        "code": "print('Hello World!')",
        "notes_en": [
          "Web Development: Django, Flask, FastAPI.",
          "AI & Data Science: PyTorch, TensorFlow, Pandas, NumPy.",
          "Automation & Scripting: Automating Excel, scraping websites, file management.",
          "Massive open-source ecosystem."
        ],
        "notes_hi": [
          "Web apps ke liye: Django, FastAPI.",
          "AI aur Data Science ka king: PyTorch, Pandas, Scikit-learn.",
          "Automation: Roz ke boring tasks ko 1 click me automate karo."
        ]
      },
      {
        "id": "comments",
        "title": "Comments (#)",
        "concept": "A comment is text in your code that Python completely ignores and humans read.",
        "analogy_en": "Comments are like sticky notes on a blueprint. The builders ignore the sticky note color, but read the instructions to understand the design.",
        "analogy_hi": "Comments code ke andar lage sticky notes hain. Python unhe chhoota bhi nahi, par tum aur tumhare team members use padh kar logic samajhte hain.",
        "visual_type": "code_card",
        "code": "# This calculates final semester SGPA\ntotal_credits = 22\nsgpa = 8.6  # Current semester grade",
        "notes_en": [
          "Python completely ignores comments during execution.",
          "Comments do not change program logic or output.",
          "Keep comments clear, short, and meaningful.",
          "Explain WHY you wrote the code, not obvious syntax."
        ],
        "notes_hi": [
          "Python comments ko ignore karta hai.",
          "Output par comments ka koi asar nahi hota.",
          "Code me 'kyun' kiya wo likho, obvious cheezein mat likho."
        ]
      },
      {
        "id": "print_function",
        "title": "The print() Function",
        "concept": "print() is a built-in function that displays output on the console screen.",
        "analogy_en": "print() is your program's loudspeaker. Without print(), your program does calculations silently in memory, but never tells you the result.",
        "analogy_hi": "print() computer ka loudspeaker hai! Agar tum calculator me 5+5 jod lo par screen off ho, to kya fayda? print() screen par answer dikhata hai.",
        "visual_type": "io_card",
        "code": "print('Hello, Python!')\nprint('Score:', 95, 'Grade:', 'A+')",
        "notes_en": [
          "print() sends output to the console but does not store it in memory.",
          "It automatically converts values to readable text.",
          "You can print multiple values separated by commas."
        ],
        "notes_hi": [
          "print() screen par dikhata hai par memory me save nahi karta.",
          "Multiple values ko comma `,` laga kar ek sath print kar sakte ho."
        ]
      },
      {
        "id": "builtin_vs_others",
        "title": "Built-in vs User-Defined vs Third-Party Functions",
        "concept": "1. Built-in (comes with Python: print, len, type)  2. Standard Library (math, random - need import)  3. Third-Party (pandas, numpy - need pip install)  4. User-Defined (def).",
        "analogy_en": "Built-ins are like your smartphone's built-in phone app (always there). Standard library is like pre-installed calculator (open it when needed). Third-party is downloading apps from the App Store.",
        "analogy_hi": "Built-in: Phone ka dialer (hamesha ready). Standard library: Phone ki settings (import karna padta hai jaise `import math`). Third-party: Play Store se app download karna (`pip install pandas`). User-defined: Apna khud ka function banana.",
        "visual_type": "hierarchy_tree",
        "code": "import math\nprint(len('Python'))       # Built-in\nprint(math.sqrt(25))        # Standard library\n# import pandas as pd      # Third-party",
        "notes_en": [
          "Built-in: No import needed (print, type, len, str, int, input).",
          "Standard Library: Maintained by Python, requires 'import' (math, random, os).",
          "Third-Party: Built by community, installed via pip (requests, pandas, flask)."
        ],
        "notes_hi": [
          "Built-in: Bina kisi import ke direct chalta hai.",
          "Standard Library: Python ke sath aati hai, par `import` likhna padta hai.",
          "Third-Party: `pip install` se install hoti hai."
        ]
      },
      {
        "id": "escape_sequences",
        "title": "Escape Sequences (\\n, \\t, \\\\, \\\")",
        "concept": "Special characters that start with a backslash \\ and control text formatting inside strings.",
        "analogy_en": "When Python sees a backslash \\, it knows: 'Don't print the next letter normally, do something special!'",
        "analogy_hi": "Backslash `\\` Python ke liye ek secret code hai! `\\n` ka matlab nayi line me jao, `\\t` ka matlab 4 space (tab) chhod do.",
        "visual_type": "escape_table",
        "code": "print('Line 1\\nLine 2')\nprint('Name:\\tAman\\tRoll:\\t101')\nprint('He said: \\\"Code is life!\\\"')",
        "notes_en": [
          "\\n -> New line",
          "\\t -> Tab (horizontal space)",
          "\\\\ -> Literal backslash",
          "\\\" -> Double quote inside double-quoted string"
        ],
        "notes_hi": [
          "`\\n` se nayi line shuru hoti hai.",
          "`\\t` se tab space aata hai.",
          "`\\\"` se string ke andar quote print hota hai."
        ]
      },
      {
        "id": "variables_concept",
        "title": "Variables: Labeled Storage Boxes",
        "concept": "A variable is a labeled name that references data in computer memory.",
        "analogy_en": "A variable is like a labeled box. You put a value inside (e.g. 25 into 'age'), and your program can access, reuse, or update that value whenever needed.",
        "analogy_hi": "Variable ek dabba hai jisme tum saman rakhte ho aur uspe naam chipka dete ho. Baad me jab bhi zaroorat ho, us dabbe ka naam lekar saman nikaal sakte ho.",
        "visual_type": "memory_box",
        "code": "x = 10\nprint(x)\nx = 25  # Value updated\nprint(x)",
        "notes_en": [
          "Variables allow programs to work with dynamic data instead of hard-coded values.",
          "Naming Rules: Must start with a letter or underscore, cannot start with numbers.",
          "Variables are case-sensitive: 'score' and 'Score' are different."
        ],
        "notes_hi": [
          "Variable se dynamic values handle hoti hain.",
          "Rules: Number se shuru nahi ho sakta (e.g. `1x` galat hai, `x1` sahi hai).",
          "Case-sensitive hota hai (`age` aur `Age` alag alag hain)."
        ]
      },
      {
        "id": "input_function",
        "title": "The input() Function",
        "concept": "input() allows a program to pause and receive data typed by the user while it is running.",
        "analogy_en": "Without input(), a program is like a movie (you just watch). With input(), a program is like a video game (it responds to what you type!).",
        "analogy_hi": "input() se program user se interact karta hai. Program wahi ruk jata hai jab tak user keyboard se type karke Enter na daba de.",
        "visual_type": "input_card",
        "code": "user_name = input('Enter your name: ')\nuser_age = int(input('Enter your age: '))  # Convert text to number\nprint(f'Welcome {user_name}, you are {user_age} years old.')",
        "notes_en": [
          "CRITICAL: input() ALWAYS returns data as text (string)!",
          "If you need numbers for calculation, wrap it with int() or float(): int(input())."
        ],
        "notes_hi": [
          "DHYAN RAHE: input() hamesha STRING (text) return karta hai!",
          "Number ke liye hamesha `int(input())` ya `float(input())` karo."
        ]
      },
      {
        "id": "data_types_intro",
        "title": "What is a Data Type?",
        "concept": "A data type defines the kind of value a variable holds and what operations you can perform on it.",
        "analogy_en": "You can add two numbers (2 + 3 = 5). But adding two words ('2' + '3' = '23') glues them together. The data type dictates the behavior of the operator.",
        "analogy_hi": "Number ke sath `+` math karta hai (2 + 3 = 5). Text ke sath `+` jodta hai ('2' + '3' = '23'). Data type hi batata hai ki operator kya karega.",
        "visual_type": "type_cards",
        "code": "a = 10         # int (Whole number)\nb = 3.14       # float (Decimal)\nc = 'Python'   # str (Text)\nd = True       # bool (True or False)",
        "notes_en": [
          "Python is dynamically typed: variable types are detected automatically at runtime.",
          "You do not need to write 'int x = 10' like in C or Java."
        ],
        "notes_hi": [
          "Python dynamically typed hai: type khud pehchan leta hai.",
          "C/Java ki tarah pehle se type declare karne ka tension nahi."
        ]
      },
      {
        "id": "data_types_categories",
        "title": "Categories of Data Types",
        "concept": "1. No Value (NoneType: None)  2. Single Value (Primitive: int, float, str, bool)  3. Multi-Values (Containers: list, tuple, set, dict).",
        "analogy_en": "No Value is an empty basket. Single Value holds one fruit (e.g. an apple). Multi-Values is a fruit basket holding an assortment of fruits together.",
        "analogy_hi": "No Value: Khaali basket (`None`). Single Value: Ek seb (`50`, `'Hello'`). Multi-Values: Pura fruits ka dabba (`list`, `dict`, `set`).",
        "visual_type": "category_tree",
        "code": "no_val = None\nsingle_val = 50\nmulti_val = [10, 20, 30]",
        "notes_en": [
          "NoneType: Represents absence of value or nothingness.",
          "Single Value: Holds one item at a time.",
          "Multi-Values: Data structures for collections."
        ],
        "notes_hi": [
          "`None`: Jab koi value na ho.",
          "Primitive: Ek hi data point.",
          "Data Structures: Ek se zyada values ko organize karne ke liye."
        ]
      },
      {
        "id": "functions_vs_methods",
        "title": "Functions vs Methods",
        "concept": "Functions are standalone tools (len, print). Methods are tools bound to a specific data type (str.upper(), list.append()).",
        "analogy_en": "A screwdriver is a standalone function (it works on many things). A car's steering wheel is a method (it only works on that specific car object).",
        "analogy_hi": "Function ek aam tool hai jo kisi par bhi chal sakta hai (`len('abc')`, `len([1, 2])`). Method ek specific data type ka personal button hai (`'abc'.upper()`, `list.append()`).",
        "visual_type": "method_comparison",
        "code": "# Function: function_name(value)\nlength = len('hello')\n\n# Method: value.method_name()\nuppercase = 'hello'.upper()",
        "notes_en": [
          "Functions are called directly: func(data).",
          "Methods are called using dot notation on an object: data.method()."
        ],
        "notes_hi": [
          "Function seedha call hota hai: `len(x)`.",
          "Method dot notation se call hota hai: `x.upper()`."
        ]
      }
    ]
  },
  {
    "id": "ch2_strings",
    "number": 2,
    "title": "Working with Strings",
    "badge": "Text Mastery",
    "slides": [
      {
        "id": "string_values",
        "title": "String Values in the Real World",
        "concept": "Most real-world data is text: names, emails, logs, file paths, API responses. Text is often messy, inconsistent, and poorly formatted.",
        "analogy_en": "Raw text from users is like raw vegetables from the market\u2014dirty and unwashed. Before cooking (analyzing), you must wash and trim it (clean and format strings).",
        "analogy_hi": "User jo text form me bharta hai wo kachre jaisa hota hai\u2014faltu spaces, chhota-bada case (`aman`, `AMAN`). Pehle string ko clean karte hain fir database me save karte hain.",
        "visual_type": "text_cleaning",
        "code": "raw_email = '   Student@LPU.in  '\nclean_email = raw_email.strip().lower()\nprint(clean_email)  # 'student@lpu.in'",
        "notes_en": [
          "Data engineering and AI spend 40% of time cleaning messy strings.",
          "Strings in Python are immutable (cannot be modified in-place)."
        ],
        "notes_hi": [
          "Strings ko clean karna real industry ka sabse bada kaam hai.",
          "Python me strings IMMUTABLE hoti hain (unhe direct change nahi kiya ja sakta, naya string banta hai)."
        ]
      },
      {
        "id": "string_tools_roadmap",
        "title": "String Tools Roadmap",
        "concept": "Types, Math, Transformations, Cleaning, Search, Validation.",
        "analogy_en": "Think of the string toolkit like a Swiss army knife with specialized blades for measuring, cleaning, searching, and reshaping text.",
        "analogy_hi": "String ek Swiss Knife ki tarah hai: Napne ke liye `len()`, Safaai ke liye `strip()`, Dhoondhne ke liye `find()` aur Badalane ke liye `replace()`.",
        "visual_type": "tools_map",
        "code": "s = '  Python 3.11  '\nprint(len(s))            # Math: 15\nprint(s.strip())         # Cleaning: 'Python 3.11'\nprint(s.replace('3.11', 'Pro'))  # Transformation",
        "notes_en": [
          "Types: type(), str()",
          "Math: len(), count()",
          "Transformations: replace(), split(), f-strings, concatenation",
          "Cleaning: strip(), lstrip(), rstrip(), lower(), upper()",
          "Search: startswith(), endswith(), find(), in",
          "Validation: isalpha(), isnumeric()"
        ],
        "notes_hi": [
          "Har kaam ke liye specialized string tool bana hua hai."
        ]
      },
      {
        "id": "string_operators",
        "title": "String Operators (+, *, in, not in)",
        "concept": "+ for Concatenation, * for Repetition, in for Membership testing.",
        "analogy_en": "'Hello' + 'World' glues them. 'ha' * 3 repeats it ('hahaha'). 'a' in 'cat' checks if 'a' exists inside 'cat'.",
        "analogy_hi": "`+` do strings ko jodta hai. `*` repeat karta hai (`'echo ' * 3`). `in` check karta hai ki wo letter andar maujood hai ya nahi.",
        "visual_type": "operator_grid",
        "code": "greeting = 'Hello ' + 'Aman'\nlaugh = 'ha' * 3\nhas_at = '@' in 'user@gmail.com'\n\nprint(greeting)  # Hello Aman\nprint(laugh)     # hahaha\nprint(has_at)    # True",
        "notes_en": [
          "Concatenation (+) only works between strings (str + str).",
          "str + int raises TypeError! Use str(num) or f-string."
        ],
        "notes_hi": [
          "`+` sirf string aur string ke beech chalta hai.",
          "String aur number ko `+` karoge to TypeError aayega!"
        ]
      },
      {
        "id": "indexing_slicing",
        "title": "String Indexing & Slicing",
        "concept": "Indexing selects 1 character: s[0]. Slicing extracts a range: s[start : end : step].",
        "analogy_en": "Indexing is pointing at one person in a queue. Slicing is cutting out a whole section of the queue from person 1 to person 4.",
        "analogy_hi": "Indexing ka matlab line me khade ek bache ko bulana (`s[0]`). Slicing ka matlab ek tukda kaatna: `s[1:4]` (1 se 3 tak, 4 include nahi hoga).",
        "visual_type": "slice_diagram",
        "code": "text = 'PYTHON'\n# P  Y  T  H  O  N\n# 0  1  2  3  4  5\n#-6 -5 -4 -3 -2 -1\n\nprint(text[0])     # 'P' (First)\nprint(text[-1])    # 'N' (Last)\nprint(text[0:4])   # 'PYTH' (0 to 3, 4 is exclusive)\nprint(text[::-1])  # 'NOHTYP' (Reverse)",
        "notes_en": [
          "Indexing starts at 0. Negative indexing starts at -1 from the end.",
          "Start is INCLUSIVE. End is EXCLUSIVE (stop - 1).",
          "text[::-1] is the famous Python idiom to reverse a string in O(N) time."
        ],
        "notes_hi": [
          "Counting hamesha 0 se shuru hoti hai. Peeche se -1 se.",
          "End index kabhi shamil nahi hota! [1:4] sirf 1, 2, 3 dega.",
          "`[::-1]` string ko ulta (reverse) kar deta hai."
        ]
      },
      {
        "id": "replace_split",
        "title": "replace() & split()",
        "concept": "replace() substitutes substrings. split() cuts text into a list of words based on a separator.",
        "analogy_en": "replace() is 'Find and Replace' in Word. split() is taking scissors and cutting a sentence at every space to make flashcards.",
        "analogy_hi": "replace() purana word hata ke naya word lagata hai. split() sentence ko tod ke shabdon ki list bana deta hai.",
        "visual_type": "split_visual",
        "code": "date_str = '2026-09-16'\nparts = date_str.split('-')  # ['2026', '09', '16']\n\nfixed_phone = '011-456-789'.replace('-', ' ')\nprint(parts)\nprint(fixed_phone)",
        "notes_en": [
          "replace() does NOT modify the original string; it returns a new updated string.",
          "split() defaults to splitting on whitespace if no separator is specified."
        ],
        "notes_hi": [
          "`replace()` original string ko change nahi karta, naya string deta hai.",
          "`split()` by default spaces par divide karta hai."
        ]
      },
      {
        "id": "strip_case",
        "title": "strip(), lower(), and upper()",
        "concept": "strip() removes leading and trailing spaces. lower() and upper() standardize casing.",
        "analogy_en": "strip() cleans the dust from the edges of a photo. lower() ensures that 'Apple', 'apple', and 'APPLE' all look identical to computer comparisons.",
        "analogy_hi": "strip() aage-peeche ke faltu spaces saaf karta hai. lower() case sensitivity ka jhanjhat khatam karta hai taaki comparison safe ho.",
        "visual_type": "strip_box",
        "code": "name = '  Alex  '\nprint(name.strip())        # 'Alex'\nprint('Python'.lower())    # 'python'\nprint('Python'.upper())    # 'PYTHON'",
        "notes_en": [
          "strip() only removes edge spaces, NOT spaces in the middle.",
          "Always use .lower() or .upper() before comparing strings from user input."
        ],
        "notes_hi": [
          "`strip()` sirf kinaro ke space hatata hai, beech ke nahi.",
          "User input compare karne se pehle hamesha `.lower()` laga lo."
        ]
      }
    ]
  },
  {
    "id": "ch3_numbers",
    "number": 3,
    "title": "Working with Numbers",
    "badge": "Math & Logic",
    "slides": [
      {
        "id": "numeric_types",
        "title": "Python Numeric Types",
        "concept": "1. int (whole numbers, unlimited size)  2. float (decimals)  3. complex (real + imaginary).",
        "analogy_en": "Integers are whole countable objects (3 students). Floats are measurements (3.14 liters of water). Complex numbers are used in electrical engineering and advanced physics (2 + 3j).",
        "analogy_hi": "int: Pura number jaise 5 samosa. float: Decimal wala number jaise 98.6 fever. complex: Math aur engineering ke numbers jaise 2 + 3j.",
        "visual_type": "number_types",
        "code": "count = 15          # int\nprice = 99.50       # float\nwave = 3 + 5j       # complex\n\nprint(type(count))\nprint(type(price))",
        "notes_en": [
          "Python integers have arbitrary precision (they never overflow, even 2**1000).",
          "Floats follow IEEE-754 double-precision standard."
        ],
        "notes_hi": [
          "Python me integers kabhi overflow nahi hote, kitna bhi bada number ho sakta hai.",
          "Floats me precision ka limit hota hai."
        ]
      },
      {
        "id": "arithmetic_operators",
        "title": "Arithmetic Operators (// vs / vs % vs **)",
        "concept": "/ is float division, // is floor division (rounds down), % is remainder, ** is exponentiation.",
        "analogy_en": "7 / 2 is 3.5. But 7 // 2 asks: 'How many whole pizzas can 2 people get?' Answer: 3 pizzas. 7 % 2 asks: 'How many slices are left over?' Answer: 1 slice.",
        "analogy_hi": "7 / 2 = 3.5 (float). 7 // 2 = 3 (sirf whole number part). 7 % 2 = 1 (remainder ya bacha hua hissa). 2 ** 3 = 8 (2 ki power 3).",
        "visual_type": "math_table",
        "code": "print(7 / 2)   # 3.5 (Float division)\nprint(7 // 2)  # 3   (Floor division)\nprint(7 % 2)   # 1   (Modulo / Remainder)\nprint(2 ** 3)  # 8   (Power: 2^3)",
        "notes_en": [
          "// rounds down to nearest whole number (towards negative infinity).",
          "-7 // 2 gives -4, NOT -3!"
        ],
        "notes_hi": [
          "`//` hamesha chhota whole number leta hai.",
          "Negative numbers me dhyan rakhna: `-7 // 2` = `-4` hota hai!"
        ]
      },
      {
        "id": "rounding_tools",
        "title": "Rounding & Precision (round, ceil, floor, trunc)",
        "concept": "abs() removes negative sign. round() rounds half-to-even. ceil() rounds UP. floor() rounds DOWN. trunc() cuts decimals.",
        "analogy_en": "floor() is the floor beneath your feet (always goes down to 1). ceil() is the ceiling above your head (always goes up to 2). trunc() just chops off decimals with an axe.",
        "analogy_hi": "floor: Zameen (niche kheenchta hai 1.7 -> 1). ceil: Chhat (upar le jata hai 1.3 -> 2). trunc: Decimal part ko scissor se kaat deta hai.",
        "visual_type": "floor_ceil_chart",
        "code": "import math\n\nprint(abs(-15))         # 15\nprint(round(2.5))       # 2 (Banker's rounding to nearest even)\nprint(round(3.5))       # 4\nprint(math.floor(1.9))  # 1\nprint(math.ceil(1.1))   # 2",
        "notes_en": [
          "Python uses Banker's Rounding (round-half-to-even) to avoid statistical bias.",
          "math.ceil and math.floor require 'import math'."
        ],
        "notes_hi": [
          "Python banker's rounding use karta hai (nearest even number par round karta hai).",
          "`math.ceil` aur `math.floor` ke liye `import math` zaroori hai."
        ]
      },
      {
        "id": "random_module",
        "title": "Random Numbers (random & randint)",
        "concept": "random.random() gives float [0.0, 1.0). random.randint(a, b) gives random integer between a and b (inclusive).",
        "analogy_en": "randint(1, 6) is rolling a 6-sided dice in Ludo.",
        "analogy_hi": "randint(1, 6) ludo ki gotti phekne jaisa hai\u20141 se 6 ke beech koi bhi number nikal sakta hai.",
        "visual_type": "dice_visual",
        "code": "import random\n\ndice = random.randint(1, 6)\nprob = random.random()\nprint(f'Rolled: {dice}, Probability: {prob:.2f}')",
        "notes_en": [
          "randint(a, b) includes BOTH a and b.",
          "Results change on every single program execution."
        ],
        "notes_hi": [
          "`randint(1, 6)` me 1 aur 6 dono aane ke chances hote hain.",
          "Har baar run karne par naya number aayega."
        ]
      }
    ]
  },
  {
    "id": "ch4_logic",
    "number": 4,
    "title": "Logic & Operators",
    "badge": "Decision Making",
    "slides": [
      {
        "id": "control_flow_intro",
        "title": "Control Flow: Straight Line vs Decisions vs Loops",
        "concept": "1. Straight line code: sequential execution  2. Conditional: choose paths based on True/False  3. Loops: repeat blocks.",
        "analogy_en": "Straight line is a one-way highway. Conditionals are crossroads with traffic signs. Loops are roundabouts you circle until your exit condition is met.",
        "analogy_hi": "Straight line: seedha rasta. Conditionals: choraha jahan decide karte ho baayein jana hai ya daayein. Loops: gol chakkar jisme ghoomte rehte ho jab tak exit na mile.",
        "visual_type": "flowchart_types",
        "code": "# 1. Sequential\nx = 5\n# 2. Conditional\nif x > 0:\n    print('Positive')\n# 3. Loop\nfor i in range(3):\n    print(i)",
        "notes_en": [
          "Control flow determines how code executes at runtime.",
          "Conditions always evaluate to a Boolean (True or False)."
        ],
        "notes_hi": [
          "Control flow se code ka execution path control hota hai."
        ]
      },
      {
        "id": "truthy_falsy",
        "title": "Truthy and Falsy Values",
        "concept": "Python does not only check True or False. It checks whether a value is empty or meaningful.",
        "analogy_en": "An empty wallet, an empty plate, or zero coins are 'Falsy'. Any wallet with even 1 rupee, or a plate with food, is 'Truthy'.",
        "analogy_hi": "Khaali jeb, khaali plate, ya zero rupaye Falsy hain! Agar jeb me 1 rupaya bhi hai, ya string me 1 letter bhi hai, to wo Truthy hai.",
        "visual_type": "truthy_table",
        "code": "# Falsy values:\n# False, None, 0, 0.0, '', [], {}, set()\n\nitems = []\nif not items:\n    print('Cart is empty!')",
        "notes_en": [
          "Falsy: False, None, 0, 0.0, empty strings '', empty lists [], empty dicts {}.",
          "Truthy: Any non-zero number, non-empty string 'Hi', non-empty collection [1]."
        ],
        "notes_hi": [
          "Falsy: `0`, `None`, `False`, khaali string `''`, khaali list `[]`.",
          "Truthy: Baki sab kuch!"
        ]
      },
      {
        "id": "logical_operators",
        "title": "Logical Operators (and / or / not)",
        "concept": "'and' requires ALL conditions True. 'or' requires AT LEAST ONE condition True. 'not' reverses the Boolean.",
        "analogy_en": "To enter exam hall: 'Admit Card AND ID Card' (both needed). To get discount: 'Student ID OR Coupon' (either one is enough).",
        "analogy_hi": "Exam hall me entry: 'Admit Card AND ID Card' (dono chahiye, ek bhi missing to bahar). Canteen discount: 'Student Card OR Faculty Card' (koi ek chalega).",
        "visual_type": "logic_gates",
        "code": "has_id = True\nhas_admit = False\n\nif has_id and has_admit:\n    print('Entry Allowed')\nelse:\n    print('Entry Denied')  # This runs",
        "notes_en": [
          "Short-circuit evaluation:",
          "'and' stops as soon as it finds False.",
          "'or' stops as soon as it finds True."
        ],
        "notes_hi": [
          "Short-circuit: `and` pehla `False` dekhte hi aage check karna band kar deta hai.",
          "`or` pehla `True` dekhte hi aage check karna band kar deta hai."
        ]
      },
      {
        "id": "identity_vs_equality",
        "title": "Identity (is) vs Equality (==)",
        "concept": "== compares VALUES. 'is' compares MEMORY ADDRESSES (Identity).",
        "analogy_en": "Two people wearing identical black Nike shoes have '==' (same style). But they do NOT have 'is' (they are two distinct pairs of shoes in the physical world).",
        "analogy_hi": "Do dosto ke paas same model ka iPhone hai -> `a == b` is True (dono phone ek jaise hain). Par kya wo ek hi phone hai? Nahi -> `a is b` is False (dono ke paas alag dabbe hain).",
        "visual_type": "pointer_diagram",
        "code": "list1 = [1, 2, 3]\nlist2 = [1, 2, 3]\n\nprint(list1 == list2)  # True (Same values)\nprint(list1 is list2)  # False (Different memory locations!)\n\n# Always use 'is' with None:\nval = None\nprint(val is None)     # True",
        "notes_en": [
          "Always use 'is None' and 'is not None', never '== None'.",
          "Small integers (-5 to 256) are cached in CPython, so 'a is b' can be True for 256."
        ],
        "notes_hi": [
          "`is None` likhna standard rule hai, `== None` mat likho.",
          "`==` value check karta hai, `is` memory ka address dekhta hai."
        ]
      }
    ]
  },
  {
    "id": "ch5_conditionals",
    "number": 5,
    "title": "Conditional Statements",
    "badge": "Flow Control",
    "slides": [
      {
        "id": "if_else_elif",
        "title": "if, if-else, and elif Chains",
        "concept": "if: runs if True. if-else: two-way decision. elif: checks another condition if previous was False.",
        "analogy_en": "A traffic light: If red -> stop. Elif yellow -> get ready. Else green -> go.",
        "analogy_hi": "College attendance: If >= 75% -> eligible. Elif >= 65% -> medical certificate do. Else -> detain.",
        "visual_type": "decision_tree",
        "code": "score = 82\n\nif score >= 90:\n    grade = 'O'\nelif score >= 80:\n    grade = 'A+'\nelif score >= 70:\n    grade = 'A'\nelse:\n    grade = 'B'\n\nprint(f'Grade: {grade}')",
        "notes_en": [
          "Conditions are evaluated top to bottom.",
          "As soon as one condition is True, the rest of the chain is SKIPPED!"
        ],
        "notes_hi": [
          "Condition upar se niche check hoti hain.",
          "Jaise hi pehla True milta hai, baaki saare elif skip ho jate hain."
        ]
      },
      {
        "id": "independent_if",
        "title": "Independent 'if' Statements",
        "concept": "Multiple separate 'if' statements where every condition is checked, unlike elif which skips after the first match.",
        "analogy_en": "Airport baggage screening: Bag is checked for weight (if > 20kg), AND checked for liquids (if liquid), AND checked for batteries. All checks run independently.",
        "analogy_hi": "College admission verification: 10th marks check honge (if), 12th marks check honge (if), aur ID verify hogi (if). Teeno checks alag alag honge, ek pass hone se doosra skip nahi hoga.",
        "visual_type": "independent_paths",
        "code": "score = 85\n\n# All these if statements will be checked independently:\nif score >= 50:\n    print('Passed Exam')\nif score >= 80:\n    print('Distinction Merit')\nif score >= 100:\n    print('Perfect Score')",
        "notes_en": [
          "Use independent if when you need to validate multiple conditions on the same data.",
          "Use if-elif when choices are mutually exclusive (only one should win)."
        ],
        "notes_hi": [
          "Independent `if`: Jab saari conditions check karni hon.",
          "`if-elif`: Jab koi ek hi option select karna ho."
        ]
      },
      {
        "id": "inline_ternary",
        "title": "Inline if (Ternary Operator)",
        "concept": "A compact way to write conditional expressions in one line: Value_If_True if Condition else Value_If_False.",
        "analogy_en": "Quick shorthand decision: 'Pass' if marks >= 40 else 'Fail'.",
        "analogy_hi": "Ek line me decision: 'Eligible' agar attendance >= 75 warna 'Detained'.",
        "visual_type": "ternary_pill",
        "code": "marks = 78\nstatus = 'Pass' if marks >= 40 else 'Fail'\nprint(status)",
        "notes_en": [
          "Must include 'else'. Cannot omit else in ternary.",
          "Best for simple variable assignments; avoid nesting ternaries for readability."
        ],
        "notes_hi": [
          "Ternary me `else` likhna mandatory hai.",
          "Simple assignments ke liye best hai."
        ]
      },
      {
        "id": "match_case",
        "title": "match-case (Structural Pattern Matching)",
        "concept": "Modern Python 3.10+ control flow structure to match a value against multiple patterns cleanly.",
        "analogy_en": "Like a modern switch-case statement, but much more powerful with pattern decomposition and guard clauses.",
        "analogy_hi": "C/C++ ke switch-case jaisa, par Python me 10 guna zyada powerful. Payment method ya command match karne ke liye best.",
        "visual_type": "match_box",
        "code": "payment = 'UPI'\n\nmatch payment:\n    case 'UPI':\n        print('Open GPay or PhonePe')\n    case 'Card':\n        print('Enter 16-digit Card number')\n    case _:\n        print('Unknown payment method')",
        "notes_en": [
          "case _ acts as the default wildcard fallback (like 'default' in C switch).",
          "Introduced in Python 3.10."
        ],
        "notes_hi": [
          "`case _` default case hota hai jo sab kuch catch kar leta hai agar match na ho.",
          "Python 3.10 me introduce hua tha."
        ]
      }
    ]
  },
  {
    "id": "ch6_loops",
    "number": 6,
    "title": "Looping & Iterations",
    "badge": "Repetition",
    "slides": [
      {
        "id": "why_loops",
        "title": "Why Do We Need Loops?",
        "concept": "Loops move your program from 'Do this once' to 'Do this as many times as needed' automatically.",
        "analogy_en": "Instead of typing `print('Hello')` 100 times, a loop tells the computer: 'Repeat this 100 times while I drink coffee'.",
        "analogy_hi": "Agar 100 bacho ko marksheet bhejni hai, to haath se 100 baar code nahi likhenge. Loop 1 second me 100 bacho ka kaam nipta dega.",
        "visual_type": "loop_circle",
        "code": "for i in range(1, 6):\n    print(f'Sending notification #{i}')",
        "notes_en": [
          "for loop: best when iterating over a known sequence or collection.",
          "while loop: best when repetition depends on a dynamic condition."
        ],
        "notes_hi": [
          "`for` loop: Jab pata ho kitne items par ghoomna hai.",
          "`while` loop: Jab kisi condition ke False hone tak ghoomna ho."
        ]
      },
      {
        "id": "how_for_loop_works",
        "title": "How a for Loop Works Behind the Scenes",
        "concept": "Python takes an Iterable, creates an Iterator from it, calls next() repeatedly, and stops when StopIteration is raised.",
        "analogy_en": "The Iterable is a Pez candy dispenser. The Iterator is your thumb clicking the dispenser. Each click gives you `next()` candy. When empty, it stops.",
        "analogy_hi": "Iterable hai candies ka packet. Iterator hai tumhara haath jo ek-ek karke candy nikaalta hai (`next()`). Jab packet khaali ho jata hai to Python `StopIteration` bolke ruk jata hai.",
        "visual_type": "iterator_machine",
        "code": "nums = [10, 20, 30]\n# Behind the scenes of 'for x in nums:':\nit = iter(nums)\nprint(next(it))  # 10\nprint(next(it))  # 20\nprint(next(it))  # 30\n# next(it) -> Raises StopIteration exception",
        "notes_en": [
          "Any object with __iter__() or __getitem__() is an Iterable.",
          "An Iterator keeps track of current position in memory."
        ],
        "notes_hi": [
          "Python internal `iter()` aur `next()` protocol use karta hai.",
          "`StopIteration` aane par for loop naturally terminate hota hai."
        ]
      },
      {
        "id": "loop_controls",
        "title": "Loop Control: break, continue, pass",
        "concept": "break stops loop immediately. continue skips to next iteration. pass is a placeholder that does nothing.",
        "analogy_en": "break: fire alarm rings, exit building immediately! continue: this apple is rotten, skip it and check the next one. pass: construction site with a 'work in progress' sign.",
        "analogy_hi": "break: Emergency stop! continue: Is round ko chhod ke agle round par jao. pass: Khaali placeholder taaki syntax error na aaye.",
        "visual_type": "control_branch",
        "code": "for i in range(1, 6):\n    if i == 3:\n        continue  # Skips 3\n    if i == 5:\n        break     # Stops at 5\n    print(i)",
        "notes_en": [
          "break exits the innermost enclosing loop.",
          "continue jumps directly to the next loop cycle."
        ],
        "notes_hi": [
          "`break` loop ko tod deta hai.",
          "`continue` current step ko skip karke agle par jata hai."
        ]
      },
      {
        "id": "for_else_logic",
        "title": "The Secret for-else Statement",
        "concept": "The else block in a loop executes ONLY IF the loop finishes normally without hitting a 'break'.",
        "analogy_en": "Searching for lost keys: If you find keys -> break! Else (checked everywhere and never found) -> 'Keys are lost'. You don't need a boolean flag variable!",
        "analogy_hi": "Chabi dhoondhne jaisa: Chabi mil gayi to `break`! Agar pura kamra chhan liya aur break nahi hua, to `else` chalega: 'Chabi nahi mili'. Koi extra flag variable lagane ki zarurat nahi.",
        "visual_type": "for_else_cycle",
        "code": "numbers = [2, 4, 6, 8]\ntarget = 5\n\nfor n in numbers:\n    if n == target:\n        print('Found target!')\n        break\nelse:\n    print('Target not found in the list!')  # This executes",
        "notes_en": [
          "CRITICAL: Loop completed naturally -> run else.",
          "Loop terminated by break -> skip else."
        ],
        "notes_hi": [
          "Agar loop pura bina `break` ke chala, tabhi `else` run hoga.",
          "Agar beech me `break` ho gaya to `else` skip ho jayega."
        ]
      },
      {
        "id": "nested_for_hierarchy",
        "title": "Nested Loops & Hierarchy",
        "concept": "A loop inside another loop. The inner loop completes all its iterations for every single step of the outer loop.",
        "analogy_en": "Navigating time: For every Year -> loop through Months -> loop through Days. Or Database: For every Table -> loop through Columns -> loop through Rows.",
        "analogy_hi": "Ghadi ki sui jaisi: Minute ki sui 60 baar ghoomti hai tab ghante ki sui sirf 1 step aage badhti hai.",
        "visual_type": "nested_clock",
        "code": "for row in range(1, 4):\n    for col in range(1, 4):\n        print(f'({row}, {col})', end=' ')\n    print()",
        "notes_en": [
          "Total iterations = Outer Count x Inner Count.",
          "Watch out for computational complexity: O(N^2) or O(N^3)."
        ],
        "notes_hi": [
          "Total iterations dono loops ka multiplication hota hai.",
          "Bohot zyada nesting se code slow ho jata hai."
        ]
      },
      {
        "id": "while_loops",
        "title": "while Loops & while True",
        "concept": "while repeats as long as condition is True. while True creates an infinite loop that requires an internal break.",
        "analogy_en": "A water tank filling up: 'while water_level < 100: fill_water()'. If you forget to increase water_level, the tap runs forever and floods the house!",
        "analogy_hi": "Tanki bharne jaisa: Jab tak paani ka level 100 na ho, bharte raho. Agar counter badhana bhool gaye, to tanki overflow ho jayegi (infinite loop).",
        "visual_type": "while_infinite_guard",
        "code": "# Safe while loop\ncount = 1\nwhile count <= 3:\n    print(f'Attempt #{count}')\n    count += 1  # MUST update condition variable!\n\n# while True with break condition\nwhile True:\n    token = input('Enter token (or exit): ')\n    if token == 'exit':\n        break",
        "notes_en": [
          "Critical Rule: The condition variable must be updated inside the while loop.",
          "while True is common in server listening, event loops, and gaming frames."
        ],
        "notes_hi": [
          "Zaroori Niyam: while loop ke andar counter ko hamesha badhao.",
          "`while True` games aur servers me hamesha active rehne ke liye use hota hai."
        ]
      }
    ]
  },
  {
    "id": "ch7_data_structures",
    "number": 7,
    "title": "Data Structures & Collections",
    "badge": "Core Memory",
    "slides": [
      {
        "id": "why_data_structures",
        "title": "Why We Need Data Structures",
        "concept": "Without data structures, you have scattered separate variables (cost1, cost2, cost3...). With data structures, you group data in one scalable container: costs = [10, 15, 20].",
        "analogy_en": "Without a suitcase, you carry 15 clothes scattered in your hands (they drop). With a suitcase (List), everything is packed in one organized container.",
        "analogy_hi": "Bina data structure ke 50 bacho ke marks ke liye 50 alag variables banane padte (`m1, m2, m3...`). List use karke ek dabbe me saare marks aa jate hain: `marks = [45, 88, 92...]`.",
        "visual_type": "suitcase_visual",
        "code": "# Without: cost1=10; cost2=15; cost3=20; total = cost1+cost2+cost3\n# With:\ncosts = [10, 15, 20, 25, 30]\ntotal_cost = sum(costs)\nprint(f'Total: {total_cost}')",
        "notes_en": [
          "Cleaner code, easy processing, and scales to millions of items."
        ],
        "notes_hi": [
          "Clean code, loop lagane me asani, aur scalable system."
        ]
      },
      {
        "id": "four_structures",
        "title": "The 4 Core Data Structures (List, Tuple, Set, Dict)",
        "concept": "1. List []: Ordered, Mutable, Allows duplicates  2. Tuple (): Ordered, Immutable, Allows duplicates  3. Set {}: Unordered, Mutable, Unique only  4. Dict {k:v}: Key-Value pairs, Unique keys.",
        "analogy_en": "List: Shopping list (can add/remove/repeat). Tuple: Your Aadhaar/Passport birth date (fixed forever). Set: Unique fingerprints in a database. Dict: Phonebook (Name -> Phone Number).",
        "analogy_hi": "List: Kirana list (badal sakte ho). Tuple: Date of Birth (kabhi badal nahi sakti, locked). Set: Fingerprints (har aadmi ka unique, duplicate allowed nahi). Dict: Phone contact (Naam -> Number).",
        "visual_type": "comparison_matrix",
        "code": "my_list = [10, 20, 20]           # Duplicates OK, Mutable\nmy_tuple = (10, 20, 20)          # Locked! Immutable\nmy_set = {10, 20}                # Automatically removes duplicates\nmy_dict = {'alex': 90, 'raj': 85} # Key -> Value mapping",
        "notes_en": [
          "List: Most versatile, default choice.",
          "Tuple: Faster and safer for fixed data.",
          "Set: Ultra-fast O(1) membership testing and math operations.",
          "Dict: Ultra-fast O(1) key lookups."
        ],
        "notes_hi": [
          "List: Sabse zyada use hone wali collection.",
          "Tuple: Safe aur memory efficient.",
          "Set: Duplicate hatane ke liye best.",
          "Dict: Key se value dhoondhne ke liye best."
        ]
      },
      {
        "id": "lists_behind_scenes",
        "title": "Lists Behind the Scenes (Memory Model)",
        "concept": "A list in Python does NOT store raw values directly. It stores an array of memory references (pointers) to objects!",
        "analogy_en": "A list is not a shelf of heavy books. It is an index card containing the room numbers where each book is located in the library.",
        "analogy_hi": "List apne andar actual data nahi rakhti, balki memory addresses (pointers) rakhti hai. Isliye list me int, string, float sab mix ho sakte hain!",
        "visual_type": "pointer_array",
        "code": "mixed = [1, 'Alex', True, None]\n# mixed stores [0x0123, 0x0124, 0x0125, 0x0126]\n# Each address points to a PyObject in heap memory!",
        "notes_en": [
          "Lists store contiguous arrays of pointers in CPython.",
          "This is why Python lists can store mixed heterogeneous data types!"
        ],
        "notes_hi": [
          "List memory references store karti hai, actual data nahi.",
          "Isi wajah se Python list me heterogeneous elements aa sakte hain."
        ]
      },
      {
        "id": "unpacking_star_underscore",
        "title": "Unpacking: Star (*) & Underscore (_) Operators",
        "concept": "* collects remaining items as a list. _ acts as a throwaway variable to ignore unwanted values.",
        "analogy_en": "You have a parcel: you take the first item (Name), throw the packing peanuts into the dustbin (_), and put all the other items into a pouch (*rest).",
        "analogy_hi": "List unpacking: Pehla item chahiye (`first`), aakhri chahiye (`last`), aur beech ka saara kachra ignore karna hai (`*_`).",
        "visual_type": "unpack_parcel",
        "code": "scores = [98, 45, 67, 82, 91]\nfirst, *middle, last = scores\n\nprint(f'Topper: {first}')      # 98\nprint(f'Middle pack: {middle}') # [45, 67, 82]\nprint(f'Last: {last}')         # 91\n\n# Ignore middle with _:\nstart, *_, end = scores",
        "notes_en": [
          "Only one starred variable (*) is allowed in an unpacking assignment.",
          "Underscore (_) tells developers and linters: 'I deliberately don't care about this value'."
        ],
        "notes_hi": [
          "Puri unpacking me sirf ek `*` allowed hota hai.",
          "`_` ka matlab hai 'ye value mere kaam ki nahi hai'."
        ]
      },
      {
        "id": "shallow_vs_deep_copy",
        "title": "Assignment vs Shallow Copy vs Deep Copy",
        "concept": "Assignment (b = a) shares reference. Shallow copy (a.copy()) clones outer list only. Deep copy (copy.deepcopy(a)) clones nested structures completely.",
        "analogy_en": "Assignment is giving your friend a second key to your house. Shallow copy is cloning the house, but both houses still share the same safe! Deep copy is building an independent duplicate house with its own duplicate safe.",
        "analogy_hi": "`b = a`: Ek hi ghar ki do chabiyan (dono ek hi list ko change karenge). `a.copy()`: Bahar ka dabba naya par andar ke dabbe wahi purane. `deepcopy()`: Sab kuch naya copy (100% independent).",
        "visual_type": "copy_tree",
        "code": "import copy\n\norig = [[1, 2], [3, 4]]\nshallow = orig.copy()\ndeep = copy.deepcopy(orig)\n\norig[0][0] = 999\nprint(shallow[0][0])  # 999! (Shared nested reference)\nprint(deep[0][0])     # 1   (Completely independent!)",
        "notes_en": [
          "Assignment (b = a) is NOT copying! It creates a new variable pointing to the SAME object.",
          "Always use deepcopy for nested 2D matrices or nested dictionaries."
        ],
        "notes_hi": [
          "`b = a` se copy nahi banta! Dono same memory ko point karte hain.",
          "Nested lists me hamesha `copy.deepcopy()` use karo."
        ]
      },
      {
        "id": "list_comprehensions",
        "title": "List Comprehensions",
        "concept": "[Transformation for Item in Iterable if Filter] \u2014 Loop + Optional Filter + Transformation all in one elegant line.",
        "analogy_en": "Instead of setting up a factory conveyor belt with manual if checks and append bins, list comprehension is a high-speed laser cutter producing finished items in one breath.",
        "analogy_hi": "Pehle khaali list banao, fir for loop lagao, fir if lagao, fir append karo (4 line). List comprehension me ye saara kaam 1 single line me ho jata hai!",
        "visual_type": "comprehension_pipe",
        "code": "# Standard way (4 lines):\nevens = []\nfor x in range(10):\n    if x % 2 == 0:\n        evens.append(x * 2)\n\n# List comprehension (1 line):\nevens_comp = [x * 2 for x in range(10) if x % 2 == 0]\nprint(evens_comp)  # [0, 4, 8, 12, 16]",
        "notes_en": [
          "Faster execution in CPython bytecode compared to manual .append() calls.",
          "Keep it readable; avoid multiple nested comprehensions."
        ],
        "notes_hi": [
          "CPython me regular loop se zyada fast chalta hai.",
          "Code clean aur professional lagta hai."
        ]
      }
    ]
  },
  {
    "id": "ch8_functions",
    "number": 8,
    "title": "Functions & Professional Python",
    "badge": "Modularity",
    "slides": [
      {
        "id": "what_is_function",
        "title": "What is a Function?",
        "concept": "A small, reusable block of code that does one specific job. They are the foundation of professional software.",
        "analogy_en": "Without functions, your program is like cooking a 10-course meal in one giant pot (chaos). With functions, each dish has its own recipe and chef.",
        "analogy_hi": "Bina function ke code 1000 line ka kachra ban jata hai jisme ek bug dhoondhna namumkin hota hai. Function code ko chhote chhote reusable blocks me baant deta hai.",
        "visual_type": "blackbox_func",
        "code": "def calculate_tax(salary):\n    \"\"\"Calculates 10% tax on annual salary.\"\"\"\n    return salary * 0.10\n\nnet_tax = calculate_tax(850000)\nprint(f'Tax: {net_tax}')",
        "notes_en": [
          "Define once with 'def', call many times.",
          "Defining a function does NOT run it; it only creates the function object in memory."
        ],
        "notes_hi": [
          "`def` se define karo, naam likh kar call karo.",
          "Define karne se code run nahi hota, jab call karoge tabhi chalega."
        ]
      },
      {
        "id": "params_vs_args",
        "title": "Parameters vs Arguments",
        "concept": "Parameters are the variable names in the function definition (the placeholder). Arguments are the actual values passed during the call.",
        "analogy_en": "Parameter is the empty cup holder in your car (it expects a cup). Argument is the actual Starbucks coffee cup you place into it.",
        "analogy_hi": "Parameter function banate waqt ka khaali placeholder hai (`def add(a, b)`). Argument wo actual value hai jo tum call karte waqt dete ho (`add(5, 10)`).",
        "visual_type": "param_arg_handshake",
        "code": "def greet(user_name):  # 'user_name' is the PARAMETER (placeholder)\n    print(f'Hello {user_name}')\n\ngreet('Priyanshu')     # 'Priyanshu' is the ARGUMENT (actual value)",
        "notes_en": [
          "Parameters exist inside the definition.",
          "Arguments exist in the call."
        ],
        "notes_hi": [
          "Parameter definition me hota hai.",
          "Argument call karte waqt diya jata hai."
        ]
      },
      {
        "id": "variable_scope_lifetime",
        "title": "Variable Scope & Lifetime (Local vs Global)",
        "concept": "Parameters & Local variables exist only during function execution and are destroyed when the function finishes. Globals live until the program stops.",
        "analogy_en": "A hotel room card (Local) only opens your hotel room and expires when you check out. Your Passport (Global) works everywhere in the country.",
        "analogy_hi": "Local variable function ka private room hai. Function khatam hote hi local variable memory se delete ho jata hai. Global variable bahar rehta hai aur sabko dikhta hai.",
        "visual_type": "scope_boxes",
        "code": "global_val = 100  # Global (Accessible everywhere)\n\ndef test_scope():\n    local_val = 25  # Local (Destroyed after function ends!)\n    print(local_val)\n\ntest_scope()\n# print(local_val) -> NameError: name 'local_val' is not defined!",
        "notes_en": [
          "Local variables are not accessible outside the function.",
          "Modifying globals inside functions requires the 'global' keyword (use sparingly)."
        ],
        "notes_hi": [
          "Local variable function ke bahar se access nahi ho sakta.",
          "Function khatam hote hi local memory clean ho jati hai."
        ]
      },
      {
        "id": "args_kwargs",
        "title": "*args & **kwargs (Flexible Arguments)",
        "concept": "*args collects arbitrary positional arguments into a TUPLE. **kwargs collects arbitrary keyword arguments into a DICTIONARY.",
        "analogy_en": "*args is a backpack where you throw as many apples as you want. **kwargs is a labeled crate where every item has a name tag (e.g. name='Alex', age=21).",
        "analogy_hi": "`*args` ek jhola hai jisme bina naam ke kitne bhi arguments daal do (tuple ban jata hai). `**kwargs` ek box hai jisme key-value pairs aate hain (dictionary ban jati hai).",
        "visual_type": "args_backpack",
        "code": "def order_food(*items, **details):\n    print('Items ordered (tuple):', items)\n    print('Delivery details (dict):', details)\n\norder_food('Pizza', 'Burger', 'Coke', address='Hostel 3', phone='9876543210')",
        "notes_en": [
          "*args handles varying number of inputs.",
          "**kwargs handles optional configuration and metadata."
        ],
        "notes_hi": [
          "`*args` se kitne bhi values bhej sakte ho.",
          "`**kwargs` se named parameters handle hote hain."
        ]
      },
      {
        "id": "print_vs_return",
        "title": "print() vs return",
        "concept": "print() displays a value on the screen for humans and returns None. return sends a value back to the caller for programs to store and use.",
        "analogy_en": "print() is a waiter saying 'Your food is ready' aloud (you hear it, but you can't eat the words). return is the waiter actually handing you the plate of food so you can eat it!",
        "analogy_hi": "`print()` sirf screen par show karta hai (insano ke dekhne ke liye). `return` program ko value wapis deta hai taaki aage math ya logic chal sake.",
        "visual_type": "return_plate",
        "code": "def add_print(a, b):\n    print(a + b)  # Shows on screen, but returns None!\n\ndef add_return(a, b):\n    return a + b  # Gives result back to code\n\nx = add_print(2, 3)    # Prints 5, but x is None!\n# x + 10 -> TypeError: unsupported operand type for None and int\n\ny = add_return(2, 3)   # y is 5\nprint(y + 10)          # 15 (Works perfectly!)",
        "notes_en": [
          "If a function lacks a return statement, it implicitly returns None.",
          "Always use return when you need the result in further calculations."
        ],
        "notes_hi": [
          "Agar function me `return` nahi likha, to Python `None` return karta hai.",
          "Calculation aage badhane ke liye hamesha `return` use karo."
        ]
      },
      {
        "id": "four_function_types",
        "title": "The 4 Types of Functions by Purpose",
        "concept": "1. Action (side effect: print, write file, save DB)  2. Transformation (pure computation: input -> output)  3. Validation (checks rules, returns True/False)  4. Orchestrator (conductor: controls workflow).",
        "analogy_en": "1. Action: The Delivery Guy (performs action outside). 2. Transformation: The Chef (turns raw veggies into dish). 3. Validation: The Food Inspector (passes/fails quality). 4. Orchestrator: The Restaurant Manager (coordinates everyone).",
        "analogy_hi": "1. Action: Jo bahar kaam kare (email bhejna, DB me save karna). 2. Transformation: Data ko clean/calculate karna. 3. Validation: Check karna ki data valid hai ya nahi (True/False). 4. Orchestrator: Manager jo baaki sabhi functions ko line se call kare.",
        "visual_type": "four_roles",
        "code": "# 1. Validation\ndef is_valid_email(email):\n    return '@' in email and '.' in email\n\n# 2. Transformation\ndef clean_text(text):\n    return text.strip().lower()\n\n# 3. Action\ndef send_welcome_email(user_email):\n    print(f'Sending email to {user_email}')\n\n# 4. Orchestrator\ndef register_user(raw_email):\n    if is_valid_email(raw_email):\n        clean = clean_text(raw_email)\n        send_welcome_email(clean)\n        return True\n    return False",
        "notes_en": [
          "Professional code separates functions by their clear purpose.",
          "Avoid mixing transformation logic with side effects inside the same function."
        ],
        "notes_hi": [
          "Professional developers har function ko ek specific role dete hain.",
          "Calculation aur file saving ko ek hi function me mix mat karo."
        ]
      }
    ]
  }
];
