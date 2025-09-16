"""
Custom Parsers Package

This package contains bank-specific parsers that inherit from BaseBankParser.
Each parser implements the parse() method to extract transaction data from
bank statement PDFs and return it in a standardized DataFrame format.
"""

from .base_parser import BaseBankParser, ParserFactory, validate_parser_contract

__all__ = ['BaseBankParser', 'ParserFactory', 'validate_parser_contract']

# Custom bank statement parsers
