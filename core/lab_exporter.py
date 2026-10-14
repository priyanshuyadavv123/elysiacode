"""
=============================================================================
✨ ELYSIA SCHOOL: COLLEGE LAB RECORD EXPORTER (lab_exporter.py)
=============================================================================
📌 KYA KAAM HAI IS FILE KA (WHAT IT DOES):
  Ye script college engineering/BCA/BSc practical lab file generate karti hai.
  Student ke naam, roll number, experiment number, Aim, Algorithm, Code, 
  aur Viva Q&A ko standard university practical format me format karti hai.

👁️ WEB PAGE PE KYA DIKHTA HAI:
  A4 page size me black-and-white official printable lab sheet (jisme Header,
  Student Table, Code Box, Output Box, aur Teacher Signature Box hota hai).
  Browser me Ctrl+P dabane par seedha PDF save ho sakti hai.

💡 KYUN USE KIYA (WHY WE USE THIS):
  Students ko practical file likhne me hafte lagte hain. HTML + CSS `@page { size: A4 }` 
  use karke hum bina kisi heavy PDF library (jaise ReportLab ya WeasyPrint) ke
  pure Python standard library se 100% accurate printable file bana lete hain!

⚠️ AGAR ISKO CHANGE YA DELETE KAREIN TO:
  "Generate Lab Sheet" button fail ho jayega aur student ko printable practical file nahi milegi.
=============================================================================
"""

import html as _html
from typing import Dict, Any


def _t(value, limit=2000):
    """Turn any value into SAFE text for HTML: converts to str, limits length, escapes < > & quotes.
    Without this a student could paste <script> into the code box and run it in the lab-sheet window."""
    return _html.escape(str(value if value is not None else "")[:limit], quote=True)


def generate_lab_record_html(
    student_name: str,
    roll_no: str,
    course_code: str,
    exp_no: int,
    title: str,
    aim: str,
    algorithm: list,
    code: str,
    sample_output: str,
    viva_qa: list
) -> str:
    """
    📌 GENERATE LAB RECORD HTML:
    Saari details lekar clean, printable A4 HTML document return karta hai.
    """
    student_name, roll_no, course_code = _t(student_name, 80), _t(roll_no, 40), _t(course_code, 40)
    title, aim = _t(title, 120), _t(aim, 600)
    try:
        exp_no = max(1, min(999, int(exp_no)))
    except (TypeError, ValueError):
        exp_no = 1
    code = _t(code, 20000)
    sample_output = _t(sample_output, 5000)
    algorithm = algorithm if isinstance(algorithm, (list, tuple)) else []
    viva_qa = [v for v in (viva_qa if isinstance(viva_qa, (list, tuple)) else []) if isinstance(v, dict)]

    algo_lis = "".join([f"<li>{_t(step, 400)}</li>" for step in list(algorithm)[:30]])
    
    viva_html = "".join([
        f"""
        <div class="viva-item">
            <p class="viva-q"><strong>Q{idx+1}:</strong> {_t(item.get('q', item.get('question', '')), 600)}</p>
            <p class="viva-a"><strong>Ans:</strong> {_t(item.get('a', item.get('answer_en', '')), 1200)}</p>
        </div>
        """
        for idx, item in enumerate(viva_qa[:30])
    ])

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Lab Practical Record - Exp {exp_no}: {title}</title>
    <style>
        @page {{
            size: A4;
            margin: 15mm 20mm;
        }}
        body {{
            font-family: 'Times New Roman', Times, serif;
            color: #111;
            background: #fff;
            line-height: 1.5;
            margin: 0;
            padding: 20px;
        }}
        .header-box {{
            border: 2px solid #000;
            padding: 12px 18px;
            margin-bottom: 20px;
        }}
        .univ-title {{
            text-align: center;
            font-size: 18pt;
            font-weight: bold;
            text-transform: uppercase;
            margin: 0;
        }}
        .sub-header {{
            text-align: center;
            font-size: 12pt;
            margin-top: 4px;
            margin-bottom: 12px;
            font-style: italic;
        }}
        .meta-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            font-size: 11pt;
            row-gap: 6px;
            border-top: 1px solid #000;
            padding-top: 8px;
        }}
        .section-heading {{
            font-size: 13pt;
            font-weight: bold;
            text-decoration: underline;
            text-transform: uppercase;
            margin-top: 18px;
            margin-bottom: 6px;
        }}
        p, li {{
            font-size: 11pt;
            margin: 4px 0;
        }}
        ol {{
            margin-top: 4px;
            padding-left: 24px;
        }}
        pre.code-block {{
            background: #f8f9fa;
            border: 1px solid #ccc;
            padding: 12px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 10pt;
            white-space: pre-wrap;
            margin: 8px 0;
        }}
        .output-block {{
            background: #000;
            color: #0f0;
            padding: 10px;
            font-family: 'Courier New', Courier, monospace;
            font-size: 10pt;
            border-radius: 4px;
            margin: 8px 0;
        }}
        .viva-item {{
            margin-bottom: 8px;
            font-size: 10.5pt;
        }}
        .viva-q {{
            color: #900;
            margin: 2px 0;
        }}
        .viva-a {{
            color: #000;
            margin: 2px 0;
        }}
        .signature-table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 30px;
            font-size: 11pt;
        }}
        .signature-table td {{
            border: 1px solid #000;
            padding: 10px;
            text-align: center;
            vertical-align: bottom;
            height: 60px;
        }}
        @media print {{
            body {{ padding: 0; }}
            .no-print {{ display: none; }}
        }}
    </style>
</head>
<body>
    <div class="no-print" style="text-align: right; margin-bottom: 15px;">
        <button onclick="window.print()" style="background: #2563eb; color: #fff; border: none; padding: 10px 20px; font-weight: bold; border-radius: 6px; cursor: pointer;">🖨️ Print / Save as PDF</button>
    </div>

    <div class="header-box">
        <div class="univ-title">ELYSIA SCHOOL OF COMPUTER SCIENCE</div>
        <div class="sub-header">Department of Computer Science & Engineering • Laboratory Practical Record File</div>
        <div class="meta-grid">
            <div><strong>Student Name:</strong> {student_name}</div>
            <div><strong>Course Code:</strong> {course_code}</div>
            <div><strong>Roll Number:</strong> {roll_no}</div>
            <div><strong>Experiment No:</strong> {exp_no}</div>
        </div>
    </div>

    <div class="section-heading">Experiment Title: {title}</div>

    <div class="section-heading">1. Aim of the Experiment</div>
    <p>{aim}</p>

    <div class="section-heading">2. Algorithm / Flow of Execution</div>
    <ol>
        {algo_lis}
    </ol>

    <div class="section-heading">3. Program Source Code</div>
    <pre class="code-block">{code}</pre>

    <div class="section-heading">4. Sample Output</div>
    <div class="output-block">{sample_output}</div>

    <div class="section-heading">5. Viva-Voce Questions</div>
    {viva_html}

    <table class="signature-table">
        <tr>
            <td style="width: 25%;">Marks Awarded (Out of 10)</td>
            <td style="width: 25%;">Date of Submission</td>
            <td style="width: 25%;">Faculty Signature</td>
            <td style="width: 25%;">Lab Incharge Seal</td>
        </tr>
    </table>
</body>
</html>
"""
