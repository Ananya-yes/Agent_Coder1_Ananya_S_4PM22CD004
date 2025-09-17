readme.md best file ok  # 🤖 Agent-as-Coder: Bank Statement Parser Generator

An intelligent AI agent that **automatically creates custom parsers** for any bank statement PDF. Just give it a PDF, and it will generate working Python code that extracts your transaction data perfectly!

## 🎬 See It In Action

📹 **Demo Video**: [Watch the Agent in Action](demo vedio.mp4)

*See how the agent analyzes your PDF, generates custom code, and parses transactions automatically!*

## 🚀 Quick Start (3 Simple Steps)

### Step 1: Install Requirements
```bash
cd /Users/abidhussains/Desktop/Agent_Coder_AS
pip install -r requirements.txt
```

### Step 2: Set Up Your API Key
Create a `.env` file in the project folder:
```bash
echo "GEMINI_API_KEY=your_api_key_here" > .env
```

### Step 3: Generate Your Parser (The Magic Happens Here!)
```bash

python3 agent.py --target mybank --pdf "path/to/your/statement.pdf" --auto-csv


python3 agent.py --target mybank --pdf "your_statement.pdf" --csv "expected_format.csv"
```

**That's it!** The agent will:
- 🧠 Analyze your PDF structure intelligently
- 💻 Generate custom Python parser code
- 🧪 Test the parser automatically (8 comprehensive tests)
- 📊 Parse your PDF and save results
- 📋 Generate detailed quality reports

## 🎯 Using Your Generated Parser

Once the agent creates your parser, use it anytime:

```bash
# Parse any PDF from the same bank
python3 agent.py --parse "new_statement.pdf" --bank mybank --output "results.csv"

# Quick parse (results display in terminal)
python3 agent.py --parse "statement.pdf" --bank mybank

# See all available parsers
python3 agent.py --list-parsers
```

## 🤖 How the AI Agent Works

Our agent follows a **smart autonomous process**:

```
📝 PLAN        🛠️ GENERATE      🧪 TEST         🔧 REFINE
┌─────────┐    ┌───────────┐    ┌──────────┐    ┌─────────┐
│ Analyze │ -> │ Create    │ -> │ Run 8    │ -> │ Learn & │
│ PDF     │    │ Python    │    │ Tests    │    │ Improve │
│ Structure│    │ Parser    │    │ Validate │    │ Code    │
│ Devise  │    │ Code      │    │ Results  │    │         │
│ Strategy│    │ with AI   │    │          │    │         │
└─────────┘    └───────────┘    └──────────┘    └─────────┘
                                                     │
                     ┌─────────────────────────────┘
                     │
                     ▼
              ┌─────────────┐
              │ 🧠 MEMORY   │
              │             │
              │ Learns from │
              │ mistakes &  │
              │ successes   │
              └─────────────┘
```

The agent **never gives up** – it keeps trying until it creates a working parser (max 5 attempts)!

## 🧪 Comprehensive Testing (8 Test Cases)

Every generated parser goes through rigorous testing:

✅ **Test 1**: Import & Instantiation Test  
✅ **Test 2**: PDF Parsing Functionality  
✅ **Test 3**: Data Structure Validation  
✅ **Test 4**: Transaction Count Accuracy  
✅ **Test 5**: Data Quality Assessment  
✅ **Test 6**: Column Schema Compliance  
✅ **Test 7**: File Save Functionality  
✅ **Test 8**: Error Handling & Edge Cases  

**Result**: 📈 Detailed test report with quality scores and recommendations

## 📋 What You Get

After running the agent, you'll have:

```
📁 your_project/
├── 💻 custom_parsers/
│   └── mybank_parser.py      # ⭐ Your custom parser!
├── 📂 data/
│   └── mybank/
│       ├── mybank_sample.pdf
│       ├── mybank_FINAL_RESULTS_[timestamp].csv
│       └── mybank_TEST_REPORT_[timestamp].json
└── 📈 parsed_data/
    └── mybank/
        └── session_[timestamp]/  # 📈 Detailed logs & reports
```

## 📊 Data Format

All parsers return data in this **standardized format**:

| Column      | Description           | Example           |
|-------------|----------------------|-------------------|
| `date`      | Transaction date     | `2023-10-06`      |
| `description` | Transaction details | `UPI Payment`     |
| `debit`     | Money going out      | `120.00` or `""` |
| `credit`    | Money coming in      | `500.00` or `""` |
| `balance`   | Account balance      | `15415.00`        |

**Note**: Each transaction has **either** debit **or** credit, never both!

## 💻 Example Commands & Use Cases

### For Different Banks:
```bash
# Indian Banks
python3 agent.py --target icici --pdf "icici_statement.pdf" --auto-csv
python3 agent.py --target sbi --pdf "sbi_statement.pdf" --auto-csv
python3 agent.py --target hdfc --pdf "hdfc_statement.pdf" --auto-csv

# International Banks
python3 agent.py --target chase --pdf "chase_statement.pdf" --auto-csv
python3 agent.py --target wells_fargo --pdf "wells_statement.pdf" --auto-csv

# Custom Bank Names
python3 agent.py --target mylocal_bank --pdf "statement.pdf" --auto-csv
```

### Advanced Usage:
```bash
# Interactive mode (guided setup)
python3 agent.py

# With sample CSV for perfect formatting
python3 agent.py --target mybank --pdf "statement.pdf" --csv "expected_format.csv"

# Quick parsing
python3 agent.py --parse "new_statement.pdf" --bank mybank

# Save to specific location
python3 agent.py --parse "statement.pdf" --bank mybank --output "/path/to/results.csv"

# Check what parsers you have
python3 agent.py --list-parsers
```

## 🔧 Troubleshooting

**Parser not working?** The agent learns from mistakes:
- It will try up to 5 times to get it right
- Each attempt gets smarter based on previous errors
- Check the session logs in `parsed_data/[bank]/session_[timestamp]/`

**Need better results?** Provide a sample CSV:
- Create a small CSV showing exactly how you want the output formatted
- Use `--csv` parameter instead of `--auto-csv`

**Different PDF format?** No problem:
- The agent analyzes each PDF's unique structure
- It adapts to different banks automatically
- Works with various date formats and layouts

## 🌟 Features

✅ **Smart PDF Analysis**: Understands any bank statement format  
✅ **Auto-Generated Code**: Creates custom Python parsers automatically  
✅ **Comprehensive Testing**: 8-point validation system  
✅ **Error Learning**: Gets smarter with each attempt  
✅ **Data Quality Reports**: Detailed analysis and recommendations  
✅ **Session Tracking**: Complete audit trail of all operations  
✅ **Multi-Bank Support**: Works with any bank worldwide  
✅ **Human-Readable Output**: Clean, standardized data format  

---

**Ready to try it?** Just run:
```bash
python3 agent.py --target mybank --pdf "your_statement.pdf" --auto-csv
```

The agent will do the rest! 🤖✨.   see remove comments from here  folloow this only 
