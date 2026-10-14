"""
=============================================================================
✨ ELYSIA CODE: SOCRATIC SENIOR AI MENTOR (socratic_ai.py)
=============================================================================
📌 KYA KAAM HAI IS FILE KA (WHAT IT DOES):
  Jab Python code run karne par koi error (jaise TypeError, IndexError, SyntaxError, 
  ZeroDivisionError, NameError) aata hai, to ye script us raw traceback ko pakadti hai 
  aur student ko hostel ke kisi smart "Senior Bhaiya/Didi" ke style me relatable, 
  humorous Hinglish advice deti hai bina direct solution spoon-feed kiye.

👁️ WEB PAGE PE KYA DIKHTA HAI:
  Screen par ek glowing golden toast bubble ("Senior Bhaiya Hint") pop up hota hai 
  jo practical analogies (jaise samosa-chai, cricket bat, etc.) se galti samjhata hai.

💡 KYUN USE KIYA (WHY WE USE THIS):
  Freshers aksar lambe-chaude red color ke Python Tracebacks dekh kar panic ho jaate hain.
  Socratic method student se sawal poochkar aur clue dekar use khud se debug karna sikhata hai.
  Zero-dependency Python `re` (Regular Expressions) use karke bina OpenAI/GPT API ke
  100% free aur 0-millisecond instant error matching ho jaati hai!

⚠️ AGAR ISKO CHANGE YA DELETE KAREIN TO:
  Error decode hona band ho jayega aur student ko sirf cryptic English traceback dikhega.
=============================================================================
"""

import os
import re
from typing import Dict, Any

ERROR_PATTERNS = [
    {
        "pattern": r"TypeError: can only concatenate str \(not \"int\"\) to str",
        "title": "Type Mismatch / Samosa + Chai Error",
        "senior_en": "You are trying to glue a number directly onto a piece of text without converting it first. Use an f-string `f'{val}'` or wrap the number with `str(num)`.",
        "senior_hi": "Bhai tu number aur text ko fevicol se chipkane ki koshish kar raha hai! Chai me samosa duba ke khayega to toot jayega na? Number ko pehle `str()` bana ya f-string use kar: `f'{num}'`."
    },
    {
        "pattern": r"IndexError: list index out of range",
        "title": "Empty Plate / Out of Bounds Error",
        "senior_en": "You asked for an element at an index that doesn't exist. Remember: lists start at index 0, and the last item is at index len(arr) - 1.",
        "senior_hi": "Plate me sirf 3 samose the (index 0, 1, 2) aur tu maang raha hai 5va samosa! Hamesha yaad rakh Python me counting 0 se shuru hoti hai."
    },
    {
        "pattern": r"SyntaxError: invalid syntax",
        "title": "Missing Colon ':' or '=' vs '==' Trap",
        "senior_en": "Check your `if`, `for`, `while`, or `def` lines. Did you forget a colon `:` at the very end? Or did you accidentally write `if a = 5` instead of `if a == 5`?",
        "senior_hi": "Dekh bhai, line ke aakhri me colon `:` lagana bhool gaya hai ya `if` ke andar single `=` laga diya hai? Compare karne ke liye double `==` lagta hai!"
    },
    {
        "pattern": r"IndentationError: unexpected indent",
        "title": "The Indentation Alignment Trap",
        "senior_en": "Python is very strict about spacing. A line of code is pushed in further than it should be. Make sure all statements in the same block align evenly (use 4 spaces).",
        "senior_hi": "Line ki alignment hil gayi hai bhai! C/C++ jaisa curly braces nahi hai yahan. Spacing ek barabar rakho (tab ya 4 spaces), aage-peeche mat karo."
    },
    {
        "pattern": r"ZeroDivisionError: division by zero",
        "title": "Black Hole / Division by Zero",
        "senior_en": "You tried to divide a number by 0. In math and computing, dividing by zero creates infinity/undefined. Check your denominator before dividing.",
        "senior_hi": "Zero se divide karne chala hai bhai? Universe fat jayega! Check kar ki denominator kahin 0 to nahi ho raha."
    },
    {
        "pattern": r"NameError: name '(\w+)' is not defined",
        "title": "Ghost Variable Error",
        "senior_en": "Python has no idea who '{var}' is. Check for spelling typos, or make sure you defined it above this line before trying to use it.",
        "senior_hi": "Python pooch raha hai: 'Bhai ye {var} kaun hai?' Ya to tune spelling galat likhi hai, ya use define karne se pehle hi bula liya hai."
    }
]

def decode_error(raw_error: str, language: str = "hi", code: str = "", offline: bool = False) -> Dict[str, Any]:
    """Translates raw traceback or code issues into friendly Socratic senior advice using Groq AI with regex fallback."""
    # 1. Try Groq AI debugger if configured and offline mode is not active
    is_offline = offline or (os.environ.get("ELYSIA_OFFLINE_AI") == "1")
    if not is_offline:
        try:
            from core.ai_tutor import ai_tutor
            if ai_tutor.get_status().get("configured") and raw_error.strip():
                ai_res = ai_tutor.diagnose_error(raw_error, code=code, lang=language)
                if ai_res.get("matched"):
                    return ai_res
        except Exception:
            pass

    # 2. Fallback to instant local regex patterns
    for item in ERROR_PATTERNS:
        match = re.search(item["pattern"], raw_error)
        if match:
            var_name = match.group(1) if match.groups() else ""
            msg_en = item["senior_en"].replace("{var}", var_name)
            msg_hi = item["senior_hi"].replace("{var}", var_name)
            
            return {
                "matched": True,
                "ai_powered": False,
                "title": item["title"],
                "advice": msg_hi if language == "hi" else msg_en,
                "advice_en": msg_en,
                "advice_hi": msg_hi
            }
            
    # Default fallback
    return {
        "matched": False,
        "ai_powered": False,
        "title": "Runtime / Logic Hiccup",
        "advice": "Bhai code me koi dikkat aayi hai. Error message ko dhyan se padh aur line number check kar!" if language == "hi" else "Take a close look at the traceback line number and review your variables.",
        "advice_en": "Take a close look at the traceback line number and review your variables.",
        "advice_hi": "Bhai code me koi dikkat aayi hai. Error message ko dhyan se padh aur line number check kar!"
    }

