# 📊 AI Homework Analyzer with Graphs - Complete Guide

## Overview

The AI Homework Analyzer now includes **professional data visualization** with multiple graph types:

✅ **Problem Distribution Charts** (Pie & Bar)  
✅ **Theory Database Coverage Visualization**  
✅ **Statistical Dashboard**  
✅ **Math Function Plots**  
✅ **Real-time Report Generation**  

---

## Graph Types

### 1. 🥧 Problem Distribution Chart
- **Type**: Pie Chart
- **Purpose**: Shows the percentage breakdown of problem types
- **Shows**: Visual proportion of different homework types
- **File**: `problem_distribution.png`

### 2. 📊 Problem Count Bar Chart
- **Type**: Horizontal/Vertical Bar Chart
- **Purpose**: Counts total problems per type
- **Shows**: Number of problems in each category
- **File**: `problem_count_bar.png`

### 3. 🧠 Theory Coverage Chart
- **Type**: Horizontal Bar Chart
- **Purpose**: Shows available theories per engineering domain
- **Shows**: Comprehensive theory database coverage
- **Domains**: 
  - Mechanical Engineering (Materials, Dynamics, etc.)
  - Civil Engineering (Structural, Transportation, etc.)
  - Electrical Engineering (Circuits, Power, etc.)
  - Chemical Engineering (Mass Balance, Kinetics, etc.)
  - And more...
- **File**: `theory_coverage.png`

### 4. 📈 Statistics Dashboard
- **Type**: Multi-panel Dashboard
- **Purpose**: Comprehensive analysis overview
- **Includes**:
  - Problem type pie chart
  - Top 5 domains bar chart
  - Analysis summary statistics
  - Database information
- **File**: `statistics_dashboard.png`

### 5. 📐 Function Plot Example
- **Type**: Multi-function line plot
- **Purpose**: Example mathematical function visualization
- **Shows**: 
  - f(x) = x²
  - f(x) = x³
  - f(x) = 10·sin(x)
- **File**: `function_example.png`

---

## Usage Methods

### Method 1: Command Line (CLI)

```bash
# Basic analysis with graphs
python src/homework_solver.py "your_homework.pdf"

# The visualizer generates graphs automatically
# Graphs saved to: reports/graphs/
```

**Output Files**:
- `homework_analysis_report.txt` (formatted text report)
- `reports/graphs/problem_distribution.png`
- `reports/graphs/problem_count_bar.png`
- `reports/graphs/theory_coverage.png`
- `reports/graphs/statistics_dashboard.png`
- `reports/graphs/function_example.png`

---

### Method 2: Desktop GUI App with Graphs

**Features**:
- 📂 Browse and select PDF files
- 📊 View real-time analysis statistics
- 🖼️ Display graphs in tabbed interface
- 💾 Auto-save reports

**Installation**:
```bash
pip install pillow  # For image display in GUI
```

**Launch**:
```bash
python gui_app_graphs.py
```

**Usage**:
1. Click "📂 Browse PDF" to select a file
2. Click "🔄 Analyze" to process the PDF
3. Click "📊 Generate Graphs" to create visualizations
4. Switch between tabs to view different graphs
5. See statistics in the Statistics panel

---

### Method 3: Web Application with Graphs

**Features**:
- 🌐 Modern web interface
- 📤 Drag-and-drop file upload
- 📊 Embedded graph display
- 🔄 Real-time processing
- 💻 Multi-user access

**Installation**:
```bash
pip install flask pillow
```

**Launch**:
```bash
python web_app_graphs.py
```

Then open: **http://localhost:5000**

**Usage**:
1. Drag-and-drop PDF or click "Choose File"
2. Browser automatically uploads and analyzes
3. View all graphs on the results page
4. See statistics cards
5. Browse identified problems

---

## API Integration

### Python Integration

```python
from src.homework_solver import HomeworkAnalyzerAlgorithm, TheoryBase
from src.visualizer import ReportVisualizer

# Analyze PDF
analyzer = HomeworkAnalyzerAlgorithm()
problems = analyzer.extract_and_analyze("homework.pdf")

# Get theories
theory_base = TheoryBase()
theories = theory_base.THEORIES

# Generate visualizations
visualizer = ReportVisualizer()
viz_paths = visualizer.generate_all_visualizations(problems, theories)

# Access individual graphs
print(viz_paths['distribution'])      # Pie chart
print(viz_paths['count_bar'])         # Bar chart
print(viz_paths['theory_coverage'])   # Theory coverage
print(viz_paths['dashboard'])         # Dashboard
print(viz_paths['function_example'])  # Function plot
```

---

## Graph Customization

### Modify Graph Colors

Edit `src/visualizer.py`, line 18:

```python
# Change color scheme
self.colors = ['#your_color1', '#your_color2', ...]
```

### Custom Graph Generation

