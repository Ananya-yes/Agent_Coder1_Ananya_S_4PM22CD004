🤖 Agent-as-Coder: Smart Bank Statement Parser

Tired of manually cleaning messy bank statements?
Meet Agent-as-Coder — your AI buddy that automatically builds a custom parser for any bank statement PDF. Just drop in a statement, and it gives you structured, ready-to-use transaction data.

🚀 Why You’ll Love It

Zero manual coding → Agent writes the parser for you

Works with any bank (India or abroad)

Smart & adaptive → learns from mistakes in real-time

Clean CSV output → ready for analysis or reporting

🎬 Demo

📹 [Watch it in action](demo vedio.mp4)

⚡ Quick Start
1️⃣ Install Requirements
cd /Users/abidhussains/Desktop/Agent_Coder_AS
pip install -r requirements.txt

2️⃣ Add Your API Key

Create a .env file:

echo "GEMINI_API_KEY=your_api_key_here" > .env

3️⃣ Run the Agent
# Auto-generate a parser & CSV
python3 agent.py --target mybank --pdf "statement.pdf" --auto-csv

# Or guide the format with your own CSV
python3 agent.py --target mybank --pdf "statement.pdf" --csv "expected_format.csv"

🎯 Use Your Parser
# Parse new statements
python3 agent.py --parse "new_statement.pdf" --bank mybank --output "results.csv"

# Quick parse (terminal only)
python3 agent.py --parse "statement.pdf" --bank mybank

# See all available parsers
python3 agent.py --list-parsers

🧪 What’s Under the Hood

The agent goes through a smart loop:

🔍 Analyze your PDF

🛠️ Generate Python parser code

✅ Run 8 validation tests

🔧 Fix mistakes automatically

🧠 Remember what worked

It keeps trying until you get a working parser (up to 5 attempts).

📂 Project Structure
📁 project/
├── custom_parsers/         # Your generated parsers
├── data/                   # PDFs, results & reports
└── parsed_data/            # Session logs & analysis

📊 Standard Output Format
Column	Description	Example
date	Transaction date	2023-10-06
description	Transaction details	UPI Payment
debit	Money out	120.00
credit	Money in	500.00
balance	Running balance	15415.00
🌟 Features

✅ Works with any bank PDF
✅ Auto-generated Python code
✅ 8-step validation system
✅ Learns from errors
✅ Standardized clean CSV output
✅ Detailed logs & reports

💡 Pro Tip: For best results, provide a sample CSV with the exact format you want.

✨ Ready to stop wrestling with PDFs? Just run:

python3 agent.py --target mybank --pdf "your_statement.pdf" --auto-csv


And let the agent do the heavy lifting.
