"""
Web Application for AI Homework Analyzer & Solver
Using Flask framework
Run: python web_app.py
Then open: http://localhost:5000
"""

from flask import Flask, render_template, request, send_file, jsonify
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from homework_solver import HomeworkAnalyzerAlgorithm
import traceback

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 50 * 1024 * 1024  # 50MB max file

# Create uploads folder
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)


@app.route('/')
def index():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>🎓 AI Homework Analyzer & Solver</title>
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                display: flex;
                align-items: center;
                justify-content: center;
                padding: 20px;
            }
            .container {
                background: white;
                border-radius: 10px;
                box-shadow: 0 10px 40px rgba(0,0,0,0.2);
                max-width: 800px;
                width: 100%;
                padding: 40px;
            }
            h1 {
                color: #333;
                margin-bottom: 10px;
                text-align: center;
            }
            .subtitle {
                text-align: center;
                color: #666;
                margin-bottom: 30px;
            }
            .upload-area {
                border: 3px dashed #667eea;
                border-radius: 8px;
                padding: 40px;
                text-align: center;
                cursor: pointer;
                transition: all 0.3s;
                margin-bottom: 20px;
            }
            .upload-area:hover {
                background: #f0f4ff;
                border-color: #764ba2;
            }
            .upload-area.dragover {
                background: #e8eeff;
                border-color: #764ba2;
            }
            input[type="file"] { display: none; }
            .upload-text { font-size: 16px; color: #667eea; margin-bottom: 10px; }
            .upload-subtext { font-size: 12px; color: #999; }
            .btn {
                background: #667eea;
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 5px;
                cursor: pointer;
                font-size: 16px;
                width: 100%;
                transition: background 0.3s;
            }
            .btn:hover { background: #764ba2; }
            .btn:disabled { background: #ccc; cursor: not-allowed; }
            .subjects {
                background: #f5f5f5;
                padding: 20px;
                border-radius: 8px;
                margin-top: 20px;
            }
            .subjects h3 { color: #333; margin-bottom: 10px; }
            .subjects ul { list-style: none; padding-left: 0; }
            .subjects li { padding: 5px 0; color: #666; }
            .output { display: none; }
            .output.show { display: block; }
            #result {
                background: #2b2b2b;
                color: #00ff00;
                padding: 15px;
                border-radius: 5px;
                max-height: 400px;
                overflow-y: auto;
                font-family: 'Courier New', monospace;
                font-size: 12px;
                margin-top: 20px;
                white-space: pre-wrap;
                word-wrap: break-word;
            }
            .status { text-align: center; margin-top: 20px; }
            .status.success { color: #4CAF50; }
            .status.error { color: #f44336; }
            .loader {
                display: none;
                text-align: center;
                margin: 20px 0;
            }
            .spinner {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #667eea;
                border-radius: 50%;
                width: 30px;
                height: 30px;
                animation: spin 1s linear infinite;
                margin: 0 auto;
            }
            @keyframes spin {
                0% { transform: rotate(0deg); }
                100% { transform: rotate(360deg); }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎓 AI HOMEWORK ANALYZER & SOLVER</h1>
            <p class="subtitle">Upload your PDF homework and get instant solutions</p>
            
            <div class="upload-area" id="uploadArea">
                <div class="upload-text">📁 Click to upload or drag & drop</div>
                <div class="upload-subtext">PDF files only (max 50MB)</div>
                <input type="file" id="fileInput" accept=".pdf" />
            </div>
            
            <div id="fileName" style="text-align: center; margin: 10px 0; color: #4CAF50;"></div>
            
            <button class="btn" id="analyzeBtn" disabled>🚀 Analyze & Generate Solutions</button>
            
            <div class="subjects">
                <h3>📚 Supported Subjects:</h3>
                <ul>
                    <li>✅ Mathematics (Calculus, Algebra, Geometry)</li>
                    <li>✅ Physics & Chemistry</li>
                    <li>✅ Mechanical Engineering</li>
                    <li>✅ Civil Engineering</li>
                    <li>✅ Electrical Engineering</li>
                    <li>✅ Chemical Engineering</li>
                    <li>✅ Aerospace Engineering</li>
                    <li>✅ Control Systems & Computer Engineering</li>
                </ul>
            </div>
            
            <div class="loader" id="loader">
                <div class="spinner"></div>
                <p>Processing your homework...</p>
            </div>
            
            <div class="output" id="outputArea">
                <div id="result"></div>
                <div class="status" id="status"></div>
            </div>
        </div>
        
        <script>
            const uploadArea = document.getElementById('uploadArea');
            const fileInput = document.getElementById('fileInput');
            const analyzeBtn = document.getElementById('analyzeBtn');
            const loader = document.getElementById('loader');
            const result = document.getElementById('result');
            const status = document.getElementById('status');
            const outputArea = document.getElementById('outputArea');
            let selectedFile = null;
            
            // Upload area click
            uploadArea.addEventListener('click', () => fileInput.click());
            
            // Drag and drop
            uploadArea.addEventListener('dragover', (e) => {
                e.preventDefault();
                uploadArea.classList.add('dragover');
            });
            uploadArea.addEventListener('dragleave', () => {
                uploadArea.classList.remove('dragover');
            });
            uploadArea.addEventListener('drop', (e) => {
                e.preventDefault();
                uploadArea.classList.remove('dragover');
                const files = e.dataTransfer.files;
                if (files.length) {
                    fileInput.files = files;
                    handleFileSelect();
                }
            });
            
            // File selection
            fileInput.addEventListener('change', handleFileSelect);
            
            function handleFileSelect() {
                selectedFile = fileInput.files[0];
                if (selectedFile && selectedFile.name.endsWith('.pdf')) {
                    document.getElementById('fileName').textContent = `✅ Selected: ${selectedFile.name}`;
                    analyzeBtn.disabled = false;
                } else {
                    document.getElementById('fileName').textContent = '❌ Please select a PDF file';
                    analyzeBtn.disabled = true;
                }
            }
            
            // Analyze button
            analyzeBtn.addEventListener('click', async () => {
                if (!selectedFile) return;
                
                const formData = new FormData();
                formData.append('file', selectedFile);
                
                loader.style.display = 'block';
                outputArea.classList.remove('show');
                analyzeBtn.disabled = true;
                
                try {
                    const response = await fetch('/analyze', {
                        method: 'POST',
                        body: formData
                    });
                    
                    const data = await response.json();
                    
                    loader.style.display = 'none';
                    outputArea.classList.add('show');
                    
                    if (data.success) {
                        result.textContent = data.output;
                        status.textContent = '✅ Analysis complete! Report saved.';
                        status.className = 'status success';
                    } else {
                        result.textContent = data.error;
                        status.textContent = '❌ An error occurred.';
                        status.className = 'status error';
                    }
                    
                } catch (error) {
                    loader.style.display = 'none';
                    outputArea.classList.add('show');
                    result.textContent = 'Error: ' + error.message;
                    status.textContent = '❌ Network error.';
                    status.className = 'status error';
                } finally {
                    analyzeBtn.disabled = false;
                }
            });
        </script>
    </body>
    </html>
    '''


@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        if 'file' not in request.files:
            return jsonify({'success': False, 'error': 'No file provided'})
        
        file = request.files['file']
        if file.filename == '' or not file.filename.endswith('.pdf'):
            return jsonify({'success': False, 'error': 'Invalid file format. Please upload a PDF.'})
        
        # Save file
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)
        
        # Run analyzer
        try:
            algorithm = HomeworkAnalyzerAlgorithm(filepath)
            # Redirect stdout to capture output
            from io import StringIO
            import contextlib
            
            f = StringIO()
            with contextlib.redirect_stdout(f):
                algorithm.run()
            
            output = f.getvalue()
            
            return jsonify({
                'success': True,
                'output': output
            })
        
        except Exception as e:
            return jsonify({
                'success': False,
                'error': f'Analysis error: {str(e)}\n{traceback.format_exc()}'
            })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': f'Server error: {str(e)}'
        })


if __name__ == '__main__':
    print("Starting AI Homework Analyzer Web App...")
    print("Open your browser and go to: http://localhost:5000")
    app.run(debug=True, port=5000)
