"""
Production-Ready Web Application
AI Homework Analyzer with Step-by-Step Solutions
"""

from flask import Flask, render_template, request, jsonify, redirect, url_for, send_file
import base64
import os
import sys
import socket
from pathlib import Path
import logging
import threading
import time

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100MB max file size
app.config['UPLOAD_FOLDER'] = 'reports/uploads'

# Create necessary directories
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs('reports/graphs', exist_ok=True)


def delete_after_delay(filepath, delay_seconds=3600):
    """
    Delete a file after a specified delay (default: 1 hour).
    Runs in a background thread for privacy protection.
    """
    def delayed_delete():
        try:
            time.sleep(delay_seconds)
            if os.path.exists(filepath):
                os.remove(filepath)
                logger.info(f"🗑️ Auto-deleted for privacy: {filepath}")
        except Exception as e:
            logger.warning(f"⚠️ Failed to auto-delete {filepath}: {str(e)}")
    
    thread = threading.Thread(target=delayed_delete, daemon=True)
    thread.start()


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


@app.route('/')
def index():
    """Home page"""
    local_ip = get_local_ip()
    return render_template('home.html', local_ip=local_ip)


@app.route('/index_with_graphs.html')
def analyzer_page():
    """Analyzer page with graphs"""
    local_ip = get_local_ip()
    return render_template('index_with_graphs.html', local_ip=local_ip)


def image_to_base64(filepath: str) -> str | None:
    """Convert a local image file into a base64 string for embedding."""
    if not filepath or not os.path.exists(filepath):
        return None
    with open(filepath, 'rb') as img_file:
        return base64.b64encode(img_file.read()).decode('utf-8')


@app.route('/analyzer')
def analyzer():
    """Solution analyzer page"""
    local_ip = get_local_ip()
    return render_template('detailed_solution.html', local_ip=local_ip)


@app.route('/api/image/<filename>')
def serve_image(filename):
    """Serve visualization images"""
    try:
        # Security: only allow serving specific problem visualization files
        if not filename.startswith('problem_') or not filename.endswith('.png'):
            return jsonify({'error': 'Invalid image'}), 400
        
        filepath = os.path.join('reports', 'graphs', f'{filename}.png')
        
        # Ensure the file exists and is in the expected directory
        if not os.path.exists(filepath):
            logger.warning(f"⚠️ Image not found: {filepath}")
            return jsonify({'error': 'Image not found'}), 404
        
        # Serve the image file
        return send_file(filepath, mimetype='image/png', cache_timeout=3600)
    except Exception as e:
        logger.error(f"❌ Error serving image: {str(e)}")
        return jsonify({'error': 'Failed to serve image'}), 500


@app.route('/api/status')
def status():
    """API status endpoint"""
    return jsonify({
        'status': 'online',
        'version': '4.0 Production',
        'features': [
            'Step-by-Step Solutions',
            'Cliff Notes Summary',
            'Theory Explanations',
            'Multiple Problem Types',
            'Professional Design'
        ]
    })


