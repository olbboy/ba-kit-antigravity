#!/usr/bin/env python3
"""
BA-Kit Writing Agent
Specializes in drafting and refining requirements documents.
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent

class WritingAgent(BaseAgent):
    """Agent specialized in writing and refining requirements."""
    
    def __init__(self):
        super().__init__("Writing Agent", "✍️")
        self.tools = ["gen_story", "lint_expert"]
    
    def capabilities(self) -> List[str]:
        return [
            "generate_user_story",
            "lint_requirements",
            "check_invest",
            "check_gherkin"
        ]
    
    def can_handle(self, intent: str) -> float:
        """Return confidence score for handling this intent."""
        keywords = ["write", "story", "user story", "draft", "requirement", 
                   "spec", "gherkin", "invest", "acceptance criteria"]
        intent_lower = intent.lower()
        matches = sum(1 for kw in keywords if kw in intent_lower)
        return min(matches * 0.2, 1.0)
    
    def execute(self, task: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute writing-related tasks."""
        self.log(f"Processing: {task}")
        
        result = {"agent": self.name, "status": "success", "outputs": []}
        task_lower = task.lower()
        
        if "story" in task_lower or "generate" in task_lower:
            # Generate user story
            if "text" in context:
                output = self.run_tool("gen_story", "--text", context["text"])
                result["outputs"].append({"tool": "gen_story", "output": output})
                self.success("Generated user story from text")
            elif "file" in context:
                output = self.run_tool("gen_story", context["file"])
                result["outputs"].append({"tool": "gen_story", "output": output})
                self.success("Generated user stories from file")
        
        if "lint" in task_lower or "check" in task_lower or "validate" in task_lower:
            # Lint requirements
            if "file" in context:
                output = self.run_tool("lint_expert", context["file"])
                result["outputs"].append({"tool": "lint_expert", "output": output})
                self.success("Linted requirements file")
        
        self.memory.add_to_history(self.name, task, str(result["outputs"]))
        return result
