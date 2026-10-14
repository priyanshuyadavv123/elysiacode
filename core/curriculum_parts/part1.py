"""
Part 1: The Absolute Basics (Zero to Code)
Chapters 1 to 5 with exact syllabus titles and subtopics.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 1: Welcome to the World of Python
    # =========================================================================
    {
        "id": "ch1_welcome_python",
        "part_number": 1,
        "part_title": "PART 1: THE ABSOLUTE BASICS (ZERO TO CODE)",
        "chapter_number": 1,
        "title": "Chapter 1: Welcome to the World of Python",
        "subtitle_en": "Start from absolute zero — understand computers, setup, and write line #1",
        "subtitle_hi": "Zero se shuruat — computer ki soch, setup aur pehla program",
        "icon": "🐍",
        "estimated_time": "35 mins",
        "prerequisites_en": "None! Just curiosity and a computer.",
        "prerequisites_hi": "Kuch nahi! Bas seekhne ki ichha aur ek computer.",
        "learning_objectives_en": [
            "Understand why Python is the #1 language for AI, web, and automation",
            "Master the Translator/Interpreter mental model",
            "Know how to install Python and set up IDLE, VS Code, or Thonny",
            "Write, save, and execute your very first .py file via terminal"
        ],
        "learning_objectives_hi": [
            "Samjho Python AI, web aur automation me sabse aage kyun hai",
            "Interpreter aur Translator ka mental model seekho",
            "Python install karna aur VS Code / IDLE setup karna seekho",
            "Apni pehli .py file save karke terminal se run karna seekho"
        ],
        "recap_en": "You learned what Python is, how interpreters translate code to machine instructions, how to set up your environment, and how to run Python scripts from the command prompt.",
        "recap_hi": "Aapne seekha ki Python kya hai, interpreter code kaise translate karta hai, environment setup kaise karein, aur terminal se script kaise chalayein.",
        "subtopics": [
            {
                "id": "ch1_sub1_what_is_python",
                "title": "What is Python and why is it so popular?",
                "title_hi": "Python kya hai aur itna popular kyun hai?",
                "icon": "🌟",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Python is a high-level, interpreted programming language created by Guido van Rossum in 1991. It emphasizes readable, clean syntax that looks almost like plain English.",
                "what_is_it_hi": "Python ek high-level, human-friendly programming language hai jise Guido van Rossum ne 1991 me banaya tha. Iska syntax itna saaf aur aasan hai ki padhne me bilkul simple English jaisa lagta hai.",
                "why_need_it_en": "Python powers Artificial Intelligence (PyTorch, TensorFlow), web servers (Django, FastAPI), data science (Pandas), and automation scripts worldwide because developers can write in 5 lines what takes 50 lines in other languages.",
                "why_need_it_hi": "Python se Artificial Intelligence, NASA ke calculations, Instagram ka backend, aur hacker scripting sab kuch hota hai. Jo kaam Java/C++ me 50 line leta hai, Python me 5 line me ho jata hai.",
                "how_to_use_en": "You write clear statements without boilerplate like semicolons or class wrappers for simple scripts.",
                "how_to_use_hi": "Bina kisi semicolon (;) ya curly brackets ({}) ke seedhe direct instructions likho.",
                "syntax": "print(\"Python makes programming simple!\")",
                "rules_en": [
                    "Python is case-sensitive: 'python' and 'Python' are treated differently.",
                    "Python uses indentation (whitespace) instead of curly braces to define blocks.",
                    "Python is dynamically typed: you don't need to specify variable types in advance."
                ],
                "rules_hi": [
                    "Python case-sensitive hai: chhota 'print' chalega, bada 'Print' crash karega.",
                    "Python blocks ke liye indentation (spacing) use karta hai, curly braces nahi.",
                    "Python dynamically typed hai: variable ka type pehle se declare nahi karna padta."
                ],
                "analogy_en": "Think of C++ as driving a manual tractor with 12 gears, while Python is like driving a modern automatic electric car with GPS assist.",
                "analogy_hi": "C++ ya Java ko 12 gear wali manual gaadi samjho, jabki Python ek automatic electric car hai jisme bas accelerator dabana hai aur gaadi chal padti hai.",
                "common_mistakes": [
                    {
                        "mistake": "Writing Print('Hello') with a capital P.",
                        "why_it_fails_en": "Python built-ins are lowercase. 'Print' causes NameError: name 'Print' is not defined.",
                        "why_it_fails_hi": "Python me built-in functions chhote letters me hote hain. Bada P likhne par NameError aayega.",
                        "fix": "Use lowercase print('Hello')."
                    }
                ],
                "example_1": {
                    "title": "Clean Readability in Python",
                    "title_hi": "Python ka saaf suthra syntax",
                    "code": "language = 'Python'\nprint(f'{language} is simple and powerful!')",
                    "expected_output": "Python is simple and powerful!",
                    "explanation_en": "Defines a variable and prints it inside an f-string cleanly.",
                    "explanation_hi": "Ek variable banata hai aur f-string se terminal me message dikhata hai."
                },
                "example_2": {
                    "title": "Looping Without Boilerplate",
                    "title_hi": "Bina kisi jhanjhat ke loop chalana",
                    "code": "for skill in ['Web', 'AI', 'Automation']:\n    print('Python excels in:', skill)",
                    "expected_output": "Python excels in: Web\nPython excels in: AI\nPython excels in: Automation",
                    "explanation_en": "Loops over a list with pure English-like readability.",
                    "explanation_hi": "List ke items par aasan English jaisa loop chalaata hai."
                },
                "challenge": {
                    "prompt_en": "Print the exact sentence: Python is everywhere!",
                    "prompt_hi": "Screen par exact ye sentence print karo: Python is everywhere!",
                    "starter_code": "# Type your code below:\n",
                    "expected_output": "Python is everywhere!",
                    "solution_code": "print('Python is everywhere!')",
                    "solution_explanation_en": "print() displays the string text passed inside parentheses to the standard output.",
                    "solution_explanation_hi": "print() ke andar string pass karne se wo terminal screen par show ho jata hai.",
                    "hints": ["Use the print() function with single or double quotes."],
                    "ego_roast_hi": "Bhai bas ek line likhni hai print('...'), isme bhi soch rahe ho?",
                    "ego_cheer_hi": "Shabash! Pehla kadam complete hua! 🔥"
                }
            },
            {
                "id": "ch1_sub2_translator_analogy",
                "title": "How computers understand code (The Translator Analogy)",
                "title_hi": "Computer code kaise samajhta hai? (Translator Analogy)",
                "icon": "🗣️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Computers only understand binary electricity (0s and 1s - machine code). An interpreter translates your human-readable Python code line-by-line into machine code on the fly.",
                "what_is_it_hi": "Computer sirf binary (0 aur 1, on aur off) samajhta hai. Python interpreter ek translator ki tarah kaam karta hai jo aapki likhi line ko padh kar turant computer ko samjhata hai.",
                "why_need_it_en": "Without an interpreter or compiler, humans would have to write incomprehensible numeric binary sequences to execute a simple calculation.",
                "why_need_it_hi": "Agar translator na ho to hume 01010101 jaise binary code me sab kuch likhna padega jo koi insaan yaad nahi rakh sakta.",
                "how_to_use_en": "When you run `python main.py`, the Python interpreter reads line 1, checks syntax, converts it to bytecode (.pyc), executes it, then moves to line 2.",
                "how_to_use_hi": "Jab aap terminal me python file run karte ho, interpreter line-by-line code padh kar execute karta hai.",
                "syntax": "# Human Code -> Python Bytecode (.pyc) -> CPU Machine Code (010101)\nprint(2 + 2)",
                "rules_en": [
                    "Python is interpreted: if line 10 has an error, lines 1 through 9 still execute before crashing.",
                    "Syntax errors are caught during the initial compile-to-bytecode phase before execution begins.",
                    "Runtime errors trigger when the faulty line is actually reached."
                ],
                "rules_hi": [
                    "Python interpreted hai: agar line 10 me error hai to line 1 se 9 pehle chal jayengi.",
                    "Syntax error pehle hi pakad liya jata hai.",
                    "Runtime error tab aata hai jab wo particular line execute hoti hai."
                ],
                "analogy_en": "Imagine a foreign diplomat speaking Hindi and an ambassador speaking Japanese. A live simultaneous interpreter translates sentence by sentence in real time. That is Python!",
                "analogy_hi": "Socho ek Japanese PM aur Indian PM baat kar rahe hain. Beech me khada translator ek-ek sentence sunkar turant translate karta hai. Wahi Python Interpreter hai!",
                "common_mistakes": [
                    {
                        "mistake": "Thinking Python code is directly running on bare silicon hardware.",
                        "why_it_fails_en": "Python runs on top of the Python Virtual Machine (PVM).",
                        "why_it_fails_hi": "Python direct hardware par nahi, PVM (Python Virtual Machine) ke upar chalta hai.",
                        "fix": "Remember the hierarchy: Python Code -> Bytecode -> PVM -> OS/CPU."
                    }
                ],
                "example_1": {
                    "title": "Instant Translation and Execution",
                    "title_hi": "Turant Translation aur Output",
                    "code": "print('Line 1: Translated & Executed')\nprint('Line 2: Translated & Executed')",
                    "expected_output": "Line 1: Translated & Executed\nLine 2: Translated & Executed",
                    "explanation_en": "Each line is interpreted in strict sequential order.",
                    "explanation_hi": "Interpreter ek ke baad ek line ko translate aur execute karta hai."
                },
                "example_2": {
                    "title": "Calculation On the Fly",
                    "title_hi": "Calculations turant karna",
                    "code": "result = (100 * 4) + 50\nprint('Computed value:', result)",
                    "expected_output": "Computed value: 450",
                    "explanation_en": "Evaluates the mathematical expression and prints the result.",
                    "explanation_hi": "Mathematical calculation karke output print karta hai."
                },
                "challenge": {
                    "prompt_en": "Print the result of 15 multiplied by 4 using Python's print(15 * 4).",
                    "prompt_hi": "Python se 15 aur 4 ka guna (multiplication) print karo: print(15 * 4)",
                    "starter_code": "# Calculate and print 15 * 4:\n",
                    "expected_output": "60",
                    "solution_code": "print(15 * 4)",
                    "solution_explanation_en": "Python calculates 15 * 4 to 60 and passes the value to print().",
                    "solution_explanation_hi": "Python 15 * 4 ko calculate karke 60 terminal par print karta hai.",
                    "hints": ["Do not put quotes around 15 * 4 if you want math, not text."],
                    "ego_roast_hi": "Maths se darr lagta hai kya? Bas print(15 * 4) likhna hai!",
                    "ego_cheer_hi": "Great! CPU ne aapka math order 1 millisecond me execute kar diya! ⚡"
                }
            },
            {
                "id": "ch1_sub3_installing_python",
                "title": "Downloading and installing Python (Windows, Mac, Linux)",
                "title_hi": "Python download aur install karna (Windows, Mac, Linux)",
                "icon": "💻",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "To run Python code locally, your computer needs the official Python runtime from python.org.",
                "what_is_it_hi": "Apne computer par Python chalane ke liye official python.org website se Python runtime install karna padta hai.",
                "why_need_it_en": "Without the runtime installed, your operating system terminal will report: 'python: command not found'.",
                "why_need_it_hi": "Bina Python install kiye terminal bolegi 'command not found'.",
                "how_to_use_en": "Windows: Download installer from python.org and CHECK 'Add python.exe to PATH'. Mac: Use brew install python or official PKG installer. Linux: sudo apt update && sudo apt install python3.",
                "how_to_use_hi": "Windows par installer chalate waqt 'Add python.exe to PATH' checkbox zaroor tick karo! Mac par brew ya official installer, Linux par apt.",
                "syntax": "# Verify installation in terminal:\npython --version  # or python3 --version",
                "rules_en": [
                    "CRITICAL on Windows: Always check 'Add Python to PATH' during installation.",
                    "On macOS and modern Linux, the command is usually 'python3' (since 'python' was Python 2).",
                    "Verify by running 'python3 --version' in Command Prompt or Terminal."
                ],
                "rules_hi": [
                    "Windows par 'Add Python to PATH' tick karna sabse zaroori step hai.",
                    "Mac aur Linux par aksar 'python3' command likhna padta hai.",
                    "Terminal me 'python3 --version' run karke check karo."
                ],
                "analogy_en": "Installing Python is like installing the Hindi or English dictionary plugin into your computer's brain so it understands your vocabulary.",
                "analogy_hi": "Python install karna matlab computer ke dimaag me ek naye language ka dictionary software install karna taaki wo aapki bhasha samajh sake.",
                "common_mistakes": [
                    {
                        "mistake": "Forgetting to check 'Add Python to PATH' on Windows installer.",
                        "why_it_fails_en": "Command Prompt cannot find python.exe without PATH configured.",
                        "why_it_fails_hi": "Terminal ko pata hi nahi chalta ki python.exe kahan rakha hai.",
                        "fix": "Re-run installer, choose Modify, and check 'Add to PATH'."
                    }
                ],
                "example_1": {
                    "title": "Checking Python Version",
                    "title_hi": "Python version check karna",
                    "code": "import sys\nprint('Running on Python:', sys.version.split()[0])",
                    "expected_output": "Running on Python: 3.14.7",
                    "explanation_en": "Imports sys to verify the exact active Python version.",
                    "explanation_hi": "sys module se pata chalta hai ki active Python version kya hai."
                },
                "example_2": {
                    "title": "System Platform Identification",
                    "title_hi": "Operating System detect karna",
                    "code": "import platform\nprint('Platform detected:', platform.system())",
                    "expected_output": "Platform detected: Darwin",
                    "explanation_en": "Demonstrates built-in library availability right out of the box.",
                    "explanation_hi": "Dikhata hai ki Python install hote hi built-in libraries ready ho jaati hain."
                },
                "challenge": {
                    "prompt_en": "Print the message: Python installed successfully!",
                    "prompt_hi": "Print karo: Python installed successfully!",
                    "starter_code": "# Print the confirmation message:\n",
                    "expected_output": "Python installed successfully!",
                    "solution_code": "print('Python installed successfully!')",
                    "solution_explanation_en": "Simple print verification confirming execution capability.",
                    "solution_explanation_hi": "Verification message print karne ka standard tareeqa.",
                    "hints": ["Use single quotes or double quotes."],
                    "ego_roast_hi": "Installer chalana to seekh gaye, ab code bhi likh lo!",
                    "ego_cheer_hi": "Awesome! System verification complete! 🚀"
                }
            },
            {
                "id": "ch1_sub4_workspace_setup",
                "title": "Setting up a beginner-friendly workspace (IDLE vs. VS Code vs. Thonny)",
                "title_hi": "Beginner workspace setup (IDLE vs. VS Code vs. Thonny)",
                "icon": "🛠️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A code editor or IDE (Integrated Development Environment) is where you write, edit, and debug your Python code with syntax highlighting and auto-completion.",
                "what_is_it_hi": "IDE ya Code Editor wo software hai jisme aap code likhte ho — jaise Word doc me essay likhte ho, waise hi VS Code ya Thonny me Python code likhte ho.",
                "why_need_it_en": "Writing code in Notepad has no color coding, no line numbers, and no error detection. A proper editor catches typos before you even run the script.",
                "why_need_it_hi": "Notepad me code likhoge to na color dikhega na galti pakad paoge. Ek achha editor galti hote hi red line dikha deta hai.",
                "how_to_use_en": "Beginners: Thonny (shows variable memory live) or IDLE (comes with Python). Serious developers: VS Code with Python extension.",
                "how_to_use_hi": "Beginners ke liye Thonny best hai kyunki wo memory live dikhata hai. Industry standard ke liye VS Code use karo.",
                "syntax": "# A good editor gives syntax highlighting:\ndef greet(name):\n    return f\"Hello, {name}\"",
                "rules_en": [
                    "IDLE: Built into official Python installer, no extra download required.",
                    "Thonny: Best for visual learners; steps through loops and memory variables.",
                    "VS Code: Industry standard; install the official Microsoft Python extension."
                ],
                "rules_hi": [
                    "IDLE: Python ke sath free aata hai, alag se kuch download nahi karna.",
                    "Thonny: Step-by-step memory dekhne ke liye sabse best beginner tool.",
                    "VS Code: Software companies ka number 1 favorite editor."
                ],
                "analogy_en": "Notepad is like writing an architect blueprint on a paper napkin. VS Code is AutoCAD with real-time laser measurement.",
                "analogy_hi": "Notepad par code likhna tissue paper par building ka naksha banane jaisa hai. VS Code ek modern computerized studio jaisa hai.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to write Python in Microsoft Word or Google Docs.",
                        "why_it_fails_en": "Word processors replace straight quotes with curly smart quotes which cause SyntaxErrors.",
                        "why_it_fails_hi": "Word processors quotes ko tedha kar dete hain (“...”) jisse Python crash ho jata hai.",
                        "fix": "Only use plain text editors: VS Code, Thonny, IDLE, or Sublime."
                    }
                ],
                "example_1": {
                    "title": "IDE Features: Indentation and Comments",
                    "title_hi": "Editor me saaf indentation",
                    "code": "# A clean workspace makes indentation clear\nmode = 'VS Code'\nprint('Editor configured:', mode)",
                    "expected_output": "Editor configured: VS Code",
                    "explanation_en": "Code editors auto-indent by 4 spaces when you press Enter.",
                    "explanation_hi": "Achhe editors Enter dabate hi automatically 4 spaces aage badha dete hain."
                },
                "example_2": {
                    "title": "Configuring Python Path",
                    "title_hi": "Python workspace settings",
                    "code": "tools = ['IDLE', 'Thonny', 'VS Code']\nprint('Top beginner editors:', ', '.join(tools))",
                    "expected_output": "Top beginner editors: IDLE, Thonny, VS Code",
                    "explanation_en": "Shows the trio of beginner-friendly programming environments.",
                    "explanation_hi": "Beginner programming ke top 3 environments ko print karta hai."
                },
                "challenge": {
                    "prompt_en": "Print: Workspace ready for Python!",
                    "prompt_hi": "Print karo: Workspace ready for Python!",
                    "starter_code": "# Setup verification code:\n",
                    "expected_output": "Workspace ready for Python!",
                    "solution_code": "print('Workspace ready for Python!')",
                    "solution_explanation_en": "Confirms readiness of the workspace.",
                    "solution_explanation_hi": "Workspace verification ka simple code.",
                    "hints": ["Double check the exact spelling and exclamation mark."],
                    "ego_roast_hi": "IDE khol li? Ab print statement likho!",
                    "ego_cheer_hi": "Workspace lock and loaded! 🎯"
                }
            },
            {
                "id": "ch1_sub5_hello_world",
                "title": "Writing your very first line of code: print(\"Hello, World!\")",
                "title_hi": "Pehla code likhna: print(\"Hello, World!\")",
                "icon": "👋",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The universal tradition of every programmer since 1974: printing 'Hello, World!' to confirm your compiler or interpreter is alive and responding.",
                "what_is_it_hi": "Duniya ke har coder ki 50 saal purani parampara: naye system par sabse pehle 'Hello, World!' print karke check karna ki code chal raha hai.",
                "why_need_it_en": "It tests your entire software chain: editor -> file saving -> interpreter -> standard output display.",
                "why_need_it_hi": "Ye test karta hai ki editor, interpreter aur screen output sab theek se jud chuke hain.",
                "how_to_use_en": "Call print() and pass the text inside quotation marks between parentheses.",
                "how_to_use_hi": "print() likho aur brackets ke andar quotes me apna text daalo.",
                "syntax": "print(\"Hello, World!\")",
                "rules_en": [
                    "Quotes must match: either both single ('...') or both double (\"...\").",
                    "Parentheses are mandatory in Python 3. In Python 2 it was a statement, but Python 3 made it a function.",
                    "The text inside quotes is called a String literal."
                ],
                "rules_hi": [
                    "Quotes match hone chahiye: dono single ya dono double.",
                    "Python 3 me brackets mandatory hain.",
                    "Quotes ke andar wale text ko String bolte hain."
                ],
                "analogy_en": "It is like testing a brand new microphone on stage by tapping it and saying 'Mic check 1, 2, 3!'.",
                "analogy_hi": "Ye naya mic check karne jaisa hai: 'Testing 1, 2, 3, aawaaz aa rahi hai?'!",
                "common_mistakes": [
                    {
                        "mistake": "Mismatched quotes: print('Hello, World!\")",
                        "why_it_fails_en": "SyntaxError: unterminated string literal.",
                        "why_it_fails_hi": "Shuru single quote se kiya aur band double quote se kiya to SyntaxError aayega.",
                        "fix": "Use identical opening and closing quotes."
                    }
                ],
                "example_1": {
                    "title": "The Canonical Hello World",
                    "title_hi": "Original Hello World",
                    "code": "print('Hello, World!')",
                    "expected_output": "Hello, World!",
                    "explanation_en": "The purest and most famous line of code in computing history.",
                    "explanation_hi": "Duniya ki sabse famous line of code."
                },
                "example_2": {
                    "title": "Double Quotes Variation",
                    "title_hi": "Double quotes ke sath",
                    "code": "print(\"Hello, World from Elysia!\")",
                    "expected_output": "Hello, World from Elysia!",
                    "explanation_en": "Double quotes are completely interchangeable with single quotes for strings.",
                    "explanation_hi": "Double quotes aur single quotes dono barabar kaam karte hain."
                },
                "challenge": {
                    "prompt_en": "Write the exact line: print(\"Hello, World!\")",
                    "prompt_hi": "Ye exact line likho: print(\"Hello, World!\")",
                    "starter_code": "# Write the universal programmer line below:\n",
                    "expected_output": "Hello, World!",
                    "solution_code": "print(\"Hello, World!\")",
                    "solution_explanation_en": "Standard print statement outputting Hello, World!",
                    "solution_explanation_hi": "Sabse pehla standard print code.",
                    "hints": ["Check your capitalization and exclamation mark."],
                    "ego_roast_hi": "Coder banna hai to Hello World to likhna hi padega!",
                    "ego_cheer_hi": "CONGRATULATIONS! You are officially a programmer! 🏆"
                }
            },
            {
                "id": "ch1_sub6_terminal_cli",
                "title": "Understanding the terminal and command prompt",
                "title_hi": "Terminal aur Command Prompt ko samajhna",
                "icon": "🖥️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The terminal (Command Prompt/PowerShell on Windows, Terminal on Mac/Linux) is a text-based interface to control your computer without clicking graphical buttons.",
                "what_is_it_hi": "Terminal ek aisi black-and-white screen hai jahan aap mouse se click karne ke bajaye text commands type karke computer ko control karte ho.",
                "why_need_it_en": "Real servers in the cloud (AWS, Google Cloud) do not have mice or desktop displays. Professional software engineers work primarily through the command line.",
                "why_need_it_hi": "Cloud servers me koi mouse ya graphical screen nahi hoti. Professional engineers terminal ke zariye hi server chalate hain.",
                "how_to_use_en": "Basic commands: pwd / cd (change directory), ls / dir (list files), clear / cls (clear screen).",
                "how_to_use_hi": "cd se folder badalte hain, ls ya dir se files dekhte hain, clear se screen saaf karte hain.",
                "syntax": "# In terminal:\npython app.py",
                "rules_en": [
                    "Commands are case-sensitive on macOS and Linux.",
                    "Spaces in folder paths must be enclosed in quotes (e.g., cd 'My Documents').",
                    "Ctrl+C terminates any running Python process in the terminal."
                ],
                "rules_hi": [
                    "Mac aur Linux par terminal case-sensitive hota hai.",
                    "Agar folder ke naam me space hai to quotes lagana padta hai.",
                    "Ctrl+C dabane se koi bhi chalti hui Python script turant ruk jaati hai."
                ],
                "analogy_en": "A GUI desktop is like ordering from a picture menu at McDonald's. The terminal is like walking straight into the kitchen and telling the chef exactly what ingredients to mix.",
                "analogy_hi": "Desktop mouse se chalana menu card dekhne jaisa hai. Terminal sidha kitchen me jaakar chef ko exact recipe batane jaisa hai.",
                "common_mistakes": [
                    {
                        "mistake": "Typing Python code directly into the terminal without entering Python interactive shell first.",
                        "why_it_fails_en": "The bash/zsh/cmd shell thinks 'print' is a system binary command and errors with 'command not found'.",
                        "why_it_fails_hi": "Terminal shell sochti hai ki print koi computer app ka naam hai aur error de deti hai.",
                        "fix": "Type 'python' first to launch the Python REPL, or run 'python file.py'."
                    }
                ],
                "example_1": {
                    "title": "Current Working Directory Check in Python",
                    "title_hi": "Python se current folder check karna",
                    "code": "import os\nprint('Running inside directory:', bool(os.getcwd()))",
                    "expected_output": "Running inside directory: True",
                    "explanation_en": "os.getcwd() retrieves the directory from which the script was launched.",
                    "explanation_hi": "os.getcwd() batata hai ki script kis folder se chali hai."
                },
                "example_2": {
                    "title": "Command-Line Arguments Emulation",
                    "title_hi": "Terminal arguments access karna",
                    "code": "import sys\nprint('Script name:', sys.argv[0])",
                    "expected_output": "Script name: main.py",
                    "explanation_en": "sys.argv contains arguments passed from the command line.",
                    "explanation_hi": "sys.argv me terminal se pass kiye gaye arguments aate hain."
                },
                "challenge": {
                    "prompt_en": "Print: Terminal mastery unlocked!",
                    "prompt_hi": "Print karo: Terminal mastery unlocked!",
                    "starter_code": "# Terminal lesson completion:\n",
                    "expected_output": "Terminal mastery unlocked!",
                    "solution_code": "print('Terminal mastery unlocked!')",
                    "solution_explanation_en": "Outputs the confirmation text.",
                    "solution_explanation_hi": "Terminal achievement confirmation.",
                    "hints": ["Double check spelling."],
                    "ego_roast_hi": "Command prompt dekh ke darr mat, bas type karo!",
                    "ego_cheer_hi": "Terminal wizard in the making! 🧙‍♂️"
                }
            },
            {
                "id": "ch1_sub7_save_run_py",
                "title": "How to save and run a Python file (.py)",
                "title_hi": "Python file (.py) ko save aur run karna",
                "icon": "💾",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A Python file is a plain text file saved with the extension '.py'. You write code in your editor, save it as 'myscript.py', and execute it from terminal.",
                "what_is_it_hi": "Python file ek simple text file hoti hai jiska naam '.py' par khatam hota hai (jaise hello.py). Isko editor me likh kar save karte hain aur terminal se run karte hain.",
                "why_need_it_en": "Interactive shells forget your code the moment you close the window. Saving a .py file preserves your program forever so it can run anytime.",
                "why_need_it_hi": "Agar file save nahi karoge to window band hote hi code gayab ho jayega. .py file banane se code hamesha ke liye safe rehta hai.",
                "how_to_use_en": "1. In VS Code, create a file 'hello.py'. 2. Type print('Hello!'). 3. Save (Ctrl+S or Cmd+S). 4. In terminal type: python hello.py.",
                "how_to_use_hi": "1. File banao 'hello.py'. 2. Code likho. 3. Save karo (Ctrl+S). 4. Terminal me likho: python hello.py.",
                "syntax": "# Command to run a python script:\n# python filename.py",
                "rules_en": [
                    "The extension must be exactly .py (not .py.txt or .doc).",
                    "Do not put spaces in filenames (use underscores: my_script.py).",
                    "You must be inside the same folder where the file is saved when running 'python filename.py'."
                ],
                "rules_hi": [
                    "File extension .py hi hona chahiye, galti se .txt mat hone dena.",
                    "File ke naam me spaces mat daalo (my_code.py likho, my code.py nahi).",
                    "Terminal me wahi folder open hona chahiye jahan file rakhi hai."
                ],
                "analogy_en": "Typing in a REPL is like writing with chalk on a blackboard (erased immediately). Saving a .py file is printing a book in permanent ink.",
                "analogy_hi": "REPL me code likhna blackboard par chalk se likhne jaisa hai jo turant mit jata hai. .py file banana diary me permanent pen se likhne jaisa hai.",
                "common_mistakes": [
                    {
                        "mistake": "Windows hiding file extensions and saving as 'test.py.txt'.",
                        "why_it_fails_en": "Running 'python test.py' fails with [Errno 2] No such file or directory.",
                        "why_it_fails_hi": "Windows chupke se .txt jod deta hai aur terminal ko file milti hi nahi.",
                        "fix": "Enable 'File name extensions' in Windows Explorer View settings."
                    }
                ],
                "example_1": {
                    "title": "Verifying Script Execution",
                    "title_hi": "Script execute hone ka proof",
                    "code": "print('File executed from top to bottom.')\nprint('Exit code: 0 (Success)')",
                    "expected_output": "File executed from top to bottom.\nExit code: 0 (Success)",
                    "explanation_en": "Python runs scripts sequentially to the final line and exits cleanly.",
                    "explanation_hi": "Python upar se neeche saari lines chala kar aakhiri line par rukta hai."
                },
                "example_2": {
                    "title": "Multi-line Script Execution",
                    "title_hi": "Multiple lines ka execution",
                    "code": "lines = 3\nprint(f'Script contains {lines} executed instructions.')",
                    "expected_output": "Script contains 3 executed instructions.",
                    "explanation_en": "Variables and expressions saved in scripts work harmoniously.",
                    "explanation_hi": "Script me save kiye gaye variables aur expressions run hote hain."
                },
                "challenge": {
                    "prompt_en": "Print: Script saved as main.py and executed cleanly!",
                    "prompt_hi": "Print karo: Script saved as main.py and executed cleanly!",
                    "starter_code": "# Complete the script execution message:\n",
                    "expected_output": "Script saved as main.py and executed cleanly!",
                    "solution_code": "print('Script saved as main.py and executed cleanly!')",
                    "solution_explanation_en": "Simple confirmation of script run.",
                    "solution_explanation_hi": "Script run ka confirmation print.",
                    "hints": ["Match the string exactly."],
                    "ego_roast_hi": "Save karna to seekh gaye na? Ab print karo!",
                    "ego_cheer_hi": "Chapter 1 Conquered! You are ready for Input & Output! 🚀"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 2: Talking to the Computer (Output and Input)
    # =========================================================================
    {
        "id": "ch2_talking_computer",
        "part_number": 1,
        "part_title": "PART 1: THE ABSOLUTE BASICS (ZERO TO CODE)",
        "chapter_number": 2,
        "title": "Chapter 2: Talking to the Computer (Output and Input)",
        "subtitle_en": "Master print parameters, user input, comments, escape sequences, and build a chatbot",
        "subtitle_hi": "Print ke parameters, user se input lena, comments, aur chatbot banana",
        "icon": "💬",
        "estimated_time": "40 mins",
        "prerequisites_en": "Chapter 1 basics (how to write and run print statements).",
        "prerequisites_hi": "Chapter 1 ke basics (print statement likhna aur chalana).",
        "learning_objectives_en": [
            "Harness sep and end parameters in print()",
            "Understand that input() ALWAYS returns a string",
            "Use single-line (#) and multi-line docstrings correctly",
            "Master escape sequences (\\n, \\t, \\\\)",
            "Build Mini-Project: An Interactive Welcome Chatbot"
        ],
        "learning_objectives_hi": [
            "print() ke sep aur end parameters master karo",
            "Samjho ki input() HAMESHA string return karta hai",
            "Comments (#) aur multi-line strings ka sahi use",
            "Escape characters (\\n, \\t, \\\\) samajhna",
            "Mini-Project: Welcome Chatbot banana"
        ],
        "recap_en": "You learned how to format terminal output with sep and end, how to capture keyboard input (and why it arrives as str), how to escape characters, and built your first interactive chatbot.",
        "recap_hi": "Aapne seekha print ke sep aur end parameters, user se input lena, escape characters aur apna pehla welcome chatbot banaya.",
        "subtopics": [
            {
                "id": "ch2_sub1_print_in_detail",
                "title": "The print() function in detail (sep, end parameters)",
                "title_hi": "print() function detail me (sep aur end parameters)",
                "icon": "🖨️",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "The print() function has hidden superpower arguments: 'sep' controls what goes between items (default is space ' '), and 'end' controls what gets appended at the finish (default is newline '\\n').",
                "what_is_it_hi": "print() me do powerful parameters hote hain: 'sep' (items ke beech kya aayega, default space ' ' hai) aur 'end' (aakhri me kya lagega, default newline '\\n' hai).",
                "why_need_it_en": "Without sep, formatting dates (2026-10-12) or CSV items requires clumsy string concatenation. Without end, consecutive print statements cannot appear on the same line.",
                "why_need_it_hi": "Agar sep na ho to date ya path format karna mushkil ho jayega. Agar end='' use na karein to do print statement ek hi line me print nahi ho sakte.",
                "how_to_use_en": "Pass named arguments: print(a, b, sep='-') or print('Loading', end='...').",
                "how_to_use_hi": "Named arguments pass karo: print(1, 2, sep=':') ya print('Wait', end='...').",
                "syntax": "print(item1, item2, sep=\" separator \", end=\" ending \")",
                "rules_en": [
                    "Default sep is ' ' (single space).",
                    "Default end is '\\n' (moves to the next line).",
                    "You can pass empty strings: sep='' or end=''."
                ],
                "rules_hi": [
                    "Default sep ek space ' ' hota hai.",
                    "Default end newline '\\n' hota hai jo cursor ko agli line me bhejta hai.",
                    "sep='' ya end='' karke blank bhi kar sakte ho."
                ],
                "analogy_en": "Imagine a necklace. 'sep' is the bead you put BETWEEN gems. 'end' is the lock clasp you attach at the very tail of the necklace.",
                "analogy_hi": "Ek maala samjho. 'sep' wo moti hai jo har heere ke BEECH me lagta hai. Aur 'end' wo aakhri kunda hai jo maala ke aakhri sire par band hota hai.",
                "common_mistakes": [
                    {
                        "mistake": "Writing print('A', 'B', sep) without an equal sign.",
                        "why_it_fails_en": "sep is a keyword parameter. Writing sep alone passes a non-existent variable name causing NameError.",
                        "why_it_fails_hi": "sep='-' likhna hota hai. Bina equal sign ke Python use variable samajh kar crash kar dega.",
                        "fix": "Always use keyword assignment syntax: sep='-' and end=' '."
                    }
                ],
                "example_1": {
                    "title": "Custom Separator for Dates",
                    "title_hi": "Date format karne ke liye custom separator",
                    "code": "print('2026', '10', '12', sep='-')",
                    "expected_output": "2026-10-12",
                    "explanation_en": "Replaces default spaces with hyphens between items.",
                    "explanation_hi": "Space ki jagah hyphens daal kar date format banata hai."
                },
                "example_2": {
                    "title": "Custom End Parameter for Progress Bars",
                    "title_hi": "Ek hi line me output rakhna (end='')",
                    "code": "print('Loading', end='...')\nprint('Done!')",
                    "expected_output": "Loading...Done!",
                    "explanation_en": "Line 1 doesn't jump to a new row because end='...', so Line 2 prints right after.",
                    "explanation_hi": "Pehle print me end='...' hone se agli line neeche nahi balki usi ke sath aage jud jaati hai."
                },
                "challenge": {
                    "prompt_en": "Print the numbers 1, 2, 3 separated by ' -> ' using sep=' -> '.",
                    "prompt_hi": "1, 2, 3 ko sep=' -> ' use karke print karo taaki output aaye: 1 -> 2 -> 3",
                    "starter_code": "# Use print with sep parameter:\n",
                    "expected_output": "1 -> 2 -> 3",
                    "solution_code": "print(1, 2, 3, sep=' -> ')",
                    "solution_explanation_en": "print(1, 2, 3, sep=' -> ') inserts ' -> ' between each argument.",
                    "solution_explanation_hi": "sep=' -> ' har item ke beech arrow laga deta hai.",
                    "hints": ["Pass 1, 2, 3 as separate arguments before sep=' -> '."],
                    "ego_roast_hi": "sep parameter use karna bhool gaye kya?",
                    "ego_cheer_hi": "Clean formatting mastery achieved! 🎯"
                }
            },
            {
                "id": "ch2_sub2_input_function",
                "title": "Asking the user for information: The input() function",
                "title_hi": "User se information maangna: input() function",
                "icon": "📥",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "The input() function pauses your program, shows an optional prompt message, waits for the user to type something on their keyboard and press Enter, and returns whatever they typed as a string (str).",
                "what_is_it_hi": "input() function program ko pause kar deta hai, screen par prompt dikhata hai, aur user ke typing karke Enter dabane ka wait karta hai. Jo bhi type kiya jata hai wo HAMESHA String (str) ban kar milta hai.",
                "why_need_it_en": "Real software must be dynamic. Programs need user names, passwords, search terms, and form inputs to do meaningful work.",
                "why_need_it_hi": "Bina input ke program har baar ek hi boring kaam karega. Dynamic apps banane ke liye user se data lena zaroori hai.",
                "how_to_use_en": "name = input('Enter your name: '). Note: For math, always convert using int() or float(): age = int(input('Age: ')).",
                "how_to_use_hi": "name = input('Naam batao: '). Numbers ke liye int() lagana zaroori hai: age = int(input('Age: ')).",
                "syntax": "user_response = input(\"Optional question prompt: \")",
                "rules_en": [
                    "CRITICAL LAW: input() ALWAYS returns a string (str), NEVER a number, even if user types '42'.",
                    "To do arithmetic on input, you MUST typecast: num = int(input()).",
                    "input() pauses the execution thread entirely until the user hits Enter."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: input() HAMESHA string (text) deta hai, chahe user 100 hi kyun na type kare.",
                    "Math calculation ke liye int() ya float() me wrap karna zaroori hai.",
                    "Jab tak user Enter nahi dabata, program aage nahi badhta."
                ],
                "analogy_en": "input() is like an ATM asking 'Please enter your 4-digit PIN' and waiting patiently before counting your cash.",
                "analogy_hi": "input() ATM machine jaisa hai jo screen par 'PIN enter karo' likh kar ruk jata hai jab tak aap number type karke Enter na daba do.",
                "common_mistakes": [
                    {
                        "mistake": "Adding input numbers directly: a = input(); b = input(); print(a + b)",
                        "why_it_fails_en": "Since inputs are strings, typing 5 and 5 outputs '55' (text concatenation), not 10!",
                        "why_it_fails_hi": "input() text deta hai, to 5 aur 5 milkar '55' ban jayenge, 10 nahi!",
                        "fix": "Convert with int(): a = int(input()); b = int(input()); print(a + b)"
                    }
                ],
                "example_1": {
                    "title": "String Input",
                    "title_hi": "Text input lena",
                    "code": "# Simulating input in test mode\nuser_name = 'Priyanshu'\nprint('Welcome aboard,', user_name)",
                    "expected_output": "Welcome aboard, Priyanshu",
                    "explanation_en": "Captures text input and personalizes the greeting.",
                    "explanation_hi": "User ka text lekar personal welcome message deta hai."
                },
                "example_2": {
                    "title": "Typecasting Input to Integer",
                    "title_hi": "Input ko number me convert karna",
                    "code": "age_str = '20'\nage = int(age_str)\nprint('Next year age will be:', age + 1)",
                    "expected_output": "Next year age will be: 21",
                    "explanation_en": "int() turns string '20' into integer 20 so arithmetic works.",
                    "explanation_hi": "int() string '20' ko number 20 banata hai taaki addition kaam kare."
                },
                "challenge": {
                    "prompt_en": "Store a user input variable greeting = 'Hello' and name = 'Alex', then print: Hello, Alex!",
                    "prompt_hi": "greeting = 'Hello' aur name = 'Alex' lekar print karo: Hello, Alex!",
                    "starter_code": "greeting = 'Hello'\nname = 'Alex'\n# Print the combined greeting:\n",
                    "expected_output": "Hello, Alex!",
                    "solution_code": "greeting = 'Hello'\nname = 'Alex'\nprint(f'{greeting}, {name}!')",
                    "solution_explanation_en": "Uses an f-string to combine greeting and name.",
                    "solution_explanation_hi": "f-string se dono variables ko jodkar print karta hai.",
                    "hints": ["Use f'{greeting}, {name}!' or print(greeting + ', ' + name + '!')"],
                    "ego_roast_hi": "User se baat karna nahi seekhe abhi tak?",
                    "ego_cheer_hi": "Interactive coding level unlocked! 🚀"
                }
            },
            {
                "id": "ch2_sub3_comments_docstrings",
                "title": "Adding notes for yourself: Single-line and multi-line comments (# and \"\"\")",
                "title_hi": "Apne liye notes likhna: Comments aur Docstrings (# aur \"\"\")",
                "icon": "📝",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Comments are human notes inside code that Python completely ignores during execution. Single-line comments start with #. Triple quotes (\"\"\"...\"\"\") are multiline string literals often used for documentation.",
                "what_is_it_hi": "Comments wo notes hote hain jo aap apne ya doosre coders ke samajhne ke liye likhte ho, Python interpreter inko bilkul ignore kar deta hai. Single-line ke liye # lagta hai, aur lambi documentation ke liye triple quotes (\"\"\").",
                "why_need_it_en": "Code is read 10 times more often than it is written. 6 months from now, you will forget why you wrote a complex algorithm without comments.",
                "why_need_it_hi": "6 mahine baad apna hi code dekh kar samajh nahi aayega ki kya kiya tha agar comments nahi likhoge.",
                "how_to_use_en": "# Explain WHY, not what. For functions, use triple quotes right under def as docstrings.",
                "how_to_use_hi": "Line ke shuru me # lagao. Yaad rakho: comment me ye likho ki code KYUN likha hai, na ki kya likha hai.",
                "syntax": "# This is a single line comment\n\"\"\"\nThis is a multiline docstring\nused to describe modules or functions.\n\"\"\"",
                "rules_en": [
                    "# ignores everything from the symbol to the end of that specific line.",
                    "Triple-quoted strings (\"\"\" or ''') are technically multiline string literals; when unassigned, Python discards them (acting as multiline comments).",
                    "When placed immediately inside a function or class, triple quotes become official docstrings accessible via __doc__."
                ],
                "rules_hi": [
                    "# ke baad se line ke aakhri tak sab kuch Python ignore karta hai.",
                    "Triple-quoted string jab kisi variable me store nahi hoti, to wo comment ki tarah behave karti hai.",
                    "Function ke andar pehli line par triple quotes official docstring ban jaati hai."
                ],
                "analogy_en": "Comments are like sticky notes left inside a complicated machine manual so the next technician knows which wire was replaced.",
                "analogy_hi": "Comments fridge par lage sticky notes jaise hain — 'Doodh ubaal diya hai, 5 baje chai bana lena'.",
                "common_mistakes": [
                    {
                        "mistake": "Believing triple quotes are dedicated comment syntax keywords in Python.",
                        "why_it_fails_en": "Triple quotes are string literals. If placed where an expression is not allowed or if assigned, they are real objects in memory.",
                        "why_it_fails_hi": "Triple quotes asal me string literals hote hain, Python me koi alag multiline comment keyword nahi hota.",
                        "fix": "Use # on every line for pure comments, and reserve triple quotes for function/module docstrings."
                    }
                ],
                "example_1": {
                    "title": "Clean Single-Line Notes",
                    "title_hi": "Single-line comment ka sahi use",
                    "code": "# Calculate discount rate for holiday sale\nprice = 100\ndiscount = 20  # 20% discount\nprint('Final price:', price - discount)",
                    "expected_output": "Final price: 80",
                    "explanation_en": "Comments clarify the intention of the calculation without affecting output.",
                    "explanation_hi": "Comments calculation ka reason batate hain bina execution ko roke."
                },
                "example_2": {
                    "title": "Docstrings for Explanation",
                    "title_hi": "Docstring se documentation",
                    "code": "\"\"\"\nElysia Code Calculator Engine\nVersion 2.0\n\"\"\"\nprint('Documentation loaded.')",
                    "expected_output": "Documentation loaded.",
                    "explanation_en": "Multiline strings provide clean header documentation.",
                    "explanation_hi": "Multiline string se clean header banaya jata hai."
                },
                "challenge": {
                    "prompt_en": "Write a comment explaining a variable total = 50, then print total.",
                    "prompt_hi": "Ek comment likho aur total = 50 ko print karo.",
                    "starter_code": "# Add your comment and code below:\n",
                    "expected_output": "50",
                    "solution_code": "# Total student count in class\ntotal = 50\nprint(total)",
                    "solution_explanation_en": "The # comment is ignored, and total is printed.",
                    "solution_explanation_hi": "Comment ignore ho jata hai aur 50 print ho jata hai.",
                    "hints": ["Start the comment line with #."],
                    "ego_roast_hi": "Comment likhna bhi bhool gaye?",
                    "ego_cheer_hi": "Code documentation skills on point! 📝"
                }
            },
            {
                "id": "ch2_sub4_escape_characters",
                "title": "Escape characters (\\n, \\t, \\\\)",
                "title_hi": "Escape characters (\\n, \\t, \\\\)",
                "icon": "⚡",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "An escape character is a backslash (\\) followed by a special character. It allows you to insert newlines (\\n), tabs (\\t), quotes inside strings (\\\" or \\'), and literal backslashes (\\\\).",
                "what_is_it_hi": "Escape character backslash (\\) hota hai jo normal letters ko special power deta hai: \\n se nayi line banti hai, \\t se tab space aati hai, aur \\\\ se literal backslash print hota hai.",
                "why_need_it_en": "Without escape characters, you cannot format a multi-line message in a single string or put double quotes inside a double-quoted string.",
                "why_need_it_hi": "Agar escape character na ho to quote ke andar quote likhte hi syntax error aa jayega.",
                "how_to_use_en": "Use \\n for newline, \\t for horizontal tab, \\' for single quote, \\\" for double quote, and \\\\ for backslash.",
                "how_to_use_hi": "\\n se line break karo, \\t se 4-space tab do, \\\" se quote print karo.",
                "syntax": "print(\"Line 1\\nLine 2\\tIndented Tab\\nHe said: \\\"Python!\\\"\")",
                "rules_en": [
                    "\\n = Newline (Enter key equivalent).",
                    "\\t = Horizontal tab (4 spaces gap).",
                    "\\\\ = Literal backslash.",
                    "\\\" = Double quote inside double quotes."
                ],
                "rules_hi": [
                    "\\n = Nayi line par cursor bhejta hai.",
                    "\\t = Tab space (gap) deta hai.",
                    "\\\\ = Asli backslash print karta hai.",
                    "\\\" = Double quote ke andar double quote print karta hai."
                ],
                "analogy_en": "The backslash (\\) is like tapping someone on the shoulder and whispering 'the next letter is a secret code, don't read it literally!'.",
                "analogy_hi": "Backslash (\\) ek secret agent code jaisa hai — agle letter ko normal mat samajhna, wo special command hai!",
                "common_mistakes": [
                    {
                        "mistake": "Using forward slash /n instead of backslash \\n.",
                        "why_it_fails_en": "/n just prints the literal characters '/n' on screen without a newline.",
                        "why_it_fails_hi": "/n likhne se screen par '/n' hi print hoga, nayi line nahi banegi.",
                        "fix": "Always use backslash (\\n), not forward slash (/n)."
                    }
                ],
                "example_1": {
                    "title": "Newline and Tab in Action",
                    "title_hi": "Nayi line aur Tab gap",
                    "code": "print('Item:\\tPrice\\nApple:\\t$2.50\\nMango:\\t$3.00')",
                    "expected_output": "Item:\tPrice\nApple:\t$2.50\nMango:\t$3.00",
                    "explanation_en": "Creates clean column formatting with tabs and breaks lines with \\n.",
                    "explanation_hi": "\\t se columns align hote hain aur \\n se nayi rows banti hain."
                },
                "example_2": {
                    "title": "Escaping Quotes Inside Strings",
                    "title_hi": "Quotes ke andar quotes likhna",
                    "code": "print('She said: \"It\\'s Python time!\"')",
                    "expected_output": "She said: \"It's Python time!\"",
                    "explanation_en": "Uses backslash before single quote to avoid terminating the string early.",
                    "explanation_hi": "Backslash lagane se single quote string ko premature band nahi karta."
                },
                "challenge": {
                    "prompt_en": "Print two lines using a single print statement and \\n: Line One on the first line and Line Two on the second line.",
                    "prompt_hi": "Ek hi print statement aur \\n se do lines print karo: Line One aur agli line par Line Two.",
                    "starter_code": "# Use a single print() with \\n:\n",
                    "expected_output": "Line One\nLine Two",
                    "solution_code": "print('Line One\\nLine Two')",
                    "solution_explanation_en": "print('Line One\\nLine Two') splits the text into two lines.",
                    "solution_explanation_hi": "\\n se text do alag-alag lines me divide ho jata hai.",
                    "hints": ["Put \\n between 'Line One' and 'Line Two'."],
                    "ego_roast_hi": "\\n lagana itna mushkil hai kya?",
                    "ego_cheer_hi": "Formatting masterclass complete! 🎯"
                }
            },
            {
                "id": "ch2_sub5_mini_project_chatbot",
                "title": "Mini-Project: An Interactive Welcome Chatbot",
                "title_hi": "Mini-Project: Ek Interactive Welcome Chatbot",
                "icon": "🤖",
                "is_mini_project": True,
                "duration": "15 mins",
                "xp": 150,
                "what_is_it_en": "A complete, functioning conversational terminal chatbot that greets the user, asks for their name and favorite programming topic, formats the responses with escape characters, and gives an animated ASCII welcome banner.",
                "what_is_it_hi": "Ek complete functioning conversational chatbot jo user ka naam aur favorite topic maangta hai, comments aur escape characters use karta hai, aur ek mast ASCII banner print karta hai.",
                "why_need_it_en": "Mini-projects synthesize all isolated concepts (print, sep, end, comments, input, escape sequences) into a real software product.",
                "why_need_it_hi": "Mini-project se print, input, escape characters sab ek real project me ek sath combine ho jaate hain.",
                "how_to_use_en": "Combine input(), variables, f-strings, \\n, and formatted ASCII borders.",
                "how_to_use_hi": "input(), variables, f-string aur \\n ko ek sath jodkar interactive bot banao.",
                "syntax": "# Interactive Chatbot Flow:\nname = input()\ntopic = input()\nprint(f\"=== WELCOME {name.upper()} ===\\nReady to master {topic}!\")",
                "rules_en": [
                    "Prompt clearly before each input.",
                    "Use f-strings for clean variable embedding.",
                    "Structure with header, body, and farewell sections."
                ],
                "rules_hi": [
                    "Input se pehle clear prompt do.",
                    "f-string use karo taaki code saaf rahe.",
                    "Header aur farewell banner format karo."
                ],
                "analogy_en": "This is like building your very first customer service virtual assistant for an airport desk.",
                "analogy_hi": "Ye airport ke reception desk par khade virtual welcome robot jaisa hai jo har visitor se uska naam poochkar welcome karta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Hardcoding user responses instead of using variables.",
                        "why_it_fails_en": "The chatbot stops being dynamic if user data is ignored.",
                        "why_it_fails_hi": "Agar variable use nahi karoge to bot har user ke liye dynamic nahi rahega.",
                        "fix": "Always bind input to variables and interpolate with f-strings."
                    }
                ],
                "example_1": {
                    "title": "The Welcome Chatbot Engine",
                    "title_hi": "Welcome Chatbot ka pura code",
                    "code": "# ========================================\n# MINI-PROJECT: ELYSIA WELCOME CHATBOT\n# ========================================\nbot_name = 'ElysiaBot'\nuser_name = 'Alex'\ntopic = 'AI & Python'\n\nprint('=' * 30)\nprint(f'🤖 Hello! I am {bot_name}.')\nprint(f'✨ Welcome, {user_name}!')\nprint(f'🎯 Selected Track: {topic}')\nprint('=' * 30)",
                    "expected_output": "==============================\n🤖 Hello! I am ElysiaBot.\n✨ Welcome, Alex!\n🎯 Selected Track: AI & Python\n==============================",
                    "explanation_en": "Combines variables, decorative borders, emojis, and multiline structure.",
                    "explanation_hi": "Variables, borders, emojis aur formatted lines ko combine karke bot banata hai."
                },
                "example_2": {
                    "title": "Chatbot with Formatted Details",
                    "title_hi": "Chatbot details banner",
                    "code": "status = 'Online'\nprint(f'System:\\t{status}\\nLevel:\\tLevel 1 Coder')",
                    "expected_output": "System:\tOnline\nLevel:\tLevel 1 Coder",
                    "explanation_en": "Uses escape characters \\t and \\n inside the bot status display.",
                    "explanation_hi": "Escape characters se bot status display format karta hai."
                },
                "challenge": {
                    "prompt_en": "Build a chatbot greeting banner that prints:\\n=== WELCOME BOT ===\\nHello Alex!\\nReady to code Python!",
                    "prompt_hi": "Chatbot banner print karo jo exact ye output de:\\n=== WELCOME BOT ===\\nHello Alex!\\nReady to code Python!",
                    "starter_code": "# Build your mini-project chatbot banner:\nname = 'Alex'\n# Write your print statements below:\n",
                    "expected_output": "=== WELCOME BOT ===\nHello Alex!\nReady to code Python!",
                    "solution_code": "name = 'Alex'\nprint('=== WELCOME BOT ===')\nprint(f'Hello {name}!')\nprint('Ready to code Python!')",
                    "solution_explanation_en": "Prints the three-line chatbot greeting header and message.",
                    "solution_explanation_hi": "Teen lines me formatted welcome chatbot message print karta hai.",
                    "hints": ["Use 3 print statements or 1 print statement with \\n."],
                    "ego_roast_hi": "Mini-project se darr gaye kya? Bas 3 print statements hain!",
                    "ego_cheer_hi": "BOOM! 💥 MINI-PROJECT 1 COMPLETED! You built a real chatbot! 🏆"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 3: Memory Boxes (Variables)
    # =========================================================================
    {
        "id": "ch3_variables",
        "part_number": 1,
        "part_title": "PART 1: THE ABSOLUTE BASICS (ZERO TO CODE)",
        "chapter_number": 3,
        "title": "Chapter 3: Memory Boxes (Variables)",
        "subtitle_en": "Understand memory allocation, naming rules, reassignments, multiple unpacks, and constants",
        "subtitle_hi": "Memory dabbe, naam ke niyam, multiple assignments aur constants",
        "icon": "📦",
        "estimated_time": "35 mins",
        "prerequisites_en": "Chapters 1 & 2 basics.",
        "prerequisites_hi": "Chapter 1 aur 2 ke basics.",
        "learning_objectives_en": [
            "Master the 'labeled memory box' mental model",
            "Learn valid Python identifier naming rules (and what causes SyntaxError)",
            "Perform value assignment and variable updates",
            "Use multi-variable single-line assignments (x, y = 10, 20)",
            "Adopt Python CONSTANT naming conventions"
        ],
        "learning_objectives_hi": [
            "Variable ka memory box mental model seekho",
            "Variable naming ke strict niyam aur syntax errors",
            "Value update karna aur reassign karna",
            "Ek line me multiple variables assign karna (x, y = 10, 20)",
            "Python me constants ke uppercase conventions"
        ],
        "recap_en": "You mastered variables as memory tags, naming constraints, reassignments, tuple unpacking in assignment, and uppercase constant conventions.",
        "recap_hi": "Aapne memory allocation, variable naming rules, multiple assignment aur constants ke niyam seekhe.",
        "subtopics": [
            {
                "id": "ch3_sub1_what_is_variable",
                "title": "What is a variable? (The \"labeled box\" concept)",
                "title_hi": "Variable kya hota hai? (\"Labeled Box\" Concept)",
                "icon": "🏷️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A variable is a labeled name that points to a value stored in your computer's RAM memory. You store data in it once, and refer to it by name anywhere in your program.",
                "what_is_it_hi": "Variable ek labeled dabba ya tag hai jo computer ki RAM memory me rakhi kisi value ki taraf point karta hai. Ek baar data daalo, fir naam se use access karo.",
                "why_need_it_en": "Without variables, you would have to retype hardcoded values hundreds of times. If a price or tax rate changes, you would have to manually edit hundreds of lines.",
                "why_need_it_hi": "Bina variable ke har jagah same number baar baar likhna padega. Agar tax rate change hua to 100 jagah manual change karna padega.",
                "how_to_use_en": "Use the assignment operator (=): variable_name = value.",
                "how_to_use_hi": "Single equal sign (=) se value store karo: score = 100.",
                "syntax": "box_name = value_to_store",
                "rules_en": [
                    "Single equal (=) is assignment, NOT mathematical equality (which is ==).",
                    "The right side is evaluated first, then stored into the left-side name.",
                    "Python variables don't require type declarations (like 'int x' in C++)."
                ],
                "rules_hi": [
                    "Single equal (=) value assign karta hai, compare karne ke liye double equal (==) lagta hai.",
                    "Right side pehle calculate hoti hai, fir left side ke dabbe me save hoti hai.",
                    "Python me int, float pehle se likhne ki zarurat nahi hoti."
                ],
                "analogy_en": "Think of a kitchen jar labeled 'Sugar'. You don't eat the label; you open the jar to get the sugar inside. The label is the variable name; the sugar is the data.",
                "analogy_hi": "Kitchen me rakha dabba jispe sticker laga hai 'Chai Patti'. Sticker variable ka naam hai, aur andar rakhi patti actual data hai!",
                "common_mistakes": [
                    {
                        "mistake": "Writing 100 = score (putting value on the left).",
                        "why_it_fails_en": "SyntaxError: cannot assign to literal. The variable name MUST be on the left.",
                        "why_it_fails_hi": "Value hamesha right me hoti hai aur variable name hamesha left me.",
                        "fix": "Always write: score = 100."
                    }
                ],
                "example_1": {
                    "title": "Creating and Reading Variables",
                    "title_hi": "Variable banana aur use karna",
                    "code": "student_name = 'Aman'\nprint('Enrolled student:', student_name)",
                    "expected_output": "Enrolled student: Aman",
                    "explanation_en": "Assigns 'Aman' to student_name and references it inside print.",
                    "explanation_hi": "'Aman' ko variable me save karta hai aur print me use karta hai."
                },
                "example_2": {
                    "title": "Numeric Variables in Calculations",
                    "title_hi": "Numbers ko variable me rakh kar math karna",
                    "code": "price = 250\nqty = 3\ntotal = price * qty\nprint('Total Bill: $', total, sep='')",
                    "expected_output": "Total Bill: $750",
                    "explanation_en": "Multiplies two variables and stores the product in a third variable.",
                    "explanation_hi": "Do variables ko multiply karke teesre variable me store karta hai."
                },
                "challenge": {
                    "prompt_en": "Create a variable named user_score with value 95 and print: Score: 95",
                    "prompt_hi": "user_score = 95 banao aur print karo: Score: 95",
                    "starter_code": "# Create variable and print:\n",
                    "expected_output": "Score: 95",
                    "solution_code": "user_score = 95\nprint(f'Score: {user_score}')",
                    "solution_explanation_en": "Assigns 95 to user_score and prints with an f-string.",
                    "solution_explanation_hi": "user_score variable me 95 rakh kar print karta hai.",
                    "hints": ["Use user_score = 95 and print(f'Score: {user_score}')"],
                    "ego_roast_hi": "Dabbe me value rakhna nahi aa raha?",
                    "ego_cheer_hi": "Memory box created successfully! 📦"
                }
            },
            {
                "id": "ch3_sub2_naming_rules",
                "title": "Rules for naming variables (what is allowed and what causes errors)",
                "title_hi": "Variable naming ke niyam (kya allowed hai aur kya error deta hai)",
                "icon": "⚖️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Python has strict legal rules for identifiers: variable names can contain letters (a-z, A-Z), digits (0-9), and underscores (_), but can NEVER start with a digit, contain spaces, or use reserved keywords (like if, for, class).",
                "what_is_it_hi": "Variable ke naam me letters, numbers aur underscore (_) aa sakte hain, lekin naam NUMBER se shuru nahi ho sakta, beech me SPACE nahi ho sakta, aur Python keywords (if, while, class) use nahi ho sakte.",
                "why_need_it_en": "The Python parser needs to unambiguously distinguish variable names from numbers, operators, and language keywords.",
                "why_need_it_hi": "Agar variable ka naam 123_abc hoga to computer confuse ho jayega ki ye number hai ya variable.",
                "how_to_use_en": "Use snake_case for variables (e.g., student_roll_number, total_cart_price).",
                "how_to_use_hi": "snake_case use karo: chhote letters aur shabdon ke beech underscore (total_bill, user_age).",
                "syntax": "# VALID:\nuser_name = \"Alex\"\n_private_key = 1234\nuser_2 = \"Sara\"\n\n# INVALID (SyntaxError):\n# 2user = \"Sara\"   (Starts with digit)\n# user name = \"Alex\" (Contains space)\n# class = \"CSE\"      (Reserved keyword)",
                "rules_en": [
                    "Must start with a letter (a-z, A-Z) or an underscore (_).",
                    "Cannot start with a number (e.g. 1st_place is illegal).",
                    "Cannot contain spaces or special characters (!, @, #, $, %, etc.).",
                    "Cannot use Python 35 reserved keywords (if, def, return, while, etc.).",
                    "Case-sensitive: age, Age, and AGE are three completely distinct variables."
                ],
                "rules_hi": [
                    "Hamesha letter ya underscore (_) se shuru hona chahiye.",
                    "Number se shuru nahi ho sakta (1st_student galat hai).",
                    "Space ya special characters (@, #, $) strictly mana hain.",
                    "Python ke reserved keywords (if, else, for) use nahi kar sakte.",
                    "Case-sensitive: age aur Age do alag-alag variables hain."
                ],
                "analogy_en": "Just like a government passport or roll number cannot have smiley emojis or spaces, a variable name must follow strict legal identity formats.",
                "analogy_hi": "Jaise bank account number ya roll number me emoji ya space nahi daal sakte, waise hi variable name ke strict rules hote hain.",
                "common_mistakes": [
                    {
                        "mistake": "Naming a variable with a space: first name = 'Aman'",
                        "why_it_fails_en": "SyntaxError: invalid syntax because the parser sees two consecutive identifiers.",
                        "why_it_fails_hi": "Space aate hi Python do alag shabd samajhta hai aur crash ho jata hai.",
                        "fix": "Use an underscore: first_name = 'Aman'."
                    }
                ],
                "example_1": {
                    "title": "Valid Snake Case Identifiers",
                    "title_hi": "Sahi snake_case variable names",
                    "code": "first_name = 'Rohan'\nlast_name = 'Sharma'\nuser_roll_no = 101\nprint(first_name, last_name, f'(Roll: {user_roll_no})')",
                    "expected_output": "Rohan Sharma (Roll: 101)",
                    "explanation_en": "Follows standard PEP 8 naming conventions with underscores.",
                    "explanation_hi": "Underscore ke sath standard snake_case naming use karta hai."
                },
                "example_2": {
                    "title": "Demonstrating Case Sensitivity",
                    "title_hi": "Case sensitivity ka saboot",
                    "code": "speed = 50\nSpeed = 100\nprint('speed:', speed, 'vs Speed:', Speed)",
                    "expected_output": "speed: 50 vs Speed: 100",
                    "explanation_en": "speed and Speed hold different memory locations and values.",
                    "explanation_hi": "speed aur Speed do alag dabbe hain, dono ki values alag rehti hain."
                },
                "challenge": {
                    "prompt_en": "Declare a valid variable valid_variable_name with value 'Rules Followed' and print it.",
                    "prompt_hi": "valid_variable_name = 'Rules Followed' banao aur print karo.",
                    "starter_code": "# Declare variable and print:\n",
                    "expected_output": "Rules Followed",
                    "solution_code": "valid_variable_name = 'Rules Followed'\nprint(valid_variable_name)",
                    "solution_explanation_en": "Valid snake_case variable name printed directly.",
                    "solution_explanation_hi": "Sahi variable name ko print karta hai.",
                    "hints": ["valid_variable_name = 'Rules Followed'"],
                    "ego_roast_hi": "Naming rules me hi phas gaye?",
                    "ego_cheer_hi": "Legal Python identifier verified! ⚖️"
                }
            },
            {
                "id": "ch3_sub3_assign_update",
                "title": "Assigning and updating values",
                "title_hi": "Values assign aur update karna",
                "icon": "🔄",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Variables are dynamic and mutable in their bindings: you can overwrite their value at any time. Updating often uses previous values (e.g. count = count + 1).",
                "what_is_it_hi": "Variable me rakhi value ko kabhi bhi badla ja sakta hai. Nayi value daalte hi purani value memory se hat jaati hai.",
                "why_need_it_en": "Game scores increase, bank balances deduct, and counters increment as an application runs.",
                "why_need_it_hi": "Game me score badhta hai, cart me items add hote hain — in sabke liye variable ki value update karni padti hai.",
                "how_to_use_en": "score = 10; score = score + 5 (or using shortcut score += 5).",
                "how_to_use_hi": "score = 10; score = score + 5 ya shortcut score += 5 use karo.",
                "syntax": "# Full form:\ncount = count + 1\n# Shorthand (Augmented assignment):\ncount += 1",
                "rules_en": [
                    "You cannot update a variable that hasn't been defined yet (results in NameError).",
                    "The right-hand side is evaluated completely using the CURRENT value before reassigning.",
                    "Reassigning to a different type is valid in Python (e.g. x = 5 then x = 'hello')."
                ],
                "rules_hi": [
                    "Jo variable pehle se exist nahi karta use direct update nahi kar sakte (NameError aayega).",
                    "Right side pehle purani value se solve hoti hai, fir naya result dabba me jaata hai.",
                    "Python me pehle number tha, baad me text daal diya — ye bhi allowed hai."
                ],
                "analogy_en": "Imagine a whiteboard where you erase 'Level 1' and write 'Level 2'. The whiteboard is the same; the content on it changed.",
                "analogy_hi": "Blackboard par purana score duster se mita kar naya score likhne jaisa hai.",
                "common_mistakes": [
                    {
                        "mistake": "Updating an undefined variable: balance += 50 before setting balance = 0.",
                        "why_it_fails_en": "NameError: name 'balance' is not defined. It needs an initial starting value.",
                        "why_it_fails_hi": "Python ko pata hi nahi ki balance shuru kahan se hua tha.",
                        "fix": "Always initialize your variables first: balance = 0; balance += 50."
                    }
                ],
                "example_1": {
                    "title": "Tracking a Game Score Update",
                    "title_hi": "Game score badhana",
                    "code": "score = 0\nprint('Start score:', score)\nscore = score + 10\nprint('After coin pickup:', score)",
                    "expected_output": "Start score: 0\nAfter coin pickup: 10",
                    "explanation_en": "Initializes score at 0, then increments it by 10.",
                    "explanation_hi": "Score pehle 0 tha, coin milte hi 10 badh gaya."
                },
                "example_2": {
                    "title": "Shorthand Augmented Assignment",
                    "title_hi": "Shortcut operators (+=, -=)",
                    "code": "health = 100\nhealth -= 25  # Took damage\nprint('Remaining health:', health)",
                    "expected_output": "Remaining health: 75",
                    "explanation_en": "health -= 25 subtracts 25 from health in-place.",
                    "explanation_hi": "health -= 25 se health 100 me se 25 kam hokar 75 ho gayi."
                },
                "challenge": {
                    "prompt_en": "Initialize counter = 10, add 5 to it, and print: Counter: 15",
                    "prompt_hi": "counter = 10 banao, usme 5 jodo, aur print karo: Counter: 15",
                    "starter_code": "# Initialize, update, and print:\n",
                    "expected_output": "Counter: 15",
                    "solution_code": "counter = 10\ncounter += 5\nprint(f'Counter: {counter}')",
                    "solution_explanation_en": "Adds 5 to counter and prints the result.",
                    "solution_explanation_hi": "counter me 5 add karke print karta hai.",
                    "hints": ["counter = 10 then counter += 5"],
                    "ego_roast_hi": "10 + 5 update karna nahi aa raha?",
                    "ego_cheer_hi": "Variable state update successful! 🔄"
                }
            },
            {
                "id": "ch3_sub4_multiple_assignments",
                "title": "Multiple assignments in a single line (x, y = 10, 20)",
                "title_hi": "Ek line me multiple assignments (x, y = 10, 20)",
                "icon": "⚡",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Python allows you to assign values to multiple variables simultaneously in one clean line using comma separation (tuple unpacking). You can also chain-assign identical values: a = b = c = 0.",
                "what_is_it_hi": "Python me ek hi line me comma laga kar multiple variables ko values di ja sakti hain: x, y = 10, 20. Ya sabko same value deni ho to: a = b = c = 0.",
                "why_need_it_en": "It enables Python's famous 1-line variable swap: 'x, y = y, x' without needing a temporary third variable!",
                "why_need_it_hi": "Isse Python ka famous 1-line swap hota hai: do variables ki values aapas me badalna (x, y = y, x) bina kisi teesre temporary variable ke!",
                "how_to_use_en": "x, y, z = 1, 2, 3 (number of variables on left must match number of values on right).",
                "how_to_use_hi": "x, y = 10, 20. Left me jitne variables hain, right me utni hi values honi chahiye.",
                "syntax": "# Parallel assignment:\nx, y = 10, 20\n# Swapping without temp variable:\nx, y = y, x\n# Chained assignment:\na = b = c = 0",
                "rules_en": [
                    "The number of variables on the left MUST match the number of values on the right, or ValueError: not enough values to unpack occurs.",
                    "Values on the right are bundled as a tuple before unpacking.",
                    "Allows atomic swapping: x, y = y, x."
                ],
                "rules_hi": [
                    "Left side aur right side ke items ki ginti barabar honi chahiye, warna ValueError aayega.",
                    "Python right side ko pehle evaluate karta hai fir simultaneously assign karta hai.",
                    "Swapping ke liye C/C++ jaisa temp variable nahi chahiye hota."
                ],
                "analogy_en": "Like a referee handing red and blue jerseys simultaneously to two team captains in one motion.",
                "analogy_hi": "Ek hath me do toffees hain aur aap ek sath dono doston ko ek-ek toffee pakda dete ho.",
                "common_mistakes": [
                    {
                        "mistake": "Unmatched counts: x, y = 1, 2, 3",
                        "why_it_fails_en": "ValueError: too many values to unpack (expected 2, got 3).",
                        "why_it_fails_hi": "Left me 2 dabbe hain aur right me 3 values, fit kaise hongi?",
                        "fix": "Ensure exact count match on both sides."
                    }
                ],
                "example_1": {
                    "title": "Assigning Coordinates in One Line",
                    "title_hi": "X aur Y coordinates ek line me",
                    "code": "x, y = 100, 250\nprint(f'Player Position -> X: {x}, Y: {y}')",
                    "expected_output": "Player Position -> X: 100, Y: 250",
                    "explanation_en": "Assigns 100 to x and 250 to y simultaneously.",
                    "explanation_hi": "x ko 100 aur y ko 250 ek sath assign karta hai."
                },
                "example_2": {
                    "title": "The Magic Variable Swap",
                    "title_hi": "Values ka aapas me swapping",
                    "code": "a, b = 'Water', 'Milk'\na, b = b, a  # Swapped!\nprint(f'a is now {a}, b is now {b}')",
                    "expected_output": "a is now Milk, b is now Water",
                    "explanation_en": "Swaps a and b in 1 elegant line with zero temporary variables.",
                    "explanation_hi": "Bina kisi teesre variable ke ek line me values swap kar deta hai."
                },
                "challenge": {
                    "prompt_en": "Assign width, height = 50, 20 in one line and print: Area: 1000",
                    "prompt_hi": "Ek line me width, height = 50, 20 assign karo aur print karo: Area: 1000",
                    "starter_code": "# Single line assignment and area calculation:\n",
                    "expected_output": "Area: 1000",
                    "solution_code": "width, height = 50, 20\nprint(f'Area: {width * height}')",
                    "solution_explanation_en": "Unpacks 50 and 20 into width and height, then calculates and prints area.",
                    "solution_explanation_hi": "width aur height ko unpack karke area print karta hai.",
                    "hints": ["width, height = 50, 20 then print(f'Area: {width * height}')"],
                    "ego_roast_hi": "Ek line me do variables assign karna nahi aaya?",
                    "ego_cheer_hi": "Unpacking power unlocked! ⚡"
                }
            },
            {
                "id": "ch3_sub5_constants",
                "title": "Constants in Python (Naming conventions)",
                "title_hi": "Python me Constants (Naming conventions)",
                "icon": "🔒",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A constant is a value meant to never change during the program's lifecycle (like PI = 3.14159 or MAX_CONNECTIONS = 100). Python does not have a 'const' keyword; instead, developers use ALL_CAPITAL_LETTERS by convention to signal 'DO NOT MODIFY'.",
                "what_is_it_hi": "Constant wo value hoti hai jo program chalte waqt kabhi badalni nahi chahiye (jaise PI = 3.14 ya MAX_USERS = 500). Python me 'const' keyword nahi hota, isliye developers convention ke mutabiq CAPITAL LETTERS me likhte hain taaki sabko pata rahe ki isko change nahi karna.",
                "why_need_it_en": "It prevents accidental bugs where another developer or function overwrites critical configuration values like database ports or math constants.",
                "why_need_it_hi": "Ye doosre developers ko galti se sensitive configuration (jaise port ya secret key) change karne se rokt hai.",
                "how_to_use_en": "Write identifiers in UPPERCASE_WITH_UNDERSCORES at the top of your file.",
                "how_to_use_hi": "File ke top par CAPITAL LETTERS aur underscore me constants declare karo.",
                "syntax": "# Constants convention:\nPI = 3.14159\nMAX_USERS = 1000\nDATABASE_URL = \"localhost:5432\"",
                "rules_en": [
                    "Python does NOT enforce constant immutability at the compiler level — it is an honor-system convention.",
                    "Naming convention: SCREAMING_SNAKE_CASE (all capital letters separated by underscores).",
                    "Place constants at the top of the module after imports."
                ],
                "rules_hi": [
                    "Python technically constant ko lock nahi karta — ye coders ke beech ka agreement hai.",
                    "Capital letters me likhna mandatory convention hai (SCREAMING_SNAKE_CASE).",
                    "Constants ko hamesha file ke shuru me likha jata hai."
                ],
                "analogy_en": "Like a red danger sign on an electric transformer: anyone CAN touch it physically, but the sign clearly tells you that doing so will blow things up.",
                "analogy_hi": "Red color ke danger board jaisa — haath to koi bhi laga sakta hai, lekin board dekh kar samajh jata hai ki chhoona mana hai!",
                "common_mistakes": [
                    {
                        "mistake": "Thinking Python will throw an error if you reassign an uppercase constant.",
                        "why_it_fails_en": "Python allows PI = 5 without error. The convention exists for human developers and linters, not compiler restrictions.",
                        "why_it_fails_hi": "Python error nahi dega, lekin aisa karna bad programming practice maana jata hai.",
                        "fix": "Treat ALL_CAPS variables as strictly read-only."
                    }
                ],
                "example_1": {
                    "title": "Using Mathematical Constants",
                    "title_hi": "Circle ka area calculate karna PI se",
                    "code": "PI = 3.14159\nradius = 5\narea = PI * (radius ** 2)\nprint('Circle Area:', area)",
                    "expected_output": "Circle Area: 78.53975",
                    "explanation_en": "PI is defined in uppercase and used in geometric formulas.",
                    "explanation_hi": "PI ko uppercase me define karke area nikaalta hai."
                },
                "example_2": {
                    "title": "Application Configuration Constants",
                    "title_hi": "App configuration limits",
                    "code": "MAX_RETRY_ATTEMPTS = 3\nprint('Max allowed retries:', MAX_RETRY_ATTEMPTS)",
                    "expected_output": "Max allowed retries: 3",
                    "explanation_en": "Configuration thresholds are stored as constants.",
                    "explanation_hi": "App limits ko constant ke roop me store karta hai."
                },
                "challenge": {
                    "prompt_en": "Define a constant SPEED_OF_LIGHT = 299792458 and print: c = 299792458 m/s",
                    "prompt_hi": "SPEED_OF_LIGHT = 299792458 define karo aur print karo: c = 299792458 m/s",
                    "starter_code": "# Define constant and print:\n",
                    "expected_output": "c = 299792458 m/s",
                    "solution_code": "SPEED_OF_LIGHT = 299792458\nprint(f'c = {SPEED_OF_LIGHT} m/s')",
                    "solution_explanation_en": "Declares uppercase constant and prints formatted string.",
                    "solution_explanation_hi": "Uppercase constant bana kar print karta hai.",
                    "hints": ["SPEED_OF_LIGHT = 299792458"],
                    "ego_roast_hi": "Constant caps me likhna bhool gaye?",
                    "ego_cheer_hi": "Professional coding convention mastered! 🔒"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 4: What Kind of Data? (Basic Data Types)
    # =========================================================================
    {
        "id": "ch4_data_types",
        "part_number": 1,
        "part_title": "PART 1: THE ABSOLUTE BASICS (ZERO TO CODE)",
        "chapter_number": 4,
        "title": "Chapter 4: What Kind of Data? (Basic Data Types)",
        "subtitle_en": "Integers, floats, strings, booleans, type checking, and explicit type conversion",
        "subtitle_hi": "Numbers, decimals, text, booleans, type() check aur type casting",
        "icon": "🧩",
        "estimated_time": "35 mins",
        "prerequisites_en": "Chapters 1 to 3.",
        "prerequisites_hi": "Chapter 1 se 3 tak.",
        "learning_objectives_en": [
            "Master Python's core primitive types: int, float, str, bool",
            "Use type() to inspect data types dynamically",
            "Understand type casting (int(), float(), str(), bool()) and conversion pitfalls"
        ],
        "learning_objectives_hi": [
            "Python ke core primitive types seekho: int, float, str, bool",
            "type() se kisi bhi value ka type check karna",
            "Type casting karna aur aam galtiyon se bachna"
        ],
        "recap_en": "You learned the distinction between whole numbers (int), decimals (float), text (str), truth values (bool), how to inspect types with type(), and how to safely convert between them.",
        "recap_hi": "Aapne int, float, str, bool ka farak seekha, type() function use kiya, aur type casting master ki.",
        "subtopics": [
            {
                "id": "ch4_sub1_integers",
                "title": "Whole numbers: Integers (int)",
                "title_hi": "Poore numbers: Integers (int)",
                "icon": "🔢",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "An integer (int) is a positive or negative whole number without any decimal point (e.g., 42, -7, 0, 1000000). In Python 3, integers have arbitrary precision (they can grow as big as your RAM memory allows!).",
                "what_is_it_hi": "Integer (int) bina decimal wala poora number hota hai (positive ya negative), jaise 10, -5, 0. Python me integer ki koi size limit nahi hoti jab tak RAM me jagah hai!",
                "why_need_it_en": "Counting items, loop iterations, ages, user IDs, and inventory quantities must be exact whole numbers.",
                "why_need_it_hi": "Items count karna, attendance ginn-na, age ya product ID hamesha whole numbers hote hain.",
                "how_to_use_en": "Just write the number directly without quotes: count = 25. Large numbers can use underscores for readability: one_million = 1_000_000.",
                "how_to_use_hi": "Bina quotes ke seedhe number type karo: count = 25. Badi sankhya me underscore laga sakte ho: 1_000_000.",
                "syntax": "x = 42\nnegative = -15\nbig_num = 1_000_000  # Python ignores underscores in numbers",
                "rules_en": [
                    "No decimal point (42.0 is a float, not an int).",
                    "Do not put commas in numbers (use 1_000_000 instead of 1,000,000).",
                    "Arbitrary precision: Python handles giant numbers (like 2**100) automatically without overflow."
                ],
                "rules_hi": [
                    "Decimal point nahi hona chahiye (42.0 float ban jata hai).",
                    "Numbers ke beech comma mat lagao, underscore laga sakte ho (1_000_000).",
                    "Python me number kabhi overflow nahi hota chahe kitna bhi bada ho."
                ],
                "analogy_en": "Counting people in a room: you can have 5 people or 6 people, but never 5.5 people. Integers are discrete counts.",
                "analogy_hi": "Class me students ki ginti: 30 honge ya 31, kabhi 30.5 student nahi ho sakte. Wahi Integer hai.",
                "common_mistakes": [
                    {
                        "mistake": "Writing numbers with commas: cash = 50,000",
                        "why_it_fails_en": "Python creates a tuple (50, 0) instead of the integer 50000!",
                        "why_it_fails_hi": "Comma lagane se Python use tuple bana deta hai number nahi.",
                        "fix": "Use cash = 50000 or cash = 50_000."
                    }
                ],
                "example_1": {
                    "title": "Integer Arithmetic",
                    "title_hi": "Integers ka jod aur ghatana",
                    "code": "apples = 15\noranges = 25\ntotal_fruits = apples + oranges\nprint('Total fruits in basket:', total_fruits)",
                    "expected_output": "Total fruits in basket: 40",
                    "explanation_en": "Adds two integers to produce exact integer sum 40.",
                    "explanation_hi": "Do integers ko jodkar exact sum deta hai."
                },
                "example_2": {
                    "title": "Massive Integer Handling",
                    "title_hi": "Bade numbers bina overflow ke",
                    "code": "huge_val = 2 ** 30\nprint('2 to the power 30 =', huge_val)",
                    "expected_output": "2 to the power 30 = 1073741824",
                    "explanation_en": "Computes giant numbers without manual buffer allocation.",
                    "explanation_hi": "Bina kisi overflow ke huge numbers handle karta hai."
                },
                "challenge": {
                    "prompt_en": "Store population = 1_500_000 and print: Population: 1500000",
                    "prompt_hi": "population = 1_500_000 store karo aur print karo: Population: 1500000",
                    "starter_code": "# Store integer and print:\n",
                    "expected_output": "Population: 1500000",
                    "solution_code": "population = 1_500_000\nprint(f'Population: {population}')",
                    "solution_explanation_en": "Demonstrates integer underscore syntax.",
                    "solution_explanation_hi": "Integer underscore format ka demo.",
                    "hints": ["population = 1_500_000"],
                    "ego_roast_hi": "Integer likhna bhool gaye?",
                    "ego_cheer_hi": "Integer precision validated! 🔢"
                }
            },
            {
                "id": "ch4_sub2_floats",
                "title": "Decimal numbers: Floats (float)",
                "title_hi": "Decimal numbers: Floats (float)",
                "icon": "🪙",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A float (floating-point number) represents real numbers with a fractional decimal point (e.g. 3.14, -0.005, 99.99, 2.0). They are implemented using IEEE 754 double precision in computer memory.",
                "what_is_it_hi": "Float (floating-point number) decimal wale numbers hote hain jaise 3.14, 99.99, 0.5. Agar kisi number me dot (.) lag gaya to wo float ban jata hai.",
                "why_need_it_en": "Prices ($19.99), GPS coordinates (28.7041), temperatures (98.6°F), and scientific measurements require continuous decimal precision.",
                "why_need_it_hi": "Prices, petrol ka rate, CGPA, temperature aur GPS coordinates me decimals zaroori hote hain.",
                "how_to_use_en": "Include a decimal point: gpa = 9.4 or scientific notation: speed = 3e8.",
                "how_to_use_hi": "Dot (.) lagao: price = 49.99 ya scientific e notation: 3e8.",
                "syntax": "pi = 3.14159\ntemp = -4.5\nscientific = 1.5e3  # 1500.0",
                "rules_en": [
                    "Any number containing a decimal point is a float (e.g. 5.0 is float, 5 is int).",
                    "Dividing with / ALWAYS produces a float in Python 3 (e.g., 4 / 2 -> 2.0).",
                    "Floating-point arithmetic has slight binary rounding limits (e.g. 0.1 + 0.2 is 0.30000000000000004)."
                ],
                "rules_hi": [
                    "Agar dot (.) hai to wo float hai (5.0 float hai, 5 int hai).",
                    "Single slash (/) se divide karne par Python 3 me HAMESHA float result milta hai (4 / 2 = 2.0).",
                    "Computer binary me float calculate karta hai isliye 0.1 + 0.2 me thoda rounding difference ho sakta hai."
                ],
                "analogy_en": "An integer is counting rupee coins. A float is measuring water in a beaker with millimeter markings.",
                "analogy_hi": "Integer sikke ginn-ne jaisa hai. Float doodh ya paani naapne jaisa hai (1.5 liter).",
                "common_mistakes": [
                    {
                        "mistake": "Expecting exact equality with floats: if (0.1 + 0.2) == 0.3",
                        "why_it_fails_en": "IEEE 754 floating point representation has tiny rounding errors.",
                        "why_it_fails_hi": "0.1 + 0.2 ka result 0.30000000000000004 hota hai, isliye direct == fail ho sakta hai.",
                        "fix": "Use round(val, 2) or math.isclose(a, b) for financial/scientific checks."
                    }
                ],
                "example_1": {
                    "title": "Division Always Produces Floats",
                    "title_hi": "Division se hamesha float banta hai",
                    "code": "result = 10 / 2\nprint('10 / 2 =', result, 'Type:', type(result).__name__)",
                    "expected_output": "10 / 2 = 5.0 Type: float",
                    "explanation_en": "Standard division / returns 5.0 (float) even when numbers divide evenly.",
                    "explanation_hi": "Poora divide hone par bhi / operator float (5.0) hi deta hai."
                },
                "example_2": {
                    "title": "Rounding Floating-Point Values",
                    "title_hi": "Float values ko round karna",
                    "code": "raw_tax = 14.8567\nclean_tax = round(raw_tax, 2)\nprint('Rounded Tax: $', clean_tax, sep='')",
                    "expected_output": "Rounded Tax: $14.86",
                    "explanation_en": "round() trims to 2 decimal places cleanly.",
                    "explanation_hi": "round() decimal ke baad sirf 2 digits rakhta hai."
                },
                "challenge": {
                    "prompt_en": "Store gpa = 8.75 and print: Student CGPA: 8.75",
                    "prompt_hi": "gpa = 8.75 store karo aur print karo: Student CGPA: 8.75",
                    "starter_code": "# Store float and print:\n",
                    "expected_output": "Student CGPA: 8.75",
                    "solution_code": "gpa = 8.75\nprint(f'Student CGPA: {gpa}')",
                    "solution_explanation_en": "Assigns and prints a floating-point value.",
                    "solution_explanation_hi": "Float value assign karke print karta hai.",
                    "hints": ["gpa = 8.75"],
                    "ego_roast_hi": "CGPA print karne me bhi galti?",
                    "ego_cheer_hi": "Float accuracy nailed! 🪙"
                }
            },
            {
                "id": "ch4_sub3_strings",
                "title": "Text: Strings (str)",
                "title_hi": "Text: Strings (str)",
                "icon": "📜",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A string (str) is an ordered sequence of Unicode characters enclosed in quotes. Strings are IMMUTABLE in Python: once created, individual characters cannot be changed in-place.",
                "what_is_it_hi": "String (str) quotes me likha gaya text hota hai. Python me strings IMMUTABLE (nachange hone wali) hoti hain — ek baar ban gayi to uske andar ka character directly modify nahi kar sakte.",
                "why_need_it_en": "User names, email addresses, blog posts, HTML code, URLs, and JSON data are all strings.",
                "why_need_it_hi": "Naam, email, address, message aur web URL sab kuch strings hi hote hain.",
                "how_to_use_en": "Wrap in single ('...'), double (\"...\"), or triple quotes (\"\"\"...\"\"\"). Use f-strings for variable interpolation: f'Hello, {name}'.",
                "how_to_use_hi": "Quotes lagao: 'text' ya \"text\". Variables jodne ke liye f-string use karo: f'Hi {name}'.",
                "syntax": "greeting = \"Hello, Python!\"\nmultiline = \"\"\"Line 1\nLine 2\"\"\"\nf_string = f\"Interpolated: {greeting}\"",
                "rules_en": [
                    "CRITICAL LAW: Strings are immutable. msg[0] = 'H' throws TypeError: 'str' object does not support item assignment.",
                    "Strings support indexing: msg[0] gives the first character, msg[-1] gives the last.",
                    "f-strings (f'...') are the fastest and most readable way to format strings in modern Python (3.6+)."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: String immutable hoti hai. msg[0] = 'X' likhne par crash ho jayega.",
                    "String me indexing hoti hai: msg[0] pehla letter, msg[-1] aakhri letter deta hai.",
                    "Modern Python me f-strings f'{var}' sabse fast aur readable tareeqa hai."
                ],
                "analogy_en": "A string is like a printed newspaper article. You cannot erase letter #5 with your finger; to change it, you must print a whole new revised edition.",
                "analogy_hi": "String chhape hue akhbar jaisi hai. Ek letter mita nahi sakte; change karna hai to naya akhbar chhapna padega.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to modify a string character in-place: s = 'cat'; s[0] = 'b'",
                        "why_it_fails_en": "TypeError: 'str' object does not support item assignment.",
                        "why_it_fails_hi": "String immutable hai, direct character change nahi hota.",
                        "fix": "Create a new string: s = 'b' + s[1:] or s = s.replace('c', 'b')."
                    }
                ],
                "example_1": {
                    "title": "String Methods and Case Conversion",
                    "title_hi": "String methods (upper, lower)",
                    "code": "raw_name = 'alex smith'\nprint('Uppercase:', raw_name.upper())\nprint('Titlecase:', raw_name.title())",
                    "expected_output": "Uppercase: ALEX SMITH\nTitlecase: Alex Smith",
                    "explanation_en": "Methods return new modified string instances without mutating the original.",
                    "explanation_hi": "Methods naya string return karte hain, original ko mutate nahi karte."
                },
                "example_2": {
                    "title": "Modern f-String Interpolation",
                    "title_hi": "f-string se formatting",
                    "code": "product = 'Laptop'\nprice = 999.5\nprint(f'Item: {product} | Cost: ${price:.2f}')",
                    "expected_output": "Item: Laptop | Cost: $999.50",
                    "explanation_en": "f'{price:.2f}' formats to 2 decimal places inline.",
                    "explanation_hi": "f-string me :.2f lagane se do decimal places tak format hota hai."
                },
                "challenge": {
                    "prompt_en": "Create course = 'Python 101' and print: Enrolled in: PYTHON 101 using .upper().",
                    "prompt_hi": "course = 'Python 101' banao aur .upper() use karke print karo: Enrolled in: PYTHON 101",
                    "starter_code": "# Use upper() and print:\n",
                    "expected_output": "Enrolled in: PYTHON 101",
                    "solution_code": "course = 'Python 101'\nprint(f'Enrolled in: {course.upper()}')",
                    "solution_explanation_en": "Calls .upper() inside an f-string.",
                    "solution_explanation_hi": "f-string ke andar .upper() call karta hai.",
                    "hints": ["print(f'Enrolled in: {course.upper()}')"],
                    "ego_roast_hi": "String methods bhool gaye?",
                    "ego_cheer_hi": "String manipulation pro! 📜"
                }
            },
            {
                "id": "ch4_sub4_booleans",
                "title": "True or False: Booleans (bool)",
                "title_hi": "True ya False: Booleans (bool)",
                "icon": "⚖️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A boolean (bool) represents one of two logical states: True or False. Named after British mathematician George Boole, they are the foundation of all computer decision-making.",
                "what_is_it_hi": "Boolean (bool) sirf do states represent karta hai: True ya False. Iska naam George Boole ke naam par rakha gaya hai. Computer ke har decision ka base yahi hota hai.",
                "why_need_it_en": "Conditionals (if/else) depend entirely on boolean values: Is user logged in? Is payment verified? Is life remaining > 0?",
                "why_need_it_hi": "if/else conditions isi par chalti hain: Kya password sahi hai (True/False)? Kya student pass hua?",
                "how_to_use_en": "Use capitalized True or False, or results of comparisons: is_active = (score > 50).",
                "how_to_use_hi": "Bada T (True) aur bada F (False) likho, ya comparisons se evaluate karo.",
                "syntax": "is_logged_in = True\nis_game_over = False\nis_adult = age >= 18",
                "rules_en": [
                    "Capitalization is MANDATORY: True and False. (Writing true or false causes NameError).",
                    "Booleans are internally a subclass of int: True == 1 and False == 0.",
                    "In Python, empty structures (0, '', [], {}, None) evaluate to False (Falsy)."
                ],
                "rules_hi": [
                    "T aur F CAPITAL hona mandatory hai: True aur False. Chhota true likhoge to crash karega.",
                    "Python me True ki internal value 1 aur False ki 0 hoti hai.",
                    "Khali cheezein (0, '', [], None) False maani jaati hain."
                ],
                "analogy_en": "A light switch on the wall: it can only be ON (True) or OFF (False). There is no in-between state.",
                "analogy_hi": "Kamre ka bijli ka switch: ya to ON (True) hoga ya OFF (False). Teesra koi option nahi hota.",
                "common_mistakes": [
                    {
                        "mistake": "Writing lowercase true or false: is_valid = true",
                        "why_it_fails_en": "NameError: name 'true' is not defined. Other languages use lowercase, but Python requires Capital True/False.",
                        "why_it_fails_hi": "JavaScript ya C++ me chhota true hota hai, lekin Python me Capital T (True) zaroori hai.",
                        "fix": "Always use Capitalized True and False."
                    }
                ],
                "example_1": {
                    "title": "Comparison Generating Booleans",
                    "title_hi": "Comparison se Boolean banna",
                    "code": "age = 20\nis_eligible = age >= 18\nprint('Eligible to vote:', is_eligible)",
                    "expected_output": "Eligible to vote: True",
                    "explanation_en": "age >= 18 evaluates to boolean True.",
                    "explanation_hi": "20 >= 18 compare hoke True ban jata hai."
                },
                "example_2": {
                    "title": "Booleans as Numeric Subclasses",
                    "title_hi": "Boolean ki internal number value",
                    "code": "print('True + True =', True + True)\nprint('False * 5 =', False * 5)",
                    "expected_output": "True + True = 2\nFalse * 5 = 0",
                    "explanation_en": "True acts as 1 and False acts as 0 in arithmetic.",
                    "explanation_hi": "True 1 aur False 0 ki tarah behave karta hai."
                },
                "challenge": {
                    "prompt_en": "Store is_python_fun = True and print: Python is fun: True",
                    "prompt_hi": "is_python_fun = True store karo aur print karo: Python is fun: True",
                    "starter_code": "# Store boolean and print:\n",
                    "expected_output": "Python is fun: True",
                    "solution_code": "is_python_fun = True\nprint(f'Python is fun: {is_python_fun}')",
                    "solution_explanation_en": "Prints boolean state.",
                    "solution_explanation_hi": "Boolean state print karta hai.",
                    "hints": ["is_python_fun = True"],
                    "ego_roast_hi": "True ko chhota 'true' to nahi likh diya?",
                    "ego_cheer_hi": "Boolean logic mastered! ⚖️"
                }
            },
            {
                "id": "ch4_sub5_type_checking",
                "title": "Checking the type of data using type()",
                "title_hi": "Data ka type check karna type() se",
                "icon": "🔍",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The built-in type() function inspects any variable or value at runtime and tells you its exact underlying data class (<class 'int'>, <class 'str'>, etc.).",
                "what_is_it_hi": "built-in type() function kisi bhi variable ya value ka exact type batata hai ki wo int hai, float hai, str hai ya bool.",
                "why_need_it_en": "When debugging strange crashes (like 5 + '5'), type() instantly reveals whether a variable is a number or text.",
                "why_need_it_hi": "Debugging ke waqt jab code crash hota hai to type() se 1 second me pata chal jata hai ki number aya ya text.",
                "how_to_use_en": "Pass the variable into type(): print(type(my_var)). To check programmatically, use isinstance(val, int).",
                "how_to_use_hi": "Variable ko type() ke andar pass karo: print(type(x)). Code me check karne ke liye isinstance() use hota hai.",
                "syntax": "print(type(42))         # <class 'int'>\nprint(type(\"Alex\"))     # <class 'str'>\nprint(type(3.14))       # <class 'float'>\nprint(type(True))       # <class 'bool'>",
                "rules_en": [
                    "type(x) returns the type object of x.",
                    "isinstance(x, int) is preferred for conditional type checking because it supports inheritance.",
                    "type() works on everything in Python (functions, classes, modules are all objects)."
                ],
                "rules_hi": [
                    "type(x) batata hai ki x kis class ka hai.",
                    "Production code me type check karne ke liye isinstance(x, int) best practice hai.",
                    "Python me har cheez ek object hai, sabka type check ho sakta hai."
                ],
                "analogy_en": "Like an x-ray scanner at an airport checking whether a closed suitcase contains clothes, metal, or liquid.",
                "analogy_hi": "Airport ke X-ray scanner jaisa — bag ke bahar se hi bata deta hai ki andar sona hai, kapde hain ya liquid.",
                "common_mistakes": [
                    {
                        "mistake": "Comparing types with strings: if type(x) == 'int'",
                        "why_it_fails_en": "type(x) returns a type object, not the string 'int'.",
                        "why_it_fails_hi": "type(x) type object deta hai string nahi, to 'int' se compare fail hoga.",
                        "fix": "Use if type(x) is int: or if isinstance(x, int):"
                    }
                ],
                "example_1": {
                    "title": "Inspecting Multiple Data Types",
                    "title_hi": "Alag-alag data types ko inspect karna",
                    "code": "val_1 = 100\nval_2 = '100'\nprint('val_1 is:', type(val_1).__name__)\nprint('val_2 is:', type(val_2).__name__)",
                    "expected_output": "val_1 is: int\nval_2 is: str",
                    "explanation_en": "Demonstrates the critical difference between numeric 100 and string '100'.",
                    "explanation_hi": "Dikhata hai ki 100 int hai aur '100' string hai.",
                },
                "example_2": {
                    "title": "Using isinstance() for Validation",
                    "title_hi": "isinstance se clean validation",
                    "code": "score = 95\nprint('Is score an integer?', isinstance(score, int))",
                    "expected_output": "Is score an integer? True",
                    "explanation_en": "isinstance(score, int) returns True.",
                    "explanation_hi": "isinstance() True return karta hai agar type match ho jaye."
                },
                "challenge": {
                    "prompt_en": "Find and print the type name of 45.67 using type(45.67).__name__.",
                    "prompt_hi": "45.67 ka type name print karo: type(45.67).__name__",
                    "starter_code": "# Print type name:\n",
                    "expected_output": "float",
                    "solution_code": "print(type(45.67).__name__)",
                    "solution_explanation_en": "Prints 'float' as the type name.",
                    "solution_explanation_hi": "'float' print karta hai.",
                    "hints": ["print(type(45.67).__name__)"],
                    "ego_roast_hi": "type() use karna nahi aaya?",
                    "ego_cheer_hi": "Type inspection master! 🔍"
                }
            },
            {
                "id": "ch4_sub6_type_casting",
                "title": "Converting one data type to another (Type Casting)",
                "title_hi": "Ek data type ko doosre me badalna (Type Casting)",
                "icon": "🔄",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Type casting (or type conversion) is explicitly transforming a value from one data type to another using constructor functions: int(), float(), str(), and bool().",
                "what_is_it_hi": "Type casting ka matlab hota hai zabardasti ek type ko doosre type me convert karna — jaise text '25' ko number 25 banana (int('25')) ya number ko text banana (str(25)).",
                "why_need_it_en": "Because input() returns a string! If a user types '25', you CANNOT add 5 to it without first typecasting: int('25') + 5 = 30.",
                "why_need_it_hi": "input() hamesha string deta hai. Agar user ne '25' type kiya to bina int() lagaye aap usme 5 add nahi kar sakte.",
                "how_to_use_en": "int('42') -> 42. float('3.14') -> 3.14. str(100) -> '100'. bool(1) -> True.",
                "how_to_use_hi": "int('50'), float('9.5'), str(100), bool(1).",
                "syntax": "num = int(\"50\")\ndecimal = float(\"12.5\")\ntext = str(999)\nflag = bool(1)",
                "rules_en": [
                    "Converting text with invalid characters (e.g. int('hello')) throws ValueError.",
                    "int() on a float truncates towards zero (int(9.99) becomes 9, it does NOT round up!).",
                    "Converting float string directly with int (e.g. int('3.14')) throws ValueError. You must do int(float('3.14'))."
                ],
                "rules_hi": [
                    "Agar text me letters hain (int('abc')) to ValueError aayega.",
                    "int(9.99) decimal hata deta hai aur 9 banta hai (round nahi karta!).",
                    "int('3.14') direct crash hota hai, pehle float('3.14') fir int karna padta hai."
                ],
                "analogy_en": "Like melting gold jewelry into an ingot. The substance is the same, but the physical form (type) changed completely.",
                "analogy_hi": "Barf (ice) ko pighla kar paani banane jaisa — cheez wahi hai, bas form badal gaya.",
                "common_mistakes": [
                    {
                        "mistake": "Calling int('15.5') directly on a decimal string.",
                        "why_it_fails_en": "ValueError: invalid literal for int() with base 10: '15.5'.",
                        "why_it_fails_hi": "int() decimal point wali string ko direct parse nahi kar sakta.",
                        "fix": "Use int(float('15.5')) or just float('15.5')."
                    }
                ],
                "example_1": {
                    "title": "String to Integer Conversion",
                    "title_hi": "String ko Integer me convert karna",
                    "code": "str_val = '50'\nnum_val = int(str_val)\nprint('Sum:', num_val + 25)",
                    "expected_output": "Sum: 75",
                    "explanation_en": "int('50') converts to number 50, allowing mathematical addition.",
                    "explanation_hi": "int('50') 50 ban gaya aur 25 jud kar 75 ho gaya."
                },
                "example_2": {
                    "title": "Truncation in Float to Int Casting",
                    "title_hi": "Float se int banate waqt truncation",
                    "code": "price = 99.99\nint_price = int(price)\nprint('Original:', price, '| Truncated int:', int_price)",
                    "expected_output": "Original: 99.99 | Truncated int: 99",
                    "explanation_en": "int() chops off the decimal part entirely without rounding.",
                    "explanation_hi": "int() decimal ke baad ka hissa kaat deta hai bina round kiye."
                },
                "challenge": {
                    "prompt_en": "Convert the string '200' to an integer, add 50, and print: Result: 250",
                    "prompt_hi": "String '200' ko int me convert karke 50 jodo aur print karo: Result: 250",
                    "starter_code": "s = '200'\n# Typecast and print:\n",
                    "expected_output": "Result: 250",
                    "solution_code": "s = '200'\nprint(f'Result: {int(s) + 50}')",
                    "solution_explanation_en": "Converts string '200' to int 200, adds 50 to get 250.",
                    "solution_explanation_hi": "'200' ko int bana kar 50 add karta hai.",
                    "hints": ["int(s) + 50"],
                    "ego_roast_hi": "int() function lagana bhool gaye?",
                    "ego_cheer_hi": "Type casting mastered! Ready for Operators! 🚀"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 5: Math and Logic (Operators)
    # =========================================================================
    {
        "id": "ch5_operators",
        "part_number": 1,
        "part_title": "PART 1: THE ABSOLUTE BASICS (ZERO TO CODE)",
        "chapter_number": 5,
        "title": "Chapter 5: Math and Logic (Operators)",
        "subtitle_en": "Arithmetic, floor division, modulus, comparison, logic, identity (is vs ==), and PEMDAS",
        "subtitle_hi": "Math operators, floor division, modulus, comparison, logic, is vs == aur BODMAS",
        "icon": "⚡",
        "estimated_time": "40 mins",
        "prerequisites_en": "Chapters 1 to 4.",
        "prerequisites_hi": "Chapter 1 se 4 tak.",
        "learning_objectives_en": [
            "Master arithmetic (+, -, *, /) and special operators (//, %, **)",
            "Use assignment shortcuts (+=, -=, *=)",
            "Master comparison operators (==, !=, >, <, >=, <=)",
            "Combine conditions with logical operators (and, or, not)",
            "Distinguish value equality (==) from object identity (is)",
            "Master operator precedence (PEMDAS/BODMAS)"
        ],
        "learning_objectives_hi": [
            "Arithmetic aur special operators (//, %, **) master karo",
            "Assignment shortcuts use karo (+=, -=, *=)",
            "Comparison operators seekho (==, !=, >, <, >=, <=)",
            "Logical operators (and, or, not) se multiple conditions jodna",
            "Value equality (==) aur identity (is) ka critical farak samjho",
            "Operator precedence (BODMAS / PEMDAS) ka niyam"
        ],
        "recap_en": "You mastered all Python operators: arithmetic, floor division, modulus, power, assignment, comparison, logical, identity, membership, and precedence order.",
        "recap_hi": "Aapne sabhi operators seekhe: math, floor division, modulus, powers, comparisons, and/or/not, is vs ==, aur BODMAS.",
        "subtopics": [
            {
                "id": "ch5_sub1_arithmetic_operators",
                "title": "Arithmetic operators (+, -, *, /)",
                "title_hi": "Arithmetic operators (+, -, *, /)",
                "icon": "➕",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The basic math operations: addition (+), subtraction (-), multiplication (*), and division (/).",
                "what_is_it_hi": "Normal maths ke operations: jodna (+), ghatana (-), guna karna (*), aur bhaag dena (/).",
                "why_need_it_en": "Every program performs math: calculating shopping cart totals, player damage, physics trajectories, or tax rates.",
                "why_need_it_hi": "Shopping cart ka bill, game physics, tax calculation — har jagah math operators use hote hain.",
                "how_to_use_en": "Place between two operands: a + b, a - b, a * b, a / b.",
                "how_to_use_hi": "Do numbers ke beech lagao: 10 + 5, 20 - 4, 6 * 7, 10 / 2.",
                "syntax": "sum_val = 10 + 5\ndiff = 20 - 4\nprod = 6 * 7\nquot = 15 / 3  # Always produces float (5.0)",
                "rules_en": [
                    "Division (/) in Python 3 ALWAYS yields a float, even if clean (8 / 2 -> 4.0).",
                    "Plus (+) can also concatenate strings ('a' + 'b' -> 'ab').",
                    "Asterisk (*) can also repeat strings ('Hi' * 3 -> 'HiHiHi')."
                ],
                "rules_hi": [
                    "Single slash (/) hamesha float (decimal) answer deta hai (8 / 2 = 4.0).",
                    "+ operator strings ko jodne ke kaam bhi aata hai ('a' + 'b' = 'ab').",
                    "* operator string ko repeat kar sakta hai ('Ha' * 3 = 'HaHaHa')."
                ],
                "analogy_en": "A pocket calculator built into your computer's CPU.",
                "analogy_hi": "Computer ke dimaag me laga hua digital calculator.",
                "common_mistakes": [
                    {
                        "mistake": "Dividing by zero: x = 10 / 0",
                        "why_it_fails_en": "ZeroDivisionError: division by zero.",
                        "why_it_fails_hi": "Zero se divide karne par computer crash ho jata hai.",
                        "fix": "Always check denominator: if denom != 0: res = num / denom."
                    }
                ],
                "example_1": {
                    "title": "Standard Arithmetic in Python",
                    "title_hi": "Basic Math Operations",
                    "code": "print('10 + 5 =', 10 + 5)\nprint('20 - 8 =', 20 - 8)\nprint('4 * 6 =', 4 * 6)\nprint('12 / 3 =', 12 / 3)",
                    "expected_output": "10 + 5 = 15\n20 - 8 = 12\n4 * 6 = 24\n12 / 3 = 4.0",
                    "explanation_en": "Shows four core arithmetic operations with exact outputs.",
                    "explanation_hi": "Chaaron core operations aur unka output dikhata hai."
                },
                "example_2": {
                    "title": "String Multiplication Trick",
                    "title_hi": "String ko repeat karna",
                    "code": "divider = '-' * 20\nprint(divider)\nprint('ALERT MESSAGE')\nprint(divider)",
                    "expected_output": "--------------------\nALERT MESSAGE\n--------------------",
                    "explanation_en": "'-' * 20 repeats the dash 20 times to create a decorative divider.",
                    "explanation_hi": "'-' * 20 se 20 baar dash repeat hoke divider banata hai."
                },
                "challenge": {
                    "prompt_en": "Calculate 25 multiplied by 4, subtract 10, and print: Result: 90",
                    "prompt_hi": "25 * 4 karke 10 ghatao aur print karo: Result: 90",
                    "starter_code": "# Calculate and print:\n",
                    "expected_output": "Result: 90",
                    "solution_code": "ans = (25 * 4) - 10\nprint(f'Result: {ans}')",
                    "solution_explanation_en": "Calculates (25 * 4) - 10 = 90 and prints it.",
                    "solution_explanation_hi": "(25 * 4) - 10 = 90 calculate karke print karta hai.",
                    "hints": ["(25 * 4) - 10"],
                    "ego_roast_hi": "Class 3 ki maths me phans gaye?",
                    "ego_cheer_hi": "Arithmetic calculations verified! ➕"
                }
            },
            {
                "id": "ch5_sub2_special_math_operators",
                "title": "Special math operators (Floor division //, Modulus %, Exponent **)",
                "title_hi": "Special math operators (Floor division //, Modulus %, Exponent **)",
                "icon": "🚀",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Python provides three super-math operators: Floor Division (//) discards the remainder to give whole quotients, Modulus (%) returns only the remainder, and Exponent (**) raises to a power.",
                "what_is_it_hi": "Floor Division (//) decimal ko hata kar poora quotient deta hai, Modulus (%) division ka remainder (bacha hua sheshphal) deta hai, aur Exponent (**) power (jaise 2 ki power 3) nikaalta hai.",
                "why_need_it_en": "Modulus is essential for checking even/odd numbers (n % 2 == 0) and clock arithmetic. Floor division calculates page counts. Exponent computes compound interest and physics formulas.",
                "why_need_it_hi": "Even/Odd number check karne ke liye % lagta hai (n % 2 == 0). Hours aur minutes calculate karne ke liye // aur % lagta hai. ** se power nikaalte hain.",
                "how_to_use_en": "7 // 2 gives 3. 7 % 2 gives 1. 2 ** 3 gives 8.",
                "how_to_use_hi": "7 // 2 = 3. 7 % 2 = 1. 2 ** 3 = 8.",
                "syntax": "quotient = 17 // 5   # 3\nremainder = 17 % 5   # 2 (since 5*3 + 2 = 17)\npower = 2 ** 8       # 256",
                "rules_en": [
                    "// rounds DOWN to the nearest integer towards negative infinity (floor).",
                    "% gives the remainder after division.",
                    "n % 2 == 0 is the universal test for even numbers; n % 2 != 0 is for odd numbers.",
                    "** has higher precedence than multiplication."
                ],
                "rules_hi": [
                    "// quotient ko neeche round karta hai (floor).",
                    "% hamesha remainder (sheshphal) nikaalta hai.",
                    "n % 2 == 0 even number check karne ka standard formula hai.",
                    "** ki priority multiplication se zyada hoti hai."
                ],
                "analogy_en": "If you have 7 samosas and 2 friends: each gets 3 full samosas (7 // 2 = 3), and 1 leftover samosa sits on the plate (7 % 2 = 1)!",
                "analogy_hi": "7 samose hain aur 2 dost. Har dost ko 3 samose milenge (7 // 2 = 3), aur 1 samosa plate me bach jayega (7 % 2 = 1)!",
                "common_mistakes": [
                    {
                        "mistake": "Using ^ for exponentiation: 2 ^ 3",
                        "why_it_fails_en": "^ in Python is bitwise XOR, NOT power! 2 ^ 3 evaluates to 1, not 8.",
                        "why_it_fails_hi": "Python me ^ power nahi balki bitwise XOR hota hai! Power ke liye double star ** lagta hai.",
                        "fix": "Always use ** for power: 2 ** 3 = 8."
                    }
                ],
                "example_1": {
                    "title": "Minutes and Seconds Conversion",
                    "title_hi": "Seconds ko Minutes aur Remainder Seconds me badalna",
                    "code": "total_seconds = 125\nminutes = total_seconds // 60\nremaining_sec = total_seconds % 60\nprint(f'{total_seconds}s = {minutes} min and {remaining_sec} sec')",
                    "expected_output": "125s = 2 min and 5 sec",
                    "explanation_en": "125 // 60 gives 2 minutes; 125 % 60 gives the remaining 5 seconds.",
                    "explanation_hi": "125 ko 60 se divide karke 2 minutes aur bache hue 5 seconds nikaalta hai."
                },
                "example_2": {
                    "title": "Powers and Squares",
                    "title_hi": "Powers nikaalna (**)",
                    "code": "base = 5\nprint('5 squared (5**2):', base ** 2)\nprint('5 cubed (5**3):', base ** 3)",
                    "expected_output": "5 squared (5**2): 25\n5 cubed (5**3): 125",
                    "explanation_en": "Uses ** for clean exponential math.",
                    "explanation_hi": "** se 5 ka square (25) aur cube (125) nikaalta hai."
                },
                "challenge": {
                    "prompt_en": "Compute 2 to the power 10 using ** and print: 2^10 = 1024",
                    "prompt_hi": "** use karke 2 ki power 10 nikaalo aur print karo: 2^10 = 1024",
                    "starter_code": "# Compute 2**10 and print:\n",
                    "expected_output": "2^10 = 1024",
                    "solution_code": "val = 2 ** 10\nprint(f'2^10 = {val}')",
                    "solution_explanation_en": "2 ** 10 computes 1024.",
                    "solution_explanation_hi": "2 ** 10 se 1024 calculate hota hai.",
                    "hints": ["2 ** 10"],
                    "ego_roast_hi": "^ mat laga dena galti se, ** lagana!",
                    "ego_cheer_hi": "Exponent power unlocked! 🚀"
                }
            },
            {
                "id": "ch5_sub3_assignment_operators",
                "title": "Assignment operators (+=, -=, *=)",
                "title_hi": "Assignment operators (+=, -=, *=)",
                "icon": "📝",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Augmented assignment operators combine a math operation with variable assignment in a single step (+=, -=, *=, /=, //=, %=, **=).",
                "what_is_it_hi": "Ye shorthand operators hote hain jo math operation aur value update ko ek hi step me kar dete hain (+=, -=, *=, /=).",
                "why_need_it_en": "Avoids repetitive typing: balance = balance + deposit becomes balance += deposit.",
                "why_need_it_hi": "Baar baar same variable ka naam do baar likhne se bachata hai: x = x + 5 ke badle x += 5.",
                "how_to_use_en": "x += 5 adds 5 to x. x *= 2 doubles x. x -= 3 subtracts 3 from x.",
                "how_to_use_hi": "x += 5 matlab 5 jod do, x *= 2 matlab double kar do.",
                "syntax": "x += 10   # Same as x = x + 10\nx -= 5    # Same as x = x - 5\nx *= 2    # Same as x = x * 2\nx /= 4    # Same as x = x / 4",
                "rules_en": [
                    "The target variable MUST already exist before applying an augmented assignment.",
                    "Evaluates the right side completely before applying the operator.",
                    "Works with other types too: string += '!' appends text."
                ],
                "rules_hi": [
                    "Variable pehle se create hona chahiye.",
                    "Right side pehle solve hoti hai fir operator apply hota hai.",
                    "String ke sath += use karne par text aage jud jata hai."
                ],
                "analogy_en": "Instead of saying 'Take my current wallet balance, add 50 rupees, and put it back', you just say 'Add 50 to my wallet'.",
                "analogy_hi": "Ye kehne ke bajaye 'Purani jeb me 50 jod kar nayi jeb banao', seedhe bolna: 'Jeb me 50 aur daal do'.",
                "common_mistakes": [
                    {
                        "mistake": "Writing =+ instead of +=: x =+ 5",
                        "why_it_fails_en": "=+ is NOT an augmented assignment; it assigns positive 5 (+5) to x!",
                        "why_it_fails_hi": "=+ likhne se x me positive 5 assign ho jayega, add nahi hoga.",
                        "fix": "Always put the operator FIRST, then the equal sign: +=, -=, *=."
                    }
                ],
                "example_1": {
                    "title": "Accumulating a Cart Total",
                    "title_hi": "Cart total me items jodna",
                    "code": "cart_total = 0\ncart_total += 500  # Book added\ncart_total += 250  # Pen added\nprint('Cart Final:', cart_total)",
                    "expected_output": "Cart Final: 750",
                    "explanation_en": "Adds 500 then 250 to cart_total cleanly.",
                    "explanation_hi": "cart_total me 500 aur 250 jod kar 750 banata hai."
                },
                "example_2": {
                    "title": "Doubling Values with *=",
                    "title_hi": "Double karna *= se",
                    "code": "power_level = 10\npower_level *= 2  # Superpower activated\nprint('Doubled Power:', power_level)",
                    "expected_output": "Doubled Power: 20",
                    "explanation_en": "Multiplies power_level by 2 in-place.",
                    "explanation_hi": "power_level ko double karke 20 banata hai."
                },
                "challenge": {
                    "prompt_en": "Initialize hp = 100, apply hp -= 30, and print: Remaining HP: 70",
                    "prompt_hi": "hp = 100 banao, hp -= 30 apply karo aur print karo: Remaining HP: 70",
                    "starter_code": "# Use -= and print:\n",
                    "expected_output": "Remaining HP: 70",
                    "solution_code": "hp = 100\nhp -= 30\nprint(f'Remaining HP: {hp}')",
                    "solution_explanation_en": "Deducts 30 using -= and prints.",
                    "solution_explanation_hi": "-= operator se 30 ghata kar print karta hai.",
                    "hints": ["hp = 100 then hp -= 30"],
                    "ego_roast_hi": "hp -= 30 likhna bhool gaye?",
                    "ego_cheer_hi": "Augmented operator mastered! ⚡"
                }
            },
            {
                "id": "ch5_sub4_comparison_operators",
                "title": "Comparison operators (==, !=, >, <, >=, <=)",
                "title_hi": "Comparison operators (==, !=, >, <, >=, <=)",
                "icon": "⚖️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Comparison operators compare two values and ALWAYS return a boolean (True or False).",
                "what_is_it_hi": "Comparison operators do values ko aapas me compare karte hain aur HAMESHA True ya False return karte hain.",
                "why_need_it_en": "All decision making in code (if statements) relies on comparisons: Is password correct (==)? Is stock out (!= 0)? Is balance sufficient (>= cost)?",
                "why_need_it_hi": "Har if/else decision isi par chalta hai: Kya password match hua (==)? Kya balance kaafi hai (>=)?",
                "how_to_use_en": "a == b (equal), a != b (not equal), a > b (greater), a < b (less), a >= b (greater/equal), a <= b (less/equal).",
                "how_to_use_hi": "== (barabar), != (barabar nahi), > (bada), < (chhota), >= (bada ya barabar), <= (chhota ya barabar).",
                "syntax": "is_match = (entered_pin == 1234)\nis_passing = (marks >= 40)\nis_different = (role != \"admin\")",
                "rules_en": [
                    "CRITICAL: Double equals (==) is comparison. Single equal (=) is assignment.",
                    "!= means NOT EQUAL.",
                    "Comparisons can be chained in Python: 10 < x < 20 (cleaner than C/Java!)."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: Double equal (==) compare karta hai, single equal (=) value assign karta hai.",
                    "!= ka matlab NOT EQUAL hota hai.",
                    "Python me chained comparison allowed hai: 10 < x < 20."
                ],
                "analogy_en": "A judge in a court holding scales of justice and saying 'Guilty (True)' or 'Not Guilty (False)'.",
                "analogy_hi": "Tarazu jaisa — dono paldon ko tola aur bataya ki barabar hain ya nahi.",
                "common_mistakes": [
                    {
                        "mistake": "Using = inside an if condition: if x = 5:",
                        "why_it_fails_en": "SyntaxError: invalid syntax. You cannot assign inside standard if conditions.",
                        "why_it_fails_hi": "if ke andar single = lagane par SyntaxError aayega.",
                        "fix": "Use double equals: if x == 5:"
                    }
                ],
                "example_1": {
                    "title": "Testing Equality and Non-Equality",
                    "title_hi": "Barabari check karna (== aur !=)",
                    "code": "secret_pin = 4455\nuser_attempt = 4455\nprint('Access Granted:', user_attempt == secret_pin)\nprint('Pin Mismatch:', user_attempt != secret_pin)",
                    "expected_output": "Access Granted: True\nPin Mismatch: False",
                    "explanation_en": "== evaluates to True because values match; != evaluates to False.",
                    "explanation_hi": "Dono match ho gaye to == True dega aur != False dega."
                },
                "example_2": {
                    "title": "Chained Comparisons in Python",
                    "title_hi": "Chained comparison (Range check)",
                    "code": "score = 85\nprint('Is score between 80 and 90?', 80 <= score <= 90)",
                    "expected_output": "Is score between 80 and 90? True",
                    "explanation_en": "Python natively evaluates 80 <= score <= 90 as (80 <= score and score <= 90).",
                    "explanation_hi": "Python seedhe check karta hai ki score 80 aur 90 ke beech me hai ya nahi."
                },
                "challenge": {
                    "prompt_en": "Check if marks = 75 is greater than or equal to 40, and print: Passed: True",
                    "prompt_hi": "Check karo kya marks = 75 >= 40 hai, aur print karo: Passed: True",
                    "starter_code": "marks = 75\n# Check >= 40 and print:\n",
                    "expected_output": "Passed: True",
                    "solution_code": "marks = 75\nprint(f'Passed: {marks >= 40}')",
                    "solution_explanation_en": "Evaluates marks >= 40 and prints True.",
                    "solution_explanation_hi": "marks >= 40 True banta hai aur print hota hai.",
                    "hints": ["print(f'Passed: {marks >= 40}')"],
                    "ego_roast_hi": ">= operator lagana bhool gaye?",
                    "ego_cheer_hi": "Comparison operator verified! ⚖️"
                }
            },
            {
                "id": "ch5_sub5_logical_operators",
                "title": "Logical operators (and, or, not)",
                "title_hi": "Logical operators (and, or, not)",
                "icon": "🧠",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Logical operators combine multiple boolean conditions. 'and' requires BOTH conditions to be True; 'or' requires AT LEAST ONE condition to be True; 'not' inverts the boolean (True becomes False, False becomes True).",
                "what_is_it_hi": "'and' tabhi True hota hai jab DONO conditions True hon. 'or' tab True hota hai jab KAM SE KAM EK condition True ho. 'not' ulta kar deta hai (True ko False, False ko True).",
                "why_need_it_en": "Real security checks have multiple rules: (has_ticket and has_id), or (is_admin or has_permission).",
                "why_need_it_hi": "Real world rules complex hote hain: (ticket bhi chahiye aur ID bhi) ya (admin ho ya special pass ho).",
                "how_to_use_en": "cond1 and cond2, cond1 or cond2, not cond.",
                "how_to_use_hi": "and, or, not seedhe English words use karo (&& ya || nahi lagta).",
                "syntax": "can_enter = (has_ticket and has_id)\ngets_discount = (is_student or is_senior)\nis_blocked = not is_verified",
                "rules_en": [
                    "Python uses plain English words: 'and', 'or', 'not' (NOT &&, ||, ! like in C/Java).",
                    "Short-circuit evaluation: In 'a and b', if 'a' is False, Python doesn't even look at 'b'!",
                    "In 'a or b', if 'a' is True, Python skips evaluating 'b'."
                ],
                "rules_hi": [
                    "Python me English words and, or, not lagte hain (&& ya || nahi).",
                    "Short-circuit evaluation: agar 'and' me pehla hi False ho gaya to Python aage check hi nahi karta.",
                    "agar 'or' me pehla hi True ho gaya to Python turant True maan leta hai."
                ],
                "analogy_en": "'and' is like a bank vault needing TWO keys simultaneously. 'or' is like a house door with a front key OR a back key. 'not' is a reverse switch.",
                "analogy_hi": "'and' bank ki tijori jaisa hai jisme dono chaabi lagani padti hai. 'or' ghar ke do darwazon jaisa hai — koi ek khula ho to andar ja sakte ho.",
                "common_mistakes": [
                    {
                        "mistake": "Writing && or || like in C/Java/JS: if a && b:",
                        "why_it_fails_en": "SyntaxError: invalid syntax. Python uses English words 'and' and 'or'.",
                        "why_it_fails_hi": "Python me && aur || syntax error dete hain.",
                        "fix": "Use words: 'and', 'or', 'not'."
                    }
                ],
                "example_1": {
                    "title": "Logical AND / OR in Action",
                    "title_hi": "and aur or ka comparison",
                    "code": "has_id = True\nhas_ticket = False\nprint('Can enter with AND:', has_id and has_ticket)\nprint('Can enter with OR:', has_id or has_ticket)",
                    "expected_output": "Can enter with AND: False\nCan enter with OR: True",
                    "explanation_en": "AND requires both True (so False here); OR needs only one True (so True here).",
                    "explanation_hi": "AND dono True maangta hai (isliye False), OR sirf ek True maangta hai (isliye True)."
                },
                "example_2": {
                    "title": "The NOT Inverter Operator",
                    "title_hi": "not se boolean ulta karna",
                    "code": "is_raining = False\nprint('Good day for a walk?', not is_raining)",
                    "expected_output": "Good day for a walk? True",
                    "explanation_en": "not False evaluates to True.",
                    "explanation_hi": "not False ko ulta karke True bana deta hai."
                },
                "challenge": {
                    "prompt_en": "Evaluate (True and False) or True and print: Result: True",
                    "prompt_hi": "Evaluate karo (True and False) or True aur print karo: Result: True",
                    "starter_code": "# Evaluate expression and print:\n",
                    "expected_output": "Result: True",
                    "solution_code": "res = (True and False) or True\nprint(f'Result: {res}')",
                    "solution_explanation_en": "(True and False) is False; False or True is True.",
                    "solution_explanation_hi": "(True and False) False hua; False or True True ban gaya.",
                    "hints": ["(True and False) or True"],
                    "ego_roast_hi": "Logic gates bhool gaye kya?",
                    "ego_cheer_hi": "Boolean logic circuits complete! 🧠"
                }
            },
            {
                "id": "ch5_sub6_identity_membership",
                "title": "Identity and Membership operators (is, is not, in, not in)",
                "title_hi": "Identity aur Membership operators (is, is not, in, not in)",
                "icon": "🎯",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Identity operators ('is', 'is not') test whether two variables point to the EXACT same memory location in RAM. Membership operators ('in', 'not in') test whether a value exists inside a sequence (string, list, tuple).",
                "what_is_it_hi": "Identity operators ('is', 'is not') check karte hain ki kya do variables RAM ke SAME memory address par point kar rahe hain. Membership operators ('in', 'not in') check karte hain ki kya koi cheez kisi list ya string ke andar maujood hai ya nahi.",
                "why_need_it_en": "Distinguishing '==' (value equality) from 'is' (identity) is one of the most critical topics in Python interviews! Checking if a character exists in a string ('a' in 'cat') is cleanest with 'in'.",
                "why_need_it_hi": "Interview ka number 1 question: '==' aur 'is' me kya farak hai? Aur kisi word me letter dhoondna ho to 'in' sabse best hai.",
                "how_to_use_en": "'x is None' checks identity with None singleton. ''py' in 'python'' checks substring membership.",
                "how_to_use_hi": "x is None check karo. 'py' in 'python' se substring check karo.",
                "syntax": "# Identity:\nx is None\nx is not None\n\n# Membership:\n\"cat\" in [\"cat\", \"dog\", \"fish\"]\n\"@\" in \"user@example.com\"",
                "rules_en": [
                    "CRITICAL LAW: '==' checks if values are EQUAL. 'is' checks if memory IDs are IDENTICAL (id(a) == id(b)).",
                    "Two lists [1, 2] and [1, 2] have identical values (== True), but different memory addresses (is False)!",
                    "ALWAYS use 'is None' or 'is not None' to check for None (never == None).",
                    "'in' works on strings, lists, tuples, sets, and dictionary keys."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: '==' value check karta hai (kya dono me same cheez likhi hai). 'is' memory address check karta hai (kya dono ek hi dabba hain).",
                    "Do alag lists [1, 2] aur [1, 2] ka '==' True hoga, lekin 'is' False hoga!",
                    "None check karne ke liye hamesha 'is None' lagao, '== None' nahi.",
                    "'in' string, list, tuple sab me search karta hai."
                ],
                "analogy_en": "Two identical twin brothers wearing the exact same clothes look identical (== is True), but they are two distinct human beings ('is' is False!). Only looking in a mirror gives 'is True'.",
                "analogy_hi": "Do judwaa bhai ek jaisi shirt pehne hain: dono dikhte barabar hain (== True), lekin dono alag insaan hain ('is' False!). Aaine me apna chehra dekhna 'is True' hai.",
                "common_mistakes": [
                    {
                        "mistake": "Using 'is' instead of '==' for value comparisons: if name is 'Alex':",
                        "why_it_fails_en": "Python will throw SyntaxWarning: 'is' with a literal. 'is' tests object identity, not value equality.",
                        "why_it_fails_hi": "String aur number compare karne ke liye '==' lagta hai, 'is' lagane par warning aur bugs aate hain.",
                        "fix": "Use '==' for values: if name == 'Alex'. Reserve 'is' for None, True, False."
                    }
                ],
                "example_1": {
                    "title": "The Classic '==' vs 'is' Proof",
                    "title_hi": "== aur is ka live farak",
                    "code": "list_a = [1, 2, 3]\nlist_b = [1, 2, 3]\nprint('Values equal (list_a == list_b):', list_a == list_b)\nprint('Same object (list_a is list_b):', list_a is list_b)",
                    "expected_output": "Values equal (list_a == list_b): True\nSame object (list_a is list_b): False",
                    "explanation_en": "list_a and list_b have identical elements (== True), but live at different memory addresses (is False).",
                    "explanation_hi": "Dono me same items hain (== True), lekin RAM me do alag jagah hain (is False)."
                },
                "example_2": {
                    "title": "Membership Operator with 'in'",
                    "title_hi": "List aur String me 'in' search karna",
                    "code": "email = 'student@college.edu'\nprint('Has @ symbol:', '@' in email)\nallowed_roles = ['admin', 'moderator']\nprint('Is guest allowed:', 'guest' in allowed_roles)",
                    "expected_output": "Has @ symbol: True\nIs guest allowed: False",
                    "explanation_en": "'in' tests substring in email and element membership in allowed_roles.",
                    "explanation_hi": "'in' email me '@' aur roles list me 'guest' dhoondta hai."
                },
                "challenge": {
                    "prompt_en": "Check if 'Python' is in 'I love Python coding' and print: Found: True",
                    "prompt_hi": "Check karo kya 'Python' in 'I love Python coding' hai aur print karo: Found: True",
                    "starter_code": "msg = 'I love Python coding'\n# Check membership and print:\n",
                    "expected_output": "Found: True",
                    "solution_code": "msg = 'I love Python coding'\nprint(f'Found: {\"Python\" in msg}')",
                    "solution_explanation_en": "Evaluates 'Python' in msg to True and prints.",
                    "solution_explanation_hi": "'Python' in msg True deta hai aur print hota hai.",
                    "hints": ["'Python' in msg"],
                    "ego_roast_hi": "in operator use karna bhool gaye?",
                    "ego_cheer_hi": "Identity & membership pro! 🎯"
                }
            },
            {
                "id": "ch5_sub7_order_of_operations",
                "title": "Order of operations (PEMDAS/BODMAS in Python)",
                "title_hi": "Order of operations (PEMDAS/BODMAS in Python)",
                "icon": "📐",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Operator precedence dictates the order in which Python evaluates expressions. Like in school mathematics, Python follows PEMDAS/BODMAS: Parentheses first (), Exponents **, Multiplication/Division (*, /, //, %), Addition/Subtraction (+, -), Comparison (==, <), Logical (not, and, or).",
                "what_is_it_hi": "Operator precedence ka matlab hai ki agar ek line me multiple operations hain to computer pehle kaun sa solve karega. Python BODMAS follow karta hai: Pehle Brackets (), fir Powers **, fir Multiply/Divide (*, /), fir Add/Subtract (+, -), aur aakhri me and/or.",
                "why_need_it_en": "Without understanding precedence, 2 + 3 * 4 would be computed as 20 instead of the mathematically correct 14!",
                "why_need_it_hi": "Agar BODMAS na ho to 2 + 3 * 4 ka answer 20 aa jayega jo galat hai. Sahi answer 14 hai kyunki multiply pehle hota hai.",
                "how_to_use_en": "When in doubt, ALWAYS use parentheses ()! They make code unambiguous to both Python and human teammates.",
                "how_to_use_hi": "Jab bhi confusion ho, brackets () lagao! Brackets se galti hone ka chance zero ho jata hai.",
                "syntax": "# 2 + (3 * 4) = 14\nresult = 2 + 3 * 4\n# (2 + 3) * 4 = 20\nbracket_result = (2 + 3) * 4",
                "rules_en": [
                    "Order: 1. Parentheses ()  2. Exponents **  3. Unary minus -x  4. *, /, //, %  5. +, -  6. Comparisons  7. not  8. and  9. or",
                    "Operations at the same level evaluate from LEFT to RIGHT (except exponentiation **, which evaluates right to left: 2**3**2 is 2**9 = 512).",
                    "Explicit parentheses always override default precedence."
                ],
                "rules_hi": [
                    "Order: 1. Brackets ()  2. Power **  3. *, /, //, %  4. +, -  5. Comparisons  6. not  7. and  8. or",
                    "Same level wale operations LEFT se RIGHT solve hote hain (lekin ** right to left hota hai).",
                    "Brackets lagane se default precedence override ho jaati hai."
                ],
                "analogy_en": "VIP line at the airport: passengers with first-class tickets (parentheses) board before general economy (addition).",
                "analogy_hi": "Airport par VIP board pass jaisa — bracket lagte hi wo calculation pehle line me sabse aage chali jaati hai.",
                "common_mistakes": [
                    {
                        "mistake": "Writing 10 + 20 / 2 and expecting 15.",
                        "why_it_fails_en": "Division happens first: 20 / 2 = 10, then 10 + 10 = 20.0!",
                        "why_it_fails_hi": "Division pehle ho gaya isliye answer 20.0 aaya, 15 nahi.",
                        "fix": "Use parentheses: (10 + 20) / 2 = 15.0."
                    }
                ],
                "example_1": {
                    "title": "PEMDAS Demonstration",
                    "title_hi": "BODMAS ka live example",
                    "code": "no_brackets = 2 + 3 * 4\nwith_brackets = (2 + 3) * 4\nprint('2 + 3 * 4 =', no_brackets)\nprint('(2 + 3) * 4 =', with_brackets)",
                    "expected_output": "2 + 3 * 4 = 14\n(2 + 3) * 4 = 20",
                    "explanation_en": "Multiplication takes precedence unless overridden by parentheses.",
                    "explanation_hi": "Multiply pehle hota hai jab tak brackets na lagaye jayein."
                },
                "example_2": {
                    "title": "Right-to-Left Exponentiation",
                    "title_hi": "Power ka Right-to-Left evaluation",
                    "code": "exp_val = 2 ** 3 ** 2  # Evaluates 3**2 = 9, then 2**9 = 512\nprint('2 ** 3 ** 2 =', exp_val)",
                    "expected_output": "2 ** 3 ** 2 = 512",
                    "explanation_en": "Double exponents evaluate from right to left (3**2 first, then 2**9).",
                    "explanation_hi": "Double exponent me pehle 3**2=9 hota hai, fir 2**9=512 banta hai."
                },
                "challenge": {
                    "prompt_en": "Calculate (10 + 5) * 2 - (8 // 2) and print: Calculated: 26",
                    "prompt_hi": "Calculate karo (10 + 5) * 2 - (8 // 2) aur print karo: Calculated: 26",
                    "starter_code": "# Calculate using order of operations:\n",
                    "expected_output": "Calculated: 26",
                    "solution_code": "val = (10 + 5) * 2 - (8 // 2)\nprint(f'Calculated: {val}')",
                    "solution_explanation_en": "(15 * 2) - 4 = 30 - 4 = 26.",
                    "solution_explanation_hi": "(15 * 2) - 4 = 30 - 4 = 26 calculate karta hai.",
                    "hints": ["(10 + 5) * 2 - (8 // 2)"],
                    "ego_roast_hi": "BODMAS rule bhool gaye?",
                    "ego_cheer_hi": "PART 1 OFFICIALLY COMPLETED! 🏆 Zero to Code Master!"
                }
            }
        ]
    }
]
