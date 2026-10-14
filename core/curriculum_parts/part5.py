"""
Part 5: The Real World (Files, Errors, and Objects)
Chapters 15, 16, 17, and 18 with exact syllabus titles and subtopics.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 15: Saving Your Work (File Handling)
    # =========================================================================
    {
        "id": "ch15_file_handling",
        "part_number": 5,
        "part_title": "PART 5: THE REAL WORLD (FILES, ERRORS, AND OBJECTS)",
        "chapter_number": 15,
        "title": "Chapter 15: Saving Your Work (File Handling)",
        "subtitle_en": "Paths, read/write/append modes, with statement, CSV spreadsheets, and JSON web data",
        "subtitle_hi": "File handling: Paths, read/write/append, with statement, CSV aur JSON files",
        "icon": "💾",
        "estimated_time": "40 mins",
        "prerequisites_en": "Parts 1 to 4 (Basic Python, strings, dictionaries).",
        "prerequisites_hi": "Part 1 se 4 tak (Python basics, strings, dicts).",
        "learning_objectives_en": [
            "Distinguish absolute and relative file paths",
            "Open files safely in read ('r'), write ('w'), and append ('a') modes",
            "Read file contents via read(), readline(), and readlines()",
            "Master the 'with' statement for leak-proof file descriptor management",
            "Parse and write CSV spreadsheets using the csv module",
            "Serialize and deserialize JSON payloads using the json module"
        ],
        "learning_objectives_hi": [
            "Absolute aur Relative file paths ka farak samjho",
            "Files ko read ('r'), write ('w') aur append ('a') modes me kholna",
            "read(), readline() aur readlines() se data padhna",
            "'with' statement se memory-leak proof file management",
            "csv module se Excel spreadsheets handle karna",
            "json module se web data (dumps, loads) parse karna"
        ],
        "recap_en": "You mastered persistent storage: navigating disk file paths, context-managed file I/O, writing reports, parsing CSV tables, and exchanging structured JSON web payloads.",
        "recap_hi": "Aapne file handling, with open, CSV spreadsheets aur JSON data exchange master kiya.",
        "subtopics": [
            {
                "id": "ch15_sub1_file_paths",
                "title": "How file paths work (Absolute vs. Relative paths)",
                "title_hi": "File paths kaise kaam karte hain (Absolute vs. Relative paths)",
                "icon": "🗺️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A file path is the address of a file on your disk. An ABSOLUTE path starts from the root of your hard drive (/Users/name/data.txt or C:\\data.txt). A RELATIVE path starts from the Current Working Directory of your running script (./data.txt or ../data.txt).",
                "what_is_it_hi": "File path computer ki hard drive me file ka address hota hai. ABSOLUTE path hard disk ke root se shuru hota hai (C:\\Users\\... ya /Users/...). RELATIVE path wahan se shuru hota hai jahan aapki script run ho rahi hai (./data.txt).",
                "why_need_it_en": "Hardcoding absolute paths (/Users/priyanshu/...) breaks your code when deployed on a server or shared with a classmate! Professional software uses relative paths with pathlib or os.path.",
                "why_need_it_hi": "Agar C:\\Users\\mera_naam likh doge to wahi code doosre dost ke computer ya cloud server par crash ho jayega. Relative path har computer par chalta hai.",
                "how_to_use_en": "Use pathlib: from pathlib import Path; base = Path(__file__).resolve().parent.",
                "how_to_use_hi": "pathlib use karo: Path(__file__).parent / 'data.txt'.",
                "syntax": "# Relative path (Starts from current folder):\npath_rel = \"data/scores.txt\"\n# Absolute path (Full disk root):\npath_abs = \"/var/log/system.log\"",
                "rules_en": [
                    "'.' represents the current directory; '..' represents the parent directory.",
                    "Always use forward slashes (/) or pathlib.Path; Windows backslashes (\\) can accidentally escape characters (e.g. \\new treated as \\n!).",
                    "Path(__file__).parent guarantees finding files relative to the script location regardless of where terminal was launched."
                ],
                "rules_hi": [
                    "'.' ka matlab current folder; '..' ka matlab pichhla (parent) folder.",
                    "Hamesha forward slash (/) ya pathlib use karo; Windows ke \\n se escape error aa sakta hai.",
                    "Path(__file__).parent se file hamesha mil jaati hai."
                ],
                "analogy_en": "Absolute path is GPS coordinates: '28.6139° N, 77.2090° E' (unambiguous anywhere on Earth). Relative path is walking directions: 'Walk 2 blocks down and turn left' (depends on where you are currently standing).",
                "analogy_hi": "Absolute path GPS coordinates jaisa hai (duniya me kahin se bhi same jagah). Relative path kisi se rasta poochne jaisa hai: 'Aage jaakar pehla right le lena' (aap kahan khade ho uspe depend karta hai).",
                "common_mistakes": [
                    {
                        "mistake": "Using raw Windows backslashes: 'C:\\users\\notes.txt'",
                        "why_it_fails_en": "\\n is parsed as a newline escape character! Throws FileNotFoundError or invalid path.",
                        "why_it_fails_hi": "\\n se nayi line ban jaati hai aur file milti hi nahi.",
                        "fix": "Use raw strings r'C:\\users\\notes.txt' or forward slashes 'C:/users/notes.txt'."
                    }
                ],
                "example_1": {
                    "title": "Resolving Script Directory with Pathlib",
                    "title_hi": "Pathlib se safe relative path nikaalna",
                    "code": "from pathlib import Path\nscript_file = Path('main.py')\nprint('Filename:', script_file.name)\nprint('Suffix extension:', script_file.suffix)",
                    "expected_output": "Filename: main.py\nSuffix extension: .py",
                    "explanation_en": "pathlib.Path inspects filename and extension cross-platform.",
                    "explanation_hi": "pathlib cross-platform tareeqe se filename aur extension nikaalta hai."
                },
                "example_2": {
                    "title": "Relative Navigation Syntax",
                    "title_hi": "Relative dots (. and ..)",
                    "code": "import os\nprint('Current folder symbol (.):', os.curdir)\nprint('Parent folder symbol (..):', os.pardir)",
                    "expected_output": "Current folder symbol (.): .\nParent folder symbol (..): ..",
                    "explanation_en": "os.curdir and os.pardir show standard relative navigation tokens.",
                    "explanation_hi": "Current aur parent folder ke standard symbols dikhata hai."
                },
                "challenge": {
                    "prompt_en": "Using pathlib.Path('data/report.csv'), print its file extension using .suffix: .csv",
                    "prompt_hi": "pathlib.Path('data/report.csv').suffix se extension print karo: .csv",
                    "starter_code": "from pathlib import Path\n# Print file extension:\n",
                    "expected_output": ".csv",
                    "solution_code": "from pathlib import Path\np = Path('data/report.csv')\nprint(p.suffix)",
                    "solution_explanation_en": "p.suffix extracts '.csv'.",
                    "solution_explanation_hi": "p.suffix se '.csv' extension milta hai.",
                    "hints": ["Path('data/report.csv').suffix"],
                    "ego_roast_hi": "Path suffix nikaalna bhool gaye?",
                    "ego_cheer_hi": "Path navigation mastered! 🗺️"
                }
            },
            {
                "id": "ch15_sub2_open_modes",
                "title": "Opening files: Read (r), Write (w), and Append (a) modes",
                "title_hi": "Files kholna: Read (r), Write (w), aur Append (a) modes",
                "icon": "📖",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The open(filename, mode) function requests access to a disk file. Mode 'r' opens for READING (fails if missing); Mode 'w' opens for WRITING (dangerously OVERWRITES and wipes existing file!); Mode 'a' opens for APPENDING (adds to bottom without erasing).",
                "what_is_it_hi": "open() function file kholta hai. 'r' sirf READ karne ke liye kholta hai (file na ho to crash); 'w' WRITE karne ke liye kholta hai (PURANI FILE KA SAARA DATA ERASE KAR DETA HAI!); 'a' APPEND karne ke liye kholta hai (purana bachaye rakhta hai aur neeche nayi lines jodta hai).",
                "why_need_it_en": "Choosing between 'w' and 'a' is critical: Writing a log file with 'w' deletes all previous server history! You must use 'a' for logs.",
                "why_need_it_hi": "'w' aur 'a' ka farak sabse zaroori hai: Server logs me 'w' use kiya to purana saara record delete ho jayega. Hamesha 'a' lagana chahiye.",
                "how_to_use_en": "f = open('log.txt', 'a', encoding='utf-8').",
                "how_to_use_hi": "open('file.txt', 'r', encoding='utf-8').",
                "syntax": "# 'r' = Read (Default)\n# 'w' = Overwrite (Wipes existing content!)\n# 'a' = Append (Adds to the end)\n# 'r+' = Read and Write simultaneously",
                "rules_en": [
                    "CRITICAL WARNING: Mode 'w' truncates the file to 0 bytes the millisecond it opens! If you want to keep old data, use 'a'.",
                    "Always specify encoding='utf-8' to prevent strange character corruption across Windows and Mac.",
                    "Every opened file MUST be closed with f.close() (or handled automatically with a 'with' statement)."
                ],
                "rules_hi": [
                    "DANGER WARNING: 'w' mode file kholte hi uska saara purana data mita deta hai. Data bachana hai to 'a' use karo.",
                    "Hamesha encoding='utf-8' likho taaki Hindi ya symbols kharab na hon.",
                    "File open karne ke baad close() karna zaroori hai."
                ],
                "analogy_en": "'r' is reading a museum book through glass. 'w' is erasing a chalkboard completely with water. 'a' is adding a new diary entry at the end of your notebook.",
                "analogy_hi": "'r' kitaab padhna hai. 'w' blackboard par duster chala kar saara purana saaf kar dena hai. 'a' diary me purane panno ke baad naya panna likhna hai.",
                "common_mistakes": [
                    {
                        "mistake": "Opening an existing data file in 'w' mode by mistake.",
                        "why_it_fails_en": "Instantly and irrecoverably deletes the entire file content before you even write anything!",
                        "why_it_fails_hi": "Purana saara data 1 millisecond me delete ho jata hai.",
                        "fix": "Use 'a' (append) whenever you intend to add data without erasing."
                    }
                ],
                "example_1": {
                    "title": "Comparing File Modes",
                    "title_hi": "File modes ka explanation",
                    "code": "modes = {'r': 'Read only', 'w': 'Overwrite / Create', 'a': 'Append to end'}\nfor m, desc in modes.items():\n    print(f'Mode \"{m}\": {desc}')",
                    "expected_output": "Mode \"r\": Read only\nMode \"w\": Overwrite / Create\nMode \"a\": Append to end",
                    "explanation_en": "Displays the three primary file operation modes.",
                    "explanation_hi": "Teeno core file modes ka description deta hai."
                },
                "example_2": {
                    "title": "Safe Encoding Parameter",
                    "title_hi": "utf-8 encoding parameter",
                    "code": "text_sample = 'Namaste Python 🙏'\nencoded = text_sample.encode('utf-8')\nprint('UTF-8 bytes valid:', len(encoded) > 0)",
                    "expected_output": "UTF-8 bytes valid: True",
                    "explanation_en": "Demonstrates why encoding='utf-8' is vital for unicode emojis and international text.",
                    "explanation_hi": "UTF-8 se Hindi aur emojis bina corrupt huye save hote hain."
                },
                "challenge": {
                    "prompt_en": "Print the safe file mode used to add new log entries without erasing: Mode: a",
                    "prompt_hi": "Purana data bachate huye naya data jodne ka mode print karo: Mode: a",
                    "starter_code": "# Print append mode:\n",
                    "expected_output": "Mode: a",
                    "solution_code": "print('Mode: a')",
                    "solution_explanation_en": "Mode 'a' appends without truncating.",
                    "solution_explanation_hi": "Mode 'a' append karta hai bina erase kiye.",
                    "hints": ["print('Mode: a')"],
                    "ego_roast_hi": "'w' aur 'a' ka farak yaad hai na?",
                    "ego_cheer_hi": "File mode safety verified! 📖"
                }
            },
            {
                "id": "ch15_sub3_reading_files",
                "title": "Reading text from a file (.read(), .readline(), .readlines())",
                "title_hi": "File se text padhna (.read(), .readline(), .readlines())",
                "icon": "📄",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Python provides 3 methods to read text: .read() reads the ENTIRE file into a single giant string; .readline() reads ONE line at a time; .readlines() reads all lines into a LIST of strings.",
                "what_is_it_hi": "File padhne ke 3 methods: .read() poori file ko ek giant string me padhta hai; .readline() ek baar me sirf 1 line padhta hai; .readlines() saari lines ko strings ki LIST me load karta hai.",
                "why_need_it_en": "Memory limits: If a server log is 20 GB, calling .read() crashes with an Out-of-Memory (OOM) error! Using 'for line in f:' or .readline() streams it line-by-line safely with near-zero RAM.",
                "why_need_it_hi": "Agar 10 GB ki file me .read() kar doge to laptop hang ho jayega! .readline() ya 'for line in f' ek-ek line padh kar RAM bachata hai.",
                "how_to_use_en": "Best practice for lines: for line in file_obj: print(line.strip()).",
                "how_to_use_hi": "Sabse best tareeqa: for line in f: print(line.strip()).",
                "syntax": "# 1. Entire file:\ncontent = f.read()\n# 2. Single line:\nfirst_line = f.readline()\n# 3. All lines as list:\nlines_list = f.readlines()\n# 4. Memory-safe streaming iterator (BEST):\nfor line in f:\n    print(line.strip())",
                "rules_en": [
                    "Lines read from files include trailing newline characters ('\\n'). Use .strip() to clean them.",
                    "Calling .read() moves the file cursor to the end; calling .read() again immediately after returns an empty string ''.",
                    "Use f.seek(0) to rewind the file cursor back to the beginning."
                ],
                "rules_hi": [
                    "File se aane wali har line ke aakhri me '\\n' hota hai, .strip() se use hatate hain.",
                    "Ek baar padhne ke baad cursor aakhri me chala jata hai, dobara padhne ke liye f.seek(0) se shuru me aana padta hai.",
                    "Badi files ke liye 'for line in f:' sabse memory-efficient tareeqa hai."
                ],
                "analogy_en": ".read() is drinking an entire 2-liter bottle of water in one gulp. .readline() is taking sips with a straw one sip at a time.",
                "analogy_hi": ".read() poori 2 liter ki botal ek ghoont me peena hai (pet fat jayega). .readline() straw se ek-ek ghoont peena hai (safe aur easy).",
                "common_mistakes": [
                    {
                        "mistake": "Calling f.read() on a multi-gigabyte production file.",
                        "why_it_fails_en": "MemoryError: CPU runs out of RAM trying to allocate a multi-gigabyte contiguous string.",
                        "why_it_fails_hi": "RAM bhar jaati hai aur computer crash ho jata hai.",
                        "fix": "Iterate directly: for line in f:"
                    }
                ],
                "example_1": {
                    "title": "Simulating File Reading Methods",
                    "title_hi": "Reading methods ka simulation",
                    "code": "sample_data = 'Line 1\\nLine 2\\nLine 3'\nlines = sample_data.splitlines()\nprint('Line count read:', len(lines))\nprint('First line:', lines[0])",
                    "expected_output": "Line count read: 3\nFirst line: Line 1",
                    "explanation_en": "Demonstrates line-by-line parsing identical to file readlines.",
                    "explanation_hi": "Lines ko alag-alag karke readlines jaisa behavior dikhata hai."
                },
                "example_2": {
                    "title": "Cleaning Trailing Newlines with strip()",
                    "title_hi": "strip() se newline hatana",
                    "code": "raw_line = 'User: Alex\\n'\nclean_line = raw_line.strip()\nprint('Raw repr:', repr(raw_line))\nprint('Cleaned repr:', repr(clean_line))",
                    "expected_output": "Raw repr: 'User: Alex\\n'\nCleaned repr: 'User: Alex'",
                    "explanation_en": "strip() removes the invisible trailing \\n character.",
                    "explanation_hi": "strip() aakhri ka invisible newline character hata deta hai."
                },
                "challenge": {
                    "prompt_en": "Simulate reading: given text = 'Header\\nBody', split into lines and print the first line: Header",
                    "prompt_hi": "text = 'Header\\nBody' ko splitlines() karke pehli line print karo: Header",
                    "starter_code": "text = 'Header\\nBody'\n# Print first line:\n",
                    "expected_output": "Header",
                    "solution_code": "text = 'Header\\nBody'\nprint(text.splitlines()[0])",
                    "solution_explanation_en": "Extracts the first line from multiline string.",
                    "solution_explanation_hi": "Pehli line nikaal kar print karta hai.",
                    "hints": ["text.splitlines()[0]"],
                    "ego_roast_hi": "Pehli line padhna bhool gaye?",
                    "ego_cheer_hi": "File reading methods verified! 📄"
                }
            },
            {
                "id": "ch15_sub4_writing_files",
                "title": "Writing text to a file",
                "title_hi": "File me text likhna (Writing files)",
                "icon": "✍️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Writing text to a file saves your program's strings onto permanent physical storage. Use f.write(string) to write text, or f.writelines(list_of_strings) to write multiple lines.",
                "what_is_it_hi": "File me likhne se aapka code permanent hard drive par data save kar deta hai. f.write(text) se likha jata hai aur f.writelines(list) se multiple lines likhi jaati hain.",
                "why_need_it_en": "Saving game progress, exporting CSV grades, generating receipts, and saving user settings.",
                "why_need_it_hi": "Game save karna, students ki marksheet export karna, user settings permanently save karna.",
                "how_to_use_en": "with open('notes.txt', 'w') as f: f.write('Hello!\\n').",
                "how_to_use_hi": "with open('file.txt', 'w') as f: f.write('Hello\\n').",
                "syntax": "with open(\"output.txt\", \"w\", encoding=\"utf-8\") as f:\n    f.write(\"Line 1: Saved forever\\n\")\n    f.write(\"Line 2: Data persisted\\n\")",
                "rules_en": [
                    "f.write() does NOT automatically add a newline! You must explicitly include '\\n' at the end of your string.",
                    "f.write() only accepts STRINGS. Trying to write an int (f.write(42)) causes TypeError: write() argument must be str.",
                    "Always convert numbers before writing: f.write(str(num))."
                ],
                "rules_hi": [
                    "f.write() apne aap nayi line nahi banata! Line break ke liye '\\n' likhna padta hai.",
                    "f.write() sirf STRING leta hai. Number pass karoge to TypeError aayega: f.write(str(42)) likho.",
                    "File close hone par buffer disk par flush hota hai."
                ],
                "analogy_en": "Carving words onto a wax tablet: once the wax cools (file closes), the message remains even when the candle blows out.",
                "analogy_hi": "Diary me pen se likhne jaisa — computer band bhi ho jaye to diary me likhi line safe rehti hai.",
                "common_mistakes": [
                    {
                        "mistake": "Writing numbers directly: f.write(100)",
                        "why_it_fails_en": "TypeError: write() argument must be str, not int.",
                        "why_it_fails_hi": "f.write sirf text samajhta hai, number nahi.",
                        "fix": "Convert to string: f.write(str(100)) or f.write(f'{100}\\n')."
                    }
                ],
                "example_1": {
                    "title": "Simulated Write Operation",
                    "title_hi": "Writing buffer simulation",
                    "code": "buffer = []\nbuffer.append('Report Header\\n')\nbuffer.append(f'Generated: 2026-10-12\\n')\noutput_text = ''.join(buffer)\nprint('Simulated disk content:')\nprint(output_text, end='')",
                    "expected_output": "Simulated disk content:\nReport Header\nGenerated: 2026-10-12",
                    "explanation_en": "Demonstrates formatted writing with explicit newlines.",
                    "explanation_hi": "Newline ke sath formatted lines likhne ka simulation.",
                },
                "example_2": {
                    "title": "String Formatting for File Persistence",
                    "title_hi": "Data formatting disk save ke liye",
                    "code": "score = 98\nline_to_write = f'UserScore:{score}\\n'\nprint('Formatted file line:', repr(line_to_write))",
                    "expected_output": "Formatted file line: 'UserScore:98\\n'",
                    "explanation_en": "Converts number to string with trailing newline ready for disk storage.",
                    "explanation_hi": "Number ko string bana kar trailing newline lagata hai."
                },
                "challenge": {
                    "prompt_en": "Format a score line for file writing: student = 'Alex', score = 95. Print exact line repr with \\n: 'Alex:95\\n'",
                    "prompt_hi": "student = 'Alex', score = 95 ko file line format me banao: 'Alex:95\\n'. Uska repr print karo.",
                    "starter_code": "student = 'Alex'\nscore = 95\n# Format and print repr:\n",
                    "expected_output": "'Alex:95\\n'",
                    "solution_code": "student = 'Alex'\nscore = 95\nline = f'{student}:{score}\\n'\nprint(repr(line))",
                    "solution_explanation_en": "Formats with f-string and newline, printed via repr().",
                    "solution_explanation_hi": "f-string aur newline se file format banata hai.",
                    "hints": ["repr(f'{student}:{score}\\n')"],
                    "ego_roast_hi": "\\n lagana bhool gaye kya?",
                    "ego_cheer_hi": "File output formatting verified! ✍️"
                }
            },
            {
                "id": "ch15_sub5_with_statement",
                "title": "The with statement (Automatically closing files)",
                "title_hi": "The with statement (Files automatically close karna)",
                "icon": "🔒",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "The 'with' statement is a Context Manager. It automatically opens the file and GUARANTEES that the file descriptor is closed the moment the indented block exits — even if your code crashes with an unhandled exception inside!",
                "what_is_it_hi": "'with' statement ek Context Manager hai. Ye file kholta hai aur GUARANTEE deta hai ki jaise hi indented block khatam hoga, file apne aap band (close) ho jayegi — chahe beech me koi error ya crash hi kyun na aa jaye!",
                "why_need_it_en": "Resource Leaks: If you use manual f.close() and an error happens before that line, the file stays permanently locked open in OS memory, corrupting data and wasting file descriptors.",
                "why_need_it_hi": "Agar manually f.close() karoge aur beech me koi error aa gaya to close wali line chalegi hi nahi aur file memory me locked reh kar corrupt ho jayegi. 'with' 100% safe hai.",
                "how_to_use_en": "Always use 'with open(...) as f:' for all file operations in modern Python.",
                "how_to_use_hi": "Hamesha 'with open(...) as f:' hi use karo.",
                "syntax": "# The Gold Standard of Python File I/O:\nwith open(\"data.txt\", \"r\", encoding=\"utf-8\") as f:\n    content = f.read()\n# File is automatically 100% CLOSED here!",
                "rules_en": [
                    "PEP 8 LAW: Always use 'with' to open files. Never call naked open() without a context manager.",
                    "The context manager calls __enter__() when entering the block and __exit__() upon leaving.",
                    "f.closed is True immediately after exiting the with block."
                ],
                "rules_hi": [
                    "PEP 8 NIYAM: Hamesha 'with open' use karo. Manual close() lagana purana tareeqa hai.",
                    "Block se nikalte hi f.closed True ho jata hai.",
                    "Crash hone par bhi background me clean exit guarantee hoti hai."
                ],
                "analogy_en": "An automatic spring-loaded hotel door: the moment you walk through, the door automatically clicks shut and locks behind you so nobody leaves it open.",
                "analogy_hi": "Hotel ke automatic door jaisa — jaise hi aap andar gaye ya bahar nikle, darwaza apne aap band ho jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to read from the file variable AFTER exiting the with block: with open(...) as f: pass; f.read()",
                        "why_it_fails_en": "ValueError: I/O operation on closed file. The file is already closed!",
                        "why_it_fails_hi": "with block ke bahar aate hi file band ho chuki hoti hai, bahar padhne par crash ho jayega.",
                        "fix": "Perform all read/write operations INSIDE the indented with block."
                    }
                ],
                "example_1": {
                    "title": "Context Manager Lifecycle",
                    "title_hi": "with statement ka auto-close lifecycle",
                    "code": "# Simulating context manager guarantee\nclass MockFileManager:\n    def __enter__(self):\n        return 'Connected'\n    def __exit__(self, exc_type, exc_val, exc_tb):\n        print('Auto-close: File safely closed in OS!')\n\nwith MockFileManager() as f:\n    print('Status inside with block:', f)",
                    "expected_output": "Status inside with block: Connected\nAuto-close: File safely closed in OS!",
                    "explanation_en": "__exit__ executes automatically upon block termination.",
                    "explanation_hi": "__exit__ automatically chalta hai aur file close kar deta hai."
                },
                "example_2": {
                    "title": "Safe File Closed Inspection",
                    "title_hi": "f.closed attribute check karna",
                    "code": "import io\nwith io.StringIO('Hello Elysia') as f:\n    data = f.read()\nprint('Read data:', data)\nprint('Is stream closed now?', f.closed)",
                    "expected_output": "Read data: Hello Elysia\nIs stream closed now? True",
                    "explanation_en": "f.closed evaluates to True immediately after exiting the with block.",
                    "explanation_hi": "with block ke bahar aate hi f.closed True ban jata hai."
                },
                "challenge": {
                    "prompt_en": "Print the status confirmation of a context-managed file: File closed automatically: True",
                    "prompt_hi": "Print karo: File closed automatically: True",
                    "starter_code": "# Print context manager confirmation:\n",
                    "expected_output": "File closed automatically: True",
                    "solution_code": "print('File closed automatically: True')",
                    "solution_explanation_en": "Confirms automatic closing guarantee.",
                    "solution_explanation_hi": "Automatic close ka confirmation print karta hai.",
                    "hints": ["print('File closed automatically: True')"],
                    "ego_roast_hi": "with statement ka fayda yaad hai na?",
                    "ego_cheer_hi": "Context manager auto-close mastered! 🔒"
                }
            },
            {
                "id": "ch15_sub6_csv_files",
                "title": "Working with CSV files (Spreadsheets) using the csv module",
                "title_hi": "CSV spreadsheets ke sath kaam karna (csv module)",
                "icon": "📊",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "A CSV (Comma-Separated Values) file is a plain text file representing spreadsheet tables (rows and columns) separated by commas. Python's built-in 'csv' module provides csv.reader, csv.writer, and csv.DictReader.",
                "what_is_it_hi": "CSV (Comma-Separated Values) file Excel spreadsheet jaisi table hoti hai jisme har column comma se alag hota hai. Python ka built-in 'csv' module csv.reader, csv.writer aur csv.DictReader deta hai.",
                "why_need_it_en": "Exporting student marksheets to Excel, importing catalog items from Google Sheets, and handling data science tabular datasets.",
                "why_need_it_hi": "Excel me marksheet export karna, Google Sheets se data import karna, data science ke datasets read karna.",
                "how_to_use_en": "import csv; reader = csv.reader(f); for row in reader: print(row).",
                "how_to_use_hi": "import csv; reader = csv.reader(f); for row in reader: print(row).",
                "syntax": "import csv\n\n# Writing CSV:\nwith open(\"students.csv\", \"w\", newline=\"\", encoding=\"utf-8\") as f:\n    writer = csv.writer(f)\n    writer.writerow([\"Name\", \"Roll\", \"Score\"])\n    writer.writerow([\"Alex\", 101, 95])\n\n# Reading CSV:\nwith open(\"students.csv\", \"r\", encoding=\"utf-8\") as f:\n    reader = csv.reader(f)\n    for row in reader:\n        print(row)",
                "rules_en": [
                    "CRITICAL on Windows: When opening for csv.writer, ALWAYS pass newline='' to prevent blank empty rows!",
                    "csv.DictReader turns each row into a dictionary mapped to the header column names.",
                    "csv handles commas inside quotes automatically (e.g. \"Smith, John\", 25)."
                ],
                "rules_hi": [
                    "WINDOWS SPECIAL: CSV file likhte waqt newline='' pass karna mandatory hai, warna beech me blank rows aayengi.",
                    "csv.DictReader har row ko column names ke sath dictionary bana deta hai.",
                    "Quotes ke andar wale comma ko csv module apne aap handle karta hai."
                ],
                "analogy_en": "A physical ledger or Excel table where comma acts as the vertical grid line dividing columns, and Enter acts as the horizontal row line.",
                "analogy_hi": "Excel sheet ke columns jaisa jahan comma column ki divider line ban jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Splitting CSV lines manually with line.split(',') instead of using the csv module.",
                        "why_it_fails_en": "Breaks immediately if any field contains an address with an internal comma like 'Delhi, India'!",
                        "why_it_fails_hi": "Agar kisi text me comma hua ('Delhi, India') to manual split code ko corrupt kar dega.",
                        "fix": "Always use the built-in 'csv' module."
                    }
                ],
                "example_1": {
                    "title": "Parsing CSV Rows with csv.reader",
                    "title_hi": "csv.reader se rows parse karna",
                    "code": "import csv\nimport io\ncsv_data = 'Name,Score\\nAlex,95\\nSara,88'\nf = io.StringIO(csv_data)\nreader = csv.reader(f)\nfor row in reader:\n    print('CSV Row:', row)",
                    "expected_output": "CSV Row: ['Name', 'Score']\nCSV Row: ['Alex', '95']\nCSV Row: ['Sara', '88']",
                    "explanation_en": "csv.reader cleanly splits each line into a list of cell strings.",
                    "explanation_hi": "csv.reader har line ko cells ki list me convert karta hai."
                },
                "example_2": {
                    "title": "DictReader Header Mapping",
                    "title_hi": "csv.DictReader se dictionary format",
                    "code": "import csv\nimport io\ncsv_data = 'Item,Price\\nPen,10\\nBook,50'\nf = io.StringIO(csv_data)\nreader = csv.DictReader(f)\nfor row in reader:\n    print(f\"{row['Item']} costs ${row['Price']}\")",
                    "expected_output": "Pen costs $10\nBook costs $50",
                    "explanation_en": "DictReader maps column headers ('Item', 'Price') directly to dictionary keys.",
                    "explanation_hi": "DictReader header ke naamo ko dictionary keys bana deta hai."
                },
                "challenge": {
                    "prompt_en": "Use csv.reader on io.StringIO('A,B,C') and print the parsed row: ['A', 'B', 'C']",
                    "prompt_hi": "csv.reader se 'A,B,C' parse karke row print karo: ['A', 'B', 'C']",
                    "starter_code": "import csv, io\nf = io.StringIO('A,B,C')\n# Parse with csv.reader and print row:\n",
                    "expected_output": "['A', 'B', 'C']",
                    "solution_code": "import csv, io\nf = io.StringIO('A,B,C')\nreader = csv.reader(f)\nfor r in reader:\n    print(r)",
                    "solution_explanation_en": "Parses comma-separated cells into a Python list.",
                    "solution_explanation_hi": "CSV line ko list me convert karke print karta hai.",
                    "hints": ["reader = csv.reader(f)\\nfor r in reader: print(r)"],
                    "ego_roast_hi": "csv.reader lagana bhool gaye?",
                    "ego_cheer_hi": "CSV spreadsheet parsing mastered! 📊"
                }
            },
            {
                "id": "ch15_sub7_json_files",
                "title": "Working with JSON files (Web data) using the json module",
                "title_hi": "JSON web data ke sath kaam karna (json module)",
                "icon": "🌐",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "JSON (JavaScript Object Notation) is the universal lingua franca of the internet. Python's built-in 'json' module translates between JSON strings and Python dictionaries using json.dumps() (Python to JSON string) and json.loads() (JSON string to Python).",
                "what_is_it_hi": "JSON internet par data exchange karne ka universal standard hai. Python ka built-in 'json' module Python dictionary aur JSON string ke beech translation karta hai: json.dumps() (Dict to JSON string) aur json.loads() (JSON to Python Dict).",
                "why_need_it_en": "Every modern REST API (GitHub, Weather, OpenAI, Payment gateways) sends and receives data formatted as JSON.",
                "why_need_it_hi": "Internet ki har API (weather, payment, AI) JSON format me hi data bhejti aur leti hai.",
                "how_to_use_en": "json.loads(text) parses JSON text into a dict; json.dumps(obj) converts a dict into JSON text.",
                "how_to_use_hi": "loads (load string) se dict banao, dumps (dump string) se JSON text banao.",
                "syntax": "import json\n\n# Python dict to JSON string (Serialization):\ndata = {\"name\": \"Alex\", \"active\": True}\njson_str = json.dumps(data, indent=2)\n\n# JSON string to Python dict (Deserialization):\nparsed_dict = json.loads(json_str)",
                "rules_en": [
                    "json.loads() = Load from STRING (takes string, returns dict/list).",
                    "json.dumps() = Dump to STRING (takes dict/list, returns string).",
                    "json.load(f) and json.dump(obj, f) work directly with file objects.",
                    "JSON booleans are lowercase 'true'/'false', while Python uses capitalized 'True'/'False'. json handles conversion automatically."
                ],
                "rules_hi": [
                    "json.loads() = String se Python Dict banana (Load String).",
                    "json.dumps() = Python Dict se String banana (Dump String).",
                    "Bina 's' wale json.load(f) aur json.dump(f) direct files par chalte hain.",
                    "JSON me chhota true hota hai, Python me bada True hota hai — json module khud convert kar deta hai."
                ],
                "analogy_en": "Currency exchange at an airport: json.dumps converts your local rupees into US dollars for travel; json.loads converts dollars back into rupees when you return home.",
                "analogy_hi": "Airport par currency exchange jaisa — Python dictionary ko international JSON currency me badalna (dumps) aur wapas convert karna (loads).",
                "common_mistakes": [
                    {
                        "mistake": "Confusing loads() and load(): calling json.loads(file_obj)",
                        "why_it_fails_en": "TypeError: the JSON object must be str, bytes or bytearray, not TextIOWrapper.",
                        "why_it_fails_hi": "loads 's' for string leta hai file nahi. File ke liye bina 's' wala json.load() lagta hai.",
                        "fix": "Use json.load(f) for files, and json.loads(s) for strings."
                    }
                ],
                "example_1": {
                    "title": "Parsing JSON Web API Response",
                    "title_hi": "JSON string ko Python Dict me convert karna",
                    "code": "import json\napi_response = '{\"status\": \"success\", \"user_id\": 42, \"verified\": true}'\ndata = json.loads(api_response)\nprint('Status:', data['status'])\nprint('Verified (Python bool):', data['verified'])",
                    "expected_output": "Status: success\nVerified (Python bool): True",
                    "explanation_en": "json.loads parses string into a Python dict; converts JSON 'true' to Python 'True'.",
                    "explanation_hi": "json.loads ne JSON 'true' ko Python boolean 'True' me badal diya."
                },
                "example_2": {
                    "title": "Serializing Python Dict to Pretty JSON",
                    "title_hi": "Pretty JSON string banana (indent=2)",
                    "code": "import json\nprofile = {'name': 'Rohan', 'skills': ['Python', 'SQL']}\njson_text = json.dumps(profile)\nprint('JSON string output:', json_text)",
                    "expected_output": "JSON string output: {\"name\": \"Rohan\", \"skills\": [\"Python\", \"SQL\"]}",
                    "explanation_en": "json.dumps converts the Python dictionary into standard JSON text.",
                    "explanation_hi": "json.dumps ne Python dict ko standard JSON text bana diya."
                },
                "challenge": {
                    "prompt_en": "Convert json_str = '{\"code\": 200}' to Python dict using json.loads and print: Status code: 200",
                    "prompt_hi": "json_str = '{\"code\": 200}' ko json.loads karke print karo: Status code: 200",
                    "starter_code": "import json\njson_str = '{\"code\": 200}'\n# Parse and print:\n",
                    "expected_output": "Status code: 200",
                    "solution_code": "import json\njson_str = '{\"code\": 200}'\ndata = json.loads(json_str)\nprint(f\"Status code: {data['code']}\")",
                    "solution_explanation_en": "json.loads parses JSON into dict and accesses ['code'].",
                    "solution_explanation_hi": "json.loads se dict bana kar code print karta hai.",
                    "hints": ["data = json.loads(json_str)\\nprint(f\"Status code: {data['code']}\")"],
                    "ego_roast_hi": "json.loads use karna bhool gaye?",
                    "ego_cheer_hi": "JSON web data exchange mastered! 🌐"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 16: Expecting the Unexpected (Error Handling)
    # =========================================================================
    {
        "id": "ch16_error_handling",
        "part_number": 5,
        "part_title": "PART 5: THE REAL WORLD (FILES, ERRORS, AND OBJECTS)",
        "chapter_number": 16,
        "title": "Chapter 16: Expecting the Unexpected (Error Handling)",
        "subtitle_en": "Syntax vs runtime bugs, try/except, catching specific exceptions, else/finally, and custom raise errors",
        "subtitle_hi": "Error handling: try-except blocks, specific errors, else, finally aur raise keyword",
        "icon": "🛡️",
        "estimated_time": "35 mins",
        "prerequisites_en": "Chapters 1 to 15.",
        "prerequisites_hi": "Chapter 1 se 15 tak.",
        "learning_objectives_en": [
            "Distinguish Syntax errors (compile time) from Runtime exceptions",
            "Catch crashes safely using try and except blocks",
            "Catch specific exceptions (ZeroDivisionError, ValueError, KeyError) without bare excepts",
            "Utilize the full try-except-else-finally pipeline",
            "Trigger intentional custom validation errors using the raise keyword"
        ],
        "learning_objectives_hi": [
            "Syntax errors aur Runtime exceptions ka farak samjho",
            "try aur except se crash-proof code likhna",
            "Specific exceptions pakadna (ValueError, ZeroDivisionError)",
            "try-except-else-finally ka poora lifecycle",
            "raise keyword se intentional custom errors phenkna"
        ],
        "recap_en": "You mastered exception resilience: differentiating bugs, catching targeted error classes, ensuring cleanup with finally, and raising domain-specific exceptions.",
        "recap_hi": "Aapne exceptions pakadna, try-except-finally pipeline aur raise errors master kiya.",
        "subtopics": [
            {
                "id": "ch16_sub1_syntax_vs_runtime",
                "title": "Syntax errors vs. Runtime errors (Bugs)",
                "title_hi": "Syntax errors vs. Runtime errors (Bugs)",
                "icon": "🐛",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "SYNTAX ERRORS occur during parsing before ANY code executes (e.g. missing colon, mismatched quotes). RUNTIME ERRORS (Exceptions) occur while the code is actively executing (e.g. dividing by zero, missing file, key not found).",
                "what_is_it_hi": "SYNTAX ERROR code chalne se PEHLE hi pakda jata hai (jaise colon bhool gaye, quote band nahi kiya). RUNTIME ERROR (Exception) code chalte waqt aata hai (jaise zero se divide kar diya, file nahi mili, number galat type kiya).",
                "why_need_it_en": "You CANNOT catch a SyntaxError with a try/except block because Python refuses to even start running the script! You CAN catch and recover from Runtime Exceptions.",
                "why_need_it_hi": "SyntaxError ko try/except se nahi pakda ja sakta kyunki code shuru hi nahi hota. Runtime exceptions ko try/except se pakad kar code ko crash hone se bachaya ja sakta hai.",
                "how_to_use_en": "Fix syntax errors in your editor. Handle runtime errors using try/except blocks.",
                "how_to_use_hi": "Syntax errors ko editor me fix karo; runtime errors ko try-except se handle karo.",
                "syntax": "# SYNTAX ERROR (Fails at compile time):\n# def test()  <- Missing colon! Script never starts.\n\n# RUNTIME ERROR (Fails at execution time):\nx = 10 / 0   # ZeroDivisionError occurs when line is reached!",
                "rules_en": [
                    "SyntaxError halts execution before line 1 runs.",
                    "Runtime exceptions can be anticipated and handled with try/except.",
                    "Exceptions in Python form an inheritance hierarchy rooted at BaseException -> Exception."
                ],
                "rules_hi": [
                    "SyntaxError me code ka ek bhi line nahi chalta.",
                    "Runtime exceptions ko try/except se pakda ja sakta hai.",
                    "Python me saare normal exceptions 'Exception' class ke bache hote hain."
                ],
                "analogy_en": "Syntax error is putting a square peg in a round keyhole (the key won't even turn). Runtime error is driving a car until running out of fuel 50 km down the road.",
                "analogy_hi": "Syntax error gaadi start hone se pehle hi chaabi na ghoomna hai. Runtime error gaadi chalne ke 50 km baad petrol khatam ho jana hai.",
                "common_mistakes": [
                    {
                        "mistake": "Trying to wrap broken syntax in try/except: try: if True print(1) except: pass",
                        "why_it_fails_en": "SyntaxError: invalid syntax. The parser crashes before the try block can ever be evaluated.",
                        "why_it_fails_hi": "Syntax galat hone par try block chalta hi nahi hai.",
                        "fix": "Fix syntax syntax errors directly in code."
                    }
                ],
                "example_1": {
                    "title": "Runtime Exception Caught at Execution",
                    "title_hi": "Runtime exception ka example",
                    "code": "print('Line 1: Runs smoothly')\ntry:\n    res = 10 / 0  # Runtime division by zero\nexcept ZeroDivisionError:\n    print('Line 2: Caught ZeroDivisionError safely!')\nprint('Line 3: App continues running!')",
                    "expected_output": "Line 1: Runs smoothly\nLine 2: Caught ZeroDivisionError safely!\nLine 3: App continues running!",
                    "explanation_en": "Shows how try/except prevents the application from abruptly crashing.",
                    "explanation_hi": "Dikhata hai ki try-except program ko crash hone se bacha leta hai."
                },
                "example_2": {
                    "title": "TypeError at Runtime",
                    "title_hi": "Runtime par TypeError",
                    "code": "try:\n    ans = 'Age: ' + 25\nexcept TypeError as e:\n    print('Type error intercepted:', bool(e))",
                    "expected_output": "Type error intercepted: True",
                    "explanation_en": "Intercepts concatenating string and int at runtime.",
                    "explanation_hi": "String aur number jodte waqt aane wale TypeError ko pakadta hai."
                },
                "challenge": {
                    "prompt_en": "Wrap 10 / 0 in a try-except ZeroDivisionError block and print: Caught division by zero!",
                    "prompt_hi": "10 / 0 ko try-except ZeroDivisionError me wrap karke print karo: Caught division by zero!",
                    "starter_code": "# Wrap in try-except:\n",
                    "expected_output": "Caught division by zero!",
                    "solution_code": "try:\n    x = 10 / 0\nexcept ZeroDivisionError:\n    print('Caught division by zero!')",
                    "solution_explanation_en": "Catches ZeroDivisionError and prints the warning.",
                    "solution_explanation_hi": "ZeroDivisionError pakad kar message print karta hai.",
                    "hints": ["try:\\n    x = 10 / 0\\nexcept ZeroDivisionError:\\n    print(...)"],
                    "ego_roast_hi": "try-except block lagana bhool gaye?",
                    "ego_cheer_hi": "Runtime exception caught safely! 🛡️"
                }
            },
            {
                "id": "ch16_sub2_try_except_blocks",
                "title": "Catching errors safely: try and except blocks",
                "title_hi": "Errors ko safely pakadna: try aur except blocks",
                "icon": "🦺",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The try/except construct is a safety net. Code that might fail is placed inside the 'try' block. If an error occurs, Python jumps immediately into the 'except' block, executes the recovery instructions, and keeps the program running.",
                "what_is_it_hi": "try/except ek safety net (suraksha jaal) hai. Jis code me risk ho (jaise user input lena ya file kholna), use 'try' me daalte hain. Agar galti hui to Python seedhe 'except' block me jump karta hai aur app crash nahi hoti.",
                "why_need_it_en": "If a user enters 'abc' instead of a number in an ATM, the ATM shouldn't shut down and reboot! It should catch the error and say 'Please enter valid digits'.",
                "why_need_it_hi": "ATM me agar kisi ne number ki jagah text daal diya to machine band nahi honi chahiye, bas bolna chahiye 'Valid PIN dalo'.",
                "how_to_use_en": "try: risky_code() except Exception as e: handle_error(e).",
                "how_to_use_hi": "try: ... except Exception as e: print('Error:', e).",
                "syntax": "try:\n    user_num = int(\"not_a_number\")\nexcept ValueError:\n    print(\"Invalid input! Please enter digits only.\")",
                "rules_en": [
                    "If no error occurs in the 'try' block, the 'except' block is completely skipped.",
                    "As soon as an error occurs in 'try', remaining lines in the 'try' block are abandoned.",
                    "Execution continues normally with the code after the except block."
                ],
                "rules_hi": [
                    "Agar try me koi error nahi aaya to except block poora skip ho jata hai.",
                    "Jaise hi try me error aata hai, uske neeche ki lines chhod kar seedhe except me jump hota hai.",
                    "Program band hone ke bajaye aage smoothly chalta rehta hai."
                ],
                "analogy_en": "An acrobat walking a tightrope with a safety net underneath. If they walk across safely, the net is never used. If they slip, the net catches them safely so they don't die.",
                "analogy_hi": "Circus ke jhoolne wale ke neeche laga safety net — agar gira to net me bach jayega, zameen par gir kar marega nahi.",
                "common_mistakes": [
                    {
                        "mistake": "Using a bare except: 'except:' with no exception type specified.",
                        "why_it_fails_en": "A bare except catches EVERYTHING, including KeyboardInterrupt (Ctrl+C) and SystemExit, making it impossible to stop your program!",
                        "why_it_fails_hi": "Bare except Ctrl+C ko bhi pakad leta hai jisse program ko terminal se band karna namumkin ho jata hai.",
                        "fix": "Always catch at least 'except Exception:' or specific errors."
                    }
                ],
                "example_1": {
                    "title": "Graceful User Input Recovery",
                    "title_hi": "User input me aane wale crash ko rokna",
                    "code": "raw_input = 'twenty'\ntry:\n    age = int(raw_input)\n    print('Age is:', age)\nexcept ValueError:\n    print('Fallback: Could not convert text to number.')",
                    "expected_output": "Fallback: Could not convert text to number.",
                    "explanation_en": "ValueError is intercepted cleanly without terminating the script.",
                    "explanation_hi": "ValueError aane par bhi script crash nahi hui, fallback message dikhaya."
                },
                "example_2": {
                    "title": "Capturing the Error Object with 'as e'",
                    "title_hi": "Error message ko variable me store karna ('as e')",
                    "code": "try:\n    arr = [1, 2]\n    print(arr[5])\nexcept IndexError as err:\n    print('Caught error description:', err)",
                    "expected_output": "Caught error description: list index out of range",
                    "explanation_en": "'as err' binds the exception object, allowing inspection of its error message.",
                    "explanation_hi": "'as err' se error ka exact message inspect kiya ja sakta hai."
                },
                "challenge": {
                    "prompt_en": "Wrap int('abc') in try-except ValueError and print: Handled ValueError successfully",
                    "prompt_hi": "int('abc') ko try-except ValueError me wrap karo aur print karo: Handled ValueError successfully",
                    "starter_code": "# Handle ValueError:\n",
                    "expected_output": "Handled ValueError successfully",
                    "solution_code": "try:\n    n = int('abc')\nexcept ValueError:\n    print('Handled ValueError successfully')",
                    "solution_explanation_en": "Catches ValueError and prints confirmation.",
                    "solution_explanation_hi": "ValueError pakad kar confirmation print karta hai.",
                    "hints": ["try:\\n    int('abc')\\nexcept ValueError:\\n    print(...)"],
                    "ego_roast_hi": "ValueError pakadna nahi aaya?",
                    "ego_cheer_hi": "Graceful error recovery verified! 🦺"
                }
            },
            {
                "id": "ch16_sub3_specific_errors",
                "title": "Catching specific errors (e.g., ZeroDivisionError, ValueError)",
                "title_hi": "Specific errors pakadna (ZeroDivisionError, ValueError, KeyError)",
                "icon": "🎯",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Different bugs need different recovery solutions! Python lets you attach multiple 'except' blocks to a single 'try', handling ValueError, ZeroDivisionError, FileNotFoundError, and KeyError with tailored solutions.",
                "what_is_it_hi": "Alag-alag galtiyon ke liye alag-alag ilaaj chahiye hota hai! Python ek hi 'try' ke sath multiple 'except' blocks lagane deta hai — ValueError ka alag solution, ZeroDivisionError ka alag solution, KeyError ka alag solution.",
                "why_need_it_en": "If a file is missing, prompt to create one. If user input is invalid, prompt to retype. If division is zero, set result to 0. Specific handlers give accurate user feedback.",
                "why_need_it_hi": "File missing ho to nayi file banao. Zero division ho to answer 0 set karo. Har problem ka alag ilaaj specific except se hota hai.",
                "how_to_use_en": "try: ... except ValueError: ... except ZeroDivisionError: ... except KeyError: ...",
                "how_to_use_hi": "try: ... except ValueError: ... except ZeroDivisionError: ...",
                "syntax": "try:\n    val = int(data[\"price\"]) / count\nexcept KeyError:\n    print(\"Missing 'price' field!\")\nexcept ValueError:\n    print(\"'price' is not a valid number!\")\nexcept ZeroDivisionError:\n    print(\"Count cannot be zero!\")",
                "rules_en": [
                    "Python tests except blocks from top to bottom and runs ONLY the first matching handler.",
                    "Put more specific exceptions FIRST, and broader parent exceptions (like Exception) LAST.",
                    "You can catch multiple exceptions in one block: except (ValueError, TypeError):."
                ],
                "rules_hi": [
                    "Python upar se neeche except check karta hai aur pehla match chalaata hai.",
                    "Chhote specific errors pehle likho, aur general 'Exception' sabse aakhri me.",
                    "Ek sath do errors bhi pakad sakte ho: except (ValueError, TypeError):."
                ],
                "analogy_en": "A hospital emergency room triage: A bone fracture goes to orthopedics; a burn goes to burn ICU; a cold goes to general physician.",
                "analogy_hi": "Hospital ke alag-alag wards jaise: Haddi tooti to Orthopedic ward, aakh me dard to Eye specialist, bukhar to General ward.",
                "common_mistakes": [
                    {
                        "mistake": "Placing 'except Exception:' BEFORE specific exceptions.",
                        "why_it_fails_en": "Because Exception is the parent of all standard errors, it catches everything first! The specific handlers underneath become unreachable dead code.",
                        "why_it_fails_hi": "Bada Exception upar rakh doge to neeche ke specific handlers kabhi chalenge hi nahi.",
                        "fix": "Always place 'except Exception:' at the very bottom as the ultimate fallback."
                    }
                ],
                "example_1": {
                    "title": "Multiple Except Handlers",
                    "title_hi": "Alag-alag errors ke liye alag except",
                    "code": "def safe_divide(a, b):\n    try:\n        return int(a) / int(b)\n    except ZeroDivisionError:\n        return 'Cannot divide by zero!'\n    except ValueError:\n        return 'Please provide valid integers!'\n\nprint(safe_divide(10, 0))\nprint(safe_divide('ten', 2))\nprint(safe_divide(20, 4))",
                    "expected_output": "Cannot divide by zero!\nPlease provide valid integers!\n5.0",
                    "explanation_en": "ZeroDivisionError handles b=0; ValueError handles non-integer text; clean execution yields 5.0.",
                    "explanation_hi": "Dono alag errors ko unke specific handlers pakadte hain."
                },
                "example_2": {
                    "title": "Catching Multiple Exceptions in a Tuple",
                    "title_hi": "Ek hi except me multiple errors",
                    "code": "try:\n    res = int('abc')\nexcept (ValueError, TypeError):\n    print('Handled input formatting error!')",
                    "expected_output": "Handled input formatting error!",
                    "explanation_en": "A tuple of exceptions catches either ValueError or TypeError.",
                    "explanation_hi": "Tuple me band karke dono me se koi bhi error aane par pakad leta hai."
                },
                "challenge": {
                    "prompt_en": "Test multi-except: given d = {}, accessing d['key'] throws KeyError. Catch KeyError specifically and print: KeyError intercepted",
                    "prompt_hi": "d = {} me d['key'] access karke KeyError pakdo aur print karo: KeyError intercepted",
                    "starter_code": "d = {}\n# Catch KeyError specifically:\n",
                    "expected_output": "KeyError intercepted",
                    "solution_code": "d = {}\ntry:\n    val = d['key']\nexcept KeyError:\n    print('KeyError intercepted')",
                    "solution_explanation_en": "Catches KeyError specifically.",
                    "solution_explanation_hi": "KeyError pakad kar message print karta hai.",
                    "hints": ["except KeyError:\\n    print('KeyError intercepted')"],
                    "ego_roast_hi": "KeyError pakadna bhool gaye?",
                    "ego_cheer_hi": "Specific exception triage verified! 🎯"
                }
            },
            {
                "id": "ch16_sub4_else_finally_blocks",
                "title": "The else and finally blocks",
                "title_hi": "The else aur finally blocks",
                "icon": "🔄",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "The complete exception pipeline is try-except-else-finally: 'else' runs ONLY IF NO EXCEPTION occurred in the try block; 'finally' runs UNCONDITIONALLY, GUARANTEED (even if the code crashed or returned early!), making it perfect for cleanup.",
                "what_is_it_hi": "Poora exception pipeline: try-except-else-finally. 'else' tab chalta hai jab try me KOI GATLI NAHI HUI. 'finally' HAR HAAL ME GUARANTEE KE SATH CHALTA HAI — chahe code crash ho ya successfully khatam ho!",
                "why_need_it_en": "Cleanup: Closing database connections, releasing camera hardware, or turning off network sockets must happen whether your query succeeded or failed. That cleanup goes in 'finally'.",
                "why_need_it_hi": "Database connection band karna, camera light off karna — chahe app chale ya crash ho, ye cleanup 'finally' me hi hota hai.",
                "how_to_use_en": "try: ... except: ... else: ... finally: cleanup().",
                "how_to_use_hi": "try -> except -> else -> finally.",
                "syntax": "try:\n    # Risky code\n    f = open(\"data.txt\")\nexcept FileNotFoundError:\n    print(\"File missing!\")\nelse:\n    print(\"File opened successfully!\")\nfinally:\n    print(\"Cleanup: Always executed no matter what!\")",
                "rules_en": [
                    "'else' runs ONLY if try succeeded with zero exceptions.",
                    "'finally' ALWAYS runs (even if a return statement was hit inside try or except!).",
                    "Never put critical business logic in finally; reserve it strictly for resource cleanup."
                ],
                "rules_hi": [
                    "'else' tabhi chalta hai jab try bina kisi error ke pass ho.",
                    "'finally' hamesha chalta hai, chahe return statement hi kyun na aa gaya ho.",
                    "'finally' me sirf cleanup aur resource release ka code likha jata hai."
                ],
                "analogy_en": "Cooking dinner: 'try' is cooking. 'except' is ordering pizza if the food burnt. 'else' is serving the food to guests if it turned out delicious. 'finally' is doing the dishes and cleaning the kitchen in either case!",
                "analogy_hi": "Khana banana: 'try' khana banana hai. 'except' jalne par Swiggy order karna hai. 'else' mast banne par mehmaano ko khilana hai. 'finally' dono case me aakhri me bartan dhona hai!",
                "common_mistakes": [
                    {
                        "mistake": "Thinking 'else' runs when an error occurs.",
                        "why_it_fails_en": "'else' is the opposite of 'except'! 'else' means 'no error occurred'.",
                        "why_it_fails_hi": "'else' ka matlab hota hai 'koi galti nahi hui'.",
                        "fix": "Remember: except runs on error; else runs on success."
                    }
                ],
                "example_1": {
                    "title": "Full Try-Except-Else-Finally Pipeline (Success Case)",
                    "title_hi": "Success hone par else aur finally dono chalna",
                    "code": "try:\n    result = 10 / 2\nexcept ZeroDivisionError:\n    print('Handled error')\nelse:\n    print('Success (else): Result is', result)\nfinally:\n    print('Cleanup (finally): Operation finished.')",
                    "expected_output": "Success (else): Result is 5.0\nCleanup (finally): Operation finished.",
                    "explanation_en": "try succeeded -> else ran -> finally ran unconditionally.",
                    "explanation_hi": "try pass hua to else chala, aur aakhri me finally chala."
                },
                "example_2": {
                    "title": "Finally Runs Even on Error",
                    "title_hi": "Error aane par bhi finally ka chalna",
                    "code": "try:\n    val = 10 / 0\nexcept ZeroDivisionError:\n    print('Handled divide by zero')\nfinally:\n    print('Guaranteed cleanup executed!')",
                    "expected_output": "Handled divide by zero\nGuaranteed cleanup executed!",
                    "explanation_en": "even though an error occurred, finally still executes without fail.",
                    "explanation_hi": "Error aane ke baad bhi finally block zaroor chalta hai."
                },
                "challenge": {
                    "prompt_en": "Write a try-finally block: inside try, print 'Running'. Inside finally, print 'Always Done'.",
                    "prompt_hi": "try-finally block likho: try me print 'Running', finally me print 'Always Done'.",
                    "starter_code": "# Write try-finally:\n",
                    "expected_output": "Running\nAlways Done",
                    "solution_code": "try:\n    print('Running')\nfinally:\n    print('Always Done')",
                    "solution_explanation_en": "try prints 'Running', followed immediately by finally printing 'Always Done'.",
                    "solution_explanation_hi": "try ke baad finally execute hota hai.",
                    "hints": ["try:\\n    print('Running')\\nfinally:\\n    print('Always Done')"],
                    "ego_roast_hi": "finally block bhool gaye?",
                    "ego_cheer_hi": "Try-Except-Else-Finally masterclass completed! 🔄"
                }
            },
            {
                "id": "ch16_sub5_custom_raise_errors",
                "title": "Creating your own custom errors using raise",
                "title_hi": "Apne custom errors create karna: raise keyword",
                "icon": "🚨",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "The 'raise' keyword intentionally triggers an exception when your code encounters an invalid state (e.g., negative bank balance, invalid password length). You can raise existing standard errors or create your own custom Exception classes.",
                "what_is_it_hi": "'raise' keyword se aap jaan-boojhkar error trigger karte ho jab koi business rule toot jata hai (jaise age negative ho, ya balance se zyada paise nikale ja rahe hon). Aap standard errors (raise ValueError) ya apni custom class raise kar sakte ho.",
                "why_need_it_en": "Data Validation: Python doesn't know that age = -5 or withdraw_amount = 1000000000 is invalid in your business domain. You must raise errors to enforce your application's rules.",
                "why_need_it_hi": "Business rules enforce karna: Python ko nahi pata ki age -5 saal nahi ho sakti. Invalid data milte hi 'raise' karke code ko aage badhne se rokna padta hai.",
                "how_to_use_en": "if age < 0: raise ValueError('Age cannot be negative!').",
                "how_to_use_hi": "if balance < amount: raise ValueError('Insufficient funds').",
                "syntax": "# Raising built-in exception:\nif age < 0:\n    raise ValueError(\"Age cannot be negative!\")\n\n# Defining custom exception class:\nclass InsufficientFundsError(Exception):\n    pass\n\nraise InsufficientFundsError(\"Account balance too low!\")",
                "rules_en": [
                    "You must raise an instance of BaseException (or a class derived from Exception).",
                    "Always provide a helpful error message string when raising.",
                    "Custom exceptions should inherit from Python's built-in 'Exception' class."
                ],
                "rules_hi": [
                    "raise hamesha Exception class ya uske derived child ka hona chahiye.",
                    "Error ke andar helpful message string zaroor pass karo.",
                    "Custom exception class banane ke liye 'class MyError(Exception): pass' likho."
                ],
                "analogy_en": "Pulling the red emergency brake handle in a train because a passenger noticed smoke. The train didn't crash on its own; a human intentionally raised the alarm.",
                "analogy_hi": "Train me red emergency chain kheenchne jaisa — train kharab nahi hui, aapne jaan-boojhkar alarm bajaya kyunki rule toot gaya tha.",
                "common_mistakes": [
                    {
                        "mistake": "Raising a raw string: raise 'Error occurred'",
                        "why_it_fails_en": "TypeError: exceptions must derive from BaseException. Strings cannot be raised in Python 3.",
                        "why_it_fails_hi": "Python 3 me direct string raise nahi ho sakti, Exception object hona chahiye.",
                        "fix": "Raise an exception class: raise ValueError('Error occurred')."
                    }
                ],
                "example_1": {
                    "title": "Raising a ValueError for Validation",
                    "title_hi": "Age validation me raise ValueError",
                    "code": "def set_age(age):\n    if age < 0:\n        raise ValueError('Age cannot be negative!')\n    return f'Age set to {age}'\n\ntry:\n    set_age(-5)\nexcept ValueError as e:\n    print('Intercepted raised error:', e)",
                    "expected_output": "Intercepted raised error: Age cannot be negative!",
                    "explanation_en": "set_age raises ValueError on invalid input, intercepted safely by try-except.",
                    "explanation_hi": "Negative number aate hi ValueError raise hua aur try-except ne use pakad liya."
                },
                "example_2": {
                    "title": "Custom Domain Exception Class",
                    "title_hi": "Custom Exception class banana",
                    "code": "class AuthError(Exception):\n    pass\n\ntry:\n    raise AuthError('Invalid API token!')\nexcept AuthError as e:\n    print('Custom Exception Caught:', e)",
                    "expected_output": "Custom Exception Caught: Invalid API token!",
                    "explanation_en": "AuthError is a custom exception class subclassing Exception.",
                    "explanation_hi": "AuthError custom exception class ko raise karke pakadta hai."
                },
                "challenge": {
                    "prompt_en": "Raise ValueError('Invalid Value') inside a function, catch it in try-except, and print: Caught custom: Invalid Value",
                    "prompt_hi": "raise ValueError('Invalid Value') ko try-except me pakad kar print karo: Caught custom: Invalid Value",
                    "starter_code": "# Raise and catch ValueError:\n",
                    "expected_output": "Caught custom: Invalid Value",
                    "solution_code": "try:\n    raise ValueError('Invalid Value')\nexcept ValueError as e:\n    print(f'Caught custom: {e}')",
                    "solution_explanation_en": "Raises ValueError and catches it safely.",
                    "solution_explanation_hi": "ValueError raise karke message print karta hai.",
                    "hints": ["try:\\n    raise ValueError('Invalid Value')\\nexcept ValueError as e:\\n    print(f'Caught custom: {e}')"],
                    "ego_roast_hi": "raise keyword use karna bhool gaye?",
                    "ego_cheer_hi": "Custom exception raising mastery verified! 🚨"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 17: Thinking Like a Software Engineer (Intro to OOP)
    # =========================================================================
    {
        "id": "ch17_intro_oop",
        "part_number": 5,
        "part_title": "PART 5: THE REAL WORLD (FILES, ERRORS, AND OBJECTS)",
        "chapter_number": 17,
        "title": "Chapter 17: Thinking Like a Software Engineer (Intro to OOP)",
        "subtitle_en": "Classes as blueprints, objects as instances, attributes, methods, __init__, and self",
        "subtitle_hi": "OOP ki shuruat: Blueprint classes, objects, attributes, methods, __init__ aur self",
        "icon": "🏗️",
        "estimated_time": "40 mins",
        "prerequisites_en": "Chapters 12 & 13 (Functions and dictionaries).",
        "prerequisites_hi": "Chapter 12 aur 13 (Functions aur dictionaries).",
        "learning_objectives_en": [
            "Understand the Object-Oriented Programming (OOP) mental model",
            "Define classes using the 'class' keyword",
            "Instantiate real objects from classes",
            "Store state inside instance attributes",
            "Define behavior using methods",
            "Master the __init__ constructor and the 'self' keyword"
        ],
        "learning_objectives_hi": [
            "OOP ka blueprint mental model samjho",
            "'class' keyword se blueprint banana",
            "Class se real objects (instances) create karna",
            "Attributes me data store karna aur methods se actions karwana",
            "__init__ constructor aur 'self' ka exact kaam master karo"
        ],
        "recap_en": "You mastered foundational Object-Oriented Programming: classes as blueprints, instantiation, instance attributes, methods, the __init__ constructor, and how 'self' binds instance identity.",
        "recap_hi": "Aapne OOP foundation: classes, objects, attributes, methods, __init__ aur self master kiya.",
        "subtopics": [
            {
                "id": "ch17_sub1_what_is_oop",
                "title": "What is Object-Oriented Programming (OOP)? (The blueprint analogy)",
                "title_hi": "Object-Oriented Programming (OOP) kya hai? (The Blueprint Analogy)",
                "icon": "📐",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Object-Oriented Programming (OOP) is a software design paradigm that organizes code around real-world 'objects' that bundle DATA (attributes) and BEHAVIOR (methods) together into a single cohesive unit.",
                "what_is_it_hi": "Object-Oriented Programming (OOP) coding ka ek aadhunik style hai jisme code ko real-world 'objects' ke roop me banaya jata hai. Har object ke paas apna DATA (attributes) aur apne ACTIONS (methods) ek hi dabba me hote hain.",
                "why_need_it_en": "Procedural programming gets messy when managing 500 game enemies. With OOP, you create an 'Enemy' blueprint once, and stamp out 500 enemy objects each with their own health, x/y position, and attack() method.",
                "why_need_it_hi": "Game me 100 enemies banane hon to alag-alag variables banana mushkil hai. OOP me ek 'Enemy' class banao aur 100 naye objects 1 second me create kar lo.",
                "how_to_use_en": "Create class Blueprint: instantiate obj = Blueprint().",
                "how_to_use_hi": "class banao aur usse objects instantiate karo.",
                "syntax": "class Car:\n    # Blueprint definition\n    pass\n\n# Create concrete objects from blueprint:\ncar1 = Car()\ncar2 = Car()",
                "rules_en": [
                    "Class = The abstract blueprint/template.",
                    "Object = The physical, concrete instance built from that blueprint.",
                    "Classes use PascalCase naming convention (e.g., BankAccount, ShoppingCart)."
                ],
                "rules_hi": [
                    "Class = Naksha ya blueprint.",
                    "Object = Us nakshe se bani asli building ya car.",
                    "Class ka naam hamesha PascalCase me hota hai (StudentProfile, BankAccount)."
                ],
                "analogy_en": "An architect's blueprint for a house: The blueprint is the CLASS (paper drawing). The 10 actual brick-and-mortar houses built in the neighborhood are the OBJECTS.",
                "analogy_hi": "Ghar ka naksha (Blueprint): Naksha CLASS hai. Us nakshe se colony me bane 10 asli makan OBJECTS hain.",
                "common_mistakes": [
                    {
                        "mistake": "Naming classes in snake_case: class bank_account:",
                        "why_it_fails_en": "Violates PEP 8 naming convention. Classes must use PascalCase (CapWords).",
                        "why_it_fails_hi": "Class ka naam lowercase me nahi hona chahiye.",
                        "fix": "Use PascalCase: class BankAccount:"
                    }
                ],
                "example_1": {
                    "title": "Blueprint vs Instances",
                    "title_hi": "Class aur Object ka live relation",
                    "code": "class Robot:\n    pass\n\nr1 = Robot()\nr2 = Robot()\nprint('r1 is a Robot:', isinstance(r1, Robot))\nprint('r1 and r2 are distinct objects:', r1 is not r2)",
                    "expected_output": "r1 is a Robot: True\nr1 and r2 are distinct objects: True",
                    "explanation_en": "r1 and r2 are two independent objects created from the same Robot class.",
                    "explanation_hi": "r1 aur r2 dono Robot class se bane do alag-alag objects hain."
                },
                "example_2": {
                    "title": "Type Name of an Instance",
                    "title_hi": "Instance ka class type check",
                    "code": "class Player:\n    pass\n\np = Player()\nprint('Object type:', type(p).__name__)",
                    "expected_output": "Object type: Player",
                    "explanation_en": "type(p) confirms the object is an instance of class Player.",
                    "explanation_hi": "type(p) batata hai ki p Player class ka object hai."
                },
                "challenge": {
                    "prompt_en": "Define an empty class Hero with pass, create hero1 = Hero(), and print: Hero created: True",
                    "prompt_hi": "class Hero: pass banao, hero1 = Hero() create karo aur print karo: Hero created: True",
                    "starter_code": "# Define class Hero and instantiate:\n",
                    "expected_output": "Hero created: True",
                    "solution_code": "class Hero:\n    pass\n\nhero1 = Hero()\nprint(f'Hero created: {isinstance(hero1, Hero)}')",
                    "solution_explanation_en": "Instantiates Hero class and verifies with isinstance.",
                    "solution_explanation_hi": "Hero class bana kar uska object banata hai.",
                    "hints": ["class Hero:\\n    pass\\nhero1 = Hero()"],
                    "ego_roast_hi": "Class define karna bhool gaye?",
                    "ego_cheer_hi": "OOP blueprint model verified! 🏗️"
                }
            },
            {
                "id": "ch17_sub2_classes",
                "title": "Creating a Blueprint: Classes",
                "title_hi": "Blueprint banana: Classes",
                "icon": "🏛️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A class is created using the 'class' keyword followed by the class name in PascalCase and a colon (:). It defines the attributes and methods that every object of this type will possess.",
                "what_is_it_hi": "'class' keyword se class banayi jaati hai. Isme wo saare rules, variables aur functions define hote hain jo is type ke har object ke paas honge.",
                "why_need_it_en": "Classes enforce consistency: every 'User' object is guaranteed to have a username, email, and login() method.",
                "why_need_it_hi": "Consistency ke liye: class ye guarantee deti hai ki har User object ke paas username, email aur password hoga hi hoga.",
                "how_to_use_en": "class ClassName: followed by indented methods and attributes.",
                "how_to_use_hi": "class Student: ke andar functions aur variables likho.",
                "syntax": "class BankAccount:\n    # Class blueprint\n    bank_name = \"Elysia Bank\"  # Class attribute",
                "rules_en": [
                    "Use the 'class' keyword.",
                    "Class names MUST follow PascalCase (CapitalizeEveryWord, no underscores).",
                    "Class body must be indented by 4 spaces."
                ],
                "rules_hi": [
                    "'class' keyword use hota hai.",
                    "Class name PascalCase me hota hai (StudentRecord).",
                    "Class ke andar ka code 4 spaces aage hota hai."
                ],
                "analogy_en": "A cookie cutter: the cookie cutter itself is made of metal (the class). It doesn't taste good, but it defines the exact shape of all 50 ginger cookies you bake.",
                "analogy_hi": "Biskut banane ka saancha (cookie cutter) — saancha khud biskut nahi hai, lekin har biskut ka shape wahi decide karta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Adding parentheses in class definition when not inheriting: class Car():",
                        "why_it_fails_en": "While legal in Python, empty parentheses are redundant and considered poor style.",
                        "why_it_fails_hi": "Bina inheritance ke empty brackets () lagana unnecessary hota hai.",
                        "fix": "Use clean syntax: class Car:"
                    }
                ],
                "example_1": {
                    "title": "Class with Class-Level Attribute",
                    "title_hi": "Class attribute ka example",
                    "code": "class University:\n    name = 'Elysia Tech'\n\nprint('Institution Name:', University.name)",
                    "expected_output": "Institution Name: Elysia Tech",
                    "explanation_en": "Class attributes are shared across all instances of the class.",
                    "explanation_hi": "Class attribute sabhi objects ke liye shared hota hai."
                },
                "example_2": {
                    "title": "Class Defining a Method",
                    "title_hi": "Class me method define karna",
                    "code": "class Greeter:\n    def say_hello(self):\n        return 'Hello from Greeter!'\n\ng = Greeter()\nprint(g.say_hello())",
                    "expected_output": "Hello from Greeter!",
                    "explanation_en": "Defines a method inside a class and executes it on an instance.",
                    "explanation_hi": "Class ke andar method bana kar object se call karta hai."
                },
                "challenge": {
                    "prompt_en": "Create class App with class attribute version = 2.0. Print: App v2.0",
                    "prompt_hi": "class App banao jisme version = 2.0 ho aur print karo: App v2.0",
                    "starter_code": "# Define class App and print version:\n",
                    "expected_output": "App v2.0",
                    "solution_code": "class App:\n    version = 2.0\n\nprint(f'App v{App.version}')",
                    "solution_explanation_en": "Accesses class attribute App.version.",
                    "solution_explanation_hi": "App.version access karke print karta hai.",
                    "hints": ["class App:\\n    version = 2.0"],
                    "ego_roast_hi": "Class attribute banana bhool gaye?",
                    "ego_cheer_hi": "Class blueprint defined cleanly! 🏛️"
                }
            },
            {
                "id": "ch17_sub3_objects_instances",
                "title": "Building from the Blueprint: Objects (Instances)",
                "title_hi": "Blueprint se build karna: Objects (Instances)",
                "icon": "🏭",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "An object (instance) is created by 'calling' the class with parentheses: my_car = Car(). Instantiation allocates dedicated memory in RAM for this specific object.",
                "what_is_it_hi": "Object (instance) class ke aage brackets () laga kar call karne se banta hai: my_car = Car(). Isse RAM me us specific object ke liye nayi jagah allocate hoti hai.",
                "why_need_it_en": "Each object holds its own independent state. Modifying player1's health does not hurt player2's health!",
                "why_need_it_hi": "Har object ki apni alag memory hoti hai. Player1 ki health kam hone se Player2 ki health par koi asar nahi padta.",
                "how_to_use_en": "obj1 = MyClass(); obj2 = MyClass().",
                "how_to_use_hi": "obj1 = MyClass(); obj2 = MyClass().",
                "syntax": "class Student:\n    pass\n\n# Two independent instances:\ns1 = Student()\ns2 = Student()",
                "rules_en": [
                    "Parentheses () are required to instantiate a class.",
                    "Each instance has a unique memory ID: id(obj1) != id(obj2).",
                    "Use isinstance(obj, ClassName) to verify instance lineage."
                ],
                "rules_hi": [
                    "Class se object banane ke liye brackets () lagana zaroori hai.",
                    "Har object ka RAM me alag memory address hota hai.",
                    "isinstance() se verify kar sakte ho ki object kis class ka hai."
                ],
                "analogy_en": "You have a car factory CAD file (class). The factory stamps out a Red Honda Civic for Alex and a Blue Honda Civic for Sara. Both are independent physical cars (objects).",
                "analogy_hi": "Factory me car ka naksha hai. Factory ne ek Red car banayi aur ek Blue car banayi. Dono alag-alag gaadiyan (objects) hain.",
                "common_mistakes": [
                    {
                        "mistake": "Assigning class without parentheses: my_car = Car",
                        "why_it_fails_en": "my_car becomes an alias to the class itself, NOT an instance!",
                        "why_it_fails_hi": "Bina () ke naya object nahi banta, bas class ka doosra naam ban jata hai.",
                        "fix": "Always instantiate with parentheses: my_car = Car()."
                    }
                ],
                "example_1": {
                    "title": "Multiple Distinct Instances",
                    "title_hi": "Do alag-alag objects",
                    "code": "class Account:\n    pass\n\nacc1 = Account()\nacc2 = Account()\nprint('Same class?', type(acc1) == type(acc2))\nprint('Separate memory IDs?', id(acc1) != id(acc2))",
                    "expected_output": "Same class? True\nSeparate memory IDs? True",
                    "explanation_en": "acc1 and acc2 share the same type, but occupy distinct memory addresses.",
                    "explanation_hi": "Dono same class ke hain lekin RAM me do alag jagah hain."
                },
                "example_2": {
                    "title": "Verifying Object Identity with isinstance",
                    "title_hi": "isinstance se check karna",
                    "code": "class Dog:\n    pass\n\npet = Dog()\nprint('pet is an instance of Dog:', isinstance(pet, Dog))",
                    "expected_output": "pet is an instance of Dog: True",
                    "explanation_en": "isinstance validates the object against its parent class.",
                    "explanation_hi": "isinstance verify karta hai ki pet Dog ka object hai."
                },
                "challenge": {
                    "prompt_en": "Create class Box. Instantiate b1 = Box() and b2 = Box(). Print: Two boxes: True",
                    "prompt_hi": "class Box banao, b1 = Box() aur b2 = Box() banao aur print karo: Two boxes: True",
                    "starter_code": "# Instantiate two Box objects:\n",
                    "expected_output": "Two boxes: True",
                    "solution_code": "class Box:\n    pass\n\nb1 = Box()\nb2 = Box()\nprint(f'Two boxes: {b1 is not b2}')",
                    "solution_explanation_en": "Instantiates two distinct Box objects.",
                    "solution_explanation_hi": "Do alag Box objects banata hai.",
                    "hints": ["b1 = Box()\\nb2 = Box()\\nprint(f'Two boxes: {b1 is not b2}')"],
                    "ego_roast_hi": "Objects instantiate karna bhool gaye?",
                    "ego_cheer_hi": "Object instantiation verified! 🏭"
                }
            },
            {
                "id": "ch17_sub4_attributes",
                "title": "Attributes (Variables inside classes)",
                "title_hi": "Attributes (Classes ke andar ke variables)",
                "icon": "🏷️",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "Attributes are variables that belong to an object. They store the object's characteristics (state) — like person.name, car.speed, or button.color.",
                "what_is_it_hi": "Attributes wo variables hote hain jo kisi object ke andar uska data (state) store karte hain — jaise student.name, car.speed, user.email.",
                "why_need_it_en": "Objects need to remember their own data! An e-commerce user object must remember its own cart items and shipping address.",
                "why_need_it_hi": "Object ko apna data yaad rakhna hota hai: User object ko apna naam aur balance yaad rakhna padta hai.",
                "how_to_use_en": "Access with dot notation: obj.attribute_name.",
                "how_to_use_hi": "Dot notation se read aur update karo: obj.name = 'Alex'.",
                "syntax": "class Person:\n    pass\n\np = Person()\np.name = \"Alex\"   # Assigning attribute\nprint(p.name)     # Reading attribute",
                "rules_en": [
                    "Instance attributes are specific to each individual object (obj.x).",
                    "Class attributes are shared by ALL objects of that class (ClassName.x).",
                    "Accessing a non-existent attribute raises AttributeError: 'Object' has no attribute 'x'."
                ],
                "rules_hi": [
                    "Instance attribute har object ka apna personal data hota hai (p1.name alag, p2.name alag).",
                    "Class attribute sabhi objects me common hota hai.",
                    "Jo attribute exist nahi karta use access karne par AttributeError aayega."
                ],
                "analogy_en": "Adjectives describing a noun: A car is a noun (object). Its color, horsepower, and fuel level are its adjectives (attributes).",
                "analogy_hi": "Insaan ki khasiyat: Insaan object hai; uski lambai, rang aur naam uske attributes hain.",
                "common_mistakes": [
                    {
                        "mistake": "Confusing class attributes with instance attributes, accidentally modifying a shared class list.",
                        "why_it_fails_en": "Modifying a class-level list mutates it across all instances simultaneously!",
                        "why_it_fails_hi": "Class attribute modify karne par saare objects ka data ek sath badal jata hai.",
                        "fix": "Always initialize instance-specific attributes inside __init__ using self."
                    }
                ],
                "example_1": {
                    "title": "Assigning and Reading Instance Attributes",
                    "title_hi": "Instance attribute assign aur read karna",
                    "code": "class Car:\n    pass\n\nc1 = Car()\nc1.brand = 'Toyota'\nc1.speed = 120\nprint(f'{c1.brand} speed: {c1.speed} km/h')",
                    "expected_output": "Toyota speed: 120 km/h",
                    "explanation_en": "brand and speed are instance attributes attached to c1.",
                    "explanation_hi": "c1 object me brand aur speed attributes attach karke print karta hai."
                },
                "example_2": {
                    "title": "Independent Attributes Across Instances",
                    "title_hi": "Do objects ke alag-alag attributes",
                    "code": "class Player:\n    pass\n\np1 = Player()\np2 = Player()\np1.health = 100\np2.health = 50\nprint(f'P1: {p1.health} HP | P2: {p2.health} HP')",
                    "expected_output": "P1: 100 HP | P2: 50 HP",
                    "explanation_en": "p1 and p2 maintain distinct health states independently.",
                    "explanation_hi": "p1 aur p2 ka health state alag-alag rehta hai."
                },
                "challenge": {
                    "prompt_en": "Create class Item with pass. Instantiate i = Item(), set i.price = 250, and print: Price: $250",
                    "prompt_hi": "class Item banao, i = Item() instantiate karke i.price = 250 set karo aur print karo: Price: $250",
                    "starter_code": "# Create Item, set price, and print:\n",
                    "expected_output": "Price: $250",
                    "solution_code": "class Item:\n    pass\n\ni = Item()\ni.price = 250\nprint(f'Price: ${i.price}')",
                    "solution_explanation_en": "Sets i.price and prints the attribute.",
                    "solution_explanation_hi": "i.price set karke print karta hai.",
                    "hints": ["i = Item()\\ni.price = 250\\nprint(f'Price: ${i.price}')"],
                    "ego_roast_hi": "Attribute set karna bhool gaye?",
                    "ego_cheer_hi": "Instance attributes validated! 🏷️"
                }
            },
            {
                "id": "ch17_sub5_methods",
                "title": "Methods (Functions inside classes)",
                "title_hi": "Methods (Classes ke andar ke functions)",
                "icon": "⚡",
                "duration": "5 mins",
                "xp": 50,
                "what_is_it_en": "A method is simply a function defined inside a class body. It defines the actions, verbs, and behaviors that an object can perform (like dog.bark(), car.accelerate(), user.login()).",
                "what_is_it_hi": "Method class ke andar define kiya gaya function hota hai. Ye batata hai ki object kya-kya ACTIONS kar sakta hai (jaise dog.bark(), car.drive(), account.deposit()).",
                "why_need_it_en": "Methods encapsulate logic with the data it operates on. Instead of passing account data into an external function, the account object manages its own deposit() logic.",
                "why_need_it_hi": "Methods se data aur action ek sath rehte hain: Account object khud apna deposit() aur withdraw() manage karta hai.",
                "how_to_use_en": "Define inside class with 'def method_name(self):'. Call with obj.method_name().",
                "how_to_use_hi": "class ke andar def method(self): likho. Call obj.method() se karo.",
                "syntax": "class Dog:\n    def bark(self):\n        return \"Woof! 🐶\"\n\nmy_dog = Dog()\nprint(my_dog.bark())",
                "rules_en": [
                    "Every instance method MUST accept 'self' as its first parameter.",
                    "Methods are called on instances using dot notation: object.method().",
                    "When called, Python automatically passes the object itself as the 'self' argument."
                ],
                "rules_hi": [
                    "Har instance method me pehla parameter 'self' hona MANDATORY hai.",
                    "Dot notation se call karte hain: obj.method().",
                    "Call karte waqt Python apne aap object ko 'self' me bhej deta hai."
                ],
                "analogy_en": "Verbs in English grammar: An object is a noun (Dog). Its methods are verbs (Bark, Run, Sleep).",
                "analogy_hi": "Grammar me Verbs jaisa: Dog Noun (object) hai; Bark, Run, Sleep uske Verbs (methods) hain.",
                "common_mistakes": [
                    {
                        "mistake": "Forgetting 'self' in method definition: def bark(): return 'Woof'",
                        "why_it_fails_en": "TypeError: bark() takes 0 positional arguments but 1 was given. Python automatically passed the object, but the method had no parameter to receive it!",
                        "why_it_fails_hi": "Python ne object bheja lekin method ne 'self' nahi lagaya tha to TypeError aayega.",
                        "fix": "Always write 'self' as the first parameter: def bark(self):"
                    }
                ],
                "example_1": {
                    "title": "Defining and Invoking a Method",
                    "title_hi": "Method banana aur run karna",
                    "code": "class Calculator:\n    def add(self, a, b):\n        return a + b\n\ncalc = Calculator()\nprint('Calculation result:', calc.add(15, 25))",
                    "expected_output": "Calculation result: 40",
                    "explanation_en": "calc.add passes calc as self, 15 as a, 25 as b, returning 40.",
                    "explanation_hi": "calc.add(15, 25) 40 calculate karke return karta hai."
                },
                "example_2": {
                    "title": "Method Modifying Object State",
                    "title_hi": "Method se object ka state badalna",
                    "code": "class Counter:\n    count = 0\n    def increment(self):\n        self.count += 1\n        return self.count\n\nc = Counter()\nprint('Turn 1:', c.increment())\nprint('Turn 2:', c.increment())",
                    "expected_output": "Turn 1: 1\nTurn 2: 2",
                    "explanation_en": "increment() method updates self.count on each call.",
                    "explanation_hi": "increment method har call par count 1 badha deta hai."
                },
                "challenge": {
                    "prompt_en": "Create class Light with method turn_on(self) returning 'Light is ON'. Call turn_on() on an instance and print output.",
                    "prompt_hi": "class Light banao jisme turn_on(self) return kare 'Light is ON'. Instance bana kar call karo aur print karo.",
                    "starter_code": "# Define Light class and call method:\n",
                    "expected_output": "Light is ON",
                    "solution_code": "class Light:\n    def turn_on(self):\n        return 'Light is ON'\n\nl = Light()\nprint(l.turn_on())",
                    "solution_explanation_en": "Defines and calls method turn_on.",
                    "solution_explanation_hi": "turn_on method call karke print karta hai.",
                    "hints": ["class Light:\\n    def turn_on(self):\\n        return 'Light is ON'"],
                    "ego_roast_hi": "self parameter lagana bhool gaye kya?",
                    "ego_cheer_hi": "Object methods verified! ⚡"
                }
            },
            {
                "id": "ch17_sub6_init_and_self",
                "title": "The magic setup method: __init__ and the self keyword",
                "title_hi": "Magic setup method: __init__ aur self keyword",
                "icon": "🧙‍♂️",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "__init__ is the CONSTRUCTOR method in Python: it executes AUTOMATICALLY the moment a new object is instantiated to setup initial attributes. 'self' is a reference to the CURRENT object instance being created or manipulated.",
                "what_is_it_hi": "__init__ Python ka CONSTRUCTOR method hai: jaise hi naya object banta hai, __init__ AUTOMATICALLY execute ho jata hai taaki initial values set ho sakein. 'self' ka matlab hota hai 'THIS OBJECT' — ye batata hai ki kis specific object ki baat ho rahi hai.",
                "why_need_it_en": "Without __init__, creating 100 users requires manually assigning 100 names and emails line-by-line! With __init__, you do it in 1 clean line: u = User('Alex', 'alex@test.com').",
                "why_need_it_hi": "__init__ ke bina har user ka naam aur email alag se 4 line likh kar assign karna padta. __init__ hone se u = User('Alex', 'alex@mail') 1 line me setup ho jata hai.",
                "how_to_use_en": "def __init__(self, name, age): self.name = name; self.age = age.",
                "how_to_use_hi": "def __init__(self, name): self.name = name.",
                "syntax": "class User:\n    def __init__(self, username, email):\n        # 'self.username' attaches attribute to THIS instance\n        self.username = username\n        self.email = email\n\n# __init__ runs automatically here:\nu1 = User(\"alex\", \"alex@test.com\")",
                "rules_en": [
                    "__init__ has TWO leading and TWO trailing underscores (a 'Dunder' method).",
                    "__init__ NEVER returns a value (it must return None; returning a value raises TypeError).",
                    "'self' must be the FIRST parameter of __init__ and all instance methods.",
                    "When calling User('Alex'), Python automatically passes the new object as 'self'."
                ],
                "rules_hi": [
                    "__init__ me 2 underscores aage aur 2 underscores peeche lagte hain (Dunder method).",
                    "__init__ kabhi koi value return nahi karta (return likhne par TypeError aayega).",
                    "'self' pehla parameter hona mandatory hai.",
                    "User('Alex') likhne par Python apne aap naye object ko 'self' me bhej deta hai."
                ],
                "analogy_en": "Birth certificate registration: When a baby is born (__init__), the registrar immediately writes the baby's name and birthdate on their permanent record.",
                "analogy_hi": "School admission form jaisa — admission lete hi (__init__) student ka naam aur roll number uske identity card (self) par print ho jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Spelling __init__ with single underscores: def _init_(self):",
                        "why_it_fails_en": "Python ignores it! It is not recognized as the constructor, so attributes are never initialized.",
                        "why_it_fails_hi": "Single underscore lagane se Python use constructor nahi maanta aur run hi nahi karta.",
                        "fix": "Always use double underscores on both sides: def __init__(self):"
                    }
                ],
                "example_1": {
                    "title": "Complete __init__ and self Implementation",
                    "title_hi": "Clean Constructor Implementation",
                    "code": "class Student:\n    def __init__(self, name, roll_no):\n        self.name = name\n        self.roll_no = roll_no\n\n    def introduce(self):\n        return f'I am {self.name}, Roll: {self.roll_no}'\n\ns1 = Student('Aman', 101)\nprint(s1.introduce())",
                    "expected_output": "I am Aman, Roll: 101",
                    "explanation_en": "__init__ sets self.name and self.roll_no; introduce() reads them via self.",
                    "explanation_hi": "__init__ ne values save ki aur introduce() ne self se padh kar print kiya."
                },
                "example_2": {
                    "title": "Default Arguments Inside __init__",
                    "title_hi": "__init__ me default parameters",
                    "code": "class Server:\n    def __init__(self, host='127.0.0.1', port=8080):\n        self.host = host\n        self.port = port\n\ns = Server()\nprint(f'Server listening at {s.host}:{s.port}')",
                    "expected_output": "Server listening at 127.0.0.1:8080",
                    "explanation_en": "__init__ can take default arguments for optional configuration.",
                    "explanation_hi": "__init__ me default arguments se safe fallback configuration banti hai."
                },
                "challenge": {
                    "prompt_en": "Create class Person with __init__(self, name). Instantiate p = Person('Alex') and print: Person: Alex",
                    "prompt_hi": "class Person banao jisme __init__(self, name) ho. p = Person('Alex') banao aur print karo: Person: Alex",
                    "starter_code": "# Define Person with __init__:\n",
                    "expected_output": "Person: Alex",
                    "solution_code": "class Person:\n    def __init__(self, name):\n        self.name = name\n\np = Person('Alex')\nprint(f'Person: {p.name}')",
                    "solution_explanation_en": "Defines __init__ constructor and prints self.name.",
                    "solution_explanation_hi": "__init__ constructor se self.name set karke print karta hai.",
                    "hints": ["def __init__(self, name):\\n    self.name = name"],
                    "ego_roast_hi": "__init__ me double underscores lagana bhool gaye?",
                    "ego_cheer_hi": "OOP constructor mastery achieved! 🧙‍♂️"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 18: Advanced Blueprinting (Advanced OOP)
    # =========================================================================
    {
        "id": "ch18_advanced_oop",
        "part_number": 5,
        "part_title": "PART 5: THE REAL WORLD (FILES, ERRORS, AND OBJECTS)",
        "chapter_number": 18,
        "title": "Chapter 18: Advanced Blueprinting (Advanced OOP)",
        "subtitle_en": "Inheritance, method overriding, super(), encapsulation, polymorphism, and dunder methods",
        "subtitle_hi": "Advanced OOP: Inheritance, super(), overriding, encapsulation, polymorphism aur dunder methods",
        "icon": "🧬",
        "estimated_time": "45 mins",
        "prerequisites_en": "Chapter 17 (Classes, objects, __init__, self).",
        "prerequisites_hi": "Chapter 17 (Classes, objects, __init__, self).",
        "learning_objectives_en": [
            "Implement single inheritance (Parent to Child class)",
            "Override parent methods and leverage super()",
            "Master encapsulation naming conventions (public, _protected, __private name mangling)",
            "Demonstrate polymorphism via uniform interfaces",
            "Harness special Dunder methods (__str__, __len__, __add__)"
        ],
        "learning_objectives_hi": [
            "Inheritance seekho (Parent se Child class me traits aana)",
            "Method overriding aur super() ka power",
            "Encapsulation: public, _protected, aur __private (name mangling)",
            "Polymorphism (alag objects, same method call)",
            "Special Dunder methods (__str__, __len__, __add__) master karna"
        ],
        "recap_en": "You mastered the four pillars of OOP: inheritance hierarchy, method overriding with super(), encapsulation levels, polymorphism, and operator overloading via dunders.",
        "recap_hi": "Aapne OOP ke 4 pillars: Inheritance, Encapsulation, Polymorphism, super() aur Dunder methods master kiye.",
        "subtopics": [
            {
                "id": "ch18_sub1_inheritance",
                "title": "Inheritance: Passing traits from a Parent class to a Child class",
                "title_hi": "Inheritance: Parent class se Child class me traits aana",
                "icon": "🧬",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Inheritance allows a Child class to inherit all attributes and methods from a Parent class automatically. You write the shared base logic once in the Parent, and specialize it in the Child: class Child(Parent):.",
                "what_is_it_hi": "Inheritance ka matlab hota hai Child class ka apne Parent class ki saari khasiyatein aur methods automatically pa lena. Shared logic Parent me ek baar likho, aur Child class me use bina dobara likhe use karo: class Child(Parent):.",
                "why_need_it_en": "DRY (Don't Repeat Yourself) architecture: If Student, Teacher, and Staff all have name, email, and login(), put them in a Person base class instead of rewriting 3 times!",
                "why_need_it_hi": "Student, Teacher aur Admin sabke paas name aur login() hota hai. Teen baar likhne ke badle ek Person class banao aur sabko usse inherit karwa lo.",
                "how_to_use_en": "class Child(Parent): pass.",
                "how_to_use_hi": "class Dog(Animal): pass.",
                "syntax": "class Animal:\n    def breathe(self):\n        return \"Breathing oxygen...\"\n\n# Dog inherits everything from Animal:\nclass Dog(Animal):\n    def bark(self):\n        return \"Woof!\"",
                "rules_en": [
                    "Put the Parent class inside parentheses after the Child class name: class Child(Parent):.",
                    "Child objects have access to all Parent methods automatically.",
                    "Python supports Multiple Inheritance: class Child(ParentA, ParentB):."
                ],
                "rules_hi": [
                    "Child class ke naam ke baad brackets me Parent class likhi jaati hai: class Dog(Animal):.",
                    "Child object Parent ke saare methods chala sakta hai.",
                    "Python me ek child ke do parents bhi ho sakte hain (Multiple Inheritance)."
                ],
                "analogy_en": "Genetics: You inherit eye color, blood type, and height potential from your biological parents, but you develop your own unique skills (like coding!).",
                "analogy_hi": "DNA aur Genetics jaisa: Mata-pita se aankhon ka rang aur height milti hai (Inheritance), aur aap apni alag skills seekhte ho (Child methods).",
                "common_mistakes": [
                    {
                        "mistake": "Calling Parent methods on a Parent instance expecting Child methods to exist.",
                        "why_it_fails_en": "Inheritance is strictly ONE-WAY (downwards). Parents do not inherit from Children!",
                        "why_it_fails_hi": "Parent child se inherit nahi karta, sirf child parent se inherit karta hai.",
                        "fix": "Remember: Child inherits from Parent, never the reverse."
                    }
                ],
                "example_1": {
                    "title": "Single Inheritance in Action",
                    "title_hi": "Single inheritance ka live use",
                    "code": "class Vehicle:\n    def start_engine(self):\n        return 'Engine started.'\n\nclass ElectricCar(Vehicle):\n    def charge_battery(self):\n        return 'Battery charging...'\n\ntesla = ElectricCar()\nprint('Inherited:', tesla.start_engine())\nprint('Child method:', tesla.charge_battery())",
                    "expected_output": "Inherited: Engine started.\nChild method: Battery charging...",
                    "explanation_en": "ElectricCar can call start_engine() because it inherited it from Vehicle.",
                    "explanation_hi": "ElectricCar Vehicle se start_engine inherit karke call karta hai."
                },
                "example_2": {
                    "title": "isinstance and issubclass Verification",
                    "title_hi": "issubclass se hierarchy check",
                    "code": "class Animal:\n    pass\nclass Cat(Animal):\n    pass\n\nprint('Is Cat a subclass of Animal?', issubclass(Cat, Animal))\nmy_cat = Cat()\nprint('Is my_cat an Animal?', isinstance(my_cat, Animal))",
                    "expected_output": "Is Cat a subclass of Animal? True\nIs my_cat an Animal? True",
                    "explanation_en": "Both issubclass and isinstance recognize inheritance hierarchies.",
                    "explanation_hi": "issubclass aur isinstance inheritance hierarchy ko verify karte hain."
                },
                "challenge": {
                    "prompt_en": "Create class Person with greet(self) returning 'Hello'. Create class Student(Person). Instantiate s = Student() and print: s.greet()",
                    "prompt_hi": "class Person me greet(self) banao jo 'Hello' return kare. class Student(Person) banao. s = Student() karke s.greet() print karo.",
                    "starter_code": "# Create Person and Student(Person):\n",
                    "expected_output": "Hello",
                    "solution_code": "class Person:\n    def greet(self):\n        return 'Hello'\n\nclass Student(Person):\n    pass\n\ns = Student()\nprint(s.greet())",
                    "solution_explanation_en": "Student inherits greet() from Person.",
                    "solution_explanation_hi": "Student ne Person se greet() inherit kiya.",
                    "hints": ["class Student(Person): pass"],
                    "ego_roast_hi": "class Student(Person) likhna bhool gaye?",
                    "ego_cheer_hi": "Inheritance hierarchy mastered! 🧬"
                }
            },
            {
                "id": "ch18_sub2_super_and_overriding",
                "title": "Overriding methods and using super()",
                "title_hi": "Methods override karna aur super() ka use",
                "icon": "⚡",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "METHOD OVERRIDING lets a child class rewrite a parent's method with its own custom implementation. super() calls the PARENT's original method from inside the child so you can extend it rather than completely replacing it.",
                "what_is_it_hi": "METHOD OVERRIDING ka matlab hota hai Child class me Parent ke purane method ko naye tareeqe se re-write kar dena. super() se aap Parent ke original method ko call karke use aage extend kar sakte ho bina code duplicate kiye.",
                "why_need_it_en": "When a Child needs to initialize new attributes: Student.__init__ needs to initialize student-specific 'gpa', but still wants Person.__init__ to initialize 'name' and 'email'. super().__init__() does this cleanly!",
                "why_need_it_hi": "Child class me naya variable jodna ho to super().__init__() se pehle Parent ka constructor chalao, fir child ka naya variable set karo.",
                "how_to_use_en": "super().__init__(name); super().parent_method().",
                "how_to_use_hi": "super().__init__(args) use karo.",
                "syntax": "class Parent:\n    def __init__(self, name):\n        self.name = name\n\nclass Child(Parent):\n    def __init__(self, name, age):\n        super().__init__(name)  # Reuse parent constructor!\n        self.age = age",
                "rules_en": [
                    "Overriding: define a method in Child with the EXACT SAME NAME as in Parent.",
                    "super() returns a temporary proxy object of the superclass.",
                    "In Python 3, write simply super() without arguments (Python 2 required super(Child, self))."
                ],
                "rules_hi": [
                    "Overriding ke liye Child me exact same naam ka method dobara define karo.",
                    "super() se Parent class ka original method run hota hai.",
                    "Python 3 me seedhe super().method() likhte hain."
                ],
                "analogy_en": "Inheriting a family recipe: Your grandmother made vanilla cake. You inherit the recipe, call super() to bake the original vanilla sponge, but override the top with chocolate frosting.",
                "analogy_hi": "Khandani recipe jaisi: Dadi ma ki cake recipe me base wahi banaya (super()), lekin upar naya chocolate frosting laga diya (overriding).",
                "common_mistakes": [
                    {
                        "mistake": "Overriding __init__ in Child but forgetting super().__init__().",
                        "why_it_fails_en": "Parent attributes are NEVER initialized, causing AttributeError when accessing parent fields!",
                        "why_it_fails_hi": "Parent ke variables initialize hi nahi hote to baad me AttributeError aa jata hai.",
                        "fix": "Always call super().__init__(...) inside the child's constructor."
                    }
                ],
                "example_1": {
                    "title": "super().__init__ in Child Constructor",
                    "title_hi": "super().__init__ se Parent fields reuse karna",
                    "code": "class Employee:\n    def __init__(self, name, salary):\n        self.name = name\n        self.salary = salary\n\nclass Manager(Employee):\n    def __init__(self, name, salary, department):\n        super().__init__(name, salary)  # Initialize base fields\n        self.department = department\n\nm = Manager('Pooja', 90000, 'Engineering')\nprint(f'{m.name} manages {m.department} (${m.salary})')",
                    "expected_output": "Pooja manages Engineering ($90000)",
                    "explanation_en": "Manager reuses Employee's name and salary initialization via super().",
                    "explanation_hi": "Manager ne super() se name aur salary set ki aur department khud set kiya."
                },
                "example_2": {
                    "title": "Method Overriding with Extension",
                    "title_hi": "Method override karke extend karna",
                    "code": "class BasicUser:\n    def access_level(self):\n        return 'Read-Only'\n\nclass AdminUser(BasicUser):\n    def access_level(self):\n        return 'Full Read-Write Admin'  # Overridden!\n\nprint('Admin access:', AdminUser().access_level())",
                    "expected_output": "Admin access: Full Read-Write Admin",
                    "explanation_en": "AdminUser overrides access_level() with its own specialized permissions.",
                    "explanation_hi": "AdminUser ne purane access_level ko override karke naya result diya."
                },
                "challenge": {
                    "prompt_en": "Create Parent with intro() returning 'Base'. Create Child(Parent) that overrides intro() to return 'Overridden'. Print Child().intro().",
                    "prompt_hi": "Parent me intro() 'Base' return kare. Child(Parent) me intro() override karke 'Overridden' return kare aur print karo.",
                    "starter_code": "# Implement method overriding:\n",
                    "expected_output": "Overridden",
                    "solution_code": "class Parent:\n    def intro(self):\n        return 'Base'\n\nclass Child(Parent):\n    def intro(self):\n        return 'Overridden'\n\nprint(Child().intro())",
                    "solution_explanation_en": "Child overrides intro() method cleanly.",
                    "solution_explanation_hi": "Child class intro() method ko override karta hai.",
                    "hints": ["class Child(Parent):\\n    def intro(self): return 'Overridden'"],
                    "ego_roast_hi": "Method override karna nahi aaya?",
                    "ego_cheer_hi": "Method overriding and super() verified! ⚡"
                }
            },
            {
                "id": "ch18_sub3_encapsulation",
                "title": "Encapsulation: Hiding data (Public, Protected, and Private attributes)",
                "title_hi": "Encapsulation: Data ko chhipana (Public, Protected, Private)",
                "icon": "🔒",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Encapsulation is bundling data and methods together while restricting direct access to internal components. Python uses naming conventions: PUBLIC (self.name), PROTECTED (self._name with 1 underscore — internal convention), and PRIVATE (self.__name with 2 underscores — triggers Name Mangling).",
                "what_is_it_hi": "Encapsulation ka matlab data ko secure rakhna aur bahar se direct chhed-chhad se bachana. Python me 3 levels hote hain: PUBLIC (self.name - sabke liye khula), PROTECTED (self._name ek underscore - internal convention), aur PRIVATE (self.__name do underscores - Name Mangling se hide ho jata hai).",
                "why_need_it_en": "Security and stability: A bank account balance (account.__balance) should only be changed via deposit() and withdraw() methods with validation, never directly overwritten from outside!",
                "why_need_it_hi": "Bank balance ko bahar se koi account.balance = 99999999 na kar sake! Balance ko private rakh kar deposit() method se hi change allow karte hain.",
                "how_to_use_en": "self.__pin = 1234. Use getter methods (get_balance()) to inspect safely.",
                "how_to_use_hi": "self.__private_var. Getters aur setters se access do.",
                "syntax": "class Account:\n    def __init__(self, balance):\n        self.public_id = 101       # Public (anybody can access)\n        self._branch = \"Delhi\"     # Protected (internal convention)\n        self.__balance = balance   # Private (Name mangled!)\n\n    def get_balance(self):         # Getter method\n        return self.__balance",
                "rules_en": [
                    "Public (no underscore): accessible anywhere (obj.name).",
                    "Protected (_single_underscore): convention indicating 'internal use only' — linters warn, but Python does not physically block access.",
                    "Private (__double_underscore): Python applies Name Mangling, renaming it internally to _ClassName__private to prevent accidental subclass overrides.",
                    "Python has no true hard private memory: access mangled via obj._ClassName__private."
                ],
                "rules_hi": [
                    "Public: Sabke liye khula hai.",
                    "Protected (_var): Coders ke beech ka agreement hai ki bahar se chhedo mat.",
                    "Private (__var): Python iska naam badal kar _ClassName__var kar deta hai (Name Mangling).",
                    "Python me 'We are all consenting adults here' philosophy hai — strict private memory hardware level par nahi hoti."
                ],
                "analogy_en": "A car dashboard: The speedometer and steering wheel are PUBLIC (driver interacts directly). The engine oil dipstick under the hood is PROTECTED (mechanic checks). The transmission ECU gearbox software is PRIVATE (sealed from tampering).",
                "analogy_hi": "Gaadi ke controls: Steering aur Horn PUBLIC hain (koi bhi use kare). Engine oil ka dabba PROTECTED hai (mechanic khole). Engine ke andar ki chip PRIVATE hai (locked).",
                "common_mistakes": [
                    {
                        "mistake": "Trying to read a private attribute directly: obj.__balance",
                        "why_it_fails_en": "AttributeError: 'Account' object has no attribute '__balance' (due to name mangling).",
                        "why_it_fails_hi": "Name mangling ki wajah se Python ko __balance nahi milta.",
                        "fix": "Use a public getter method: obj.get_balance()."
                    }
                ],
                "example_1": {
                    "title": "Private Attribute and Name Mangling Proof",
                    "title_hi": "Private attribute aur Name Mangling ka saboot",
                    "code": "class SecretVault:\n    def __init__(self, code):\n        self.__secret_code = code\n\n    def reveal(self):\n        return self.__secret_code\n\nv = SecretVault(9988)\nprint('Safe access via getter:', v.reveal())\n# Mangled name exists internally\nprint('Mangled name access:', v._SecretVault__secret_code)",
                    "expected_output": "Safe access via getter: 9988\nMangled name access: 9988",
                    "explanation_en": "Shows how Python mangles __secret_code to _SecretVault__secret_code.",
                    "explanation_hi": "Dikhata hai ki __secret_code ka naam badal kar _SecretVault__secret_code ho jata hai."
                },
                "example_2": {
                    "title": "Encapsulated Bank Account with Validation",
                    "title_hi": "Encapsulated bank deposit validation",
                    "code": "class Bank:\n    def __init__(self, bal):\n        self.__bal = bal\n    def deposit(self, amt):\n        if amt > 0:\n            self.__bal += amt\n    def get_bal(self):\n        return self.__bal\n\nb = Bank(100)\nb.deposit(50)\nprint('Validated Balance:', b.get_bal())",
                    "expected_output": "Validated Balance: 150",
                    "explanation_en": "Balance cannot be set to invalid negative numbers because it is encapsulated behind deposit().",
                    "explanation_hi": "Encapsulation ki wajah se balance galat tarike se modify nahi ho sakta."
                },
                "challenge": {
                    "prompt_en": "Create class Safe with private attribute self.__pin = 4455 and getter get_pin(self). Print: PIN: 4455",
                    "prompt_hi": "class Safe banao jisme __pin = 4455 aur get_pin(self) method ho. PIN print karo: PIN: 4455",
                    "starter_code": "# Create Safe with private pin:\n",
                    "expected_output": "PIN: 4455",
                    "solution_code": "class Safe:\n    def __init__(self, pin):\n        self.__pin = pin\n    def get_pin(self):\n        return self.__pin\n\ns = Safe(4455)\nprint(f'PIN: {s.get_pin()}')",
                    "solution_explanation_en": "Encapsulates __pin and accesses via getter method.",
                    "solution_explanation_hi": "Private __pin ko getter method se read karta hai.",
                    "hints": ["self.__pin = pin\\ndef get_pin(self): return self.__pin"],
                    "ego_roast_hi": "Double underscore private variable lagana bhool gaye?",
                    "ego_cheer_hi": "Encapsulation security verified! 🔒"
                }
            },
            {
                "id": "ch18_sub4_polymorphism",
                "title": "Polymorphism: Using the same method name for different objects",
                "title_hi": "Polymorphism: Alag objects ke liye same method name",
                "icon": "🎭",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Polymorphism (Greek for 'many forms') allows different classes to implement methods with the EXACT SAME NAME. A caller can loop over diverse objects and invoke that same method without caring which specific class each object belongs to (Duck Typing: 'If it quacks like a duck, it is a duck').",
                "what_is_it_hi": "Polymorphism ka matlab hota hai 'ek cheez ke alag-alag roop'. Alag-alag classes ke paas same naam ka method hota hai (jaise Dog.speak(), Cat.speak(), Cow.speak()). Aap sab par ek loop chala kar .speak() call kar sakte ho bina unke specific type ki chinta kiye.",
                "why_need_it_en": "In a graphics program, shapes = [Circle(), Rectangle(), Triangle()]. To draw them all, you just loop: for s in shapes: s.draw(). Zero complex if-else checks needed!",
                "why_need_it_hi": "Graphics app me agar 50 shapes hain to if/else lagane ke badle seedhe loop chalao: for s in shapes: s.draw(). Har shape apna draw method khud handle karegi.",
                "how_to_use_en": "Define common method name across distinct classes; iterate over them polymorphically.",
                "how_to_use_hi": "Dono classes me same method naam rakho.",
                "syntax": "class Dog:\n    def speak(self): return \"Woof!\"\n\nclass Cat:\n    def speak(self): return \"Meow!\"\n\n# Polymorphic loop:\nfor animal in [Dog(), Cat()]:\n    print(animal.speak())",
                "rules_en": [
                    "Duck Typing in Python: Code cares about an object's BEHAVIOR (methods), not its explicit inheritance hierarchy.",
                    "Built-in polymorphism: len('hello') works on strings, lists, dicts, and tuples because all implement __len__().",
                    "Eliminates giant fragile if/elif chains checking object types."
                ],
                "rules_hi": [
                    "Python me Duck Typing chalti hai: agar object ke paas wo method hai to chal jayega.",
                    "Python ka len() function Polymorphism ka example hai — string, list, dict sab par chalta hai.",
                    "Bina if-else ke clean scalable code banta hai."
                ],
                "analogy_en": "The 'Play' button on a remote: pressing 'Play' plays a movie on Netflix, a song on Spotify, or a podcast on YouTube. The button is the same; the action depends on the app.",
                "analogy_hi": "Remote ka 'Power' button jaisa: TV par dabaoge to TV band hogi, AC par dabaoge to AC band hoga. Button same hai, kaam alag-alag.",
                "common_mistakes": [
                    {
                        "mistake": "Writing manual type-checking loops: if isinstance(obj, Dog): obj.bark() elif isinstance(obj, Cat): obj.meow()",
                        "why_it_fails_en": "Defeats the entire purpose of OOP! Adding a new animal requires modifying the if-else loop.",
                        "why_it_fails_hi": "Har jagah if isinstance lagane se polymorphism ka fayda khatam ho jata hai.",
                        "fix": "Give both classes a unified method name like .speak() and call obj.speak()."
                    }
                ],
                "example_1": {
                    "title": "Polymorphic Payment Gateways",
                    "title_hi": "Payment gateways ka polymorphic design",
                    "code": "class CreditCard:\n    def pay(self, amount):\n        return f'Paid ${amount} via Card'\n\nclass UPI:\n    def pay(self, amount):\n        return f'Paid ${amount} via UPI'\n\n# Universal checkout processor\nfor payment_method in [CreditCard(), UPI()]:\n    print(payment_method.pay(500))",
                    "expected_output": "Paid $500 via Card\nPaid $500 via UPI",
                    "explanation_en": "Both classes implement .pay(amount), allowing universal polymorphic iteration.",
                    "explanation_hi": "Dono classes me .pay() method hai to loop dono ko bina if-else ke chala deta hai."
                },
                "example_2": {
                    "title": "Built-in Polymorphism with len()",
                    "title_hi": "Built-in polymorphism (len function)",
                    "code": "items = ['abc', [1, 2, 3], {'a': 1, 'b': 2}]\nfor item in items:\n    print(f'Length of {type(item).__name__}: {len(item)}')",
                    "expected_output": "Length of str: 3\nLength of list: 3\nLength of dict: 2",
                    "explanation_en": "len() polymorphically queries the __len__() method of strings, lists, and dicts.",
                    "explanation_hi": "len() function har data structure ke __len__ method ko polymorphically call karta hai."
                },
                "challenge": {
                    "prompt_en": "Create class A with sound() returning 'Beep', and class B with sound() returning 'Boop'. Loop over [A(), B()] and print each sound.",
                    "prompt_hi": "class A me sound() 'Beep' aur class B me sound() 'Boop' banao. Loop chala kar dono ka sound print karo.",
                    "starter_code": "# Define A and B with sound() and loop:\n",
                    "expected_output": "Beep\nBoop",
                    "solution_code": "class A:\n    def sound(self):\n        return 'Beep'\nclass B:\n    def sound(self):\n        return 'Boop'\n\nfor obj in [A(), B()]:\n    print(obj.sound())",
                    "solution_explanation_en": "Invokes .sound() polymorphically on both instances.",
                    "solution_explanation_hi": "Polymorphic loop dono ke sound methods ko call karta hai.",
                    "hints": ["for obj in [A(), B()]: print(obj.sound())"],
                    "ego_roast_hi": "Polymorphic loop likhna bhool gaye?",
                    "ego_cheer_hi": "Polymorphic design pattern validated! 🎭"
                }
            },
            {
                "id": "ch18_sub5_dunder_methods",
                "title": "Special \"Dunder\" (Double Underscore) methods (__str__, __len__, __add__)",
                "title_hi": "Special \"Dunder\" Methods (__str__, __len__, __add__)",
                "icon": "✨",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "Dunder methods (Magic methods) begin and end with double underscores (like __str__, __len__, __add__). They allow your custom classes to integrate seamlessly with Python's built-in operators: print(obj) triggers __str__, len(obj) triggers __len__, and obj1 + obj2 triggers __add__!",
                "what_is_it_hi": "Dunder methods (Double Underscore methods) Python ke magic methods hote hain jaise __str__, __len__, __add__. Ye aapki classes ko Python ke operators se jodte hain: print(obj) karne par __str__ chalta hai, len(obj) par __len__ chalta hai, aur obj1 + obj2 karne par __add__ chalta hai!",
                "why_need_it_en": "Operator Overloading: Without __str__, printing an object outputs ugly garbage like <__main__.Book object at 0x103a>. With __str__, it prints beautifully: 'Python 101 by Elysia'.",
                "why_need_it_hi": "Bina __str__ ke object print karne par ajeeb sa memory address dikhta hai (<__main__.User at 0x...>). __str__ lagane se saaf sundar text print hota hai.",
                "how_to_use_en": "def __str__(self): return f'Book({self.title})'.",
                "how_to_use_hi": "def __str__(self): return f'{self.name}'.",
                "syntax": "class Book:\n    def __init__(self, title, pages):\n        self.title = title\n        self.pages = pages\n\n    def __str__(self):  # Called by print(b) and str(b)\n        return f\"'{self.title}' ({self.pages} pages)\"\n\n    def __len__(self):  # Called by len(b)\n        return self.pages",
                "rules_en": [
                    "__str__() MUST return a string (for human end-users).",
                    "__repr__() should return an unambiguous representation (ideal for debugging).",
                    "__len__() MUST return a non-negative integer.",
                    "__add__(self, other) intercepts the '+' operator for custom math."
                ],
                "rules_hi": [
                    "__str__() ko HAMESHA string return karni hoti hai.",
                    "__len__() ko HAMESHA non-negative integer return karna hota hai.",
                    "__add__(self, other) se aap '+' operator ko apne tareeqe se define kar sakte ho.",
                    "Python ke sabhi built-in functions ke peeche yahi dunder methods hote hain."
                ],
                "analogy_en": "Universal adapters for power sockets: Dunder methods are standard universal prongs that allow your custom appliances to plug directly into Python's native wall power.",
                "analogy_hi": "Universal charging adapter jaisa — dunder method lagate hi aapka custom object Python ke built-in features (print, len, +) me fit ho jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Returning an integer from __str__: def __str__(self): return self.id",
                        "why_it_fails_en": "TypeError: __str__ returned non-string (type int).",
                        "why_it_fails_hi": "__str__ sirf string return kar sakta hai, number nahi.",
                        "fix": "Always return string: return str(self.id)."
                    }
                ],
                "example_1": {
                    "title": "Beautiful String Formatting with __str__",
                    "title_hi": "__str__ se clean print output",
                    "code": "class Book:\n    def __init__(self, title, pages):\n        self.title = title\n        self.pages = pages\n    def __str__(self):\n        return f'{self.title} ({self.pages}pp)'\n    def __len__(self):\n        return self.pages\n\nb = Book('Elysia Python', 350)\nprint('Printed object:', b)\nprint('len() result:', len(b))",
                    "expected_output": "Printed object: Elysia Python (350pp)\nlen() result: 350",
                    "explanation_en": "print(b) automatically triggers __str__; len(b) automatically triggers __len__.",
                    "explanation_hi": "print(b) karne par __str__ chala aur len(b) karne par __len__ chala."
                },
                "example_2": {
                    "title": "Operator Overloading with __add__",
                    "title_hi": "+ operator overload karna (__add__)",
                    "code": "class Point:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __add__(self, other):\n        return Point(self.x + other.x, self.y + other.y)\n    def __str__(self):\n        return f'({self.x}, {self.y})'\n\np1 = Point(1, 2)\np2 = Point(3, 4)\nprint('Point addition (p1 + p2):', p1 + p2)",
                    "expected_output": "Point addition (p1 + p2): (4, 6)",
                    "explanation_en": "p1 + p2 triggers __add__, summing coordinates and returning a new Point.",
                    "explanation_hi": "p1 + p2 ne coordinates ko jodkar naya Point return kiya."
                },
                "challenge": {
                    "prompt_en": "Create class Box with __init__(self, size) and __len__(self) returning size. For b = Box(42), print: len: 42",
                    "prompt_hi": "class Box me __init__(self, size) aur __len__(self) return size banao. b = Box(42) ka len print karo: len: 42",
                    "starter_code": "# Define Box with __len__:\n",
                    "expected_output": "len: 42",
                    "solution_code": "class Box:\n    def __init__(self, size):\n        self.size = size\n    def __len__(self):\n        return self.size\n\nb = Box(42)\nprint(f'len: {len(b)}')",
                    "solution_explanation_en": "len(b) invokes __len__ to return size.",
                    "solution_explanation_hi": "len(b) se __len__ chalta hai aur size return hota hai.",
                    "hints": ["def __len__(self): return self.size"],
                    "ego_roast_hi": "__len__ dunder method bhool gaye?",
                    "ego_cheer_hi": "PART 5 REAL WORLD OOP & FILES CONQUERED! 🏆 Python Software Engineer!"
                }
            }
        ]
    }
]
