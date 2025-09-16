# 🤖 Agent-as-Coder: Bank Statement Parser Generator

An intelligent coding agent that generates custom parsers for bank statement PDFs using true agent paradigm (plan → call tools → observe → refine).

## 🚀 5-Step Setup & Usage

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Set API Key
Create a `.env` file in project root:
```
GROQ_API_KEY=your_groq_api_key_here
```

### Step 3: Prepare Sample Data
Place your bank PDF and expected CSV in `data/[bank_name]/`:
```
data/
  icici/
    icici_sample.pdf    # Your bank statement PDF
    icici_sample.csv    # Expected output format
```

### Step 4: Generate Parser
Create a custom parser for any bank:
```bash
python agent.py --target icici --pdf "path/to/your/statement.pdf"
```

### Step 5: Parse PDFs
Use the generated parser on any PDF:
```bash
python agent.py --parse "statement.pdf" --bank icici --output "results.csv"
```

## 🧠 Agent Architecture

The agent follows a **true agent paradigm** with self-improvement loops:

```
┌─────────────┐    ┌──────────────┐    ┌─────────────┐    ┌─────────────┐
│    PLAN     │ -> │ CALL TOOLS   │ -> │   OBSERVE   │ -> │   REFINE    │
│             │    │              │    │             │    │             │
│ • Analyze   │    │ • Generate   │    │ • Test      │    │ • Learn     │
│   PDF       │    │   Code       │    │   Parser    │    │   from      │
│ • Devise    │    │ • Write      │    │ • Validate  │    │   Errors    │
│   Strategy  │    │   to File    │    │   Output    │    │ • Improve   │
│             │    │ • Run Tests  │    │ • Compare   │    │   Next      │
│             │    │              │    │   Results   │    │   Cycle     │
└─────────────┘    └──────────────┘    └─────────────┘    └─────────────┘
                                                                   │
                                                                   │
                   ┌─────────────────────────────────────────────┘
                   │
                   ▼
              ┌─────────────┐
              │   MEMORY    │
              │             │
              │ • Failed    │
              │   Attempts  │
              │ • Success   │
              │   Patterns  │
              │ • Learning  │
              └─────────────┘
```

The agent maintains **short-term memory** and runs **≤3 correction cycles** until success, generating genuinely human-like code that doesn't look bot-created.

## 📊 Parser Contract

All generated parsers implement:
```python
def parse(pdf_path: str) -> pd.DataFrame:
    # Returns DataFrame with columns: ['date', 'description', 'debit', 'credit', 'balance']
```

## 💡 Additional Commands

```bash
# List available parsers
python agent.py --list-parsers

# Create parser for different banks
python agent.py --target sbi --pdf "sbi_statement.pdf"
python agent.py --target hdfc --pdf "hdfc_statement.pdf"

# Parse without saving to file
python agent.py --parse "statement.pdf" --bank icici
```

## 🎯 Core Features

- ✅ **T1**: Agent loop with plan → generate → test → self-fix (≤3 attempts)
- ✅ **T2**: CLI command creates custom parser from PDF & CSV samples  
- ✅ **T3**: Parser contract returns standardized DataFrame
- ✅ **T4**: Automated testing with DataFrame.equals validation
- ✅ **T5**: Complete documentation with agent architecture diagram

The agent generates **human-like code** with natural variable names, thoughtful comments, and robust error handling - not robotic patterns that look AI-generated.