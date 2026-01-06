#!/usr/bin/env python3
"""
BA-Kit Cognitive Multi-Agent System CLI
Entry point for natural language processing of BA tasks.
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents import OrchestratorAgent


def main():
    orchestrator = OrchestratorAgent()
    
    if len(sys.argv) < 2 or sys.argv[1] in ['-h', '--help', 'help']:
        orchestrator.help()
        return
    
    # Join all arguments as the request
    request = " ".join(sys.argv[1:])
    
    # Process through multi-agent system
    result = orchestrator.process(request)
    
    # Return exit code based on status
    sys.exit(0 if result.get("status") == "success" else 1)


if __name__ == "__main__":
    main()
