import json

tree = [
  # =========================================================================
  # CHAPTER 0: THE BIG AWAKENING
  # =========================================================================
  {
    "id": "ch_0_intro",
    "title": "Chapter 0: The Big Awakening",
    "subtitle_en": "What is Coding? Why Python? What Can You Build?",
    "subtitle_hi": "Coding kya hai? Python kyun chahiye? Isse kya-kya bana sakte ho?",
    "icon": "🚀",
    "subtopics": [
      {
        "id": "sub_0_1_how_cpu_thinks",
        "title": "How Computers Think (The Superfast Idiot Secret)",
        "title_hi": "Computer kaise sochta hai? (Superfast Gadha)",
        "icon": "🧠",
        "duration": "4 mins",
        "xp": 50,
        "what_is_it_en": "A computer is not an intelligent brain. It is merely a lightning-fast calculation engine that blindly executes instructions step-by-step. 'Coding' is simply writing an unambiguous set of instructions (a recipe) for this machine.",
        "what_is_it_hi": "Computer koi jaadugar ya insaan jaisa samajhdaar nahi hai. Ye bas ek superfast calculation machine hai jo bina apna dimaag lagaye tumhare orders follow karta hai. 'Coding' ka matlab bas computer ke liye bina kisi confusion ke step-by-step recipe likhna hai!",
        "why_need_it_en": "Computers do not understand human feelings or vague hints. Without precise instructions, a computer cannot calculate a single bank balance, store an image, or run an app. You must tell it EXACTLY what to do, step by step.",
        "why_need_it_hi": "Computer ko tumhari bolchaal ki bhasha ya ishare samajh nahi aate. Agar use ek bhi step galat doge to wo crash ho jayega. Isliye hume computer ki bhasha me exact aur clear steps likhne padte hain.",
        "how_to_use_en": "You write instructions line-by-line using commands like `print()` to tell the computer to show text on the screen.",
        "how_to_use_hi": "Hum computer ko built-in commands dete hain. Jaise screen par koi message dikhane ke liye `print('Tumhara Message')` likha jata hai.",
        "syntax": "print(\"Exact text to display on screen\")",
        "rules_en": [
          "Case Sensitivity Rule: `print()` is valid. `Print()` or `PRINT()` will crash with `NameError`.",
          "Quote Matching Rule: Text strings must start and end with the exact same quote type (single `'...'` or double `\"...\"`).",
          "Parentheses Pairing: Every opening `(` must have a corresponding closing `)`.",
          "Sequential Execution: The computer runs your code strictly from top to bottom, one line at a time."
        ],
        "rules_hi": [
          "Case Sensitivity Niyam: Python me `print()` chhota hi likhna padega. Bada `Print()` ya `PRINT()` likhoge to computer crash ho jayega (`NameError`).",
          "Quotes ka Niyam: Text likhte waqt shuru aur aakhir me same quote hona chahiye — `'Hello'` ya `\"Hello\"`. Ek single aur ek double quote lagane par syntax error aayega.",
          "Brackets ka Niyam: Har khulne wale bracket `(` ke sath closing bracket `)` lagana mandatory hai.",
          "Top-to-Bottom Niyam: Computer hamesha pehli line se aakhri line tak ek-ek karke code chalaata hai."
        ],
        "analogy_en": "Think of the computer as a robot chef in a restaurant. If you say 'make food', it will freeze. But if you say '1. Take 2 eggs. 2. Boil for 5 minutes. 3. Add salt', it delivers a 5-star dish in 1 second. Code is that exact recipe!",
        "analogy_hi": "Computer ko ek robot chef samjho. Agar tum use bologe 'khana banao', wo confuse ho jayega. Lekin agar bologe '1. 2 cup paani ubaalo. 2. Maggi daalo. 3. 2 minute pakao', to wo 1 second me mast Maggi bana dega! Code wahi exact step-by-step recipe hai.",
        "example_1": {
          "title": "Giving the Computer a Voice",
          "title_hi": "Computer ko aawaaz dena (Pehla Instruction)",
          "code": "print('Hello, World!')\nprint('I am officially giving orders to a computer!')",
          "explanation_en": "• Line 1: `print()` sends 'Hello, World!' to the console.\n• Line 2: Runs immediately after Line 1 and prints the second line on a new row.",
          "explanation_hi": "• Line 1: `print()` computer ko screen par 'Hello, World!' dikhane ka order deta hai.\n• Line 2: Pehli line ke theek baad doosri line screen par print hoti hai."
        },
        "example_2": {
          "title": "Real World: Automated Server Startup Banner",
          "title_hi": "Real World: Server Startup Notification",
          "code": "print('=== SYSTEM ONLINE ===')\nprint('Status: Server running on port 8080')\nprint('Waiting for client connections...')",
          "explanation_en": "• Real production servers print these startup banners when initializing.",
          "explanation_hi": "• Real production backend servers start hote waqt engineer ko yahi print karke batate hain ki server ready hai."
        },
        "challenge": {
          "prompt_en": "Write a Python instruction to print the exact message: `I am a future Python Pro`",
          "prompt_hi": "Python instruction likho jo screen par exact print kare: `I am a future Python Pro`",
          "starter_code": "# Write your print statement below:\n",
          "expected_output": "I am a future Python Pro",
          "solution_code": "print('I am a future Python Pro')",
          "solution_explanation_hi": "`print('I am a future Python Pro')` likhne se computer exact wahi text terminal me display kar deta hai.",
          "ego_roast_hi": "Bhai sirf ek print line likhni hai! 6th class ka bachha bhi 10 second me likh deta hai. Jaldi type karo!",
          "ego_cheer_hi": "BOOM! 💥 Tumne computer ko pehla order de diya! Ab tum official coder ban chuke ho!"
        }
      },
      {
        "id": "sub_0_2_why_python",
        "title": "Why Python Over C++ / Java? (The Human-Friendly Giant)",
        "title_hi": "Python kyun seekhein? (C++ aur Java se 10x Aasaan)",
        "icon": "🐍",
        "duration": "4 mins",
        "xp": 50,
        "what_is_it_en": "Python is a high-level, human-readable programming language. It is designed so that reading Python code feels like reading simple English sentences.",
        "what_is_it_hi": "Python ek aisi programming language hai jise aam insaani English jaisa banaya gaya hai. Isko padhna aur likhna bilkul aam English sentences jaisa hota hai.",
        "why_need_it_en": "In older languages like C++ or Java, printing 'Hello World' takes 7+ lines of complex boilerplate (`class`, `public static void main`, `System.out.println`). In Python, it takes 1 clean line.",
        "why_need_it_hi": "Agar Java ya C++ me chhota sa naam bhi print karna ho, to 7-8 line ka kathin boilerplate likhna padta hai. Python me wahi kaam bina kisi headache ke sirf 1 line me ho jata hai!",
        "how_to_use_en": "Write concise statements without semicolons `;` or enclosing curly brackets `{}`.",
        "how_to_use_hi": "Bina kisi semicolon `;` ya curly brackets `{}` ke direct aur saaf code likho.",
        "syntax": "# Java/C++ needs 7 lines. Python needs 1:\nprint(\"Clean, fast, readable\")",
        "rules_en": [
          "Zero Semicolons: Semicolons `;` at line ends are unnecessary and considered bad practice in Python.",
          "Code Readability Counts: Always write clear, simple logic over clever unreadable shortcuts.",
          "Indentation Over Brackets: Python uses 4-space indentation to define blocks, not curly braces `{}`."
        ],
        "rules_hi": [
          "Semicolon ki Chutti: Python me line ke aakhir me semicolon `;` lagane ki koi zarurat nahi hoti.",
          "Readability ka Niyam: Code jitna simple hoga, utna jaldi chalega aur bugs aane ke chances kam honge.",
          "Indentation ka Niyam: Python me curly braces `{}` nahi hote; blocks barabar space (indentation) se bante hain."
        ],
        "analogy_en": "C++ is like driving a manual 18-gear truck with tricky clutch controls. Python is like driving a Tesla on autopilot — you just tell it where to go!",
        "analogy_hi": "C++ ya Java chalana 18 gears wale puraane truck jaisa hai jisme har clutch sambhalna padta hai. Python automatic Tesla jaisi hai — bas destination batao aur gaadi chal padti hai!",
        "example_1": {
          "title": "Clean Multi-Line Output",
          "title_hi": "Multiple lines bina kisi headache ke print karna",
          "code": "print('1. Clean English syntax')\nprint('2. No ugly semicolons')\nprint('3. 10x faster development')",
          "explanation_en": "• Shows how clean and readable Python code looks compared to boilerplate-heavy languages.",
          "explanation_hi": "• Dikhata hai ki bina kisi faltu symbols ke Python code kitna saaf dikhta hai."
        },
        "example_2": {
          "title": "Real World: Instant Math Engine",
          "title_hi": "Real World: Direct Mathematical Calculation",
          "code": "print(250 + 750)\nprint(50 * 20)",
          "explanation_en": "• Python acts as a high-powered calculator directly without needing variable setup.",
          "explanation_hi": "• Python direct bina kisi setup ke bade se bade calculation 1 millisecond me solve kar deta hai."
        },
        "challenge": {
          "prompt_en": "Print the result of multiplying 25 by 4 directly inside a print statement. Expected output: `100`",
          "prompt_hi": "Print statement ke andar 25 aur 4 ko multiply karke result print karo. Expected output: `100`",
          "starter_code": "# Multiply 25 by 4 inside print:\n",
          "expected_output": "100",
          "solution_code": "print(25 * 4)",
          "solution_explanation_hi": "`print(25 * 4)` direct calculation karke 100 print kar deta hai.",
          "ego_roast_hi": "Bhai 25 * 4 bhi calculate nahi ho raha? Calculator mat dhoondo, Python hi calculator hai!",
          "ego_cheer_hi": "Shaandar! ⚡ Tumne dekha Python kitna direct aur simple hai!"
        }
      },
      {
        "id": "sub_0_3_what_can_you_do",
        "title": "What Can You Build with Python? (The Real Superpowers)",
        "title_hi": "Python se kya-kya bana sakte ho? (Real Superpowers)",
        "icon": "🌐",
        "duration": "5 mins",
        "xp": 50,
        "what_is_it_en": "Python is a multi-paradigm, general-purpose language. It powers Artificial Intelligence (OpenAI, ChatGPT), Web Backends (Instagram, YouTube), Data Science (Netflix algorithms), and Cybersecurity.",
        "what_is_it_hi": "Python ek 'General Purpose' bhasha hai. Iska matlab ye kisi ek kaam tak seemit nahi hai — chahe AI banana ho (ChatGPT), Web Backends (Instagram, YouTube), Data Science (Netflix recommendation) ya hacking tools, sab Python se bante hain.",
        "why_need_it_en": "By learning Python once, you gain the superpower to build almost anything in tech without having to learn 10 different languages.",
        "why_need_it_hi": "Ek baar Python seekh li, to alag-alag fields ke liye 10 nayi bhashayein nahi seekhni padengi. Ek hi language se tum bot bhi bana loge aur machine learning model bhi!",
        "how_to_use_en": "You write core Python logic and connect it with pre-built professional libraries (like Django for web, PyTorch for AI).",
        "how_to_use_hi": "Python ke basic logic ko industry ki libraries ke sath jod kar bade-bade projects banaye jaate hain.",
        "syntax": "# 1. Web: Flask / Django\n# 2. AI: PyTorch / TensorFlow\n# 3. Data: Pandas / NumPy",
        "rules_en": [
          "Master Core Logic First: Never jump into advanced AI libraries until you master Variables, Conditions, Loops, and Functions.",
          "Understand Under-the-hood: Understand how data moves in memory before building complex apps."
        ],
        "rules_hi": [
          "Basics Pehle Master Karo: AI ya Web development me jaane se pehle Variables, Conditions, Loops aur Functions me pakad hona zaroori hai.",
          "Logic First: Code ratna nahi hai, logic dimaag me step-by-step banana hai."
        ],
        "analogy_en": "Learning Python is like getting a Master Key. With this one key, you can unlock the door to AI, the door to Web Apps, and the door to Automation!",
        "analogy_hi": "Python seekhna ek Master Key milne jaisa hai. Is ek chaabi se tum AI ka darwaza bhi khol sakte ho, Web Apps ka bhi aur Automation ka bhi!",
        "example_1": {
          "title": "Automated Status Pipeline",
          "title_hi": "Automated Status Pipeline",
          "code": "project = 'Instagram Auto-Scheduler'\nstatus = 'Completed in 15ms'\nprint(project + ' -> ' + status)",
          "explanation_en": "• Combines strings to create automated operational messages.",
          "explanation_hi": "• String ko jodkar automated task report print karta hai."
        },
        "example_2": {
          "title": "Real World: AI Prediction Confidence",
          "title_hi": "Real World: AI Decision Confidence",
          "code": "label = 'Fraudulent Transaction'\nconfidence = 98.7\nprint(f'Alert: {label} detected with {confidence}% confidence!')",
          "explanation_en": "• Outputs real-time AI security detection alerts.",
          "explanation_hi": "• AI fraud detection model ka output alert ke roop me print karta hai."
        },
        "challenge": {
          "prompt_en": "Print: `Python powers AI, Web, and Automation!`",
          "prompt_hi": "Print karo: `Python powers AI, Web, and Automation!`",
          "starter_code": "# Write the exact print statement:\n",
          "expected_output": "Python powers AI, Web, and Automation!",
          "solution_code": "print('Python powers AI, Web, and Automation!')",
          "solution_explanation_hi": "Exact wahi text quotes ke andar pass karke print kiya.",
          "ego_roast_hi": "Bhai spelling check karo! Ek bhi letter galat hua to computer reject kar dega!",
          "ego_cheer_hi": "Chapter 0 Conquered! 🚀 Ab tum asli memory aur data structures me enter karne ke liye ready ho!"
        }
      }
    ]
  },

  # =========================================================================
  # CHAPTER 1: MEMORY, VARIABLES & USER INPUT
  # =========================================================================
  {
    "id": "ch_1_variables",
    "title": "Chapter 1: Memory, Variables & User Input",
    "subtitle_en": "Variables, Data Types, input(), and Type Casting",
    "subtitle_hi": "Variables, Data Types, input() aur Type Casting ka Masterclass",
    "icon": "📦",
    "subtopics": [
      {
        "id": "sub_1_1_variables_mental_model",
        "title": "What is a Variable? (RAM Storage Lockers & Naming Rules)",
        "title_hi": "Variable kya hota hai? (RAM Storage Lockers & Naming Rules)",
        "icon": "🏷️",
        "duration": "5 mins",
        "xp": 60,
        "what_is_it_en": "A variable is a named storage location in your computer's RAM (memory) that holds a piece of data so you can use, modify, and refer to it later in your program.",
        "what_is_it_hi": "Variable tumhare computer ki RAM (memory) ke andar ek aisa dabba (storage locker) hota hai jiska ek naam hota hai. Us dabbe me tum koi bhi data (number, naam, score) store karte ho taaki baad me use kar sako.",
        "why_need_it_en": "Without variables, every calculation would be immediately forgotten by the CPU. If you calculate an order total of $450, you must store it in a variable, otherwise you cannot apply discounts or print the receipt.",
        "why_need_it_hi": "Agar variables na hote, to computer jo bhi calculation karta use agle hi second bhool jata! Agar tumne kisi customer ka bill calculate kiya, to use kisi variable me store karna padega taaki baad me discount de sako ya receipt print kar sako.",
        "how_to_use_en": "Write the variable name on the left, an equals sign `=` (the assignment operator), and the value on the right.",
        "how_to_use_hi": "Left side me variable ka naam likho, beech me `=` lagao, aur right side me uski value likho. Computer right side ki value ko left wale dabbe me daal deta hai.",
        "syntax": "variable_name = value\n# Example:\nage = 21\nuser_name = \"Priyanshu\"",
        "rules_en": [
          "1. Cannot Start with a Number: `1player` is illegal (SyntaxError). `player1` is valid.",
          "2. No Spaces or Dashes: `user name` or `user-name` is illegal. Use snake_case: `user_name`.",
          "3. Only Letters, Numbers, and Underscores: Special characters like `@`, `$`, `%`, `!` are strictly forbidden.",
          "4. Case Sensitive: `age`, `Age`, and `AGE` are 3 completely separate variables in memory!",
          "5. No Python Keywords: You cannot name a variable `print`, `def`, `class`, `if`, or `while`."
        ],
        "rules_hi": [
          "1. Number se shuru nahi ho sakta: `1score` likhoge to error aayega. `score1` likh sakte ho.",
          "2. Space aur Minus mana hai: `user name` ya `user-name` galat hai. Underscore use karo: `user_name`.",
          "3. Special characters forbidden: `@`, `#`, `$`, `%` variable ke naam me nahi lag sakte.",
          "4. Case Sensitive Niyam: `age`, `Age` aur `AGE` teeno alag-alag dabbe hain RAM me!",
          "5. Reserved Keywords se bacho: `print`, `if`, `while`, `def` ko variable ka naam nahi bana sakte."
        ],
        "analogy_en": "Think of saving a contact on your phone: 'Rahul = 9876543210'. You don't dial all 10 digits every time you call; you just tap 'Rahul'. That label 'Rahul' is the variable holding the phone number in memory!",
        "analogy_hi": "Apne phone me contact save karne jaisa hai: 'Rahul = 9876543210'. Har baar 10 digit dial nahi karte, bas 'Rahul' par click karte ho. Rahul hi variable hai jo phone number ko memory me sambhal kar rakhe hue hai!",
        "example_1": {
          "title": "Creating and Updating Variables",
          "title_hi": "Variable banana aur uski value update karna",
          "code": "wallet = 500\nprint('Initial wallet:', wallet)\nwallet = wallet - 150\nprint('After spending:', wallet)",
          "explanation_en": "• Line 1: Creates `wallet` with 500 in RAM.\n• Line 3: Reads 500, subtracts 150 (350), and stores 350 back into `wallet`.",
          "explanation_hi": "• Line 1: RAM me `wallet` naam ka dabba banta hai jisme 500 save hota hai.\n• Line 3: 500 me se 150 kharch karke 350 wapas `wallet` me save kar diya jata hai."
        },
        "example_2": {
          "title": "Real World: Instagram Follower Counter",
          "title_hi": "Real World: Follower Count Tracker",
          "code": "followers = 1200\nnew_followers = 50\ntotal = followers + new_followers\nprint('Total Followers:', total)",
          "explanation_en": "• Combines two variables to calculate an updated follower count.",
          "explanation_hi": "• Do variables ko jodkar naya follower count calculate karke print karta hai."
        },
        "challenge": {
          "prompt_en": "Create a variable named `coins = 100`. Add 50 to it. Then print: `Total coins: 150`",
          "prompt_hi": "`coins = 100` variable banao. Usme 50 add karo. Fir print karo: `Total coins: 150`",
          "starter_code": "coins = 100\n# Add 50 and print output:\n",
          "expected_output": "Total coins: 150",
          "solution_code": "coins = 100\ncoins = coins + 50\nprint(f'Total coins: {coins}')",
          "solution_explanation_hi": "`coins = coins + 50` karne se value 150 ho gayi aur print statement ne use print kar diya.",
          "ego_roast_hi": "Bhai 100 + 50 jodkar variable me save nahi kar pa rahe? `coins = coins + 50` likho!",
          "ego_cheer_hi": "Superb! 💰 Tumne computer ki RAM me variable storage master kar liya!"
        }
      },
      {
        "id": "sub_1_2_data_types",
        "title": "The 4 Core Data Types (int, float, str, bool)",
        "title_hi": "4 Main Data Types (int, float, str, bool) & type()",
        "icon": "🧩",
        "duration": "5 mins",
        "xp": 70,
        "what_is_it_en": "A Data Type tells Python what kind of value a variable is holding. Python has 4 primary data types: `int` (integers), `float` (decimals), `str` (text strings), and `bool` (boolean True/False).",
        "what_is_it_hi": "Data Type computer ko batata hai ki dabbe ke andar kis tarah ka samaan rakha hai:\n1. `int`: Poore numbers (jaise 5, 20, -10)\n2. `float`: Point / Decimal wale numbers (jaise 99.5, 3.14)\n3. `str`: Quotes ke andar ka text (jaise 'Priyanshu')\n4. `bool`: Sirf do values — `True` ya `False`.",
        "why_need_it_en": "The CPU processes numbers differently from text. You can multiply `5 * 5 = 25`, but you cannot multiply `'apple' * 'banana'`. Python enforces data types so you don't perform invalid mathematical operations on words.",
        "why_need_it_hi": "Computer numbers aur text ko alag-alag tareeke se handle karta hai. Tum `5 * 5` kar sakte ho, lekin `'seb' * 'kela'` nahi kar sakte. Data type hone se computer ko pata rehta hai ki kahan maths chalega aur kahan text.",
        "how_to_use_en": "Simply assign values; Python automatically detects the type dynamically. Use `type(variable)` to check.",
        "how_to_use_hi": "Python me type declare karne ki zarurat nahi hoti (Dynamic Typing). Bas value assign karo, aur `type(var)` se check kar lo.",
        "syntax": "x = 10         # int\ny = 3.14       # float\nz = \"Hello\"    # str\nis_ok = True   # bool (Capital T!)\nprint(type(x)) # <class 'int'>",
        "rules_en": [
          "Boolean Capitalization Rule: Must be `True` or `False` with capital T and F! Writing `true` or `false` throws `NameError`.",
          "String Quotes Rule: Text must be enclosed in `'...'` or `\"...\"`. Without quotes, Python thinks it's a variable name.",
          "Float Precision: Any number with a decimal point (even `5.0`) is stored as a `float`, NOT an `int`.",
          "Dynamic Typing: A variable can change its type dynamically if you reassign it."
        ],
        "rules_hi": [
          "Boolean ka Capital Niyam: `True` aur `False` ka T aur F hamesha BADA hona chahiye. Chhota `true` likhoge to error aayega!",
          "String ke Quotes: Text ko hamesha quotes `'...'` ya `\"...\"` me band karna padega, warna Python use variable samajhkar dhoondne lagega.",
          "Point lagte hi Float: Agar number me `.0` bhi laga hai (jaise `5.0`), to Python use `float` manta hai, `int` nahi.",
          "Dynamic Typing: Python me ek hi variable pehle number aur baad me text store kar sakta hai bina kisi problem ke."
        ],
        "analogy_en": "Think of different containers: an int is a solid coin, a float is water measured in milliliters, a str is a printed label, and a bool is a light switch (ON/OFF). You can't pour a coin like water!",
        "analogy_hi": "Alag-alag dabbon jaisa hai: int ek solid sikka hai, float paani ki bottle hai, str ek likhi hui chitthi hai, aur bool light ka switch hai (ON ya OFF). Har cheez ka apna roop hai!",
        "example_1": {
          "title": "Inspecting Types with type()",
          "title_hi": "type() function se Data Type inspect karna",
          "code": "age = 21\nheight = 5.9\nname = 'Aryan'\nis_student = True\n\nprint(type(age))\nprint(type(height))\nprint(type(name))\nprint(type(is_student))",
          "explanation_en": "• `type()` returns the internal Python class: `<class 'int'>`, `<class 'float'>`, etc.",
          "explanation_hi": "• `type()` computer se poochta hai ki variable kis category ka hai."
        },
        "example_2": {
          "title": "Real World: Gaming Player Stats",
          "title_hi": "Real World: PUBG/FreeFire Player Profile",
          "code": "player_name = 'Viper'\nscore = 4500\naccuracy = 87.5\nis_alive = True\nprint(f'{player_name} -> Score: {score}, Acc: {accuracy}%, Alive: {is_alive}')",
          "explanation_en": "• Combines all four core types to represent a complete player state.",
          "explanation_hi": "• Chaaro data types ko ek gaming profile card me combine kiya gaya hai."
        },
        "challenge": {
          "prompt_en": "Create `runs = 120` and `run_rate = 8.5`. Print their types on separate lines using `print(type(...))`.",
          "prompt_hi": "`runs = 120` aur `run_rate = 8.5` banao aur dono ke types alag-alag lines par print karo.",
          "starter_code": "runs = 120\nrun_rate = 8.5\n# Print types below:\n",
          "expected_output": "<class 'int'>\n<class 'float'>",
          "solution_code": "runs = 120\nrun_rate = 8.5\nprint(type(runs))\nprint(type(run_rate))",
          "solution_explanation_hi": "`type(runs)` int deta hai aur `type(run_rate)` float deta hai.",
          "ego_roast_hi": "Data type pehchanna nahi aa raha? `print(type(runs))` likhna tha bas!",
          "ego_cheer_hi": "Level Up! 🎯 Ab tum Python ke chaaro basic building blocks samajh chuke ho!"
        }
      },
      {
        "id": "sub_1_3_input_function",
        "title": "Taking User Input with input() & The String Trap",
        "title_hi": "User se Input lena: input() function aur String Trap",
        "icon": "⌨️",
        "duration": "6 mins",
        "xp": 80,
        "what_is_it_en": "The `input()` function pauses program execution and waits for the user to type something on their keyboard and press Enter.",
        "what_is_it_hi": "`input()` function Python ka wo darwaza hai jisse computer user se baat karta hai. Ye program ko rokh kar user ke keyboard se type karne aur Enter dabane ka wait karta hai.",
        "why_need_it_en": "Static programs with hardcoded values are useless in real life. Google needs your search query, Instagram needs your username/password, and an ATM needs your PIN. `input()` makes programs interactive.",
        "why_need_it_hi": "Agar code me pehle se sab likha hoga to website ya app kisi kaam ki nahi hogi! ATM machine ko tumhara PIN poochna padta hai, Instagram ko tumhara password poochna padta hai. `input()` ke bina koi bhi real app nahi ban sakti!",
        "how_to_use_en": "Place a prompt message inside the parentheses: `variable = input('Prompt message: ')`.",
        "how_to_use_hi": "`input('User ke liye message: ')` likh kar kisi variable me assign kar lo.",
        "syntax": "user_data = input(\"Enter something: \")\n# What user types gets stored as text inside user_data",
        "rules_en": [
          "THE GOLDEN RULE OF INPUT: `input()` ALWAYS returns data as a `str` (String / Text). ALWAYS. NO EXCEPTIONS!",
          "The '5050' Math Trap: If user types `50` and you write `num + 50`, Python crashes with `TypeError` because you cannot add int to str.",
          "Concatenation Trap: If `a = input()` gives `'5'` and `b = input()` gives `'5'`, `a + b` results in `'55'`, NOT `10`!",
          "Prompt String: Always provide a clear prompt inside quotes so the user knows what to type."
        ],
        "rules_hi": [
          "INPUT KA SABSE BADA SUNEHRA NIYAM: `input()` hamesha aur hamesha STRING (Text) return karta hai! Chahe user 100 type kare ya 500, Python use text hi manega!",
          "'5050' Math Trap: Agar user ne `50` type kiya aur tumne `num + 50` kiya, to Python error de dega (`TypeError`), kyunki text me number nahi judta.",
          "Chipakne ka Trap (Concatenation): Agar user pehle 5 type kare aur fir 5 type kare, to bina conversion ke `5 + 5 = 55` ho jayega, 10 nahi!",
          "Clear Prompt Niyam: `input('Enter your name: ')` ke andar hamesha saaf message likho taaki user ko pata chale kya type karna hai."
        ],
        "analogy_en": "Imagine a passport scanner at the airport. It doesn't care if your name is letters or numbers; it takes an image of everything as text. `input()` is that scanner — it sees everything typed as raw text!",
        "analogy_hi": "Photocopy machine jaisa hai! Photocopy machine ko farq nahi padta ki kagaz par maths ka formula likha hai ya shayari — wo sabko ek tasveer (photo/text) ki tarah scan karti hai. `input()` wahi scanner hai jo har cheez ko text bana deta hai!",
        "example_1": {
          "title": "Interactive Greeting Script",
          "title_hi": "User se naam poochkar greet karna",
          "code": "# In interactive shell: user types Priyanshu\nname = 'Priyanshu' # simulated input\nprint('Welcome to Elysia Code, ' + name + '!')",
          "explanation_en": "• Takes user input and attaches it into a personalized greeting.",
          "explanation_hi": "• User ka input le kar use personalized welcome message me jod deta hai."
        },
        "example_2": {
          "title": "Demonstrating the String Addition Trap",
          "title_hi": "Kyun 10 + 20 = 1020 ban jata hai bina conversion ke",
          "code": "a = '10' # raw input string\nb = '20' # raw input string\nresult = a + b\nprint('Raw string addition gives:', result)\n# Notice output is 1020, NOT 30!",
          "explanation_en": "• Strings are joined (concatenated) end-to-end like glue: '10' + '20' = '1020'.",
          "explanation_hi": "• Text ko jodte waqt Python Fevicol ki tarah chipka deta hai: '10' + '20' = '1020'."
        },
        "challenge": {
          "prompt_en": "Given `first_name = 'Alex'` and `city = 'Delhi'`, print: `Alex lives in Delhi` using string concatenation.",
          "prompt_hi": "`first_name = 'Alex'` aur `city = 'Delhi'` ko jodkar print karo: `Alex lives in Delhi`",
          "starter_code": "first_name = 'Alex'\ncity = 'Delhi'\n# Print the message:\n",
          "expected_output": "Alex lives in Delhi",
          "solution_code": "first_name = 'Alex'\ncity = 'Delhi'\nprint(first_name + ' lives in ' + city)",
          "solution_explanation_hi": "Strings ko `+` operator se jodkar sentence banaya.",
          "ego_roast_hi": "String jodne me space bhool gaye kya? `' lives in '` me aage peeche space dena padta hai!",
          "ego_cheer_hi": "Zabardast! 🎯 Ab tum Samajh gaye ki input() hamesha text deta hai!"
        }
      },
      {
        "id": "sub_1_4_int_input_typecasting",
        "title": "Integer & Float Input with Type Casting (int(input()))",
        "title_hi": "Integer & Float Input: int(input()) aur Type Casting ke Niyam",
        "icon": "🔢",
        "duration": "6 mins",
        "xp": 90,
        "what_is_it_en": "Type Casting is the process of converting a value from one data type to another. Wrapping `int()` around `input()` converts the incoming string into a real mathematical number.",
        "what_is_it_hi": "Type Casting ka matlab hai kisi data ka roop badalna (shapeshifting). Jab hum `input()` ke bahar `int()` pehna dete hain — `int(input())` — to aane wala text pighal kar asli mathematical number ban jata hai jisse hum maths kar sakte hain!",
        "why_need_it_en": "Because `input()` gives a string, you CANNOT do math with it. To build a calculator, calculate age, or deduct wallet balance, you MUST cast user input into an `int` or `float`.",
        "why_need_it_hi": "Kyunki `input()` sirf text deta hai, tum uspar maths nahi kar sakte! Agar calculator banana hai, Swiggy ka bill jodna hai, ya umar nikaalni hai, to tumhe input ko `int()` ya `float()` me convert karna hi padega!",
        "how_to_use_en": "For whole numbers use `int(input())`. For decimals use `float(input())`.",
        "how_to_use_hi": "Poore number ke liye `int(input('Enter number: '))` likho. Decimal/point wale number ke liye `float(input('Enter price: '))` likho.",
        "syntax": "# 1. Whole Number Input:\nage = int(input(\"Enter your age: \"))\n\n# 2. Decimal / Price Input:\nprice = float(input(\"Enter price: \"))\n\n# 3. Number to String Conversion:\ntext_score = str(100)",
        "rules_en": [
          "The ValueError Crash: If user types non-digits (e.g. 'twenty' or 'abc') into `int()`, Python crashes with `ValueError: invalid literal for int()`.",
          "Float Truncation Rule: `int(7.99)` drops the decimal and returns `7`. It does NOT round to 8!",
          "Two-Step Execution: Python first runs the inner `input()`, gets the text, and then runs the outer `int()` to convert it.",
          "Decimal String Trap: `int('45.5')` fails! You must do `float('45.5')` first, or Python crashes."
        ],
        "rules_hi": [
          "ValueError ka Khatra: Agar user ne number ki jagah 'dus' ya 'twenty' likh diya, to `int()` crash ho jayega (`ValueError`).",
          "Pura Number Chop Rule: `int(7.99)` decimal ke baad sab hata deta hai aur sirf `7` deta hai (round up nahi karta).",
          "Pehle Andar, Fir Bahar: Python pehle andar wala `input()` chalata hai text lene ke liye, fir bahar wala `int()` chalata hai number banane ke liye.",
          "Decimal String Trap: `int('45.5')` direct crash ho jata hai! Agar point wala text hai to pehle `float()` lagana padega."
        ],
        "analogy_en": "Think of unrefined gold ore. You cannot wear it as jewelry directly. You must melt it in a furnace (`int()`) to turn it into pure gold. `int(input())` is the furnace that melts raw text into pure numbers!",
        "analogy_hi": "Kachhi mitti aur banni hui eent jaisa hai! Kachhi mitti (`input()`) se direct deewar nahi bana sakte, use pehle bhatti (`int()`) me pakana padta hai. `int(input())` wahi bhatti hai jo kachhe text ko pakka number bana deti hai!",
        "example_1": {
          "title": "Taking Two Numbers and Adding Them",
          "title_hi": "Do numbers ka input lekar unhe jodna",
          "code": "num1 = int('25') # simulated int(input())\nnum2 = int('75') # simulated int(input())\ntotal = num1 + num2\nprint('Correct Sum:', total)",
          "explanation_en": "• Both string values are converted to integers, allowing mathematical addition `25 + 75 = 100`.",
          "explanation_hi": "• Dono text values ko int me badla gaya jisse 25 + 75 = 100 sahi jod nikal kar aaya."
        },
        "example_2": {
          "title": "Real World: Automatic Age Calculator in 2026",
          "title_hi": "Real World: 2026 Age Calculator",
          "code": "birth_year = int('2005') # simulated int(input())\ncurrent_year = 2026\nage = current_year - birth_year\nprint('Calculated Age in 2026:', age)",
          "explanation_en": "• Subtracts birth year integer from current year integer.",
          "explanation_hi": "• Current year me se birth year minus karke exact age nikaalta hai."
        },
        "challenge": {
          "prompt_en": "You have `subtotal_str = '450'` and `tax_str = '50'`. Cast both into `int`, calculate total, and print: `Total: 500`",
          "prompt_hi": "`subtotal_str = '450'` aur `tax_str = '50'` ko `int` me convert karke total calculate karo aur print karo: `Total: 500`",
          "starter_code": "subtotal_str = '450'\ntax_str = '50'\n# Typecast to int and print:\n",
          "expected_output": "Total: 500",
          "solution_code": "subtotal_str = '450'\ntax_str = '50'\ntotal = int(subtotal_str) + int(tax_str)\nprint(f'Total: {total}')",
          "solution_explanation_hi": "`int(subtotal_str) + int(tax_str)` se 450 + 50 = 500 calculate ho gaya.",
          "ego_roast_hi": "Bhai text aur number me farq nahi pata kya? `int()` lagao bina aalsi bane!",
          "ego_cheer_hi": "BULLSEYE! 🎯 Ab tum user se mathematical input lene ke badshah ban chuke ho!"
        }
      },
      {
        "id": "sub_1_5_fstrings",
        "title": "Modern String Formatting with f-Strings",
        "title_hi": "Modern String Formatting (f-Strings ka Magic)",
        "icon": "⚡",
        "duration": "5 mins",
        "xp": 75,
        "what_is_it_en": "f-strings (Formatted String Literals, introduced in Python 3.6) let you embed variables and Python expressions directly inside a string using `{variable_name}` without manual type conversion.",
        "what_is_it_hi": "f-string Python ka sabse powerful aur modern tareeka hai text aur variables ko ek sath print karne ka. Bas string se pehle `f` lagao aur curly brackets `{variable}` ke andar koi bhi variable likh do — Python automatically use text me convert kar dega!",
        "why_need_it_en": "The old way was painful: `print('Hello ' + str(name) + ' your score is ' + str(score))`. If you forgot one `str()`, it crashed with `TypeError`. f-strings make this 10x cleaner: `print(f'Hello {name}, your score is {score}')`.",
        "why_need_it_hi": "Puraana tareeka bahut ghatiya tha: har variable ke sath `+ str(...)` jodte raho, aur ek bhi chhoota to code crash! f-string me bas `f'Hello {name}'` likho aur chill karo.",
        "how_to_use_en": "Prefix the string with letter `f` or `F`, and put variables or math inside `{}` curly braces.",
        "how_to_use_hi": "Quotes se theek pehle `f` likho, aur quotes ke andar jahan bhi variable chahiye wahan `{variable}` likho.",
        "syntax": "name = \"Aryan\"\nage = 20\nprint(f\"Hey {name}, you are {age} years old!\")\n# Inside {}: can also do math: {age + 5}",
        "rules_en": [
          "Prefix Rule: The letter `f` or `F` MUST be placed immediately before the opening quote without spaces: `f\"...\"`.",
          "Expressions Allowed: You can do math inside `{}` like `{price * 1.18}` or call functions like `{name.upper()}`.",
          "Quote Nesting: If your f-string uses double quotes `\"...\"`, use single quotes inside `{user['name']}` to avoid closing the string early."
        ],
        "rules_hi": [
          "f Prefix ka Niyam: `f` hamesha quotes ke theek pehle chipak kar aayega: `f\"...\"`. Space mat dena.",
          "Maths Allowed: Brackets ke andar direct calculation bhi kar sakte ho, jaise `{price * 1.18}`.",
          "Quotes ka Dhyan: Agar bahar double quote `\"` hai to andar single quote `'` use karo taaki string beech me hi close na ho jaye."
        ],
        "analogy_en": "Think of a fill-in-the-blank exam sheet: 'My name is ____ and I scored ____ marks.' f-strings are those blanks `{}` that Python automatically fills with live data!",
        "analogy_hi": "Fill-in-the-blanks wale sawal jaisa hai: 'Mera naam ____ hai aur mere ____ marks aaye.' f-strings ke curly braces `{}` wahi khaali jagah hain jo Python live data se bhar deta hai!",
        "example_1": {
          "title": "Clean Variable Injection",
          "title_hi": "Clean tareeke se variables inject karna",
          "code": "product = 'MacBook M3'\nprice = 120000\nprint(f'Item: {product} | Price: Rs {price}')",
          "explanation_en": "• Replaces `{product}` and `{price}` with their values seamlessly without `str()` casting.",
          "explanation_hi": "• `{product}` aur `{price}` bina kisi `str()` lagaye direct text me convert ho kar print hote hain."
        },
        "example_2": {
          "title": "Real World: Shopping Cart Bill Receipt",
          "title_hi": "Real World: E-Commerce Bill Receipt",
          "code": "item = 'Wireless Headphones'\nqty = 2\nprice = 1500\nprint(f'{qty}x {item} = Rs {qty * price}')",
          "explanation_en": "• Evaluates math `{qty * price}` directly inside the string template.",
          "explanation_hi": "• `{qty * price}` ka maths direct string ke andar calculate karke print karta hai."
        },
        "challenge": {
          "prompt_en": "You have `user = 'Karan'` and `level = 10`. Use an f-string to print: `Player Karan is at Level 10`",
          "prompt_hi": "`user = 'Karan'` aur `level = 10` hain. f-string use karke print karo: `Player Karan is at Level 10`",
          "starter_code": "user = 'Karan'\nlevel = 10\n# Print using f-string:\n",
          "expected_output": "Player Karan is at Level 10",
          "solution_code": "user = 'Karan'\nlevel = 10\nprint(f'Player {user} is at Level {level}')",
          "solution_explanation_hi": "f-string template `f'Player {user} is at Level {level}'` use kiya.",
          "ego_roast_hi": "f lagana bhool gaye kya? Agar quotes ke pehle f nahi lagaya to curly brackets `{}` as it is print ho jayenge!",
          "ego_cheer_hi": "Clean and Modern! 🏆 Ab tum professional Python developers ki tarah formatting karte ho!"
        }
      }
    ]
  },

  # =========================================================================
  # CHAPTER 2: DECISIONS & LOGIC (CONDITIONALS)
  # =========================================================================
  {
    "id": "ch_2_conditionals",
    "title": "Chapter 2: Decisions & Logic (Conditionals)",
    "subtitle_en": "if, else, elif ladders, and Boolean logic",
    "subtitle_hi": "if, else, elif ladder aur Boolean Comparisons",
    "icon": "🚦",
    "subtopics": [
      {
        "id": "sub_2_1_if_else",
        "title": "The Fork in the Road: if and else (The Colon & Indentation Rules)",
        "title_hi": "Raaste ka Mod: if aur else (Colon aur Indentation ke Niyam)",
        "icon": "👮",
        "duration": "5 mins",
        "xp": 80,
        "what_is_it_en": "`if` and `else` statements allow your program to make decisions. If a condition evaluates to `True`, one block of code runs; if it evaluates to `False`, the `else` block runs.",
        "what_is_it_hi": "`if` aur `else` computer ke dimaag me faisla lene ki taaqat dete hain. Agar shart (condition) `True` hai to `if` wala code chalega, aur agar galat (`False`) hai to `else` wala chalega.",
        "why_need_it_en": "Without conditionals, code would just run blindly in a straight line. An app could never check if a password is correct, if a bank account has sufficient funds, or if a user is an adult.",
        "why_need_it_hi": "Agar `if-else` na ho to computer andha ho jayega! Na wo password check kar payega, na ATM me balance check kar payega, aur na hi kisi game me Game Over kar payega.",
        "how_to_use_en": "Write `if condition:` followed by an indented block (4 spaces), then `else:` followed by another indented block.",
        "how_to_use_hi": "Pehle `if condition:` likho, fir agli line me 4 space chhod kar code likho jo shart sahi hone par chalega.",
        "syntax": "if age >= 18:\n    print(\"Eligible to vote\")\nelse:\n    print(\"Too young to vote\")",
        "rules_en": [
          "THE MANDATORY COLON RULE: Every `if` and `else` line MUST end with a colon `:`! Missing it causes instant `SyntaxError`.",
          "THE INDENTATION RULE: Python does NOT use `{}` braces. The code inside an `if` block MUST be indented by 4 spaces. Missing indentation causes `IndentationError`.",
          "Assignment `=` vs Comparison `==`: `=` stores a value. `==` checks equality! Writing `if score = 100:` will crash your code with a SyntaxError.",
          "Comparison Operators: `>` (greater), `<` (less), `>=` (greater or equal), `<=` (less or equal), `==` (equal), `!=` (not equal)."
        ],
        "rules_hi": [
          "COLON LAGANA MANDATORY HAI: Har `if` aur `else` ke aakhir me colon `:` lagana zaroori hai! Bhool gaye to seedha `SyntaxError` aayega.",
          "INDENTATION KA KANOON: Python me curly brackets `{}` nahi hote. `if` ke andar ka code 4 space aage khiska kar likhna padta hai (`Tab` dabao).",
          "`=` aur `==` ka Fasaad: Ek barabar `=` value save karta hai. Do barabar `==` check karta hai ki barabar hai ya nahi! `if x = 10` likhoge to error aayega.",
          "Comparison Signs: `>` (bada), `<` (chhota), `>=` (bada ya barabar), `<=` (chhota ya barabar), `==` (barabar), `!=` (barabar nahi)."
        ],
        "analogy_en": "Think of a security guard at a club gate. If you have a VIP pass, he opens the VIP gate. Otherwise (else), he sends you to the regular line. `if-else` is that security guard!",
        "analogy_hi": "Cinema hall ke guard jaisa hai! Agar ticket hai (`if`), to andar entry milti hai. Warna (`else`), bahar bhej diya jata hai. `if-else` wahi guard hai!",
        "example_1": {
          "title": "Voting Eligibility Checker",
          "title_hi": "Vote dene ki eligibility check karna",
          "code": "age = 20\nif age >= 18:\n    print('Eligible to vote!')\nelse:\n    print('Not eligible to vote.')",
          "explanation_en": "• `20 >= 18` evaluates to `True`, so the first block executes.",
          "explanation_hi": "• 20 >= 18 True hai, isliye pehla block chala."
        },
        "example_2": {
          "title": "Real World: ATM Insufficient Funds Guard",
          "title_hi": "Real World: ATM Cash Withdrawal Security",
          "code": "balance = 5000\nwithdrawal = 2000\nif withdrawal <= balance:\n    balance = balance - withdrawal\n    print(f'Dispensing cash. New balance: Rs {balance}')\nelse:\n    print('Error: Insufficient funds!')",
          "explanation_en": "• Guards against negative bank balances before dispensing cash.",
          "explanation_hi": "• Cash nikaalne se pehle check karta hai ki account me utne paise hain ya nahi."
        },
        "challenge": {
          "prompt_en": "Given `marks = 75`. If `marks >= 40`, print `Status: Passed`, else print `Status: Failed`.",
          "prompt_hi": "`marks = 75` hai. Agar marks 40 ya usse zyada hain to print karo: `Status: Passed`, warna print karo `Status: Failed`.",
          "starter_code": "marks = 75\n# Write your if-else logic below:\n",
          "expected_output": "Status: Passed",
          "solution_code": "marks = 75\nif marks >= 40:\n    print('Status: Passed')\nelse:\n    print('Status: Failed')",
          "solution_explanation_hi": "75 >= 40 True hai, isliye 'Status: Passed' print hota hai.",
          "ego_roast_hi": "Colon `:` bhool gaye kya? Ya indentation gap nahi diya? Check karo!",
          "ego_cheer_hi": "Flawless! 🚦 Tumne computer ko faisla lena sikha diya!"
        }
      },
      {
        "id": "sub_2_2_elif_ladder",
        "title": "Multiple Choices: The elif Ladder",
        "title_hi": "Multiple Choices: elif Ladder (Top-to-Bottom Execution)",
        "icon": "🪜",
        "duration": "5 mins",
        "xp": 85,
        "what_is_it_en": "`elif` (short for 'else if') lets you evaluate multiple mutually exclusive conditions one after another in a clean ladder structure.",
        "what_is_it_hi": "`elif` ka matlab hai 'else if'. Jab 2 se zyada raaste ho (jaise Grade A, B, C, D ya Traffic light Red, Yellow, Green), tab hum `elif` ki seedhi (ladder) banate hain.",
        "why_need_it_en": "With only `if` and `else`, you can only handle 2 options (Yes or No). If you have 5 different discount tiers, nesting multiple `if` inside `else` becomes unreadable spaghetti code. `elif` solves this cleanly.",
        "why_need_it_hi": "Sirf `if-else` se 2 hi raaste ho sakte hain. Agar college me Grade A, B, C, F check karna ho, to `if` ke andar `if` daalne se code khichdi ban jayega. `elif` se code ekdum seedha aur saaf rehta hai.",
        "how_to_use_en": "Chain `elif` statements between the initial `if` and final optional `else`.",
        "how_to_use_hi": "Shuru me `if` likho, beech me jitni chahe `elif` shartein lagao, aur aakhir me default fallback ke liye `else` likho.",
        "syntax": "if score >= 90:\n    grade = \"A\"\nelif score >= 75:\n    grade = \"B\"\nelif score >= 50:\n    grade = \"C\"\nelse:\n    grade = \"F\"",
        "rules_en": [
          "Top-to-Bottom Evaluation Rule: Python tests conditions from top to bottom. The VERY FIRST condition that is `True` executes its block, and Python IMMEDIATELY SKIPS the rest of the ladder!",
          "Order Matters Critically: Always put more specific/higher conditions at the top, otherwise lower conditions will swallow them.",
          "Optional else: The final `else` is optional, but it's best practice to keep it as a catch-all safety net."
        ],
        "rules_hi": [
          "Pehla Sahi Hote hi Bahar: Python upar se neeche shartein check karta hai. JAISE HI pehli shart `True` hoti hai, uska code chalta hai aur Python baaki saari elif ko bina dekhe chhod kar aage badh jata hai!",
          "Order ka Niyam: Hamesha sabse badi/specific condition sabse upar rakho, warna neeche wali condition pehle hi sabko capture kar legi.",
          "Default else: Aakhri `else` lagana acchi aadat hai taaki agar koi bhi shart match na ho to wo chale."
        ],
        "analogy_en": "Think of a hospital triage desk: 1. If critical heart emergency -> ICU. 2. Else if broken bone -> X-Ray. 3. Else if mild fever -> General clinic. As soon as you match one department, you go there!",
        "analogy_hi": "Hospital ke emergency ward jaisa hai: 1. Agar critical hai to seedha ICU. 2. Agar haddi tooti hai to X-ray. 3. Warna general OPD. Jahan match hua wahan bhej diya jata hai, baaki doctors ke paas nahi bhejte!",
        "example_1": {
          "title": "College Grading System",
          "title_hi": "Marks ke hisab se Grade dena",
          "code": "score = 82\nif score >= 90:\n    print('Grade: A')\nelif score >= 75:\n    print('Grade: B')\nelif score >= 50:\n    print('Grade: C')\nelse:\n    print('Grade: F')",
          "explanation_en": "• `score >= 90` is False. Next `score >= 75` is True! It prints 'Grade: B' and exits the ladder.",
          "explanation_hi": "• Pehli shart fail hui, doosri shart (>= 75) pass ho gayi. 'Grade: B' print hua aur aage ki cheezein skip ho gayi."
        },
        "example_2": {
          "title": "Real World: Traffic Signal Decision",
          "title_hi": "Real World: Traffic Light Automation",
          "code": "light = 'YELLOW'\nif light == 'RED':\n    print('Action: STOP')\nelif light == 'YELLOW':\n    print('Action: SLOW DOWN')\nelif light == 'GREEN':\n    print('Action: GO')\nelse:\n    print('Action: CAUTION - Signal broken')",
          "explanation_en": "• Handles multiple states of a physical traffic light safely.",
          "explanation_hi": "• Traffic light ke alag-alag rangon par sahi action decide karta hai."
        },
        "challenge": {
          "prompt_en": "Given `hour = 14` (2 PM in 24-hr format). If `hour < 12` print `Good morning`. Else if `hour < 18` print `Good afternoon`. Else print `Good evening`.",
          "prompt_hi": "`hour = 14` hai. Agar 12 se kam ho to `Good morning`, agar 18 se kam ho to `Good afternoon`, warna `Good evening` print karo.",
          "starter_code": "hour = 14\n# Write elif ladder:\n",
          "expected_output": "Good afternoon",
          "solution_code": "hour = 14\nif hour < 12:\n    print('Good morning')\nelif hour < 18:\n    print('Good afternoon')\nelse:\n    print('Good evening')",
          "solution_explanation_hi": "14 < 18 True hai, isliye 'Good afternoon' print hota hai.",
          "ego_roast_hi": "Condition ka order ulta mat kar dena! `hour < 12` pehle aayega, fir `hour < 18`!",
          "ego_cheer_hi": "Masterclass! 🪜 Multiple conditions handle karne me ab tum pro ban chuke ho!"
        }
      },
      {
        "id": "sub_2_3_logical_operators",
        "title": "Logical Operators: and, or, not",
        "title_hi": "Logical Operators: and, or, not (Compound Conditions)",
        "icon": "⚡",
        "duration": "5 mins",
        "xp": 85,
        "what_is_it_en": "Logical operators let you combine multiple conditions together into one decision rule. Python uses English words: `and`, `or`, and `not`.",
        "what_is_it_hi": "Logical operators se hum do ya teen sharton ko ek sath jodte hain: `and` (dono shart sach honi chahiye), `or` (koi ek shart sach ho to chalega), aur `not` (sach ko jhooth, jhooth ko sach bana deta hai).",
        "why_need_it_en": "Real decisions depend on multiple factors. For an online loan: you must have `salary > 30000` AND `credit_score > 700`. You cannot test these in isolation.",
        "why_need_it_hi": "Asli zindagi me faisle kisi ek cheez par nahi hote. Loan lene ke liye: salary bhi acchi honi chahiye AND credit score bhi accha hona chahiye. Dono check karne ke liye logical operators chahiye hote hain.",
        "how_to_use_en": "Place `and` or `or` between two boolean expressions.",
        "how_to_use_hi": "Do sharton ke beech me `and` ya `or` likho.",
        "syntax": "if age >= 18 and has_license == True:\n    print(\"Can drive\")\n\nif is_weekend or is_holiday:\n    print(\"Sleeping late\")",
        "rules_en": [
          "The 'and' Rule: Evaluates to `True` ONLY if ALL conditions are `True`. If even ONE is `False`, the whole thing is `False`.",
          "The 'or' Rule: Evaluates to `True` if AT LEAST ONE condition is `True`.",
          "The 'not' Rule: Inverts boolean: `not True` becomes `False`. `not False` becomes `True`.",
          "Short-Circuit Evaluation: If the first condition in an `and` is `False`, Python doesn't even bother checking the second condition (saves CPU time)."
        ],
        "rules_hi": [
          "`and` ka Niyam: `and` tabhi `True` deta hai jab DONO shartein 100% sahi ho. Ek bhi galat hui to sab cancel!",
          "`or` ka Niyam: `or` tab `True` de deta hai agar koi BHI EK shart sahi nikal aaye.",
          "`not` ka Niyam: `not` ulta kar deta hai — `True` ko `False`, aur `False` ko `True`.",
          "Short-Circuit ka Niyam: Agar `and` me pehli hi shart galat ho gayi, to computer doosri shart ko check hi nahi karta (time bachata hai)."
        ],
        "analogy_en": "Think of a flight boarding gate: to board, you need your Ticket AND your Passport. If you have a ticket but no passport, you cannot board! But for payments: you can pay via UPI OR Cash.",
        "analogy_hi": "Aeroplane me baithne jaisa: Boarding pass AND Passport dono chahiye! Ek bhi nahi hua to flight miss. Lekin dukaan par payment karte waqt: Cash OR UPI me se koi ek chalega!",
        "example_1": {
          "title": "Job Interview Eligibility",
          "title_hi": "Job ke liye eligible candidate check karna",
          "code": "degree = True\nexperience_years = 3\nif degree and experience_years >= 2:\n    print('Shortlisted for technical interview!')\nelse:\n    print('Criteria not met.')",
          "explanation_en": "• Both conditions are True, so the candidate is shortlisted.",
          "explanation_hi": "• Dono shartein poori hain isliye candidate shortlist hua."
        },
        "example_2": {
          "title": "Real World: Free Delivery Qualifier",
          "title_hi": "Real World: Amazon/Swiggy Free Delivery",
          "code": "order_amount = 350\nis_vip_member = True\nif order_amount >= 500 or is_vip_member:\n    print('Eligible for FREE Express Delivery!')\nelse:\n    print('Delivery Fee: Rs 40')",
          "explanation_en": "• Order amount is only 350, but `is_vip_member` is True, so free delivery is granted via `or`.",
          "explanation_hi": "• Order 500 se kam tha, lekin VIP member hone ki wajah se `or` condition pass ho gayi aur delivery free mili!"
        },
        "challenge": {
          "prompt_en": "Given `has_id = True` and `has_wristband = False`. If `has_id or has_wristband`, print `Access: Granted`, else print `Access: Denied`.",
          "prompt_hi": "`has_id = True` aur `has_wristband = False` hain. Agar `has_id or has_wristband` ho to print karo `Access: Granted`, warna `Access: Denied`.",
          "starter_code": "has_id = True\nhas_wristband = False\n# Write logic below:\n",
          "expected_output": "Access: Granted",
          "solution_code": "has_id = True\nhas_wristband = False\nif has_id or has_wristband:\n    print('Access: Granted')\nelse:\n    print('Access: Denied')",
          "solution_explanation_hi": "Kyunki `has_id` True hai, `or` condition pass ho gayi aur 'Access: Granted' print hua.",
          "ego_roast_hi": "and aur or me confuse mat hona! Yahan 'or' likha hai matlab koi ek bhi chalega!",
          "ego_cheer_hi": "BRILLIANT! ⚡ Logic gates aur conditional branches ab tumhare control me hain!"
        }
      }
    ]
  },

  # =========================================================================
  # CHAPTER 3: LOOPS & AUTOMATION
  # =========================================================================
  {
    "id": "ch_3_loops",
    "title": "Chapter 3: Loops & Automation",
    "subtitle_en": "for loops, range(), while loops, and loop control",
    "subtitle_hi": "for Loops, range(), while Loops aur Automation",
    "icon": "🔁",
    "subtopics": [
      {
        "id": "sub_3_1_for_range",
        "title": "The for Loop & range(start, stop, step)",
        "title_hi": "for Loop aur range() ka Stop-Exclusive Niyam",
        "icon": "🏃",
        "duration": "6 mins",
        "xp": 90,
        "what_is_it_en": "A `for` loop repeats a block of code a specific number of times, or iterates across items in a sequence. The built-in `range()` function generates an arithmetic progression of numbers.",
        "what_is_it_hi": "`for` loop kisi code ko baar-baar repeat (dohraane) ke liye use hota hai. `range()` function computer ke liye numbers ki ginti (counting) generate karta hai.",
        "why_need_it_en": "If you need to send 1,000 WhatsApp emails or calculate salaries for 500 employees, typing 500 lines manually is impossible. A `for` loop executes 1,000 times in 2 milliseconds.",
        "why_need_it_hi": "Agar tumhe 1,000 logo ko email bhejna ho ya 500 employees ki salary calculate karni ho, to kya 1,000 baar code type karoge? `for` loop wahi kaam 2 millisecond me 1000 baar automatic chala deta hai!",
        "how_to_use_en": "Use `for item in range(start, stop, step):` followed by an indented body.",
        "how_to_use_hi": "`for i in range(shuru, khatam, jump):` likho aur 4 space dekar loop ke andar ka code likho.",
        "syntax": "# 1. range(N): 0 to N-1\nfor i in range(5):\n    print(i) # 0, 1, 2, 3, 4\n\n# 2. range(start, stop, step):\nfor i in range(2, 10, 2):\n    print(i) # 2, 4, 6, 8",
        "rules_en": [
          "THE CRITICAL 'STOP-EXCLUSIVE' RULE: `range(1, 5)` stops BEFORE 5! It produces `1, 2, 3, 4`. It NEVER touches the stop number!",
          "Default Start is 0: If you write `range(5)`, Python starts at `0` and stops at `4` (total 5 numbers).",
          "Step Parameter: The third argument `step` specifies the interval. `range(0, 10, 2)` gives even numbers `0, 2, 4, 6, 8`.",
          "Negative Step: To count backwards, supply a negative step: `range(5, 0, -1)` counts `5, 4, 3, 2, 1`."
        ],
        "rules_hi": [
          "SABSE BADA NIYAM (STOP IS EXCLUSIVE): `range(1, 5)` 5 par nahi jaata! Ye sirf `1, 2, 3, 4` tak chalta hai. Aakhri number ko Python touch nahi karta!",
          "Default Shuruaat 0 se: Agar sirf `range(5)` likha hai, to ginti 0 se shuru hoke 4 par khatam hogi (total 5 baar).",
          "Step ka Niyam: Teesri value jump hoti hai. `range(1, 10, 2)` do-do ki chhalang lagayega: `1, 3, 5, 7, 9`.",
          "Ultee Ginti: Piche aane ke liye negative step chahiye: `range(5, 0, -1)` se `5, 4, 3, 2, 1` aayega."
        ],
        "analogy_en": "Think of doing 10 pushups. Your trainer counts: 1, 2, 3... until 10. `range(1, 11)` is that automatic trainer counting reps for you!",
        "analogy_hi": "Gym me 10 pushups lagane jaisa hai: Coach ginta hai '1, 2, 3... 10'. `range(1, 11)` wahi automatic coach hai jo har repetition ko track karta hai!",
        "example_1": {
          "title": "Printing Numbers 1 to 5",
          "title_hi": "1 se 5 tak numbers print karna",
          "code": "for i in range(1, 6):\n    print('Count:', i)",
          "explanation_en": "• Notice `range(1, 6)` is used because 6 is excluded, so it prints 1 to 5.",
          "explanation_hi": "• Dhyan do `range(1, 6)` likha hai kyunki 6 include nahi hota, isliye 1 se 5 print hua."
        },
        "example_2": {
          "title": "Real World: Multiplication Table of 7",
          "title_hi": "Real World: 7 ka Pahada (Multiplication Table)",
          "code": "n = 7\nfor i in range(1, 6):\n    print(f'{n} x {i} = {n * i}')",
          "explanation_en": "• Generates the first 5 multiples of 7 automatically.",
          "explanation_hi": "• Loop use karke 7 ke pehle 5 multiples automatic calculate karke print kiye."
        },
        "challenge": {
          "prompt_en": "Write a `for` loop using `range(1, 5)` that prints: `Attempt 1`, `Attempt 2`, `Attempt 3`, `Attempt 4`.",
          "prompt_hi": "`range(1, 5)` ka `for` loop likho jo print kare: `Attempt 1`, `Attempt 2`, `Attempt 3`, `Attempt 4`.",
          "starter_code": "# Write for loop below:\n",
          "expected_output": "Attempt 1\nAttempt 2\nAttempt 3\nAttempt 4",
          "solution_code": "for i in range(1, 5):\n    print(f'Attempt {i}')",
          "solution_explanation_hi": "range(1, 5) 1 se 4 tak chalta hai aur har iteration me print karta hai.",
          "ego_roast_hi": "range(1, 4) likh diya kya? Yaad rakho stop number kabhi include nahi hota!",
          "ego_cheer_hi": "Automation Unleashed! ⚡ Ab tum hazaron calculations ek pal me dohra sakte ho!"
        }
      },
      {
        "id": "sub_3_2_while_loop",
        "title": "The while Loop & Preventing Infinite Loops",
        "title_hi": "while Loop aur Infinite Loop Crash se Bachna",
        "icon": "🔄",
        "duration": "6 mins",
        "xp": 90,
        "what_is_it_en": "A `while` loop keeps running AS LONG AS a given condition remains `True`. It checks the condition before every single iteration.",
        "what_is_it_hi": "`while` loop tab tak chalta rehta hai jab tak di gayi shart `True` rehti hai. Har round se pehle computer shart check karta hai — agar abhi bhi True hai, to dobara chala deta hai.",
        "why_need_it_en": "When you don't know in advance how many times code must run. For example, an ATM asks for your PIN until you enter it correctly. You cannot use a fixed `range()` for that.",
        "why_need_it_hi": "Jab tumhe pehle se pata na ho ki loop kitni baar chalana padega! Jaise game tab tak chalta hai jab tak player mar na jaye. Ya ATM tab tak PIN maangta hai jab tak sahi na dale. Iske liye `while` loop chahiye.",
        "how_to_use_en": "Define a loop variable, check it in `while condition:`, and CRITICALLY: update the variable inside the loop body!",
        "how_to_use_hi": "Ek variable banao, `while condition:` likho, aur loop ke andar us variable ko badalte raho (update counter).",
        "syntax": "count = 1\nwhile count <= 5:\n    print(count)\n    count = count + 1 # CRUCIAL! Otherwise infinite loop!",
        "rules_en": [
          "THE INFINITE LOOP TRAP: If you forget to update the variable (e.g. `count = count + 1`), the condition remains `True` forever. The CPU hangs, RAM maxes out, and the browser crashes!",
          "Pre-Condition Check: If the condition is `False` at the very start, the while loop body will NEVER run even once.",
          "Always Ensure an Exit Strategy: Every while loop must have a guaranteed path to make the condition `False`."
        ],
        "rules_hi": [
          "INFINITE LOOP KA MAHABHAYANAK TRAP: Agar tum loop ke andar variable ko badalna bhool gaye (jaise `count = count + 1`), to condition hamesha True rahegi aur computer kabhi rukega nahi! CPU 100% ho jayega aur browser hang ho jayega!",
          "Pehle Check: Agar shuru me hi condition False hai, to while loop ek baar bhi nahi chalega.",
          "Exit Strategy zaroori hai: Hamesha aisa rasta hona chahiye jisse condition kabhi na kabhi False ho sake."
        ],
        "analogy_en": "Think of charging your phone: the charger keeps pumping electricity WHILE battery < 100%. As soon as it hits 100%, the charging circuit cuts off!",
        "analogy_hi": "Phone charging jaisa hai: Charger electricity deta rehta hai JAB TAK (while) battery 100% na ho jaye. Jaise hi 100% hoti hai, circuit band ho jata hai!",
        "example_1": {
          "title": "Rocket Launch Countdown",
          "title_hi": "Rocket Launch ka Countdown Timer",
          "code": "timer = 3\nwhile timer > 0:\n    print(f'T-minus: {timer}')\n    timer = timer - 1\nprint('Blast off! 🚀')",
          "explanation_en": "• Decrements timer by 1 each loop until timer becomes 0, then exits cleanly.",
          "explanation_hi": "• Har round me timer 1 kam hota hai. Jab 0 hota hai to loop khatam hoke Blast off print hota hai."
        },
        "example_2": {
          "title": "Real World: Battery Charging Simulation",
          "title_hi": "Real World: Battery Fast Charger",
          "code": "battery = 85\nwhile battery < 100:\n    battery = battery + 5\n    print(f'Charging... {battery}%')\nprint('Battery Fully Charged!')",
          "explanation_en": "• Increments battery in steps of 5 until fully charged.",
          "explanation_hi": "• 5-5% karke battery charge hoti hai jab tak 100% na ho jaye."
        },
        "challenge": {
          "prompt_en": "Create `n = 1`. Write a `while n <= 3:` loop that prints: `Step 1`, `Step 2`, `Step 3`.",
          "prompt_hi": "`n = 1` banao. `while n <= 3:` loop likho jo print kare: `Step 1`, `Step 2`, `Step 3`.",
          "starter_code": "n = 1\n# Write while loop with increment:\n",
          "expected_output": "Step 1\nStep 2\nStep 3",
          "solution_code": "n = 1\nwhile n <= 3:\n    print(f'Step {n}')\n    n = n + 1",
          "solution_explanation_hi": "n = n + 1 har round me n ko badhata hai, jisse loop 3 ke baad ruk jata hai.",
          "ego_roast_hi": "n = n + 1 bhool gaye to code infinite loop me chala jayega! Increment lagao jaldi!",
          "ego_cheer_hi": "Clean execution! 🔄 Tumne infinite loop trap ko smartly bypass kar liya!"
        }
      },
      {
        "id": "sub_3_3_loop_control",
        "title": "Loop Control: break, continue, and pass",
        "title_hi": "Loop Control: break, continue aur pass ka Niyam",
        "icon": "🛑",
        "duration": "5 mins",
        "xp": 80,
        "what_is_it_en": "Loop control statements let you alter the normal flow of a loop: `break` terminates the loop completely, `continue` skips to the next iteration, and `pass` acts as a placeholder.",
        "what_is_it_hi": "`break` loop ko usi waqt emergency brake laga kar khatam kar deta hai. `continue` sirf us ek round ko chhod kar agle round par jump kar deta hai. `pass` bas ek khaali placeholder hota hai taaki syntax error na aaye.",
        "why_need_it_en": "When searching for a user in a million-item list: once found, you MUST stop searching immediately using `break` to avoid wasting 10 seconds of CPU time.",
        "why_need_it_hi": "Agar tum 10 lakh logo me kisi ek ko dhoond rahe ho, to milte hi loop ko `break` karna padega! Warna wo faltu me baaki 9 lakh logo ko bhi scan karega aur computer slow ho jayega.",
        "how_to_use_en": "Place `break` or `continue` inside an `if` statement inside the loop body.",
        "how_to_use_hi": "Loop ke andar `if` condition lagao aur uske andar `break` ya `continue` likho.",
        "syntax": "for i in range(10):\n    if i == 5:\n        break # Kills loop immediately\n    if i == 2:\n        continue # Skips 2, goes to 3\n    print(i)",
        "rules_en": [
          "break Kills Everything: When `break` executes, the loop terminates immediately. No further iterations will run.",
          "continue Skips One Round: When `continue` executes, all code below it in the CURRENT iteration is skipped, and the loop starts the next iteration.",
          "pass is a No-Op: `pass` does absolutely nothing. It is used when syntax requires a statement but you have no logic to write yet."
        ],
        "rules_hi": [
          "break ka Niyam: `break` chalte hi pura loop usi millisecond me khatam ho jata hai.",
          "continue ka Niyam: `continue` ke neeche ka code us round ke liye skip ho jata hai aur loop agle number par chala jata hai.",
          "pass ka Niyam: `pass` kuch nahi karta; bas empty block me error rokne ke liye likha jata hai."
        ],
        "analogy_en": "Think of a queue at a movie counter: `break` is when the counter closes and everyone goes home. `continue` is when one customer has invalid cash, so the clerk skips them and serves the next person!",
        "analogy_hi": "Movie ticket counter jaisa: `break` ka matlab counter band ho gaya, sab ghar jao. `continue` ka matlab ek aadmi ke paas chhutta nahi tha, to use bola 'side me khade ho, agla banda aao'!",
        "example_1": {
          "title": "Using break to Stop on Target",
          "title_hi": "Target milte hi break se loop rokna",
          "code": "for n in range(1, 10):\n    if n == 4:\n        print('Found 4! Stopping loop.')\n        break\n    print('Checking:', n)",
          "explanation_en": "• Stops running as soon as `n == 4`, avoiding checking 5 through 9.",
          "explanation_hi": "• 4 aate hi break chal gaya aur 5 se 9 tak ka loop nahi chala."
        },
        "example_2": {
          "title": "Using continue to Skip Odd Numbers",
          "title_hi": "continue se sirf Even numbers print karna",
          "code": "for n in range(1, 6):\n    if n % 2 != 0:\n        continue # Skip odd numbers\n    print('Even number:', n)",
          "explanation_en": "• Skips 1, 3, 5 and prints only 2 and 4.",
          "explanation_hi": "• Odd numbers ko continue ne skip kar diya aur sirf 2 aur 4 print huye."
        },
        "challenge": {
          "prompt_en": "Write a `for i in range(1, 6):` loop. If `i == 3`, `break`. Print each number before the break condition. Expected output: `1` then `2`.",
          "prompt_hi": "`for i in range(1, 6):` loop me agar `i == 3` ho to `break` karo. Expected output: `1` aur `2`.",
          "starter_code": "for i in range(1, 6):\n    # Write break condition:\n",
          "expected_output": "1\n2",
          "solution_code": "for i in range(1, 6):\n    if i == 3:\n        break\n    print(i)",
          "solution_explanation_hi": "1 aur 2 print hote hain, aur 3 par aakar loop break ho jata hai.",
          "ego_roast_hi": "print ko if ke neeche rakhna ya upar, yahi to dhyan dena hota hai!",
          "ego_cheer_hi": "Precision Control! 🛑 Tum loop ke flow ko ungliyon par nacha sakte ho!"
        }
      }
    ]
  },

  # =========================================================================
  # CHAPTER 4: DATA COLLECTIONS (LISTS & DICTIONARIES)
  # =========================================================================
  {
    "id": "ch_4_data_structures",
    "title": "Chapter 4: Data Collections",
    "subtitle_en": "Lists, 0-Based Indexing, Dictionaries, and Key-Value pairs",
    "subtitle_hi": "Python Lists, 0-Based Indexing aur Dictionaries ka Funda",
    "icon": "🗃️",
    "subtopics": [
      {
        "id": "sub_4_1_lists",
        "title": "Python Lists & 0-Based Indexing (Negative Indexing Rules)",
        "title_hi": "Python Lists aur 0-Based Indexing ke Niyam",
        "icon": "📋",
        "duration": "6 mins",
        "xp": 95,
        "what_is_it_en": "A List is an ordered, mutable collection of items enclosed in square brackets `[...]`. Items can be accessed using their numerical position (index).",
        "what_is_it_hi": "List ek ordered collection hoti hai jisme square brackets `[...]` ke andar kai saari values comma `,` lagakar rakhi jaati hain. Har item ka ek seat number (index) hota hai.",
        "why_need_it_en": "Without lists, managing 100 students would require 100 separate variables (`student1`, `student2`...). A list holds all 100 students inside one single variable: `students = [...]`.",
        "why_need_it_hi": "Agar list na ho, to 100 students ke liye 100 alag-alag variables banane padenge! List ki madad se ek hi variable ke andar hazaron items ek sath sambhale ja sakte hain.",
        "how_to_use_en": "Create with `[item1, item2]`. Access with `list[index]`. Add with `.append(item)`. Count with `len(list)`.",
        "how_to_use_hi": "`items = ['Apple', 'Banana']` se list banti hai. `items[0]` se pehla item milta hai. `items.append('Orange')` se naya item judta hai.",
        "syntax": "fruits = [\"Apple\", \"Banana\", \"Mango\"]\nprint(fruits[0])   # Apple (0-based!)\nprint(fruits[-1])  # Mango (Last item!)\nfruits.append(\"Orange\") # Adds to end",
        "rules_en": [
          "THE 0-BASED INDEXING RULE: The first item is at index `0`, NOT `1`! The second item is at `1`.",
          "Negative Indexing Rule: `list[-1]` always accesses the VERY LAST item! `list[-2]` accesses second-to-last.",
          "IndexError Crash: Accessing an index that does not exist (e.g. `fruits[99]` on a 3-item list) crashes with `IndexError: list index out of range`.",
          "Mutability: Lists are mutable — you can modify items in place: `fruits[0] = 'Strawberry'`."
        ],
        "rules_hi": [
          "0-BASED INDEXING KA SUNEHRA NIYAM: Pehla item seat number `0` par hota hai, `1` par nahi! Doosra item `1` par hota hai.",
          "Negative Indexing ka Jaadu: `list[-1]` hamesha AAKHRI item deta hai! `list[-2]` piche se doosra item deta hai.",
          "IndexError ka Khatra: Agar list me 3 items hain aur tumne `list[10]` maang liya, to Python crash ho jayega (`IndexError`).",
          "Mutable Niyam: List ke items ko baad me badla ja sakta hai: `fruits[0] = 'Mango'`."
        ],
        "analogy_en": "Think of an egg tray with numbered slots: Slot 0, Slot 1, Slot 2... You can grab an egg from any slot or put a new egg in slot 3. That's a Python list!",
        "analogy_hi": "Train ke dibbon jaisa: Pehla dibba Engine ke theek baad Seat 0 hai, agla Seat 1 hai. Aakhri dibba guard ka dibba hai jise `-1` bolte hain!",
        "example_1": {
          "title": "Accessing and Appending to a List",
          "title_hi": "List me se item nikaalna aur naya item jodna",
          "code": "cart = ['Laptop', 'Mouse', 'Keyboard']\nprint('First item:', cart[0])\nprint('Last item:', cart[-1])\ncart.append('Monitor')\nprint('Total items:', len(cart))",
          "explanation_en": "• Demonstrates 0-based indexing, negative indexing, `.append()`, and `len()`.",
          "explanation_hi": "• Seat 0, aakhri seat -1, naya item append karna aur len() se ginti karna dikhata hai."
        },
        "example_2": {
          "title": "Real World: Looping Over Student Names",
          "title_hi": "Real World: Students ki attendance lagana",
          "code": "students = ['Aryan', 'Sneha', 'Rohan']\nfor name in students:\n    print(f'Present: {name}')",
          "explanation_en": "• A `for` loop seamlessly iterates through every item in a list one by one.",
          "explanation_hi": "• for loop list ke har item ko ek-ek karke nikaalta hai aur attendance print karta hai."
        },
        "challenge": {
          "prompt_en": "Given `languages = ['C++', 'Java', 'Python']`. Print the last item using negative indexing `[-1]`.",
          "prompt_hi": "`languages = ['C++', 'Java', 'Python']` me se negative indexing `[-1]` use karke aakhri item print karo.",
          "starter_code": "languages = ['C++', 'Java', 'Python']\n# Print last item:\n",
          "expected_output": "Python",
          "solution_code": "languages = ['C++', 'Java', 'Python']\nprint(languages[-1])",
          "solution_explanation_hi": "`languages[-1]` hamesha list ka aakhri item deta hai jo ki 'Python' hai.",
          "ego_roast_hi": "languages[3] likh kar IndexError mat le aana! Aakhri item ke liye [-1] use karo!",
          "ego_cheer_hi": "Top Tier! 📋 Lists data ko organize karne ka sabse powerful hathiyar hain!"
        }
      },
      {
        "id": "sub_4_2_dictionaries",
        "title": "Dictionaries (Key-Value Pairs & Lookup Rules)",
        "title_hi": "Dictionaries (Key-Value Pairs aur .get() ke Niyam)",
        "icon": "📖",
        "duration": "6 mins",
        "xp": 95,
        "what_is_it_en": "A Dictionary is an unordered collection of key-value pairs enclosed in curly braces `{}`. Instead of accessing items by index number, you access them by their unique key name.",
        "what_is_it_hi": "Dictionary ek aisi collection hoti hai jisme data 'Key: Value' (Naam: Data) ke jode me curly braces `{}` ke andar store hota hai. Yahan seat number se nahi, balki key ke naam se data dhoonda jata hai.",
        "why_need_it_en": "In a list `['Aryan', 21, 'Delhi']`, you don't know what `21` means (Is it age? roll number? rank?). A dictionary gives names to values: `{'name': 'Aryan', 'age': 21, 'city': 'Delhi'}`.",
        "why_need_it_hi": "Agar list me `['Aryan', 21, 'Delhi']` likh doge, to pata nahi chalega ki 21 age hai ya roll number! Dictionary har value ko ek label de deti hai: `{'name': 'Aryan', 'age': 21}`. Saara internet aur APIs isi format (JSON) par chalti hain!",
        "how_to_use_en": "Create with `{key: value}`. Access with `dict[key]` or safe lookup `dict.get(key, default)`.",
        "how_to_use_hi": "`user = {'name': 'Aryan', 'age': 21}` banao. `user['name']` se naam mil jayega.",
        "syntax": "student = {\n    \"name\": \"Priyanshu\",\n    \"course\": \"B.Tech CSE\",\n    \"gpa\": 9.2\n}\nprint(student[\"name\"]) # Priyanshu",
        "rules_en": [
          "Unique Keys Rule: Keys MUST be unique. If you define the same key twice, the second value overwrites the first!",
          "Immutable Keys: Keys must be immutable types (strings or integers). You cannot use a list as a dictionary key.",
          "KeyError Trap: Accessing a key that doesn't exist (`student['phone']`) crashes with `KeyError`. Use `.get('phone', 'Not Found')` for safe access!",
          "Adding/Updating: `dict['new_key'] = new_value` inserts if missing, or updates if already present."
        ],
        "rules_hi": [
          "Unique Key ka Niyam: Har key ka naam alag hona chahiye. Agar ek hi key do baar likhoge to doosri wali pehli ko mita degi.",
          "KeyError ka Khatra: Agar aisi key maang loge jo dictionary me nahi hai (`student['phone']`), to Python crash ho jayega (`KeyError`). Bachaav ke liye `.get('phone')` use karo.",
          "Naya data jodna: `dict['phone'] = '98765'` likhne se agar phone nahi tha to naya jud jayega, aur agar tha to update ho jayega."
        ],
        "analogy_en": "Think of an actual English dictionary: you search for the word (the Key) 'Serendipity', and right next to it is the explanation (the Value). You don't search by page number; you search by the word!",
        "analogy_hi": "Asli English dictionary jaisi hai! Tumhe kisi word ka matlab chahiye to tum us word (Key) ko dhoondte ho, aur uske aage uska meaning (Value) mil jata hai!",
        "example_1": {
          "title": "Creating and Reading a Dictionary",
          "title_hi": "Dictionary banana aur key se data nikaalna",
          "code": "car = {'brand': 'Tesla', 'model': 'Model 3', 'year': 2024}\nprint('Brand:', car['brand'])\ncar['color'] = 'Red' # add new key\nprint('Color:', car['color'])",
          "explanation_en": "• Accesses values by key name and adds a new key-value pair dynamically.",
          "explanation_hi": "• Key ke naam se data nikaalta hai aur naya key-value joda add karta hai."
        },
        "example_2": {
          "title": "Real World: Safe Lookup with .get()",
          "title_hi": "Real World: .get() se crash hone se bachna",
          "code": "user = {'username': 'coder99', 'email': 'coder@test.com'}\n# Safe lookup that won't crash if key is missing:\nphone = user.get('phone', 'No Phone Provided')\nprint('Phone status:', phone)",
          "explanation_en": "• `.get()` returns fallback default value instead of throwing a KeyError crash.",
          "explanation_hi": "• `.get()` use karne se agar key na bhi ho to code crash nahi hota, default fallback message milta hai."
        },
        "challenge": {
          "prompt_en": "Create `player = {'name': 'Virat', 'score': 183}`. Print: `Virat scored 183 runs` using the dictionary keys.",
          "prompt_hi": "`player = {'name': 'Virat', 'score': 183}` banao aur keys use karke print karo: `Virat scored 183 runs`.",
          "starter_code": "player = {'name': 'Virat', 'score': 183}\n# Print using dictionary keys:\n",
          "expected_output": "Virat scored 183 runs",
          "solution_code": "player = {'name': 'Virat', 'score': 183}\nprint(f\"{player['name']} scored {player['score']} runs\")",
          "solution_explanation_hi": "`player['name']` se 'Virat' mila aur `player['score']` se 183 mila.",
          "ego_roast_hi": "Quotes ka dhyan rakho! f\"{player['name']}\" me bahar double aur andar single quote lagao!",
          "ego_cheer_hi": "Masterclass! 🏆 Ab tum Web APIs aur JSON data format handle karne ke kaabil ban gaye!"
        }
      }
    ]
  },

  # =========================================================================
  # CHAPTER 5: REUSABLE SUPERPOWERS (FUNCTIONS)
  # =========================================================================
  {
    "id": "ch_5_functions",
    "title": "Chapter 5: Reusable Superpowers (Functions)",
    "subtitle_en": "def, parameters, return vs print, and modular code",
    "subtitle_hi": "Functions: def, return aur reusable code ka mantra",
    "icon": "⚡",
    "subtopics": [
      {
        "id": "sub_5_1_functions_intro",
        "title": "Creating Your Own Magic Spells with def & Parameters",
        "title_hi": "Apna khud ka function banana (def & Parameters)",
        "icon": "🪄",
        "duration": "5 mins",
        "xp": 100,
        "what_is_it_en": "A function is a named, reusable block of code that performs an isolated specific task. You define it once using the `def` keyword, and you can call it thousands of times from anywhere in your project.",
        "what_is_it_hi": "Function ek aisa shortcut / spell hota hai jise tum ek baar likhte ho (`def`), aur fir jab chahe hazaro baar bula (call) sakte ho bina dobara code likhe!",
        "why_need_it_en": "Without functions, if you have a 10-line tax calculation formula, and your project calculates taxes in 50 different places, you would copy-paste 500 lines. If the tax rate changes, you must edit 50 places! With a function, you write it once and edit 1 place.",
        "why_need_it_hi": "Bina function ke agar 10 line ka tax calculation formula hai aur wo website me 50 jagah chahiye, to kya 500 lines copy-paste karoge? Kal ko GST badla to 50 jagah edit karna padega! Function se bas ek jagah badlo, poori website automatic update ho jati hai.",
        "how_to_use_en": "Define using `def func_name(params):` followed by indented body. Call using `func_name(args)`.",
        "how_to_use_hi": "`def function_ka_naam(inputs):` likho aur andar logic likho. Baad me `function_ka_naam(values)` likh kar call karo.",
        "syntax": "def greet(name):\n    print(f\"Hello, {name}!\")\n\n# Call the function:\ngreet(\"Aryan\")\ngreet(\"Sneha\")",
        "rules_en": [
          "Definition vs Execution Rule: Defining a function with `def` does NOT run the code inside it! It only runs when you explicitly CALL it with parentheses `()`.",
          "Parameter vs Argument: A 'parameter' is the placeholder variable in the `def` line. An 'argument' is the actual value passed during the function call.",
          "Indentation Rule: All code belonging to the function must be indented 4 spaces.",
          "Scope Rule: Variables created inside a function are local. They vanish from memory as soon as the function finishes running!"
        ],
        "rules_hi": [
          "Define aur Call ka Niyam: `def` likhne se function chalta nahi hai! Wo tabhi chalega jab tum use call karoge `func()` likhkar.",
          "Parameter vs Argument: `def greet(name)` me `name` parameter (placeholder) hai. Jab tum `greet('Priyanshu')` bhejte ho to 'Priyanshu' argument (asli value) hai.",
          "Local Scope ka Niyam: Function ke andar banaye gaye variables function khatam hote hi RAM se gayab ho jaate hain (bahar access nahi ho sakte)."
        ],
        "analogy_en": "Think of the 'Boil Water' button on an electric kettle. The internal heating circuitry is already wired up (`def`). You just press the button with water (`call`), and it does the job!",
        "analogy_hi": "Electric kettle ke 'Boil Water' button jaisa hai: Andar ka circuit pehle se bana hai (`def`). Tum bas ek button dabate ho (`call`), aur paani ubal jata hai!",
        "example_1": {
          "title": "A Reusable Greeting Function",
          "title_hi": "Greeting function banana aur call karna",
          "code": "def send_welcome(user):\n    print(f'Welcome aboard, {user}! Ready to code?')\n\nsend_welcome('Aryan')\nsend_welcome('Sneha')",
          "explanation_en": "• The function executes twice with two different arguments.",
          "explanation_hi": "• Function do alag-alag naamo ke sath do baar execute hota hai bina code repeat kiye."
        },
        "example_2": {
          "title": "Real World: Automated 18% GST Calculator",
          "title_hi": "Real World: GST Bill Calculator",
          "code": "def show_gst(amount):\n    tax = amount * 0.18\n    print(f'Amount: Rs {amount} | GST (18%): Rs {tax}')\n\nshow_gst(1000)\nshow_gst(5000)",
          "explanation_en": "• Centralizes tax calculation logic into one reusable function.",
          "explanation_hi": "• Tax calculation logic ko ek function me pack karke bar-bar use kiya gaya."
        },
        "challenge": {
          "prompt_en": "Define a function `say_hi(name)` that prints `Hi, {name}!`. Call it with `'Rohan'`. Expected output: `Hi, Rohan!`",
          "prompt_hi": "`say_hi(name)` function banao jo `Hi, {name}!` print kare. Use `'Rohan'` ke sath call karo.",
          "starter_code": "# Define say_hi(name) and call it:\n",
          "expected_output": "Hi, Rohan!",
          "solution_code": "def say_hi(name):\n    print(f'Hi, {name}!')\n\nsay_hi('Rohan')",
          "solution_explanation_hi": "`say_hi('Rohan')` call karne par name me 'Rohan' chala gaya aur output print ho gaya.",
          "ego_roast_hi": "Function bana liya par call karna bhool gaye? `say_hi('Rohan')` likhna zaroori hai!",
          "ego_cheer_hi": "Brilliant! 🪄 Tumne modular programming ka sabse powerful hathiyar unlock kar liya!"
        }
      },
      {
        "id": "sub_5_2_return_vs_print",
        "title": "The Golden Law: return vs print (The None Trap & Scope Rules)",
        "title_hi": "Sunehra Kanoon: return vs print (None Trap aur Scope Rules)",
        "icon": "🔄",
        "duration": "5 mins",
        "xp": 110,
        "what_is_it_en": "`print()` only displays characters on the monitor for human eyes. It returns NOTHING (`None`). `return` hands the calculated data back to the calling code so it can be stored in a variable and used for further calculations.",
        "what_is_it_hi": "`print()` sirf screen par insaano ke dekhne ke liye text dikhata hai. Lekin program ko ghanta kuch nahi milta (`None`). `return` calculated answer ko variable ke andar pack karke aage doosre calculations ke liye bhejta hai.",
        "why_need_it_en": "If a function calculates tax, you cannot add the printed tax to your bill total because `print()` produces `None`. You MUST `return` the tax amount so your billing system can calculate `subtotal + tax`.",
        "why_need_it_hi": "Agar tumne tax calculate karne wale function me sirf `print()` kiya, to wo screen par to dikh jayega lekin tum use bill ke total me jod nahi paoge (TypeError: NoneType aayega). Function se answer le kar aage calculation karne ke liye `return` mandatory hai!",
        "how_to_use_en": "Write `return result` at the end of your function. Store the output in a variable: `ans = my_func()`.",
        "how_to_use_hi": "Function ke aakhir me `return value` likho, aur jahan se call kiya hai wahan variable me store kar lo: `ans = my_func()`.",
        "syntax": "def add(a, b):\n    return a + b # Gives value back\n\ntotal = add(10, 20) # total becomes 30\nprint(total * 2)    # 60",
        "rules_en": [
          "THE PRINT GIVES NONE TRAP: If a function has no `return` statement, it automatically returns `None`. If you write `x = bad_func()` and then try `x + 5`, it crashes with `TypeError: unsupported operand type for +: 'NoneType' and 'int'`.",
          "return Terminate Rule: As soon as a function hits a `return` statement, it EXITS IMMEDIATELY. Any lines of code written below `return` are DEAD code and will never run!",
          "Returning Multiple Values: Python can return multiple values separated by commas: `return x, y` (returns a tuple)."
        ],
        "rules_hi": [
          "NONE TRAP KA MAHADUKH: Agar function me `return` nahi lagaya, to Python chupke se `None` return karta hai. Fir agar tumne `x + 5` kiya to `TypeError: NoneType` aayega!",
          "return chalte hi Function Khatam: Jaise hi function me `return` line execute hoti hai, function usi waqt band ho jata hai. Uske neeche likhi hui koi bhi line kabhi nahi chalegi!",
          "Multiple Values: Python me `return x, y` likh kar ek sath 2-3 answers bhi wapas bheje ja sakte hain."
        ],
        "analogy_en": "If a restaurant waiter shouts your bill amount, that's `print()`. If the waiter hands you the actual debit card receipt so you can claim company reimbursement, that's `return`!",
        "analogy_hi": "Waiter agar zor se chillakar bol de 'Aapka bill 500 rupay hua', to ye `print()` hai. Lekin agar wo hath me receipt thama de jise tum company se claim kar sako, to wo `return` hai!",
        "example_1": {
          "title": "Proof that Print Gives None",
          "title_hi": "Kyun print se None milta hai",
          "code": "def bad_add(a, b):\n    print(a + b)\n\ndef good_add(a, b):\n    return a + b\n\nx = bad_add(2, 3)   # prints 5, but x is None!\ny = good_add(2, 3)  # y becomes 5\nprint('y multiplied by 10 =', y * 10)",
          "explanation_en": "• `bad_add` returns None because there is no `return`.\n• `good_add` returns 5, which allows multiplying `y * 10 = 50`.",
          "explanation_hi": "• `bad_add` me koi return nahi tha isliye x me None mila.\n• `good_add` ne value return ki jisse y * 10 = 50 calculate ho saka."
        },
        "example_2": {
          "title": "Real World: Discount Eligibility Checker",
          "title_hi": "Real World: Discount Eligibility",
          "code": "def is_eligible_for_discount(cart_total):\n    return cart_total >= 1000\n\ncart = 1450\nif is_eligible_for_discount(cart):\n    print('Special 20% Discount Applied!')",
          "explanation_en": "• The function returns a boolean (True/False) directly used in an `if` condition.",
          "explanation_hi": "• Function direct True ya False return karta hai jise `if` statement me check karte hain."
        },
        "challenge": {
          "prompt_en": "Write a function `square(n)` that returns `n * n`. Call it with 6 and print: `Result: 36`",
          "prompt_hi": "`square(n)` function banao jo `n * n` return kare. Use 6 ke sath call karke print karo: `Result: 36`",
          "starter_code": "# Define square(n) and return n * n:\n\n# Call and print Result:\n",
          "expected_output": "Result: 36",
          "solution_code": "def square(n):\n    return n * n\n\nprint(f'Result: {square(6)}')",
          "solution_explanation_hi": "`return n * n` se 6 * 6 = 36 return hota hai aur print ho jata hai.",
          "ego_roast_hi": "print aur return me confuse ho gaye kya? Function se answer wapas paane ke liye `return` use hota hai!",
          "ego_cheer_hi": "LEGENDARY! 🔥 Clean, professional modular logic bina kisi None trap ke!"
        }
      },
      {
        "id": "sub_5_3_mini_capstone",
        "title": "Mini Capstone: The Automated Supermarket Biller",
        "title_hi": "Mini Capstone Project: Supermarket Automated Biller",
        "icon": "🛒",
        "duration": "7 mins",
        "xp": 200,
        "what_is_it_en": "Congratulations! You now combine Variables, Lists, Loops, Conditionals, and Functions into one complete, real-world Python automation project.",
        "what_is_it_hi": "Mubarak ho! Ab tum Variables, Lists, Dictionaries, Loops aur Functions sabko milakar ek complete real-world Python automation project banaoge!",
        "why_need_it_en": "Real software engineering is not about memorizing isolated keywords; it is about orchestrating multiple concepts together into an automated solution.",
        "why_need_it_hi": "Asli software engineering alag-alag keywords ratne me nahi hai, balki sabko milakar ek real application khadi karne me hai.",
        "how_to_use_en": "Define structured functions that accept lists of item dictionaries, compute totals, apply discounts, and generate printable receipts.",
        "how_to_use_hi": "Functions banao jo items ki list accept karein, total jodein, tax lagayein aur final receipt print karein.",
        "syntax": "# Architecture:\n# 1. Variables -> Cart items\n# 2. Function -> calculate_bill(cart)\n# 3. Loop -> sum prices\n# 4. Condition -> apply discount\n# 5. Return -> final total",
        "rules_en": [
          "Separation of Concerns: Keep calculation logic separate from display logic.",
          "Reusable Components: Functions should accept parameters rather than hardcoding global variables.",
          "Test Edge Cases: Always test with empty carts or zero quantities."
        ],
        "rules_hi": [
          "Separation of Concerns: Calculation ka kaam alag function me rakho aur display ka kaam alag.",
          "Reusable Components: Functions me hardcoded values mat dalo, parameters pass karo.",
          "Edge Cases ka Dhyan: Zero items ya negative prices par code crash na ho."
        ],
        "analogy_en": "You have gathered all the Infinity Stones of Python programming. Now we snap our fingers and build a full production automated billing engine!",
        "analogy_hi": "Tumne Python ke saare hathiyar ikattha kar liye hain. Ab hum pura Supermarket Billing bot banayenge!",
        "example_1": {
          "title": "The Supermarket Cart Processor",
          "title_hi": "Cart Total aur GST Generator",
          "code": "items = [\n    {'name': 'Milk', 'price': 50},\n    {'name': 'Bread', 'price': 40},\n    {'name': 'Eggs', 'price': 70}\n]\n\ndef generate_bill(cart):\n    subtotal = sum(i['price'] for i in cart)\n    tax = subtotal * 0.05\n    return subtotal + tax\n\nprint('Final Bill with 5% GST: Rs', generate_bill(items))",
          "explanation_en": "• Combines list of dictionaries with function and math.",
          "explanation_hi": "• List, Dictionaries, aur Function ko combine karke final bill calculate karta hai."
        },
        "example_2": {
          "title": "Real World: Swiggy / Zomato Delivery Fee Waiver",
          "title_hi": "Zomato Free Delivery Rule",
          "code": "def calculate_delivery(cart_value):\n    if cart_value > 299:\n        return 0\n    return 40\n\nprint('Delivery Fee for Rs 350 cart: Rs', calculate_delivery(350))",
          "explanation_en": "• If cart is above Rs 299, delivery fee is 0; otherwise Rs 40.",
          "explanation_hi": "• 299 se upar free delivery, warna 40 rupay."
        },
        "challenge": {
          "prompt_en": "Write a function `calculate_fare(distance_km)` where base fare is 50, and each km costs 12. Return the total. Call it for 10 km and print: `Total Fare: Rs 170`",
          "prompt_hi": "`calculate_fare(distance_km)` function banao jisme base fare 50 hai aur 12 rupay per km. 10 km ke liye call karke print karo: `Total Fare: Rs 170`",
          "starter_code": "# Define calculate_fare(distance_km):\n\n# Call for 10 km and print:\n",
          "expected_output": "Total Fare: Rs 170",
          "solution_code": "def calculate_fare(distance_km):\n    return 50 + (distance_km * 12)\n\nprint('Total Fare: Rs', calculate_fare(10))",
          "solution_explanation_hi": "50 + (10 * 12) = 50 + 120 = 170. Total Fare: Rs 170 print hota hai.",
          "ego_roast_hi": "Uber/Ola ka formula calculate nahi kar pa rahe? 50 + (distance * 12) return karna hai bas!",
          "ego_cheer_hi": "🏆 PYTHON FOUNDATION CRUSHED! Tum ab beginner nahi rahe — tum officially Python Programmer ho!"
        }
      }
    ]
  }
]

content = "/**\n * ELYSIA CODE: COMPREHENSIVE PYTHON CURRICULUM TREE\n */\n\nwindow.PYTHON_CURRICULUM_TREE = " + json.dumps(tree, indent=2) + ";\n"

with open("/Users/priyanshuyadav/.gemini/antigravity/scratch/elysia-code/web/js/curriculum_tree.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Full curriculum tree written successfully. Subtopics count:")
total = sum(len(ch["subtopics"]) for ch in tree)
print(f"Total Chapters: {len(tree)}, Total Subtopics: {total}")
