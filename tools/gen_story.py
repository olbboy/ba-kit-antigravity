#!/usr/bin/env python3
import argparse
import re
from pathlib import Path

# ANSI colors
GREEN = '\033[92m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

def extract_actors(text):
    """Heuristically find actors (users, roles) in text."""
    # Common role keywords
    role_keywords = [
        'customer', 'user', 'admin', 'administrator', 'manager', 
        'employee', 'client', 'operator', 'analyst', 'staff',
        'guest', 'member', 'subscriber', 'visitor', 'owner'
    ]
    
    text_lower = text.lower()
    for role in role_keywords:
        if role in text_lower:
            return role.title()
    
    # Look for "The [Role]" pattern
    match = re.search(r'\bthe\s+([A-Z][a-z]+)\b', text)
    if match:
        return match.group(1)
    
    return "User"  # Default

def extract_goal(text):
    """Heuristically find the main goal/action."""
    # Look for verbs after "to" or infinitive patterns
    patterns = [
        r'(?:to|shall|must|should|can)\s+([\w\s]+?)(?:\.|,|;|$)',
        r'(?:ability|need|want)\s+to\s+([\w\s]+?)(?:\.|,|;|$)',
    ]
    for p in patterns:
        match = re.search(p, text, re.IGNORECASE)
        if match:
            goal = match.group(1).strip()
            # Limit length
            if len(goal) > 80:
                goal = goal[:80] + "..."
            return goal
    
    # Fallback: first 50 chars
    return text[:50].strip() + "..."

def extract_benefit(text):
    """Heuristically find the benefit (so that...)."""
    patterns = [
        r'(?:so that|in order to|to achieve|to ensure|for)\s+([\w\s,]+?)(?:\.|;|$)',
        r'(?:benefit|value|result)[\s:]+([^.;]+)',
    ]
    for p in patterns:
        match = re.search(p, text, re.IGNORECASE)
        if match:
            return match.group(1).strip()
    
    return "achieve their goal efficiently"

def generate_ac(text):
    """Generate Acceptance Criteria (Gherkin) from text heuristics."""
    acs = []
    
    # Look for conditions/actions
    if re.search(r'\b(valid|invalid|correct|incorrect|success|fail)\b', text, re.IGNORECASE):
        acs.append("Given I am on the relevant page")
        acs.append("When I perform the action with valid input")
        acs.append("Then the system should respond successfully")
        acs.append("")
        acs.append("Given I am on the relevant page")
        acs.append("When I perform the action with invalid input")
        acs.append("Then the system should display an error message")
    else:
        acs.append("Given I am on the relevant page")
        acs.append("When I perform the required action")
        acs.append("Then the expected outcome occurs")
    
    return acs

def generate_story(input_text, story_id="US-XXX"):
    """Main generation logic."""
    actor = extract_actors(input_text)
    goal = extract_goal(input_text)
    benefit = extract_benefit(input_text)
    acs = generate_ac(input_text)
    
    story = f"""
## {story_id}: [Generated Title - Review]

**As a** {actor}
**I want** {goal}
**So that** {benefit}

### Acceptance Criteria

```gherkin
Scenario: Happy Path
  {chr(10).join('  ' + a for a in acs[:3])}

Scenario: Error Path
  {chr(10).join('  ' + a for a in acs[3:] if acs[3:])}
```

### Notes
- ⚠️ This is an AI-generated draft. Review and refine before approval.
- Priority: [TBD]
- Estimation: [TBD]
"""
    return story.strip()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Auto Story Generator')
    parser.add_argument('--text', help='BRD text to convert', required=False)
    parser.add_argument('--file', help='File containing BRD text', required=False)
    parser.add_argument('--id', help='Story ID prefix', default='US-GEN-001')
    
    args = parser.parse_args()
    
    if args.file:
        input_text = Path(args.file).read_text(encoding='utf-8')
    elif args.text:
        input_text = args.text
    else:
        print(f"{YELLOW}Usage: python3 gen_story.py --text \"Your BRD text here\"{RESET}")
        print(f"       python3 gen_story.py --file path/to/brd_section.txt")
        exit(1)
    
    print(f"{CYAN}🪄 Generating User Story from input...{RESET}\n")
    result = generate_story(input_text, args.id)
    print(result)
    print(f"\n{GREEN}✅ Story generated. Copy above or pipe to file.{RESET}")
