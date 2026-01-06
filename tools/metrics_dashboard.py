#!/usr/bin/env python3
import os
import re
import argparse
from pathlib import Path
from datetime import datetime

# ANSI colors
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
RESET = '\033[0m'

IGNORE_DIRS = ['.git', '.agent', 'tools', 'node_modules', '.gemini']

# Weak words list (Ambiguity)
AMBIGUOUS_TERMS = [
    "fast", "slow", "easy", "clean", "robust", "sufficient", 
    "user-friendly", "intuitive", "flexible", "modern", 
    "immediately", "later", "efficient", "seamless", "adequate"
]

def get_markdown_files(root_dir):
    files = []
    for root, dirs, filenames in os.walk(root_dir):
        # Filter directories
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
        for filename in filenames:
            if filename.endswith('.md'):
                files.append(Path(root) / filename)
    return files

def analyze_metrics(files):
    metrics = {
        "total_files": len(files),
        "total_reqs": 0,
        "total_tbds": 0,
        "ambiguous_count": 0,
        "total_words": 0,
        "files_with_issues": 0
    }
    
    print(f"📊 Analyzing {len(files)} files for comprehensive metrics...\n")
    
    for file_path in files:
        try:
            content = file_path.read_text(encoding='utf-8')
            words = content.split()
            metrics["total_words"] += len(words)
            
            # Count REQs (Heuristic: Look for ID patterns like REQ-001, US-101, BR-01)
            reqs = re.findall(r'\b[A-Z]{2,}-\d{3,}\b', content)
            metrics["total_reqs"] += len(set(reqs)) # Unique IDs
            
            # Count TBDs
            tbds = len(re.findall(r'\b(TBD|TODO|FIXME)\b', content, re.IGNORECASE))
            metrics["total_tbds"] += tbds
            
            # Count Ambiguity
            ambiguity = 0
            for term in AMBIGUOUS_TERMS:
                ambiguity += len(re.findall(r'\b' + re.escape(term) + r'\b', content, re.IGNORECASE))
            metrics["ambiguous_count"] += ambiguity
            
            if tbds > 0 or ambiguity > 0:
                metrics["files_with_issues"] += 1
                
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            
    return metrics

def calculate_health_score(metrics):
    # Base score
    score = 100
    
    # Penalties
    if metrics["total_reqs"] > 0:
        # 1. TBD Penalty (Heavy)
        # If 10% of reqs are TBD, lose 20 points
        tbd_ratio = metrics["total_tbds"] / max(1, metrics["total_reqs"])
        score -= min(40, tbd_ratio * 200) # Cap penalty
        
        # 2. Ambiguity Penalty (Medium)
        # If 1 ambiguity per 100 words, lose points
        ambiguity_ratio = metrics["ambiguous_count"] / max(1, metrics["total_words"])
        score -= min(30, ambiguity_ratio * 3000) # Cap penalty
    else:
        # No Reqs yet? Neutral score
        score = 80 
        
    return max(0, round(score))

def draw_dashboard(metrics, score):
    # Calculations
    ambiguity_index = (metrics["ambiguous_count"] / max(1, metrics["total_words"])) * 100 if metrics["total_words"] else 0
    tbd_rate = (metrics["total_tbds"] / max(1, metrics["total_reqs"])) * 100 if metrics["total_reqs"] else 0
    
    # Color coding
    score_color = GREEN if score >= 80 else YELLOW if score >= 60 else RED
    
    print(f"╔═════════════════════════════════════════════════════════════╗")
    print(f"║               🚀 BA-KIT PROJECT HEALTH DASHBOARD            ║")
    print(f"╠═════════════════════════════════════════════════════════════╣")
    print(f"║                                                             ║")
    print(f"║  {BOLD}OVERALL HEALTH SCORE{RESET}: {score_color}{score}/100{RESET}                            ║")
    print(f"║  (Based on CMMI Level 4 Quantitative Metrics)               ║")
    print(f"║                                                             ║")
    print(f"╠═════════════════════════════════════════════════════════════╣")
    print(f"║  📊 METRICS SUMMARY                                         ║")
    print(f"╠══════════════════════╦══════════════════════════════════════╣")
    print(f"║  Files Analyzed      ║ {str(metrics['total_files']).ljust(36)} ║")
    print(f"║  Total Requirements  ║ {str(metrics['total_reqs']).ljust(36)} ║")
    print(f"║  Completeness (TBDs) ║ {str(metrics['total_tbds']).ljust(5)} ({tbd_rate:.1f}% rate)                 ║")
    print(f"║  Ambiguity Index     ║ {str(metrics['ambiguous_count']).ljust(5)} ({ambiguity_index:.2f}%)                   ║")
    print(f"║  Files w/ Issues     ║ {str(metrics['files_with_issues']).ljust(36)} ║")
    print(f"╠══════════════════════╩══════════════════════════════════════╣")
    print(f"║  ✅ RECOMMENDATION                                          ║")
    
    if score >= 90:
        print(f"║  {GREEN}Excellent! Ready for baseline.{RESET}                             ║")
    elif score >= 75:
        print(f"║  {GREEN}Good. Review TBDs before baseline.{RESET}                         ║")
    elif score >= 50:
        print(f"║  {YELLOW}Needs Improvement. Focus on Ambiguity & Completeness.{RESET}      ║")
    else:
        print(f"║  {RED}CRITICAL. Do not proceed to development.{RESET}                   ║")
        
    print(f"╚═════════════════════════════════════════════════════════════╝")
    print("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='BA-Kit Metrics Dashboard')
    parser.add_argument('--path', help='Root directory', default='.')
    args = parser.parse_args()
    
    root_path = Path(args.path)
    files = get_markdown_files(root_path)
    metrics = analyze_metrics(files)
    score = calculate_health_score(metrics)
    draw_dashboard(metrics, score)
