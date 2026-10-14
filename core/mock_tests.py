"""
Elysia Code: College Lab Exam & Viva Simulator
Simulates standard university practical lab evaluations (e.g. CA1/CA2/End-Term):
- Section A: Output Prediction (MCQ)
- Section B: Doctor Mode (Code Debugging / Syntax Hunt)
- Section C: Coding Practical
- Section D: Oral Viva Simulator with Model Answers
"""

from typing import Dict, Any, List

MOCK_EXAMS: Dict[str, Dict[str, Any]] = {
    "python_ca1": {
        "id": "py_ca1",
        "title": "Python Lab Practical Evaluation (CA1 / Mid-Term)",
        "duration_minutes": 25,
        "total_marks": 30,
        "instructions_en": "Complete all sections within 25 minutes. No external copy-pasting allowed. You will face a rapid oral viva in Section D.",
        "instructions_hi": "25 minute me saare sections solve karo. Cheating allowed nahi hai. Section D me oral viva test hoga.",
        "section_a_mcq": [
            {
                "id": "mcq_1",
                "marks": 2,
                "question_en": "What will be the exact output of this code snippet?",
                "question_hi": "Is code snippet ka exact output kya hoga?",
                "code": "a = [1, 2, 3]\nb = a\nb.append(4)\nprint(len(a))",
                "options": ["3", "4", "Error: b is not defined", "None"],
                "correct_index": 1,
                "explanation_en": "Lists in Python are mutable reference objects. 'b = a' does not create a copy; both variables point to the same list in memory.",
                "explanation_hi": "Python me `b = a` naya dabba nahi banata, balki usi dabbe ka doosra naam ban jata hai. Isliye jab b me 4 joda, to a me bhi jud gaya aur length 4 ho gayi."
            },
            {
                "id": "mcq_2",
                "marks": 2,
                "question_en": "What does the expression `bool('False')` evaluate to?",
                "question_hi": "Expression `bool('False')` ka result kya hoga?",
                "code": "result = bool('False')\nprint(result)",
                "options": ["False", "True", "SyntaxError", "0"],
                "correct_index": 1,
                "explanation_en": "Any non-empty string in Python evaluates to True in a boolean context, regardless of the text inside.",
                "explanation_hi": "Python me koi bhi string jisme kuch bhi likha ho (chahe 'False' hi kyu na ho) True hoti hai. Khali string `''` hi False hoti hai."
            }
        ],
        "section_b_debug": [
            {
                "id": "debug_1",
                "title": "Doctor Mode: Fix the Broken Even Counter",
                "marks": 6,
                "desc_en": "This code is supposed to count even numbers between 1 and 10 and print 'Even count: 5'. It currently crashes or gives the wrong output. Find and fix the 2 bugs!",
                "desc_hi": "Ye code 1 se 10 ke beech even numbers count karne ke liye tha taaki 'Even count: 5' aaye. Isme 2 bugs hain. Fix karo!",
                "broken_code": "count = 0\nfor i in range(1, 10)\n    if i % 2 = 0:\n        count = count + 1\nprint('Even count: ' + count)",
                "expected_output": "Even count: 5",
                "solution_code": "count = 0\nfor i in range(1, 11):\n    if i % 2 == 0:\n        count = count + 1\nprint(f'Even count: {count}')",
                "bugs_breakdown": [
                    "Missing colon on line 2 (for i in range(1, 11):)",
                    "Using '=' instead of '==' on line 3",
                    "String concatenation with int on line 5 without converting to str or using f-string"
                ]
            }
        ],
        "section_c_coding": [
            {
                "id": "coding_1",
                "title": "Hostel Canteen Discount Calculator",
                "marks": 10,
                "desc_en": "Write a program that takes bill = 450. If bill >= 500, apply a 20% discount. If bill >= 300, apply a 10% discount. Otherwise no discount. Compute and print: 'Final Bill: X'",
                "desc_hi": "Ek program likho jisme bill = 450 hai. Agar bill >= 500 hai to 20% discount, >= 300 par 10% discount, warna 0% discount. Print karo: 'Final Bill: X'",
                "starter_code": "bill = 450\n# Calculate final_bill and print:\n",
                "solution_code": "bill = 450\nif bill >= 500:\n    discount = bill * 0.20\nelif bill >= 300:\n    discount = bill * 0.10\nelse:\n    discount = 0\nfinal_bill = bill - discount\nprint(f'Final Bill: {final_bill}')",
                "expected_output": "Final Bill: 405.0"
            }
        ],
        "section_d_viva": [
            {
                "id": "viva_1",
                "marks": 10,
                "question": "Explain the difference between deep copy and shallow copy in Python.",
                "answer_en": "A shallow copy creates a new collection object, but inserts references into it to the objects found in the original. A deep copy recursively duplicates every object found in the original, creating completely independent copies.",
                "answer_hi": "Shallow copy sirf bahar ka dabba naya banata hai par andar ke saman ka reference purana rehta hai. Deep copy andar tak sab kuch naya copy karta hai taaki ek ko change karne se doosre par koi asar na ho."
            },
            {
                "id": "viva_2",
                "marks": 10,
                "question": "What is the Time Complexity of searching an item in a Python list vs a set?",
                "answer_en": "Searching in a list is O(n) because it checks elements sequentially. Searching in a set is O(1) average time complexity because it uses hashing.",
                "answer_hi": "List me item dhoondhne me O(n) time lagta hai kyunki line se har element check karna padta hai. Set me hash table use hota hai, isliye O(1) me turant mil jata hai."
            }
        ]
    },
    "html_ca1": {
        "id": "html_ca1",
        "title": "Web Foundations & HTML5 Lab Practical",
        "duration_minutes": 20,
        "total_marks": 25,
        "instructions_en": "Build standards-compliant HTML structures with zero semantic errors.",
        "instructions_hi": "Standard HTML code likho bina kisi semantic ya tag closing error ke.",
        "section_a_mcq": [
            {
                "id": "html_mcq_1",
                "marks": 2,
                "question_en": "Which tag should be used for the most important navigation links on a website?",
                "question_hi": "Website ke main navigation links ke liye kaunsa semantic tag use karna chahiye?",
                "code": "<!-- Choose the best semantic tag -->",
                "options": ["<div class='nav'>", "<navigation>", "<nav>", "<links>"],
                "correct_index": 2,
                "explanation_en": "<nav> is the standard semantic HTML5 element dedicated for primary navigation blocks.",
                "explanation_hi": "<nav> HTML5 ka official semantic tag hai jo browser aur search engine ko batata hai ki ye menu links hain."
            }
        ],
        "section_b_debug": [
            {
                "id": "html_debug_1",
                "title": "Doctor Mode: Fix the Broken Table Markup",
                "marks": 8,
                "desc_en": "Fix this malformed HTML table so that it properly uses <table>, <thead>, <tbody>, <tr>, and <th>.",
                "desc_hi": "Is tooti hui HTML table ko theek karo standard tags use karke.",
                "broken_code": "<table>\n  <tr>\n    <td>Name</td>\n    <td>Roll No</td>\n  </tr>\n  <tr>\n    <td>Aman</td>\n    <td>101</td>\n  </tr>\n</table>",
                "expected_output": "Proper semantic headers",
                "solution_code": "<table>\n  <thead>\n    <tr>\n      <th>Name</th>\n      <th>Roll No</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <td>Aman</td>\n      <td>101</td>\n    </tr>\n  </tbody>\n</table>"
            }
        ],
        "section_c_coding": [
            {
                "id": "html_coding_1",
                "title": "Student Feedback Form",
                "marks": 15,
                "desc_en": "Create a feedback form containing: 1 text input for Name, 1 textarea for Comments, and a Submit button.",
                "desc_hi": "Ek student feedback form banao jisme Name input, Comments textarea, aur Submit button ho.",
                "starter_code": "<form>\n  <!-- Add input, textarea, button here -->\n</form>",
                "solution_code": "<form>\n  <input type=\"text\" name=\"name\" placeholder=\"Your Name\" required>\n  <textarea name=\"comments\" placeholder=\"Your feedback\"></textarea>\n  <button type=\"submit\">Submit Feedback</button>\n</form>"
            }
        ],
        "section_d_viva": [
            {
                "id": "html_viva_1",
                "marks": 10,
                "question": "What is the Box Model in web styling?",
                "answer_en": "The CSS Box Model is a container that wraps around every HTML element: Content, Padding, Border, and Margin.",
                "answer_hi": "Box model web design ka basic rule hai: har element ke 4 hisse hote hain — Content (text/image), Padding (andar ka space), Border (boundary), aur Margin (bahar ka space)."
            }
        ]
    }
}

def get_mock_exam(exam_id: str = "py_ca1") -> Dict[str, Any]:
    return MOCK_EXAMS.get(exam_id, MOCK_EXAMS["python_ca1"])