```python
from src.visualizer import ReportVisualizer

visualizer = ReportVisualizer(output_dir="my_graphs")

# Generate specific graphs
visualizer.plot_problem_distribution(problems)
visualizer.plot_theory_coverage(theories_dict)
visualizer.plot_function_example("My Function Title")
```

---

## System Requirements

### Required Libraries

```bash
pip install matplotlib>=3.5.0
pip install pillow>=8.0.0
pip install pdfplumber>=0.11.0
pip install flask>=2.0.0  # For web app only
```

### Python Version
- Python 3.8+

### System Resources
- RAM: 2GB minimum (4GB recommended)
- Disk: 500MB for graphs storage
- Graphics: Any system with display output

---

## Output File Structure

```
homework.ai.py/
├── reports/
│   ├── graphs/
│   │   ├── problem_distribution.png
│   │   ├── problem_count_bar.png
│   │   ├── theory_coverage.png
│   │   ├── statistics_dashboard.png
│   │   ├── function_example.png
│   │   └── uploads/          # Uploaded PDFs
│   └── homework_analysis_report.txt
├── src/
│   ├── homework_solver.py    # Core engine
│   └── visualizer.py         # Graph generation (NEW)
├── gui_app_graphs.py         # Desktop app (NEW)
└── web_app_graphs.py         # Web app (NEW)
```

---

## Troubleshooting

### Graphs Not Generated

❌ **Issue**: `visualizer module not found`

```bash
# Solution: Ensure src directory has visualizer.py
python -c "from src.visualizer import ReportVisualizer; print('OK')"
```

### Image Display Issues in GUI

❌ **Issue**: Graphs not showing in GUI tabs

```bash
# Solution: Install Pillow
pip install pillow --upgrade
```

### Web App Graph Display

❌ **Issue**: Graphs appear as broken images

```bash
# Solution: Check reports/graphs directory exists
python -c "from pathlib import Path; Path('reports/graphs').mkdir(parents=True, exist_ok=True); print('Directory created')"
```

### Out of Memory

❌ **Issue**: `MemoryError` during graph generation

```python
# Solution: Reduce DPI in visualizer.py (line 43, etc.)
# Change from dpi=300 to dpi=100
plt.savefig(filepath, dpi=100, bbox_inches='tight')
```

---

## Advanced Features

### 1. Batch Graph Generation

```python
from pathlib import Path
from src.visualizer import ReportVisualizer
from src.homework_solver import HomeworkAnalyzerAlgorithm

analyzer = HomeworkAnalyzerAlgorithm()
visualizer = ReportVisualizer()

# Process multiple PDFs
pdf_files = Path('.').glob('*.pdf')
for pdf_file in pdf_files:
    problems = analyzer.extract_and_analyze(str(pdf_file))
    visualizer.generate_all_visualizations(problems, {})
    print(f"✅ Processed: {pdf_file.name}")
```

### 2. Custom Statistics

```python
from collections import Counter

# Analyze problem distribution
problem_types = [p['type'] for p in problems]
distribution = Counter(problem_types)

# Find most common
most_common = distribution.most_common(5)
print("Top 5 Problem Types:")
for ptype, count in most_common:
    print(f"  {ptype}: {count} problems")
```

### 3. Export to PDF Reports

```bash
pip install reportlab
```

```python
# Generate PDF with embedded graphs
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

# Create PDF and embed graphs (custom implementation)
```

---

## Performance Metrics

| Task | Time | Output Size |
|------|------|------------|
| PDF Analysis | 1-2s | Depends on PDF |
| Graph Generation (5 graphs) | 2-3s | ~500KB |
| Web Upload + Analysis | 3-5s | ~1MB total |
| GUI Display | <1s | Cached in memory |

---

## Features Summary

| Feature | CLI | GUI | Web |
|---------|-----|-----|-----|
| PDF Analysis | ✅ | ✅ | ✅ |
| Graph Generation | ✅ | ✅ | ✅ |
| Real-time Display | ❌ | ✅ | ✅ |
| Drag-and-drop | ❌ | ⚠️ | ✅ |
| Multiple PDFs | ✅ | ⚠️ | ✅ |
| Export Report | ✅ | ✅ | ✅ |
| Graph Export | ✅ | ✅ | ✅ |

---

## Next Steps

1. **Install PIL**: `pip install pillow`
2. **Try Desktop GUI**: `python gui_app_graphs.py`
3. **Try Web App**: `python web_app_graphs.py`
4. **Analyze Your PDF**: Upload and see graphs in action
5. **Customize Colors**: Edit `src/visualizer.py` line 18
6. **Share Reports**: Graphs saved to `reports/graphs/`

---

## Support

For issues:
1. Check graph output directory: `reports/graphs/`
2. Verify all dependencies: `pip list | grep matplotlib`
3. Check error messages in console
4. Enable debug mode: Set `debug=True` in development

---

**Happy Learning! 📚📊🎓**
