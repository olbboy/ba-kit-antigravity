#!/usr/bin/env python3
"""
BA-Kit Elicitation Agent
Specializes in gathering and structuring information from stakeholders.
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent

class ElicitationAgent(BaseAgent):
    """Agent specialized in elicitation and information gathering."""
    
    def __init__(self):
        super().__init__("Elicitation Agent", "🎤")
        self.tools = ["structure_notes", "gen_prompt"]
    
    def capabilities(self) -> List[str]:
        return [
            "structure_notes",
            "generate_questions",
            "parse_interview",
            "identify_gaps"
        ]
    
    def can_handle(self, intent: str) -> float:
        """Return confidence score for handling this intent."""
        keywords = ["interview", "question", "elicit", "gather", "stakeholder", 
                   "notes", "structure", "ask", "meeting"]
        intent_lower = intent.lower()
        matches = sum(1 for kw in keywords if kw in intent_lower)
        return min(matches * 0.2, 1.0)
    
    def execute(self, task: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute elicitation-related tasks."""
        self.log(f"Processing: {task}")
        
        result = {"agent": self.name, "status": "success", "outputs": []}
        
        # Determine which tool to use based on task
        task_lower = task.lower()
        
        if "structure" in task_lower or "notes" in task_lower:
            # Structure notes
            if "file" in context:
                output = self.run_tool("structure_notes", context["file"])
                result["outputs"].append({"tool": "structure_notes", "output": output})
                self.success("Structured notes into table format")
            else:
                self.warn("No file provided for structuring")
        
        if "prompt" in task_lower or "question" in task_lower:
            # Generate questions/prompts
            if "file" in context:
                output = self.run_tool("gen_prompt", context["file"])
                result["outputs"].append({"tool": "gen_prompt", "output": output})
                self.success("Generated AI review prompt")
        
        # Store in memory
        self.memory.add_to_history(self.name, task, str(result["outputs"]))
        
        return result
