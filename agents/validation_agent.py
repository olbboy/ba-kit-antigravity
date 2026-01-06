#!/usr/bin/env python3
"""
BA-Kit Validation Agent
Specializes in quality checking and verification.
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent

class ValidationAgent(BaseAgent):
    """Agent specialized in validation and quality checking."""
    
    def __init__(self):
        super().__init__("Validation Agent", "✅")
        self.tools = ["lint_req", "consistency_checker", "gap_analyst", "metrics_dashboard"]
    
    def capabilities(self) -> List[str]:
        return [
            "validate_requirements",
            "check_consistency",
            "find_gaps",
            "compute_metrics",
            "health_check"
        ]
    
    def can_handle(self, intent: str) -> float:
        """Return confidence score for handling this intent."""
        keywords = ["validate", "check", "quality", "gap", "consistency", 
                   "metrics", "health", "score", "lint", "verify"]
        intent_lower = intent.lower()
        matches = sum(1 for kw in keywords if kw in intent_lower)
        return min(matches * 0.2, 1.0)
    
    def execute(self, task: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute validation-related tasks."""
        self.log(f"Processing: {task}")
        
        result = {"agent": self.name, "status": "success", "outputs": []}
        task_lower = task.lower()
        path = context.get("path", ".")
        
        if "health" in task_lower or "metrics" in task_lower or "doctor" in task_lower:
            output = self.run_tool("metrics_dashboard", "--path", path)
            result["outputs"].append({"tool": "metrics_dashboard", "output": output})
            self.success("Computed project health metrics")
        
        if "gap" in task_lower:
            output = self.run_tool("gap_analyst", "--path", path)
            result["outputs"].append({"tool": "gap_analyst", "output": output})
            self.success("Analyzed traceability gaps")
        
        if "consistency" in task_lower:
            output = self.run_tool("consistency_checker", "--path", path)
            result["outputs"].append({"tool": "consistency_checker", "output": output})
            self.success("Checked cross-document consistency")
        
        if "lint" in task_lower and "file" in context:
            output = self.run_tool("lint_req", context["file"])
            result["outputs"].append({"tool": "lint_req", "output": output})
            self.success("Linted requirements")
        
        self.memory.add_to_history(self.name, task, str(result["outputs"]))
        return result
