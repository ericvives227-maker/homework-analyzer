"""
Enhanced Web Application with Graphs - AI Homework Analyzer
Displays analysis with visual charts and statistics
"""

from flask import Flask, render_template, request, jsonify, send_file
import os
import sys
from pathlib import Path

# Add src to Python path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from homework_solver import HomeworkAnalyzerAlgorithm
from visualizer import ReportVisualizer
import base64
from io import BytesIO

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# Create reports directory
REPORTS_DIR = Path(__file__).parent.parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)

def image_to_base64(filepath):
    """Convert image to base64 for embedding in HTML"""
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


@app.route('/')
def index():
    """Main page with upload"""
    return render_template('index_with_graphs.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze uploaded PDF and return results with graphs"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Save uploaded file
        upload_dir = REPORTS_DIR / 'uploads'
        upload_dir.mkdir(exist_ok=True)
        
        filepath = upload_dir / file.filename
        file.save(str(filepath))
        
        # Analyze
        analyzer = HomeworkAnalyzerAlgorithm()
        try:
            problems = analyzer.extract_and_analyze(str(filepath))
        except Exception as e:
            return jsonify({'error': f'PDF Analysis Error: {str(e)}'}), 400
        
        # Get theories
        from homework_solver import TheoryBase
        theory_base = TheoryBase()
        theories = theory_base.THEORIES
        
        # Generate visualizations
        visualizer = ReportVisualizer(str(REPORTS_DIR / 'graphs'))
        viz_paths = visualizer.generate_all_visualizations(problems, theories)
        
        # Convert images to base64
        images = {}
        for key, path in viz_paths.items():
            if path:
                images[key] = image_to_base64(path)
        
        # Prepare response
        response = {
            'success': True,
            'filename': file.filename,
            'total_problems': len(problems),
            'problem_types': list(set(p['type'].upper() for p in problems)),
            'problems': problems[:10],  # First 10 for display
            'images': images,
            'statistics': {
                'total_theories': sum(len(t) for t in theories.values()),
                'total_domains': len(theories),
                'problems_found': len(problems)
            }
        }
        
        return jsonify(response)
        
    except Exception as e:
        return jsonify({'error': f'Server Error: {str(e)}'}), 500


@app.route('/api/theory/<domain>')
def get_theory(domain):
    """Get theories for a specific domain"""
    from homework_solver import TheoryBase
    theory_base = TheoryBase()
    theories = theory_base.THEORIES
    
    if domain in theories:
        return jsonify({
            'domain': domain,
            'theories': theories[domain][:5]  # First 5
        })
    return jsonify({'error': 'Domain not found'}), 404


if __name__ == '__main__':
    print("\n" + "="*50)
    print("🌐 AI Homework Analyzer - Web App with Graphs")
    print("="*50)
    print("\n📊 Features:")
    print("✅ PDF upload and analysis")
    print("✅ Problem distribution charts")
    print("✅ Theory coverage visualization")
    print("✅ Statistics dashboard")
    print("✅ Real-time processing")
    print("\n🔗 Starting server at http://localhost:5000")
    print("="*50 + "\n")
    
    app.run(debug=True, port=5000, use_reloader=False)
