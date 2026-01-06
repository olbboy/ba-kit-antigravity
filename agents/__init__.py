# BA-Kit Cognitive Multi-Agent System
"""
agents/
├── __init__.py              # Package exports
├── base_agent.py            # Base class with memory
├── orchestrator.py          # Master coordinator
├── elicitation_agent.py     # 🎤 Information gathering
├── writing_agent.py         # ✍️ Requirements drafting
├── validation_agent.py      # ✅ Quality checking
├── traceability_agent.py    # 🔗 Relationship tracking
├── export_agent.py          # 📤 Document generation
└── decision_agent.py        # ⚖️ Decision logging
"""

from .base_agent import BaseAgent, AgentMemory, AgentMessage
from .orchestrator import OrchestratorAgent
from .elicitation_agent import ElicitationAgent
from .writing_agent import WritingAgent
from .validation_agent import ValidationAgent
from .traceability_agent import TraceabilityAgent
from .export_agent import ExportAgent
from .decision_agent import DecisionAgent

__all__ = [
    'BaseAgent',
    'AgentMemory',
    'AgentMessage',
    'OrchestratorAgent',
    'ElicitationAgent',
    'WritingAgent',
    'ValidationAgent',
    'TraceabilityAgent',
    'ExportAgent',
    'DecisionAgent'
]
