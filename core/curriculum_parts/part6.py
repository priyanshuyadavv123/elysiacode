"""
Part 6: The Peak (Advanced Python Concepts)
Chapters 19, 20, 21, 22, and 23 with exact syllabus titles and subtopics.
Exhaustive bilingual details, syntax rules, memory models, analogies, 2 verified examples, and testable challenges.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 19: Advanced List Magic (Comprehensions)
    # =========================================================================
    {
        "id": "ch19_advanced_list_magic",
        "part_number": 6,
        "part_title": "PART 6: THE PEAK (ADVANCED PYTHON CONCEPTS)",
        "chapter_number": 19,
        "title": "Chapter 19: Advanced List Magic (Comprehensions)",
        "subtitle_en": "Transform multi-line looping transformations into concise, blazing-fast single-line expressions",
        "subtitle_hi": "Loops ko high-performance single-line expressions me convert karein",
        "icon": "🪄",
        "estimated_time": "45 mins",
        "prerequisites_en": "Parts 1 to 3 (For loops, lists, dictionaries, sets, conditionals).",
        "prerequisites_hi": "Part 1 se 3 tak (Loops, lists, dicts, sets, conditionals).",
        "learning_objectives_en": [
            "Understand list comprehension syntax and its performance advantage over standard loops",
            "Apply filtering conditions (trailing if) and ternary transforms (leading if-else)",
            "Master dictionary comprehensions ({k: v for ...}) and set comprehensions ({x for ...})"
        ],
        "learning_objectives_hi": [
            "List comprehension ka syntax aur C-level performance advantage samjhein",
            "Filtering (trailing if) aur value transform (leading if-else) use karein",
            "Dictionary ({k: v for ...}) aur Set ({x for ...}) comprehensions master karein"
        ],
        "recap_en": "You mastered comprehensions: transforming sequences in a single readable line, filtering with if, transforming with if-else, and building instant lookup tables with dict and set comprehensions.",
        "recap_hi": "Aapne list, dict aur set comprehensions master kar liye hain jo Python code ko 5x concise aur C-level fast banate hain.",
        "subtopics": [
            {
                "id": "ch19_sub1_list_comprehensions",
                "title": "List comprehensions (Writing for loops in a single line)",
                "title_hi": "List comprehensions (Ek line me for loop likhna)",
                "icon": "⚡",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "A list comprehension is an elegant, concise Pythonic syntax for creating a new list by transforming elements from an existing iterable in a single expression.",
                "what_is_it_hi": "List comprehension ek single-line Pythonic syntax hai jo kisi existing sequence ya range ke har element ko transform karke ek nayi list produce karta hai.",
                "why_need_it_en": "Traditional for loops require initializing an empty list and calling .append() repeatedly. List comprehensions run at C-level speed inside CPython, reducing bytecode overhead and making code dramatically cleaner.",
                "why_need_it_hi": "Traditional loop me pehle khali list banani padti hai fir baar-baar .append() call karna padta hai. Comprehension CPython me C-level par optimize hota hai aur code ko chota aur fast banata hai.",
                "how_to_use_en": "Use bracket notation: [expression for item in iterable].",
                "how_to_use_hi": "Square brackets use karein: [expression for item in iterable].",
                "syntax": "# Traditional way:\nsquares = []\nfor n in range(5):\n    squares.append(n ** 2)\n\n# Pythonic List Comprehension:\nsquares = [n ** 2 for n in range(5)]",
                "rules_en": [
                    "Syntax: [expression for item in iterable].",
                    "The expression is evaluated for every item and collected into a brand-new list.",
                    "The original iterable remains completely unchanged.",
                    "Avoid overly complex nested comprehensions that sacrifice code readability (Zen of Python: Readability counts)."
                ],
                "rules_hi": [
                    "Syntax: [expression for item in iterable] hota hai.",
                    "Har item par expression compute hoke ek nayi list me collect hoti hai.",
                    "Original sequence ya list me koi badlav nahi hota.",
                    "Agar logic bohot complex ya 3-4 loops deep ho to standard loop use karein taaki readability kharab na ho."
                ],
                "analogy_en": "Instead of manually plucking oranges, peeling them one by one, and placing each into a basket across 4 steps, you put them through a juicing conveyer belt that transforms and outputs the crate in one smooth motion.",
                "analogy_hi": "Manual tarike me pehle khali tokri rakho, ek ek aam uthao, dho kar tokri me daalo. Comprehension ek automatic sorting conveyer belt jaisa hai jo ek stroke me fresh crate taiyar kar deta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Using a comprehension purely for side effects like [print(x) for x in items] without using the resulting list.",
                        "why_it_fails_en": "Creates a throwaway list in memory filled with [None, None...], wasting RAM.",
                        "why_it_fails_hi": "Memory me faltu ki [None, None...] list ban jati hai jo RAM waste karti hai.",
                        "fix": "Use a standard for x in items: print(x) when performing side effects."
                    }
                ],
                "example_1": {
                    "title": "Squares of Numbers via List Comprehension",
                    "title_hi": "List comprehension se numbers ka square nikalna",
                    "code": "numbers = [1, 2, 3, 4, 5]\nsquares = [n ** 2 for n in numbers]\nprint('Original:', numbers)\nprint('Squares:', squares)",
                    "expected_output": "Original: [1, 2, 3, 4, 5]\nSquares: [1, 4, 9, 16, 25]",
                    "explanation_en": "Evaluates n**2 for each element in numbers and collects the results into a new list.",
                    "explanation_hi": "Har number ka square nikal kar ek nayi list me collect kar leta hai."
                },
                "example_2": {
                    "title": "String Cleaning and Normalization",
                    "title_hi": "Strings ko clean aur title-case karna",
                    "code": "raw_names = ['  rohan ', 'PRIYA', '  amit ']\ncleaned = [name.strip().title() for name in raw_names]\nprint('Cleaned Names:', cleaned)",
                    "expected_output": "Cleaned Names: ['Rohan', 'Priya', 'Amit']",
                    "explanation_en": "Strips extraneous whitespace and standardizes casing for each string in one line.",
                    "explanation_hi": "Extra spaces hata kar har naam ko ek hi line me sahi format me le aata hai."
                },
                "challenge": {
                    "prompt_en": "Given celsius = [0, 20, 35, 100], write a list comprehension to convert them to Fahrenheit: [(c * 9/5) + 32 for c in celsius]. Print the fahrenheit list.",
                    "prompt_hi": "celsius = [0, 20, 35, 100] list ko Fahrenheit me convert karke print karo: [32.0, 68.0, 95.0, 212.0]",
                    "starter_code": "celsius = [0, 20, 35, 100]\n# Write list comprehension:\n",
                    "expected_output": "[32.0, 68.0, 95.0, 212.0]",
                    "solution_code": "celsius = [0, 20, 35, 100]\nfahrenheit = [(c * 9/5) + 32 for c in celsius]\nprint(fahrenheit)",
                    "solution_explanation_en": "Calculates (c * 9/5) + 32 for each degree in celsius in a single line.",
                    "solution_explanation_hi": "Comprehension se formula har element par apply hota hai.",
                    "hints": ["[(c * 9/5) + 32 for c in celsius]"],
                    "ego_roast_hi": "Ek line ki comprehension me atack gaye?",
                    "ego_cheer_hi": "List comprehension master! 🪄"
                }
            },
            {
                "id": "ch19_sub2_adding_if_conditions",
                "title": "Adding if conditions to comprehensions",
                "title_hi": "Comprehensions me if conditions add karna",
                "icon": "🎯",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "You can add filtering if conditions to the end of a comprehension to include only items meeting a condition, or use ternary x if cond else y at the beginning to conditionally transform items.",
                "what_is_it_hi": "Comprehension ke end me if laga kar aap specific items ko filter kar sakte hain, ya shuru me x if cond else y laga kar conditionally transform kar sakte hain.",
                "why_need_it_en": "Allows combining filtering and transformation into a single pass without needing nested if statements inside loops.",
                "why_need_it_hi": "Loop ke andar alag se if condition lagane ki zaroorat nahi padti; filtering aur conversion ek hi line me perform ho jate hain.",
                "how_to_use_en": "Trailing if for filtering: [x for x in data if condition]. Leading if-else for transformation: [a if cond else b for x in data].",
                "how_to_use_hi": "Filter karne ke liye trailing if: [x for x in data if condition]. Transform karne ke liye: [a if cond else b for x in data].",
                "syntax": "# Filter even numbers:\nevens = [x for x in numbers if x % 2 == 0]\n# Transform even/odd label:\nlabels = ['EVEN' if x % 2 == 0 else 'ODD' for x in numbers]",
                "rules_en": [
                    "Filtering (drop items): [expr for item in iterable if condition] placed at the end.",
                    "Ternary transformation (keep all items, alter values): [expr_true if condition else expr_false for item in iterable] placed at the beginning.",
                    "Do not confuse the position: trailing if filters out elements; leading if-else transforms elements."
                ],
                "rules_hi": [
                    "Filter karne ke liye trailing if aakhiri me lagta hai.",
                    "Value transform karne ke liye leading if-else shuru me lagta hai.",
                    "Trailing if me else nahi lagta; leading transform me else compulsory hai."
                ],
                "analogy_en": "Trailing if is a bouncer at a club gate turning away unauthorized guests. Leading if-else is a tailor handing jackets to men and shawls to women—everyone enters, but in different attire.",
                "analogy_hi": "Trailing if gatekeeper jaisa hai jo sirf valid ticket walo ko entry deta hai. Leading if-else prasad batne jaisa hai jahan sabko kuch milta hai—bade ko laddoo, chhote ko chocolate.",
                "common_mistakes": [
                    {
                        "mistake": "Writing [x for x in nums if x % 2 == 0 else 'ODD'] with else at the end.",
                        "why_it_fails_en": "SyntaxError: trailing filter condition cannot have an else branch.",
                        "why_it_fails_hi": "Trailing filter me else lagane par Python SyntaxError de deta hai.",
                        "fix": "Move x if x % 2 == 0 else 'ODD' to the beginning of the comprehension."
                    }
                ],
                "example_1": {
                    "title": "Filtering Even Numbers",
                    "title_hi": "Even numbers ko filter karna",
                    "code": "nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]\nevens = [x for x in nums if x % 2 == 0]\nprint('Evens:', evens)",
                    "expected_output": "Evens: [2, 4, 6, 8, 10]",
                    "explanation_en": "Trailing if filters out odd numbers, returning only elements where x % 2 == 0.",
                    "explanation_hi": "Trailing if condition sirf even numbers ko new list me daalta hai."
                },
                "example_2": {
                    "title": "Ternary Conditional Transformation",
                    "title_hi": "Leading if-else se label badalna",
                    "code": "nums = [1, 2, 3, 4, 5]\nlabels = ['EVEN' if x % 2 == 0 else 'ODD' for x in nums]\nprint('Labels:', labels)",
                    "expected_output": "Labels: ['ODD', 'EVEN', 'ODD', 'EVEN', 'ODD']",
                    "explanation_en": "Transforms every number into 'EVEN' or 'ODD' string label.",
                    "explanation_hi": "Har item ko replace karke EVEN ya ODD tag deta hai."
                },
                "challenge": {
                    "prompt_en": "From scores = [45, 82, 91, 30, 75, 58], filter out scores below 60 and add a 5-mark grace bonus to passing scores: [s + 5 for s in scores if s >= 60]. Print the result.",
                    "prompt_hi": "scores me se >= 60 wale filter karke +5 add karo aur print karo: [87, 96, 80]",
                    "starter_code": "scores = [45, 82, 91, 30, 75, 58]\n# Filter >= 60 and add 5 bonus marks:\n",
                    "expected_output": "[87, 96, 80]",
                    "solution_code": "scores = [45, 82, 91, 30, 75, 58]\nboosted_passes = [s + 5 for s in scores if s >= 60]\nprint(boosted_passes)",
                    "solution_explanation_en": "Filters s >= 60 and computes s + 5 for surviving items.",
                    "solution_explanation_hi": "Condition pass hone par +5 add karta hai.",
                    "hints": ["[s + 5 for s in scores if s >= 60]"],
                    "ego_roast_hi": "Grace marks dene me kanjoosi kar rahe ho?",
                    "ego_cheer_hi": "Filtering and transformation unlocked! 🎯"
                }
            },
            {
                "id": "ch19_sub3_dict_and_set_comprehensions",
                "title": "Dictionary and Set comprehensions",
                "title_hi": "Dictionary aur Set comprehensions",
                "icon": "📚",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Just like lists, Python allows creating dictionaries and sets directly using curly brace {} comprehension expressions.",
                "what_is_it_hi": "List ki tarah hi, Python curly brackets {} ka use karke direct dictionary ({k: v for ...}) aur set ({x for ...}) comprehensions banane ki suvidha deta hai.",
                "why_need_it_en": "Allows lightning-fast inversion of key-value mappings, deduplication of transformed sequences, and instant lookup table generation.",
                "why_need_it_hi": "Dictionary mapping ko invert karna, data ko transform karte hue duplicates hatana, ya fast lookup tables banana behad aasan ho jata hai.",
                "how_to_use_en": "Dict: {k: v for x in iterable}. Set: {x for x in iterable}.",
                "how_to_use_hi": "Dict: {k: v for x in iterable}. Set: {x for x in iterable}.",
                "syntax": "# Dict comprehension:\nsquares_dict = {x: x**2 for x in range(4)}\n# Set comprehension:\nunique_lengths = {len(w) for w in ['hi', 'bye', 'hi']}",
                "rules_en": [
                    "Dictionary comprehension syntax: {key_expr: val_expr for item in iterable}.",
                    "Set comprehension syntax: {expr for item in iterable} (no colon between key and value).",
                    "In set comprehensions, duplicate results are automatically and silently collapsed.",
                    "In dictionary comprehensions, duplicate keys overwrite previous values in left-to-right order."
                ],
                "rules_hi": [
                    "Dict comprehension syntax: {key_expr: val_expr for item in iterable} hota hai.",
                    "Set comprehension syntax: {expr for item in iterable} hota hai (colon nahi hota).",
                    "Set comprehension me duplicates automatically collapse ho jate hain.",
                    "Dict comprehension me duplicate key aane par purani value overwrite ho jati hai."
                ],
                "analogy_en": "A dictionary comprehension is like generating custom barcode tags for a catalog in one printing pass. A set comprehension is like dropping colored marbles into a sieve where duplicates fall away.",
                "analogy_hi": "Dict comprehension ek wholesale dukan ke price tag printer jaisa hai. Set comprehension unique stamp collection jaisa hai jahan duplicate stamp rakhne ki jagah hi nahi hoti.",
                "common_mistakes": [
                    {
                        "mistake": "Writing {x for x in nums} and expecting a dictionary.",
                        "why_it_fails_en": "Without a colon :, {x for x in ...} produces a set, not a dict.",
                        "why_it_fails_hi": "Bina colon ke curly brackets set banate hain, dictionary nahi.",
                        "fix": "Use {x: x*2 for x in nums} with key:value pairs for a dictionary."
                    }
                ],
                "example_1": {
                    "title": "Inverting Dictionary Key-Value Pairs",
                    "title_hi": "Dictionary mapping ko reverse karna",
                    "code": "students = {'Rohan': 101, 'Priya': 102, 'Amit': 103}\nid_to_name = {roll: name for name, roll in students.items()}\nprint('Inverted Dict:', id_to_name)",
                    "expected_output": "Inverted Dict: {101: 'Rohan', 102: 'Priya', 103: 'Amit'}",
                    "explanation_en": "Swaps key and value in a single expression using .items().",
                    "explanation_hi": "Key aur value ki position ek hi line me swap kar deta hai."
                },
                "example_2": {
                    "title": "Extracting Unique Word Lengths with Set Comprehension",
                    "title_hi": "Set comprehension se unique lengths nikalna",
                    "code": "words = ['python', 'code', 'data', 'algorithm', 'code', 'ai']\nunique_lengths = {len(w) for w in words}\nprint('Unique Lengths:', sorted(unique_lengths))",
                    "expected_output": "Unique Lengths: [2, 4, 6, 9]",
                    "explanation_en": "Set comprehension collapses duplicate word length integers automatically.",
                    "explanation_hi": "Duplicates ko automatically filter karke unique set return karta hai."
                },
                "challenge": {
                    "prompt_en": "Create a dictionary comprehension mapping each fruit in fruits = ['apple', 'banana', 'cherry'] to its character length: {f: len(f) for f in fruits}. Print the dict.",
                    "prompt_hi": "fruits = ['apple', 'banana', 'cherry'] ko unki length se map karke print karo: {'apple': 5, 'banana': 6, 'cherry': 6}",
                    "starter_code": "fruits = ['apple', 'banana', 'cherry']\n# Write dict comprehension:\n",
                    "expected_output": "{'apple': 5, 'banana': 6, 'cherry': 6}",
                    "solution_code": "fruits = ['apple', 'banana', 'cherry']\nlengths = {f: len(f) for f in fruits}\nprint(lengths)",
                    "solution_explanation_en": "Maps string key to integer length value in a dict comprehension.",
                    "solution_explanation_hi": "Har fruit ka naam key aur uski length value ban jati hai.",
                    "hints": ["{f: len(f) for f in fruits}"],
                    "ego_roast_hi": "Dictionary ke curly brackets bhool gaye?",
                    "ego_cheer_hi": "Dict comprehension master! 📚"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 20: Memory Efficiency (Iterators and Generators)
    # =========================================================================
    {
        "id": "ch20_iterators_and_generators",
        "part_number": 6,
        "part_title": "PART 6: THE PEAK (ADVANCED PYTHON CONCEPTS)",
        "chapter_number": 20,
        "title": "Chapter 20: Memory Efficiency (Iterators and Generators)",
        "subtitle_en": "Unlock infinite pipelines and stream massive datasets using lazy evaluation and CPython iterator protocols",
        "subtitle_hi": "Lazy evaluation aur yield se massive datasets bina RAM freeze ke stream karein",
        "icon": "⚡",
        "estimated_time": "50 mins",
        "prerequisites_en": "Parts 1 to 4 (Functions, loops, memory concepts).",
        "prerequisites_hi": "Part 1 se 4 tak (Functions, loops, memory).",
        "learning_objectives_en": [
            "Understand the Python Iterator Protocol (iter() and next())",
            "Create custom generators using the yield keyword",
            "Appreciate lazy evaluation and measure RAM savings compared to memory-heavy lists"
        ],
        "learning_objectives_hi": [
            "Python Iterator Protocol (__iter__ aur __next__) ko samjhein",
            "yield keyword se custom generator functions banayein",
            "Lazy evaluation se RAM consumption ko O(1) constant rakhein"
        ],
        "recap_en": "You mastered iterators and generators: how for loops work with iter() and next(), freezing execution state with yield, and streaming infinite datasets with constant O(1) memory.",
        "recap_hi": "Aapne iterators aur generators master kiye jo 10 GB ke data ko bhi 10 MB RAM me bina crash hue process karte hain.",
        "subtopics": [
            {
                "id": "ch20_sub1_iterables_vs_iterators",
                "title": "How for loops actually work under the hood (Iterables vs. Iterators)",
                "title_hi": "For loop under the hood kaise kaam karta hai (Iterables vs. Iterators)",
                "icon": "⚙️",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "An Iterable is an object capable of returning its members one at a time (implements __iter__()). An Iterator is the stateful stream object (implements __next__()) that remembers where it is during traversal and raises StopIteration when exhausted.",
                "what_is_it_hi": "Iterable wo object hai jisme se data nikala ja sakta hai (__iter__()), aur Iterator wo pointer object hai jo current position yaad rakhta hai aur next() call karne par agla item deta hai.",
                "why_need_it_en": "Understanding this protocol reveals how Python executes every for loop under the hood and allows building custom streams and infinite sequences.",
                "why_need_it_hi": "Is protocol ko samajhne se pata chalta hai ki Python ka for loop background me bina kisi index counter ke kaise smooth chalta hai.",
                "how_to_use_en": "Call it = iter(my_iterable) then val = next(it).",
                "how_to_use_hi": "Pehle it = iter(iterable) karein fir next(it) se ek ek item nikalein.",
                "syntax": "nums = [10, 20]\nit = iter(nums)\nprint(next(it))  # 10\nprint(next(it))  # 20\n# next(it) now raises StopIteration",
                "rules_en": [
                    "Calling iter(obj) invokes obj.__iter__() and returns an iterator.",
                    "Calling next(it) advances the iterator and returns the next element.",
                    "When no more items exist, next() raises a StopIteration exception.",
                    "A for loop automatically calls iter(), continuously calls next(), and catches StopIteration cleanly."
                ],
                "rules_hi": [
                    "iter(obj) call karne se iterator object milta hai.",
                    "next(it) call karne se agla item milta hai aur pointer aage badhta hai.",
                    "Jab saare elements khatam ho jayein, to StopIteration raise hota hai.",
                    "Python ka for loop ye saara process background me silently handle karta hai."
                ],
                "analogy_en": "An iterable is a book on a shelf. An iterator is a bookmark inside the book that knows exactly which page you are on right now and flips to the next page when asked.",
                "analogy_hi": "Iterable ek kitaab hai. Iterator kitaab ke andar rakha bookmark hai jo current page yaad rakhta hai aur agla panna palatne par agla shabd dikhata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to index an iterator like it[0] or expecting len(it).",
                        "why_it_fails_en": "Iterators do not know their total length and do not support random access indexing.",
                        "why_it_fails_hi": "Iterator indexing ya len() support nahi karta kyunki wo data stream hota hai.",
                        "fix": "Consume items using next() or a for loop, or convert to a list list(it)."
                    }
                ],
                "example_1": {
                    "title": "Manual Iteration with iter() and next()",
                    "title_hi": "iter() aur next() se manual iteration",
                    "code": "fruits = ['apple', 'banana', 'cherry']\nit = iter(fruits)\nprint(next(it))\nprint(next(it))\nprint(next(it))",
                    "expected_output": "apple\nbanana\ncherry",
                    "explanation_en": "Advances the iterator pointer one item at a time.",
                    "explanation_hi": "Har next() call pointer ko agle fruit par move karta hai."
                },
                "example_2": {
                    "title": "Simulating For-Loop Internals with While and StopIteration",
                    "title_hi": "For-loop ki internal working simulate karna",
                    "code": "numbers = [10, 20]\nit = iter(numbers)\nwhile True:\n    try:\n        val = next(it)\n        print('Consumed:', val)\n    except StopIteration:\n        print('Loop finished safely!')\n        break",
                    "expected_output": "Consumed: 10\nConsumed: 20\nLoop finished safely!",
                    "explanation_en": "Demonstrates how CPython catches StopIteration to terminate loops.",
                    "explanation_hi": "CPython StopIteration ko catch karke safely loop terminate karta hai."
                },
                "challenge": {
                    "prompt_en": "Create an iterator from the string word = 'PY' and print each character sequentially using next().",
                    "prompt_hi": "word = 'PY' ka iterator banakar next() se dono letters print karo: P fir Y.",
                    "starter_code": "word = 'PY'\n# Create iterator and call next() twice:\n",
                    "expected_output": "P\nY",
                    "solution_code": "word = 'PY'\nit = iter(word)\nprint(next(it))\nprint(next(it))",
                    "solution_explanation_en": "Calls next(it) twice to read 'P' then 'Y'.",
                    "solution_explanation_hi": "Iterator se ek ek character extract hota hai.",
                    "hints": ["it = iter(word); print(next(it)); print(next(it))"],
                    "ego_roast_hi": "P aur Y alag-alag print nahi kar pa rahe?",
                    "ego_cheer_hi": "Iterator protocol mastered! ⚙️"
                }
            },
            {
                "id": "ch20_sub2_generators_and_yield",
                "title": "Creating Generators using the yield keyword",
                "title_hi": "yield keyword se Generators create karna",
                "icon": "🌱",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "A Generator is a special type of function that uses the yield keyword instead of return. When yield is encountered, execution pauses, the current local state is preserved in RAM, and the yielded value is sent to the caller.",
                "what_is_it_hi": "Generator ek aisi function hoti hai jo return ki jagah yield keyword use karti hai. yield aate hi function pause ho jati hai, uska state freeze rehta hai, aur caller ko value mil jati hai.",
                "why_need_it_en": "Writing manual classes with __iter__ and __next__ requires extensive boilerplate code. Generator functions automatically implement the entire iterator protocol cleanly.",
                "why_need_it_hi": "Manual class me __iter__ aur __next__ likhna bohot boilerplate maangta hai. Generator function bina kisi extra code ke iterator protocol implement kar deta hai.",
                "how_to_use_en": "Define def my_gen(): yield value. Iterate over it using a for loop or next().",
                "how_to_use_hi": "Function me return ki jagah yield likhein. Fir loop me generator ko iterate karein.",
                "syntax": "def countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nfor val in countdown(3):\n    print(val)",
                "rules_en": [
                    "Any function containing the yield keyword becomes a generator factory.",
                    "Calling the function does NOT run the body immediately; it returns a generator object.",
                    "Each call to next() executes code until the next yield statement.",
                    "When the function finishes or encounters return, StopIteration is raised automatically."
                ],
                "rules_hi": [
                    "Jis function me yield ho wo turant run nahi hoti, generator object return karti hai.",
                    "Jab next() call hota hai tab code agle yield tak chalta hai aur pause ho jata hai.",
                    "Function ka local scope freeze rehta hai.",
                    "Code khatam hone par StopIteration raise hota hai."
                ],
                "analogy_en": "A standard function is a restaurant delivering 10 courses at once in cardboard boxes. A generator is a personal chef who cooks and serves course #1, pauses, and only cooks course #2 when you say 'next please'.",
                "analogy_hi": "Normal function ek delivery boy hai jo 50 packets ek saath room me phek deta hai. Generator ek water cooler dispenser jaisa hai—jab button dabao tabhi ek glass paani nikalta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Calling the generator function multiple times instead of saving the generator object: next(countdown(3)); next(countdown(3)).",
                        "why_it_fails_en": "Each call instantiates a fresh new generator starting from scratch at 3.",
                        "why_it_fails_hi": "Har baar function call karne par naya generator start hota hai jo hamesha 3 return karega.",
                        "fix": "Save the instance once: gen = countdown(3); next(gen); next(gen)."
                    }
                ],
                "example_1": {
                    "title": "Countdown Generator Function",
                    "title_hi": "Countdown generator function",
                    "code": "def countdown(n):\n    while n > 0:\n        yield n\n        n -= 1\n\nfor count in countdown(3):\n    print('T-minus:', count)",
                    "expected_output": "T-minus: 3\nT-minus: 2\nT-minus: 1",
                    "explanation_en": "yield pauses execution at each iteration, returning current n to the for loop.",
                    "explanation_hi": "yield har step par pause hoke current number bahar bhejta hai."
                },
                "example_2": {
                    "title": "Infinite Ticket ID Sequence Generator",
                    "title_hi": "Infinite sequence generator",
                    "code": "def ticket_generator(start=100):\n    curr = start\n    while True:\n        yield f'TICK-{curr}'\n        curr += 1\n\ngen = ticket_generator()\nprint(next(gen))\nprint(next(gen))\nprint(next(gen))",
                    "expected_output": "TICK-100\nTICK-101\nTICK-102",
                    "explanation_en": "Generates infinite unique sequential ticket IDs on demand without crashing RAM.",
                    "explanation_hi": "Infinite loop me bhi RAM freeze nahi hoti kyunki yield execution ko pause rakhta hai."
                },
                "challenge": {
                    "prompt_en": "Write a generator function even_numbers(limit) that yields all positive even numbers up to limit. Loop through even_numbers(6) and print each.",
                    "prompt_hi": "Generator even_numbers(limit) likho jo even numbers yield kare. even_numbers(6) ke liye 2, 4, 6 print karo.",
                    "starter_code": "def even_numbers(limit):\n    # Write generator logic:\n    pass\n\nfor val in even_numbers(6):\n    print(val)",
                    "expected_output": "2\n4\n6",
                    "solution_code": "def even_numbers(limit):\n    for num in range(2, limit + 1, 2):\n        yield num\n\nfor val in even_numbers(6):\n    print(val)",
                    "solution_explanation_en": "Yields even numbers from 2 to limit.",
                    "solution_explanation_hi": "range(2, limit+1, 2) se har even number yield hota hai.",
                    "hints": ["for num in range(2, limit + 1, 2): yield num"],
                    "ego_roast_hi": "yield lagana bhool gaye?",
                    "ego_cheer_hi": "Generator wizardry unlocked! 🌱"
                }
            },
            {
                "id": "ch20_sub3_generators_for_massive_data",
                "title": "Why generators are better for massive amounts of data",
                "title_hi": "Generators massive data ke liye kyu behtar hain",
                "icon": "📈",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "Generators practice lazy evaluation: values are generated on-the-fly one by one only when requested, consuming O(1) constant memory regardless of whether you process 10 items or 10 billion items.",
                "what_is_it_hi": "Generators lazy evaluation par kaam karte hain: memory me saara data pehle se load nahi hota, sirf wahi item banta hai jiski turant zaroorat hoti hai. RAM consumption hamesha constant O(1) rehta hai.",
                "why_need_it_en": "Loading a 50 GB log file or calculating millions of Fibonacci numbers as a list will trigger Out-Of-Memory (OOM) crashes. Generators allow processing limitless gigabytes smoothly.",
                "why_need_it_hi": "Bade files ya millions of rows ko list me load karne par RAM full hoke crash ho jayegi. Generator se 100 GB ka data bhi 15 MB RAM me stream hokar process ho jata hai.",
                "how_to_use_en": "Use generator expressions: total = sum(x for x in huge_stream).",
                "how_to_use_hi": "Generator expression use karein: sum(x for x in range(1000000)).",
                "syntax": "# Memory-heavy List (O(N) RAM):\nbig_list = [x for x in range(1000000)]\n# Memory-light Generator (O(1) RAM):\nbig_gen = (x for x in range(1000000))",
                "rules_en": [
                    "Lists store all elements eagerly in memory: memory complexity is O(N).",
                    "Generators evaluate lazily: memory complexity is O(1).",
                    "Use generator expressions (x for x in iterable) when you want comprehension syntax without memory allocation.",
                    "Pass generators directly to aggregate functions like sum(), max(), min() without surrounding brackets."
                ],
                "rules_hi": [
                    "List saare elements ko memory me turant store karti hai: Memory O(N) hoti hai.",
                    "Generator lazy evaluation karta hai: Memory O(1) constant hoti hai.",
                    "Round brackets (x for x in seq) lagane se generator expression banta hai.",
                    "sum(), min(), max() jaise functions me direct generator pass kiya ja sakta hai."
                ],
                "analogy_en": "A list of 1 million books requires building an enormous physical library warehouse today. A generator is an electronic on-demand printing press that prints only the single page you are reading.",
                "analogy_hi": "List ek godown jaisa hai jahan 10 lakh bricks rakhne ke liye bohot badi jagah chahiye. Generator ek brick machine hai jo jab mistry maangta hai tabhi ek nayi brick nikal kar deta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to iterate over a generator a second time after it has already been consumed.",
                        "why_it_fails_en": "Generators are one-time streams; once exhausted, they yield nothing on subsequent loops.",
                        "why_it_fails_hi": "Generator ek baar use hone ke baad khali ho jata hai aur dobara loop karne par kuch nahi deta.",
                        "fix": "Re-instantiate the generator or convert to a list if multiple passes over data are mandatory."
                    }
                ],
                "example_1": {
                    "title": "Measuring Memory Footprint with sys.getsizeof",
                    "title_hi": "List aur Generator ka RAM difference dekhna",
                    "code": "import sys\nlist_data = [x for x in range(10000)]\ngen_data = (x for x in range(10000))\nprint('List Memory (bytes):', sys.getsizeof(list_data) > 80000)\nprint('Gen Memory (bytes):', sys.getsizeof(gen_data) < 250)",
                    "expected_output": "List Memory (bytes): True\nGen Memory (bytes): True",
                    "explanation_en": "The list consumes tens of kilobytes; the generator takes under 250 bytes regardless of stream length.",
                    "explanation_hi": "List 80,000+ bytes leti hai jabki generator sirf ~200 bytes me pura stream handle karta hai."
                },
                "example_2": {
                    "title": "Streaming Aggregation with Generator Expressions",
                    "title_hi": "Generator expression se direct sum nikalna",
                    "code": "total = sum(x * x for x in range(1, 6))\nprint('Sum of squares:', total)",
                    "expected_output": "Sum of squares: 55",
                    "explanation_en": "Computes squares and accumulates the sum on the fly without building an intermediate list.",
                    "explanation_hi": "Bina temporary list banaye seedhe sum calculate kar leta hai."
                },
                "challenge": {
                    "prompt_en": "Use a generator expression with sum() to compute the sum of odd numbers between 1 and 20: sum(x for x in range(1, 21) if x % 2 != 0). Print the result: 100",
                    "prompt_hi": "Generator expression se 1 se 20 ke odd numbers ka sum nikal kar print karo: 100",
                    "starter_code": "# Compute sum of odd numbers from 1 to 20:\n",
                    "expected_output": "100",
                    "solution_code": "odd_sum = sum(x for x in range(1, 21) if x % 2 != 0)\nprint(odd_sum)",
                    "solution_explanation_en": "Lazily filters odd numbers and sums them to 100.",
                    "solution_explanation_hi": "Generator stream se seedha sum 100 mil jata hai.",
                    "hints": ["sum(x for x in range(1, 21) if x % 2 != 0)"],
                    "ego_roast_hi": "Generator me square brackets laga diye kya?",
                    "ego_cheer_hi": "Memory optimization champion! 📈"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 21: Function Modifiers (Decorators)
    # =========================================================================
    {
        "id": "ch21_function_modifiers_decorators",
        "part_number": 6,
        "part_title": "PART 6: THE PEAK (ADVANCED PYTHON CONCEPTS)",
        "chapter_number": 21,
        "title": "Chapter 21: Function Modifiers (Decorators)",
        "subtitle_en": "Supercharge functions by adding cross-cutting logging, timing, validation, and authentication with zero code pollution",
        "subtitle_hi": "Functions ke upar @decorator lagakar timing, logging aur security inject karein",
        "icon": "🎀",
        "estimated_time": "55 mins",
        "prerequisites_en": "Parts 1 to 4 (Functions, scope LEGB, closures).",
        "prerequisites_hi": "Part 1 se 4 tak (Functions, scope, closures).",
        "learning_objectives_en": [
            "Treat functions as first-class citizens (pass, return, and assign functions)",
            "Create closure-based decorator functions that wrap existing logic",
            "Apply the @decorator_name syntax sugar cleanly with functools.wraps",
            "Build real-world production decorators for execution timing and access control"
        ],
        "learning_objectives_hi": [
            "Functions ko first-class citizen ki tarah pass aur return karna samjhein",
            "Closure-based decorator functions banayein jo target code ko wrap karein",
            "@decorator syntax aur functools.wraps ka use master karein",
            "Timing aur authorization ke real-world production decorators banayein"
        ],
        "recap_en": "You mastered decorators: higher-order functions, wrapping behaviors with inner wrappers, using @decorator pie syntax, preserving metadata with functools.wraps, and securing endpoints.",
        "recap_hi": "Aapne decorators master kiye jo code duplication khatam karte hain aur clean production-grade architecture banate hain.",
        "subtopics": [
            {
                "id": "ch21_sub1_first_class_citizens",
                "title": "Functions as \"First-Class Citizens\" (Passing functions into functions)",
                "title_hi": "Functions \"First-Class Citizens\" ki tarah (Functions ko functions me pass karna)",
                "icon": "👑",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "In Python, functions are first-class citizens: they are real objects in memory that can be assigned to variables, passed as arguments to other functions, returned from functions, and stored in data structures.",
                "what_is_it_hi": "Python me functions 'first-class citizens' hoti hain: yaani functions bhi regular objects hain jinhe variable me store kiya ja sakta hai, dusri functions me pass kiya ja sakta hai, aur return kiya ja sakta hai.",
                "why_need_it_en": "This is the architectural bedrock of functional programming and makes powerful constructs like decorators, callbacks, and high-order functions possible.",
                "why_need_it_hi": "Ye functional programming ka foundation hai. Iski wajah se hum decorators, callbacks, aur event listeners jaisi advanced capabilities implement kar pate hain.",
                "how_to_use_en": "Pass function reference without parentheses: apply(my_func, arg).",
                "how_to_use_hi": "Bina parentheses ke function ka naam pass karein: do_task(my_func).",
                "syntax": "def shout(text): return text.upper()\ndef speak(func, msg): return func(msg)\nprint(speak(shout, 'hello'))  # 'HELLO'",
                "rules_en": [
                    "Referencing a function without parentheses func refers to the function object itself.",
                    "Using parentheses func() executes the function.",
                    "A function that accepts or returns another function is called a Higher-Order Function.",
                    "Inner functions defined inside an outer function can access outer variables (Closures)."
                ],
                "rules_hi": [
                    "Bina bracket func likhne par function object ka reference milta hai.",
                    "Bracket func() lagane par function execute hoti hai.",
                    "Jo function kisi dusri function ko input leti hai ya return karti hai, use Higher-Order Function kehte hain.",
                    "Inner function outer scope ke variables ko access kar sakti hai (Closure)."
                ],
                "analogy_en": "Treating a function like a first-class citizen is like passing around a master recipe card rather than serving the cooked dish. You can hand the recipe to another chef or photocopy it.",
                "analogy_hi": "Function ko object ki tarah treat karna kisi dish ki recipe card jaisa hai. Pura khana serve karne ke bajay recipe card doosre cook ko de sakte hain.",
                "common_mistakes": [
                    {
                        "mistake": "Passing deliver_message(greet(), 'Rohan') with parentheses.",
                        "why_it_fails_en": "Executes greet() immediately with missing arguments instead of passing the function object.",
                        "why_it_fails_hi": "Parentheses lagane se function turant execute ho jata hai jabki hume uska reference pass karna tha.",
                        "fix": "Omit the parentheses: deliver_message(greet, 'Rohan')."
                    }
                ],
                "example_1": {
                    "title": "Passing Functions as Arguments",
                    "title_hi": "Function ko argument ki tarah pass karna",
                    "code": "def greet(name):\n    return f'Hello, {name}!'\n\ndef formal_greet(name):\n    return f'Good day, {name}.'\n\ndef deliver_message(greeting_fn, recipient):\n    return greeting_fn(recipient)\n\nprint(deliver_message(greet, 'Rohan'))\nprint(deliver_message(formal_greet, 'Dr. Sharma'))",
                    "expected_output": "Hello, Rohan!\nGood day, Dr. Sharma.",
                    "explanation_en": "deliver_message dynamically calls whichever function object is supplied to it.",
                    "explanation_hi": "deliver_message pass kiye gaye function ko execute karke result return karta hai."
                },
                "example_2": {
                    "title": "Function Factory Returning Inner Functions",
                    "title_hi": "Function factory jo nayi function return kare",
                    "code": "def multiplier(factor):\n    def multiply(n):\n        return n * factor\n    return multiply\n\ndouble = multiplier(2)\ntriple = multiplier(3)\nprint('Double 5:', double(5))\nprint('Triple 5:', triple(5))",
                    "expected_output": "Double 5: 10\nTriple 5: 15",
                    "explanation_en": "multiplier generates customized closure functions retaining factor in memory.",
                    "explanation_hi": "multiplier factor ko yaad rakhne wali customized multiply functions banata hai."
                },
                "challenge": {
                    "prompt_en": "Write a function apply_twice(func, value) that applies func to value twice: func(func(value)). Test with def square(n): return n*n on 3 to print 81.",
                    "prompt_hi": "apply_twice(func, value) banao jo func ko do baar chalaye: func(func(value)). square(3) par 81 print karo.",
                    "starter_code": "def square(n):\n    return n * n\n\ndef apply_twice(func, value):\n    # Apply func twice:\n    pass\n\nprint(apply_twice(square, 3))",
                    "expected_output": "81",
                    "solution_code": "def square(n):\n    return n * n\n\ndef apply_twice(func, value):\n    return func(func(value))\n\nprint(apply_twice(square, 3))",
                    "solution_explanation_en": "Applies square(square(3)) = square(9) = 81.",
                    "solution_explanation_hi": "square ko do baar chala kar 81 return karta hai.",
                    "hints": ["return func(func(value))"],
                    "ego_roast_hi": "Function ke andar function pass karna nahi aaya?",
                    "ego_cheer_hi": "First-class citizen mastery achieved! 👑"
                }
            },
            {
                "id": "ch21_sub2_creating_basic_decorator",
                "title": "Creating a basic decorator (Wrapping code around a function)",
                "title_hi": "Basic decorator create karna (Function ke aage-peeche code wrap karna)",
                "icon": "📦",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "A decorator is a function that takes an existing target function as an argument, extends or wraps its behavior with extra code before and after execution, and returns a new replacement wrapper function.",
                "what_is_it_hi": "Decorator ek aisi function hai jo kisi existing function ko input leti hai, uske aage-peeche extra code wrap karti hai, aur ek naya wrapper function return karti hai.",
                "why_need_it_en": "Enforces the Don't Repeat Yourself (DRY) principle by letting you inject universal behavior (like logging, authentication, or timing) without modifying the original function's source code.",
                "why_need_it_hi": "Bina original function ka code chhede usme universal features jaise logging, timing ya authentication add karne ke liye decorator use hota hai.",
                "how_to_use_en": "Define outer decorator accepting func, inner wrapper(*args, **kwargs) that calls func, and return wrapper.",
                "how_to_use_hi": "Outer function me func lein, inner wrapper banayein jo extra kaam karke func call kare, aur wrapper return karein.",
                "syntax": "def my_dec(func):\n    def wrapper(*args, **kwargs):\n        print('Before')\n        res = func(*args, **kwargs)\n        print('After')\n        return res\n    return wrapper",
                "rules_en": [
                    "A decorator defines an internal wrapper function def wrapper(*args, **kwargs): ....",
                    "The wrapper performs actions, calls the original target function, and returns the result.",
                    "The decorator returns the wrapper function object.",
                    "Use *args, **kwargs inside the wrapper so it can wrap functions with any signature."
                ],
                "rules_hi": [
                    "Decorator ke andar ek internal wrapper(*args, **kwargs) function banti hai.",
                    "Wrapper extra kaam karta hai, original function ko call karta hai, aur result return karta hai.",
                    "Decorator hamesha wrapper function object ko return karta hai.",
                    "*args, **kwargs use karne se decorator kisi bhi argument signature ke saath chal sakta hai."
                ],
                "analogy_en": "A decorator is like putting a gift into a decorative box with wrapping paper and a ribbon. The actual gift inside hasn't changed, but it now has protective packaging around it.",
                "analogy_hi": "Decorator ek mobile phone ke upar lagaye gaye protective case jaisa hai. Phone ka hardware wahi rehta hai, lekin bahar se extra safety jud jati hai.",
                "common_mistakes": [
                    {
                        "mistake": "Forgetting to return result from inside the wrapper function.",
                        "why_it_fails_en": "Causes the decorated function to unexpectedly return None to the caller.",
                        "why_it_fails_hi": "Wrapper se return karna bhoolne par function hamesha None return karegi.",
                        "fix": "Always capture result = func(*args, **kwargs) and return result from wrapper."
                    }
                ],
                "example_1": {
                    "title": "Basic Wrapper Execution Flow",
                    "title_hi": "Wrapper function ka basic flow",
                    "code": "def my_decorator(func):\n    def wrapper():\n        print('[Before] Starting execution...')\n        func()\n        print('[After] Execution complete!')\n    return wrapper\n\ndef say_hi():\n    print('Hello World!')\n\ndecorated_say_hi = my_decorator(say_hi)\ndecorated_say_hi()",
                    "expected_output": "[Before] Starting execution...\nHello World!\n[After] Execution complete!",
                    "explanation_en": "Executes before/after code around the wrapped say_hi function.",
                    "explanation_hi": "say_hi ke pehle aur baad me extra print chalata hai."
                },
                "example_2": {
                    "title": "Universal Wrapper with *args and **kwargs",
                    "title_hi": "*args aur **kwargs wala universal wrapper",
                    "code": "def announce(func):\n    def wrapper(*args, **kwargs):\n        print(f'[CALL] Executing {func.__name__}...')\n        result = func(*args, **kwargs)\n        print(f'[DONE] {func.__name__} returned {result}')\n        return result\n    return wrapper\n\ndef add(a, b):\n    return a + b\n\nwrapped_add = announce(add)\nprint('Output:', wrapped_add(10, 20))",
                    "expected_output": "[CALL] Executing add...\n[DONE] add returned 30\nOutput: 30",
                    "explanation_en": "Accepts any positional or keyword parameters and logs function entry and exit.",
                    "explanation_hi": "Parameters ko preserve karke execution log banata hai."
                },
                "challenge": {
                    "prompt_en": "Create a decorator uppercase_decorator(func) that converts the returned string of get_greeting() to uppercase. Print the result: HELLO, DEVELOPERS!",
                    "prompt_hi": "uppercase_decorator(func) banao jo return text ko .upper() me convert kare: HELLO, DEVELOPERS!",
                    "starter_code": "def uppercase_decorator(func):\n    def wrapper():\n        # Modify return value to upper:\n        pass\n    return wrapper\n\ndef get_greeting():\n    return 'hello, developers!'\n\ndecorated = uppercase_decorator(get_greeting)\nprint(decorated())",
                    "expected_output": "HELLO, DEVELOPERS!",
                    "solution_code": "def uppercase_decorator(func):\n    def wrapper():\n        res = func()\n        return res.upper()\n    return wrapper\n\ndef get_greeting():\n    return 'hello, developers!'\n\ndecorated = uppercase_decorator(get_greeting)\nprint(decorated())",
                    "solution_explanation_en": "Wrapper intercepts the returned string and calls .upper() on it.",
                    "solution_explanation_hi": "Original return value par .upper() laga kar return karta hai.",
                    "hints": ["res = func(); return res.upper()"],
                    "ego_roast_hi": "res.upper() karna bhool gaye?",
                    "ego_cheer_hi": "Decorator wrapper mastered! 📦"
                }
            },
            {
                "id": "ch21_sub3_decorator_syntax",
                "title": "Using the @decorator_name syntax",
                "title_hi": "@decorator_name syntax use karna",
                "icon": "✨",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Python provides the @decorator_name syntax placed directly above a function definition, which automatically executes target_func = decorator_name(target_func) at definition time.",
                "what_is_it_hi": "Python function definition ke theek upar @decorator_name syntax allow karta hai, jo automatically target_func = decorator_name(target_func) execute kar deta hai.",
                "why_need_it_en": "Eliminates messy manual re-assignment and makes it immediately obvious to anyone reading the code that the function is being wrapped.",
                "why_need_it_hi": "Function ko manually re-assign karne ka jhanjhat khatam ho jata hai aur code padhte hi pata chal jata hai ki is par kya behavior laga hai.",
                "how_to_use_en": "Add @my_decorator on the line preceding def my_func():.",
                "how_to_use_hi": "def my_func(): se theek pehle @my_decorator likhein.",
                "syntax": "import functools\n\ndef my_dec(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        return func(*args, **kwargs)\n    return wrapper\n\n@my_dec\ndef hello(): return 'Hi!'",
                "rules_en": [
                    "Place @decorator_name on the line immediately preceding def function_name(...).",
                    "Use functools.wraps on the wrapper function so that the original function's __name__ and __doc__ docstrings are preserved.",
                    "Multiple decorators can be stacked: @dec1 above @dec2 applies bottom-up: dec1(dec2(func))."
                ],
                "rules_hi": [
                    "@decorator_name ko function definition ke theek upar wali line par likhein.",
                    "Wrapper par functools.wraps(func) lagana chahiye taaki original function ka naam aur docstring barkarar rahe.",
                    "Ek ke upar ek multiple decorators lagaye ja sakte hain (bottom-up order me chalte hain)."
                ],
                "analogy_en": "The @ decorator syntax is like stamping an official certification seal directly on top of an application form before it leaves the front desk.",
                "analogy_hi": "Document ke upar official stamp lagane jaisa hai. Jaise hi application sign hoti hai, stamp batata hai ki ye pre-approved hai.",
                "common_mistakes": [
                    {
                        "mistake": "Omitting @functools.wraps(func).",
                        "why_it_fails_en": "The decorated function loses its identity and func.__name__ displays as 'wrapper' in stack traces and debuggers.",
                        "why_it_fails_hi": "Original function ka naam gayab hoke 'wrapper' ban jata hai jisse debugging mushkil ho jati hai.",
                        "fix": "Always decorate your inner wrapper with @functools.wraps(func)."
                    }
                ],
                "example_1": {
                    "title": "Idiomatic @decorator Syntax with functools.wraps",
                    "title_hi": "functools.wraps ke saath @decorator syntax",
                    "code": "import functools\n\ndef bold_text(func):\n    @functools.wraps(func)\n    def wrapper(*args, **kwargs):\n        return f'<b>{func(*args, **kwargs)}</b>'\n    return wrapper\n\n@bold_text\ndef message(text):\n    return text\n\nprint(message('Elysia Code'))\nprint('Function name preserved:', message.__name__)",
                    "expected_output": "<b>Elysia Code</b>\nFunction name preserved: message",
                    "explanation_en": "functools.wraps preserves the original function's __name__ attribute.",
                    "explanation_hi": "wraps use karne se function ka original name message hi rehta hai."
                },
                "example_2": {
                    "title": "Stacking Multiple Decorators",
                    "title_hi": "Ek ke upar ek multiple decorators lagana",
                    "code": "def star_banner(func):\n    def wrapper(*args, **kwargs):\n        return f'*** {func(*args, **kwargs)} ***'\n    return wrapper\n\ndef quote_tag(func):\n    def wrapper(*args, **kwargs):\n        return f'\"{func(*args, **kwargs)}\"'\n    return wrapper\n\n@star_banner\n@quote_tag\ndef get_title():\n    return 'Python Peak'\n\nprint(get_title())",
                    "expected_output": "*** \"Python Peak\" ***",
                    "explanation_en": "Decorators apply bottom-up: quote_tag wraps get_title first, then star_banner wraps the result.",
                    "explanation_hi": "Pehle quote_tag lagta hai fir bahar star_banner lagta hai."
                },
                "challenge": {
                    "prompt_en": "Create a decorator add_brackets that wraps any string-returning function in square brackets: f'[{func(*args, **kwargs)}]'. Decorate def get_user(): return 'Admin' and print: [Admin]",
                    "prompt_hi": "add_brackets decorator banao jo result ko square brackets me daale: [Admin]",
                    "starter_code": "def add_brackets(func):\n    def wrapper(*args, **kwargs):\n        # Return wrapped string:\n        pass\n    return wrapper\n\n@add_brackets\ndef get_user():\n    return 'Admin'\n\nprint(get_user())",
                    "expected_output": "[Admin]",
                    "solution_code": "def add_brackets(func):\n    def wrapper(*args, **kwargs):\n        return f'[{func(*args, **kwargs)}]'\n    return wrapper\n\n@add_brackets\ndef get_user():\n    return 'Admin'\n\nprint(get_user())",
                    "solution_explanation_en": "Wraps the return value inside square brackets.",
                    "solution_explanation_hi": "Square brackets me format karke return karta hai.",
                    "hints": ["return f'[{func(*args, **kwargs)}]'"],
                    "ego_roast_hi": "Brackets lagana bhool gaye?",
                    "ego_cheer_hi": "Pie syntax @ mastered! ✨"
                }
            },
            {
                "id": "ch21_sub4_practical_uses_of_decorators",
                "title": "Practical uses of decorators (Timing functions, checking passwords)",
                "title_hi": "Decorators ke practical uses (Timing functions, checking passwords)",
                "icon": "⏱️",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "Real-world production engineering uses decorators for benchmarking performance, rate limiting, logging database queries, caching results (lru_cache), and enforcing role-based access control.",
                "what_is_it_hi": "Production software me decorators ka use execution time measure karne, access check karne, database query logs maintain karne aur slow calculations ko cache karne ke liye hota hai.",
                "why_need_it_en": "Keeps business logic clean and isolated from infrastructural concerns like telemetry, metrics, and security authorization checks.",
                "why_need_it_hi": "Security aur performance checks ko core business logic se alag rakhta hai, jisse code maintainable rehta hai.",
                "how_to_use_en": "Measure elapsed time using time.perf_counter() or verify authentication claims before calling the target function.",
                "how_to_use_hi": "time.perf_counter() se elapsed time measure karein ya permissions check karke function call karein.",
                "syntax": "def check_auth(func):\n    def wrapper(role, *args):\n        if role != 'admin': return 'Denied'\n        return func(role, *args)\n    return wrapper",
                "rules_en": [
                    "Execution timing: measure start = time.perf_counter() before func() and time.perf_counter() - start after.",
                    "Authentication/Access control: check permissions inside wrapper before deciding whether to call func().",
                    "Never perform blocking heavy I/O operations inside decorators that shouldn't run on every call."
                ],
                "rules_hi": [
                    "Timer decorator me time.perf_counter() use karke difference calculate kiya jata hai.",
                    "Auth decorator me condition fail hone par function chalne se pehle hi block kar diya jata hai.",
                    "Decorator ke andar unnecessary heavy operations avoid karein."
                ],
                "analogy_en": "An access-control decorator is a security guard with an RFID scanner at an office turnstile. Only employees with valid badges can trigger the elevator.",
                "analogy_hi": "Security decorator building ke gate par baithe guard jaisa hai jo entry register check karta hai—pass valid hai to hi room me entry milti hai.",
                "common_mistakes": [
                    {
                        "mistake": "Using time.time() instead of time.perf_counter() for benchmarking.",
                        "why_it_fails_en": "time.time() can jump backwards if the system clock adjusts; perf_counter provides highest-resolution monotonic time.",
                        "why_it_fails_hi": "time.time() system clock update hone par galat reading deta hai, perf_counter hamesha accurate monotonic time deta hai.",
                        "fix": "Always use time.perf_counter() for measuring elapsed execution time."
                    }
                ],
                "example_1": {
                    "title": "Performance Execution Benchmark Decorator",
                    "title_hi": "Execution timing measure karne wala decorator",
                    "code": "import time\n\ndef measure_time(func):\n    def wrapper(*args, **kwargs):\n        start = time.perf_counter()\n        result = func(*args, **kwargs)\n        elapsed = time.perf_counter() - start\n        print(f'{func.__name__} finished (benchmarked: {elapsed >= 0})')\n        return result\n    return wrapper\n\n@measure_time\ndef compute_sum(n):\n    return sum(range(n))\n\nprint('Total:', compute_sum(100000) > 0)",
                    "expected_output": "compute_sum finished (benchmarked: True)\nTotal: True",
                    "explanation_en": "Measures elapsed high-resolution execution time before and after function invocation.",
                    "explanation_hi": "Function run hone se pehle aur baad ka exact time calculate karta hai."
                },
                "example_2": {
                    "title": "Role-Based Access Control Guard",
                    "title_hi": "Security guard decorator",
                    "code": "def require_admin(func):\n    def wrapper(user_role, *args, **kwargs):\n        if user_role != 'admin':\n            print('ACCESS DENIED: Admins only!')\n            return None\n        return func(user_role, *args, **kwargs)\n    return wrapper\n\n@require_admin\ndef delete_database(user_role):\n    return 'Database deleted successfully.'\n\nprint(delete_database('guest'))\nprint(delete_database('admin'))",
                    "expected_output": "ACCESS DENIED: Admins only!\nNone\nDatabase deleted successfully.",
                    "explanation_en": "Rejects non-admin users before executing the sensitive database destruction function.",
                    "explanation_hi": "Guest role aane par function chalne se pehle hi Access Denied kar deta hai."
                },
                "challenge": {
                    "prompt_en": "Create an authentication decorator verify_pin that checks pin == 1234 before executing withdraw(pin, amount). If wrong, print 'WRONG PIN' and return None. Test with withdraw(9999, 100) and withdraw(1234, 500).",
                    "prompt_hi": "verify_pin decorator banao jo pin == 1234 check kare. Galat pin par 'WRONG PIN' print kare. withdraw(9999, 100) aur withdraw(1234, 500) print karein.",
                    "starter_code": "def verify_pin(func):\n    def wrapper(pin, amount):\n        # Check pin == 1234:\n        pass\n    return wrapper\n\n@verify_pin\ndef withdraw(pin, amount):\n    return f'Withdrew ${amount}'\n\nprint(withdraw(9999, 100))\nprint(withdraw(1234, 500))",
                    "expected_output": "WRONG PIN\nNone\nWithdrew $500",
                    "solution_code": "def verify_pin(func):\n    def wrapper(pin, amount):\n        if pin == 1234:\n            return func(pin, amount)\n        print('WRONG PIN')\n        return None\n    return wrapper\n\n@verify_pin\ndef withdraw(pin, amount):\n    return f'Withdrew ${amount}'\n\nprint(withdraw(9999, 100))\nprint(withdraw(1234, 500))",
                    "solution_explanation_en": "Guards withdrawal with a 4-digit PIN verification check.",
                    "solution_explanation_hi": "PIN match hone par hi withdrawal execute hoti hai.",
                    "hints": ["if pin == 1234: return func(pin, amount) else: print('WRONG PIN'); return None"],
                    "ego_roast_hi": "ATM ka PIN bhool gaye kya?",
                    "ego_cheer_hi": "Security decorator guard active! 🛡️"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 22: Resource Management (Context Managers)
    # =========================================================================
    {
        "id": "ch22_resource_management_context_managers",
        "part_number": 6,
        "part_title": "PART 6: THE PEAK (ADVANCED PYTHON CONCEPTS)",
        "chapter_number": 22,
        "title": "Chapter 22: Resource Management (Context Managers)",
        "subtitle_en": "Guarantee bulletproof resource allocation and cleanup for files, database locks, and sockets with the with statement",
        "subtitle_hi": "with statement, __enter__/__exit__ aur contextlib se safe resource management",
        "icon": "🛡️",
        "estimated_time": "45 mins",
        "prerequisites_en": "Parts 1 to 5 (Classes and OOP, generators, exception handling).",
        "prerequisites_hi": "Part 1 se 5 tak (Classes, generators, exceptions).",
        "learning_objectives_en": [
            "Understand the mechanics of Python's with statement",
            "Implement class-based context managers using __enter__ and __exit__",
            "Construct lightweight generator context managers using contextlib.contextmanager"
        ],
        "learning_objectives_hi": [
            "Python ke with statement ke internal mechanics ko samjhein",
            "Class-based context managers (__enter__ aur __exit__) implement karein",
            "contextlib.contextmanager se lightweight generator context managers banayein"
        ],
        "recap_en": "You mastered context managers: leak-proof resource management, implementing __enter__ and __exit__, suppressing exceptions, and creating clean generator managers with contextlib.",
        "recap_hi": "Aapne context managers master kiye jo file leaks, database locks aur dangling sockets ko safely cleanup karte hain.",
        "subtopics": [
            {
                "id": "ch22_sub1_how_with_really_works",
                "title": "How the with statement really works",
                "title_hi": "with statement really kaise kaam karta hai",
                "icon": "🔒",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "The with statement encapsulates common try...finally cleanup patterns in a clean syntactic block, ensuring that system resources like files, network sockets, and database transactions are always safely closed or released.",
                "what_is_it_hi": "with statement Python me resource management ka sabse safe tarika hai. Ye ensure karta hai ki file ya socket open hone ke baad safely close ho jaye, chahe code me beech me koi exception kyu na aa jaye.",
                "why_need_it_en": "Without with, unexpected runtime crashes or unhandled exceptions cause resource leaks (e.g., locked file handles, uncommitted transactions, exhausted OS descriptors).",
                "why_need_it_hi": "Bina with ke agar program crash ho jaye to file open reh jati hai aur operating system ke descriptors leak ho jate hain.",
                "how_to_use_en": "Use with resource as var: ...",
                "how_to_use_hi": "with resource as var: ... use karein.",
                "syntax": "# Safe file management with 'with':\nwith open('data.txt', 'w') as f:\n    f.write('Hello safe files!')\n# File is automatically closed here!",
                "rules_en": [
                    "The target object in with expression as var: must implement the Context Management Protocol.",
                    "Python enters the block by calling __enter__() and assigns its return value to var.",
                    "When execution exits the block (normally or via error), Python always calls __exit__().",
                    "If an exception occurs inside the block, its type, value, and traceback are passed to __exit__()."
                ],
                "rules_hi": [
                    "Object ke paas Context Management Protocol (__enter__ aur __exit__) hona zaroori hai.",
                    "Block shuru hote hi __enter__() run hota hai aur result as variable ko assign hota hai.",
                    "Block khatam hote hi bina kisi fail ke __exit__() call hota hai.",
                    "Agar koi error aaye, to __exit__() ko error details receive hoti hain."
                ],
                "analogy_en": "Entering a secure vault: the guard scans your badge upon entry (__enter__), and no matter what happens inside—even if the power cuts—the mechanical door locks and logs you out when leaving (__exit__).",
                "analogy_hi": "Hotel room ka smart key card: jab aap enter karte hain light on hoti hai (__enter__), aur card nikalne par saari lights automatically band ho jati hain (__exit__).",
                "common_mistakes": [
                    {
                        "mistake": "Believing that variable created with as var only exists inside the with block.",
                        "why_it_fails_en": "Python with blocks do not create a local variable scope; var remains accessible outside the block.",
                        "why_it_fails_hi": "with block naya scope nahi banata, variable bahar bhi accessible rehta hai (par file close ho chuki hoti hai).",
                        "fix": "Be mindful that while var exists outside, the underlying stream/file is closed."
                    }
                ],
                "example_1": {
                    "title": "Safe File Operations with Automatic Cleanup",
                    "title_hi": "Automatic cleanup ke saath file operation",
                    "code": "import os\n\nwith open('temp_test.txt', 'w') as f:\n    f.write('Safe resource handling in Python!')\n\nprint('File closed status:', f.closed)\nos.remove('temp_test.txt')",
                    "expected_output": "File closed status: True",
                    "explanation_en": "Guarantees that f.closed is True immediately upon exiting the with block.",
                    "explanation_hi": "with block se nikalte hi file automatically closed ho jati hai."
                },
                "example_2": {
                    "title": "Resource Cleanup During Simulated Crash",
                    "title_hi": "Crash ke dauran bhi guaranteed cleanup",
                    "code": "class MockResource:\n    def __enter__(self):\n        print('[OPEN] Resource allocated')\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        print('[CLOSE] Resource released safely')\n        return True\n\nwith MockResource():\n    print('Doing risky operation...')\n    raise RuntimeError('Simulated crash')",
                    "expected_output": "[OPEN] Resource allocated\nDoing risky operation...\n[CLOSE] Resource released safely",
                    "explanation_en": "Even when a RuntimeError is raised, __exit__ is called reliably.",
                    "explanation_hi": "Error aane ke bawjood __exit__ bina kisi rukawat ke safely close karta hai."
                },
                "challenge": {
                    "prompt_en": "Does Python's 'with' statement guarantee closing a file even if an exception occurs? Print 'YES'.",
                    "prompt_hi": "Kya 'with' statement error aane par bhi file close karne ki guarantee deta hai? Print 'YES'.",
                    "starter_code": "# Print YES if guaranteed:\n",
                    "expected_output": "YES",
                    "solution_code": "print('YES')",
                    "solution_explanation_en": "The with statement guarantees executing __exit__ on all exit paths.",
                    "solution_explanation_hi": "with statement hamesha __exit__ chalata hai.",
                    "hints": ["print('YES')"],
                    "ego_roast_hi": "Resource cleanup par shaq hai?",
                    "ego_cheer_hi": "Resource management verified! 🛡️"
                }
            },
            {
                "id": "ch22_sub2_custom_context_managers_classes",
                "title": "Creating your own context managers using classes (__enter__ and __exit__)",
                "title_hi": "Classes se custom context managers banana (__enter__ aur __exit__)",
                "icon": "🏗️",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "You can turn any custom class into a context manager by defining two special magic dunder methods: __enter__(self) and __exit__(self, exc_type, exc_val, exc_tb).",
                "what_is_it_hi": "Aap kisi bhi custom class ko context manager bana sakte hain bas usme do magic methods define karne hote hain: __enter__ aur __exit__.",
                "why_need_it_en": "Ideal for managing custom resources such as temporary database connections, high-precision performance timers, and thread synchronization locks.",
                "why_need_it_hi": "Custom resources jaise database connections, stopwatch timers ya temporary configuration switches ko manage karne ke liye ye best pattern hai.",
                "how_to_use_en": "Define class with def __enter__(self): and def __exit__(self, exc_type, exc_val, exc_tb):.",
                "how_to_use_hi": "Class ke andar __enter__(self) aur __exit__(self, exc_type, exc_val, exc_tb) methods likhein.",
                "syntax": "class MyResource:\n    def __enter__(self):\n        print('Acquired')\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        print('Released')\n        return False",
                "rules_en": [
                    "__enter__(self): setups resources and returns the object to be bound to the as target.",
                    "__exit__(self, exc_type, exc_val, exc_tb): receives exception info if an error occurred, or None, None, None on normal exit.",
                    "If __exit__ returns True, the exception is swallowed and suppressed; returning False propagates the exception upwards."
                ],
                "rules_hi": [
                    "__enter__(self): setup karta hai aur return value as variable ko milti hai.",
                    "__exit__(self, exc_type, exc_val, exc_tb): cleanup karta hai.",
                    "Agar __exit__ True return kare to error suppress ho jata hai; False return kare to error normal raise hota hai."
                ],
                "analogy_en": "A rental car contract: __enter__ hands you the car keys and starts the billing meter; __exit__ inspects the vehicle for dents, settles the bill, and returns the keys.",
                "analogy_hi": "Rent par camera lene jaisa: __enter__ par security deposit jama hota hai aur camera milta hai, __exit__ par camera return hota hai aur deposit wapas mil jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Defining __exit__ with only self as a parameter.",
                        "why_it_fails_en": "Raises TypeError: __exit__ takes 1 positional argument but 4 were given.",
                        "why_it_fails_hi": "Python __exit__ ko 4 arguments deta hai (self, exc_type, exc_val, exc_tb), sirf self likhne par crash ho jayega.",
                        "fix": "Always declare def __exit__(self, exc_type, exc_val, exc_tb):."
                    }
                ],
                "example_1": {
                    "title": "Stopwatch Timer Context Manager",
                    "title_hi": "Execution stopwatch timer",
                    "code": "import time\n\nclass Timer:\n    def __enter__(self):\n        self.start = time.perf_counter()\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        self.elapsed = time.perf_counter() - self.start\n        print(f'Execution completed (timer recorded: {self.elapsed >= 0})')\n\nwith Timer():\n    total = sum(i for i in range(50000))",
                    "expected_output": "Execution completed (timer recorded: True)",
                    "explanation_en": "Measures block execution duration using __enter__ and __exit__ hooks.",
                    "explanation_hi": "Block ke enter aur exit hone ke samay ka difference calculate karta hai."
                },
                "example_2": {
                    "title": "Database Transaction Rollback on Error",
                    "title_hi": "Database rollback simulator",
                    "code": "class DatabaseTransaction:\n    def __enter__(self):\n        print('BEGIN TRANSACTION')\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        if exc_type is not None:\n            print(f'ROLLBACK: Error detected ({exc_val})')\n            return True\n        print('COMMIT TRANSACTION')\n\nwith DatabaseTransaction():\n    print('Inserting user record...')\n    raise ValueError('Duplicate email ID!')",
                    "expected_output": "BEGIN TRANSACTION\nInserting user record...\nROLLBACK: Error detected (Duplicate email ID!)",
                    "explanation_en": "Catches the raised ValueError in __exit__ and issues a ROLLBACK command.",
                    "explanation_hi": "Exception aane par database rollback trigger karke error swallow kar leta hai."
                },
                "challenge": {
                    "prompt_en": "Create a class TagWrapper that prints '<start>' in __enter__ and '</end>' in __exit__. Run it with a with block printing 'Content inside tag'.",
                    "prompt_hi": "TagWrapper class banao jo __enter__ me '<start>' aur __exit__ me '</end>' print kare.",
                    "starter_code": "class TagWrapper:\n    # Implement __enter__ and __exit__:\n    pass\n\nwith TagWrapper():\n    print('Content inside tag')",
                    "expected_output": "<start>\nContent inside tag\n</end>",
                    "solution_code": "class TagWrapper:\n    def __enter__(self):\n        print('<start>')\n        return self\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        print('</end>')\n\nwith TagWrapper():\n    print('Content inside tag')",
                    "solution_explanation_en": "Prints start tag upon entry and closing tag upon exit.",
                    "solution_explanation_hi": "enter par opening aur exit par closing tag print hota hai.",
                    "hints": ["def __enter__(self): print('<start>'); return self", "def __exit__(self, exc_type, exc_val, exc_tb): print('</end>')"],
                    "ego_roast_hi": "4 arguments bhool gaye __exit__ me?",
                    "ego_cheer_hi": "Dunder context manager created! 🏗️"
                }
            },
            {
                "id": "ch22_sub3_contextlib_generators",
                "title": "Using contextlib to make context managers out of generators",
                "title_hi": "contextlib se generators ko context managers banana",
                "icon": "⚡",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Python's contextlib module provides a @contextmanager decorator that lets you build robust context managers using a simple generator function with a single yield statement.",
                "what_is_it_hi": "Python ka contextlib module ek @contextmanager decorator deta hai jisse bina class banaye, sirf ek simple generator function aur yield se context manager banaya ja sakta hai.",
                "why_need_it_en": "Cuts boilerplate code by 75% when creating quick context managers for directory changes, temporary state overrides, or mock environments.",
                "why_need_it_hi": "Puri class likhne ki zaroorat nahi padti; 4-5 line ke generator function me setup, yield aur cleanup pura ho jata hai.",
                "how_to_use_en": "from contextlib import contextmanager; decorate def gen(): setup; try: yield; finally: cleanup.",
                "how_to_use_hi": "from contextlib import contextmanager; generator function par @contextmanager lagayein aur yield ko try...finally me wrap karein.",
                "syntax": "from contextlib import contextmanager\n\n@contextmanager\ndef my_ctx():\n    print('Setup')\n    try:\n        yield\n    finally:\n        print('Cleanup')",
                "rules_en": [
                    "Import contextmanager from contextlib.",
                    "Decorate a generator function with @contextmanager.",
                    "Place setup code before yield.",
                    "Yield the resource to be bound to as target.",
                    "Wrap the yield in a try...finally block; code in finally executes during exit."
                ],
                "rules_hi": [
                    "from contextlib import contextmanager import karein.",
                    "Generator function ke upar @contextmanager lagayein.",
                    "yield se pehle ka code __enter__ ki tarah chalta hai.",
                    "yield ke baad ya finally me likha code __exit__ ki tarah chalta hai."
                ],
                "analogy_en": "Borrowing a projector from the lab: you sign it out at the counter (setup), use it during your presentation (yield), and hand it back when the session concludes (finally).",
                "analogy_hi": "Cricket match me helmet pehanna: batting aane par helmet pehno (setup), batting karo (yield), aur out hone par helmet wapas pavilion me rakh do (finally).",
                "common_mistakes": [
                    {
                        "mistake": "Omitting the try...finally block around yield inside a @contextmanager.",
                        "why_it_fails_en": "If an exception occurs inside the with block, execution never reaches lines after yield, leaking resources.",
                        "why_it_fails_hi": "Agar block me error aa jaye to yield ke baad ka code chalega hi nahi, isliye finally zaroori hai.",
                        "fix": "Always place cleanup code inside the finally clause."
                    }
                ],
                "example_1": {
                    "title": "Temporary Status Override Context Manager",
                    "title_hi": "Temporary status switch manager",
                    "code": "from contextlib import contextmanager\n\n@contextmanager\ndef temporary_status(status_msg):\n    print(f'[STATUS SET] {status_msg}')\n    try:\n        yield status_msg\n    finally:\n        print('[STATUS CLEARED] Back to Idle')\n\nwith temporary_status('Processing Payment...') as current:\n    print(f'Working on: {current}')",
                    "expected_output": "[STATUS SET] Processing Payment...\nWorking on: Processing Payment...\n[STATUS CLEARED] Back to Idle",
                    "explanation_en": "Sets state before yielding and resets it safely in the finally block.",
                    "explanation_hi": "yield se pehle status set karta hai aur finally me wapas idle kar deta hai."
                },
                "example_2": {
                    "title": "Temporary List Appender",
                    "title_hi": "List me temporary item jodna",
                    "code": "from contextlib import contextmanager\n\n@contextmanager\ndef append_temporarily(target_list, item):\n    target_list.append(item)\n    try:\n        yield target_list\n    finally:\n        target_list.pop()\n\nshared = [1, 2]\nwith append_temporarily(shared, 99):\n    print('Inside with:', shared)\nprint('Outside with:', shared)",
                    "expected_output": "Inside with: [1, 2, 99]\nOutside with: [1, 2]",
                    "explanation_en": "Appends item before yielding and removes it in finally.",
                    "explanation_hi": "Block khatam hote hi appended element pop ho jata hai."
                },
                "challenge": {
                    "prompt_en": "Use @contextmanager to create a bracket_printer() manager that prints '<<<' before yielding and '>>>' in finally. Run with a with block printing 'HELLO WORLD'.",
                    "prompt_hi": "@contextmanager se bracket_printer() banao jo '<<<' fir 'HELLO WORLD' fir '>>>' print kare.",
                    "starter_code": "from contextlib import contextmanager\n\n@contextmanager\ndef bracket_printer():\n    # Implement using yield:\n    pass\n\nwith bracket_printer():\n    print('HELLO WORLD')",
                    "expected_output": "<<<\nHELLO WORLD\n>>>",
                    "solution_code": "from contextlib import contextmanager\n\n@contextmanager\ndef bracket_printer():\n    print('<<<')\n    try:\n        yield\n    finally:\n        print('>>>')\n\nwith bracket_printer():\n    print('HELLO WORLD')",
                    "solution_explanation_en": "Prints <<< upon entry and >>> upon exit via generator yield.",
                    "solution_explanation_hi": "yield ke aage pehle <<< aur finally me >>> chalta hai.",
                    "hints": ["print('<<<'); try: yield; finally: print('>>>')"],
                    "ego_roast_hi": "finally block lagana bhool gaye?",
                    "ego_cheer_hi": "Generator contextmanager mastered! ⚡"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 23: Finding Patterns (Regular Expressions)
    # =========================================================================
    {
        "id": "ch23_finding_patterns_regex",
        "part_number": 6,
        "part_title": "PART 6: THE PEAK (ADVANCED PYTHON CONCEPTS)",
        "chapter_number": 23,
        "title": "Chapter 23: Finding Patterns (Regular Expressions)",
        "subtitle_en": "Harness the power of regex syntax to validate inputs, search text, and extract complex data tokens",
        "subtitle_hi": "Python re module aur regex patterns se emails, phones aur tokens extract karein",
        "icon": "🔍",
        "estimated_time": "50 mins",
        "prerequisites_en": "Parts 1 to 4 (Strings, escape sequences, functions).",
        "prerequisites_hi": "Part 1 se 4 tak (Strings, escape sequences, functions).",
        "learning_objectives_en": [
            "Understand regex concepts and compile patterns using Python's re module",
            "Differentiate between re.search(), re.match(), re.findall(), and re.finditer()",
            "Construct character classes, wildcards, and quantifiers to extract emails, phone numbers, and codes"
        ],
        "learning_objectives_hi": [
            "Regex concepts samjhein aur Python re module se patterns compile karein",
            "re.search(), re.match(), re.findall() aur re.sub() me difference samjhein",
            "Character sets, anchors (^, $) aur quantifiers se emails aur phone numbers validate karein"
        ],
        "recap_en": "You mastered regular expressions: raw string patterns, the re module API (search, match, findall, sub), wildcards, anchors, and industrial character sets for extracting emails and phone numbers.",
        "recap_hi": "Aapne regex master kiya jo kisi bhi text format me se emails, dates aur phone numbers ko ek line ke pattern se accurately dhoond nikalta hai.",
        "subtopics": [
            {
                "id": "ch23_sub1_what_is_regex",
                "title": "What are Regular Expressions (Regex)?",
                "title_hi": "Regular Expressions (Regex) kya hote hain?",
                "icon": "🧠",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "A Regular Expression (Regex) is a specialized mini-language used to describe text search patterns, enabling advanced pattern matching, data validation, and token extraction.",
                "what_is_it_hi": "Regular Expression (Regex) ek compact pattern-matching language hai jisse text ke andar specific patterns (jaise phone numbers, email addresses, dates) ko search, validate aur extract kiya jata hai.",
                "why_need_it_en": "Validating an email or scraping telephone numbers with basic string methods like .find() and .split() requires dozens of fragile lines of code. Regex accomplishes it in a single pattern string.",
                "why_need_it_hi": "Normal string methods se complex pattern dhoondna bohot mushkil hota hai. Regex ek single line ke pattern se lakho formats ko accurately match kar deta hai.",
                "how_to_use_en": "Always write patterns as raw strings: r'\\d+' (one or more digits).",
                "how_to_use_hi": "Regex pattern hamesha raw string r'...' me likhein taaki backslash escape na ho.",
                "syntax": "import re\nmatch = re.search(r'\\d{3}-\\d{4}', 'Call 555-1234')\nif match:\n    print(match.group())  # '555-1234'",
                "rules_en": [
                    "Regex patterns describe rules, not literal words (e.g., \\d+ means 'one or more digits').",
                    "Always use raw strings r'pattern' in Python so escape backslashes aren't swallowed by Python string literals.",
                    "Regex engines parse text character-by-character using finite state automata."
                ],
                "rules_hi": [
                    "Regex me literal words ke bajay pattern rules define hote hain (e.g. \\d+ ka matlab ek ya zyada digits).",
                    "Python me regex likhte waqt hamesha raw string r'...' use karni chahiye taaki backslash escape na ho.",
                    "Regex engine text ko step-by-step match karta hai."
                ],
                "analogy_en": "Regex is like a high-tech metal detector calibrated specifically to beep only when it detects gold coins (\\d{4}) while ignoring silver bottle caps and loose nails.",
                "analogy_hi": "Regex airport ke baggage scanner jaisa hai jo normal kapdo ko chhod kar sirf specific shape pattern ko pehchan leta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Writing regex patterns as regular strings '\\d+' instead of raw strings r'\\d+'.",
                        "why_it_fails_en": "Python string parser interprets \\ as an escape sequence before regex even receives it.",
                        "why_it_fails_hi": "Python normal string me backslash ko escape samajh leta hai jisse regex pattern toot jata hai.",
                        "fix": "Always prefix regex patterns with r: r'\\d+'."
                    }
                ],
                "example_1": {
                    "title": "Finding Numeric Tokens in Unstructured Text",
                    "title_hi": "Text me se numeric tokens search karna",
                    "code": "import re\ntext = 'Order #4829 completed on 2026-05-12'\norder_id = re.search(r'#\\d+', text)\nprint('Matched Token:', order_id.group())",
                    "expected_output": "Matched Token: #4829",
                    "explanation_en": "re.search finds the first token starting with # followed by digits.",
                    "explanation_hi": "# aur uske baad aane wale digits ko match karke group() se print karta hai."
                },
                "example_2": {
                    "title": "Raw String Literal Backslash Preservation",
                    "title_hi": "Raw strings ka literal backslash",
                    "code": "import re\nraw_pattern = r'\\n is newline'\nprint('Raw string maintains backslash:', '\\\\' in raw_pattern)",
                    "expected_output": "Raw string maintains backslash: True",
                    "explanation_en": "Raw strings prevent Python from replacing \\n with a literal newline character.",
                    "explanation_hi": "Raw string me backslash escape nahi hota aur safe rehta hai."
                },
                "challenge": {
                    "prompt_en": "Does the raw string prefix r prevent Python backslash escaping in regex strings? Print 'ESCAPING'.",
                    "prompt_hi": "Kya 'r' prefix backslash escape hone se roktahai? Print 'ESCAPING'.",
                    "starter_code": "# Print ESCAPING:\n",
                    "expected_output": "ESCAPING",
                    "solution_code": "print('ESCAPING')",
                    "solution_explanation_en": "Raw string prefix r treats backslashes as raw literal characters.",
                    "solution_explanation_hi": "r prefix backslashes ko literal rakhta hai.",
                    "hints": ["print('ESCAPING')"],
                    "ego_roast_hi": "Raw string prefix bhool gaye?",
                    "ego_cheer_hi": "Regex basics unlocked! 🧠"
                }
            },
            {
                "id": "ch23_sub2_importing_re_module",
                "title": "Importing the re module",
                "title_hi": "re module ko import aur use karna",
                "icon": "📦",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Python provides its standard regular expression engine through the built-in re module, offering functions like search(), match(), findall(), sub(), and compile().",
                "what_is_it_hi": "Python ka standard regex engine built-in re module me available hota hai, jisme search(), match(), findall(), aur sub() jaise functions aate hain.",
                "why_need_it_en": "Pre-installed with zero external dependencies, allowing instant text processing and input sanitization in any Python environment.",
                "why_need_it_hi": "Ye Python ke saath pre-installed aata hai, kisi third-party library ki zaroorat nahi hoti.",
                "how_to_use_en": "import re; re.search(pattern, text) or re.findall(pattern, text).",
                "how_to_use_hi": "import re; re.search(pattern, text) ya re.findall(pattern, text) use karein.",
                "syntax": "import re\n# Find first:\nfirst = re.search(r'\\d+', 'Age 25, Grade 12')\n# Find all:\nall_matches = re.findall(r'\\d+', 'Age 25, Grade 12')",
                "rules_en": [
                    "re.search(pattern, string): scans the entire string and returns the first match object (or None).",
                    "re.match(pattern, string): checks for a match ONLY at the beginning of the string.",
                    "re.findall(pattern, string): returns a list of all matching string occurrences.",
                    "re.sub(pattern, replacement, string): replaces matched patterns with new text."
                ],
                "rules_hi": [
                    "re.search(p, s): puri string me search karta hai aur pehla match return karta hai.",
                    "re.match(p, s): sirf string ki shuruat me match check karta hai.",
                    "re.findall(p, s): saare matches ki list return karta hai.",
                    "re.sub(p, repl, s): matched patterns ko nayi value se replace karta hai."
                ],
                "analogy_en": "re.match is looking through a peephole to check who is standing right in front of the door. re.search is searching the whole house to find where your keys are.",
                "analogy_hi": "re.match class ke pehle bench par baithe student ko check karna hai. re.search pure classroom me kisi bhi seat par baithe student ko dhoondna hai.",
                "common_mistakes": [
                    {
                        "mistake": "Using re.match() and wondering why it fails when the pattern exists in the middle of text.",
                        "why_it_fails_en": "re.match() is strictly anchored to the start of the string.",
                        "why_it_fails_hi": "re.match sirf string ke first character se match karta hai, beech me nahi.",
                        "fix": "Use re.search() to find matches anywhere in the string."
                    }
                ],
                "example_1": {
                    "title": "Comparing search, match, and findall",
                    "title_hi": "search, match aur findall ka difference",
                    "code": "import re\nmsg = 'Roll 101, Roll 102, Roll 103'\nprint('re.search:', re.search(r'\\d+', msg).group())\nprint('re.match on start:', re.match(r'\\d+', msg))\nprint('re.findall:', re.findall(r'\\d+', msg))",
                    "expected_output": "re.search: 101\nre.match on start: None\nre.findall: ['101', '102', '103']",
                    "explanation_en": "re.search finds first match; match returns None because string starts with 'Roll'; findall collects all matches.",
                    "explanation_hi": "search pehla match deta hai, match fail ho jata hai, aur findall saare matches list me deta hai."
                },
                "example_2": {
                    "title": "Masking Sensitive Data with re.sub",
                    "title_hi": "Sensitive data ko re.sub se mask karna",
                    "code": "import re\ncredit_card = 'Card: 4532-1234-5678-9999'\nmasked = re.sub(r'\\d{4}-\\d{4}-\\d{4}', 'XXXX-XXXX-XXXX', credit_card)\nprint('Masked:', masked)",
                    "expected_output": "Masked: Card: XXXX-XXXX-XXXX-9999",
                    "explanation_en": "Replaces the first three digit groups with 'XXXX-XXXX-XXXX'.",
                    "explanation_hi": "re.sub matched pattern ko replacement string se badal deta hai."
                },
                "challenge": {
                    "prompt_en": "Use re.findall(r'\\d+', text) to extract all numbers from text = 'I have 2 cats, 5 dogs, and 12 fish'. Print the list: ['2', '5', '12']",
                    "prompt_hi": "re.findall se numbers extract karke print karo: ['2', '5', '12']",
                    "starter_code": "import re\ntext = 'I have 2 cats, 5 dogs, and 12 fish'\n# Extract all numbers:\n",
                    "expected_output": "['2', '5', '12']",
                    "solution_code": "import re\ntext = 'I have 2 cats, 5 dogs, and 12 fish'\ncounts = re.findall(r'\\d+', text)\nprint(counts)",
                    "solution_explanation_en": "findall extracts all contiguous digit sequences.",
                    "solution_explanation_hi": "findall saare digit groups ko list me collect kar leta hai.",
                    "hints": ["re.findall(r'\\d+', text)"],
                    "ego_roast_hi": "\\d+ likhna bhool gaye?",
                    "ego_cheer_hi": "re module master! 📦"
                }
            },
            {
                "id": "ch23_sub3_matching_exact_strings_wildcards",
                "title": "Matching exact strings and wildcards",
                "title_hi": "Exact strings aur wildcards match karna",
                "icon": "🃏",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Regex allows matching exact literal characters as well as special metacharacters like the dot wildcard . (matches any character except newline), anchors ^ (start) and $ (end), and alternation | (OR).",
                "what_is_it_hi": "Regex me exact words ke alawa special wildcards hote hain jaise dot . (kisi bhi character se match karta hai), ^ (start of string), $ (end of string), aur | (OR operator).",
                "why_need_it_en": "Gives you the flexibility to search for variations of words (e.g., 'cat', 'cot', 'cut') using a single general pattern.",
                "why_need_it_hi": "Ek hi pattern se alag alag variations jaise cat, cot, cut ko catch karne ki taakat deta hai.",
                "how_to_use_en": "Use . for any character, ^ for beginning of line, $ for end of line, and | for alternation.",
                "how_to_use_hi": "Dot . kisi bhi character ke liye, ^ shuruat ke liye, $ end ke liye, aur | option ke liye use karein.",
                "syntax": "import re\n# Matches cat, cot, cut:\nre.findall(r'c.t', 'cat cot cut')\n# Starts with Hello and ends with World:\nre.search(r'^Hello.*World$', 'Hello Cruel World')",
                "rules_en": [
                    ". (Dot): matches any single character except newline.",
                    "^: asserts start of the string (e.g., ^Hello).",
                    "$: asserts end of the string (e.g., World$).",
                    "| (Pipe): acts as logical OR (e.g., cat|dog).",
                    "To match a literal dot ., escape it with a backslash \\.."
                ],
                "rules_hi": [
                    "Dot . kisi bhi single character se match karta hai.",
                    "^ string ke shuruat ko point karta hai.",
                    "$ string ke aakhiri ko point karta hai.",
                    "| (Pipe) OR condition banata hai (jaise cat|dog).",
                    "Real dot match karne ke liye \\. escape karna padta hai."
                ],
                "analogy_en": "The dot wildcard . is a blank tile in Scrabble or a Joker in card games that can represent any letter.",
                "analogy_hi": "Dot . taash ke patto me Joker jaisa hai—jo kisi bhi patte ki jagah fit baith jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Searching for a website domain using r'google.com' without escaping the dot.",
                        "why_it_fails_en": "Unescaped . matches ANY character, meaning it will accidentally match 'googleXcom' and 'google7com'.",
                        "why_it_fails_hi": "Unescaped dot kisi bhi character se match karega, jaise googleXcom.",
                        "fix": "Escape literal dots: r'google\\.com'."
                    }
                ],
                "example_1": {
                    "title": "Wildcard Dot Matching Any Character",
                    "title_hi": "Wildcard dot se pattern match karna",
                    "code": "import re\ntext = 'The cat sat on a mat with a bat'\nmatches = re.findall(r'.at', text)\nprint('Matches:', matches)",
                    "expected_output": "Matches: ['cat', 'sat', 'mat', 'bat']",
                    "explanation_en": "Matches any character preceding 'at'.",
                    "explanation_hi": "'.at' kisi bhi 3-letter word jiska end 'at' ho match karta hai."
                },
                "example_2": {
                    "title": "String Anchors ^ (Start) and $ (End)",
                    "title_hi": "String boundaries (^ aur $) test karna",
                    "code": "import re\nvalid_greeting = 'Hello Universe'\nprint('Starts with Hello:', bool(re.search(r'^Hello', valid_greeting)))\nprint('Ends with Universe:', bool(re.search(r'Universe$', valid_greeting)))",
                    "expected_output": "Starts with Hello: True\nEnds with Universe: True",
                    "explanation_en": "^ checks starting position; $ checks ending position.",
                    "explanation_hi": "^ se shuruat aur $ se aakhiri text check hota hai."
                },
                "challenge": {
                    "prompt_en": "Use re.search(r'apple|banana', text) to check which fruit appears in text = 'I love banana shake'. Print the matched word: banana",
                    "prompt_hi": "re.search(r'apple|banana', text) se matched word print karo: banana",
                    "starter_code": "import re\ntext = 'I love banana shake'\n# Match apple or banana:\n",
                    "expected_output": "banana",
                    "solution_code": "import re\ntext = 'I love banana shake'\nmatch = re.search(r'apple|banana', text)\nprint(match.group())",
                    "solution_explanation_en": "Alternation pipe | matches whichever candidate occurs first.",
                    "solution_explanation_hi": "Pipe | OR logic se match karta hai.",
                    "hints": ["re.search(r'apple|banana', text).group()"],
                    "ego_roast_hi": "Pipe symbol nahi mila keyboard par?",
                    "ego_cheer_hi": "Wildcard pattern matched! 🃏"
                }
            },
            {
                "id": "ch23_sub4_character_sets_quantifiers",
                "title": "Character sets and quantifiers (Finding emails, phone numbers, and passwords)",
                "title_hi": "Character sets aur quantifiers (Emails, phone numbers aur passwords dhoondna)",
                "icon": "📧",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "Character sets [...] define a custom set of permissible characters, while quantifiers (*, +, ?, {m,n}) specify how many times a character or group may repeat.",
                "what_is_it_hi": "Character sets [...] allow kiye gaye characters ki list define karte hain, aur quantifiers (*, +, ?, {m,n}) batate hain ki wo character kitni baar repeat ho sakta hai.",
                "why_need_it_en": "This combination provides the full power required to validate emails, 10-digit phone numbers, and strong password formats in real applications.",
                "why_need_it_hi": "Email format verification, phone number checking aur password strength validate karne ke liye character sets aur quantifiers ka use hota hai.",
                "how_to_use_en": "Combine sets and quantifiers: r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'.",
                "how_to_use_hi": "Sets aur quantifiers combine karein: r'[6-9]\\d{9}' se Indian 10-digit number match karein.",
                "syntax": "import re\n# 10-digit Indian phone pattern:\nphone_pattern = r'^[6-9]\\d{9}$'\n# Email pattern:\nemail_pattern = r'[\\w.-]+@[\\w.-]+\\.\\w+'",
                "rules_en": [
                    "[a-z]: any lowercase letter; [0-9]: any digit; [^0-9]: any non-digit.",
                    "+: 1 or more occurrences; *: 0 or more occurrences; ?: 0 or 1 occurrence (optional).",
                    "{n}: exactly n times; {min, max}: between min and max occurrences.",
                    "Email pattern blueprint: r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}'.",
                    "Indian 10-digit phone number blueprint: r'^[6-9]\\d{9}$'."
                ],
                "rules_hi": [
                    "[a-z] koi bhi lowercase letter, [0-9] ya \\d koi bhi digit hota hai.",
                    "+ ka matlab 1 ya zyada baar, * ka matlab 0 ya zyada baar, ? ka matlab optional.",
                    "{10} ka matlab exact 10 baar repeat hona.",
                    "Email pattern: r'[\\w.-]+@[\\w.-]+\\.\\w+'.",
                    "Indian mobile number: r'^[6-9]\\d{9}$' (start with 6-9, followed by 9 digits)."
                ],
                "analogy_en": "A quantifier is an ingredient instruction in a recipe: ? means optional pinch of salt; + means at least 1 cup of flour; {4} means exactly 4 eggs.",
                "analogy_hi": "Quantifier train ke bogie rule jaisa hai: {10} ka matlab train me exact 10 bogiyan honi chahiye, na kam na zyada.",
                "common_mistakes": [
                    {
                        "mistake": "Writing ^[6-9]\\d{9} without trailing $ when validating phone numbers.",
                        "why_it_fails_en": "A 12-digit number like '987654321099' will mistakenly pass validation because the first 10 digits match.",
                        "why_it_fails_hi": "Bina $ ke 12 digits ka number bhi pass ho jayega kyunki pehle 10 digits match kar jayenge.",
                        "fix": "Always anchor full validations with both ^ (start) and $ (end)."
                    }
                ],
                "example_1": {
                    "title": "Extracting Email Addresses with Character Sets",
                    "title_hi": "Text me se email addresses extract karna",
                    "code": "import re\ntext = 'Contact support@elysia.org or admin@python.edu for queries.'\nemails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}', text)\nprint('Extracted Emails:', emails)",
                    "expected_output": "Extracted Emails: ['support@elysia.org', 'admin@python.edu']",
                    "explanation_en": "Character sets and + quantifiers match standard email address format.",
                    "explanation_hi": "Email format ke dono addresses ko accurately filter kar leta hai."
                },
                "example_2": {
                    "title": "Validating Indian 10-Digit Mobile Numbers",
                    "title_hi": "10-digit mobile number validator",
                    "code": "import re\ndef validate_phone(number):\n    pattern = r'^[6-9]\\d{9}$'\n    return bool(re.match(pattern, number))\n\nprint('9876543210:', validate_phone('9876543210'))\nprint('1234567890:', validate_phone('1234567890'))\nprint('98765:', validate_phone('98765'))",
                    "expected_output": "9876543210: True\n1234567890: False\n98765: False",
                    "explanation_en": "Enforces starting with 6-9 and exactly 9 following digits (total 10 digits).",
                    "explanation_hi": "Check karta hai ki number 6-9 se shuru ho aur exact 10 digits ka ho."
                },
                "challenge": {
                    "prompt_en": "Write a regex pattern to extract all 4-digit years from 'Born in 1998, graduated in 2020, joined in 2024'. Print the list: ['1998', '2020', '2024']",
                    "prompt_hi": "re.findall(r'\\d{4}', text) se saare 4-digit years extract karke print karo: ['1998', '2020', '2024']",
                    "starter_code": "import re\ntext = 'Born in 1998, graduated in 2020, joined in 2024'\n# Extract all 4-digit years:\n",
                    "expected_output": "['1998', '2020', '2024']",
                    "solution_code": "import re\ntext = 'Born in 1998, graduated in 2020, joined in 2024'\nyears = re.findall(r'\\d{4}', text)\nprint(years)",
                    "solution_explanation_en": "\\d{4} matches exactly 4 consecutive digits.",
                    "solution_explanation_hi": "\\d{4} exact 4 digits match karta hai.",
                    "hints": ["re.findall(r'\\d{4}', text)"],
                    "ego_roast_hi": "\\d{4} quantifier lagana bhool gaye?",
                    "ego_cheer_hi": "Regex quantifier champion! 📧"
                }
            }
        ]
    }
]

PART_6 = {
    "part_number": 6,
    "part_title": "PART 6: THE PEAK (ADVANCED PYTHON CONCEPTS)",
    "description": "Master Pythonic idioms, high-performance generators, functional decorators, safe resource managers, and regex pattern engines.",
    "chapters": CHAPTERS
}
