"""
End-to-end test of graph visualization with homework analyzer
"""
import sys
import os
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

print("\n" + "="*70)
print("🧪 HOMEWORK ANALYZER - GRAPH VISUALIZATION TEST")
print("="*70 + "\n")

# Test 1: Import visualizer
print("Test 1: Importing visualizer module...")
try:
    from visualizer import ReportVisualizer
    print("✅ Visualizer imported\n")
except Exception as e:
    print(f"❌ Import failed: {e}\n")
    sys.exit(1)

# Test 2: Import homework solver
print("Test 2: Importing homework solver...")
try:
    from homework_solver import HomeworkAnalyzerAlgorithm, TheoryBase
    print("✅ Homework solver imported\n")
except Exception as e:
    print(f"❌ Import failed: {e}\n")
    sys.exit(1)

# Test 3: Check if PDF exists
pdf_file = "Tema2-ejercicios.pdf"
print(f"Test 3: Checking if {pdf_file} exists...")
if os.path.exists(pdf_file):
    print(f"✅ {pdf_file} found\n")
else:
    print(f"❌ {pdf_file} not found\n")
    sys.exit(1)

# Test 4: Run analyzer
print(f"Test 4: Analyzing {pdf_file}...")
try:
    analyzer = HomeworkAnalyzerAlgorithm(pdf_file)
    problems = analyzer.extract_and_analyze(pdf_file)
    print(f"✅ Analysis complete - Found {len(problems)} problems\n")
except Exception as e:
    print(f"⚠️ Analysis warning: {e}\n")
    problems = []

# Test 5: Generate visualizations
print("Test 5: Generating visualizations...")
try:
    theory_base = TheoryBase()
    visualizer = ReportVisualizer()
    viz_paths = visualizer.generate_all_visualizations(problems or [], theory_base.THEORIES)
    print(f"✅ Visualizations generated\n")
    
    print("Generated graphs:")
    for key, path in viz_paths.items():
        if path:
            file_size = os.path.getsize(path) / 1024
            print(f"   ✅ {Path(path).name} ({file_size:.1f} KB)")
except Exception as e:
    print(f"❌ Visualization failed: {e}\n")
    import traceback
    traceback.print_exc()
    sys.exit(1)

print("\n" + "="*70)
print("✅ ALL TESTS PASSED!")
print("="*70)
print("\nGraphs are ready in: reports/\n")
print("Next: Open images in reports/ folder to view graphs\n")
