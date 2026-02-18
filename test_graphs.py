"""
Test script to demonstrate graph visualization capabilities
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from visualizer import ReportVisualizer


def test_visualizer():
    """Test graph generation with sample data"""
    
    print("\n" + "="*60)
    print("📊 Testing AI Homework Analyzer Visualization Module")
    print("="*60 + "\n")
    
    # Sample problems data
    sample_problems = [
        {'type': 'calculus', 'text': 'Compute the limit of sin(x)/x as x approaches 0'},
        {'type': 'algebra', 'text': 'Solve the quadratic equation x² + 5x + 6 = 0'},
        {'type': 'calculus', 'text': 'Find the derivative of f(x) = 3x³ + 2x²'},
        {'type': 'physics', 'text': 'Calculate the velocity of an object after 5 seconds'},
        {'type': 'physics', 'text': 'Determine the force applied to move an object'},
        {'type': 'chemistry', 'text': 'Balance the chemical equation'},
        {'type': 'calculus', 'text': 'Evaluate the definite integral from 0 to 1 of x² dx'},
        {'type': 'algebra', 'text': 'Simplify the algebraic expression'},
        {'type': 'physics', 'text': 'Calculate the energy in a system'},
        {'type': 'geometry', 'text': 'Find the area of a triangle'},
    ]
    
    # Sample theories
    sample_theories = {
        'calculus': ['Derivative Rules', 'Limits', 'Integration', 'Series', 'Differential Equations'],
        'algebra': ['Linear Equations', 'Quadratic Formulas', 'Polynomials', 'Factoring', 'Matrices'],
        'physics': ['Mechanics', 'Thermodynamics', 'Electromagnetism', 'Optics', 'Waves'],
        'chemistry': ['Stoichiometry', 'Atomic Structure', 'Chemical Bonding', 'Equilibrium', 'Kinetics'],
        'geometry': ['Euclidean Geometry', 'Trigonometry', 'Vectors', 'Transformations', 'Coordinate Systems'],
        'mechanical_engineering': ['Materials Science', 'Dynamics', 'Thermodynamics', 'Fluid Mechanics'],
        'civil_engineering': ['Structural Analysis', 'Geotechnical', 'Transportation', 'Hydraulics'],
        'electrical_engineering': ['Circuit Analysis', 'Electromagnetics', 'Power Systems', 'Signals']
    }
    
    # Create visualizer
    print("📁 Creating reports directory...")
    visualizer = ReportVisualizer()
    print("✅ Visualizer initialized\n")
    
    # Generate all visualizations
    print("📊 Generating visualizations...\n")
    
    try:
        # 1. Problem distribution
        print("  1️⃣  Generating problem distribution chart...")
        dist_path = visualizer.plot_problem_distribution(sample_problems)
        print(f"     ✅ Saved: {dist_path}\n")
        
        # 2. Problem count bar
        print("  2️⃣  Generating problem count bar chart...")
        count_path = visualizer.plot_problem_count_bar(sample_problems)
        print(f"     ✅ Saved: {count_path}\n")
        
        # 3. Theory coverage
        print("  3️⃣  Generating theory coverage chart...")
        theory_path = visualizer.plot_theory_coverage(sample_theories)
        print(f"     ✅ Saved: {theory_path}\n")
        
        # 4. Statistics dashboard
        print("  4️⃣  Generating statistics dashboard...")
        dashboard_path = visualizer.plot_statistics_summary(sample_problems, sample_theories)
        print(f"     ✅ Saved: {dashboard_path}\n")
        
        # 5. Function example
        print("  5️⃣  Generating function plot example...")
        func_path = visualizer.plot_function_example("Test Functions")
        print(f"     ✅ Saved: {func_path}\n")
        
        print("="*60)
        print("✅ ALL GRAPHS GENERATED SUCCESSFULLY!")
        print("="*60)
        print("\n📊 Generated files:")
        print(f"  📁 Output directory: {visualizer.output_dir}\n")
        print(f"  📄 Files created:")
        print(f"     1. {Path(dist_path).name}")
        print(f"     2. {Path(count_path).name}")
        print(f"     3. {Path(theory_path).name}")
        print(f"     4. {Path(dashboard_path).name}")
        print(f"     5. {Path(func_path).name}")
        
        print("\n🎉 Visualization test completed successfully!")
        print("\nYou can now use these graphs with:")
        print("  • Web App:   python web_app_graphs.py")
        print("  • Desktop GUI: python gui_app_graphs.py")
        print("  • CLI:        python src/homework_solver.py your_file.pdf")
        print("\n" + "="*60 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error during visualization: {str(e)}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == '__main__':
    success = test_visualizer()
    sys.exit(0 if success else 1)
