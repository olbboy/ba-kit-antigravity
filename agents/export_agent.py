#!/usr/bin/env python3
"""
BA-Kit Export Agent
Specializes in producing deliverables and reports.
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent

class ExportAgent(BaseAgent):
    """Agent specialized in exporting documents and reports."""
    
    def __init__(self):
        super().__init__("Export Agent", "📤")
        self.tools = ["gen_docx", "gen_report", "validate_export", "gen_test_playwright"]
    
    def capabilities(self) -> List[str]:
        return [
            "export_docx",
            "generate_report",
            "validate_export",
            "generate_tests"
        ]
    
    def can_handle(self, intent: str) -> float:
        """Return confidence score for handling this intent."""
        keywords = ["export", "docx", "report", "pdf", "certificate", 
                   "test", "playwright", "generate"]
        intent_lower = intent.lower()
        matches = sum(1 for kw in keywords if kw in intent_lower)
        return min(matches * 0.2, 1.0)
    
    def execute(self, task: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute export-related tasks."""
        self.log(f"Processing: {task}")
        
        result = {"agent": self.name, "status": "success", "outputs": []}
        task_lower = task.lower()
        
        if "docx" in task_lower or "word" in task_lower:
            if "file" in context:
                args = [context["file"]]
                if "customer" in context:
                    args.extend(["--customer", context["customer"]])
                output = self.run_tool("gen_docx", *args)
                result["outputs"].append({"tool": "gen_docx", "output": output})
                self.success("Exported to DOCX")
        
        if "report" in task_lower or "certificate" in task_lower:
            output = self.run_tool("gen_report")
            result["outputs"].append({"tool": "gen_report", "output": output})
            self.success("Generated quality report")
        
        if "test" in task_lower or "playwright" in task_lower:
            if "file" in context:
                output = self.run_tool("gen_test_playwright", context["file"])
                result["outputs"].append({"tool": "gen_test_playwright", "output": output})
                self.success("Generated Playwright tests")
        
        if "validate" in task_lower and "export" in task_lower:
            if "file" in context:
                output = self.run_tool("validate_export", context["file"])
                result["outputs"].append({"tool": "validate_export", "output": output})
                self.success("Validated export readiness")
        
        self.memory.add_to_history(self.name, task, str(result["outputs"]))
        return result