@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    """Analyze PDF and generate complete solution with cliff notes"""
    try:
        if request.method == 'GET':
            return redirect(url_for('index'))

        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400
        
        file = request.files['file']
        if not file.filename or not file.filename.lower().endswith('.pdf'):
            return jsonify({'error': 'Please upload a valid PDF file'}), 400
        
        # Save uploaded file
        upload_dir = Path(app.config['UPLOAD_FOLDER'])
        upload_dir.mkdir(parents=True, exist_ok=True)
        filepath = upload_dir / file.filename
        
        try:
            file.save(str(filepath))
            logger.info(f"✅ File saved: {filepath}")
        except Exception as e:
            logger.error(f"❌ File save error: {str(e)}")
            return jsonify({'error': f'Failed to save file: {str(e)}'}), 400
        
        # Analyze PDF
        try:
            from homework_solver import HomeworkAnalyzerAlgorithm, TheoryBase
            from detailed_solver import generate_detailed_report
            
            logger.info(f"🔄 Analyzing PDF: {file.filename}")
            analyzer = HomeworkAnalyzerAlgorithm()
            problems = analyzer.extract_and_analyze(str(filepath))
            
            if not problems:
                logger.warning("⚠️ No problems found in PDF")
                # Delete uploaded file for privacy even when no problems found
                delete_after_delay(str(filepath), delay_seconds=3600)
                logger.info("🔒 Scheduling empty PDF deletion for privacy")
                return jsonify({'error': 'No problems found in PDF. Please check the file format.'}), 400
            
            logger.info(f"✅ Found {len(problems)} problems")
            
            theory_base = TheoryBase()
            theories = theory_base.THEORIES
            
            # Generate comprehensive detailed report with cliff notes
            report = generate_detailed_report(problems, theories)
            
            # Generate graphs (optional)
            graph_paths = {}
            try:
                from visualizer import ReportVisualizer
                logger.info("📊 Generating visualizations...")
                visualizer = ReportVisualizer()
                graph_paths = visualizer.generate_all_visualizations(problems, theories)
                logger.info(f"✅ Generated {len(graph_paths)} graphs")
                
                # Generate individual problem visualizations
                logger.info("🎨 Generating individual problem visualizations...")
                problems_with_viz = 0
                for idx, problem in enumerate(problems):
                    try:
                        viz_path = visualizer.generate_problem_visualization(problem, idx)
                        if viz_path and os.path.exists(viz_path):
                            # Store file path (not base64) for frontend to request
                            viz_url = f"/api/image/problem_{idx}"
                            problems[idx]['visualization'] = viz_url
                            if idx < len(report['problems_analyzed']):
                                report['problems_analyzed'][idx]['visualization'] = viz_url
                            problems_with_viz += 1
                            # Schedule deletion of individual viz
                            delete_after_delay(viz_path, delay_seconds=3600)
                    except Exception as viz_error:
                        logger.warning(f"⚠️ Skipped visualization for problem {idx}: {str(viz_error)}")
                logger.info(f"✅ Generated visualizations for {problems_with_viz}/{len(problems)} problems")
            except Exception as e:
                logger.warning(f"⚠️ Graph generation skipped: {str(e)}")
            
            # Build response (much smaller now - no base64 images)
            response = {
                'success': True,
                'filename': file.filename,
                'total_problems': len(problems),
                'problem_types': report['summary']['problem_types'],
                'problems': problems[:10],
                'solutions': report['problems_analyzed'],
                'cliff_notes': report.get('cliff_notes', {}),
                'statistics': {
                    'total_theories': report['summary']['total_theories'],
                    'total_domains': len(theories),
                    'problems_solved': len(problems)
                },
                'graphs': list(graph_paths.keys())
            }
            
            # Schedule automatic deletion after 1 hour for privacy
            logger.info("🔒 Scheduling file deletion in 1 hour for privacy protection")
            delete_after_delay(str(filepath), delay_seconds=3600)
            
            # Delete generated graph files after 1 hour
            for graph_path in graph_paths.values():
                if graph_path and os.path.exists(graph_path):
                    delete_after_delay(graph_path, delay_seconds=3600)
            
            logger.info("✅ Analysis complete")
            return jsonify(response)
            
        except Exception as e:
            import traceback
            logger.error(f"❌ Analysis error: {str(e)}")
            logger.error(traceback.format_exc())
            
            # Still delete uploaded file even if analysis fails (privacy)
            if filepath and os.path.exists(filepath):
                delete_after_delay(str(filepath), delay_seconds=3600)
                logger.info("🔒 Scheduling failed upload deletion for privacy")
            
            return jsonify({
                'error': f'Analysis failed: {str(e)}',
                'details': traceback.format_exc()
            }), 400
            
    except Exception as e:
        logger.error(f"❌ Server error: {str(e)}")
        return jsonify({'error': f'Server error: {str(e)}'}), 500


@app.errorhandler(404)
def not_found(error):
    """Handle 404 errors"""
    return jsonify({'error': 'Endpoint not found'}), 404


@app.errorhandler(500)
def server_error(error):
    """Handle 500 errors"""
    return jsonify({'error': 'Internal server error'}), 500


@app.errorhandler(413)
def request_entity_too_large(error):
    """Handle file too large error"""
    return jsonify({'error': 'File too large (max 100MB)'}), 413


if __name__ == '__main__':
    local_ip = get_local_ip()
    
    print("\n" + "="*80)
    print("🎓 AI HOMEWORK ANALYZER - PROFESSIONAL SOLUTION REPORT")
    print("="*80)
    print("\n✅ Server starting on all network interfaces...")
    print(f"\n🔗 Access from this computer:")
    print(f"   http://localhost:5000")
    print(f"   http://127.0.0.1:5000")
    print(f"\n👥 Share with friends on same network:")
    print(f"   http://{local_ip}:5000")
    print(f"\n📋 Features:")
    print(f"   ✓ Complete step-by-step solutions")
    print(f"   ✓ Cliff notes summary")
    print(f"   ✓ Theory explanations for each problem")
    print(f"   ✓ Professional visual graphs")
    print(f"   ✓ PDF upload and analysis")
    print(f"   ✓ Network shareable")
    print(f"   ✓ Print-friendly format")
    print(f"\n🚀 Press Ctrl+C to stop server")
    print("\n" + "="*80 + "\n")
    
    # Run Flask app
    # Use debug=False for production
    app.run(
        debug=False,
        port=5000,
        host='0.0.0.0',
        use_reloader=False,
        threaded=True
    )
