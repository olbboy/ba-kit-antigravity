#!/usr/bin/env python3
"""
BA-Kit Decision Agent
Specializes in recording decisions and resolving conflicts.
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent

class DecisionAgent(BaseAgent):
    """Agent specialized in decision logging and conflict resolution."""
    
    def __init__(self):
        super().__init__("Decision Agent", "⚖️")
        self.tools = ["decision_log"]
    
    def capabilities(self) -> List[str]:
        return [
            "log_decision",
            "query_history",
            "document_rationale"
        ]
    
    def can_handle(self, intent: str) -> float:
        """Return confidence score for handling this intent."""
        keywords = ["decision", "why", "rationale", "log", "reason", 
                   "conflict", "resolve", "history"]
        intent_lower = intent.lower()
        matches = sum(1 for kw in keywords if kw in intent_lower)
        return min(matches * 0.2, 1.0)
    
    def execute(self, task: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute decision-related tasks."""
        self.log(f"Processing: {task}")
        
        result = {"agent": self.name, "status": "success", "outputs": []}
        task_lower = task.lower()
        
        if "log" in task_lower or "record" in task_lower:
            if "id" in context and "reason" in context:
                output = self.run_tool("decision_log", "log", 
                                      "--id", context["id"],
                                      "--reason", context["reason"])
                result["outputs"].append({"tool": "decision_log", "output": output})
                self.success(f"Logged decision for {context['id']}")
        
        if "why" in task_lower or "query" in task_lower or "history" in task_lower:
            if "id" in context:
                output = self.run_tool("decision_log", "why", "--id", context["id"])
                result["outputs"].append({"tool": "decision_log", "output": output})
                self.success(f"Retrieved decision history for {context['id']}")
        
        self.memory.add_to_history(self.name, task, str(result["outputs"]))
        return result
