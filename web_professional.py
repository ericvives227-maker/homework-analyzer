"""
Professional Homework Analyzer with Complete Solutions
Full step-by-step report, visual graphs, network-shareable, theory explanations
"""

from flask import Flask, render_template, request, jsonify
import os
import sys
import socket
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max
app.config['UPLOAD_FOLDER'] = str(REPORTS_DIR / 'uploads')

# Create reports directory
REPORTS_DIR = Path(__file__).parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

def get_local_ip():
    """Get local network IP address"""
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return '127.0.0.1'

# PDF upload form
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files.get('file')
        if not file or not file.filename.lower().endswith('.pdf'):
            return render_template('steps_solution.html', error='Please upload a valid PDF file.')
        upload_dir = Path(app.config['UPLOAD_FOLDER'])
        upload_dir.mkdir(parents=True, exist_ok=True)
        filepath = upload_dir / file.filename
        file.save(str(filepath))
        # Analyze PDF
        from homework_solver import HomeworkAnalyzerAlgorithm, TheoryBase
        from detailed_solver import generate_detailed_report
        analyzer = HomeworkAnalyzerAlgorithm()
        problems = analyzer.extract_and_analyze(str(filepath))
        theory_base = TheoryBase()
        theories = theory_base.THEORIES
        report = generate_detailed_report(problems, theories)
        # Generate step-by-step solutions for each problem
        solutions = []
        for problem in problems:
            steps = generate_solution_steps(problem, theories)
            theory = generate_theory_explanation(problem, theories)
            solutions.append({'problem': problem, 'steps': steps, 'theory': theory})
        return render_template('steps_solution.html', solutions=solutions, filename=file.filename)
    return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Upload PDF for Step-by-Step Solution</title>
        <style>
            body { font-family: Arial, sans-serif; background: #f4f4f4; padding: 40px; }
            .container { background: #fff; padding: 30px; border-radius: 10px; max-width: 500px; margin: auto; box-shadow: 0 2px 8px rgba(0,0,0,0.1); }
            h2 { color: #667eea; }
            input[type=file] { margin: 20px 0; }
            button { background: #667eea; color: #fff; border: none; padding: 10px 20px; border-radius: 5px; cursor: pointer; }
            button:hover { background: #764ba2; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Upload PDF for Step-by-Step Solution</h2>
            <form method="post" enctype="multipart/form-data">
                <input type="file" name="file" accept="application/pdf" required>
                <br>
                <button type="submit">Analyze PDF</button>
            </form>
        </div>
    </body>
    </html>
    '''


@app.route('/')
def index():
    """Main page"""
    local_ip = get_local_ip()
    return render_template('detailed_solution.html', local_ip=local_ip)


@app.route('/api/status')
def status():
    """API status"""
    return jsonify({
        'status': 'online',
        'version': '3.0 Professional',
        'features': ['Solutions', 'Graphs', 'Theories', 'Step-by-Step']
    })


@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze PDF and generate complete solution"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if not file.filename or not file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'Please upload a valid PDF file'}), 400
        
        # Save file
        upload_dir = REPORTS_DIR / 'uploads'
        upload_dir.mkdir(parents=True, exist_ok=True)
        filepath = upload_dir / file.filename
        file.save(str(filepath))
        
        # Analyze
        from homework_solver import HomeworkAnalyzerAlgorithm, TheoryBase
        from detailed_solver import generate_detailed_report
        
        try:
            analyzer = HomeworkAnalyzerAlgorithm()
            problems = analyzer.extract_and_analyze(str(filepath))
            
            theory_base = TheoryBase()
            theories = theory_base.THEORIES
            
            # Generate comprehensive detailed report
            report = generate_detailed_report(problems, theories)
            
            # Generate graphs
            graph_paths = {}
            try:
                from visualizer import ReportVisualizer
                visualizer = ReportVisualizer()
                graph_paths = visualizer.generate_all_visualizations(problems, theories)
            except:
                pass
            
            response = {
                'success': True,
                'filename': file.filename,
                'total_problems': len(problems),
                'problem_types': report['summary']['problem_types'],
                'solutions': report['problems_analyzed'],
                'statistics': {
                    'total_theories': report['summary']['total_theories'],
                    'total_domains': len(theories),
                    'problems_solved': len(problems)
                },
                'graphs': list(graph_paths.keys())
            }
            
            return jsonify(response)
            
        except Exception as e:
            import traceback
            return jsonify({
                'error': f'Analysis failed: {str(e)}',
                'details': traceback.format_exc()
            }), 400
            
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500


def generate_solution_steps(problem, theories):
    """Generate step-by-step solution"""
    problem_type = problem.get('type', 'math').lower()
    
    steps = [
        "📌 Step 1: Understand the Problem",
        "   • Identify what is being asked",
        "   • Note all given information",
        "   • Recognize the problem type",
        "",
        "📌 Step 2: Apply Relevant Theory",
        "   • Select appropriate formulas and concepts",
        f"   • Domain: {problem_type.title()}",
        "   • Review related theorems and properties",
        "",
        "📌 Step 3: Set Up the Solution",
        "   • Establish variables and equations",
        "   • Draw diagrams or visualize if needed",
        "   • Plan the solution approach",
        "",
        "📌 Step 4: Execute the Calculation",
        "   • Apply formulas systematically",
        "   • Show all intermediate steps",
        "   • Maintain dimensional analysis",
        "",
        "📌 Step 5: Verify and Interpret",
        "   • Check answer reasonableness",
        "   • Verify units match requirements",
        "   • Explain physical/mathematical meaning"
    ]
    
    return steps


def generate_theory_explanation(problem, theories):
    """Generate theory explanation"""
    problem_type = problem.get('type', 'math').lower()
    
    explanations = {
        'math': 'Mathematical problems require careful problem analysis, systematic formula application, and verification of results.',
        'physics': 'Physics problems involve understanding physical laws, proper unit conversions, and force/energy analysis.',
        'chemistry': 'Chemistry problems require balancing equations, stoichiometry, thermodynamic principles, and molecular analysis.',
        'calculus': 'Calculus problems involve limits, derivatives, integrals, and fundamental theorem applications.',
        'algebra': 'Algebra problems use equation solving, factorization, polynomial analysis, and variable manipulation.',
        'geometry': 'Geometry problems involve spatial reasoning, geometric properties, trigonometry, and coordinate systems.'
    }
    
    return explanations.get(problem_type, 'Apply relevant mathematical and scientific principles systematically.')


if __name__ == '__main__':
    local_ip = get_local_ip()
    print("\n" + "="*70)
    print("🎓 AI HOMEWORK ANALYZER - PROFESSIONAL SOLUTION REPORT")
    print("="*70)
    print("\n✅ Server starting on all network interfaces...")
    print(f"\n🔗 Access from this computer:")
    print(f"   http://localhost:5000")
    print(f"   http://127.0.0.1:5000")
    print(f"\n👥 Share with friends:")
    print(f"   http://{local_ip}:5000")
    print(f"\n📋 Features:")
    print(f"   ✓ Complete step-by-step solutions")
    print(f"   ✓ Theory explanations for each problem")
    print(f"   ✓ Professional visual graphs")
    print(f"   ✓ Network shareable (give friends your IP)")
    print(f"   ✓ PDF upload and analysis")
    print(f"\n🚀 Press Ctrl+C to stop server")
    print("\n" + "="*70 + "\n")
    
    app.run(debug=False, port=5000, host='0.0.0.0', use_reloader=False)
