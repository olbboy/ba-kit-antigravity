#!/usr/bin/env python3
"""
BA-Kit Traceability Agent
Specializes in tracking relationships and impacts.
"""

from typing import Dict, Any, List
from .base_agent import BaseAgent

class TraceabilityAgent(BaseAgent):
    """Agent specialized in traceability and impact analysis."""
    
    def __init__(self):
        super().__init__("Traceability Agent", "🔗")
        self.tools = ["knowledge_graph", "impact_sim", "trace_graph"]
    
    def capabilities(self) -> List[str]:
        return [
            "build_graph",
            "analyze_impact",
            "find_orphans",
            "visualize_traces"
        ]
    
    def can_handle(self, intent: str) -> float:
        """Return confidence score for handling this intent."""
        keywords = ["trace", "graph", "impact", "relationship", "link", 
                   "orphan", "dependency", "connection"]
        intent_lower = intent.lower()
        matches = sum(1 for kw in keywords if kw in intent_lower)
        return min(matches * 0.2, 1.0)
    
    def execute(self, task: str, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute traceability-related tasks."""
        self.log(f"Processing: {task}")
        
        result = {"agent": self.name, "status": "success", "outputs": []}
        task_lower = task.lower()
        path = context.get("path", ".")
        
        if "graph" in task_lower or "knowledge" in task_lower:
            output = self.run_tool("knowledge_graph", "--path", path)
            result["outputs"].append({"tool": "knowledge_graph", "output": output})
            self.success("Built knowledge graph")
        
        if "impact" in task_lower:
            if "id" in context:
                output = self.run_tool("impact_sim", context["id"])
                result["outputs"].append({"tool": "impact_sim", "output": output})
                self.success(f"Simulated impact for {context['id']}")
        
        if "trace" in task_lower and "visualize" in task_lower:
            output = self.run_tool("trace_graph", "--path", path)
            result["outputs"].append({"tool": "trace_graph", "output": output})
            self.success("Generated trace visualization")
        
        self.memory.add_to_history(self.name, task, str(result["outputs"]))
        return result
