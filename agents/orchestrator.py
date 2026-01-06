#!/usr/bin/env python3
"""
BA-Kit Orchestrator Agent
Master agent that understands user intent and delegates to specialized agents.
"""

from typing import Dict, Any, List, Tuple
from .base_agent import BaseAgent, AgentMemory

# Import all specialized agents
from .elicitation_agent import ElicitationAgent
from .writing_agent import WritingAgent
from .validation_agent import ValidationAgent
from .traceability_agent import TraceabilityAgent
from .export_agent import ExportAgent
from .decision_agent import DecisionAgent

# ANSI colors
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RED = '\033[91m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
RESET = '\033[0m'
BOLD = '\033[1m'


class OrchestratorAgent:
    """Master agent that coordinates all specialized agents."""
    
    def __init__(self):
        self.name = "Orchestrator"
        self.emoji = "🧠"
        self.memory = AgentMemory()
        
        # Initialize all specialized agents
        self.agents: List[BaseAgent] = [
            ElicitationAgent(),
            WritingAgent(),
            ValidationAgent(),
            TraceabilityAgent(),
            ExportAgent(),
            DecisionAgent()
        ]
    
    def banner(self):
        """Display system banner."""
        print(f"""
{CYAN}╔══════════════════════════════════════════════════════════════════╗
║                                                                  ║
║   {BOLD}BA-KIT COGNITIVE MULTI-AGENT SYSTEM{RESET}{CYAN}                           ║
║                                                                  ║
║   🧠 Orchestrator   │  🎤 Elicitation   │  ✍️  Writing          ║
║   ✅ Validation     │  🔗 Traceability  │  📤 Export            ║
║   ⚖️  Decision      │                   │                       ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝{RESET}
""")
    
    def parse_intent(self, request: str) -> Dict[str, Any]:
        """Parse user request into intent and context."""
        # Simple intent extraction
        context = {
            "raw_request": request,
            "path": ".",  # Default path
        }
        
        # Extract file paths (simple heuristic)
        words = request.split()
        for word in words:
            if word.endswith('.md') or word.endswith('.txt'):
                context["file"] = word
            if word.startswith('BR-') or word.startswith('SR-') or word.startswith('NFR-'):
                context["id"] = word
        
        return context
    
    def select_agents(self, request: str) -> List[Tuple[BaseAgent, float]]:
        """Select best agents for the request based on confidence scores."""
        scored_agents = []
        
        for agent in self.agents:
            confidence = agent.can_handle(request)
            if confidence > 0:
                scored_agents.append((agent, confidence))
        
        # Sort by confidence descending
        scored_agents.sort(key=lambda x: x[1], reverse=True)
        return scored_agents
    
    def process(self, request: str) -> Dict[str, Any]:
        """Process a user request through the multi-agent system."""
        self.banner()
        
        print(f"{MAGENTA}🧠 [Orchestrator] Analyzing request...{RESET}")
        print(f"   Request: \"{request}\"")
        print()
        
        # Parse intent
        context = self.parse_intent(request)
        
        # Select agents
        selected = self.select_agents(request)
        
        if not selected:
            print(f"{YELLOW}⚠ No agent could handle this request.{RESET}")
            return {"status": "no_agent", "message": "No agent matched the request"}
        
        print(f"{CYAN}🧠 [Orchestrator] Agent selection:{RESET}")
        for agent, confidence in selected[:3]:
            bar = "█" * int(confidence * 10) + "░" * (10 - int(confidence * 10))
            print(f"   {agent.emoji} {agent.name}: [{bar}] {confidence:.0%}")
        print()
        
        # Execute with best matching agents
        results = []
        for agent, confidence in selected:
            if confidence >= 0.2:  # Minimum threshold
                print(f"{BLUE}{'─'*60}{RESET}")
                result = agent.execute(request, context)
                results.append(result)
        
        # Aggregate results
        final_result = {
            "status": "success",
            "agents_invoked": [r["agent"] for r in results],
            "outputs": [o for r in results for o in r.get("outputs", [])]
        }
        
        print(f"{BLUE}{'─'*60}{RESET}")
        print(f"{GREEN}✓ Multi-agent processing complete.{RESET}")
        print(f"   Agents invoked: {', '.join(final_result['agents_invoked'])}")
        
        return final_result
    
    def help(self):
        """Display help information."""
        print(f"""
{CYAN}BA-Kit Cognitive Multi-Agent System{RESET}
{BOLD}Usage:{RESET} ./ba-agent "<your request in natural language>"

{BOLD}Examples:{RESET}
  ./ba-agent "check health of my requirements"
  ./ba-agent "generate user stories from BRD.md"
  ./ba-agent "validate and lint requirements.md"
  ./ba-agent "export spec.md to docx"
  ./ba-agent "analyze impact of BR-001"
  ./ba-agent "log decision for SR-007 because of performance"

{BOLD}Available Agents:{RESET}
  🎤 Elicitation   - Gather and structure information
  ✍️  Writing       - Draft and refine requirements
  ✅ Validation    - Check quality and completeness
  🔗 Traceability  - Track relationships and impacts
  📤 Export        - Produce deliverables
  ⚖️  Decision      - Record decisions and rationale
""")
