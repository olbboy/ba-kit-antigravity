#!/usr/bin/env python3
"""
BA-Kit Cognitive Multi-Agent System
Base Agent Class - Abstract interface for all specialized agents.
"""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Dict, Any, List, Optional
import json
import subprocess
import sys

# ANSI colors
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

TOOLS_DIR = Path(__file__).parent.parent / "tools"
MEMORY_DIR = Path(__file__).parent.parent / ".ba-memory"

class BaseAgent(ABC):
    """Abstract base class for all BA-Kit agents."""
    
    def __init__(self, name: str, emoji: str):
        self.name = name
        self.emoji = emoji
        self.tools: List[str] = []
        self.memory = AgentMemory()
    
    @abstractmethod
    def capabilities(self) -> List[str]:
        """Return list of capabilities this agent provides."""
        pass
    
    @abstractmethod
    def can_handle(self, intent: str) -> float:
        """Return confidence (0-1) that this agent can handle the intent."""
        pass
    
    @abstractmethod
    def execute(self, task: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a task and return results."""
        pass
    
    def run_tool(self, tool_name: str, *args) -> str:
        """Run a tool from the tools directory."""
        tool_path = TOOLS_DIR / f"{tool_name}.py"
        if not tool_path.exists():
            return f"Error: Tool {tool_name} not found"
        
        cmd = ["python3", str(tool_path)] + list(args)
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.stdout + result.stderr
    
    def log(self, message: str):
        """Log a message with agent prefix."""
        print(f"{self.emoji} [{self.name}] {message}")
    
    def success(self, message: str):
        print(f"{GREEN}{self.emoji} [{self.name}] ✓ {message}{RESET}")
    
    def warn(self, message: str):
        print(f"{YELLOW}{self.emoji} [{self.name}] ⚠ {message}{RESET}")
    
    def error(self, message: str):
        print(f"{RED}{self.emoji} [{self.name}] ✗ {message}{RESET}")


class AgentMemory:
    """Persistent memory system for agents."""
    
    def __init__(self):
        MEMORY_DIR.mkdir(exist_ok=True)
        self.context_file = MEMORY_DIR / "context.json"
        self.session_file = MEMORY_DIR / "session.json"
    
    def load_context(self) -> Dict[str, Any]:
        """Load project context from memory."""
        if self.context_file.exists():
            return json.loads(self.context_file.read_text())
        return {"project": None, "stakeholders": [], "goals": []}
    
    def save_context(self, context: Dict[str, Any]):
        """Save project context to memory."""
        self.context_file.write_text(json.dumps(context, indent=2))
    
    def load_session(self) -> Dict[str, Any]:
        """Load current session state."""
        if self.session_file.exists():
            return json.loads(self.session_file.read_text())
        return {"history": [], "last_agent": None}
    
    def save_session(self, session: Dict[str, Any]):
        """Save session state."""
        self.session_file.write_text(json.dumps(session, indent=2))
    
    def add_to_history(self, agent: str, action: str, result: str):
        """Add an action to session history."""
        session = self.load_session()
        session["history"].append({
            "agent": agent,
            "action": action,
            "result": result[:500]  # Truncate for storage
        })
        session["last_agent"] = agent
        self.save_session(session)


class AgentMessage:
    """Message passed between agents."""
    
    def __init__(self, from_agent: str, to_agent: str, action: str, 
                 payload: Dict[str, Any], priority: str = "normal"):
        self.from_agent = from_agent
        self.to_agent = to_agent
        self.action = action
        self.payload = payload
        self.priority = priority
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "from": self.from_agent,
            "to": self.to_agent,
            "action": self.action,
            "payload": self.payload,
            "priority": self.priority
        }
