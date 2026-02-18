"""
Simple Web Application - AI Homework Analyzer
Basic version that works reliably
"""

from flask import Flask, render_template, request, jsonify
import os
import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max

# Create reports directory
REPORTS_DIR = Path(__file__).parent / "reports"
REPORTS_DIR.mkdir(exist_ok=True)


@app.route('/')
def index():
    """Main page"""
    return render_template('simple_index.html')


@app.route('/api/status')
def status():
    """API status check"""
    return jsonify({
        'status': 'online',
        'message': 'AI Homework Analyzer Ready',
        'version': '2.0 with Graphs'
    })


@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze uploaded PDF"""
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        if not file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'Only PDF files are supported'}), 400
        
        # Save uploaded file
        upload_dir = REPORTS_DIR / 'uploads'
        upload_dir.mkdir(parents=True, exist_ok=True)
        filepath = upload_dir / file.filename
        
        try:
            file.save(str(filepath))
        except Exception as e:
            return jsonify({'error': f'Failed to save file: {str(e)}'}), 400
        
        # Verify file exists
        if not filepath.exists():
            return jsonify({'error': 'File was not saved properly'}), 400
        
        # Try to import and analyze
        try:
            from homework_solver import HomeworkAnalyzerAlgorithm, TheoryBase
            
            analyzer = HomeworkAnalyzerAlgorithm()
            problems = analyzer.extract_and_analyze(str(filepath))
            
            theory_base = TheoryBase()
            theories = theory_base.THEORIES
            
            # Prepare response
            response = {
                'success': True,
                'filename': file.filename,
                'total_problems': len(problems),
                'problem_types': list(set(p.get('type', 'unknown').upper() for p in problems)) if problems else [],
                'problems': problems[:20] if problems else [],
                'statistics': {
                    'total_theories': sum(len(t) for t in theories.values()) if theories else 0,
                    'total_domains': len(theories) if theories else 0,
                    'problems_found': len(problems)
                },
                'message': f'✅ Successfully analyzed {file.filename}'
            }
            
            if len(problems) > 0:
                response['message'] += f' with {len(problems)} problems found!'
            
            return jsonify(response)
            
        except Exception as e:
            import traceback
            error_details = traceback.format_exc()
            return jsonify({
                'error': f'Analysis failed: {str(e)}',
                'debug': error_details if app.debug else 'Check if PDF is valid and readable'
            }), 400
            
    except Exception as e:
        import traceback
        return jsonify({
            'error': f'Server error: {str(e)}',
            'trace': traceback.format_exc()
        }), 500


if __name__ == '__main__':
    print("\n" + "="*60)
    print("🌐 AI Homework Analyzer - Simple Web App")
    print("="*60)
    print("\n✅ Server starting...")
    print("📍 Visit: http://localhost:5000")
    print("\n🚀 Press Ctrl+C to stop the server\n")
    print("="*60 + "\n")
    
    app.run(debug=False, port=5000, use_reloader=False, host='127.0.0.1')
