"""
Test runner for the homework solver with sample data
"""

import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from homework_solver import ProblemAnalyzer, SolutionGenerator


def test_with_sample_data():
    """Test the solver with sample homework data"""
    
    print("\n" + "="*100)
    print("🎓 AI HOMEWORK ANALYZER & SOLVER - TEST RUN")
    print("="*100 + "\n")
    
    # Read sample homework
    sample_file = os.path.join(os.path.dirname(__file__), '..', 'samples', 'sample_homework.txt')
    
    if not os.path.exists(sample_file):
        print(f"❌ Sample file not found: {sample_file}")
        return False
    
    print("📂 Loading sample homework from: samples/sample_homework.txt\n")
    
    with open(sample_file, 'r', encoding='utf-8') as f:
        sample_text = f.read()
    
    # Create analyzer
    analyzer = ProblemAnalyzer("test.pdf")
    analyzer.raw_text = sample_text
    
    # Parse problems
    print("Step 1️⃣  : PARSING PROBLEMS")
    print("-"*100)
    problems = analyzer.parse_problems()
    print(f"✅ Found {len(problems)} problems\n")
    
    # Display identified problems
    print("Step 2️⃣  : PROBLEMS IDENTIFIED")
    print("-"*100)
    for idx, problem in enumerate(problems, 1):
        problem_text = problem['text'][:80] + "..." if len(problem['text']) > 80 else problem['text']
        print(f"  Problem {idx}: {problem['type'].upper()}")
        print(f"  {problem_text}\n")
    
    # Generate solutions for first 3 problems
    print("\nStep 3️⃣  : GENERATING SOLUTIONS FOR FIRST 3 PROBLEMS")
    print("-"*100 + "\n")
    
    solution_gen = SolutionGenerator()
    all_solutions = ""
    
    for problem in problems[:3]:
        solution = solution_gen.format_solution(
            problem['number'],
            problem['text'],
            problem['type']
        )
        all_solutions += solution
        print(f"✅ Generated solution for Problem {problem['number']}")
    
    print("\n" + "="*100)
    print("📊 SUMMARY")
    print("="*100)
    print(f"Total Problems Found: {len(problems)}")
    print(f"Solutions Generated: 3 (sample)")
    print(f"Problem Types Identified: {len(set(p['type'] for p in problems))}")
    print("")
    print("Problem Type Distribution:")
    type_count = {}
    for problem in problems:
        ptype = problem['type']
        type_count[ptype] = type_count.get(ptype, 0) + 1
    
    for ptype, count in sorted(type_count.items()):
        print(f"  • {ptype.upper()}: {count} problem(s)")
    
    # Save full report
    output_file = "test_analysis_report.txt"
    
    full_report = f"\n📚 TEST HOMEWORK ANALYSIS REPORT\n"
    full_report += f"{'='*100}\n"
    full_report += f"SAMPLE DATA FROM: samples/sample_homework.txt\n"
    full_report += f"Total Problems Parsed: {len(problems)}\n"
    full_report += f"{'='*100}\n\n"
    
    for problem in problems:
        solution = solution_gen.format_solution(
            problem['number'],
            problem['text'],
            problem['type']
        )
        full_report += solution
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(full_report)
    
    print(f"\n✅ Full analysis saved to: {output_file}")
    print("\n" + "="*100)
    print("TEST COMPLETED SUCCESSFULLY ✅")
    print("="*100 + "\n")
    
    return True


if __name__ == "__main__":
    success = test_with_sample_data()
    sys.exit(0 if success else 1)
