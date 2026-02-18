"""
Advanced Solution Generator with Step-by-Step Analysis
Generates detailed solutions for each problem independently
"""

import os
from pathlib import Path


class AdvancedSolutionGenerator:
    """Generates comprehensive step-by-step solutions for individual problems"""
    
    def __init__(self):
        self.solution_templates = {
            'calculus': self.solve_calculus,
            'algebra': self.solve_algebra,
            'physics': self.solve_physics,
            'chemistry': self.solve_chemistry,
            'geometry': self.solve_geometry,
            'physics': self.solve_physics,
            'math': self.solve_math
        }
    
    def generate_solution(self, problem_number, problem_text, problem_type):
        """Generate a complete solution for a single problem"""
        
        problem_type_lower = problem_type.lower() if problem_type else 'math'
        
        # Get the appropriate solver
        solver = self.solution_templates.get(problem_type_lower, self.solve_generic)
        
        return solver(problem_number, problem_text, problem_type)
    
    def solve_generic(self, num, text, ptype):
        """Generic problem solver"""
        return {
            'number': num,
            'type': ptype,
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Problem Analysis',
                    'description': 'Read and understand what is being asked',
                    'action': 'Identify given information and required output'
                },
                {
                    'step': 2,
                    'title': 'Gather Information',
                    'description': 'List all given data and constraints',
                    'action': 'Write down: known values, formulas, constraints'
                },
                {
                    'step': 3,
                    'title': 'Identify Method',
                    'description': 'Determine the approach to solve',
                    'action': 'Choose appropriate techniques and formulas'
                },
                {
                    'step': 4,
                    'title': 'Execute Solution',
                    'description': 'Apply selected method step by step',
                    'action': 'Show all calculations clearly'
                },
                {
                    'step': 5,
                    'title': 'Verify Result',
                    'description': 'Check if answer makes sense',
                    'action': 'Verify units, reasonableness, alternative methods'
                }
            ],
            'theories': [
                'Problem-solving methodology',
                'Logical reasoning',
                'Mathematical principles',
                'Verification techniques'
            ],
            'key_concepts': 'Apply systematic approach to solve the given problem',
            'common_mistakes': 'Not reading carefully, skipping verification steps'
        }
    
    def solve_calculus(self, num, text, ptype):
        """Calculus problem solver"""
        return {
            'number': num,
            'type': ptype,
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Identify Problem Type',
                    'description': 'Determine if this is a limit, derivative, integral, or series problem',
                    'action': 'Look for keywords: limit as x→, find derivative, integrate, sum of series'
                },
                {
                    'step': 2,
                    'title': 'Recall Relevant Theorems',
                    'description': 'Apply appropriate calculus theorems',
                    'action': 'Use derivative rules, integration techniques, limit properties'
                },
                {
                    'step': 3,
                    'title': 'Simplify the Expression',
                    'description': 'Manipulate the function or limit into workable form',
                    'action': 'Factor, rationalize, use L\'Hôpital\'s rule if needed'
                },
                {
                    'step': 4,
                    'title': 'Apply Calculus Rules',
                    'description': 'Execute derivative, integral, or limit calculation',
                    'action': 'Power rule, product rule, chain rule, or integration methods'
                },
                {
                    'step': 5,
                    'title': 'Evaluate and Verify',
                    'description': 'Get final answer and check for correctness',
                    'action': 'Substitute values, check dimensions, verify with alternative method'
                }
            ],
            'theories': [
                'Derivative Rules (Power, Product, Chain)',
                'Integration Techniques (Substitution, Parts)',
                'Limit Properties and L\'Hôpital\'s Rule',
                'Fundamental Theorem of Calculus',
                'Taylor Series Expansion'
            ],
            'key_concepts': 'Calculus is about rates of change (derivatives) and accumulation (integrals)',
            'common_mistakes': 'Forgetting chain rule, incorrect limits of integration, algebraic errors'
        }
    
    def solve_algebra(self, num, text, ptype):
        """Algebra problem solver"""
        return {
            'number': num,
            'type': ptype,
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Identify Equation Type',
                    'description': 'Determine if linear, quadratic, or higher degree',
                    'action': 'Count highest power of variable, look for special forms'
                },
                {
                    'step': 2,
                    'title': 'Isolate Variable Terms',
                    'description': 'Move all terms with variables to one side',
                    'action': 'Add/subtract constants from both sides'
                },
                {
                    'step': 3,
                    'title': 'Simplify',
                    'description': 'Combine like terms and reduce the equation',
                    'action': 'Use distributive property, combine coefficients'
                },
                {
                    'step': 4,
                    'title': 'Solve for Variable',
                    'description': 'Get the variable by itself',
                    'action': 'Divide by coefficient, use quadratic formula if needed, factor'
                },
                {
                    'step': 5,
                    'title': 'Check Solution',
                    'description': 'Substitute back into original equation',
                    'action': 'Verify both sides are equal, check for extraneous solutions'
                }
            ],
            'theories': [
                'Linear Equations',
                'Quadratic Equations and Factoring',
                'Polynomial Operations',
                'Equation Properties (equality)',
                'Rational Functions'
            ],
            'key_concepts': 'Algebra is about finding unknown values using equation properties',
            'common_mistakes': 'Sign errors, forgetting to apply operations to both sides, missed solutions'
        }
    
    def solve_physics(self, num, text, ptype):
        """Physics problem solver"""
        return {
            'number': num,
            'type': ptype,
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Identify Physics Concept',
                    'description': 'Determine which physics principle applies',
                    'action': 'Mechanics, forces, energy, motion, waves, electricity, etc.'
                },
                {
                    'step': 2,
                    'title': 'Extract Given Data',
                    'description': 'List all given values with their units',
                    'action': 'Write: m = ___kg, v = ___m/s, t = ___s, F = ___N, etc.'
                },
                {
                    'step': 3,
                    'title': 'Select Relevant Formula',
                    'description': 'Choose equation(s) that connect given and unknown',
                    'action': 'Use F=ma, E=mc², v=d/t, F=kx, etc.'
                },
                {
                    'step': 4,
                    'title': 'Substitute and Calculate',
                    'description': 'Plug in values and solve algebraically',
                    'action': 'Show all arithmetic, track significant figures'
                },
                {
                    'step': 5,
                    'title': 'State Answer with Units',
                    'description': 'Give final answer with proper units and significant figures',
                    'action': 'Include direction if vector, check reasonableness'
                }
            ],
            'theories': [
                'Newton\'s Laws of Motion',
                'Energy Conservation',
                'Kinematic Equations',
                'Work and Power',
                'Momentum Conservation',
                'Simple Harmonic Motion'
            ],
            'key_concepts': 'Physics connects real-world phenomena to mathematical equations',
            'common_mistakes': 'Unit conversion errors, forgetting to square values, sign errors in direction'
        }
    
    def solve_chemistry(self, num, text, ptype):
        """Chemistry problem solver"""
        return {
            'number': num,
            'type': ptype,
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Identify Chemistry Type',
                    'description': 'Stoichiometry, kinetics, equilibrium, thermodynamics, or acid-base',
                    'action': 'Read problem context carefully'
                },
                {
                    'step': 2,
                    'title': 'Balance Chemistry Equation (if needed)',
                    'description': 'Ensure atoms and charge are balanced',
                    'action': 'Equal atoms on both sides, proper coefficients'
                },
                {
                    'step': 3,
                    'title': 'Use Molar Relationships',
                    'description': 'Convert between moles, mass, volume using stoichiometry',
                    'action': 'Use molar mass, Avogadro\'s number, molar ratios'
                },
                {
                    'step': 4,
                    'title': 'Apply Chemical Principles',
                    'description': 'Use gas laws, equilibrium constants, or reaction rates',
                    'action': 'PV=nRT, Ka/Kb, rate laws, ΔH, ΔG'
                },
                {
                    'step': 5,
                    'title': 'Report Answer',
                    'description': 'Include concentration, mass, volume, or pressure with units',
                    'action': 'Significant figures, proper notation'
                }
            ],
            'theories': [
                'Stoichiometry and Mole Concept',
                'Chemical Equations and Balancing',
                'Equilibrium and Le Chatelier\'s Principle',
                'Acid-Base Chemistry',
                'Thermodynamics',
                'Reaction Kinetics'
            ],
            'key_concepts': 'Chemistry is about quantitative relationships in reactions',
            'common_mistakes': 'Unbalanced equations, unit conversion, molar mass calculation errors'
        }
    
    def solve_geometry(self, num, text, ptype):
        """Geometry problem solver"""
        return {
            'number': num,
            'type': ptype,
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Visualize the Problem',
                    'description': 'Draw a diagram of the geometric figure',
                    'action': 'Label known angles, sides, properties'
                },
                {
                    'step': 2,
                    'title': 'Identify Geometric Properties',
                    'description': 'Apply angle theorems, parallel lines, congruence',
                    'action': 'Use properties of triangles, circles, polygons'
                },
                {
                    'step': 3,
                    'title': 'Set Up Equations',
                    'description': 'Convert geometric relationships to equations',
                    'action': 'Pythagorean theorem, area formulas, angle sums'
                },
                {
                    'step': 4,
                    'title': 'Solve Algebraically',
                    'description': 'Solve the equations from step 3',
                    'action': 'Find unknown lengths, angles, or areas'
                },
                {
                    'step': 5,
                    'title': 'Interpret Result',
                    'description': 'Relate algebraic solution back to geometry',
                    'action': 'State answer with correct units and geometric interpretation'
                }
            ],
            'theories': [
                'Triangle Properties and Pythagorean Theorem',
                'Circle Theorems',
                'Area and Volume Formulas',
                'Trigonometry (Sin, Cos, Tan)',
                'Coordinate Geometry',
                'Transformation Geometry'
            ],
            'key_concepts': 'Geometry connects shapes to mathematics using properties and formulas',
            'common_mistakes': 'Wrong formula application, measurement errors, unit mistakes'
        }
    
    def solve_math(self, num, text, ptype):
        """General math problem solver"""
        return self.solve_generic(num, text, ptype)


def generate_analysis_report(problems, theories_dict):
    """Generate comprehensive analysis report with separate solutions"""
    
    report = {
        'summary': {
            'total_problems': len(problems),
            'problem_types': list(set(p.get('type', 'Unknown').upper() for p in problems)),
            'total_theories': sum(len(t) for t in theories_dict.values())
        },
        'problems_analyzed': []
    }
    
    solver = AdvancedSolutionGenerator()
    
    for idx, problem in enumerate(problems, 1):
        solution = solver.generate_solution(
            idx,
            problem.get('text', 'No description'),
            problem.get('type', 'math')
        )
        report['problems_analyzed'].append(solution)
    
    return report
