"""
Unit tests for AI Homework Analyzer & Solver
"""

import unittest
import sys
import os

# Add src directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from homework_solver import TheoryBase, ProblemAnalyzer, SolutionGenerator, ProblemType


class TestTheoryBase(unittest.TestCase):
    """Test theory database"""
    
    def test_theories_dict_exists(self):
        """Test that theories dictionary exists and is not empty"""
        self.assertIsNotNone(TheoryBase.THEORIES)
        self.assertTrue(len(TheoryBase.THEORIES) > 0)
    
    def test_calculus_theories(self):
        """Test that calculus theories are defined"""
        self.assertIn("calculus", TheoryBase.THEORIES)
        self.assertIn("derivative", TheoryBase.THEORIES["calculus"])
        self.assertIn("integral", TheoryBase.THEORIES["calculus"])
    
    def test_engineering_theories(self):
        """Test that major engineering theories are defined"""
        expected_domains = [
            "mechanics_of_materials", "dynamics", "thermodynamics", 
            "fluid_mechanics", "heat_transfer", "circuit_analysis",
            "electromagnetics", "mass_balance", "aerodynamics"
        ]
        for domain in expected_domains:
            self.assertIn(domain, TheoryBase.THEORIES, 
                         f"Missing domain: {domain}")


class TestProblemAnalyzer(unittest.TestCase):
    """Test problem analyzer"""
    
    def test_problem_type_identification(self):
        """Test problem type identification"""
        analyzer = ProblemAnalyzer("dummy.pdf")
        
        # Test calculus
        calc_problem = "Find the derivative of x^3 + 2x using chain rule"
        result = analyzer.identify_problem_type(calc_problem)
        self.assertEqual(result, "calculus")
        
        # Test circuit analysis
        circuit_problem = "Calculate the voltage and current using Kirchhoff's law"
        result = analyzer.identify_problem_type(circuit_problem)
        self.assertEqual(result, "circuit_analysis")
        
        # Test thermodynamics
        thermo_problem = "Calculate entropy and enthalpy for the cycle"
        result = analyzer.identify_problem_type(thermo_problem)
        self.assertEqual(result, "thermodynamics")
    
    def test_problem_type_fallback(self):
        """Test fallback to 'other' for unrecognized problems"""
        analyzer = ProblemAnalyzer("dummy.pdf")
        unrecognized = "What is the meaning of life?"
        result = analyzer.identify_problem_type(unrecognized)
        self.assertEqual(result, "other")


class TestSolutionGenerator(unittest.TestCase):
    """Test solution generator"""
    
    def test_solution_format(self):
        """Test that solutions are formatted correctly"""
        gen = SolutionGenerator()
        
        solution = gen.format_solution(
            1,
            "Find the derivative of f(x) = x^2",
            "calculus"
        )
        
        # Check that solution contains expected sections
        self.assertIn("PROBLEM 1", solution)
        self.assertIn("[CALCULUS]", solution)
        self.assertIn("📋 PROBLEM STATEMENT", solution)
        self.assertIn("🧠 RELEVANT THEORIES", solution)
        self.assertIn("📝 SOLUTION STEPS", solution)
        self.assertIn("💬 DETAILED VERBAL WALKTHROUGH", solution)
    
    def test_theories_included_in_solution(self):
        """Test that relevant theories are included in solution"""
        gen = SolutionGenerator()
        
        solution = gen.format_solution(
            1,
            "Calculate stress and strain",
            "mechanics_of_materials"
        )
        
        # Check that mechanics theories are included
        self.assertIn("STRESS", solution)
        self.assertIn("STRAIN", solution)


class TestProblemType(unittest.TestCase):
    """Test ProblemType enum"""
    
    def test_problem_types_exist(self):
        """Test that all expected problem types are defined"""
        expected_types = [
            "MATH", "PHYSICS", "CHEMISTRY", "MECHANICAL", "CIVIL",
            "ELECTRICAL", "CHEMICAL", "AEROSPACE", "CALCULUS",
            "THERMODYNAMICS", "FLUID_MECHANICS", "CIRCUITS"
        ]
        
        for problem_type in expected_types:
            self.assertTrue(hasattr(ProblemType, problem_type))


class TestIntegration(unittest.TestCase):
    """Integration tests"""
    
    def test_full_workflow(self):
        """Test the full analysis workflow"""
        # Create a dummy analyzer
        analyzer = ProblemAnalyzer("test.pdf")
        
        # Set raw text manually (simulating PDF extraction)
        analyzer.raw_text = """
        --- PAGE 1 ---
        Problem 1: Find the derivative of f(x) = 3x^2 + 2x - 5
        
        Problem 2: A beam with stress 50 MPa and cross-section 10 cm^2
        """
        
        # Parse problems
        problems = analyzer.parse_problems()
        
        self.assertIsNotNone(problems)
        self.assertTrue(len(problems) > 0)
        
        # Check that problem types were identified
        problem_types = [p['type'] for p in problems]
        self.assertIn('calculus', problem_types)


def run_tests():
    """Run all tests"""
    unittest.main(argv=[''], exit=False, verbosity=2)


if __name__ == '__main__':
    run_tests()
run tema2-ejercicios.pdf

