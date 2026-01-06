#!/usr/bin/env python3
import sys
import os
import datetime
from pathlib import Path

# Add tools directory to path
current_dir = Path(__file__).parent
sys.path.append(str(current_dir))

try:
    import metrics_dashboard
    import gap_analyst
except ImportError:
    print("Error: Could not import sibling tools. Make sure metrics_dashboard.py and gap_analyst.py are in the tools/ directory.")
    sys.exit(1)

def generate_html(metrics, score, gaps):
    date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Color logic
    score_color = "#2ecc71" if score >= 80 else "#f1c40f" if score >= 60 else "#e74c3c"
    
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>BA-Kit Quality Certificate</title>
        <style>
            body {{ font-family: 'Inter', sans-serif; background: #1a1a1a; color: #ecf0f1; margin: 0; padding: 40px; }}
            .container {{ max-width: 900px; margin: 0 auto; background: #2c3e50; padding: 40px; border-radius: 12px; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }}
            h1 {{ text-align: center; color: #fff; margin-bottom: 10px; }}
            .subtitle {{ text-align: center; color: #bdc3c7; margin-bottom: 40px; font-size: 0.9em; }}
            
            .score-card {{ text-align: center; margin-bottom: 40px; padding: 20px; background: #34495e; border-radius: 8px; }}
            .score-val {{ font-size: 4em; font-weight: bold; color: {score_color}; }}
            .score-label {{ text-transform: uppercase; letter-spacing: 2px; font-size: 0.8em; color: #95a5a6; }}
            
            .grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-bottom: 40px; }}
            .card {{ background: #34495e; padding: 20px; border-radius: 8px; }}
            .card h3 {{ margin-top: 0; color: #3498db; }}
            .metric {{ font-size: 1.5em; font-weight: bold; }}
            
            .alert {{ background: #e74c3c; padding: 15px; border-radius: 8px; margin-bottom: 20px; }}
            .alert h3 {{ margin-top: 0; color: #fff; }}
            
            table {{ width: 100%; border-collapse: collapse; margin-top: 10px; }}
            th, td {{ text-align: left; padding: 10px; border-bottom: 1px solid #7f8c8d; }}
            th {{ color: #3498db; }}
            
            .footer {{ text-align: center; margin-top: 50px; color: #7f8c8d; font-size: 0.8em; border-top: 1px solid #7f8c8d; padding-top: 20px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🛡️ BA-Kit Quality Certificate</h1>
            <div class="subtitle">Generated on {date_str}</div>
            
            <div class="score-card">
                <div class="score-val">{score}/100</div>
                <div class="score-label">Project Health Score</div>
            </div>
            
            <div class="grid">
                <div class="card">
                    <h3>📊 Quantitative Metrics</h3>
                    <div>Completeness (TBDs): <span class="metric">{metrics['total_tbds']}</span></div>
                    <div>Ambiguity Index: <span class="metric">{metrics['ambiguous_count']}</span></div>
                    <div>Total Requirements: <span class="metric">{metrics['total_reqs']}</span></div>
                </div>
                <div class="card">
                    <h3>📉 Traceability Status</h3>
                    <div>Total Files Scanned: <span class="metric">{metrics['total_files']}</span></div>
                    <div>Untraced Requirements: <span class="metric" style="color: {'#e74c3c' if gaps else '#2ecc71'}">{len(gaps)}</span></div>
                </div>
            </div>
            
            {get_gap_section(gaps)}
            
            <div class="footer">
                Authenticated by Antigravity BA-Kit Agent • SKILL-18 Compliant
            </div>
        </div>
    </body>
    </html>
    """
    return html

def get_gap_section(gaps):
    if not gaps:
        return """
        <div class="card" style="background: #27ae60; text-align: center;">
            <h3 style="color: #fff;">✅ Perfect Traceability Coverage</h3>
            <p>All business requirements are properly linked to solution artifacts.</p>
        </div>
        """
        
    rows = ""
    for gap in gaps[:10]: # Limit to top 10
        rows += f"<tr><td>{gap['id']}</td><td>{Path(gap['file']).name}</td><td>{gap['type']}</td></tr>"
        
    more = f"<tr><td colspan='3'>...and {len(gaps)-10} more items.</td></tr>" if len(gaps) > 10 else ""
    
    return f"""
    <div class="card">
        <h3 style="color: #e74c3c;">⚠️ Traceability Gaps Detected</h3>
        <p>The following IDs are defined but not referenced downstream:</p>
        <table>
            <tr><th>ID</th><th>Source File</th><th>Issue</th></tr>
            {rows}
            {more}
        </table>
    </div>
    """

if __name__ == "__main__":
    # 1. Gather Data
    root = Path('.')
    files = metrics_dashboard.get_markdown_files(root)
    
    # Metric Data
    metrics = metrics_dashboard.analyze_metrics(files)
    score = metrics_dashboard.calculate_health_score(metrics)
    
    # Gap Data
    defs, refs = gap_analyst.find_ids_and_refs(files)
    gaps = gap_analyst.analyze_gaps(defs, refs)
    
    # 2. Adjust Score based on gaps (Penalty for orphaned items)
    # 5 points penalty per orphan, cap at 30
    gap_penalty = min(30, len(gaps) * 5)
    final_score = max(0, score - gap_penalty)
    
    # 3. Generate Report
    html_content = generate_html(metrics, final_score, gaps)
    
    out_file = root / "ba_quality_report.html"
    out_file.write_text(html_content, encoding='utf-8')
    
    print(f"✅ Quality Report Generated: {out_file}")
    print(f"   Score: {final_score}/100 (adjusted for gaps)")
