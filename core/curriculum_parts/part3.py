"""
Part 3: Organizing Lots of Data (Data Structures)
Chapters 8, 9, 10, and 11 with exact syllabus titles and subtopics.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 8: The Ultimate Organizer (Lists)
    # =========================================================================
    {
        "id": "ch8_lists",
        "part_number": 3,
        "part_title": "PART 3: ORGANIZING LOTS OF DATA (DATA STRUCTURES)",
        "chapter_number": 8,
        "title": "Chapter 8: The Ultimate Organizer (Lists)",
        "subtitle_en": "Master mutable sequences: indexing, slicing, appending, mutating, sorting, and 2D matrices",
        "subtitle_hi": "Lists master karo: indexing, slicing, append, remove, sort aur 2D matrices",
        "icon": "📋",
        "estimated_time": "40 mins",
        "prerequisites_en": "Parts 1 & 2 (Variables, loops, and basic operations).",
        "prerequisites_hi": "Part 1 aur 2 (Variables, loops aur operations).",
        "learning_objectives_en": [
            "Understand lists as ordered, mutable collections",
            "Master positive (0, 1) and negative (-1, -2) indexing",
            "Extract slices using [start:stop:step]",
            "Add elements via append(), insert(), and extend()",
            "Remove elements via remove(), pop(), clear(), and del",
            "Sort, reverse, and calculate aggregates (len, min, max, sum)",
            "Navigate 2D nested lists and grids"
        ],
        "learning_objectives_hi": [
            "List ka concept samjho (ordered, mutable)",
            "Positive aur negative indexing master karo",
            "Slicing [start:stop:step] se hissa nikaalna",
            "append(), insert(), extend() ka farak",
            "remove(), pop(), del se elements hatana",
            "Sorting aur aggregate functions (sum, len, min, max)",
            "2D nested lists aur grids handle karna"
        ],
        "recap_en": "You mastered Python lists: mutability, indexing, slicing, modification methods, sorting, built-in functions, and 2D grids.",
        "recap_hi": "Aapne lists ki mutability, indexing, slicing, methods, sorting aur 2D grids master ki.",
        "subtopics": [
            {
                "id": "ch8_sub1_what_is_a_list",
                "title": "What is a list? (Creating arrays of data)",
                "title_hi": "List kya hoti hai? (Data ke arrays banana)",
                "icon": "📦",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A list is an ordered, mutable (changeable) collection of items enclosed in square brackets []. Unlike arrays in C or Java, Python lists can hold heterogeneous types (integers, strings, floats, even other lists all together!).",
                "what_is_it_hi": "List square brackets [] me band items ka ek ordered collection hota hai jo MUTABLE (badla ja sakne wala) hota hai. C ya Java ke arrays se alag, Python list me ek sath numbers, text, decimals sab kuch rakh sakte ho!",
                "why_need_it_en": "Instead of creating 50 separate variables (student1, student2, student3...), you store all 50 in a single list: students = ['Aman', 'Sara', ...].",
                "why_need_it_hi": "50 alag variables banane ke badle ek hi list me saare students ka data store ho jata hai: students = ['Aman', 'Sara'].",
                "how_to_use_en": "items = [1, 'two', 3.0, True]. Empty list: empty = [] or empty = list().",
                "how_to_use_hi": "Square brackets use karo: my_list = [10, 20, 30].",
                "syntax": "shopping_cart = [\"Apples\", \"Milk\", \"Eggs\"]\nmixed_data = [101, \"Alex\", 9.4, True]",
                "rules_en": [
                    "Lists are ordered: items retain their exact sequence unless explicitly rearranged.",
                    "Lists are mutable: you can add, remove, and replace items in-place.",
                    "Lists allow duplicates: ['apple', 'apple'] is completely valid."
                ],
                "rules_hi": [
                    "List ordered hoti hai: items ka sequence wahi rehta hai jo aapne daala.",
                    "List mutable hoti hai: items ko kabhi bhi change ya delete kar sakte ho.",
                    "Duplicates allowed hote hain: ek hi naam do baar aa sakta hai."
                ],
                "analogy_en": "A shopping cart at a supermarket: you toss in items in order, rearrange them, add more, or take something out at checkout.",
                "analogy_hi": "Supermarket ki shopping trolley jaisi — saman daalo, nikaalo, ya badlo.",
                "common_mistakes": [
                    {
                        "mistake": "Using parentheses instead of square brackets: my_list = (1, 2, 3)",
                        "why_it_fails_en": "Parentheses create an immutable TUPLE, not a mutable list!",
                        "why_it_fails_hi": "Gol brackets () se tuple banta hai list nahi.",
                        "fix": "Always use square brackets [] for lists."
                    }
                ],
                "example_1": {
                    "title": "Creating and Displaying a List",
                    "title_hi": "List banana aur print karna",
                    "code": "fruits = ['Apple', 'Banana', 'Mango']\nprint('Shopping list:', fruits)\nprint('Total items in list:', len(fruits))",
                    "expected_output": "Shopping list: ['Apple', 'Banana', 'Mango']\nTotal items in list: 3",
                    "explanation_en": "Initializes a list with 3 string items and inspects length with len().",
                    "explanation_hi": "3 items ki list banata hai aur len() se ginti batata hai."
                },
                "example_2": {
                    "title": "Heterogeneous Mixed List",
                    "title_hi": "Mixed data types ek list me",
                    "code": "student = ['Rohan', 21, 8.85, True]\nprint('Student profile list:', student)",
                    "expected_output": "Student profile list: ['Rohan', 21, 8.85, True]",
                    "explanation_en": "Contains str, int, float, and bool simultaneously.",
                    "explanation_hi": "String, integer, float aur boolean sab ek sath store karta hai."
                },
                "challenge": {
                    "prompt_en": "Create a list skills = ['Python', 'SQL'] and print: Skills count: 2",
                    "prompt_hi": "skills = ['Python', 'SQL'] banao aur print karo: Skills count: 2",
                    "starter_code": "# Create list and print length:\n",
                    "expected_output": "Skills count: 2",
                    "solution_code": "skills = ['Python', 'SQL']\nprint(f'Skills count: {len(skills)}')",
                    "solution_explanation_en": "Uses len() to find list length.",
                    "solution_explanation_hi": "len() se list ki lambai nikaalta hai.",
                    "hints": ["skills = ['Python', 'SQL']\\nprint(f'Skills count: {len(skills)}')"],
                    "ego_roast_hi": "List banana bhool gaye?",
                    "ego_cheer_hi": "List collection initialized! 📋"
                }
            },
            {
                "id": "ch8_sub2_indexing",
                "title": "Accessing items using Indexing (Positive and Negative indexes)",
                "title_hi": "Indexing se items access karna (Positive aur Negative indexes)",
                "icon": "📍",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Indexing accesses individual elements by their positional index. Positive indexing starts at 0 from the left. Negative indexing starts at -1 from the very right (the last item).",
                "what_is_it_hi": "Indexing ka matlab list ke kisi specific item ko uski seat number se nikaalna. Positive indexing 0 se shuru hoti hai (left se). Negative indexing -1 se shuru hoti hai (right se aakhri item).",
                "why_need_it_en": "Accessing the latest notification (items[-1]) or the first applicant (items[0]) requires zero searching time — it is instant O(1) memory lookup.",
                "why_need_it_hi": "Aakhri message dekhna ho to items[-1] likho. Pehla item chahiye to items[0]. 1 millisecond me data mil jata hai.",
                "how_to_use_en": "first = items[0], last = items[-1].",
                "how_to_use_hi": "Pehle ke liye items[0], aakhri ke liye items[-1].",
                "syntax": "colors = [\"red\", \"green\", \"blue\"]\nfirst = colors[0]    # 'red'\nlast = colors[-1]    # 'blue'\nsecond_last = colors[-2] # 'green'",
                "rules_en": [
                    "Python lists are ZERO-INDEXED: first item is at index 0, not index 1.",
                    "Negative indexes count backwards: -1 is last, -2 is second to last.",
                    "Accessing an index >= len(list) throws IndexError: list index out of range."
                ],
                "rules_hi": [
                    "Counting 0 se shuru hoti hai: pehla item seat #0 par baithta hai.",
                    "Negative index peeche se chalta hai: -1 aakhri item hai.",
                    "Aisi seat access karne par jo list me hai hi nahi, IndexError aayega."
                ],
                "analogy_en": "Train compartments: Engine is at compartment 0. The guard van at the caboose is compartment -1.",
                "analogy_hi": "Train ke dibbe: Engine ke baad pehla dibba 0 hai, aur sabse pichhla guard ka dibba -1 hai.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to get the 3rd item of a 3-item list using items[3].",
                        "why_it_fails_en": "IndexError: list index out of range. In a 3-item list, indices are 0, 1, and 2!",
                        "why_it_fails_hi": "3 items wali list me seats 0, 1, aur 2 hoti hain. 3rd seat exist hi nahi karti.",
                        "fix": "Use items[2] for the 3rd item, or items[-1] for the last."
                    }
                ],
                "example_1": {
                    "title": "Positive and Negative Indexing",
                    "title_hi": "Left aur Right se access karna",
                    "code": "cities = ['Delhi', 'Mumbai', 'Bangalore', 'Kolkata']\nprint('First city (index 0):', cities[0])\nprint('Last city (index -1):', cities[-1])",
                    "expected_output": "First city (index 0): Delhi\nLast city (index -1): Kolkata",
                    "explanation_en": "cities[0] retrieves 'Delhi'; cities[-1] retrieves 'Kolkata'.",
                    "explanation_hi": "0 pehla shahar aur -1 aakhri shahar deta hai."
                },
                "example_2": {
                    "title": "Modifying via Index",
                    "title_hi": "Seat par baitha item badalna",
                    "code": "nums = [10, 20, 30]\nnums[1] = 99  # Replace index 1\nprint('Updated list:', nums)",
                    "expected_output": "Updated list: [10, 99, 30]",
                    "explanation_en": "Mutates the item at index 1 from 20 to 99 in-place.",
                    "explanation_hi": "Index 1 par 20 ki jagah 99 replace kar diya."
                },
                "challenge": {
                    "prompt_en": "Given langs = ['C', 'Java', 'Python'], print the last element using negative indexing: Python",
                    "prompt_hi": "langs = ['C', 'Java', 'Python'] se negative indexing (-1) use karke print karo: Python",
                    "starter_code": "langs = ['C', 'Java', 'Python']\n# Print last item:\n",
                    "expected_output": "Python",
                    "solution_code": "langs = ['C', 'Java', 'Python']\nprint(langs[-1])",
                    "solution_explanation_en": "langs[-1] accesses the final item 'Python'.",
                    "solution_explanation_hi": "langs[-1] aakhri item print karta hai.",
                    "hints": ["langs[-1]"],
                    "ego_roast_hi": "-1 lagana itna mushkil hai?",
                    "ego_cheer_hi": "Index positioning pinpointed! 📍"
                }
            },
            {
                "id": "ch8_sub3_slicing",
                "title": "Grabbing chunks of data using Slicing [start:stop:step]",
                "title_hi": "Slicing se data ke chunks nikaalna [start:stop:step]",
                "icon": "🔪",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Slicing extracts a sub-portion of a list or string using the syntax [start:stop:step]. It returns a brand new list containing only the requested subset.",
                "what_is_it_hi": "Slicing ka matlab list me se cake ki tarah ek tukda kaat kar nikaalna: [start:stop:step]. Ye original list ko chhedta nahi, balki ek nayi chhoti list bana kar deta hai.",
                "why_need_it_en": "Pagination (first 10 results: [:10]), reversing a list ([::-1]), or grabbing every second item ([::2]).",
                "why_need_it_hi": "Google search ke pehle 10 results dikhana ([:10]), list ko ulta karna ([::-1]), ya even index wale items nikaalna.",
                "how_to_use_en": "sub = items[1:4] grabs indices 1, 2, 3. Omitting start means from 0; omitting stop means to the end.",
                "how_to_use_hi": "items[1:4] se index 1, 2, 3 aayenge. items[:3] shuru ke 3 items deta hai. items[::-1] list ulta kar deta hai.",
                "syntax": "arr[start:stop]       # From start up to (stop - 1)\narr[:stop]            # From beginning up to (stop - 1)\narr[start:]           # From start to the very end\narr[::step]           # Every step-th item\narr[::-1]             # Reverse the whole list!",
                "rules_en": [
                    "CRITICAL LAW: 'stop' is EXCLUSIVE! arr[1:4] includes indices 1, 2, and 3 only.",
                    "Slicing NEVER throws IndexError! If indices are out of range, Python gracefully clips to available elements.",
                    "[::-1] is the famous Python idiom to reverse any sequence in O(n) time."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: stop index HAMESHA chhoot jata hai (exclusive). arr[1:4] me sirf 1, 2, 3 aayenge.",
                    "Slicing me kabhi IndexError nahi aata! Agar range bahar hai to Python jitna mila utna return kar deta hai.",
                    "[::-1] list ya string ko ulta (reverse) karne ka sabse famous Python formula hai."
                ],
                "analogy_en": "Slicing a loaf of bread: you cut from bread slice #2 to slice #5 to make a sandwich, leaving the rest of the loaf intact.",
                "analogy_hi": "Bread ka packet: slice #2 se #5 tak nikaal kar sandwich bana liya, baaki bread packet me waisi ki waisi bachi rahi.",
                "common_mistakes": [
                    {
                        "mistake": "Thinking arr[0:3] gives 4 elements because 0, 1, 2, 3.",
                        "why_it_fails_en": "stop is exclusive! arr[0:3] yields exactly 3 elements: indices 0, 1, and 2.",
                        "why_it_fails_hi": "arr[0:3] sirf 3 items deta hai (0, 1, 2).",
                        "fix": "Formula for sliced length: len = stop - start (3 - 0 = 3)."
                    }
                ],
                "example_1": {
                    "title": "Sub-list Slicing and Top-3 Rankings",
                    "title_hi": "Top 3 items nikaalna",
                    "code": "scores = [99, 95, 91, 88, 82, 75]\ntop_three = scores[:3]\nprint('Top 3 scores:', top_three)",
                    "expected_output": "Top 3 scores: [99, 95, 91]",
                    "explanation_en": "scores[:3] grabs from start up to index 2 (the top 3 scores).",
                    "explanation_hi": "scores[:3] pehle 3 items ka slice nikaalta hai."
                },
                "example_2": {
                    "title": "List Reversal via Slicing Trick",
                    "title_hi": "List ko ulta karna ([::-1])",
                    "code": "letters = ['A', 'B', 'C', 'D']\nreversed_list = letters[::-1]\nprint('Reversed sequence:', reversed_list)",
                    "expected_output": "Reversed sequence: ['D', 'C', 'B', 'A']",
                    "explanation_en": "Step of -1 traverses backwards, creating a reversed copy.",
                    "explanation_hi": "Step -1 lagane se list ulte order me copy ho jaati hai."
                },
                "challenge": {
                    "prompt_en": "Given data = [10, 20, 30, 40, 50], slice the middle three items [20, 30, 40] using data[1:4] and print them.",
                    "prompt_hi": "data = [10, 20, 30, 40, 50] me se data[1:4] slice karke [20, 30, 40] print karo.",
                    "starter_code": "data = [10, 20, 30, 40, 50]\n# Slice and print:\n",
                    "expected_output": "[20, 30, 40]",
                    "solution_code": "data = [10, 20, 30, 40, 50]\nprint(data[1:4])",
                    "solution_explanation_en": "data[1:4] extracts indices 1, 2, and 3.",
                    "solution_explanation_hi": "data[1:4] se beech ke 3 elements aate hain.",
                    "hints": ["print(data[1:4])"],
                    "ego_roast_hi": "Slice ka formula bhool gaye?",
                    "ego_cheer_hi": "Slicing surgical precision! 🔪"
                }
            },
            {
                "id": "ch8_sub4_adding_items",
                "title": "Adding items: append(), insert(), extend()",
                "title_hi": "Items add karna: append(), insert(), extend()",
                "icon": "➕",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Python provides three distinct methods to grow a list: append() adds a single item to the very END; insert() inserts an item at a SPECIFIC INDEX; extend() unpacks and appends all items from another iterable.",
                "what_is_it_hi": "List me items jodne ke 3 tareeqe hote hain: append() hamesha AAKHRI me 1 item jodta hai; insert() kisi SPECIFIC SEAT par ghusata hai; extend() doosri list ke saare items ko khol kar jod deta hai.",
                "why_need_it_en": "A user clicks 'Add to Cart' (append), a VIP jumps to front of line (insert at index 0), or you merge two search results together (extend).",
                "why_need_it_hi": "Cart me product add karna (append), VIP ko line me sabse aage bithana (insert at 0), do lists ko aapas me milana (extend).",
                "how_to_use_en": "arr.append(x), arr.insert(index, x), arr.extend(other_list).",
                "how_to_use_hi": "arr.append('item'), arr.insert(0, 'vip'), arr.extend(['a', 'b']).",
                "syntax": "nums = [1, 2]\nnums.append(3)          # [1, 2, 3]\nnums.insert(0, 99)      # [99, 1, 2, 3]\nnums.extend([4, 5])     # [99, 1, 2, 3, 4, 5]",
                "rules_en": [
                    "append() always adds exactly ONE element to the end. If you pass a list to append, it nests it: [1, [2, 3]].",
                    "extend() unpacks elements: passing [2, 3] yields [1, 2, 3].",
                    "insert(idx, val) shifts all existing elements to the right; it does NOT overwrite."
                ],
                "rules_hi": [
                    "append() sirf 1 item jodta hai. Agar doosri list append kar doge to wo list ke andar list ban jayegi.",
                    "extend() items ko khol kar individual elements ki tarah jodta hai.",
                    "insert() purane items ko aage khiska deta hai, delete nahi karta."
                ],
                "analogy_en": "append() is joining the back of the movie ticket queue. insert() is cutting into the middle of the line. extend() is a whole bus of people joining the queue together.",
                "analogy_hi": "append() line ke pichhe khade hona hai. insert() line ke beech me ghusna hai. extend() poori bus ke logon ka line me judna hai.",
                "common_mistakes": [
                    {
                        "mistake": "Assigning the result of append: new_list = my_list.append('x')",
                        "why_it_fails_en": "append() modifies the list in-place and returns None! new_list becomes None.",
                        "why_it_fails_hi": "append() kuch return nahi karta (None deta hai), wo original list ko hi modify karta hai.",
                        "fix": "Call my_list.append('x') on its own line; do not assign it."
                    }
                ],
                "example_1": {
                    "title": "Append vs Extend Distinction",
                    "title_hi": "append aur extend ka live farak",
                    "code": "list1 = [1, 2]\nlist1.append([3, 4])\nprint('After append:', list1)\n\nlist2 = [1, 2]\nlist2.extend([3, 4])\nprint('After extend:', list2)",
                    "expected_output": "After append: [1, 2, [3, 4]]\nAfter extend: [1, 2, 3, 4]",
                    "explanation_en": "append creates a nested list; extend flattens the items into the parent list.",
                    "explanation_hi": "append se nested list bani, jabki extend se flat list bani."
                },
                "example_2": {
                    "title": "Inserting at Front (Index 0)",
                    "title_hi": "Sabse aage insert karna",
                    "code": "queue = ['Bob', 'Charlie']\nqueue.insert(0, 'Alice')  # Jumped to front\nprint('Queue order:', queue)",
                    "expected_output": "Queue order: ['Alice', 'Bob', 'Charlie']",
                    "explanation_en": "Alice is inserted at index 0, shifting Bob and Charlie rightwards.",
                    "explanation_hi": "Alice index 0 par aayi aur baaki sab right shift ho gaye."
                },
                "challenge": {
                    "prompt_en": "Start with nums = [1, 2], append 3, extend [4, 5], and print the list.",
                    "prompt_hi": "nums = [1, 2] me 3 append karo, fir [4, 5] extend karo aur list print karo: [1, 2, 3, 4, 5]",
                    "starter_code": "nums = [1, 2]\n# Append 3, extend [4, 5], and print:\n",
                    "expected_output": "[1, 2, 3, 4, 5]",
                    "solution_code": "nums = [1, 2]\nnums.append(3)\nnums.extend([4, 5])\nprint(nums)",
                    "solution_explanation_en": "Grows the list to [1, 2, 3, 4, 5].",
                    "solution_explanation_hi": "append aur extend se list 5 items ki ho jaati hai.",
                    "hints": ["nums.append(3) then nums.extend([4, 5])"],
                    "ego_roast_hi": "append aur extend mix kar diya kya?",
                    "ego_cheer_hi": "List expansion master! ➕"
                }
            },
            {
                "id": "ch8_sub5_removing_items",
                "title": "Removing items: remove(), pop(), clear(), del",
                "title_hi": "Items hatana: remove(), pop(), clear(), del",
                "icon": "🗑️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Python provides 4 ways to delete list items: remove(val) deletes by VALUE; pop(idx) deletes by INDEX and returns the removed item; clear() empties the entire list; del removes by index or slices.",
                "what_is_it_hi": "Items delete karne ke 4 tareeqe: remove(val) VALUE ke naam se hatata hai; pop(idx) SEAT INDEX se hatata hai aur hataya hua item wapas bhi karta hai; clear() poori list khali kar deta hai; del index ya slice ko delete karta hai.",
                "why_need_it_en": "Deleting canceled orders, popping the top card from a deck of cards, or clearing a completed shopping cart.",
                "why_need_it_hi": "Cancel hua order hatana, taash ke patte me se card nikaalna (pop), cart khali karna (clear).",
                "how_to_use_en": "arr.remove('Apple'), item = arr.pop(0), arr.clear(), del arr[1].",
                "how_to_use_hi": "arr.remove('val'), last = arr.pop(), arr.clear(), del arr[0].",
                "syntax": "items = [\"A\", \"B\", \"C\", \"D\"]\nitems.remove(\"B\")    # Removes by value\nlast = items.pop()   # Removes and returns last item ('D')\ndel items[0]         # Deletes index 0\nitems.clear()        # List is now empty []",
                "rules_en": [
                    "remove(val) only deletes the FIRST matching occurrence. If value doesn't exist, it throws ValueError.",
                    "pop() with no argument removes and returns the VERY LAST element (O(1) stack operation).",
                    "pop(idx) removes and returns element at that index (shifts subsequent items left).",
                    "del is a Python keyword statement, not a method."
                ],
                "rules_hi": [
                    "remove(val) sirf PEHLE match ko hatata hai. Agar item nahi mila to ValueError phekega.",
                    "pop() bina index ke AAKHRI item nikaal kar deta hai (Stack LIFO pop).",
                    "del ek Python keyword hai, method nahi.",
                    "clear() list ko [] khali bana deta hai."
                ],
                "analogy_en": "remove() is finding a spoiled apple by looking for it and throwing it away. pop() is taking the top plate off a stack of dishes.",
                "analogy_hi": "remove() dukan me se kharab seb dhoond kar phenkna hai. pop() plate ke dher me se sabse upar ki plate utha lena hai.",
                "common_mistakes": [
                    {
                        "mistake": "Calling remove() on a value that isn't present in the list.",
                        "why_it_fails_en": "ValueError: list.remove(x): x not in list.",
                        "why_it_fails_hi": "Jo cheez list me hai hi nahi use remove karne par code crash ho jata hai.",
                        "fix": "Check membership first: if 'x' in my_list: my_list.remove('x')."
                    }
                ],
                "example_1": {
                    "title": "Popping from a Stack",
                    "title_hi": "pop() se item nikaalna aur use karna",
                    "code": "tasks = ['Email', 'Report', 'Meeting']\ncurrent_task = tasks.pop()\nprint('Working on popped task:', current_task)\nprint('Remaining tasks in queue:', tasks)",
                    "expected_output": "Working on popped task: Meeting\nRemaining tasks in queue: ['Email', 'Report']",
                    "explanation_en": "tasks.pop() extracts 'Meeting' from the list and returns it.",
                    "explanation_hi": "pop() ne 'Meeting' nikaal kar current_task me store kar diya."
                },
                "example_2": {
                    "title": "Remove by Value and Clear",
                    "title_hi": "Value se remove aur poori list clear",
                    "code": "cart = ['Apple', 'Soda', 'Apple']\ncart.remove('Apple')  # Removes first Apple only\nprint('After remove first apple:', cart)\ncart.clear()\nprint('After clear:', cart)",
                    "expected_output": "After remove first apple: ['Soda', 'Apple']\nAfter clear: []",
                    "explanation_en": "remove() eliminates the first match; clear() empties the entire list.",
                    "explanation_hi": "remove ne pehla Apple hataya, clear ne poori list khali kar di."
                },
                "challenge": {
                    "prompt_en": "Given inventory = ['Sword', 'Shield', 'Potion'], pop the last item and print: Popped: Potion",
                    "prompt_hi": "inventory = ['Sword', 'Shield', 'Potion'] se aakhri item pop karo aur print karo: Popped: Potion",
                    "starter_code": "inventory = ['Sword', 'Shield', 'Potion']\n# Pop and print:\n",
                    "expected_output": "Popped: Potion",
                    "solution_code": "inventory = ['Sword', 'Shield', 'Potion']\nitem = inventory.pop()\nprint(f'Popped: {item}')",
                    "solution_explanation_en": "Pops the last item and formats output.",
                    "solution_explanation_hi": "Aakhri item pop karke print karta hai.",
                    "hints": ["item = inventory.pop()\\nprint(f'Popped: {item}')"],
                    "ego_roast_hi": "pop() lagana nahi aaya?",
                    "ego_cheer_hi": "List cleanup and deletion mastered! 🗑️"
                }
            },
            {
                "id": "ch8_sub6_sorting_reversing",
                "title": "Sorting and reversing lists",
                "title_hi": "Lists ko sort aur reverse karna",
                "icon": "🔃",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Python provides both in-place modification methods (arr.sort() and arr.reverse()) and non-destructive built-in functions (sorted(arr) and reversed(arr)) to reorder elements.",
                "what_is_it_hi": "Python me sorting ke do tareeqe hain: list.sort() original list ko hi arrange kar deta hai, jabki sorted(list) original ko chhed bina ek nayi sorted list return karta hai.",
                "why_need_it_en": "Sorting leaderboard scores from highest to lowest, displaying e-commerce products alphabetically, or organizing dates.",
                "why_need_it_hi": "Leaderboard scores ko high to low lagana, products ko A to Z arrange karna, dates ko order me karna.",
                "how_to_use_en": "In-place: arr.sort(reverse=True). Non-destructive: new_arr = sorted(arr).",
                "how_to_use_hi": "arr.sort() original badalta hai; sorted(arr) nayi list deta hai.",
                "syntax": "# In-place modification:\nnums = [4, 1, 3]\nnums.sort()              # nums is now [1, 3, 4]\nnums.sort(reverse=True)  # nums is now [4, 3, 1]\nnums.reverse()           # Just flips order\n\n# Non-destructive:\nnew_sorted = sorted([4, 1, 3])",
                "rules_en": [
                    "list.sort() returns None! It mutates the list in-place.",
                    "sorted(list) returns a brand new sorted list; the original remains unchanged.",
                    "Elements must be comparable: sorting a list with mixed numbers and strings throws TypeError."
                ],
                "rules_hi": [
                    "list.sort() None return karta hai, original list ko update karta hai.",
                    "sorted(list) ek nayi sorted list return karta hai, original waise hi rehti hai.",
                    "Number aur string mix list ko sort karne par TypeError aayega."
                ],
                "analogy_en": "arr.sort() is rearranging your books directly on your shelf. sorted(arr) is taking a photo of the books and digitally sorting the photo.",
                "analogy_hi": "sort() almirah me jaakar kitabein re-arrange karne jaisa hai. sorted() kitabon ki photo kheench kar phone me sort karne jaisa hai.",
                "common_mistakes": [
                    {
                        "mistake": "Assigning result of sort: my_list = my_list.sort()",
                        "why_it_fails_en": "my_list becomes None! sort() mutates in-place and returns None.",
                        "why_it_fails_hi": "my_list.sort() None return karta hai, to my_list gayab hokar None ban jayegi!",
                        "fix": "Either call my_list.sort() alone, or write my_list = sorted(my_list)."
                    }
                ],
                "example_1": {
                    "title": "In-Place Sort vs Built-in Sorted",
                    "title_hi": "sort() vs sorted() ka live farak",
                    "code": "raw_scores = [45, 12, 89, 32]\n# Non-destructive\nnew_scores = sorted(raw_scores)\nprint('Original untouched:', raw_scores)\nprint('New sorted copy:', new_scores)",
                    "expected_output": "Original untouched: [45, 12, 89, 32]\nNew sorted copy: [12, 32, 45, 89]",
                    "explanation_en": "sorted() left raw_scores completely intact while creating new_scores.",
                    "explanation_hi": "sorted() ne original list ko chhede bina nayi sorted copy banayi."
                },
                "example_2": {
                    "title": "Descending Sort with reverse=True",
                    "title_hi": "Descending order me sort karna",
                    "code": "rankings = [3, 1, 4, 2]\nrankings.sort(reverse=True)\nprint('Leaderboard rankings:', rankings)",
                    "expected_output": "Leaderboard rankings: [4, 3, 2, 1]",
                    "explanation_en": "sort(reverse=True) sorts from highest to lowest.",
                    "explanation_hi": "reverse=True se highest se lowest order me sort ho jata hai."
                },
                "challenge": {
                    "prompt_en": "Sort marks = [50, 20, 80] in ascending order using .sort() and print the list: [20, 50, 80]",
                    "prompt_hi": "marks = [50, 20, 80] ko .sort() se sort karke print karo: [20, 50, 80]",
                    "starter_code": "marks = [50, 20, 80]\n# Sort in-place and print:\n",
                    "expected_output": "[20, 50, 80]",
                    "solution_code": "marks = [50, 20, 80]\nmarks.sort()\nprint(marks)",
                    "solution_explanation_en": "Sorts marks in ascending order in-place.",
                    "solution_explanation_hi": "marks.sort() karke print karta hai.",
                    "hints": ["marks.sort() then print(marks)"],
                    "ego_roast_hi": "my_list = my_list.sort() to nahi likh diya?",
                    "ego_cheer_hi": "Sorting algorithm executed! 🔃"
                }
            },
            {
                "id": "ch8_sub7_list_functions",
                "title": "List functions (len(), max(), min(), sum())",
                "title_hi": "List functions (len(), max(), min(), sum())",
                "icon": "📊",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Python provides high-speed built-in C-optimized statistical functions: len() returns item count; max() finds highest value; min() finds lowest value; sum() computes total sum.",
                "what_is_it_hi": "Python me superfast built-in functions hote hain: len() items ki ginti batata hai, max() sabse bada number nikaalta hai, min() sabse chhota number nikaalta hai, aur sum() sabhi numbers ka total jod nikaalta hai.",
                "why_need_it_en": "Calculating student averages: avg = sum(marks) / len(marks), or finding the highest price on an e-commerce page: max(prices).",
                "why_need_it_hi": "Average nikaalna: sum(marks) / len(marks). Sabse mehenga product dhoondna: max(prices).",
                "how_to_use_en": "len(arr), max(arr), min(arr), sum(arr).",
                "how_to_use_hi": "len(x), max(x), min(x), sum(x) seedhe call karo.",
                "syntax": "nums = [10, 20, 30, 40]\ncount = len(nums)      # 4\nhighest = max(nums)    # 40\nlowest = min(nums)     # 10\ntotal = sum(nums)      # 100\naverage = sum(nums) / len(nums)  # 25.0",
                "rules_en": [
                    "sum() works strictly on numbers (int, float). Passing strings causes TypeError.",
                    "max() and min() work on strings too (evaluates lexicographical ASCII/Unicode order: max(['a', 'z']) is 'z').",
                    "Calling max(), min(), or sum() on an empty list [] raises ValueError (except sum which returns 0)."
                ],
                "rules_hi": [
                    "sum() sirf numbers par chalta hai, string par TypeError aayega.",
                    "max() aur min() strings par bhi chalte hain (A to Z order me).",
                    "Khali list [] par max() ya min() lagane par ValueError aayega."
                ],
                "analogy_en": "A business dashboard showing Total Sales (sum), Best Selling Product (max), and Transaction Count (len).",
                "analogy_hi": "Dukan ke ledger jaisa — kul bikri (sum), sabse bada bill (max), aur kitne grahak aaye (len).",
                "common_mistakes": [
                    {
                        "mistake": "Naming your variable 'sum' or 'max' or 'min': sum = sum(nums)",
                        "why_it_fails_en": "Shadows the built-in function! You can never call sum() again in that scope.",
                        "why_it_fails_hi": "built-in function ke naam se variable banane par built-in function override ho jata hai.",
                        "fix": "Use descriptive names like total_sum = sum(nums)."
                    }
                ],
                "example_1": {
                    "title": "Grade Point Average Calculation",
                    "title_hi": "Class Average aur Max Score nikaalna",
                    "code": "marks = [85, 92, 78, 96, 89]\ntotal = sum(marks)\navg = total / len(marks)\nprint(f'Max: {max(marks)} | Min: {min(marks)} | Average: {avg:.1f}')",
                    "expected_output": "Max: 96 | Min: 78 | Average: 88.0",
                    "explanation_en": "Computes max, min, and mean with 3 clean one-liners.",
                    "explanation_hi": "max, min aur average 3 lines me calculate karta hai."
                },
                "example_2": {
                    "title": "Lexicographical String Min/Max",
                    "title_hi": "Strings me se min aur max nikaalna",
                    "code": "words = ['apple', 'zebra', 'banana']\nprint('Alphabetical first (min):', min(words))\nprint('Alphabetical last (max):', max(words))",
                    "expected_output": "Alphabetical first (min): apple\nAlphabetical last (max): zebra",
                    "explanation_en": "min() finds alphabetically earliest; max() finds alphabetically latest.",
                    "explanation_hi": "min() pehla aur max() aakhri alphabetical word dhoondta hai."
                },
                "challenge": {
                    "prompt_en": "Given test_scores = [10, 20, 30], compute and print: Sum: 60 | Count: 3",
                    "prompt_hi": "test_scores = [10, 20, 30] se print karo: Sum: 60 | Count: 3",
                    "starter_code": "test_scores = [10, 20, 30]\n# Print sum and len:\n",
                    "expected_output": "Sum: 60 | Count: 3",
                    "solution_code": "test_scores = [10, 20, 30]\nprint(f'Sum: {sum(test_scores)} | Count: {len(test_scores)}')",
                    "solution_explanation_en": "Uses sum() and len() in an f-string.",
                    "solution_explanation_hi": "sum aur len se formatted string print karta hai.",
                    "hints": ["sum(test_scores) and len(test_scores)"],
                    "ego_roast_hi": "sum aur len nikaalna bhool gaye?",
                    "ego_cheer_hi": "Statistical calculations verified! 📊"
                }
            },
            {
                "id": "ch8_sub8_nested_lists",
                "title": "Nested lists (2D grids and matrices)",
                "title_hi": "Nested lists (2D grids aur matrices)",
                "icon": "🏁",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "A nested list is a list containing other lists as its elements. In mathematics and computer science, this represents a 2D matrix, table, or grid with rows and columns: matrix[row][col].",
                "what_is_it_hi": "Nested list ka matlab hota hai list ke andar aur lists. Ye maths aur coding me 2D matrix ya table (rows aur columns) banata hai. Element access karne ke liye do brackets lagte hain: matrix[row][col].",
                "why_need_it_en": "Tic-Tac-Toe boards, chess grids, pixel matrices in image processing, and CSV spreadsheet rows.",
                "why_need_it_hi": "Tic-Tac-Toe board (3x3), Chessboard (8x8), Excel spreadsheet rows, images ke pixels.",
                "how_to_use_en": "grid[0][1] gets row 0, column 1.",
                "how_to_use_hi": "grid[r][c] se row aur column ka data milta hai.",
                "syntax": "matrix = [\n    [1, 2, 3],  # Row 0\n    [4, 5, 6],  # Row 1\n    [7, 8, 9]   # Row 2\n]\ncenter_val = matrix[1][1]  # 5",
                "rules_en": [
                    "First index matrix[i] selects the entire ROW (a list).",
                    "Second index matrix[i][j] selects the specific COLUMN element inside that row.",
                    "Traverse 2D matrices using nested for loops (for row in matrix: for val in row:)."
                ],
                "rules_hi": [
                    "Pehla index matrix[i] poori ROW select karta hai.",
                    "Doosra index matrix[i][j] us row ke andar ka COLUMN element deta hai.",
                    "2D list par ghoomne ke liye nested for loops lagte hain."
                ],
                "analogy_en": "A tic-tac-toe grid or an apartment building with floors (rows) and room numbers (columns).",
                "analogy_hi": "Apartment building jaisa: Pehla index floor number (Row), doosra index room number (Column).",
                "common_mistakes": [
                    {
                        "mistake": "Reversing index order: matrix[col][row]",
                        "why_it_fails_en": "Python follows Row-Major order: matrix[row][column]. Reversing will access the wrong element or cause IndexError.",
                        "why_it_fails_hi": "Pehle row hoti hai fir column hota hai [row][col]. Ulta karne par galat data aayega.",
                        "fix": "Always remember [Row][Column] (RC Cola or Remote Control)."
                    }
                ],
                "example_1": {
                    "title": "Tic-Tac-Toe 3x3 Grid State",
                    "title_hi": "Tic-Tac-Toe board nested list me",
                    "code": "board = [\n    ['X', 'O', 'X'],\n    ['O', 'X', 'O'],\n    ['O', 'X', 'X']\n]\nprint('Top-left corner:', board[0][0])\nprint('Center piece:', board[1][1])",
                    "expected_output": "Top-left corner: X\nCenter piece: X",
                    "explanation_en": "board[0][0] targets row 0 col 0; board[1][1] targets row 1 col 1.",
                    "explanation_hi": "board[0][0] aur board[1][1] se exact positions read karta hai."
                },
                "example_2": {
                    "title": "Iterating Over a 2D Grid",
                    "title_hi": "2D Grid par nested loop chalana",
                    "code": "grid = [[1, 2], [3, 4]]\nfor row in grid:\n    for val in row:\n        print(val, end=' ')\nprint()",
                    "expected_output": "1 2 3 4 ",
                    "explanation_en": "Flattens the 2D grid display using nested iteration.",
                    "explanation_hi": "Nested loops se saare 2D elements ek-ek karke print karta hai."
                },
                "challenge": {
                    "prompt_en": "Given matrix = [[1, 2], [3, 4]], access and print the element 4 using matrix[1][1]: 4",
                    "prompt_hi": "matrix = [[1, 2], [3, 4]] se matrix[1][1] access karke print karo: 4",
                    "starter_code": "matrix = [[1, 2], [3, 4]]\n# Print bottom-right item (4):\n",
                    "expected_output": "4",
                    "solution_code": "matrix = [[1, 2], [3, 4]]\nprint(matrix[1][1])",
                    "solution_explanation_en": "matrix[1][1] accesses row 1, col 1, which holds 4.",
                    "solution_explanation_hi": "matrix[1][1] se 4 print hota hai.",
                    "hints": ["print(matrix[1][1])"],
                    "ego_roast_hi": "2D indexing me bhatak gaye kya?",
                    "ego_cheer_hi": "2D matrix mastery unlocked! 🏁"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 9: The Unchanging List (Tuples)
    # =========================================================================
    {
        "id": "ch9_tuples",
        "part_number": 3,
        "part_title": "PART 3: ORGANIZING LOTS OF DATA (DATA STRUCTURES)",
        "chapter_number": 9,
        "title": "Chapter 9: The Unchanging List (Tuples)",
        "subtitle_en": "Immutability, parentheses syntax, packing, unpacking, and when to use tuples over lists",
        "subtitle_hi": "Immutability, parentheses syntax, tuple packing, unpacking aur list se farak",
        "icon": "🔒",
        "estimated_time": "30 mins",
        "prerequisites_en": "Chapter 8 (Lists and indexing).",
        "prerequisites_hi": "Chapter 8 (Lists aur indexing).",
        "learning_objectives_en": [
            "Understand tuple immutability and memory protection",
            "Create tuples with and without parentheses (and the single-item comma rule)",
            "Master tuple packing and unpacking",
            "Know exactly when to choose a tuple instead of a list (dictionary keys, fixed records)"
        ],
        "learning_objectives_hi": [
            "Tuple immutability aur security samjho",
            "Bina parentheses ke tuple banana aur single-item comma rule",
            "Tuple packing aur unpacking master karo",
            "List aur Tuple me sahi choice kab karni hai"
        ],
        "recap_en": "You mastered tuples: why immutability matters for safety, syntax nuances, parallel unpacking, and performance advantages over lists.",
        "recap_hi": "Aapne tuples ki immutability, syntax, unpacking aur lists se comparative benefits seekhe.",
        "subtopics": [
            {
                "id": "ch9_sub1_what_is_a_tuple",
                "title": "What is a tuple and how is it different from a list? (Immutability)",
                "title_hi": "Tuple kya hota hai aur list se kaise alag hai? (Immutability)",
                "icon": "🛡️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A tuple is an ordered collection of items enclosed in parentheses (). Unlike lists, tuples are 100% IMMUTABLE: once created, items cannot be modified, added, removed, or rearranged.",
                "what_is_it_hi": "Tuple parentheses () me band ek ordered collection hota hai jo 100% IMMUTABLE (kabhi na badalne wala) hota hai. Ek baar ban gaya to usme na item jud sakta hai, na delete ho sakta hai, na change ho sakta hai.",
                "why_need_it_en": "Data integrity: GPS coordinates (latitude, longitude), RGB colors (255, 0, 0), and database primary keys must NEVER be accidentally modified by bugs.",
                "why_need_it_hi": "Data safety: GPS coordinates, screen resolution (1920, 1080), aur RGB colors galti se bhi code me change na ho jayein, isliye tuple use karte hain.",
                "how_to_use_en": "coords = (28.7041, 77.1025). Attempting coords[0] = 30 throws TypeError.",
                "how_to_use_hi": "coords = (28.7, 77.1). Agar coords[0] = 30 karoge to TypeError aa jayega.",
                "syntax": "point = (10, 20)\n# point[0] = 15  # ERROR: TypeError: 'tuple' object does not support item assignment",
                "rules_en": [
                    "Tuples use parentheses (), whereas lists use square brackets [].",
                    "Tuples cannot be mutated in-place (no append, insert, remove, pop, or sort methods).",
                    "Tuples are faster and use less memory than lists.",
                    "Because tuples are immutable, they CAN be used as dictionary keys (lists cannot!)."
                ],
                "rules_hi": [
                    "Tuples me gol brackets () lagte hain, lists me square [].",
                    "Tuple me append, pop, sort jaise methods nahi hote.",
                    "Tuples memory kam lete hain aur list se fast hote hain.",
                    "Tuples ko dictionary keys ke roop me use kiya ja sakta hai."
                ],
                "analogy_en": "A list is a pencil sketch (you can erase and redraw anytime). A tuple is an engraved stone monument carved with a chisel.",
                "analogy_hi": "List pencil se likha paper hai jise eraser se mita sakte ho. Tuple patthar par khuda hua shilalekh hai jo badla nahi ja sakta.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to call t.append(5) on a tuple.",
                        "why_it_fails_en": "AttributeError: 'tuple' object has no attribute 'append'.",
                        "why_it_fails_hi": "Tuple immutable hai, usme append naam ka method hota hi nahi.",
                        "fix": "Use a list if you need to append, or concatenate a new tuple: t = t + (5,)."
                    }
                ],
                "example_1": {
                    "title": "Creating and Reading a Tuple",
                    "title_hi": "Tuple banana aur read karna",
                    "code": "screen_res = (1920, 1080)\nprint('Width:', screen_res[0], '| Height:', screen_res[1])",
                    "expected_output": "Width: 1920 | Height: 1080",
                    "explanation_en": "Accesses tuple elements via standard bracket indexing.",
                    "explanation_hi": "Standard index se tuple ke elements ko read karta hai."
                },
                "example_2": {
                    "title": "Tuple Immutability Protection",
                    "title_hi": "Immutability se error protection",
                    "code": "rgb_color = (255, 128, 0)\ntry:\n    rgb_color[0] = 0\nexcept TypeError as e:\n    print('Protection triggered:', e)",
                    "expected_output": "Protection triggered: 'tuple' object does not support item assignment",
                    "explanation_en": "Catches and displays the TypeError protecting tuple contents from mutation.",
                    "explanation_hi": "Dikhata hai ki Python tuple me mutation hone hi nahi deta."
                },
                "challenge": {
                    "prompt_en": "Create a tuple coords = (12.5, 77.2) and print: Coordinates: (12.5, 77.2)",
                    "prompt_hi": "coords = (12.5, 77.2) banao aur print karo: Coordinates: (12.5, 77.2)",
                    "starter_code": "# Create tuple and print:\n",
                    "expected_output": "Coordinates: (12.5, 77.2)",
                    "solution_code": "coords = (12.5, 77.2)\nprint(f'Coordinates: {coords}')",
                    "solution_explanation_en": "Creates and prints a tuple.",
                    "solution_explanation_hi": "Tuple bana kar print karta hai.",
                    "hints": ["coords = (12.5, 77.2)"],
                    "ego_roast_hi": "Tuple banana bhool gaye?",
                    "ego_cheer_hi": "Immutable tuple created! 🛡️"
                }
            },
            {
                "id": "ch9_sub2_creating_tuples",
                "title": "Creating tuples (with and without parentheses)",
                "title_hi": "Tuples banana (with aur without parentheses)",
                "icon": "📦",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Tuples can be created with parentheses (1, 2) OR simply separated by commas without any parentheses: t = 1, 2. The COMMA is what actually defines a tuple in Python! A single-item tuple REQUIRES a trailing comma: single = (42,).",
                "what_is_it_hi": "Tuples bina brackets ke bhi sirf comma lagakar banaye ja sakte hain: t = 1, 2. Python me tuple bracket se nahi COMMA se banta hai! Single item ka tuple banane ke liye comma lagana MANDATORY hai: (42,).",
                "why_need_it_en": "If you write x = (42) without a comma, Python evaluates it as a simple integer inside math parentheses! Writing x = (42,) makes it an official tuple.",
                "why_need_it_hi": "Agar comma nahi lagaya (42), to Python use normal number 42 samajhta hai! (42,) likhne par hi tuple banta hai.",
                "how_to_use_en": "Multiple items: t = 1, 2, 3. Single item: single = (99,).",
                "how_to_use_hi": "t = 1, 2, 3 ya single item ke liye (99,).",
                "syntax": "# With parentheses:\nt1 = (1, 2, 3)\n# Without parentheses (Tuple packing):\nt2 = 1, 2, 3\n# Single item tuple (COMMA MANDATORY!):\nsingle_tuple = (42,)\nnot_a_tuple = (42)  # This is just an int!",
                "rules_en": [
                    "CRITICAL LAW: A single-item tuple MUST have a trailing comma: (x,). Without the comma, it is just parentheses around a value.",
                    "Parentheses are optional when defining tuples, except for empty tuple () or when needed to resolve syntax ambiguity.",
                    "type((42,)) is <class 'tuple'>; type((42)) is <class 'int'>."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: Single item tuple me aakhri me comma lagana MANDATORY hai: (x,).",
                    "Khali tuple ke liye () lagana padta hai.",
                    "type((42,)) tuple hai; type((42)) int hai!"
                ],
                "analogy_en": "Wrapping a single gift requires tape (the comma). Without tape, the wrapping paper falls off and you just have the item.",
                "analogy_hi": "Gift pack karne par ribbon lagane jaisa — comma nahi lagaya to packaging khul kar normal number ban jayegi.",
                "common_mistakes": [
                    {
                        "mistake": "Creating a single-element tuple without a comma: item = (50)",
                        "why_it_fails_en": "type(item) will be int, not tuple! Mathematical parentheses are treated as grouping, not tuple constructors.",
                        "why_it_fails_hi": "Python ise math ka bracket samajh kar number 50 bana deta hai.",
                        "fix": "Always add a trailing comma: item = (50,)."
                    }
                ],
                "example_1": {
                    "title": "Single-Item Tuple vs Integer",
                    "title_hi": "Comma ka jaadu (Tuple vs Int)",
                    "code": "a = (42)\nb = (42,)\nprint('Type of a:', type(a).__name__)\nprint('Type of b:', type(b).__name__)",
                    "expected_output": "Type of a: int\nType of b: tuple",
                    "explanation_en": "Shows how the trailing comma transforms an integer into a tuple.",
                    "explanation_hi": "Dikhata hai ki aakhri comma lagane se integer tuple ban jata hai."
                },
                "example_2": {
                    "title": "Tuple Without Parentheses",
                    "title_hi": "Bina brackets ke tuple banana",
                    "code": "point = 10, 20, 30\nprint('Point value:', point, '| Type:', type(point).__name__)",
                    "expected_output": "Point value: (10, 20, 30) | Type: tuple",
                    "explanation_en": "Commas alone are sufficient to construct a tuple.",
                    "explanation_hi": "Sirf comma lagane se bhi tuple ban jata hai."
                },
                "challenge": {
                    "prompt_en": "Create a single-item tuple with value 'solo' and print its type name: tuple",
                    "prompt_hi": "'solo' ka single-item tuple bana kar uska type name print karo: tuple",
                    "starter_code": "# Create single-item tuple and print type name:\n",
                    "expected_output": "tuple",
                    "solution_code": "t = ('solo',)\nprint(type(t).__name__)",
                    "solution_explanation_en": "Uses trailing comma ('solo',) to create a single-element tuple.",
                    "solution_explanation_hi": "Trailing comma lagakar tuple banata hai.",
                    "hints": ["t = ('solo',)\\nprint(type(t).__name__)"],
                    "ego_roast_hi": "Trailing comma bhool gaye?",
                    "ego_cheer_hi": "Tuple comma law mastered! 📦"
                }
            },
            {
                "id": "ch9_sub3_packing_unpacking",
                "title": "Tuple packing and unpacking",
                "title_hi": "Tuple packing aur unpacking",
                "icon": "🎁",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Tuple packing is grouping multiple values into a single tuple (record = 'Alex', 21, 'CS'). Tuple unpacking is extracting those values back into distinct variables in one clean line (name, age, dept = record).",
                "what_is_it_hi": "Packing ka matlab multiple values ko ek tuple me pack karna (data = 1, 2, 3). Unpacking ka matlab us tuple ko khol kar har value ko alag-alag variable me nikaalna (x, y, z = data).",
                "why_need_it_en": "Functions that return multiple values in Python are actually packing and returning a tuple! Unpacking lets you receive them into separate variables effortlessly.",
                "why_need_it_hi": "Jab koi Python function ek sath do values return karta hai (return x, y), to wo asal me tuple return karta hai jise unpacking se alag karte hain.",
                "how_to_use_en": "name, age = ('Alex', 20). Using asterisk for rest: first, *rest = (1, 2, 3, 4).",
                "how_to_use_hi": "x, y = (10, 20). Baaki items ke liye *rest: a, *b = (1, 2, 3).",
                "syntax": "# Packing:\nperson = \"Sara\", 25, \"Developer\"\n# Unpacking:\nname, age, job = person",
                "rules_en": [
                    "The number of variables on the left MUST match the number of tuple items, or ValueError occurs.",
                    "Extended unpacking using an asterisk (*var) captures variable-length remainders as a list.",
                    "Powers atomic variable swapping: a, b = b, a."
                ],
                "rules_hi": [
                    "Left side ke variables aur right side ke items barabar hone chahiye, warna ValueError aayega.",
                    "Asterisk (*rest) lagane se bache hue saare items ek list me pack ho jaate hain.",
                    "Variable swap (a, b = b, a) isi par chalta hai."
                ],
                "analogy_en": "Packing a travel suitcase before a trip, and unpacking each shirt into the hotel wardrobe upon arrival.",
                "analogy_hi": "Suitcase pack karne jaisa — kapde daal kar band kiya (packing), hotel pahunch kar har kapda alag shelf me rakha (unpacking).",
                "common_mistakes": [
                    {
                        "mistake": "Unmatched variable count: a, b = (1, 2, 3)",
                        "why_it_fails_en": "ValueError: too many values to unpack (expected 2).",
                        "why_it_fails_hi": "Do variables me 3 values fit nahi ho sakti.",
                        "fix": "Either match variable count, or use *rest: a, *rest = (1, 2, 3)."
                    }
                ],
                "example_1": {
                    "title": "Classic Record Unpacking",
                    "title_hi": "Student record unpack karna",
                    "code": "student_data = ('Pooja', 101, 'CSE')\nname, roll, branch = student_data\nprint(f'Student: {name} | Roll: {roll} | Branch: {branch}')",
                    "expected_output": "Student: Pooja | Roll: 101 | Branch: CSE",
                    "explanation_en": "Unpacks 3 elements into 3 distinct variables.",
                    "explanation_hi": "Teeno elements ko 3 alag variables me unpack karta hai."
                },
                "example_2": {
                    "title": "Extended Unpacking with Asterisk (*)",
                    "title_hi": "Asterisk (*) se bache hue items pack karna",
                    "code": "grades = (95, 88, 72, 65, 50)\ntop_score, *other_scores = grades\nprint('Topper:', top_score)\nprint('Rest of class:', other_scores)",
                    "expected_output": "Topper: 95\nRest of class: [88, 72, 65, 50]",
                    "explanation_en": "top_score grabs 95; *other_scores gathers all remaining elements into a list.",
                    "explanation_hi": "Pehla topper me gaya, baaki saare list bankar other_scores me chale gaye."
                },
                "challenge": {
                    "prompt_en": "Unpack pair = (100, 200) into a and b, and print: a=100 b=200",
                    "prompt_hi": "pair = (100, 200) ko a aur b me unpack karo aur print karo: a=100 b=200",
                    "starter_code": "pair = (100, 200)\n# Unpack and print:\n",
                    "expected_output": "a=100 b=200",
                    "solution_code": "pair = (100, 200)\na, b = pair\nprint(f'a={a} b={b}')",
                    "solution_explanation_en": "Unpacks pair into a and b.",
                    "solution_explanation_hi": "pair ko a aur b me unpack karta hai.",
                    "hints": ["a, b = pair"],
                    "ego_roast_hi": "Unpacking me galti kar di?",
                    "ego_cheer_hi": "Tuple unpacking mastery! 🎁"
                }
            },
            {
                "id": "ch9_sub4_when_to_use_tuples",
                "title": "When to use a tuple instead of a list",
                "title_hi": "List ke badle Tuple kab use karein?",
                "icon": "⚖️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Rule of Thumb: Use LISTS for homogenous collections that will grow or change (shopping cart, comments). Use TUPLES for heterogeneous fixed records that must NEVER change (database rows, coordinates, dictionary keys).",
                "what_is_it_hi": "Golden Rule: LIST tab use karo jab data badalna ho (cart items, active users). TUPLE tab use karo jab data fixed aur permanent ho (GPS coordinates, database primary key, dictionary keys).",
                "why_need_it_en": "Tuples provide defensive programming (guarantees other functions won't mutate your data) and allow hashability (can be keys in dictionaries).",
                "why_need_it_hi": "Tuples se code secure banta hai (koi galti se data change nahi kar sakta) aur ye dictionary ke keys ban sakte hain.",
                "how_to_use_en": "Dict key: location_map[(28.7, 77.1)] = 'New Delhi'. A list would crash with TypeError: unhashable type.",
                "how_to_use_hi": "Dictionary key ke liye tuple lagao: points[(0, 0)] = 'Origin'. List crash karegi.",
                "syntax": "# TUPLE AS DICTIONARY KEY (Valid because immutable):\nlocations = {}\nlocations[(12.97, 77.59)] = \"Bangalore\"\n\n# LIST AS KEY (Crashes with TypeError!):\n# locations[[12.97, 77.59]] = \"Error\"",
                "rules_en": [
                    "Tuples are HASHABLE (if all elements inside are hashable) -> Can be dict keys and set elements.",
                    "Lists are UNHASHABLE -> Cannot be dict keys or set elements.",
                    "Tuples use less RAM and allocate faster than lists."
                ],
                "rules_hi": [
                    "Tuples HASHABLE hote hain -> Dictionary keys aur Sets me use ho sakte hain.",
                    "Lists UNHASHABLE hoti hain -> Dictionary keys nahi ban sakti.",
                    "Tuples RAM kam lete hain aur fast chalte hain."
                ],
                "analogy_en": "A shopping cart is a list (you add and remove groceries). A passport number with birthdate is a tuple (permanent identity).",
                "analogy_hi": "Shopping list ek list hai (item jodo ya kaato). Aadhar card number aur date of birth ek tuple hai (hamesha permanent).",
                "common_mistakes": [
                    {
                        "mistake": "Using a list as a dictionary key: cache[[1, 2]] = 'result'.",
                        "why_it_fails_en": "TypeError: unhashable type: 'list'. Lists can change, so Python cannot calculate a permanent hash address.",
                        "why_it_fails_hi": "List mutable hai, isliye Python uska permanent hash address nahi bana pata aur TypeError de deta hai.",
                        "fix": "Use a tuple as the key: cache[(1, 2)] = 'result'."
                    }
                ],
                "example_1": {
                    "title": "Tuple as a Dictionary Key (Coordinates Map)",
                    "title_hi": "Tuple ko Dictionary Key banana (Coordinates Map)",
                    "code": "city_locations = {}\ncity_locations[(28.6139, 77.2090)] = 'New Delhi'\ncity_locations[(19.0760, 72.8777)] = 'Mumbai'\nprint('Delhi coordinates lookup:', city_locations[(28.6139, 77.2090)])",
                    "expected_output": "Delhi coordinates lookup: New Delhi",
                    "explanation_en": "Because tuples are immutable and hashable, they can serve as multi-part keys in dictionaries.",
                    "explanation_hi": "Tuple immutable aur hashable hota hai, isliye coordinates ko dictionary ki key banakar store kiya ja sakta hai."
                },
                "example_2": {
                    "title": "Data Integrity Protection in Critical Records",
                    "title_hi": "Critical Records me Data Integrity Protection",
                    "code": "db_row = (101, 'admin', 'supersecret_hash')\n# db_row[1] = 'hacker' -> TypeError: 'tuple' object does not support item assignment\nprint(f'Protected DB record ID={db_row[0]}, Role={db_row[1]}')",
                    "expected_output": "Protected DB record ID=101, Role=admin",
                    "explanation_en": "Tuples guarantee that critical read-only database records cannot be mutated in place by downstream functions.",
                    "explanation_hi": "Tuples guarantee karte hain ki koi bhi function beech me aakar record ko alter nahi kar sakta."
                },
                "challenge": {
                    "prompt_en": "Create a dictionary named locations. Add an entry with key (10, 20) and value 'Base'. Print: Base at: Base",
                    "prompt_hi": "locations naam ki dictionary banao. Key (10, 20) aur value 'Base' add karo. Print karo: Base at: Base",
                    "starter_code": "locations = {}\n# Add key (10, 20) with value 'Base' and print:\n",
                    "expected_output": "Base at: Base",
                    "solution_code": "locations = {}\nlocations[(10, 20)] = 'Base'\nprint(f'Base at: {locations[(10, 20)]}')",
                    "solution_explanation_en": "Uses an immutable tuple as a dictionary key and retrieves its value.",
                    "solution_explanation_hi": "Immutable tuple ko dictionary key banata hai aur uski value print karta hai.",
                    "hints": ["locations[(10, 20)] = 'Base'\\nprint(f'Base at: {locations[(10, 20)]}')"],
                    "ego_roast_hi": "Tuple ko dictionary key banana bhool gaye?",
                    "ego_cheer_hi": "Tuple vs List wisdom achieved! ⚖️"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 10: The Dictionary (Key-Value Pairs)
    # =========================================================================
    {
        "id": "ch10_dictionaries",
        "part_number": 3,
        "part_title": "PART 3: ORGANIZING LOTS OF DATA (DATA STRUCTURES)",
        "chapter_number": 10,
        "title": "Chapter 10: The Dictionary (Key-Value Pairs)",
        "subtitle_en": "Hash maps, keys vs values, safe lookups with get(), dictionary looping, and nested structures",
        "subtitle_hi": "Dictionary: Key-Value pairs, get() se safe lookup, looping aur nested data",
        "icon": "📖",
        "estimated_time": "40 mins",
        "prerequisites_en": "Chapters 8 & 9 (Lists and tuples).",
        "prerequisites_hi": "Chapter 8 aur 9 (Lists aur tuples).",
        "learning_objectives_en": [
            "Understand the Hash Map (Key-Value) mental model",
            "Create dictionaries and enforce valid immutable keys",
            "Add, update, and delete dictionary elements",
            "Use .get() to prevent KeyError crashes",
            "Loop across .keys(), .values(), and .items()",
            "Construct and navigate nested JSON-like dictionaries"
        ],
        "learning_objectives_hi": [
            "Hash Map aur Key-Value ka mental model seekho",
            "Dictionary banana aur immutable keys ke niyam",
            "Add, update, aur remove karna",
            "get() se bina crash huye safe lookup karna",
            "keys(), values(), aur items() par loop chalana",
            "Nested dictionaries aur JSON data handle karna"
        ],
        "recap_en": "You mastered Python dictionaries: key-value data modeling, O(1) lookups, get() error-handling, dictionary iteration, and complex nested data structures.",
        "recap_hi": "Aapne dictionaries ki key-value pairing, get() method, dictionary loops aur nested data structures master kiye.",
        "subtopics": [
            {
                "id": "ch10_sub1_what_is_a_dictionary",
                "title": "What is a dictionary? (Looking up definitions)",
                "title_hi": "Dictionary kya hoti hai? (Definitions dhoondna)",
                "icon": "📚",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A dictionary (dict) is an unordered (or insertion-ordered in Python 3.7+) collection of key-value pairs enclosed in curly braces {}. Instead of looking up items by numeric index (0, 1, 2), you look them up by a meaningful KEY (like 'name' or 'email').",
                "what_is_it_hi": "Dictionary curly braces {} me band Key-Value pairs ka collection hoti hai. List ki tarah number index (0, 1, 2) ke bajaye aap MEANINGFUL KEYS (jaise 'name', 'roll_no') se data dhoondte ho.",
                "why_need_it_en": "User profiles, database records, and web API responses (JSON) are all structured as key-value pairs.",
                "why_need_it_hi": "User profile, database records, aur web APIs ka data (JSON) sab kuch key-value format me hi hota hai.",
                "how_to_use_en": "user = {'name': 'Alex', 'age': 20}. Access with user['name'].",
                "how_to_use_hi": "Curly braces lagao: user = {'name': 'Alex', 'age': 20}. Data nikaalo: user['name'].",
                "syntax": "phonebook = {\n    \"police\": 100,\n    \"ambulance\": 102,\n    \"fire\": 101\n}\nemergency = phonebook[\"police\"]  # 100",
                "rules_en": [
                    "Keys must be UNIQUE: duplicate keys overwrite the previous value.",
                    "Keys must be IMMUTABLE/HASHABLE (strings, numbers, tuples). Lists cannot be keys!",
                    "Values can be anything: numbers, strings, lists, even other dictionaries."
                ],
                "rules_hi": [
                    "Keys hamesha UNIQUE honi chahiye: same key do baar likhoge to purani value overwrite ho jayegi.",
                    "Keys IMMUTABLE honi chahiye (strings, numbers, tuples). List key nahi ban sakti!",
                    "Values kuch bhi ho sakti hain: number, list, dictionary."
                ],
                "analogy_en": "An actual English dictionary: you search by word (Key) to read its meaning (Value). Or a phonebook: name (Key) -> phone number (Value).",
                "analogy_hi": "Asli English dictionary jaisi: word (Key) dekh kar uska matlab (Value) nikaal lete ho. Ya Phonebook: naam (Key) -> number (Value).",
                "common_mistakes": [
                    {
                        "mistake": "Using a list as a dictionary key: d = {[1, 2]: 'val'}",
                        "why_it_fails_en": "TypeError: unhashable type: 'list'. Keys must be immutable.",
                        "why_it_fails_hi": "List mutable hoti hai isliye dictionary key nahi ban sakti.",
                        "fix": "Use a tuple as the key: d = {(1, 2): 'val'}."
                    }
                ],
                "example_1": {
                    "title": "Creating and Accessing a Dictionary",
                    "title_hi": "Dictionary banana aur read karna",
                    "code": "student = {'name': 'Rohan', 'cgpa': 9.2, 'branch': 'CSE'}\nprint('Student Name:', student['name'])\nprint('Student CGPA:', student['cgpa'])",
                    "expected_output": "Student Name: Rohan\nStudent CGPA: 9.2",
                    "explanation_en": "Accesses dictionary values using their string keys.",
                    "explanation_hi": "Keys se values access karta hai."
                },
                "example_2": {
                    "title": "Fast O(1) Key Lookups",
                    "title_hi": "Instant key lookups",
                    "code": "caps = {'India': 'New Delhi', 'Japan': 'Tokyo'}\nprint('Capital of India:', caps['India'])",
                    "expected_output": "Capital of India: New Delhi",
                    "explanation_en": "Hash table lookups take constant O(1) time.",
                    "explanation_hi": "Hash table se 1 millisecond me capital mil jati hai."
                },
                "challenge": {
                    "prompt_en": "Create user = {'username': 'coder1', 'level': 5} and print: User coder1 is level 5",
                    "prompt_hi": "user = {'username': 'coder1', 'level': 5} banao aur print karo: User coder1 is level 5",
                    "starter_code": "# Create dict and print:\n",
                    "expected_output": "User coder1 is level 5",
                    "solution_code": "user = {'username': 'coder1', 'level': 5}\nprint(f\"User {user['username']} is level {user['level']}\")",
                    "solution_explanation_en": "Accesses username and level keys and formats output.",
                    "solution_explanation_hi": "Keys access karke print karta hai.",
                    "hints": ["user['username'] and user['level']"],
                    "ego_roast_hi": "Dictionary banana bhool gaye?",
                    "ego_cheer_hi": "Dictionary key-value model mastered! 📖"
                }
            },
            {
                "id": "ch10_sub2_keys_vs_values",
                "title": "Creating dictionaries and understanding keys vs. values",
                "title_hi": "Dictionary banana aur Keys vs Values ko samajhna",
                "icon": "🔑",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "In every key-value pair (key: value), the KEY is the unique address label used to find the data, and the VALUE is the actual stored payload.",
                "what_is_it_hi": "Har pair (key: value) me KEY wo address ya label hai jisse data dhoonda jaata hai, aur VALUE wo actual saman ya information hai jo store ki gayi hai.",
                "why_need_it_en": "Understanding the separation allows you to search specifically for keys (dict.keys()) or values (dict.values()).",
                "why_need_it_hi": "Is separation se aap sirf keys dekh sakte ho ya sirf values dekh sakte ho.",
                "how_to_use_en": "Use dict constructor or braces: profile = dict(name='Alex', age=20) or {'name': 'Alex', 'age': 20}.",
                "how_to_use_hi": "profile = {'name': 'Alex', 'age': 20} ya dict(name='Alex', age=20).",
                "syntax": "profile = {\n    \"id\": 101,              # Key is 'id', Value is 101\n    \"tags\": [\"py\", \"web\"]  # Value is a list!\n}",
                "rules_en": [
                    "Colon (:) separates each key from its value.",
                    "Comma (,) separates each key-value pair.",
                    "Values can be duplicate, but Keys MUST be unique."
                ],
                "rules_hi": [
                    "Colon (:) key aur value ke beech lagta hai.",
                    "Comma (,) har pair ke baad lagta hai.",
                    "Values same ho sakti hain (do logon ki age 20 ho sakti hai), lekin Keys unique honi chahiye."
                ],
                "analogy_en": "Bank locker: The key/number on the locker door is the KEY. The gold and papers locked inside is the VALUE.",
                "analogy_hi": "Bank locker jaisa: Locker ka number KEY hai, aur andar rakha sona VALUE hai.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to access by value instead of key: user[20] instead of user['age']",
                        "why_it_fails_en": "KeyError: 20. Python dictionaries only look up by key, never by value directly.",
                        "why_it_fails_hi": "Dictionary me search hamesha key se hoti hai value se nahi.",
                        "fix": "Always supply the key: user['age']."
                    }
                ],
                "example_1": {
                    "title": "Keys and Values Inspection",
                    "title_hi": "Keys aur Values alag-alag dekhna",
                    "code": "car = {'brand': 'Tesla', 'model': 'Model 3', 'year': 2024}\nprint('Keys:', list(car.keys()))\nprint('Values:', list(car.values()))",
                    "expected_output": "Keys: ['brand', 'model', 'year']\nValues: ['Tesla', 'Model 3', 2024]",
                    "explanation_en": "Separates the dictionary into its distinct keys and values lists.",
                    "explanation_hi": "Keys aur values ko alag-alag list me badal kar dikhata hai."
                },
                "example_2": {
                    "title": "Duplicate Values with Unique Keys",
                    "title_hi": "Same values allowed hain",
                    "code": "ages = {'Alice': 20, 'Bob': 20}\nprint('Both share age 20:', ages['Alice'] == ages['Bob'])",
                    "expected_output": "Both share age 20: True",
                    "explanation_en": "Demonstrates that values can be identical across different keys.",
                    "explanation_hi": "Dikhata hai ki do alag keys ki value same ho sakti hai."
                },
                "challenge": {
                    "prompt_en": "Check if 'email' is a key in data = {'name': 'Sam', 'age': 22} using 'email' in data. Print: Has email: False",
                    "prompt_hi": "Check karo kya 'email' key hai data = {'name': 'Sam', 'age': 22} me. Print karo: Has email: False",
                    "starter_code": "data = {'name': 'Sam', 'age': 22}\n# Check key existence and print:\n",
                    "expected_output": "Has email: False",
                    "solution_code": "data = {'name': 'Sam', 'age': 22}\nprint(f\"Has email: {'email' in data}\")",
                    "solution_explanation_en": "'in' checks key membership in a dictionary.",
                    "solution_explanation_hi": "'in' operator dictionary me key search karta hai.",
                    "hints": ["'email' in data"],
                    "ego_roast_hi": "in operator bhool gaye?",
                    "ego_cheer_hi": "Key-value relationships validated! 🔑"
                }
            },
            {
                "id": "ch10_sub3_add_update_remove",
                "title": "Adding, updating, and removing items in a dictionary",
                "title_hi": "Dictionary me items add, update aur delete karna",
                "icon": "🔄",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Dictionaries are fully mutable: you add or update by assigning to a key: dict[key] = val. To delete, use del dict[key] or dict.pop(key).",
                "what_is_it_hi": "Dictionary mutable hoti hai: Naya data jodna ya purana badalna ho to dict[key] = value likho. Delete karne ke liye del dict[key] ya dict.pop(key) use hota hai.",
                "why_need_it_en": "Updating user profile pictures, incrementing view counts, or deleting expired auth sessions.",
                "why_need_it_hi": "User ka profile update karna, view count badhana, ya account delete karna.",
                "how_to_use_en": "Add/update: d['role'] = 'admin'. Delete: del d['role'] or d.pop('role').",
                "how_to_use_hi": "Update: d['role'] = 'admin'. Delete: del d['role'] ya d.pop('role').",
                "syntax": "profile = {\"name\": \"Alex\"}\nprofile[\"email\"] = \"alex@test.com\"  # ADD new key\nprofile[\"name\"] = \"Alexander\"       # UPDATE existing key\ndel profile[\"email\"]                # REMOVE key\npopped_val = profile.pop(\"name\")   # REMOVE & return value",
                "rules_en": [
                    "If the key does NOT exist, assigning to it ADDS the new key-value pair.",
                    "If the key ALREADY exists, assigning to it OVERWRITES the previous value.",
                    "del d[key] removes the key; throws KeyError if the key does not exist.",
                    "d.pop(key, default) safely removes and returns the value without crashing."
                ],
                "rules_hi": [
                    "Agar key pehle se nahi hai to naya pair ADD ho jata hai.",
                    "Agar key pehle se hai to purani value OVERWRITE ho jaati hai.",
                    "del d[key] se pair delete ho jata hai.",
                    "pop(key) value nikaal kar delete karta hai."
                ],
                "analogy_en": "A smartphone contact card: you edit the phone number, add an Instagram handle, or delete a discarded old address.",
                "analogy_hi": "Phone me contact edit karne jaisa: naya number add kiya, purana badla, ya contact delete kar diya.",
                "common_mistakes": [
                    {
                        "mistake": "Calling del on a non-existent key: del user['missing']",
                        "why_it_fails_en": "KeyError: 'missing'.",
                        "why_it_fails_hi": "Jo key hai hi nahi use del karne par KeyError aayega.",
                        "fix": "Use user.pop('missing', None) which safely returns None if missing."
                    }
                ],
                "example_1": {
                    "title": "Adding and Modifying Keys",
                    "title_hi": "Key add karna aur update karna",
                    "code": "player = {'name': 'Mario', 'coins': 5}\nplayer['coins'] += 10  # UPDATE\nplayer['power'] = 'Fire'  # ADD\nprint('Updated player:', player)",
                    "expected_output": "Updated player: {'name': 'Mario', 'coins': 15, 'power': 'Fire'}",
                    "explanation_en": "Increments coins from 5 to 15 and introduces new 'power' key.",
                    "explanation_hi": "Coins ko 15 banaya aur naya 'power' key add kiya."
                },
                "example_2": {
                    "title": "Safely Popping with Fallback",
                    "title_hi": "Safe pop() fallback ke sath",
                    "code": "user = {'id': 1, 'role': 'guest'}\nrole = user.pop('role', 'none')\nmissing = user.pop('avatar', 'default.png')\nprint('Popped role:', role)\nprint('Fallback avatar:', missing)",
                    "expected_output": "Popped role: guest\nFallback avatar: default.png",
                    "explanation_en": "user.pop('avatar', 'default.png') doesn't crash even though 'avatar' was absent.",
                    "explanation_hi": "'avatar' na hone par bhi crash nahi hua, default.png de diya."
                },
                "challenge": {
                    "prompt_en": "Start with app = {'version': 1.0}. Update version to 2.0, add 'author': 'Elysia', and print app.",
                    "prompt_hi": "app = {'version': 1.0} me version 2.0 karo, 'author': 'Elysia' jodo aur print karo: {'version': 2.0, 'author': 'Elysia'}",
                    "starter_code": "app = {'version': 1.0}\n# Update version, add author, and print:\n",
                    "expected_output": "{'version': 2.0, 'author': 'Elysia'}",
                    "solution_code": "app = {'version': 1.0}\napp['version'] = 2.0\napp['author'] = 'Elysia'\nprint(app)",
                    "solution_explanation_en": "Updates 'version' and adds 'author'.",
                    "solution_explanation_hi": "Version update karke author add karta hai.",
                    "hints": ["app['version'] = 2.0\\napp['author'] = 'Elysia'"],
                    "ego_roast_hi": "Dictionary update karna nahi aaya?",
                    "ego_cheer_hi": "Dictionary mutation successful! 🔄"
                }
            },
            {
                "id": "ch10_sub4_get_method",
                "title": "Using get() to safely find data without errors",
                "title_hi": "Bina error ke safe lookup: get() method",
                "icon": "🛡️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The .get(key, default) method safely retrieves a value from a dictionary. If the key exists, it returns the value; if the key is missing, it returns None (or your custom default fallback) instead of crashing with a fatal KeyError!",
                "what_is_it_hi": ".get(key, default) method dictionary se safe lookup karta hai. Agar key hai to value de deta hai; agar key missing hai to crash hone ke bajaye None (ya aapka diya default backup value) deta hai.",
                "why_need_it_en": "In web applications, user profiles often have optional fields (like middle_name, phone_number, bio). Using user['bio'] crashes if empty, but user.get('bio', 'No bio provided') is rock-solid.",
                "why_need_it_hi": "Web apps me optional fields (jaise bio ya phone number) na hone par bracket notation crash kar deta hai. get() se crash hone ka khatra zero rehta hai.",
                "how_to_use_en": "val = d.get('key', 'default_fallback').",
                "how_to_use_hi": "d.get('key', 'Not Found') use karo.",
                "syntax": "profile = {\"name\": \"Alex\"}\n# Unsafe (CRASHES if missing):\n# age = profile[\"age\"]  # KeyError!\n\n# Safe (NEVER crashes):\nage = profile.get(\"age\", 18)  # Returns 18 fallback",
                "rules_en": [
                    "d.get(key) defaults to returning None if the key is missing.",
                    "d.get(key, default) returns the specified default if key is missing.",
                    "If key exists with value None, get() returns None (it doesn't trigger default)."
                ],
                "rules_hi": [
                    "d.get(key) agar key na mile to None return karta hai.",
                    "d.get(key, 'default') key na milne par default value deta hai.",
                    "Bracket notation se crash hota hai, get() se kabhi crash nahi hota."
                ],
                "analogy_en": "Asking a receptionist: 'Is Room 502 available? If not, please give me Room 101.' You don't get thrown out of the hotel; you get the backup room.",
                "analogy_hi": "Hotel me poochne jaisa: 'Kya AC room hai? Agar nahi to non-AC de do.' Seedhe bahar nikaalne ke bajaye backup room mil jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Using bracket notation on untrusted external JSON/API data: data['status']['code']",
                        "why_it_fails_en": "If any key is missing or renamed by the API, the whole server crashes with KeyError.",
                        "why_it_fails_hi": "API se koi key gayab hui to poora server crash ho jayega.",
                        "fix": "Use .get() with fallbacks for untrusted external payloads."
                    }
                ],
                "example_1": {
                    "title": "Bracket Notation vs .get()",
                    "title_hi": "user['age'] vs user.get('age') ka farak",
                    "code": "user = {'name': 'Alex'}\nprint('Name found:', user.get('name'))\nprint('Age fallback:', user.get('age', 25))",
                    "expected_output": "Name found: Alex\nAge fallback: 25",
                    "explanation_en": "Retrieves 'Alex' for existing key, and 25 fallback for missing key.",
                    "explanation_hi": "Mili hui key ka naam aur missing key ka default fallback 25 deta hai."
                },
                "example_2": {
                    "title": "Word Frequency Counting with .get()",
                    "title_hi": "get() se word counter banana",
                    "code": "words = ['cat', 'dog', 'cat']\ncounts = {}\nfor w in words:\n    counts[w] = counts.get(w, 0) + 1\nprint('Word frequencies:', counts)",
                    "expected_output": "Word frequencies: {'cat': 2, 'dog': 1}",
                    "explanation_en": "counts.get(w, 0) starts count at 0 for new words, incrementing smoothly.",
                    "explanation_hi": "counts.get(w, 0) se pehli baar 0 milta hai fir 1 add ho jata hai."
                },
                "challenge": {
                    "prompt_en": "Given config = {'theme': 'dark'}, safely fetch 'font' with default 'Arial' using .get() and print: Font: Arial",
                    "prompt_hi": "config = {'theme': 'dark'} se .get('font', 'Arial') use karke print karo: Font: Arial",
                    "starter_code": "config = {'theme': 'dark'}\n# Safe get with default:\n",
                    "expected_output": "Font: Arial",
                    "solution_code": "config = {'theme': 'dark'}\nfont = config.get('font', 'Arial')\nprint(f'Font: {font}')",
                    "solution_explanation_en": "Uses .get('font', 'Arial') fallback.",
                    "solution_explanation_hi": "get() se default Arial nikaalta hai.",
                    "hints": ["config.get('font', 'Arial')"],
                    "ego_roast_hi": "get() me default value daalna bhool gaye?",
                    "ego_cheer_hi": "Crash-proof dictionary lookup! 🛡️"
                }
            },
            {
                "id": "ch10_sub5_looping_dictionaries",
                "title": "Looping through dictionaries (.keys(), .values(), .items())",
                "title_hi": "Dictionary par loop chalana (.keys(), .values(), .items())",
                "icon": "🔄",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "You can loop over a dictionary in three distinct ways: 1. By default or with .keys() iterates over KEYS; 2. .values() iterates over VALUES; 3. .items() unpacks both KEY and VALUE simultaneously on every turn.",
                "what_is_it_hi": "Dictionary par 3 tareeqon se loop chalta hai: 1. for k in dict (sirf KEYS par); 2. for v in dict.values() (sirf VALUES par); 3. for k, v in dict.items() (KEY aur VALUE dono par ek sath).",
                "why_need_it_en": "Generating formatted user reports, printing invoices, or checking all scores in a gradebook.",
                "why_need_it_hi": "Invoice print karna (Item: Price), attendance sheet banana (Naam: Status).",
                "how_to_use_en": "for k, v in d.items(): print(f'{k} -> {v}').",
                "how_to_use_hi": "for key, value in d.items(): print(key, value).",
                "syntax": "# 1. Keys loop:\nfor k in d.keys(): ...\n# 2. Values loop:\nfor v in d.values(): ...\n# 3. Keys and Values (MOST COMMON):\nfor key, value in d.items():\n    print(f\"{key}: {value}\")",
                "rules_en": [
                    "Looping directly over 'd' (for k in d) iterates over KEYS by default.",
                    ".items() yields a tuple (key, value) on every iteration.",
                    "Never add or remove keys from a dictionary while looping over it (causes RuntimeError: dictionary changed size during iteration)."
                ],
                "rules_hi": [
                    "Direct 'for k in d' likhne par sirf KEYS milti hain.",
                    ".items() se har turn par (key, value) ka pair milta hai.",
                    "Loop chalte waqt dictionary me items add ya delete mat karo, RuntimeError aayega."
                ],
                "analogy_en": "Reading a receipt: reading the item column (keys), reading the price column (values), or reading both side-by-side (items).",
                "analogy_hi": "Dukan ke bill par: sirf saman ka naam padhna (.keys()), sirf rate padhna (.values()), ya dono sath me padhna (.items()).",
                "common_mistakes": [
                    {
                        "mistake": "Looping over d and expecting values: for val in user: print(val)",
                        "why_it_fails_en": "Loops over keys! It prints 'name', 'age', NOT 'Alex', 20.",
                        "why_it_fails_hi": "Direct loop sirf keys print karta hai, values nahi.",
                        "fix": "Use for key, value in user.items():"
                    }
                ],
                "example_1": {
                    "title": "The Power of .items()",
                    "title_hi": ".items() se dono ek sath print karna",
                    "code": "prices = {'Apple': 50, 'Mango': 80}\nfor fruit, price in prices.items():\n    print(f'{fruit} costs ${price}')",
                    "expected_output": "Apple costs $50\nMango costs $80",
                    "explanation_en": ".items() unpacks both fruit name and price simultaneously.",
                    "explanation_hi": ".items() har turn me fruit aur uska price dono deta hai."
                },
                "example_2": {
                    "title": "Summing Values with .values()",
                    "title_hi": ".values() se total nikaalna",
                    "code": "expenses = {'rent': 500, 'groceries': 200, 'wifi': 50}\ntotal_expense = sum(expenses.values())\nprint('Total Monthly Spend:', total_expense)",
                    "expected_output": "Total Monthly Spend: 750",
                    "explanation_en": "Passes expenses.values() view directly to sum().",
                    "explanation_hi": "expenses.values() ko seedhe sum() me pass karke total nikaalta hai."
                },
                "challenge": {
                    "prompt_en": "Loop through scores = {'Math': 90, 'Science': 85} using .items() and print: Math: 90 then Science: 85",
                    "prompt_hi": "scores = {'Math': 90, 'Science': 85} par .items() loop chala kar print karo: Math: 90 aur Science: 85",
                    "starter_code": "scores = {'Math': 90, 'Science': 85}\n# Loop with .items():\n",
                    "expected_output": "Math: 90\nScience: 85",
                    "solution_code": "scores = {'Math': 90, 'Science': 85}\nfor subject, mark in scores.items():\n    print(f'{subject}: {mark}')",
                    "solution_explanation_en": "Iterates using .items() and prints subject: mark.",
                    "solution_explanation_hi": ".items() se subject aur mark print karta hai.",
                    "hints": ["for subject, mark in scores.items():\\n    print(f'{subject}: {mark}')"],
                    "ego_roast_hi": ".items() use karna bhool gaye?",
                    "ego_cheer_hi": "Dictionary iteration pro! 🔄"
                }
            },
            {
                "id": "ch10_sub6_nested_dictionaries",
                "title": "Nesting dictionaries inside dictionaries",
                "title_hi": "Nested Dictionaries (Dictionary ke andar dictionary)",
                "icon": "🗂️",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "A nested dictionary is a dictionary that contains other dictionaries as values. This is the universal foundation of JSON data used across all modern internet APIs, databases (MongoDB), and configurations.",
                "what_is_it_hi": "Nested Dictionary ka matlab dictionary ke andar doosri dictionary. Internet ki saari APIs, mobile apps, aur MongoDB database me yahi JSON format use hota hai.",
                "why_need_it_en": "Representing structured entities: a user has an address, which has a street and a pincode: user['address']['pincode'].",
                "why_need_it_hi": "Complex data store karna: Student ke andar marks, marks ke andar subjects (student['marks']['math']).",
                "how_to_use_en": "Chain keys: db['users']['alex']['email'].",
                "how_to_use_hi": "Keys chain karo: users['alex']['city'].",
                "syntax": "users = {\n    \"alex\": {\n        \"email\": \"alex@test.com\",\n        \"role\": \"admin\"\n    },\n    \"sara\": {\n        \"email\": \"sara@test.com\",\n        \"role\": \"member\"\n    }\n}\nalex_role = users[\"alex\"][\"role\"]  # 'admin'",
                "rules_en": [
                    "Chain square brackets to drill down: dict[outer_key][inner_key].",
                    "If outer_key is missing, chaining brackets throws KeyError immediately.",
                    "Safe navigation: d.get('outer', {}).get('inner', 'fallback')."
                ],
                "rules_hi": [
                    "Ek ke baad ek bracket lagao: dict[outer][inner].",
                    "Agar outer key missing hai to bracket notation crash kar dega.",
                    "Safe navigation ke liye: d.get('outer', {}).get('inner', 'default') use karo."
                ],
                "analogy_en": "A filing cabinet (outer dict): you open the drawer labeled 'Engineers', then pull out the folder labeled 'Priyanshu' to read his email.",
                "analogy_hi": "Office ki almari jaisi: Pehle 'Finance' ka drawer khola (outer key), fir usme se 'Invoice #101' ka kagaz nikala (inner key).",
                "common_mistakes": [
                    {
                        "mistake": "Unchecked deep lookup: data['user']['profile']['avatar'] when 'profile' is None.",
                        "why_it_fails_en": "TypeError: 'NoneType' object is not subscriptable.",
                        "why_it_fails_hi": "Agar beech me koi key None hui to code crash ho jayega.",
                        "fix": "Use safe chained gets or try/except."
                    }
                ],
                "example_1": {
                    "title": "Accessing Nested User Profile",
                    "title_hi": "Nested profile me se data nikaalna",
                    "code": "company = {\n    'emp_1': {'name': 'Rohan', 'salary': 50000},\n    'emp_2': {'name': 'Pooja', 'salary': 65000}\n}\nprint('Employee 1 Name:', company['emp_1']['name'])\nprint('Employee 2 Salary:', company['emp_2']['salary'])",
                    "expected_output": "Employee 1 Name: Rohan\nEmployee 2 Salary: 65000",
                    "explanation_en": "Drills into nested dictionaries with chained bracket access.",
                    "explanation_hi": "Chained brackets se nested data access karta hai."
                },
                "example_2": {
                    "title": "Safe Nested Traversal",
                    "title_hi": "Safe nested traversal",
                    "code": "db = {'user': {'name': 'Sara'}}\ncity = db.get('user', {}).get('city', 'Unknown City')\nprint('Detected City:', city)",
                    "expected_output": "Detected City: Unknown City",
                    "explanation_en": "Falls back safely to 'Unknown City' without throwing KeyError.",
                    "explanation_hi": "City na milne par safe fallback 'Unknown City' deta hai."
                },
                "challenge": {
                    "prompt_en": "Given data = {'student': {'name': 'Alex', 'grade': 'A'}}, print: Alex: Grade A",
                    "prompt_hi": "data = {'student': {'name': 'Alex', 'grade': 'A'}} se print karo: Alex: Grade A",
                    "starter_code": "data = {'student': {'name': 'Alex', 'grade': 'A'}}\n# Drill down and print:\n",
                    "expected_output": "Alex: Grade A",
                    "solution_code": "data = {'student': {'name': 'Alex', 'grade': 'A'}}\ns = data['student']\nprint(f\"{s['name']}: Grade {s['grade']}\")",
                    "solution_explanation_en": "Accesses nested dictionary keys cleanly.",
                    "solution_explanation_hi": "Nested dictionary keys access karke print karta hai.",
                    "hints": ["data['student']['name'] and data['student']['grade']"],
                    "ego_roast_hi": "Nested brackets me ghoom gaye?",
                    "ego_cheer_hi": "Complex JSON dictionary structures mastered! 🗂️"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 11: The Mathematical Collection (Sets)
    # =========================================================================
    {
        "id": "ch11_sets",
        "part_number": 3,
        "part_title": "PART 3: ORGANIZING LOTS OF DATA (DATA STRUCTURES)",
        "chapter_number": 11,
        "title": "Chapter 11: The Mathematical Collection (Sets)",
        "subtitle_en": "Unordered unique collections, set theory (union, intersection, difference), and deduplication",
        "subtitle_hi": "Sets: Unique elements, Union, Intersection, Difference aur duplicates hatana",
        "icon": "⭕",
        "estimated_time": "30 mins",
        "prerequisites_en": "Chapters 8 to 10 (Lists, tuples, dictionaries).",
        "prerequisites_hi": "Chapter 8 se 10 tak (Lists, tuples, dicts).",
        "learning_objectives_en": [
            "Understand sets as unordered, strictly unique collections",
            "Add and remove elements from sets (.add(), .remove(), .discard())",
            "Master mathematical set operations (|, &, -, ^)",
            "Deduplicate lists instantly with set(my_list)"
        ],
        "learning_objectives_hi": [
            "Sets ka unique elements concept samjho",
            "Elements add aur discard karna",
            "Mathematical set operations (Union, Intersection, Difference)",
            "List me se duplicates 1 second me hatana set() se"
        ],
        "recap_en": "You mastered sets: uniqueness enforcement, O(1) membership lookups, set theory algebra, and lightning-fast list deduplication.",
        "recap_hi": "Aapne sets ke unique rules, set operations (|, &, -) aur list se duplicates hatane ka formula seekha.",
        "subtopics": [
            {
                "id": "ch11_sub1_what_is_a_set",
                "title": "What is a set? (Unordered, unique items only)",
                "title_hi": "Set kya hota hai? (Unordered, unique items only)",
                "icon": "✨",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A set is an unordered, unindexed collection of UNIQUE elements enclosed in curly braces {}. Any duplicate items added to a set are silently and automatically discarded.",
                "what_is_it_hi": "Set curly braces {} me band UNIQUE (bina kisi duplicate) elements ka collection hota hai. Isme order nahi hota aur indexing [0] nahi hoti. Agar duplicate daaloge to set use chupke se ignore kar dega.",
                "why_need_it_en": "Tracking unique visitors to a website, unique email recipients, or checking membership in ultra-fast O(1) time.",
                "why_need_it_hi": "Website ke unique visitors ginn-na, unique phone numbers nikaalna, aur ultra-fast O(1) speed me search karna.",
                "how_to_use_en": "s = {1, 2, 3}. To create an empty set, use s = set() (because {} creates an empty dictionary!).",
                "how_to_use_hi": "s = {1, 2, 3}. Khali set banane ke liye set() likho (khali {} likhoge to dictionary ban jayegi!).",
                "syntax": "nums = {1, 2, 2, 3, 3, 3}  # Automatically becomes {1, 2, 3}\nempty_set = set()          # Correct empty set\nnot_empty_set = {}         # WARNING: This is an empty dict!",
                "rules_en": [
                    "CRITICAL: Sets can NEVER contain duplicates. Every element is guaranteed unique.",
                    "Sets are UNORDERED: items have no fixed index (s[0] throws TypeError).",
                    "Elements inside a set must be immutable/hashable (strings, ints, tuples; lists CANNOT be inside a set).",
                    "Empty set MUST be created with set(), NOT {}."
                ],
                "rules_hi": [
                    "SUNEHRA NIYAM: Set me duplicate kabhi nahi reh sakta.",
                    "Set unordered hota hai: isme koi seat number [0] nahi hota.",
                    "Set ke andar sirf immutable cheezein aa sakti hain (list set ke andar nahi ja sakti).",
                    "Khali set banane ke liye hamesha set() use karo, {} mat likho."
                ],
                "analogy_en": "A bag of unique lottery balls: no matter how many times you drop in a duplicate #7 ball, there is only one ball #7 in the bag.",
                "analogy_hi": "Party me aane wale guests ki unique guest list — ek mehmaan chahe 5 baar darwaze par aaye, list me naam 1 hi baar likha jayega.",
                "common_mistakes": [
                    {
                        "mistake": "Creating an empty set with curly braces: s = {}",
                        "why_it_fails_en": "type({}) is <class 'dict'>, NOT set! Python defaults empty curly braces to dictionaries.",
                        "why_it_fails_hi": "Khali {} likhne se dictionary ban jaati hai set nahi.",
                        "fix": "Always use set() for an empty set."
                    }
                ],
                "example_1": {
                    "title": "Automatic Duplicate Elimination",
                    "title_hi": "Duplicates ka apne aap gayab hona",
                    "code": "tags = {'python', 'code', 'python', 'ai', 'ai'}\nprint('Unique tags sorted:', sorted(tags))\nprint('Total unique count:', len(tags))",
                    "expected_output": "Unique tags sorted: ['ai', 'code', 'python']\nTotal unique count: 3",
                    "explanation_en": "Duplicates 'python' and 'ai' were automatically collapsed into single entries.",
                    "explanation_hi": "Duplicates apne aap hat gaye aur sirf 3 unique tags bache."
                },
                "example_2": {
                    "title": "Empty Set Verification",
                    "title_hi": "Empty set ka type check",
                    "code": "s1 = set()\ns2 = {}\nprint('Type of set():', type(s1).__name__)\nprint('Type of {}:', type(s2).__name__)",
                    "expected_output": "Type of set(): set\nType of {}: dict",
                    "explanation_en": "Demonstrates that set() creates a set, while {} creates a dict.",
                    "explanation_hi": "Dikhata hai ki set() set banata hai aur {} dictionary banata hai."
                },
                "challenge": {
                    "prompt_en": "Create a set from {5, 5, 10, 10, 15} and print its length: 3",
                    "prompt_hi": "{5, 5, 10, 10, 15} ka set banao aur uski length print karo: 3",
                    "starter_code": "s = {5, 5, 10, 10, 15}\n# Print length of set:\n",
                    "expected_output": "3",
                    "solution_code": "s = {5, 5, 10, 10, 15}\nprint(len(s))",
                    "solution_explanation_en": "Deduplicates 5 and 10, leaving {5, 10, 15} of length 3.",
                    "solution_explanation_hi": "Duplicates hatne ke baad length 3 bachti hai.",
                    "hints": ["len(s)"],
                    "ego_roast_hi": "Set duplicates hatata hai, yaad hai na?",
                    "ego_cheer_hi": "Set uniqueness verified! ✨"
                }
            },
            {
                "id": "ch11_sub2_add_remove_set",
                "title": "Adding and removing set elements",
                "title_hi": "Set me elements add aur remove karna",
                "icon": "➕",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "You add items to a set using .add(x). To remove, use .remove(x) (crashes with KeyError if missing) or .discard(x) (safe; does nothing if missing).",
                "what_is_it_hi": "Set me item add karne ke liye .add(x) use hota hai. Hatane ke liye do methods hain: .remove(x) (agar item na ho to crash ho jata hai) aur .discard(x) (safe hai, item na ho to bina crash huye chup rehta hai).",
                "why_need_it_en": "Managing user active status or tags: s.add('admin') activates role; s.discard('admin') removes role safely.",
                "why_need_it_hi": "Active users me add karna, ya session disconnect hone par discard karna.",
                "how_to_use_en": "s.add('newItem'), s.discard('oldItem').",
                "how_to_use_hi": "s.add(10), s.discard(10).",
                "syntax": "skills = {\"Python\"}\nskills.add(\"SQL\")        # {'Python', 'SQL'}\nskills.add(\"Python\")     # Ignored (already present)\nskills.discard(\"Java\")   # Safe (no error even though 'Java' is missing)\nskills.remove(\"SQL\")     # Removes 'SQL'",
                "rules_en": [
                    "use .add() for a single item; use .update([a, b]) to add multiple items from an iterable.",
                    "prefer .discard() over .remove() because discard NEVER crashes if the item is missing.",
                    ".pop() on a set removes and returns an ARBITRARY element (since sets are unordered)."
                ],
                "rules_hi": [
                    "Single item ke liye .add(), multiple ke liye .update() use karo.",
                    ".discard() use karo kyunki item na hone par ye crash nahi hota.",
                    "Set me .pop() random item nikaalta hai kyunki set unordered hota hai."
                ],
                "analogy_en": "A VIP party guest list: you add a new invitee with .add(). When someone cancels, you cross their name off with .discard().",
                "analogy_hi": "Guest list me naya naam likhna (.add()) aur aane se mana karne par naam kaat dena (.discard()).",
                "common_mistakes": [
                    {
                        "mistake": "Calling .remove() on a value that doesn't exist.",
                        "why_it_fails_en": "KeyError: 'item'.",
                        "why_it_fails_hi": "remove() missing item par KeyError phek deta hai.",
                        "fix": "Always use .discard() for safe element deletion."
                    }
                ],
                "example_1": {
                    "title": "Add and Safe Discard",
                    "title_hi": "Add karna aur safe discard",
                    "code": "roles = {'viewer'}\nroles.add('editor')\nroles.discard('superadmin')  # Won't crash!\nprint('Roles set:', sorted(roles))",
                    "expected_output": "Roles set: ['editor', 'viewer']",
                    "explanation_en": "Adds 'editor' and safely discards non-existent 'superadmin' without error.",
                    "explanation_hi": "'editor' add kiya aur na hone par bhi 'superadmin' bina crash huye discard kiya."
                },
                "example_2": {
                    "title": "Adding Multiple Elements with .update()",
                    "title_hi": "Ek sath multiple elements add karna",
                    "code": "primes = {2, 3}\nprimes.update([5, 7, 2])  # 2 is duplicate\nprint('Primes set:', sorted(primes))",
                    "expected_output": "Primes set: [2, 3, 5, 7]",
                    "explanation_en": "update() merges multiple items while respecting uniqueness.",
                    "explanation_hi": "update() ne naye numbers jode aur duplicate 2 ko ignore kar diya."
                },
                "challenge": {
                    "prompt_en": "Start with s = {1, 2}. Add 3, discard 1, and print the sorted set elements as a list: [2, 3]",
                    "prompt_hi": "s = {1, 2} me 3 add karo, 1 discard karo aur sorted list print karo: [2, 3]",
                    "starter_code": "s = {1, 2}\n# Add 3, discard 1, print sorted:\n",
                    "expected_output": "[2, 3]",
                    "solution_code": "s = {1, 2}\ns.add(3)\ns.discard(1)\nprint(sorted(s))",
                    "solution_explanation_en": "Adds 3 and discards 1.",
                    "solution_explanation_hi": "3 add kiya aur 1 discard karke sorted list print ki.",
                    "hints": ["s.add(3) then s.discard(1) then print(sorted(s))"],
                    "ego_roast_hi": "add aur discard karna bhool gaye?",
                    "ego_cheer_hi": "Set elements modified cleanly! ➕"
                }
            },
            {
                "id": "ch11_sub3_set_operations",
                "title": "Set operations: Union (|), Intersection (&), Difference (-), Symmetric Difference (^)",
                "title_hi": "Set operations: Union (|), Intersection (&), Difference (-), Symmetric Difference (^)",
                "icon": "📐",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Python implements pure mathematical Venn Diagram operations: Union (|) combines both sets; Intersection (&) finds common elements; Difference (-) finds elements in A but not B; Symmetric Difference (^) finds elements in either set, but NOT in both.",
                "what_is_it_hi": "Venn Diagram ke 4 math operations: Union (|) dono sets ke saare items jodta hai; Intersection (&) common items nikaalta hai; Difference (-) A ke wo items jo B me nahi hain; Symmetric Difference (^) jo dono me se kisi EK me hain lekin common nahi hain.",
                "why_need_it_en": "Social media: Mutual friends = userA_friends & userB_friends. Suggested friends = userA_friends ^ userB_friends. Unread messages = all_messages - read_messages.",
                "why_need_it_hi": "Instagram mutual friends nikaalna (Intersection &), do groups ke common members dhoondna, pending tasks nikaalna (Difference -).",
                "how_to_use_en": "A | B (Union), A & B (Intersection), A - B (Difference), A ^ B (Symmetric Diff).",
                "how_to_use_hi": "A | B, A & B, A - B, A ^ B.",
                "syntax": "a = {1, 2, 3}\nb = {2, 3, 4}\nunion_val = a | b      # {1, 2, 3, 4}\ninter_val = a & b      # {2, 3} (Common)\ndiff_val = a - b       # {1} (In A only)\nsymm_val = a ^ b       # {1, 4} (In either, but not both)",
                "rules_en": [
                    "| (Union): Everything in A OR B.",
                    "& (Intersection): Everything in A AND B (mutual overlap).",
                    "- (Difference): In A, minus anything that also appears in B.",
                    "^ (Symmetric Difference): In A or B, but NOT both."
                ],
                "rules_hi": [
                    "| (Union): A aur B ka milan (sab kuch).",
                    "& (Intersection): Dono ka COMMON part (overlap).",
                    "- (Difference): Sirf A me jo hai (B ka nikaal kar).",
                    "^ (Symmetric Difference): Unique to either (common wala hata kar)."
                ],
                "analogy_en": "Venn diagrams drawn with two overlapping circles on a school chalkboard.",
                "analogy_hi": "School ke do overlapping gole (Venn Diagram) — beech ka common hissa & hai, poora mila kar | hai.",
                "common_mistakes": [
                    {
                        "mistake": "Confusing difference order: a - b vs b - a",
                        "why_it_fails_en": "a - b gives items in A only; b - a gives items in B only! Set difference is NOT commutative.",
                        "why_it_fails_hi": "a - b aur b - a alag-alag answers dete hain.",
                        "fix": "Remember: left side is what you start with, right side is what gets subtracted."
                    }
                ],
                "example_1": {
                    "title": "Finding Mutual Friends (Intersection)",
                    "title_hi": "Mutual friends nikaalna (&)",
                    "code": "alex_friends = {'Rohan', 'Sara', 'Pooja'}\nsam_friends = {'Pooja', 'Aman', 'Rohan'}\nmutual = alex_friends & sam_friends\nprint('Mutual Friends:', sorted(mutual))",
                    "expected_output": "Mutual Friends: ['Pooja', 'Rohan']",
                    "explanation_en": "& identifies the common friends shared between both users.",
                    "explanation_hi": "& operator se dono ke common friends mil gaye."
                },
                "example_2": {
                    "title": "Unfinished Tasks (Difference)",
                    "title_hi": "Bache hue kaam nikaalna (-)",
                    "code": "all_tasks = {'task1', 'task2', 'task3'}\ndone_tasks = {'task1'}\npending = all_tasks - done_tasks\nprint('Pending Tasks:', sorted(pending))",
                    "expected_output": "Pending Tasks: ['task2', 'task3']",
                    "explanation_en": "Subtracts completed tasks to isolate remaining work.",
                    "explanation_hi": "Completed tasks minus karke bache hue tasks nikaalta hai."
                },
                "challenge": {
                    "prompt_en": "Find intersection of {1, 2, 3} & {2, 3, 4} and print the sorted list: [2, 3]",
                    "prompt_hi": "{1, 2, 3} aur {2, 3, 4} ka intersection (&) nikaal kar sorted list print karo: [2, 3]",
                    "starter_code": "a = {1, 2, 3}\nb = {2, 3, 4}\n# Find intersection and print sorted:\n",
                    "expected_output": "[2, 3]",
                    "solution_code": "a = {1, 2, 3}\nb = {2, 3, 4}\nprint(sorted(a & b))",
                    "solution_explanation_en": "a & b yields {2, 3}.",
                    "solution_explanation_hi": "a & b se common {2, 3} milta hai.",
                    "hints": ["print(sorted(a & b))"],
                    "ego_roast_hi": "& operator use karna bhool gaye?",
                    "ego_cheer_hi": "Venn diagram algebra mastered! 📐"
                }
            },
            {
                "id": "ch11_sub4_deduplicating_lists",
                "title": "Using sets to remove duplicates from a list",
                "title_hi": "List me se duplicates hatane ke liye sets use karna",
                "icon": "🧹",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The fastest, most famous Python idiom to remove duplicates from a list is passing it into set() and back into list(): unique_list = list(set(raw_list)).",
                "what_is_it_hi": "List me se duplicates hatane ka Python ka sabse famous 1-line formula hai: list ko set me daalo aur wapas list bana lo: unique_list = list(set(my_list)).",
                "why_need_it_en": "Cleaning dirty data from CSV uploads, deduplicating email mailing lists, or removing repeated search suggestions.",
                "why_need_it_hi": "Email list me se repeat emails hatana, search queries me se duplicate words hatana — 1 second me saara kachra saaf.",
                "how_to_use_en": "clean_list = list(set(dirty_list)). Note: order may change; if order matters, use dict.fromkeys(raw_list).",
                "how_to_use_hi": "clean = list(set(dirty_list)). Agar order maintain rakhna hai to list(dict.fromkeys(dirty_list)) use karo.",
                "syntax": "# Instant Deduplication Idiom:\nraw = [1, 2, 2, 3, 4, 4, 4, 5]\nclean = list(set(raw))  # [1, 2, 3, 4, 5]",
                "rules_en": [
                    "list(set(x)) removes all duplicates in O(n) linear time.",
                    "Tradeoff: because sets are unordered, the original order of items may NOT be preserved.",
                    "If you must preserve insertion order while deduplicating, use list(dict.fromkeys(x))."
                ],
                "rules_hi": [
                    "list(set(x)) superfast O(n) speed me saare duplicates saaf kar deta hai.",
                    "Dhyan rahe: Set unordered hota hai isliye items ka aage-peeche order badal sakta hai.",
                    "Agar exact order bachana hai to list(dict.fromkeys(x)) use karo."
                ],
                "analogy_en": "Pouring a bag of mixed coins through a coin sorter: duplicate coins drop into the same slot, leaving you with exactly one of each coin denomination.",
                "analogy_hi": "Chhalni (filter) se chaan-ne jaisa — saare duplicate baahar nikal gaye aur sirf unique moti bache.",
                "common_mistakes": [
                    {
                        "mistake": "Relying on list(set(x)) when exact item order is critical.",
                        "why_it_fails_en": "Sets do not guarantee order preservation across Python runs or different values.",
                        "why_it_fails_hi": "Set order guarantee nahi karta to items ka sequence hil sakta hai.",
                        "fix": "Use list(dict.fromkeys(x)) for order-preserving deduplication."
                    }
                ],
                "example_1": {
                    "title": "Cleaning Duplicate Phone Numbers",
                    "title_hi": "Duplicate numbers saaf karna",
                    "code": "raw_numbers = [98765, 12345, 98765, 45678, 12345]\nunique_numbers = sorted(list(set(raw_numbers)))\nprint('Clean deduplicated numbers:', unique_numbers)",
                    "expected_output": "Clean deduplicated numbers: [12345, 45678, 98765]",
                    "explanation_en": "list(set()) eliminates repeat phone numbers instantly.",
                    "explanation_hi": "list(set()) ne repeat numbers hata diye aur sorted order me list mili."
                },
                "example_2": {
                    "title": "Order-Preserving Deduplication Alternative",
                    "title_hi": "Order maintain rakhte huye duplicates hatana",
                    "code": "raw_names = ['Zack', 'Alex', 'Zack', 'Bob']\nclean_ordered = list(dict.fromkeys(raw_names))\nprint('Deduplicated keeping order:', clean_ordered)",
                    "expected_output": "Deduplicated keeping order: ['Zack', 'Alex', 'Bob']",
                    "explanation_en": "dict.fromkeys() removes duplicates while strictly preserving the first appearance order.",
                    "explanation_hi": "dict.fromkeys() ne pehle aane wale sequence ko bachaye rakha."
                },
                "challenge": {
                    "prompt_en": "Deduplicate nums = [1, 1, 2, 3, 3] using list(set(nums)) and print the sorted result: [1, 2, 3]",
                    "prompt_hi": "nums = [1, 1, 2, 3, 3] me se list(set(nums)) use karke duplicates hatao aur sorted print karo: [1, 2, 3]",
                    "starter_code": "nums = [1, 1, 2, 3, 3]\n# Deduplicate and print sorted:\n",
                    "expected_output": "[1, 2, 3]",
                    "solution_code": "nums = [1, 1, 2, 3, 3]\nprint(sorted(list(set(nums))))",
                    "solution_explanation_en": "Deduplicates to {1, 2, 3} and outputs as sorted list.",
                    "solution_explanation_hi": "set se duplicates hata kar sorted list print karta hai.",
                    "hints": ["print(sorted(list(set(nums))))"],
                    "ego_roast_hi": "list(set()) formula bhool gaye?",
                    "ego_cheer_hi": "PART 3 DATA STRUCTURES CONQUERED! 🏆 Lists, Tuples, Dicts, Sets Mastered!"
                }
            }
        ]
    }
]
