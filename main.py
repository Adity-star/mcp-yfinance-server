#!/usr/bin/env python3
"""
MCP Server Runner - For testing and development
This file provides a simple way to run the yfinance MCP server
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from yfinance_mcp.server import main

if __name__ == "__main__":    
    main()




