#!/usr/bin/env python3
import pytest
import pandas as pd
from pathlib import Path
import sys

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from agent import BankParserAgent, load_api_key


class TestBankParserAgent:
    """Test suite for production-ready agent"""
    
    @pytest.fixture
    def agent(self):
        """Create agent instance with API key"""
        try:
            api_key = load_api_key()
            return BankParserAgent(api_key)
        except ValueError:
            pytest.skip("GROQ_API_KEY not found")
    
    def test_agent_initialization(self, agent):
        """Test agent can be initialized properly"""
        assert agent is not None
        assert agent.client is not None
        assert agent.project_root.exists()
    
    def test_parser_contract_compliance(self):
        """Test that generated parsers follow the contract: parse(pdf_path) -> pd.DataFrame"""
        # This will be tested after parser generation
        project_root = Path(__file__).parent.parent
        custom_parsers_dir = project_root / "custom_parsers"
        
        if custom_parsers_dir.exists():
            parser_files = list(custom_parsers_dir.glob("*_parser.py"))
            
            for parser_file in parser_files:
                # Import parser module
                import importlib.util
                spec = importlib.util.spec_from_file_location(
                    parser_file.stem, parser_file
                )
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                # Find parser class
                bank_name = parser_file.stem.replace('_parser', '').upper()
                parser_class = getattr(module, f"{bank_name}Parser")
                
                # Test parser contract
                parser = parser_class()
                assert hasattr(parser, 'parse'), f"{bank_name}Parser missing parse method"
                
                # Test method signature (should accept pdf_path and return DataFrame)
                import inspect
                sig = inspect.signature(parser.parse)
                assert 'pdf_path' in sig.parameters, f"{bank_name}Parser.parse missing pdf_path parameter"
    
    def test_dataframe_schema_compliance(self):
        """Test that parsers return DataFrame with correct schema"""
        project_root = Path(__file__).parent.parent
        data_dir = project_root / "data"
        
        if data_dir.exists():
            for bank_dir in data_dir.iterdir():
                if bank_dir.is_dir():
                    csv_file = bank_dir / f"{bank_dir.name}_sample.csv"
                    if csv_file.exists():
                        df = pd.read_csv(csv_file)
                        
                        # Test required columns
                        required_cols = ['date', 'description', 'debit', 'credit', 'balance']
                        assert list(df.columns) == required_cols, f"Schema mismatch in {csv_file}"
                        
                        # Test data types
                        assert not df.empty, f"Empty DataFrame in {csv_file}"
    
    def test_agent_autonomy_loop(self, agent):
        """Test that agent follows PLAN → GENERATE → TEST → REFINE loop"""
        # Test that agent has required methods for autonomy
        assert hasattr(agent, '_plan_phase'), "Agent missing _plan_phase method"
        assert hasattr(agent, '_generate_phase'), "Agent missing _generate_phase method"
        assert hasattr(agent, '_test_phase'), "Agent missing _test_phase method"
        assert hasattr(agent, '_refine_phase'), "Agent missing _refine_phase method"
        
        # Test that agent has memory for self-improvement
        assert hasattr(agent, 'memory'), "Agent missing memory attribute"
        assert 'failed_attempts' in agent.memory, "Agent memory missing failed_attempts"
        assert 'successful_patterns' in agent.memory, "Agent memory missing successful_patterns"


def test_project_structure():
    """Test that project has correct structure"""
    project_root = Path(__file__).parent.parent
    
    # Required files
    assert (project_root / "agent.py").exists(), "agent.py not found"
    assert (project_root / "requirements.txt").exists(), "requirements.txt not found"
    assert (project_root / "README.md").exists(), "README.md not found"
    
    # Required directories
    custom_parsers_dir = project_root / "custom_parsers"
    assert custom_parsers_dir.exists(), "custom_parsers directory not found"


def test_cli_interface():
    """Test CLI interface functionality"""
    import subprocess
    import os
    
    project_root = Path(__file__).parent.parent
    agent_script = project_root / "agent.py"
    
    # Test help command
    result = subprocess.run([
        "python", str(agent_script), "--help"
    ], capture_output=True, text=True, cwd=project_root)
    
    assert result.returncode == 0, "CLI help command failed"
    assert "--target" in result.stdout, "CLI missing --target option"
    assert "--parse" in result.stdout, "CLI missing --parse option"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])