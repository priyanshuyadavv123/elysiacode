import json

curriculum = [
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
        "why_need_it_en": "Computers do not speak human languages (like Hindi or English). Without a standardized programming language, you cannot command hardware to store files, calculate bank transactions, or stream video.",
        "why_need_it_hi": "Computer insaani bhasha (Hindi ya English) nahi samajhta. Agar hum coding language use nahi karenge, to computer se na to bank calculation karwa sakte hain, na YouTube video play karwa sakte hain, aur na hi games chala sakte hain.",
        "how_to_use_en": "You write instructions using standard commands like `print()` to send output to the screen.",
        "how_to_use_hi": "Hum computer ko built-in commands dete hain. Jaise screen par kuch bolne ke liye `print('Text')` command likhi jaati hai.",
        "syntax": "print(\"Message to display\")",
        "rules_en": [
          "Case Sensitivity Rule: `print()` is valid. `Print()` or `PRINT()` with capital P will crash with `NameError`.",
          "Quote Matching Rule: Text strings must start and end with the EXACT same quote type (single `'...'` or double `\"...\"`).",
          "Parentheses Pairing: Every opening parenthesis `(` must have a closing parenthesis `)`.",
          "Sequential Execution: The computer executes your code line-by-line from TOP to BOTTOM, never jumping randomly."
        ],
        "rules_hi": [
          "Case Sensitivity Niyam: Python me `print()` chhota likhna zaroori hai. Bada `Print()` ya `PRINT()` likhoge to computer crash ho jayega (`NameError`).",
          "Quotes ka Niyam: Text likhte waqt shuru aur aakhir me same quote hona chahiye — `'Hello'` ya `\"Hello\"`. Aisa nahi kar sakte: `'Hello\"`.",
          "Brackets ka Niyam: Har khulne wale bracket `(` ke sath closing bracket `)` lagana zaroori hai.",
          "Top-to-Bottom Niyam: Computer hamesha pehli line se aakhri line tak ek-ek karke code chalaata hai."
        ],
        "analogy_en": "Think of the computer as a robot chef in a kitchen. If you shout 'make food', it will crash. But if you give a step-by-step recipe: '1. Take 2 cups of water. 2. Boil for 2 minutes. 3. Put noodles', it makes the best dish in seconds. Code is that exact recipe!",
        "analogy_hi": "Computer ko ek robot chef samjho. Agar tum use bologe 'khana banao', wo confuse ho jayega. Lekin agar bologe '1. 2 cup paani ubaalo. 2. Maggi daalo. 3. 2 minute pakao', to wo 1 second me mast Maggi bana dega! Code wahi exact step-by-step recipe hai.",
        "example_1": {
          "title": "Giving the Computer a Voice",
          "title_hi": "Computer ko aawaaz dena (Pehla Instruction)",
          "code": "print('Hello, World!')\nprint('I am learning Python from scratch!')",
          "explanation_en": "• Line 1: Tells the computer to display 'Hello, World!' on the terminal.\n• Line 2: Runs immediately after Line 1 and outputs the second line of text.",
          "explanation_hi": "• Line 1: Computer terminal screen par 'Hello, World!' print karta hai.\n• Line 2: Line 1 khatam hote hi agli line par naya message print karta hai."
        },
        "example_2": {
          "title": "Real World: Automated Server Health Check",
          "title_hi": "Real World: Server Status Notification",
          "code": "print('--- SYSTEM INITIALIZING ---')\nprint('CPU Status: Online (100% Healthy)')\nprint('Ready to accept user traffic.')",
          "explanation_en": "• Displays real-time status messages during server startup.",
          "explanation_hi": "• Server start hote waqt engineer ko terminal me green status dikhane ke liye print statements use hote hain."
        },
        "challenge": {
          "prompt_en": "Write a Python instruction to print the exact message: `I am a future Python Pro`",
          "prompt_hi": "Python instruction likho jo screen par exact print kare: `I am a future Python Pro`",
          "starter_code": "# Write your print statement below:\n",
          "expected_output": "I am a future Python Pro",
          "solution_code": "print('I am a future Python Pro')",
          "solution_explanation_hi": "`print('I am a future Python Pro')` likhne se computer exact wahi text terminal screen par display kar deta hai.",
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
        "what_is_it_en": "Python is a high-level, interpreted programming language created by Guido van Rossum in 1991. Its core design philosophy emphasizes code readability and simplicity above all else.",
        "what_is_it_hi": "Python ek aisi programming language hai jise insaani English jaisa banaya gaya hai. 1991 me Guido van Rossum ne isko is soch ke sath banaya tha ki coding har aam insaan ke liye aasaan honi chahiye.",
        "why_need_it_en": "In languages like C++ or Java, writing 'Hello World' requires 7+ lines of boilerplate (classes, public static void main, header imports). Python lets you express complex thoughts in 1 line.",
        "why_need_it_hi": "Agar C++ ya Java me ek chhota sa naam print karna ho, to 7-8 line ka kathin code likhna padta hai (classes, public static void main, curly braces). Python me wahi kaam sirf 1 line me ho jata hai bina faltu formality ke.",
        "how_to_use_en": "Just write clean, plain English-like statements without semicolons `;` or curly braces `{}`.",
        "how_to_use_hi": "Bina kisi semicolon `;` ya curly brackets `{}` ke saaf-suthri English ki tarah lines likho.",
        "syntax": "# Java: 7 lines boilerplate\n# Python:\nprint(\"Clean and simple\")",
        "rules_en": [
          "No Semicolons: Python does not require semicolons `;` at the end of lines.",
          "Readability Counts: Write simple, direct code instead of complicated nested hacks.",
          "Indentation Replaces Braces: In Python, whitespace and indentation define code blocks, not curly braces `{}`.",
          "Massive Ecosystem: Always check if a built-in function or standard library module already solves your problem."
        ],
        "rules_hi": [
          "Semicolon ki Chutti: Python me har line ke aakhir me semicolon `;` lagane ki koi zarurat nahi hoti.",
          "Indentation ka Niyam: Python me blocks curly braces `{}` se nahi, balki barabar spaces (indentation) se bante hain.",
          "Clean English Style: Code jitna simple hoga, utna jaldi chalega aur bugs kam aayenge.",
          "Standard Library ka Jaadu: Python me har mushkil kaam ke liye pehle se built-in tools maujood hote hain."
        ],
        "analogy_en": "C++ is like driving a manual formula-1 racing car with 18 complex levers. Python is like driving a modern Tesla with autopilot — you just tell it where to go!",
        "analogy_hi": "C++ ya Java chalana 18 gears wale puraane truck jaisa hai jisme har clutch sambhalna padta hai. Python automatic Tesla jaisi hai — bas destination batao aur gaadi chal padti hai!",
        "example_1": {
          "title": "Printing Multiple Lines Cleanly",
          "title_hi": "Multiple lines bina kisi headache ke print karna",
          "code": "print('1. Clean Syntax')\nprint('2. No Semicolons')\nprint('3. Huge Community')",
          "explanation_en": "• Each `print()` automatically places its output on a brand-new line.",
          "explanation_hi": "• Har `print()` statement automatically agla output nayi line par bhejta hai."
        },
        "example_2": {
          "title": "Real World: Math Made Simple",
          "title_hi": "Real World: Direct Mathematical Calculation",
          "code": "print(250 + 750)\nprint(50 * 20)",
          "explanation_en": "• Python acts as a high-powered calculator directly without needing variable declarations.",
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
        "what_is_it_en": "Python is a general-purpose language. That means it is not restricted to one platform — it dominates Artificial Intelligence, Web Development, Automation Bots, Data Science, and Cybersecurity.",
        "what_is_it_hi": "Python ek 'General Purpose' bhasha hai. Iska matlab ye kisi ek kaam tak seemit nahi hai — chahe AI banana ho, Instagram bot banana ho, data analytics karni ho ya hacking tools banane ho, sab Python se hota hai.",
        "why_need_it_en": "Learning Python gives you an unfair advantage: with one single language, you can switch from building websites to training neural networks without learning a new language from scratch.",
        "why_need_it_hi": "Agar tum Python seekh lete ho, to tumhe alag-alag field ke liye 10 nayi languages nahi seekhni padengi. Ek hi language se tum bot bhi bana loge aur ChatGPT jaisa AI bhi!",
        "how_to_use_en": "You combine Python's core logic with specialized industry libraries (like Django for web, TensorFlow for AI, Pandas for data).",
        "how_to_use_hi": "Python ke basic logic ko industry ki libraries ke sath jod kar bade-bade projects banaye jaate hain.",
        "syntax": "# 1. Web: Flask / Django\n# 2. AI: PyTorch / TensorFlow\n# 3. Automation: Selenium / Requests",
        "rules_en": [
          "Master Fundamentals First: Before jumping into AI or web frameworks, you must master Variables, Conditionals, Loops, and Functions.",
          "DRY Principle: Don't Repeat Yourself. Use reusable code instead of copy-pasting.",
          "Understand the Problem: 80% of programming is thinking about logic; only 20% is typing code."
        ],
        "rules_hi": [
          "Basics Pehle Master Karo: AI ya Web development me jaane se pehle Variables, Conditions, Loops aur Functions me pakad hona zaroori hai.",
          "DRY Rule (Don't Repeat Yourself): Ek hi code ko baar-baar copy-paste mat karo, reusable functions banao.",
          "Logic First: 80% kaam dimaag me sochna hota hai, code likhna sirf 20% hota hai."
        ],
        "analogy_en": "Learning Python is like learning English. Once you know English, you can write a poem, a business contract, a legal paper, or a comic book. Python is the universal language of modern tech!",
        "analogy_hi": "Python seekhna English seekhne jaisa hai. Ek baar English aa gayi to tum gaana bhi likh sakte ho, business deal bhi kar sakte ho aur comedy bhi. Python technology ki universal bhasha hai!",
        "example_1": {
          "title": "A Mini Automation Script",
          "title_hi": "Chhota Automation Script",
          "code": "task = 'Automate Instagram Daily Report'\nstatus = 'Done in 0.05 seconds'\nprint(task + ' -> ' + status)",
          "explanation_en": "• Demonstrates how Python combines strings to generate automated reports.",
          "explanation_hi": "• String concatenation use karke automated task ki report print karta hai."
        },
        "example_2": {
          "title": "Real World: AI Bot Confidence Score",
          "title_hi": "Real World: AI Decision Confidence",
          "code": "prediction = 'Cat'\nconfidence_percentage = 99.4\nprint(f'AI Prediction: {prediction} ({confidence_percentage}%)')",
          "explanation_en": "• Formats an AI vision model's output cleanly.",
          "explanation_hi": "• AI image classifier ka output formatted text me print karta hai."
        },
        "challenge": {
          "prompt_en": "Print: `Python powers AI, Web, and Automation!`",
          "prompt_hi": "Print karo: `Python powers AI, Web, and Automation!`",
          "starter_code": "# Write the exact print statement:\n",
          "expected_output": "Python powers AI, Web, and Automation!",
          "solution_code": "print('Python powers AI, Web, and Automation!')",
          "solution_explanation_hi": "Exact wahi text quotes ke andar pass kiya.",
          "ego_roast_hi": "Bhai spelling check karo! Ek bhi letter galat hua to computer reject kar dega!",
          "ego_cheer_hi": "Chapter 0 Conquered! 🚀 Ab tum asli memory aur data structures me enter karne ke liye ready ho!"
        }
      }
    ]
  }
]

print("Chapter 0 structured.")
