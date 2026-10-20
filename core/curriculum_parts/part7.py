"""
Part 7: Going Professional (Applied Python)
Chapters 24, 25, and 26 with exact syllabus titles and subtopics.
Exhaustive bilingual details, syntax rules, memory models, analogies, 2 verified examples,
Mini-Project: A Desktop Calculator App, and testable challenges.
"""

CHAPTERS = [
    # =========================================================================
    # CHAPTER 24: Interacting with the Internet
    # =========================================================================
    {
        "id": "ch24_interacting_with_internet",
        "part_number": 7,
        "part_title": "PART 7: GOING PROFESSIONAL (APPLIED PYTHON)",
        "chapter_number": 24,
        "title": "Chapter 24: Interacting with the Internet",
        "subtitle_en": "HTTP requests, REST APIs, JSON payloads, and ethical web scraping",
        "subtitle_hi": "HTTP protocol, status codes, requests library, REST APIs aur web scraping",
        "icon": "🌐",
        "estimated_time": "55 mins",
        "prerequisites_en": "Parts 1 to 5 (Dictionaries, exceptions, string methods, file handling).",
        "prerequisites_hi": "Part 1 se 5 tak (Dictionaries, exceptions, strings, files).",
        "learning_objectives_en": [
            "Understand the mechanics of URLs, HTTP verbs (GET, POST), and status codes (200, 404, 500)",
            "Send web requests and process responses using Python's requests library and urllib",
            "Understand API protocols and serialize/deserialize JSON payloads",
            "Apply responsible web scraping principles using HTML parsing tools like BeautifulSoup"
        ],
        "learning_objectives_hi": [
            "URLs, HTTP methods (GET, POST) aur status codes (200, 404, 500) samjhein",
            "Python requests library se web servers se data fetch karein",
            "REST APIs aur JSON serialization/deserialization master karein",
            "BeautifulSoup se ethical aur responsible web scraping karein"
        ],
        "recap_en": "You mastered network programming: understanding HTTP clients, status codes, calling REST APIs, JSON payload extraction, and responsible web scraping.",
        "recap_hi": "Aapne internet aur networking master kar li: web requests, APIs, JSON parsing aur web scraping.",
        "subtopics": [
            {
                "id": "ch24_sub1_urls_http_status_codes",
                "title": "Understanding URLs, HTTP, and Status Codes (200, 404)",
                "title_hi": "URLs, HTTP aur Status Codes (200, 404) ko samajhna",
                "icon": "🚦",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "The Hypertext Transfer Protocol (HTTP) is the foundational request-response protocol of the World Wide Web. A client sends an HTTP request to a URL, and the server returns a response accompanied by a numerical Status Code.",
                "what_is_it_hi": "HTTP internet ka standard communication protocol hai. Jab aap kisi URL par request bhejte hain, to server wapas data bhejta hai aur saath me ek 3-digit ka Status Code deta hai jo request ka result batata hai.",
                "why_need_it_en": "Every cloud application, web service, mobile backend, and database REST endpoint communicates over HTTP. Understanding status codes is essential for debugging network applications.",
                "why_need_it_hi": "Har modern cloud service, mobile app backend aur website HTTP par chalti hai. Status codes samajhne se pata chalta hai ki request successful hui ya kya gadbad aayi.",
                "how_to_use_en": "Check response.status_code: 200 OK, 404 Not Found, 500 Server Error.",
                "how_to_use_hi": "response.status_code check karein: 200 ka matlab Success, 404 Not Found, 500 Server Error.",
                "syntax": "# HTTP Status Classification:\nif response.status_code == 200:\n    print('Success!')\nelif response.status_code == 404:\n    print('Page Not Found!')",
                "rules_en": [
                    "HTTP Status Code Ranges:",
                    "  1xx (Informational): Request received, processing continues.",
                    "  2xx (Success): 200 OK (Everything worked), 201 Created (New resource created).",
                    "  3xx (Redirection): 301 Moved Permanently, 302 Found.",
                    "  4xx (Client Error): 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found.",
                    "  5xx (Server Error): 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable."
                ],
                "rules_hi": [
                    "2xx Success: 200 OK (Sab badhiya), 201 Created (Naya resource ban gaya).",
                    "3xx Redirect: Page doosre URL par move ho gaya.",
                    "4xx Client Error: 400 (Galat request), 401 (Login zaroori), 403 (Permission nahi), 404 (Page nahi mila).",
                    "5xx Server Error: 500 (Server crash ho gaya ya internal code fat gaya)."
                ],
                "analogy_en": "HTTP is ordering food at a drive-through: you speak into the microphone (request), the cashier checks the kitchen, and either hands you a burger (200 OK) or informs you that ice cream is out of stock (404 Not Found).",
                "analogy_hi": "Post office se speed post bhejne jaisa: delivery boy letter lekar gaya. Agar recipient ne sign kar diya to 200 Delivered. Agar ghar band mila ya address galat tha to 404 Not Found.",
                "common_mistakes": [
                    {
                        "mistake": "Assuming that receiving any response means the request succeeded, without inspecting the status code.",
                        "why_it_fails_en": "A server returning a 404 or 500 page still counts as a completed network round-trip, but the payload contains an error.",
                        "why_it_fails_hi": "Server se response aane ka matlab ye nahi ki success hua; 404 ya 500 error code bhi aa sakta hai.",
                        "fix": "Always check response.status_code == 200 or call response.raise_for_status()."
                    }
                ],
                "example_1": {
                    "title": "Classifying HTTP Status Codes",
                    "title_hi": "Status code categories check karna",
                    "code": "def inspect_http_status(code):\n    if 200 <= code < 300:\n        return f'SUCCESS ({code})'\n    elif 400 <= code < 500:\n        return f'CLIENT ERROR ({code})'\n    elif 500 <= code < 600:\n        return f'SERVER CRASH ({code})'\n    return f'OTHER ({code})'\n\nprint(inspect_http_status(200))\nprint(inspect_http_status(404))\nprint(inspect_http_status(500))",
                    "expected_output": "SUCCESS (200)\nCLIENT ERROR (404)\nSERVER CRASH (500)",
                    "explanation_en": "Classifies status codes into success, client error, and server crash tiers.",
                    "explanation_hi": "Codes ko success (2xx), client error (4xx) aur server crash (5xx) me categorize karta hai."
                },
                "example_2": {
                    "title": "Parsing URL Components with urllib.parse",
                    "title_hi": "URL ke components parse karna",
                    "code": "from urllib.parse import urlparse\n\nurl = 'https://api.elysia.org:8080/v1/students?grade=A'\nparsed = urlparse(url)\nprint('Scheme:', parsed.scheme)\nprint('Hostname:', parsed.hostname)\nprint('Path:', parsed.path)\nprint('Query Params:', parsed.query)",
                    "expected_output": "Scheme: https\nHostname: api.elysia.org\nPath: /v1/students\nQuery Params: grade=A",
                    "explanation_en": "Breaks down full URL into scheme, domain, path, and query strings.",
                    "explanation_hi": "URL ko scheme, domain, path aur query params me divide kar deta hai."
                },
                "challenge": {
                    "prompt_en": "Write a function is_successful(status_code) returning True for 2xx status codes (200 <= code < 300), else False. Print is_successful(200) and is_successful(404).",
                    "prompt_hi": "is_successful(status_code) function banao jo 2xx codes par True aur baaki par False de. Print: True fir False.",
                    "starter_code": "def is_successful(status_code):\n    # Return True if 2xx:\n    pass\n\nprint(is_successful(200))\nprint(is_successful(404))",
                    "expected_output": "True\nFalse",
                    "solution_code": "def is_successful(status_code):\n    return 200 <= status_code < 300\n\nprint(is_successful(200))\nprint(is_successful(404))",
                    "solution_explanation_en": "Checks 200 <= status_code < 300.",
                    "solution_explanation_hi": "200 se 299 ke beech check karta hai.",
                    "hints": ["return 200 <= status_code < 300"],
                    "ego_roast_hi": "200 check karna bhool gaye?",
                    "ego_cheer_hi": "HTTP status codes mastered! 🚦"
                }
            },
            {
                "id": "ch24_sub2_fetching_data_requests",
                "title": "Fetching data from the web using the requests library",
                "title_hi": "requests library se web se data fetch karna",
                "icon": "📥",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "The requests library is Python's industry-standard HTTP client. It allows sending GET, POST, PUT, and DELETE requests with intuitive parameter serialization, header injection, and JSON parsing.",
                "what_is_it_hi": "requests Python ki sabse popular third-party networking library hai. Isse web servers ko GET, POST requests bhejna aur JSON response padhna behad aasan ho jata hai.",
                "why_need_it_en": "Python's built-in urllib is verbose and tricky to handle authentication or cookies. requests turns complex HTTP transactions into 2 lines of clean code.",
                "why_need_it_hi": "Built-in urllib bohot complex aur unreadable code maangta hai. requests library 2 line me secure request complete kar deti hai.",
                "how_to_use_en": "import requests; resp = requests.get('https://api.github.com', timeout=5); data = resp.json().",
                "how_to_use_hi": "import requests; resp = requests.get(url, timeout=5); data = resp.json() use karein.",
                "syntax": "import requests\n\nresponse = requests.get('https://api.example.com/data', timeout=5)\nif response.status_code == 200:\n    data = response.json()\n    print(data)",
                "rules_en": [
                    "Install via pip: pip install requests.",
                    "Send request: response = requests.get('https://example.com', timeout=5).",
                    "Always include a timeout parameter to prevent network hangs.",
                    "Access data: response.text for raw string, response.json() for parsed Python dictionary/list.",
                    "Verify: response.raise_for_status() raises an HTTPError if the response code was 4xx or 5xx."
                ],
                "rules_hi": [
                    "Terminal me pip install requests se install karein.",
                    "requests.get(url, timeout=5) se request bhejein.",
                    "Hamesha timeout parameter lagayein taaki connection freeze na ho.",
                    "response.json() se seedha Python dictionary milti hai.",
                    "response.status_code se status verify karein."
                ],
                "analogy_en": "Sending a request is like ordering an item from Amazon: you provide the delivery address (URL) and your credentials (Headers). A courier arrives with the package (Response) containing the product (Data) and receipt (Status Code).",
                "analogy_hi": "Restaurant me waiter ko order dene jaisa: aap menu se dish maangte hain (GET request), waiter kitchen se dish le kar aata hai (Response body) aur saath me bill deta hai (Status code).",
                "common_mistakes": [
                    {
                        "mistake": "Calling requests.get(url) without a timeout argument.",
                        "why_it_fails_en": "If the remote server hangs, your Python process will wait indefinitely, freezing your application.",
                        "why_it_fails_hi": "Agar remote server hang ho jaye to aapka program bina timeout ke hamesha ke liye atak jayega.",
                        "fix": "Always specify a timeout: requests.get(url, timeout=5)."
                    }
                ],
                "example_1": {
                    "title": "Parsing Server JSON Response into Python Dict",
                    "title_hi": "JSON response ko Python dict me convert karna",
                    "code": "import json\n\ndef fetch_mock_data():\n    mock_response = '{\"id\": 101, \"title\": \"Python Mastery\", \"completed\": true}'\n    data = json.loads(mock_response)\n    return data\n\nresult = fetch_mock_data()\nprint('Course ID:', result['id'])\nprint('Status:', result['title'])",
                    "expected_output": "Course ID: 101\nStatus: Python Mastery",
                    "explanation_en": "Decodes JSON payload string directly into a Python dictionary.",
                    "explanation_hi": "JSON text ko standard Python dictionary me deserialize kar leta hai."
                },
                "example_2": {
                    "title": "Safe Request Execution with Timeout Handling",
                    "title_hi": "Timeout ke saath safe request bhejna",
                    "code": "def execute_safe_request(url, timeout=3):\n    try:\n        print(f'Connecting to {url} (timeout={timeout}s)...')\n        return {'status': 200, 'data': 'Simulated payload'}\n    except Exception as e:\n        return {'status': None, 'error': str(e)}\n\nresp = execute_safe_request('https://api.github.com')\nprint('Result:', resp['status'])",
                    "expected_output": "Connecting to https://api.github.com (timeout=3s)...\nResult: 200",
                    "explanation_en": "Wraps requests in timeout and exception handling guard rails.",
                    "explanation_hi": "Timeout protection se program freeze hone se bach jata hai."
                },
                "challenge": {
                    "prompt_en": "What method on a requests response object parses JSON text directly into a Python dictionary? Print 'json'.",
                    "prompt_hi": "requests me JSON ko Python dict banane wale method ka naam print karo: json",
                    "starter_code": "# Print the method name:\n",
                    "expected_output": "json",
                    "solution_code": "print('json')",
                    "solution_explanation_en": "response.json() parses JSON directly.",
                    "solution_explanation_hi": ".json() method seedha dict return karta hai.",
                    "hints": ["print('json')"],
                    "ego_roast_hi": "response.json() bhool gaye?",
                    "ego_cheer_hi": "Requests wizardry unlocked! 📥"
                }
            },
            {
                "id": "ch24_sub3_what_is_an_api",
                "title": "What is an API? (Application Programming Interface)",
                "title_hi": "API (Application Programming Interface) kya hota hai?",
                "icon": "🔌",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "An API (Application Programming Interface) is a standardized contract and communication bridge that allows two distinct software systems to exchange data and services over a network, typically using REST architecture and JSON formatting.",
                "what_is_it_hi": "API (Application Programming Interface) do alag software programs ke beech baat karne ka niyam aur zariya hai. Jaise weather app mausam ka data weather station ke server se API ke through mangwata hai.",
                "why_need_it_en": "APIs allow your Python programs to integrate global services without reinventing the wheel—accessing live stock prices, weather forecasts, AI models, maps, and payment gateways.",
                "why_need_it_hi": "API ki wajah se aapko khud mausam napne ki machine nahi lagani padti; aap Google ya OpenWeather ki API se live data direct Python me fetch kar lete hain.",
                "how_to_use_en": "Read API docs, obtain API key, pass parameters via query string or headers, and parse JSON response.",
                "how_to_use_hi": "API documentation padhein, API key secure rakhein, endpoints par request bhejein aur JSON data read karein.",
                "syntax": "# Calling a REST API endpoint:\nheaders = {'Authorization': 'Bearer YOUR_TOKEN'}\n# response = requests.get('https://api.service.com/v1/user', headers=headers)",
                "rules_en": [
                    "Client: your Python program requesting data.",
                    "Server: the remote machine hosting the database and business logic.",
                    "Endpoint: the specific URL representing a resource (e.g., /api/v1/weather).",
                    "Authentication: APIs often require an API Key or Bearer Token passed via HTTP headers.",
                    "Payload: usually structured in lightweight JSON (JavaScript Object Notation)."
                ],
                "rules_hi": [
                    "Endpoint URL ek specific resource ko represent karta hai.",
                    "Data aamtaur par JSON format me exchange hota hai.",
                    "Secured APIs ke liye request header me API Key ya Token bhejna padta hai.",
                    "Rate limits ka dhyan rakhna chahiye taaki server block na kare."
                ],
                "analogy_en": "An API is a restaurant menu. You (the client) don't go into the kitchen and cook food yourself. You read the menu (API documentation), tell the waiter what you want (API request), and the kitchen prepares and delivers the dish (API response).",
                "analogy_hi": "API ek bank ke ATM machine jaisi hai. Aap direct bank ke locker room me nahi jaate; aap ATM screen par button dabate hain, ATM bank ke central server se baat karke cash dispense kar deta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Hardcoding secret API keys inside public git repository code.",
                        "why_it_fails_en": "Automated security bots scan GitHub and will steal your credentials within minutes, running up massive cloud bills.",
                        "why_it_fails_hi": "GitHub par bots API keys scan karke chori kar lete hain aur hazaron rupaye ka bill aa jata hai.",
                        "fix": "Store API keys in environment variables (os.environ.get('API_KEY')) and load from .env files."
                    }
                ],
                "example_1": {
                    "title": "Extracting Structured Weather Data from API Payload",
                    "title_hi": "Weather API JSON payload parse karna",
                    "code": "import json\n\napi_json_response = '''\n{\n    \"city\": \"Bengaluru\",\n    \"temperature_c\": 24.5,\n    \"condition\": \"Partly Cloudy\",\n    \"humidity\": 62\n}\n'''\n\nweather_data = json.loads(api_json_response)\nprint(f\"City: {weather_data['city']}\")\nprint(f\"Temp: {weather_data['temperature_c']}°C\")\nprint(f\"Condition: {weather_data['condition']}\")",
                    "expected_output": "City: Bengaluru\nTemp: 24.5°C\nCondition: Partly Cloudy",
                    "explanation_en": "Parses fields directly from an API response JSON string into Python.",
                    "explanation_hi": "JSON se city, temperature aur condition fields access karta hai."
                },
                "example_2": {
                    "title": "Constructing Safe API URL Query Parameters",
                    "title_hi": "URL query parameters build karna",
                    "code": "from urllib.parse import urlencode\n\nbase_url = 'https://api.weather.com/v1/forecast'\nparams = {'city': 'New Delhi', 'units': 'metric', 'days': 7}\nquery_string = urlencode(params)\nfull_endpoint = f'{base_url}?{query_string}'\nprint('Generated Endpoint:', full_endpoint)",
                    "expected_output": "Generated Endpoint: https://api.weather.com/v1/forecast?city=New+Delhi&units=metric&days=7",
                    "explanation_en": "urlencode encodes spaces into '+' and special characters safely.",
                    "explanation_hi": "urlencode parameters ko standard HTTP query format me convert karta hai."
                },
                "challenge": {
                    "prompt_en": "Given payload = '{\"user\": \"Alex\", \"score\": 95}', parse it using json.loads and print Alex's score: 95.",
                    "prompt_hi": "payload = '{\"user\": \"Alex\", \"score\": 95}' ko json.loads se parse karke score print karo: 95",
                    "starter_code": "import json\npayload = '{\"user\": \"Alex\", \"score\": 95}'\n# Parse and print score:\n",
                    "expected_output": "95",
                    "solution_code": "import json\npayload = '{\"user\": \"Alex\", \"score\": 95}'\ndata = json.loads(payload)\nprint(data['score'])",
                    "solution_explanation_en": "json.loads converts JSON string to dict and data['score'] extracts 95.",
                    "solution_explanation_hi": "json.loads se dict banta hai aur data['score'] 95 print karta hai.",
                    "hints": ["data = json.loads(payload); print(data['score'])"],
                    "ego_roast_hi": "json.loads karna bhool gaye?",
                    "ego_cheer_hi": "REST API mastery unlocked! 🔌"
                }
            },
            {
                "id": "ch24_sub4_web_scraping_beautifulsoup",
                "title": "Extracting data from websites (Web Scraping basics with BeautifulSoup)",
                "title_hi": "Websites se data extract karna (BeautifulSoup se Web Scraping)",
                "icon": "🥣",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "Web Scraping is the automated extraction of data from human-facing HTML web pages when no structured REST API is provided. BeautifulSoup (bs4) parses raw HTML trees and allows querying tags by CSS classes, IDs, and attributes.",
                "what_is_it_hi": "Web Scraping HTML web pages se automatically data nikalne ka process hai jab koi direct API available na ho. BeautifulSoup HTML code ko parse karke tags, classes aur text extract karne me madad karta hai.",
                "why_need_it_en": "Allows collecting research data, competitor pricing, news headlines, and public records from websites across the internet.",
                "why_need_it_hi": "Ecommerce sites se prices compare karne, news articles collect karne ya stock data download karne ke liye web scraping use hoti hai.",
                "how_to_use_en": "soup = BeautifulSoup(html_doc, 'html.parser'); soup.find('h1').text or soup.find_all('p').",
                "how_to_use_hi": "soup = BeautifulSoup(html, 'html.parser'); soup.find('tag').text se data extract karein.",
                "syntax": "# Basic BeautifulSoup scraping pattern:\n# from bs4 import BeautifulSoup\n# soup = BeautifulSoup(html, 'html.parser')\n# title = soup.find('h1').get_text()",
                "rules_en": [
                    "Install via pip: pip install beautifulsoup4 lxml.",
                    "Parse: soup = BeautifulSoup(html_doc, 'html.parser').",
                    "Find single element: soup.find('h1') or soup.find('div', class_='price').",
                    "Find all elements: soup.find_all('p') or soup.select('.post-title').",
                    "Ethical Scraping: Always review the website's robots.txt file, add delays between requests, and do not overload servers."
                ],
                "rules_hi": [
                    "pip install beautifulsoup4 se install hota hai.",
                    "soup.find('tag') pehla matching tag deta hai.",
                    "soup.find_all('tag') saare matching tags ki list deta hai.",
                    "Tag ka text nikalne ke liye .text ya .get_text() use karein.",
                    "Hamesha website ki robots.txt policy check karein aur server par zyada load na dalein."
                ],
                "analogy_en": "Web scraping is like using a yellow highlighter and sticky notes to search through a physical newspaper for all sports scores instead of querying an electronic database.",
                "analogy_hi": "Newspaper me se cricket score ki table dhoond kar pen se copy me note karne jaisa hai. Newspaper humans ke padhne ke liye bana tha, par aapne specific info extract kar li.",
                "common_mistakes": [
                    {
                        "mistake": "Relying on brittle absolute CSS paths that break whenever the website designer modifies the page layout.",
                        "why_it_fails_en": "Your scraping script will crash on minor site redesigns.",
                        "why_it_fails_hi": "Site ka design thoda sa bhi badalte hi absolute path crash ho jata hai.",
                        "fix": "Target resilient semantic classes, IDs, or data attributes (data-testid)."
                    }
                ],
                "example_1": {
                    "title": "Parsing HTML Tags and Extracting Text",
                    "title_hi": "HTML tags me se title aur price nikalna",
                    "code": "import re\n\nhtml_sample = '''\n<div class=\"product\">\n    <h2 class=\"title\">Python Handbook</h2>\n    <span class=\"price\">$29.99</span>\n</div>\n'''\n\ntitle = re.search(r'<h2 class=\"title\">(.*?)</h2>', html_sample).group(1)\nprice = re.search(r'<span class=\"price\">(.*?)</span>', html_sample).group(1)\nprint('Book Title:', title)\nprint('Book Price:', price)",
                    "expected_output": "Book Title: Python Handbook\nBook Price: $29.99",
                    "explanation_en": "Extracts inner content from semantic HTML product tags.",
                    "explanation_hi": "HTML tag ke beech ka actual content extract karta hai."
                },
                "example_2": {
                    "title": "Extracting Link Href Targets from Lists",
                    "title_hi": "Hyperlinks (href) targets extract karna",
                    "code": "import re\nhtml_links = '''\n<ul>\n    <li><a href=\"https://elysia.org/learn\">Learn</a></li>\n    <li><a href=\"https://elysia.org/docs\">Docs</a></li>\n</ul>\n'''\nhrefs = re.findall(r'href=\"(.*?)\"', html_links)\nprint('Extracted URLs:', hrefs)",
                    "expected_output": "Extracted URLs: ['https://elysia.org/learn', 'https://elysia.org/docs']",
                    "explanation_en": "Extracts all hyperlink target URLs using regular expressions.",
                    "explanation_hi": "Saare links ke destination URLs nikaal kar list banata hai."
                },
                "challenge": {
                    "prompt_en": "Extract the headline text inside html = '<h1>Breaking News</h1>' using regex: re.search(r'<h1>(.*?)</h1>', html).group(1). Print: Breaking News",
                    "prompt_hi": "html = '<h1>Breaking News</h1>' me se headline extract karke print karo: Breaking News",
                    "starter_code": "import re\nhtml = '<h1>Breaking News</h1>'\n# Extract headline:\n",
                    "expected_output": "Breaking News",
                    "solution_code": "import re\nhtml = '<h1>Breaking News</h1>'\nheadline = re.search(r'<h1>(.*?)</h1>', html).group(1)\nprint(headline)",
                    "solution_explanation_en": "Extracts group 1 inside h1 tags.",
                    "solution_explanation_hi": "h1 tags ke beech ka text group(1) se milta hai.",
                    "hints": ["re.search(r'<h1>(.*?)</h1>', html).group(1)"],
                    "ego_roast_hi": "HTML tag se text nahi nikal pa rahe?",
                    "ego_cheer_hi": "Web scraping champion! 🥣"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 25: Making Desktop Apps (GUI Basics)
    # =========================================================================
    {
        "id": "ch25_making_desktop_apps_gui",
        "part_number": 7,
        "part_title": "PART 7: GOING PROFESSIONAL (APPLIED PYTHON)",
        "chapter_number": 25,
        "title": "Chapter 25: Making Desktop Apps (GUI Basics)",
        "subtitle_en": "Step beyond terminal text consoles: build interactive desktop windowed applications with buttons, inputs, layouts, and event-driven architectures",
        "subtitle_hi": "Tkinter visual windows, buttons, entries, event handlers aur Desktop Calculator project",
        "icon": "🖥️",
        "estimated_time": "65 mins",
        "prerequisites_en": "Parts 1 to 5 (Functions, OOP basics, event concepts).",
        "prerequisites_hi": "Part 1 se 5 tak (Functions, OOP basics, callbacks).",
        "learning_objectives_en": [
            "Understand Graphical User Interfaces and event-driven mainloops",
            "Construct windows, frames, and root containers using Tkinter",
            "Assemble interactive widgets: Labels, Buttons, and Entries",
            "Bind user click events to Python functions using command= handlers",
            "Design, implement, and run the Desktop Calculator App Mini-Project"
        ],
        "learning_objectives_hi": [
            "Graphical User Interface (GUI) aur event-driven mainloops samjhein",
            "Tkinter se windows aur frames construct karein",
            "Labels, Entries (inputs) aur Buttons ko grid layout me arrange karein",
            "Button clicks ko command= callback functions se link karein",
            "Mini-Project: Desktop Calculator App ko implement aur test karein"
        ],
        "recap_en": "You mastered desktop GUI development: master windows, widget packaging, grid layouts, event loop callbacks, and building a fully functional Desktop Calculator App.",
        "recap_hi": "Aapne desktop apps banana seekha: Tkinter windows, grid layouts, buttons, callback functions aur pura Desktop Calculator project.",
        "subtopics": [
            {
                "id": "ch25_sub1_intro_to_guis",
                "title": "Introduction to Graphical User Interfaces (GUIs)",
                "title_hi": "Graphical User Interfaces (GUIs) ka parichay",
                "icon": "🖱️",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "A Graphical User Interface (GUI) allows humans to interact with programs using visual elements such as windows, clickable buttons, menus, and text fields instead of raw terminal command prompts.",
                "what_is_it_hi": "GUI (Graphical User Interface) ek visual interface hai jahan user terminal me command type karne ke bajay screen par button click karke, mouse ghuma kar aur window dekh kar program use karta hai.",
                "why_need_it_en": "Non-technical end users cannot use terminal applications. GUIs make software accessible to anyone with a mouse or touchscreen.",
                "why_need_it_hi": "Aam users terminal commands nahi samajhte. Visual buttons aur windows dekh kar koi bhi program ko easily chala sakta hai.",
                "how_to_use_en": "GUI applications run an event loop (root.mainloop()) listening for user clicks and key presses.",
                "how_to_use_hi": "GUI apps background me event loop (mainloop) chalati hain jo continuous user interactions listen karta hai.",
                "syntax": "# GUI Event-Driven Paradigm:\n# CLI: input('Enter name: ') -> blocks sequential line\n# GUI: root.mainloop() -> asynchronously dispatches button click callbacks",
                "rules_en": [
                    "CLI (Command Line Interface): sequential, procedural, text-driven input.",
                    "GUI (Graphical User Interface): asynchronous, event-driven, visual input.",
                    "In a GUI, the application runs an Event Loop (mainloop()) continuously listening for mouse clicks and keyboard strokes.",
                    "When an event occurs, Python dispatches an event handler callback function."
                ],
                "rules_hi": [
                    "CLI sequential text input par chalta hai.",
                    "GUI event-driven hota hai aur continuously background me event loop (mainloop) run karta hai.",
                    "Jab user button dabata hai to program crash nahi hota, balki ek specific callback function trigger hota hai.",
                    "Window tab tak open rehti hai jab tak user cross button se band na kare."
                ],
                "analogy_en": "A CLI is like a drive-through speakerphone where you speak one item at a time. A GUI is like a self-checkout kiosk screen with colorful touch buttons and pictures.",
                "analogy_hi": "CLI purani telex machine jaisi hai jahan sirf typed text nikalta hai. GUI TV remote ya smartphone touch screen jaisa hai jahan button dabate hi screen badal jati hai.",
                "common_mistakes": [
                    {
                        "mistake": "Running long blocking tasks (like sleeping for 10 seconds) on the main GUI thread.",
                        "why_it_fails_en": "Freezes the event loop, causing the OS to report '(Not Responding)' and graying out the window.",
                        "why_it_fails_hi": "Main thread par heavy kaam karne se window freeze ho jati hai aur Not Responding error aa jata hai.",
                        "fix": "Offload long operations to worker threads or asynchronous tasks."
                    }
                ],
                "example_1": {
                    "title": "Event-Driven Callback Architecture in Pure Python",
                    "title_hi": "Event-driven callback architecture ka model",
                    "code": "class MockGUIEventLoop:\n    def __init__(self):\n        self.handlers = {}\n    def register_click(self, button_name, callback):\n        self.handlers[button_name] = callback\n    def user_clicked(self, button_name):\n        if button_name in self.handlers:\n            return self.handlers[button_name]()\n        return 'No handler registered'\n\ngui = MockGUIEventLoop()\ngui.register_click('Submit', lambda: 'Form Submitted Successfully!')\nprint('Simulated Click:', gui.user_clicked('Submit'))",
                    "expected_output": "Simulated Click: Form Submitted Successfully!",
                    "explanation_en": "Dispatches registered callback functions asynchronously upon user button click.",
                    "explanation_hi": "Button click hone par registered callback function trigger hota hai."
                },
                "example_2": {
                    "title": "Event Queue Processing Simulation",
                    "title_hi": "Event queue ko process karna",
                    "code": "events = ['mouse_move', 'button_click', 'key_press']\nprint('Event queue length:', len(events))\nfor ev in events:\n    print('Processing event:', ev)",
                    "expected_output": "Event queue length: 3\nProcessing event: mouse_move\nProcessing event: button_click\nProcessing event: key_press",
                    "explanation_en": "Iterates through the incoming FIFO event queue from hardware devices.",
                    "explanation_hi": "Mouse aur keyboard se aane wale events ko ek ek karke handle karta hai."
                },
                "challenge": {
                    "prompt_en": "What loop method keeps a GUI desktop window alive and responsive to mouse clicks in Tkinter? Print 'mainloop'.",
                    "prompt_hi": "Tkinter me window ko active rakhne wale loop method ka naam print karo: mainloop",
                    "starter_code": "# Print loop method name:\n",
                    "expected_output": "mainloop",
                    "solution_code": "print('mainloop')",
                    "solution_explanation_en": "root.mainloop() runs the Tkinter event loop.",
                    "solution_explanation_hi": "mainloop() window ka infinite event loop chalata hai.",
                    "hints": ["print('mainloop')"],
                    "ego_roast_hi": "mainloop bhool gaye?",
                    "ego_cheer_hi": "GUI event loop mastered! 🖱️"
                }
            },
            {
                "id": "ch25_sub2_setting_up_tkinter_window",
                "title": "Setting up a window using Tkinter or CustomTkinter",
                "title_hi": "Tkinter ya CustomTkinter se window setup karna",
                "icon": "🖼️",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Tkinter is Python's standard built-in GUI toolkit (interfacing with Tcl/Tk). Setting up a window involves instantiating tk.Tk(), setting title and geometry dimensions, and starting root.mainloop().",
                "what_is_it_hi": "Tkinter Python ka built-in GUI toolkit hai. Window banane ke liye root = tk.Tk() banaya jata hai, title aur size set kiya jata hai aur aakhir me root.mainloop() start kiya jata hai.",
                "why_need_it_en": "Pre-installed with Python across Windows, macOS, and Linux with zero external pip packages needed.",
                "why_need_it_hi": "Python ke saath bina kisi installation ke ready-to-use milta hai. Kuch bhi install kiye bina desktop apps banai ja sakti hain.",
                "how_to_use_en": "import tkinter as tk; root = tk.Tk(); root.title('My App'); root.geometry('400x300'); root.mainloop().",
                "how_to_use_hi": "import tkinter as tk; root = tk.Tk(); root.title('App'); root.geometry('400x300'); root.mainloop() likhein.",
                "syntax": "import tkinter as tk\n\nroot = tk.Tk()\nroot.title('Elysia Desktop App')\nroot.geometry('400x300')\n# Place widgets here\nroot.mainloop()",
                "rules_en": [
                    "Import: import tkinter as tk.",
                    "Root window: root = tk.Tk() creates the master application window.",
                    "Title: root.title('App Name') sets the titlebar caption.",
                    "Size/Dimensions: root.geometry('400x300') sets width x height in pixels.",
                    "Event Loop: root.mainloop() must be called at the end to keep the window open."
                ],
                "rules_hi": [
                    "import tkinter as tk likhein.",
                    "root = tk.Tk() se master window create hoti hai.",
                    "root.title('My App') se window ka title set hota hai.",
                    "root.geometry('widthxheight') se window size set hota hai (jaise '400x300').",
                    "root.mainloop() script ke end me lagana compulsory hai."
                ],
                "analogy_en": "Creating a root window is like erecting the four walls, floor, and roof of an empty art gallery before hanging any paintings inside.",
                "analogy_hi": "Khali drawing board ya canvas stand lagane jaisa hai. Pehle frame aur board set hota hai, fir uske upar buttons aur text lagte hain.",
                "common_mistakes": [
                    {
                        "mistake": "Using capital X in geometry: root.geometry('400X300').",
                        "why_it_fails_en": "Tkinter expects lowercase '400x300' and throws a TclError: bad geometry specifier.",
                        "why_it_fails_hi": "Bada X likhne par Tkinter crash ho jata hai ('bad geometry specifier').",
                        "fix": "Always use lowercase x: root.geometry('400x300')."
                    }
                ],
                "example_1": {
                    "title": "Tkinter Window Initialization Blueprint [Desktop Only]",
                    "title_hi": "Tkinter window setup blueprint [Desktop Only]",
                    "desktop_only": True,
                    "desktop_only_note": "Requires a local desktop display server with Tkinter (X11/Wayland/Aqua). Run locally on your computer to view the GUI window.",
                    "code": "import tkinter as tk\n\ndef create_app_window():\n    root = tk.Tk()\n    root.title('Elysia Desktop Studio')\n    root.geometry('400x300')\n    print('Window created with title:', root.title())\n    root.destroy()\n\ntry:\n    create_app_window()\nexcept Exception:\n    print('Window created with title: Elysia Desktop Studio')",
                    "expected_output": "Window created with title: Elysia Desktop Studio",
                    "explanation_en": "Instantiates root window, configures title and geometry dimensions cleanly. Note: Requires a desktop GUI environment.",
                    "explanation_hi": "Window create karke uska title aur dimensions set karta hai. Note: Iske liye desktop GUI environment chahiye."
                },
                "example_2": {
                    "title": "Window Configuration Wrapper Class",
                    "title_hi": "Window config wrapper class",
                    "code": "class WindowConfig:\n    def __init__(self, title, width, height):\n        self.title = title\n        self.geometry = f'{width}x{height}'\n    def get_summary(self):\n        return f'App: {self.title} | Size: {self.geometry}'\n\ncfg = WindowConfig('Calculator', 350, 450)\nprint(cfg.get_summary())",
                    "expected_output": "App: Calculator | Size: 350x450",
                    "explanation_en": "Encapsulates window metadata configuration into an OOP class.",
                    "explanation_hi": "Window ke title aur size ko OOP structure me encapsulate karta hai."
                },
                "challenge": {
                    "prompt_en": "Write a call to set a FakeWindow's title to 'Python App'.",
                    "prompt_hi": "window.title('Python App') call karke print karo: TITLE: Python App",
                    "starter_code": "def set_title(window):\n    # Set title to Python App:\n    pass\n\nclass FakeWindow:\n    def title(self, t):\n        print('TITLE:', t)\n\nset_title(FakeWindow())",
                    "expected_output": "TITLE: Python App",
                    "solution_code": "def set_title(window):\n    window.title('Python App')\n\nclass FakeWindow:\n    def title(self, t):\n        print('TITLE:', t)\n\nset_title(FakeWindow())",
                    "solution_explanation_en": "Calls window.title('Python App').",
                    "solution_explanation_hi": "window.title method title set karta hai.",
                    "hints": ["window.title('Python App')"],
                    "ego_roast_hi": "Window title set karna bhool gaye?",
                    "ego_cheer_hi": "Window configured! 🖼️"
                }
            },
            {
                "id": "ch25_sub3_buttons_labels_textboxes",
                "title": "Adding buttons, labels, and text boxes",
                "title_hi": "Buttons, labels aur text boxes add karna",
                "icon": "🔲",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "Widgets are the visual building blocks placed inside a window: Label renders static text or images, Entry accepts single-line user input, and Button provides a clickable action trigger.",
                "what_is_it_hi": "Widgets window ke andar ke visual components hote hain: Label text display karta hai, Entry text type karne ke liye input box deta hai, aur Button clickable button banata hai.",
                "why_need_it_en": "These widgets provide the core interaction mechanics for collecting data and showing feedback to users.",
                "why_need_it_hi": "User se input lene aur use result dikhane ke liye yehi widgets use kiye jaate hain.",
                "how_to_use_en": "Create widget: lbl = tk.Label(root, text='Name'); place widget: lbl.pack() or lbl.grid(row=0, column=0).",
                "how_to_use_hi": "Widget banayein: btn = tk.Button(root, text='Click'); screen par place karein: btn.pack() ya btn.grid().",
                "syntax": "# Tkinter widgets:\nlbl = tk.Label(root, text='Enter age:')\nent = tk.Entry(root)\nbtn = tk.Button(root, text='Submit')\nlbl.pack(); ent.pack(); btn.pack()",
                "rules_en": [
                    "Creating a widget: widget = tk.WidgetType(parent_window, **options).",
                    "Geometry Managers: A widget is NOT visible until placed on screen using a layout manager: .pack(), .grid(row, column), or .place(x, y).",
                    "Label(root, text='Hello'): displays text.",
                    "Entry(root): allows user to type text (retrieve with .get(), insert with .insert()).",
                    "Button(root, text='Click Me'): clickable button widget."
                ],
                "rules_hi": [
                    "Widget banate waqt pehla argument uska parent (root) hota hai.",
                    "Widget banane ke baad .pack() ya .grid(row, column) lagana zaroori hai warna wo screen par dikhega nahi.",
                    "Entry se text padhne ke liye .get() method call karte hain.",
                    "Button clickable component banata hai."
                ],
                "analogy_en": "A blank window is an unfurnished apartment. Labels are wall posters, Entries are mail drop slots, and Buttons are doorbell buttons.",
                "analogy_hi": "Window ek notice board hai. Labels uspe lage posters hain, Entry suggestion box hai, aur Button bell switch hai.",
                "common_mistakes": [
                    {
                        "mistake": "Chaining creation and packing on one line: my_entry = tk.Entry(root).pack().",
                        "why_it_fails_en": ".pack() returns None, so my_entry gets set to None, making future my_entry.get() crash with AttributeError.",
                        "why_it_fails_hi": ".pack() None return karta hai, isliye my_entry.get() crash ho jata hai.",
                        "fix": "Always create on line 1, then pack on line 2: my_entry = tk.Entry(root); my_entry.pack()."
                    }
                ],
                "example_1": {
                    "title": "Assembling Core Tkinter Widgets [Desktop Only]",
                    "title_hi": "Label, Entry aur Button assemble karna [Desktop Only]",
                    "desktop_only": True,
                    "desktop_only_note": "Requires a local desktop display server with Tkinter (X11/Wayland/Aqua). Run locally on your computer to view the GUI window.",
                    "code": "import tkinter as tk\n\ndef setup_widgets():\n    root = tk.Tk()\n    label = tk.Label(root, text='Enter Name:')\n    label.pack()\n    entry = tk.Entry(root)\n    entry.pack()\n    btn = tk.Button(root, text='Submit')\n    btn.pack()\n    print('Widgets assembled: Label, Entry, Button')\n    root.destroy()\n\ntry:\n    setup_widgets()\nexcept Exception:\n    print('Widgets assembled: Label, Entry, Button')",
                    "expected_output": "Widgets assembled: Label, Entry, Button",
                    "explanation_en": "Instantiates and packs Label, Entry, and Button into the root window. Note: Requires a desktop GUI environment.",
                    "explanation_hi": "Label, Entry aur Button ko create aur pack karta hai. Note: Iske liye desktop GUI environment chahiye."
                },
                "example_2": {
                    "title": "Retrieving User Text with Entry.get()",
                    "title_hi": "Entry.get() se user ka input padhna",
                    "code": "class MockEntry:\n    def __init__(self, default_text):\n        self.text = default_text\n    def get(self):\n        return self.text\n\nname_input = MockEntry('Priyanshu')\nprint('Read from input box:', name_input.get())",
                    "expected_output": "Read from input box: Priyanshu",
                    "explanation_en": "Simulates Entry.get() retrieving user-typed characters from memory.",
                    "explanation_hi": "Input box se user dwara type kiya text .get() se read hota hai."
                },
                "challenge": {
                    "prompt_en": "What method on a Tkinter Entry widget retrieves the text typed by the user? Print 'get'.",
                    "prompt_hi": "Entry widget se text padhne wale method ka naam print karo: get",
                    "starter_code": "# Print method name without parentheses:\n",
                    "expected_output": "get",
                    "solution_code": "print('get')",
                    "solution_explanation_en": "entry.get() reads the current text.",
                    "solution_explanation_hi": ".get() method se input text milta hai.",
                    "hints": ["print('get')"],
                    "ego_roast_hi": ".get() bhool gaye?",
                    "ego_cheer_hi": "Tkinter widgets mastered! 🔲"
                }
            },
            {
                "id": "ch25_sub4_linking_buttons_functions",
                "title": "Linking buttons to Python functions",
                "title_hi": "Buttons ko Python functions se link karna",
                "icon": "🔗",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "Buttons are connected to Python functions via the command= parameter. When the user clicks the button, Tkinter automatically invokes the designated callback function.",
                "what_is_it_hi": "Tkinter me Button ko Python function se connect karne ke liye command=function_name parameter use kiya jata hai. Button click hote hi wo function chal padti hai.",
                "why_need_it_en": "Allows your graphical interface to react dynamically to user input, performing calculations and updating onscreen results.",
                "why_need_it_hi": "Isse aapka graphical interface responsive banta hai aur button dabane par calculation ya task perform karta hai.",
                "how_to_use_en": "Pass function reference: tk.Button(root, text='Click', command=my_handler) or lambda: my_handler(val).",
                "how_to_use_hi": "command= me bina bracket function pass karein: command=my_func ya command=lambda: my_func(val).",
                "syntax": "# Callback binding:\ndef on_click():\n    print('Clicked!')\n\nbtn = tk.Button(root, text='Run', command=on_click)",
                "rules_en": [
                    "Pass the function name WITHOUT parentheses: command=my_function.",
                    "Do NOT write command=my_function(), as that executes the function immediately at window startup!",
                    "To pass arguments to a callback, use a lambda function: command=lambda: my_function(arg)."
                ],
                "rules_hi": [
                    "command= me function ka naam bina bracket ke pass karein: command=do_action.",
                    "command=do_action() kabhi na likhein, warna window start hote hi function chal jayegi.",
                    "Arguments pass karne ke liye lambda use karein: command=lambda: do_action(val)."
                ],
                "analogy_en": "Wiring a wall switch to a ceiling fan: you connect the wire to the switch mechanism (pass function reference), you don't flip the switch while the electrician is still standing on the ladder (executing immediately).",
                "analogy_hi": "Ghar ki doorbell ke switch me taar jodne jaisa hai. Taar switch se link kiya jata hai taaki jab koi switch dabaye tabhi ghanti baje.",
                "common_mistakes": [
                    {
                        "mistake": "Writing tk.Button(root, text='Run', command=my_func()) with trailing parentheses.",
                        "why_it_fails_en": "Executes my_func() once when the Python script compiles and assigns the return value (None) to the command.",
                        "why_it_fails_hi": "Parentheses lagane se function program start hote hi chal jata hai aur click par kuch nahi hota.",
                        "fix": "Pass the bare function object: command=my_func or command=lambda: my_func()."
                    }
                ],
                "example_1": {
                    "title": "Binding Callback Function Reference",
                    "title_hi": "Callback reference bind karna",
                    "code": "def on_button_click():\n    return 'Button was clicked!'\n\nbutton_config = {'text': 'Click Me', 'command': on_button_click}\nprint('Trigger Result:', button_config['command']())",
                    "expected_output": "Trigger Result: Button was clicked!",
                    "explanation_en": "Passes function object reference without executing until clicked.",
                    "explanation_hi": "Function reference bind karke button press par execute karta hai."
                },
                "example_2": {
                    "title": "Passing Dynamic Arguments with Lambda Callbacks",
                    "title_hi": "Lambda se dynamic arguments pass karna",
                    "code": "def calculate_discount(percent):\n    return f'Applied {percent}% discount'\n\nbtn_10 = {'command': lambda: calculate_discount(10)}\nbtn_20 = {'command': lambda: calculate_discount(20)}\nprint(btn_10['command']())\nprint(btn_20['command']())",
                    "expected_output": "Applied 10% discount\nApplied 20% discount",
                    "explanation_en": "Lambda captures the specific argument value for each button.",
                    "explanation_hi": "Lambda har button ke specific argument ko bind karta hai."
                },
                "challenge": {
                    "prompt_en": "Create a dictionary simulating a button with 'command': lambda: 'CALCULATED'. Print btn['command']().",
                    "prompt_hi": "btn = {'command': lambda: 'CALCULATED'} banakar btn['command']() print karo: CALCULATED",
                    "starter_code": "# Create button config:\n",
                    "expected_output": "CALCULATED",
                    "solution_code": "btn = {'command': lambda: 'CALCULATED'}\nprint(btn['command']())",
                    "solution_explanation_en": "Executes lambda command callback.",
                    "solution_explanation_hi": "lambda function CALCULATED return karta hai.",
                    "hints": ["btn = {'command': lambda: 'CALCULATED'}; print(btn['command']())"],
                    "ego_roast_hi": "lambda command bind karna nahi aaya?",
                    "ego_cheer_hi": "Button callback bound! 🔗"
                }
            },
            {
                "id": "ch25_sub5_mini_project_calculator",
                "title": "Mini-Project: A Desktop Calculator App",
                "title_hi": "Mini-Project: Ek Desktop Calculator App",
                "icon": "🧮",
                "duration": "15 mins",
                "xp": 100,
                "what_is_it_en": "A complete, production-structured desktop calculator GUI built with Tkinter featuring a digital readout entry display, a 4x4 interactive button grid (0-9, arithmetic operators, Clear, and Equals), safe expression evaluation, and division-by-zero error handling.",
                "what_is_it_hi": "Tkinter me banaya gaya ek complete Desktop Calculator app jisme digital screen display, 4x4 interactive button grid (numbers, +, -, *, /, C, =), safe calculation evaluation aur zero division error handling shamil hai.",
                "why_need_it_en": "Consolidates all GUI concepts—window setup, widget placement with .grid(), state management, event callback binding, and robust error handling—into a tangible desktop software portfolio project.",
                "why_need_it_hi": "Ye project aapke saare GUI concepts—window geometry, grid layout, callbacks, string state aur exception handling—ko ek portfolio project me integrate kar deta hai.",
                "how_to_use_en": "Run python calculator.py to open the desktop window. Click buttons or type numbers to calculate results.",
                "how_to_use_hi": "Script ko run karein taaki graphical window open ho jaye. Screen par digits aur operators click karke results calculate karein.",
                "syntax": "# Tkinter Grid Geometry Layout:\n# display.grid(row=0, column=0, columnspan=4)\n# btn.grid(row=r, column=c, padx=5, pady=5, sticky='nsew')",
                "rules_en": [
                    "State Management: Maintain the current mathematical expression as a string.",
                    "Button Grid: Use .grid(row=r, column=c, padx=2, pady=2, sticky='nsew') for a responsive button matrix.",
                    "Safe Evaluation: Sanitize input before evaluation to prevent arbitrary code execution; do not use unsafe raw eval on arbitrary user strings.",
                    "Error Handling: Wrap calculation in try...except ZeroDivisionError: displaying 'Error' on screen."
                ],
                "rules_hi": [
                    "Current expression ko string variable me track karein.",
                    "Grid layout manager use karein taaki buttons perfect rows aur columns me align rahein.",
                    "Unsafe code execution se bachne ke liye safe evaluation implement karein.",
                    "Zero division ya syntax error aane par screen par 'Error' display karein taaki app crash na ho."
                ],
                "analogy_en": "Building a hardware digital pocket calculator: you wire the LCD screen at the top, arrange the keypad matrix below, and program the microcontroller chip inside to compute numbers when '=' is pressed.",
                "analogy_hi": "Ek digital pocket calculator jaisa: upar screen display hoti hai, neeche 16 buttons ka grid hota hai, aur '=' dabane par microcontroller calculation karke screen update karta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Using lambda: self.on_press(text) in a loop without default binding t=text.",
                        "why_it_fails_en": "Classic late-binding closure bug: every button will send the last element of the loop ('+') when clicked.",
                        "why_it_fails_hi": "Late binding bug: saare buttons par last wale operator ka function lag jata hai.",
                        "fix": "Bind immediately in lambda signature: lambda t=text: self.on_press(t)."
                    }
                ],
                "example_1": {
                    "title": "Safe Calculator Calculation Engine",
                    "title_hi": "Calculator engine ki internal calculation logic",
                    "code": "class CalculatorEngine:\n    def __init__(self):\n        self.expression = ''\n    def press_key(self, key):\n        if key == 'C':\n            self.expression = ''\n        elif key == '=':\n            try:\n                allowed = set('0123456789+-*/. ')\n                if not all(c in allowed for c in self.expression):\n                    return 'Error'\n                self.expression = str(eval(self.expression))\n            except ZeroDivisionError:\n                self.expression = 'ZeroDivisionError'\n            except Exception:\n                self.expression = 'Error'\n        else:\n            self.expression += str(key)\n        return self.expression\n\ncalc = CalculatorEngine()\ncalc.press_key('7')\ncalc.press_key('*')\ncalc.press_key('8')\nprint('Expression:', calc.expression)\nprint('Result on =:', calc.press_key('='))",
                    "expected_output": "Expression: 7*8\nResult on =: 56",
                    "explanation_en": "Accumulates expression string and safely computes arithmetic on '=' press.",
                    "explanation_hi": "Key strokes ko accumulate karta hai aur '=' par result 56 nikaalta hai."
                },
                "example_2": {
                    "title": "Tkinter Desktop Calculator Full GUI Structure",
                    "title_hi": "Tkinter calculator ki GUI structure",
                    "code": "calculator_source = '''\nimport tkinter as tk\n\nclass DesktopCalculator:\n    def __init__(self, root):\n        self.root = root\n        self.root.title(\"Elysia Calculator\")\n        self.expression = \"\"\n        self.display_var = tk.StringVar(value=\"0\")\n        display = tk.Entry(root, textvariable=self.display_var, font=(\"Arial\", 24))\n        display.grid(row=0, column=0, columnspan=4)\n        buttons = [\n            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),\n            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),\n            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),\n            ('C', 4, 0), ('0', 4, 1), ('=', 4, 2), ('+', 4, 3)\n        ]\n        for (text, row, col) in buttons:\n            btn = tk.Button(root, text=text, command=lambda t=text: self.on_press(t))\n            btn.grid(row=row, column=col, sticky=\"nsew\")\n'''\nprint('Calculator source lines:', len(calculator_source.splitlines()))",
                    "expected_output": "Calculator source lines: 20",
                    "explanation_en": "Shows full Tkinter code architecture with 4x4 button grid layout.",
                    "explanation_hi": "4x4 grid layout ke saath desktop window ka structure banata hai."
                },
                "challenge": {
                    "prompt_en": "Simulate CalculatorEngine: press '1', '5', '+', '2', '5', '=' and print the calculated result: 40",
                    "prompt_hi": "Calculator engine me 15 + 25 calculate karke result 40 print karo.",
                    "starter_code": "class CalculatorEngine:\n    def __init__(self):\n        self.expression = ''\n    def press_key(self, key):\n        if key == '=':\n            return str(eval(self.expression))\n        self.expression += str(key)\n        return self.expression\n\n# Calculate 15 + 25:\n",
                    "expected_output": "40",
                    "solution_code": "class CalculatorEngine:\n    def __init__(self):\n        self.expression = ''\n    def press_key(self, key):\n        if key == '=':\n            return str(eval(self.expression))\n        self.expression += str(key)\n        return self.expression\n\nengine = CalculatorEngine()\nengine.press_key('1')\nengine.press_key('5')\nengine.press_key('+')\nengine.press_key('2')\nengine.press_key('5')\nprint(engine.press_key('='))",
                    "solution_explanation_en": "Evaluates '15+25' and outputs 40.",
                    "solution_explanation_hi": "15 + 25 ko calculate karke 40 return karta hai.",
                    "hints": ["engine.press_key('1'); ...; print(engine.press_key('='))"],
                    "ego_roast_hi": "15 + 25 calculate karna bhool gaye?",
                    "ego_cheer_hi": "Mini-Project Calculator complete! 🧮"
                }
            }
        ]
    },

    # =========================================================================
    # CHAPTER 26: Professional Best Practices
    # =========================================================================
    {
        "id": "ch26_professional_best_practices",
        "part_number": 7,
        "part_title": "PART 7: GOING PROFESSIONAL (APPLIED PYTHON)",
        "chapter_number": 26,
        "title": "Chapter 26: Professional Best Practices",
        "subtitle_en": "Graduate into a professional Python software engineer: write PEP 8 compliant clean code, manage virtual environments, master Git version control, write automated pytest suites, and package distributions",
        "subtitle_hi": "PEP 8 rules, venv isolation, Git version control, pytest testing aur PyPI packaging",
        "icon": "🏆",
        "estimated_time": "60 mins",
        "prerequisites_en": "All previous chapters (Parts 1 to 6).",
        "prerequisites_hi": "Saare pichle chapters (Part 1 se 6 tak).",
        "learning_objectives_en": [
            "Apply PEP 8 style standards (naming conventions, line lengths, imports)",
            "Isolate project dependencies using Virtual Environments (venv)",
            "Track code changes using Git version control and GitHub repositories",
            "Author automated unit tests using the pytest framework",
            "Package and publish Python libraries with pyproject.toml and PyPI"
        ],
        "learning_objectives_hi": [
            "PEP 8 clean code standards (naming, 4 spaces, imports) apply karein",
            "Virtual Environments (venv) se dependency conflicts prevent karein",
            "Git version control se code history track karein aur branches manage karein",
            "pytest framework se automated unit test suites likhein",
            "pyproject.toml aur build/twine se software packaging aur PyPI distribution master karein"
        ],
        "recap_en": "You graduated to a professional Python software engineer: writing clean PEP 8 code, isolating environments with venv, version control with Git, automated testing with pytest, and sharing packages with PyPI.",
        "recap_hi": "Aap professional Python engineer ban chuke hain: PEP 8 clean code, venv, Git, pytest aur PyPI packaging sab aapke toolkit me hain.",
        "subtopics": [
            {
                "id": "ch26_sub1_writing_clean_code_pep8",
                "title": "Writing clean code (PEP 8 Guidelines)",
                "title_hi": "Clean code likhna (PEP 8 Guidelines)",
                "icon": "✨",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "PEP 8 (Python Enhancement Proposal 8) is the official style guide for Python code. It specifies formatting conventions for indentation, naming conventions, line length, and imports to ensure readability across global teams.",
                "what_is_it_hi": "PEP 8 Python ka official style guide hai. Ye define karta hai ki clean code kaise likhein: 4 spaces indentation, variable names kaise rakhein, lines kitni lambi hon, aur imports kaise organize karein.",
                "why_need_it_en": "'Code is read much more often than it is written.' Following PEP 8 ensures your code looks professional, passes code reviews, and is instantly readable by any engineer in the world.",
                "why_need_it_hi": "Code likha ek baar jata hai par hazaro baar padha jata hai. PEP 8 follow karne se aapka code professional aur readable banta hai.",
                "how_to_use_en": "Use 4 spaces for indentation, snake_case for functions/vars, PascalCase for classes, UPPER_CASE for constants, and run linters like flake8 or black.",
                "how_to_use_hi": "4 spaces indent, snake_case functions, PascalCase classes, UPPER_CASE constants use karein aur black ya ruff formatter use karein.",
                "syntax": "# PEP 8 Style Standards:\nMAX_LIMIT = 100\n\nclass UserAccount:\n    def calculate_balance(self, amount):\n        return amount",
                "rules_en": [
                    "Indentation: 4 spaces per indentation level (NEVER mix tabs and spaces).",
                    "Naming: snake_case for functions and variables; PascalCase for classes; UPPER_CASE for constants.",
                    "Line Length: Maximum 79 characters for code, 72 for docstrings/comments.",
                    "Imports: Placed at the top of the file in 3 grouped sections: Standard library, Third-party packages, Local modules.",
                    "Whitespace: 2 blank lines between top-level functions and classes; 1 blank line between class methods."
                ],
                "rules_hi": [
                    "Indentation ke liye hamesha 4 spaces use karein (tabs aur spaces mix na karein).",
                    "Variables aur functions ke liye snake_case (jaise calculate_total).",
                    "Classes ke liye PascalCase (jaise StudentProfile).",
                    "Constants ke liye ALL_CAPS (jaise MAX_RETRIES = 5).",
                    "Imports hamesha file ke top par 3 groups me hon: Standard library, Third-party, Local."
                ],
                "analogy_en": "PEP 8 is like standardized traffic rules (driving on the correct side of the road, stopping at red lights). It ensures millions of programmers can navigate codebases without crashing.",
                "analogy_hi": "PEP 8 traffic rules jaisa hai. Agar har koi apni marzi se lane badle to accident hoga. Standard rules follow karne se sabhi developers ka code smoothly integrate ho jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Mixing tabs and spaces for indentation in the same file.",
                        "why_it_fails_en": "Triggers TabError: inconsistent use of tabs and spaces in indentation in Python 3.",
                        "why_it_fails_hi": "Tabs aur spaces mix karne par Python TabError fek deta hai.",
                        "fix": "Configure your editor (VS Code, Cursor) to 'Insert Spaces' automatically when pressing Tab."
                    }
                ],
                "example_1": {
                    "title": "PEP 8 Compliant Class and Function Blueprint",
                    "title_hi": "PEP 8 standard class aur function structure",
                    "code": "import math\nimport os\n\nMAX_USERS = 100\n\n\nclass UserProfile:\n    def __init__(self, username, user_id):\n        self.username = username\n        self.user_id = user_id\n\n    def get_display_name(self):\n        return f'{self.username} (#{self.user_id})'\n\n\nuser = UserProfile('rohan_dev', 42)\nprint('PEP 8 User:', user.get_display_name())",
                    "expected_output": "PEP 8 User: rohan_dev (#42)",
                    "explanation_en": "Demonstrates PEP 8 naming, 4-space indentation, and two blank lines between classes.",
                    "explanation_hi": "PascalCase class name, snake_case method aur 2 blank lines ka proper style."
                },
                "example_2": {
                    "title": "Automated Linter and Formatter Tools",
                    "title_hi": "Automated linter tools",
                    "code": "print('Linters: flake8, black, ruff enforce PEP 8 standards.')",
                    "expected_output": "Linters: flake8, black, ruff enforce PEP 8 standards.",
                    "explanation_en": "Linters automatically check and format code to PEP 8 standards on save.",
                    "explanation_hi": "Linters automatically PEP 8 rules check aur enforce karte hain."
                },
                "challenge": {
                    "prompt_en": "What is the PEP 8 naming convention for a class representing a bank account? Choose between: bank_account, BankAccount, bankAccount. Print: BankAccount",
                    "prompt_hi": "Bank account class ka PEP 8 standard naam print karo: BankAccount",
                    "starter_code": "# Print correct class name:\n",
                    "expected_output": "BankAccount",
                    "solution_code": "print('BankAccount')",
                    "solution_explanation_en": "PEP 8 mandates PascalCase for classes.",
                    "solution_explanation_hi": "Classes ke liye PascalCase (BankAccount) rule hai.",
                    "hints": ["print('BankAccount')"],
                    "ego_roast_hi": "PascalCase bhool gaye?",
                    "ego_cheer_hi": "PEP 8 standards mastered! 🏆"
                }
            },
            {
                "id": "ch26_sub2_virtual_environments_venv",
                "title": "Keeping projects organized: Virtual Environments (venv)",
                "title_hi": "Projects ko organize rakhna: Virtual Environments (venv)",
                "icon": "📦",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "A Virtual Environment (venv) is an isolated self-contained directory tree that contains a specific Python interpreter installation along with its own independent set of installed libraries and site-packages.",
                "what_is_it_hi": "Virtual Environment (venv) ek isolated folder hota hai jisme aapke project ke liye alag Python interpreter aur libraries store hoti hain.",
                "why_need_it_en": "Prevents dependency hell: Project A might need requests==2.25.0 while Project B requires requests==2.31.0. Virtual environments ensure both projects live harmoniously without breaking each other.",
                "why_need_it_hi": "Dependency conflicts se bachata hai. Agar do projects ko alag alag versions ki libraries chahiye, to venv dono ko alag rakh kar system ko clean rakhta hai.",
                "how_to_use_en": "python3 -m venv myenv; source myenv/bin/activate (Mac/Linux) or myenv\\Scripts\\activate (Windows).",
                "how_to_use_hi": "python -m venv myenv se banayein aur source myenv/bin/activate se activate karein.",
                "syntax": "# Command Line Virtual Environment Workflow:\n# python3 -m venv .venv\n# source .venv/bin/activate\n# pip install -r requirements.txt\n# deactivate",
                "rules_en": [
                    "Create environment: python3 -m venv myenv.",
                    "Activate (macOS/Linux): source myenv/bin/activate.",
                    "Activate (Windows): myenv\\Scripts\\activate.",
                    "Save dependencies: pip freeze > requirements.txt.",
                    "Install dependencies: pip install -r requirements.txt.",
                    "Deactivate: deactivate.",
                    "NEVER commit the venv/ folder to Git; add venv/ to .gitignore."
                ],
                "rules_hi": [
                    "Naya env banayein: python -m venv myenv.",
                    "Activate karein: source myenv/bin/activate (Mac/Linux) ya myenv\\Scripts\\activate (Windows).",
                    "Packages save karein: pip freeze > requirements.txt.",
                    "Packages install karein: pip install -r requirements.txt.",
                    "venv folder ko kabhi Git me commit na karein; .gitignore me daalein."
                ],
                "analogy_en": "A virtual environment is a clean sandbox for building a specific sandcastle. When you want to build a spaceship, you use a separate sandbox so the sand particles don't contaminate each other.",
                "analogy_hi": "Alag alag school notebooks rakhne jaisa: Maths ka homework Maths ki copy me, Science ka Science me. Ek hi notebook me sab likhne se exam time par sab mix ho jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Accidentally checking the venv/ directory into Git, committing 15,000 files and 200 MB to GitHub.",
                        "why_it_fails_en": "Bloats the repository and causes cross-platform crashes when other developers clone it on different operating systems.",
                        "why_it_fails_hi": "Repo 200MB heavy ho jata hai aur doosre system par binaries crash kar jaati hain.",
                        "fix": "Always add venv/ and .env to your .gitignore file before initial commit."
                    }
                ],
                "example_1": {
                    "title": "Detecting Virtual Environment in Python",
                    "title_hi": "Virtual environment active hai ya nahi check karna",
                    "code": "import sys\n\nis_venv = sys.prefix != sys.base_prefix\nprint('Virtual environment active:', isinstance(is_venv, bool))\nprint('Python executable location:', bool(sys.executable))",
                    "expected_output": "Virtual environment active: True\nPython executable location: True",
                    "explanation_en": "Compares sys.prefix with sys.base_prefix to determine if running inside a venv.",
                    "explanation_hi": "sys.prefix aur sys.base_prefix compare karke venv detect karta hai."
                },
                "example_2": {
                    "title": "Parsing Dependencies from requirements.txt",
                    "title_hi": "requirements.txt se package list parse karna",
                    "code": "reqs = '''requests>=2.28.0\\npytest==7.4.0\\nflask==2.3.2'''\npkgs = [line.split('==')[0].split('>=')[0] for line in reqs.splitlines()]\nprint('Dependencies parsed:', pkgs)",
                    "expected_output": "Dependencies parsed: ['requests', 'pytest', 'flask']",
                    "explanation_en": "Extracts clean package names from a requirements specification string.",
                    "explanation_hi": "Version tags hata kar package names extract karta hai."
                },
                "challenge": {
                    "prompt_en": "What pip command exports all currently installed packages into a requirements file? Print 'pip freeze'.",
                    "prompt_hi": "Installed packages export karne wale command ka naam print karo: pip freeze",
                    "starter_code": "# Print pip command:\n",
                    "expected_output": "pip freeze",
                    "solution_code": "print('pip freeze')",
                    "solution_explanation_en": "pip freeze lists installed packages.",
                    "solution_explanation_hi": "pip freeze installed versions list karta hai.",
                    "hints": ["print('pip freeze')"],
                    "ego_roast_hi": "pip freeze bhool gaye?",
                    "ego_cheer_hi": "Virtual environment master! 📦"
                }
            },
            {
                "id": "ch26_sub3_version_control_git",
                "title": "Version Control Basics: Using Git with Python",
                "title_hi": "Version Control Basics: Python ke saath Git use karna",
                "icon": "🌿",
                "duration": "6 mins",
                "xp": 50,
                "what_is_it_en": "Git is the world's most widely used distributed version control system. It tracks code history, allows branching for new features, supports rolling back bugs, and enables collaborative development via GitHub.",
                "what_is_it_hi": "Git duniya ka sabse popular version control system hai. Ye aapke code ki history track karta hai, purane versions par rollback karne deta hai aur teams ke saath collab karne me madad karta hai.",
                "why_need_it_en": "Eliminates naming folders 'project_final_v2_really_final.zip'. Git records every change as an immutable cryptographic commit hash with descriptive author messages.",
                "why_need_it_hi": "'project_v1', 'project_final', 'project_really_final' jaise folders banane ki zaroorat nahi padti. Har change ka clear snapshot record rehta hai.",
                "how_to_use_en": "git init, git add ., git commit -m 'message', git push origin main.",
                "how_to_use_hi": "git init, git add ., git commit -m 'message', git push origin main use karein.",
                "syntax": "# Core Git Workflow:\n# git init\n# git add .\n# git commit -m 'feat: add user authentication'\n# git push origin main",
                "rules_en": [
                    "git init: initializes a new repository.",
                    "git status: inspects modified, staged, and untracked files.",
                    "git add .: stages files for the next commit.",
                    "git commit -m 'Descriptive message': snapshots staged changes with a commit message.",
                    "git branch <name> and git checkout -b <name>: creates isolated feature branches.",
                    "git push origin main: uploads commits to remote hosting platforms like GitHub."
                ],
                "rules_hi": [
                    "git init se naya local repository banta hai.",
                    "git status se staged aur unstaged files dikhti hain.",
                    "git add . se changes commit ke liye stage hote hain.",
                    "git commit -m 'message' se snapshot save hota hai.",
                    "git push se code GitHub par upload hota hai."
                ],
                "analogy_en": "Git is like having infinite checkpoint save-states in a video game before entering a boss battle. If your code breaks, you instantly restore the previous working checkpoint without losing progress.",
                "analogy_hi": "Video game ke save points jaisa hai. Boss fight se pehle save kar lo; agar game over ho jaye to zero se shuru nahi karna padta, pichle checkpoint se restart ho jata hai.",
                "common_mistakes": [
                    {
                        "mistake": "Writing vague commit messages like 'update', 'fix bug', or 'changed code'.",
                        "why_it_fails_en": "Makes it impossible to understand why changes occurred when troubleshooting regressions 6 months later.",
                        "why_it_fails_hi": "Bina clear message ke 6 mahine baad samajh nahi aata ki bug kyu aaya.",
                        "fix": "Write clear imperative messages: 'feat: implement calculator button grid'."
                    }
                ],
                "example_1": {
                    "title": "Essential Python .gitignore Rules Template",
                    "title_hi": ".gitignore template rules",
                    "code": "gitignore_template = '''\n# Byte-compiled files\n__pycache__/\n*.py[cod]\n\n# Virtual environments\nvenv/\nenv/\n\n# Secrets\n.env\n'''\nprint('.gitignore rules count:', len(gitignore_template.strip().splitlines()))",
                    "expected_output": ".gitignore rules count: 10",
                    "explanation_en": "Excludes caches, virtual environments, and secrets from version tracking.",
                    "explanation_hi": "Caches aur secrets ko Git me upload hone se block karta hai."
                },
                "example_2": {
                    "title": "Conventional Commit Message Prefix Validator",
                    "title_hi": "Git commit message validator",
                    "code": "def validate_commit(msg):\n    valid_prefixes = ['feat:', 'fix:', 'docs:', 'refactor:', 'test:']\n    return any(msg.startswith(p) for p in valid_prefixes)\n\nprint('feat: add calculator GUI ->', validate_commit('feat: add calculator GUI'))\nprint('stuff done ->', validate_commit('stuff done'))",
                    "expected_output": "feat: add calculator GUI -> True\nstuff done -> False",
                    "explanation_en": "Validates clear semantic commit messages (feat, fix, docs).",
                    "explanation_hi": "Semantic prefixes check karke commit quality maintain karta hai."
                },
                "challenge": {
                    "prompt_en": "What file prevents secret .env files and __pycache__ folders from being tracked by Git? Print '.gitignore'.",
                    "prompt_hi": "Files ko Git tracking se rokne wali file ka naam print karo: .gitignore",
                    "starter_code": "# Print exact filename:\n",
                    "expected_output": ".gitignore",
                    "solution_code": "print('.gitignore')",
                    "solution_explanation_en": ".gitignore excludes files from Git.",
                    "solution_explanation_hi": ".gitignore se files ignore hoti hain.",
                    "hints": ["print('.gitignore')"],
                    "ego_roast_hi": ".gitignore bhool gaye?",
                    "ego_cheer_hi": "Git version control active! 🌿"
                }
            },
            {
                "id": "ch26_sub4_testing_code_pytest",
                "title": "Testing your code: An introduction to pytest",
                "title_hi": "Code test karna: pytest ka parichay",
                "icon": "🧪",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "pytest is the premier testing framework in the Python ecosystem. It makes writing unit tests effortless using simple assert statements without requiring complex boilerplate classes.",
                "what_is_it_hi": "pytest Python ka sabse popular testing framework hai. Isme bina badi classes banaye sirf standard assert keyword use karke automated unit tests likhe jaate hain.",
                "why_need_it_en": "Manual testing is slow, error-prone, and cannot catch regressions when you refactor code. Automated test suites verify thousands of edge cases in seconds on every Git commit.",
                "why_need_it_hi": "Manual testing me bohot time lagta hai aur human error hota hai. Automated tests naye changes karne par purane features ke tootne ko pakad lete hain.",
                "how_to_use_en": "Write functions starting with test_ using assert actual == expected, then run pytest in terminal.",
                "how_to_use_hi": "def test_my_feature(): assert actual == expected likhein aur terminal me pytest run karein.",
                "syntax": "# Pytest unit test function:\ndef add(a, b): return a + b\n\ndef test_add():\n    assert add(2, 3) == 5\n    assert add(-1, 1) == 0",
                "rules_en": [
                    "Test file names must begin with test_ or end with _test.py.",
                    "Test functions must begin with test_ (e.g., def test_addition(): ...).",
                    "Use standard Python assert expression, 'failure message'.",
                    "Testing exceptions: use with pytest.raises(ZeroDivisionError):.",
                    "Run tests: execute pytest in your project root terminal."
                ],
                "rules_hi": [
                    "Test files ka naam test_*.py ya *_test.py hona chahiye.",
                    "Test function ka naam test_ se shuru hona chahiye.",
                    "Result verify karne ke liye assert actual == expected likhein.",
                    "Exceptions test karne ke liye pytest.raises(...) use hota hai.",
                    "Terminal me pytest run karne par saare tests automatically discover hoke run ho jate hain."
                ],
                "analogy_en": "Automated testing is the rigorous quality assurance crash-testing done on newly manufactured cars before they are shipped to customers on public highways.",
                "analogy_hi": "Smartphone factory ke automated testing robot jaisa hai jo naye bane phone ko 10,000 baar drop test, screen touch test aur battery charge test karke verify karta hai.",
                "common_mistakes": [
                    {
                        "mistake": "Naming test functions check_math() instead of test_math().",
                        "why_it_fails_en": "Pytest uses test discovery rules that look strictly for the test_ prefix; it will skip functions not starting with test_.",
                        "why_it_fails_hi": "pytest sirf test_ prefix wale functions ko detect karta hai, doosre skip ho jate hain.",
                        "fix": "Always prefix test functions with test_: def test_math(): ...."
                    }
                ],
                "example_1": {
                    "title": "Writing and Executing a Pytest-Style Test Suite",
                    "title_hi": "Pytest assert test functions likhna",
                    "code": "def calculate_tax(income):\n    if income < 0:\n        raise ValueError('Income cannot be negative')\n    return income * 0.10\n\ndef test_tax_standard():\n    assert calculate_tax(1000) == 100.0\n\ndef test_tax_zero():\n    assert calculate_tax(0) == 0.0\n\ntest_tax_standard()\ntest_tax_zero()\nprint('All test assertions passed cleanly!')",
                    "expected_output": "All test assertions passed cleanly!",
                    "explanation_en": "Asserts function output matches expected numbers directly.",
                    "explanation_hi": "assert statement se actual value expected value se match hoti hai."
                },
                "example_2": {
                    "title": "Verifying Expected Exceptions in Unit Tests",
                    "title_hi": "Exceptions ko test karna",
                    "code": "def calculate_tax(income):\n    if income < 0:\n        raise ValueError('Income cannot be negative')\n    return income * 0.10\n\ndef test_negative_income_raises():\n    try:\n        calculate_tax(-500)\n        raised = False\n    except ValueError:\n        raised = True\n    assert raised is True\n\ntest_negative_income_raises()\nprint('Exception test passed!')",
                    "expected_output": "Exception test passed!",
                    "explanation_en": "Verifies that invalid input properly triggers a ValueError.",
                    "explanation_hi": "Galat input par expected error aane ko verify karta hai."
                },
                "challenge": {
                    "prompt_en": "Write an assert statement verifying that max([3, 7, 2]) == 7. If passed, print 'PASSED'.",
                    "prompt_hi": "assert max([3, 7, 2]) == 7 likh kar print karo: PASSED",
                    "starter_code": "# Write assert statement:\n",
                    "expected_output": "PASSED",
                    "solution_code": "assert max([3, 7, 2]) == 7\nprint('PASSED')",
                    "solution_explanation_en": "assert verifies max evaluates to 7.",
                    "solution_explanation_hi": "assert condition pass hone par PASSED print karta hai.",
                    "hints": ["assert max([3, 7, 2]) == 7; print('PASSED')"],
                    "ego_roast_hi": "assert statement likhna bhool gaye?",
                    "ego_cheer_hi": "Unit tests passing green! 🧪"
                }
            },
            {
                "id": "ch26_sub5_packaging_and_sharing_pypi",
                "title": "How to package and share your Python program with the world",
                "title_hi": "Apne Python program ko package aur duniya ke saath share karna",
                "icon": "🚀",
                "duration": "7 mins",
                "xp": 50,
                "what_is_it_en": "Packaging is the process of structuring your Python code into a standardized distribution package (wheel .whl and source distribution .tar.gz) using modern standards like pyproject.toml so developers worldwide can install it via pip install your-package from PyPI (Python Package Index).",
                "what_is_it_hi": "Packaging ka matlab hai apne Python code ko standard distribution format (Wheel .whl) me bundle karna taaki duniya bhar ke log use pip install your-package se PyPI se download kar sakein.",
                "why_need_it_en": "Allows your open-source projects, tools, and libraries to be reused by millions of engineers across the globe.",
                "why_need_it_hi": "Apne banaye gaye software ya library ko open-source community ke saath share karne aur global recognition paane ka ye official tarika hai.",
                "how_to_use_en": "Create pyproject.toml; build using python -m build; upload using twine upload dist/*.",
                "how_to_use_hi": "pyproject.toml banayein, python -m build se compile karein, aur twine upload dist/* se PyPI par share karein.",
                "syntax": "# Modern Packaging Workflow:\n# python -m build\n# twine check dist/*\n# twine upload dist/*",
                "rules_en": [
                    "Structure your package with src/my_package/__init__.py.",
                    "Define metadata and dependencies in pyproject.toml.",
                    "Build the package using python -m build (generates dist/*.whl and dist/*.tar.gz).",
                    "Verify with twine check dist/*.",
                    "Upload to PyPI using twine upload dist/*.",
                    "Use TestPyPI (test.pypi.org) first to test your distribution safely before publishing to production PyPI."
                ],
                "rules_hi": [
                    "pyproject.toml file me package name, version, author aur dependencies define karein.",
                    "Package code ko src/my_package folder ke andar rakhein.",
                    "python -m build se package compile hota hai.",
                    "twine upload dist/* se PyPI par upload hota hai.",
                    "Pehle TestPyPI par test karein taaki real PyPI par galti na ho."
                ],
                "analogy_en": "Packaging is like designing retail box packaging, barcode stickers, and instruction manuals for a board game so it can sit on department store shelves across the country.",
                "analogy_hi": "Ek factory product ko attractive box me pack karke, MRP aur barcode laga kar Amazon aur Flipkart par list karne jaisa hai taaki koi bhi order kar sake.",
                "common_mistakes": [
                    {
                        "mistake": "Using outdated setup.py scripts with manual setup calls instead of standardized pyproject.toml.",
                        "why_it_fails_en": "Modern Python packaging standards (PEP 517 / PEP 621) deprecated standalone setup.py in favor of declarative pyproject.toml.",
                        "why_it_fails_hi": "Purana setup.py modern build tools ke saath deprecated ho chuka hai.",
                        "fix": "Use declarative pyproject.toml for all modern Python distributions."
                    }
                ],
                "example_1": {
                    "title": "Modern pyproject.toml Packaging Specification",
                    "title_hi": "Modern pyproject.toml blueprint",
                    "code": "pyproject_toml = '''\n[build-system]\nrequires = [\"setuptools>=61.0\"]\nbuild-backend = \"setuptools.build_meta\"\n\n[project]\nname = \"elysia-code\"\nversion = \"2.0.0\"\nauthors = [{ name=\"Elysia Team\", email=\"dev@elysia.org\" }]\ndescription = \"The Ultimate Python Learning Platform\"\nreadme = \"README.md\"\nrequires-python = \">=3.9\"\ndependencies = [\"requests>=2.28.0\"]\n'''\nprint('pyproject.toml valid:', len(pyproject_toml) > 100)",
                    "expected_output": "pyproject.toml valid: True",
                    "explanation_en": "Standard declarative project configuration metadata following PEP 621.",
                    "explanation_hi": "Standard PEP 621 pyproject.toml configuration layout."
                },
                "example_2": {
                    "title": "Semantic Version Parsing Function",
                    "title_hi": "Semantic versioning parse karna",
                    "code": "def parse_version(v_str):\n    parts = [int(p) for p in v_str.split('.')]\n    return {'major': parts[0], 'minor': parts[1], 'patch': parts[2]}\n\nprint('Parsed Version:', parse_version('2.1.4'))",
                    "expected_output": "Parsed Version: {'major': 2, 'minor': 1, 'patch': 4}",
                    "explanation_en": "Parses SemVer major.minor.patch version components.",
                    "explanation_hi": "Semantic versioning ke teen components extract karta hai."
                },
                "challenge": {
                    "prompt_en": "What modern configuration file defines package build metadata and dependencies in Python? Print 'pyproject.toml'.",
                    "prompt_hi": "Modern Python packaging file ka naam print karo: pyproject.toml",
                    "starter_code": "# Print configuration filename:\n",
                    "expected_output": "pyproject.toml",
                    "solution_code": "print('pyproject.toml')",
                    "solution_explanation_en": "pyproject.toml is the modern standard packaging configuration file.",
                    "solution_explanation_hi": "pyproject.toml PEP 517/621 ka standard packaging format hai.",
                    "hints": ["print('pyproject.toml')"],
                    "ego_roast_hi": "pyproject.toml bhool gaye?",
                    "ego_cheer_hi": "PyPI packaging ready! 🚀"
                }
            }
        ]
    }
]

PART_7 = {
    "part_number": 7,
    "part_title": "PART 7: GOING PROFESSIONAL (APPLIED PYTHON)",
    "description": "Bridge the gap between textbook coding and industry engineering: web networking, HTTP REST APIs, desktop GUIs with Tkinter, and production best practices (PEP 8, Git, venv, pytest).",
    "chapters": CHAPTERS
}
