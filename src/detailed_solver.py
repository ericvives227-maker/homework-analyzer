"""
Detailed Solution Generator with Complete Step-by-Step Explanations
Provides comprehensive solutions with full reasoning and worked examples
"""

import re


class DetailedSolutionGenerator:
    """Generates detailed, comprehensive step-by-step solutions"""
    
    def __init__(self):
        self.problem_patterns = {
            'derivative': r'(deriv|d/d|prime|slope)',
            'integral': r'(integr|∫|sum)',
            'limit': r'(limit|lim|approaches|→)',
            'equation': r'(solve|find|equation|=)',
            'simplify': r'(simplify|reduce|factor)',
            'geometry': r'(area|volume|perimeter|angle|triangle|circle)',
            'force': r'(force|newton|acceleration|F=ma)',
            'energy': r'(energy|work|kinetic|potential)',
            'chemistry': r'(stoich|balance|react|mole)',
            'algebra': r'(quadratic|linear|factor|solve)'
        }
    
    def detect_problem_type(self, text):
        """Detect problem type from text"""
        text_lower = text.lower()
        for ptype, pattern in self.problem_patterns.items():
            if re.search(pattern, text_lower, re.IGNORECASE):
                return ptype
        return 'general'
    
    def generate_detailed_solution(self, problem_num, problem_text, problem_type):
        """Generate comprehensive solution for a problem"""
        
        detected_type = self.detect_problem_type(problem_text)
        
        # Map to specific solvers
        if 'derivative' in detected_type or 'calculus' in problem_type.lower():
            return self._solve_derivative(problem_num, problem_text)
        elif 'integral' in detected_type:
            return self._solve_integral(problem_num, problem_text)
        elif 'limit' in detected_type:
            return self._solve_limit(problem_num, problem_text)
        elif any(x in detected_type for x in ['force', 'energy', 'acceleration']):
            return self._solve_physics(problem_num, problem_text)
        elif 'chemistry' in detected_type or 'stoich' in detected_type:
            return self._solve_chemistry(problem_num, problem_text)
        elif any(x in detected_type for x in ['geometry', 'area', 'volume']):
            return self._solve_geometry(problem_num, problem_text)
        elif 'algebra' in problem_type.lower() or 'equation' in detected_type:
            return self._solve_algebra(problem_num, problem_text)
        else:
            return self._solve_general(problem_num, problem_text)
    
    def _solve_derivative(self, num, text):
        """Detailed derivative solution"""
        return {
            'number': num,
            'type': 'CALCULUS - DERIVATIVES',
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Identify the Function and Its Form',
                    'detailed_explanation': '''Read the problem carefully to identify:
• The function f(x) that needs to be differentiated
• Whether it's polynomial, trigonometric, exponential, logarithmic, or a combination
• If it's a quotient (use quotient rule) or product (use product rule)
• If it contains a function inside another function (chain rule needed)

Keyword indicators:
- "Find the derivative" → Need to find f'(x)
- "Find the slope" → Finding derivative at a point
- "Rate of change" → First derivative interpreted in context
- "Find the tangent line" → Need derivative to get slope
- "Concavity" → Need second derivative f''(x)''',
                    'worked_example': 'For f(x) = 3x⁴ + 2x² - 5: Identify polynomial form with multiple terms'
                },
                {
                    'step': 2,
                    'title': 'Select the Appropriate Differentiation Rule(s)',
                    'detailed_explanation': '''Choose the correct rule(s):

POWER RULE: d/dx[xⁿ] = n·xⁿ⁻¹
- Apply to each term of polynomials
- Example: d/dx[x⁴] = 4x³, d/dx[x] = 1, d/dx[5] = 0

PRODUCT RULE: d/dx[u·v] = u'·v + u·v'
- When TWO functions are multiplied
- First·(derivative of second) + Second·(derivative of first)
- Example: f(x) = x² · sin(x) needs product rule

QUOTIENT RULE: d/dx[u/v] = (u'·v - u·v')/v²
- When function is a fraction
- (Top's derivative · Bottom) - (Top · Bottom's derivative) / (Bottom)²
- Example: f(x) = (x² + 1)/(x - 1) needs quotient rule

CHAIN RULE: d/dx[f(g(x))] = f'(g(x)) · g'(x)
- When one function is inside another (composition)
- Differentiate outer function (keeping inner the same), multiply by derivative of inner
- Example: d/dx[sin(x²)] = cos(x²) · 2x

TRIGONOMETRIC: 
- d/dx[sin(x)] = cos(x)
- d/dx[cos(x)] = -sin(x)
- d/dx[tan(x)] = sec²(x)

EXPONENTIAL & LOGARITHMIC:
- d/dx[eˣ] = eˣ
- d/dx[aˣ] = aˣ · ln(a)
- d/dx[ln(x)] = 1/x
- d/dx[logₐ(x)] = 1/(x·ln(a))''',
                    'worked_example': 'For f(x) = 3x⁴ + 2x² - 5: Use power rule on each term separately'
                },
                {
                    'step': 3,
                    'title': 'Apply the Rule(s) Step-by-Step',
                    'detailed_explanation': '''Execute the differentiation carefully:

STEP-BY-STEP APPLICATION:
1. Identify each term/component
2. Apply the rule to each part
3. Write out intermediate results clearly
4. Combine like terms

Show ALL work:
- Don't skip steps
- Clearly show exponent changes
- Show coefficient multiplications
- Keep careful track of signs

Organize as:
f(x) = [first component] + [second component] - [third component]
f'(x) = [derivative of first] + [derivative of second] - [derivative of third]
f'(x) = [simplified result]''',
                    'worked_example': 'f(x) = 3x⁴ + 2x² - 5\nf\'(x) = 3·(4x³) + 2·(2x) - 0\nf\'(x) = 12x³ + 4x'
                },
                {
                    'step': 4,
                    'title': 'Simplify and Verify',
                    'detailed_explanation': '''SIMPLIFICATION:
- Combine like terms if any
- Factor out common factors if helpful
- Ensure no negative exponents remain (unless originally required)
- Check for arithmetic errors

VERIFICATION METHODS:
1. Dimensional analysis: exponents should decrease by 1
2. Special case check: plug in x=0 or x=1 if possible
3. Limit check: as x→∞, derivative behavior matches original function trend
4. Graph interpretation: derivative should match slope visually''',
                    'worked_example': 'f\'(x) = 12x³ + 4x = 4x(3x² + 1) [factored form]\nVerify: x³ → x² (exponent decreased by 1) ✓'
                },
                {
                    'step': 5,
                    'title': 'Interpret the Result in Context',
                    'detailed_explanation': '''INTERPRETATION:
- State the derivative function f'(x)
- If asked for slope at specific point: evaluate f'(x₀)
- If asked for critical points: solve f'(x) = 0
- If tangent line requested: y - y₀ = m(x - x₀) where m = f'(x₀)
- If rate of change: express units (units of y per unit of x)

COMMON QUESTIONS:
• "Find f'(2)" → Substitute x=2 into f'(x) to get slope at that point
• "Where is tangent horizontal?" → Solve f'(x) = 0
• "Is function increasing/decreasing at x=3?" → If f'(3)>0 → increasing, if f'(3)<0 → decreasing
• "Find equation of tangent line at x=1" → Use point-slope form with slope from f'(1)''',
                    'worked_example': 'f\'(x) = 12x³ + 4x is the derivative function\nAt x=1: f\'(1) = 12(1)³ + 4(1) = 12 + 4 = 16 (slope at x=1)\nTangent line at (x₀,y₀) with slope 16: y - y₀ = 16(x - x₀)'
                }
            ],
            'theories': [
                'Derivative Definition: f\'(x) = lim[h→0] (f(x+h) - f(x))/h',
                'Power Rule: d/dx[xⁿ] = n·xⁿ⁻¹',
                'Product Rule: d/dx[u·v] = u\'v + uv\'',
                'Quotient Rule: d/dx[u/v] = (u\'v - uv\')/v²',
                'Chain Rule: d/dx[f(g(x))] = f\'(g(x))·g\'(x)',
                'Trigonometric Derivatives',
                'Exponential and Logarithmic Derivatives',
                'Higher Order Derivatives: f\'\'(x), f\'\'\'(x), etc.'
            ],
            'key_concepts': '''Derivatives measure instantaneous rate of change. 
- First derivative f'(x) gives slope of tangent line
- f'(x) > 0 means function is increasing
- f'(x) < 0 means function is decreasing  
- f'(x) = 0 indicates critical points (maxima/minima)
- Multiple derivative rules exist for different function types''',
            'common_mistakes': '''
1. Forgetting to apply chain rule for composite functions
2. Sign errors with negative terms
3. Mixing up product rule with distribution
4. Using wrong exponent rule (exponent doesn't just multiply coefficient)
5. Not simplifying final answer
6. Forgetting to include all terms of the function
7. Incorrectly applying quotient rule signs (numerator derivation order matters)'''
        }
    
    def _solve_integral(self, num, text):
        """Detailed integral solution"""
        return {
            'number': num,
            'type': 'CALCULUS - INTEGRALS',
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Identify Integral Type and Bounds',
                    'detailed_explanation': '''Determine the type of integral:

INDEFINITE INTEGRAL (Antiderivative):
- Form: ∫ f(x) dx
- Problem says: "Find the antiderivative" or "Find ∫f(x)dx"
- Answer includes "+ C" (arbitrary constant)
- Represents family of antiderivative functions

DEFINITE INTEGRAL (Area):
- Form: ∫ₐᵇ f(x) dx from a to b
- Problem says: "Evaluate the integral from a to b" or "Find area under curve"
- Answer is a NUMBER (specific value)
- Represents area between curve and x-axis between x=a and x=b

IMPROPER INTEGRAL:
- When bounds are ∞ or function has discontinuity in interval
- Requires limit notation: lim[t→∞] ∫...dt''',
                    'worked_example': '∫ (3x² + 2x) dx is indefinite\n∫₀² (3x² + 2x) dx is definite (bounds 0 to 2)'
                },
                {
                    'step': 2,
                    'title': 'Choose Integration Method',
                    'detailed_explanation': '''Select appropriate technique:

POWER RULE (Most Common):
∫ xⁿ dx = (xⁿ⁺¹)/(n+1) + C, where n ≠ -1
- Add 1 to exponent, divide by new exponent
- Example: ∫ x⁵ dx = x⁶/6 + C

CONSTANT MULTIPLE:
∫ k·f(x) dx = k·∫ f(x) dx
- Pull constant out front
- Then integrate the remaining function
- Example: ∫ 5x² dx = 5·∫ x² dx = 5·(x³/3) + C

SUM/DIFFERENCE RULE:
∫ [f(x) + g(x)] dx = ∫ f(x) dx + ∫ g(x) dx
- Integrate each term separately
- Then add results together

U-SUBSTITUTION:
- When you have a composite function
- Let u = inner function, find du
- Rewrite integral in terms of u
- Integrate with respect to u
- Back-substitute to get answer in x

INTEGRATION BY PARTS:
∫ u dv = uv - ∫ v du
- Use LIATE to choose u (Logarithmic, Inverse trig, Algebraic, Trig, Exponential)
- For products of different function types

PARTIAL FRACTIONS:
- When denominator is polynomial
- Break into simpler fractions
- Integrate each simpler fraction separately''',
                    'worked_example': '∫ (4x³ - 3x + 1) dx uses power rule on each term'
                },
                {
                    'step': 3,
                    'title': 'Execute Integration',
                    'detailed_explanation': '''Perform integration carefully:

FOR INDEFINITE INTEGRALS:
1. Integrate each term using appropriate rule
2. Show all work clearly
3. Add "+ C" at the very end
4. Format: ∫[original] = [antiderivative] + C

FOR DEFINITE INTEGRALS:
1. First find the antiderivative F(x)
2. Apply Fundamental Theorem: ∫ₐᵇ f(x) dx = F(b) - F(a)
3. Evaluate antiderivative at upper bound
4. Evaluate antiderivative at lower bound
5. Subtract: top value - bottom value
6. Do NOT include "+ C" for definite integrals (cancels out)

ORGANIZATION:
Step A: Identify form of each term
Step B: Apply rule to each term
Step C: Write accumulated result
Step D: Simplify
Step E: (Definite only) Apply bounds using Fundamental Theorem''',
                    'worked_example': '∫ (4x³ - 3x + 1) dx\n= 4·∫x³dx - 3·∫xdx + ∫1dx\n= 4·(x⁴/4) - 3·(x²/2) + x + C\n= x⁴ - (3x²/2) + x + C'
                },
                {
                    'step': 4,
                    'title': 'Apply Bounds (if Definite) and Simplify',
                    'detailed_explanation': '''APPLYING BOUNDS FOR DEFINITE INTEGRALS:

Fundamental Theorem of Calculus:
If F\'(x) = f(x), then ∫ₐᵇ f(x) dx = F(b) - F(a)

Step 1: Evaluate F at upper bound x = b: F(b)
Step 2: Evaluate F at lower bound x = a: F(a)  
Step 3: Calculate difference: F(b) - F(a)
Step 4: Simplify the numerical result

NOTATION:
∫ₐᵇ f(x) dx = [F(x)]|ₐᵇ = F(b) - F(a)

Common mistakes with bounds:
- Using wrong bound values
- Forgetting to subtract (must be upper minus lower)
- Not fully evaluating both bounds
- Sign errors in subtraction''',
                    'worked_example': '∫₀² (4x³ - 3x + 1) dx\n= [x⁴ - (3x²/2) + x]|₀²\n= [2⁴ - 3(2²)/2 + 2] - [0⁴ - 3(0²)/2 + 0]\n= [16 - 6 + 2] - [0]\n= 12'
                },
                {
                    'step': 5,
                    'title': 'Verify Result and Interpret',
                    'detailed_explanation': '''VERIFICATION:
1. Check by differentiation: Take your antiderivative F(x), differentiate it, should get f(x)
   - If ∫ f(x) dx = F(x) + C, then F\'(x) should equal f(x)
2. Dimensional analysis: Check units make sense
3. Reasonableness: For areas, is answer positive? Does magnitude seem right?

INTERPRETATION:

For INDEFINITE INTEGRALS:
- State the family of antiderivatives: "The antiderivative is..."
- Explain meaning: "This represents all functions whose derivative is f(x)"
- Note: "+C represents the vertical shift of all possible curves"

For DEFINITE INTEGRALS:
- Interpret the value: "The area under the curve y = f(x) from x = a to x = b is [answer] square units"
- Consider sign: If negative, curve is below x-axis in that region
- Consider context: In physics (distance), economics (revenue), etc.

SPECIAL CASES:
- If answer is 0: curve enters above x-axis and below equally
- If answer is negative: curve mostly below x-axis
- Large positive answer: significant area under curve''',
                    'worked_example': 'Verification: d/dx[x⁴ - (3x²/2) + x] = 4x³ - 3x + 1 ✓ Correct!\nFor ∫₀² (4x³ - 3x + 1) dx = 12: Area under curve from x=0 to x=2 is 12 square units'
                }
            ],
            'theories': [
                'Fundamental Theorem of Calculus: ∫ₐᵇ f\'(x) dx = f(b) - f(a)',
                'Power Rule for Integration: ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C',
                'Sum and Difference Rules',
                'U-Substitution Technique',
                'Integration by Parts',
                'Partial Fractions Decomposition',
                'Trigonometric Integrals',
                'Exponential and Logarithmic Integrals'
            ],
            'key_concepts': '''Integration is the reverse of differentiation (antidifferentiation).
- Indefinite integral gives a family of functions  
- Definite integral gives the numerical area under a curve
- "+C" only appears in indefinite integrals
- Bounds matter: ∫ₐᵇ is different from ∫ᵇₐ (opposite signs)
- Many integration techniques exist for different function types''',
            'common_mistakes': '''
1. Forgetting the "+ C" in indefinite integrals
2. Including "+ C" in definite integrals (it cancels, don't write it)
3. Incorrect exponent: exponent should go UP by 1, then DIVIDE by new exponent
4. Sign errors when bounds are negative
5. Wrong order in subtraction: must be F(upper) - F(lower)
6. Not fully evaluating at both bounds
7. Using wrong integration technique for the function type
8. Arithmetic errors in exponent or constant calculations'''
        }
    
    def _solve_limit(self, num, text):
        """Detailed limit solution"""
        return {
            'number': num,
            'type': 'CALCULUS - LIMITS',
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Write the Limit in Standard Notation',
                    'detailed_explanation': 'Parse problem to write: lim[x→a] f(x) where a is where x approaches and f(x) is the function',
                    'worked_example': 'If problem says "What does 3x² + 2 approach as x approaches 1?"\nWrite: lim[x→1] (3x² + 2)'
                },
                {
                    'step': 2,
                    'title': 'Try Direct Substitution',
                    'detailed_explanation': 'Substitute x = a directly into f(x). If you get a number (not 0/0 or ∞/∞), that IS the limit.',
                    'worked_example': 'lim[x→1] (3x² + 2) = 3(1)² + 2 = 5 → Answer is 5'
                },
                {
                    'step': 3,
                    'title': 'Handle Indeterminate Forms',
                    'detailed_explanation': 'If direct substitution gives 0/0, ∞/∞, or other indeterminate form, use algebraic techniques:\n• Factor and cancel\n• Rationalize (multiply by conjugate)\n• Combine fractions\n• L\'Hôpital\'s Rule: lim[x→a] f(x)/g(x) = lim[x→a] f\'(x)/g\'(x)',
                    'worked_example': 'For 0/0 form: factor numerator and denominator, cancel common terms'
                },
                {
                    'step': 4,
                    'title': 'Evaluate After Simplification',
                    'detailed_explanation': 'After algebraic manipulation, substitute x = a into simplified form',
                    'worked_example': 'After factoring and canceling: substitute back to find the limit value'
                },
                {
                    'step': 5,
                    'title': 'State the Limit or Conclusion',
                    'detailed_explanation': '''State result clearly:
• "The limit exists and equals [value]"
• "The limit does not exist"
• "The limit is infinity (approaches unbounded)"
• Describe one-sided behavior if needed''',
                    'worked_example': 'lim[x→1] (3x² + 2) = 5 means as x gets arbitrarily close to 1, the function value approaches 5'
                }
            ],
            'theories': [
                'Limit Definition and Notation',
                'Direct Substitution',
                'Indeterminate Forms (0/0, ∞/∞, etc.)',
                'L\'Hôpital\'s Rule',
                'Limits at Infinity',
                'One-sided Limits'
            ],
            'key_concepts': 'Limits describe what value a function approaches as x approaches some value.',
            'common_mistakes': 'Not recognizing indeterminate forms, incorrect algebraic manipulation, not checking one-sided limits'
        }
    
    def _solve_physics(self, num, text):
        """Detailed physics solution"""
        return {
            'number': num,
            'type': 'PHYSICS',
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Identify Position, Forces, and Constraints',
                    'detailed_explanation': '''Read problem carefully:
GIVEN INFORMATION:
• List all numerical values with units (mass, velocity, distance, time, force, etc.)
• Identify what's being asked to find
• Identify the type of problem (kinematics, dynamics, energy, etc.)
• Note any special conditions (friction? air resistance? angles?)

ORGANIZE as table:
Given:
- m = ___ kg
- v = ___ m/s  
- F = ___ N
- etc.

Find: ___
Type: (kinematics/dynamics/energy/etc.)
Constraints: (moving on incline? with friction? etc.)''',
                    'worked_example': '''Given: m=5kg, v₀=0, a=3m/s², t=4s
Find: Distance traveled
Type: Kinematics (constant acceleration)'''
                },
                {
                    'step': 2,
                    'title': 'Select Appropriate Equations',
                    'detailed_explanation': '''Choose the physics equations that connect given and unknown:

KINEMATICS (motion with constant acceleration):
- v = v₀ + at (velocity)
- x = v₀t + ½at² (position)
- v² = v₀² + 2ax (relates v, x, a)
- x = (v + v₀)/2 · t (average velocity)

DYNAMICS (forces):
- F = ma (Newton's 2nd Law)
- Fnet = ma (apply to all forces)
- f = μN (friction force)

ENERGY:
- KE = ½mv² (kinetic energy)
- PE = mgh (gravitational potential)
- W = F·d (work)
- E_total = KE + PE (conservation)

CIRCULAR MOTION:
- ac = v²/r (centripetal acceleration)
- Fc = mv²/r (centripetal force)

Decide: Which equation(s) directly connect given information to what you need to find?''',
                    'worked_example': 'Given: v₀=0, a=3m/s², t=4s, Find: x\nEquation needed: x = v₀t + ½at² because it connects all given values to x'
                },
                {
                    'step': 3,
                    'title': 'Substitute Values and Calculate',
                    'detailed_explanation': '''SUBSTITUTION PROCESS:
1. Write the equation with variable symbols
2. Write the same equation below with actual numbers
3. Perform calculations step-by-step
4. Track units throughout
5. Show intermediate calculations clearly

CALCULATION STEPS:
- First, calculate powers/exponentiations
- Then multiply/divide in order from left to right
- Finally add/subtract results
- Keep proper significant figures''',
                    'worked_example': 'x = v₀t + ½at²\nx = (0)(4) + ½(3)(4²)\nx = 0 + ½(3)(16)\nx = ½(48)\nx = 24 m'
                },
                {
                    'step': 4,
                    'title': 'Check Units and Reasonableness',
                    'detailed_explanation': '''UNIT VERIFICATION:
- Track units through entire calculation
- Final units should match what you\'re solving for
- Example: kg·m/s² = N (Newton\'s 2nd law check)
- Distance should have units of length (m, km, cm, etc.)

REASONABLENESS CHECK:
- Does sign make sense? (positive for distance, negative for deceleration)
- Is magnitude reasonable? (person can\'t run 1000 m/s)
- Compare to similar known quantities
- Check limiting cases: if t=0, should x=0 (usually yes)''',
                    'worked_example': 'x = 24 m has correct units (meters)\nIs reasonable: 5 kg accelerating at 3 m/s² for 4 seconds travels 24 m ✓'
                },
                {
                    'step': 5,
                    'title': 'State Final Answer in Context',
                    'detailed_explanation': '''ANSWER FORMAT:
• Number with correct units
• Direction if vector (North, at 45°, etc.)
• Significant figures matching given data
• Brief statement interpreting result
• Connect back to physical situation

INTERPRETATION:
- What does this answer mean in the real world?
- How does it compare to expectations?
- State any approximations made
- Mention any assumptions''',
                    'worked_example': '''Final Answer: x = 24 m (or 24 meters to the right)
Interpretation: Starting from rest, an object accelerating at 3 m/s² travels 24 meters in 4 seconds.'''
                }
            ],
            'theories': [
                'Newton\'s Laws of Motion (F=ma, action-reaction)',
                'Kinematic Equations for Constant Acceleration',
                'Work and Energy Relationships',
                'Momentum and Impulse',
                'Circular Motion and Centripetal Force',
                'Oscillation and Simple Harmonic Motion',
                'Waves and Sound',
                'Electromagnetism Basics'
            ],
            'key_concepts': '''Physics connects real phenomena to mathematical equations.
- Always track units through calculations
- Free body diagrams help identify forces
- Energy is often conserved 
- Newton's 2nd Law (F=ma) is fundamental
- Check if situation involves constant or changing quantities''',
            'common_mistakes': '''
1. Unit conversion errors (forgetting to convert km to m)
2. Using wrong units in equation
3. Forgetting to square velocity in kinetic energy
4. Sign errors especially with downward forces
5. Not accounting for all forces in Fnet
6. Mixing up position/velocity/acceleration
7. Rounding too early in multi-step calculations
8. Not considering vector directions (magnitude vs signed component)'''
        }
    
    def _solve_chemistry(self, num, text):
        """Detailed chemistry solution"""
        return {
            'number': num,
            'type': 'CHEMISTRY',
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Identify Reaction Type and Given Information',
                    'detailed_explanation': '''PROBLEM IDENTIFICATION:
1. What type of chemistry? (stoichiometry, equilibrium, kinetics, acid-base, redox, etc.)
2. Is there a chemical equation? (may need to balance it)
3. What's given? (masses, moles, volumes, molarity, etc.)
4. What's being asked? (moles, mass, concentration, pH, percent yield, etc.)

ORGANIZE INFORMATION:
Reaction type: ___
Chemical equation: ___
Given:
- Substance A: ___ g/mol/L
- Substance B: ___ g/mol/L
- etc.
Find: ___''',
                    'worked_example': '2H₂ + O₂ → 2H₂O (reaction already balanced)\nGiven: 4 g H₂\nFind: moles of H₂O produced'
                },
                {
                    'step': 2,
                    'title': 'Balance Chemical Equation (if needed)',
                    'detailed_explanation': '''BALANCING STEPS:
1. Count atoms of each element on both sides
2. Add coefficients to balance each element
3. Check: same number of each atom type on left and right
4. Coefficients show mole ratios between substances

TIPS:
- Balance metals first, then non-metals, then hydrogen, then oxygen
- Use least common multiples to find coefficients
- After balancing, coefficients tell you mole relationships
- Each coefficient is a multiplier for that substance''',
                    'worked_example': '2H₂ + O₂ → 2H₂O\nH atoms: left has 4, right has 4 ✓\nO atoms: left has 2, right has 2 ✓\nBalanced!'
                },
                {
                    'step': 3,
                    'title': 'Convert to Moles and Use Stoichiometry',
                    'detailed_explanation': '''CONVERSION PATHS:

If given MASS → Convert to MOLES:
moles = mass / molar mass
(mass in grams, molar mass from periodic table)
Example: 4 g H₂ ÷ 2 g/mol = 2 mol H₂

If given VOLUME & MOLARITY → Convert to MOLES:
moles = Molarity × Volume (in liters)
Example: 0.5 M × 2 L = 1 mol

If given PARTICLES (atoms/molecules) → Convert to MOLES:
moles = particles / 6.022×10²³ (Avogadro's number)

STOICHIOMETRIC RATIOS (from balanced equation):
From 2H₂ + O₂ → 2H₂O:
- 2 mol H₂ : 1 mol O₂ : 2 mol H₂O
- Ratio H₂ to H₂O is 2:2 or 1:1
- Ratio O₂ to H₂O is 1:2

USE RATIO:
If 2 mol H₂ reacts, and ratio is 1:1, then 2 mol H₂O forms''',
                    'worked_example': '''4 g H₂ × (1 mol/2 g) = 2 mol H₂
Ratio: 2 mol H₂ → 2 mol H₂O
Therefore: 2 mol H₂ → 2 mol H₂O produced'''
                },
                {
                    'step': 4,
                    'title': 'Convert Result Back to Required Units',
                    'detailed_explanation': '''REVERSE CONVERSIONS:

From MOLES to MASS:
mass = moles × molar mass
Example: 2 mol H₂O × 18 g/mol = 36 g H₂O

From MOLES to VOLUME (at STP):
volume = moles × 22.4 L/mol (at STP: 0°C, 1 atm)
OR use ideal gas law: PV = nRT

From MOLES to MOLARITY:
Molarity = moles / volume in liters
Example: 2 mol / 5 L = 0.4 M

PERCENTAGE CALCULATIONS:
% yield = (actual yield / theoretical yield) × 100%
% composition = (mass of element / mass of compound) × 100%''',
                    'worked_example': '2 mol H₂O × 18 g/mol = 36 g H₂O is the result'
                },
                {
                    'step': 5,
                    'title': 'State Answer and Check Reasonableness',
                    'detailed_explanation': '''FINAL ANSWER FORMAT:
- Number with correct units (g, mol, L, M, %, etc.)
- Significant figures matching given data
- Full unit label (not just "36")

REASONABLENESS CHECK:
- Do mole ratios make sense from balanced equation?
- Is product yield reasonable given reactants?
- Did units cancel properly in calculations?
- Are significant figures appropriate?
- For yields: is percentage between 0-100%?

INTERPRET:
Briefly state what the answer means:
"4 grams of H₂ produces 36 grams of H₂O through combustion"
"The limiting reactant is..." (most common problem)''',
                    'worked_example': 'Answer: 36 g H₂O (or 2 mol H₂O)\nThis means 4g H₂ burns completely to produce 36g water'
                }
            ],
            'theories': [
                'Stoichiometry and Mole Concept',
                'Balancing Chemical Equations',
                'Molar Mass and Avogadro\'s Number',
                'Limiting Reactants and Excess Reactants',
                'Percent Yield',
                'Chemical Equilibrium (Le Chatelier\'s Principle)',
                'Acid-Base Chemistry (pH, Ka, Kb)',
                'Redox Reactions and Electron Transfer',
                'Thermochemistry (ΔH, ΔG)'
            ],
            'key_concepts': '''Chemistry uses stoichiometry to relate quantities in reactions.
- Balanced equation gives mole ratios
- Mole is the central unit connecting mass, volume, particles
- Limiting reactant determines maximum product
- Always convert to moles for problem-solving
- Significant figures and units are critical''',
            'common_mistakes': '''
1. Not balancing equation first (wrong mole ratios!)
2. Using unbalanced coefficients for stoichiometry
3. Forgetting to divide mass by molar mass
4. Unit conversion errors (g ↔ mol ↔ L)
5. Wrong molar mass from periodic table
6. Not identifying limiting reactant
7. Using wrong stoichiometric ratio
8. Rounding too early (causes significant figure errors)
9. Forgetting to match significant figures in final answer'''
        }
    
    def _solve_geometry(self, num, text):
        """Detailed geometry solution"""
        return {
            'number': num,
            'type': 'GEOMETRY',
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Visualize and Draw Diagram',
                    'detailed_explanation': '''CREATE A CLEAR DIAGRAM:
1. Draw the geometric figure described
2. Label all known dimensions, angles
3. Mark unknown quantities with variables
4. Show any special features (right angles, parallel lines, etc.)
5. Draw to approximate scale if possible

IDENTIFY PROPERTIES:
- What shape is it? (triangle, circle, polygon, etc.)
- What type? (equilateral, isosceles, right triangle, etc.)
- Are any lines parallel? Perpendicular?
- Are there any special angle relationships?''',
                    'worked_example': 'For a right triangle with hypotenuse 5 and one leg 3:\nDraw right angle, label sides: legs 3 and ?, hypotenuse 5'
                },
                {
                    'step': 2,
                    'title': 'Identify Geometric Theorems',
                    'detailed_explanation': '''SELECT RELEVANT THEOREMS:

TRIANGLES:
- Pythagorean Theorem: a² + b² = c² (right triangles)
- Sum of angles: A + B + C = 180°
- Area = ½base × height
- Triangle inequality: sum of any two sides > third side

CIRCLES:
- Circumference = 2πr
- Area = πr²
- Arc length = rθ (θ in radians)
- Inscribed angle = ½(central angle subtended by same arc)

POLYGONS:
- Sum of interior angles = (n-2) × 180° for n-sided polygon
- Regular polygon area = ½ × perimeter × apothem

TRIGONOMETRY:
- sin(θ) = opposite/hypotenuse
- cos(θ) = adjacent/hypotenuse  
- tan(θ) = opposite/adjacent
- Law of Sines: a/sin(A) = b/sin(B) = c/sin(C)
- Law of Cosines: c² = a² + b² - 2ab·cos(C)

CONGRUENCE & SIMILARITY:
- Congruent figures: same size and shape
- Similar figures: same shape, different size, corresponding angles equal''',
                    'worked_example': 'For right triangle: Use Pythagorean Theorem\n3² + b² = 5²\n9 + b² = 25'
                },
                {
                    'step': 3,
                    'title': 'Set Up Equations Using Theorems',
                    'detailed_explanation': '''TRANSLATE GEOMETRY TO ALGEBRA:
1. Identify which geometric properties/theorems apply
2. Write equations using those properties
3. Include all known values
4. Use geometric variables for unknowns

EQUATION SETUP:
- From Pythagorean Theorem: a² + b² = c²
- From area formula: A = ½bh
- From angle sum: ∠A + ∠B + ∠C = 180°
- From perimeter: P = sum of all sides
- From trigonometry: tan(35°) = height/base''',
                    'worked_example': '3² + b² = 5²\n9 + b² = 25\nb² = 16'
                },
                {
                    'step': 4,
                    'title': 'Solve Algebraically',
                    'detailed_explanation': '''SOLVE THE EQUATIONS:
1. Take each geometric equation
2. Apply algebra to solve for unknowns
3. Show all steps clearly
4. Maintain equation balance (do same operation both sides)

For our example:
b² = 16
b = 4 (take positive square root for length)''',
                    'worked_example': 'b = √16 = 4 units'
                },
                {
                    'step': 5,
                    'title': 'Verify and Interpret Geometrically',
                    'detailed_explanation': '''VERIFICATION:
1. Substitute answer back into geometric relationships
2. Check: Does 3² + 4² = 5²? → 9 + 16 = 25? → 25 = 25 ✓
3. Does it make geometric sense? Is every side positive? Are angles reasonable?

GEOMETRIC INTERPRETATION:
- State what you found: "The missing side is 4 units"
- Confirm it makes sense: "A 3-4-5 triangle is a common right triangle"
- If finding area/volume: "Area = ½ × 3 × 4 = 6 square units"
- Include appropriate units in final answer''',
                    'worked_example': '''Verification: 3² + 4² = 9 + 16 = 25 = 5² ✓
This is the famous 3-4-5 right triangle.
The missing leg is 4 units.'''
                }
            ],
            'theories': [
                'Pythagorean Theorem and Right Triangles',
                'Properties of Triangles (angle sum, area formulas)',
                'Circle Properties (circumference, area, central angles)',
                'Trigonometric Ratios (sin, cos, tan)',
                'Law of Sines and Law of Cosines',
                'Angle Theorems (vertical, corresponding, inscribed, etc.)',
                'Congruence and Similarity',
                'Transformation Geometry (rotation, reflection, translation)',
                'Coordinate Geometry and Distance Formula'
            ],
            'key_concepts': '''Geometry connects spatial properties to mathematics.
- Always draw and label diagrams
- Know theorems relevant to the shape
- Convert geometric relationships to equations
- Solve algebraically, then interpret geometrically
- Check that answer makes geometric sense''',
            'common_mistakes': '''
1. Not drawing a diagram or drawing one incorrectly
2. Using wrong theorem for the shape
3. Confusing radius with diameter
4. Angle errors (degrees vs. radians, wrong angle measure)
5. Forgetting to include proper units in answer
6. Negative lengths (not physically meaningful)
7. Not checking if answer satisfies original geometric constraints
8. Rounding errors in multi-step problems
9. Using wrong formula (area vs. circumference confusion)'''
        }
    
    def _solve_algebra(self, num, text):
        """Detailed algebra solution"""
        return {
            'number': num,
            'type': 'ALGEBRA',
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Write the Equation Clearly and Identify Type',
                    'detailed_explanation': '''PARSE THE PROBLEM:
1. Read the verbal description carefully
2. Identify what variable represents the unknown
3. Write the equation with proper symbols
4. Identify equation type (linear, quadratic, rational, exponential, etc.)

EQUATION TYPES:
- Linear: ax + b = 0 (highest power is 1)
- Quadratic: ax² + bx + c = 0 (highest power is 2)
- Polynomial: higher powers
- Rational: variables in denominators
- Radical: variables under roots

SETUP:
Original problem → Equation form
"A number plus 3 equals 15" → x + 3 = 15
"Twice a number squared equals 50" → 2x² = 50''',
                    'worked_example': '''"Find a number such that 2x - 5 = 11"
Equation: 2x - 5 = 11
Type: Linear equation (highest power is 1)'''
                },
                {
                    'step': 2,
                    'title': 'Isolate Constant Terms on One Side',
                    'detailed_explanation': '''MOVE CONSTANTS:
1. Identify all terms WITHOUT the variable
2. Move them to one side (usually right side)
3. Add or subtract these terms from BOTH sides
4. Maintain equation balance

PROCESS:
Original: 2x - 5 = 11
Add 5 to both sides: 2x - 5 + 5 = 11 + 5
Simplified: 2x = 16

KEY RULE:
Whatever you do to one side, do to the other!
If you add 5 to left, add 5 to right
If you subtract 3 from left, subtract 3 from right''',
                    'worked_example': '''2x - 5 = 11
Add 5 to both sides:
2x - 5 + 5 = 11 + 5
2x = 16'''
                },
                {
                    'step': 3,
                    'title': 'Isolate Variable Terms',
                    'detailed_explanation': '''COLLECT LIKE TERMS:
1. Move all terms with the variable to one side
2. Move all constant terms to the other side
3. Add/subtract as needed

FOR VARIABLES:
- 3x + x = 4x (combine like terms)
- 5y² + 3y² = 8y² (same power)
- 2x + 3y cannot be combined (different variables)

EXAMPLE:
3x + 2 = x - 4
Move x terms left: 3x - x + 2 = -4
Combine: 2x + 2 = -4
Move constants right: 2x = -4 - 2
Simplify: 2x = -6''',
                    'worked_example': '''2x = 16
Already isolated! x term on left, constant on right.'''
                },
                {
                    'step': 4,
                    'title': 'Solve for the Variable',
                    'detailed_explanation': '''FINAL ISOLATION:
1. If coefficient multiplies variable: DIVIDE both sides
2. If variable is squared: take square ROOT both sides
3. If variable is in denominator: MULTIPLY both sides by denominator

INVERSE OPERATIONS:
- Multiplication ↔ Division
- Addition ↔ Subtraction
- Squaring ↔ Square root
- Exponential ↔ Logarithm

FOR LINEAR: 2x = 16
Divide both sides by 2:
2x/2 = 16/2
x = 8

FOR QUADRATIC: x² = 25
Take square root:
x = ±5 (two solutions!)''',
                    'worked_example': '''2x = 16
Divide both sides by 2:
x = 8'''
                },
                {
                    'step': 5,
                    'title': 'Check Solution(s)',
                    'detailed_explanation': '''VERIFICATION PROCESS:
1. Take the solution value(s)
2. Substitute back into ORIGINAL equation
3. Evaluate both sides
4. Check if they're equal

IF SOLUTION IS CORRECT:
Both sides should equal
Left side = Right side ✓

IF SOLUTION IS WRONG:
Left side ≠ Right side ✗
Check your algebra again

SPECIAL CHECKS:
- For quadratic: check both solutions if two exist
- For rational equations: check for extraneous solutions (makes denominator=0)
- For radical equations: check (squaring can introduce fake solutions)
- For domain issues: is solution valid?''',
                    'worked_example': '''Check: x = 8 in original equation 2x - 5 = 11
Left side: 2(8) - 5 = 16 - 5 = 11
Right side: 11
Left = Right ✓ Solution is CORRECT!'''
                }
            ],
            'theories': [
                'Linear Equations and Solving',
                'Quadratic Equations (factoring, quadratic formula)',
                'Polynomial Equations',
                'Rational Equations',
                'Radical Equations',
                'Systems of Equations',
                'Exponential and Logarithmic Equations',
                'Inequalities and Interval Notation',
                'Factoring and Special Products'
            ],
            'key_concepts': '''Algebra is about finding unknown values using equation properties.
- Variables represent unknowns
- Equations show relationships between quantities
- Inverse operations isolate variables
- Always check solutions in original equation
- Some problems have no solution or infinite solutions''',
            'common_mistakes': '''
1. Not applying operations to BOTH sides of equation
2. Sign errors (especially with negative numbers)
3. Forgetting to multiply coefficient when multiplying through by denominator
4. Not checking for both solutions in quadratic (±)
5. Algebraic mistakes when combining like terms
6. Forgetting to check solution in original equation
7. Dividing by zero (denominator can't be zero)
8. Extraneous solutions from squaring both sides
9. Rounding too early in multi-step problems
10. Not distributing properly when removing parentheses'''
        }
    
    def _solve_general(self, num, text):
        """General purpose solver for any problem"""
        return {
            'number': num,
            'type': 'GENERAL PROBLEM',
            'problem': text,
            'steps': [
                {
                    'step': 1,
                    'title': 'Understand the Problem',
                    'detailed_explanation': '''Read carefully and identify:
1. WHAT is being asked?
2. WHAT information is given?
3. WHAT is unknown?
4. Are there any special conditions or constraints?

Organize given information:
Given:
- [Value 1]: [description and units]
- [Value 2]: [description and units]
- etc.

Find: [What you need to determine]''',
                    'worked_example': 'Read problem multiple times until clear what needs solving'
                },
                {
                    'step': 2,
                    'title': 'Gather Relevant Information and Formulas',
                    'detailed_explanation': '''Identify which:
1. Formulas apply to this problem type?
2. Theorems or principles are relevant?
3. Previous knowledge connects?
4. Methods have worked for similar problems?

List applicable formulas with descriptions''',
                    'worked_example': 'Determine which mathematical tools are needed'
                },
                {
                    'step': 3,
                    'title': 'Plan Solution Strategy',
                    'detailed_explanation': '''Outline the approach:
1. What steps will get from given to answer?
2. In what order should operations proceed?
3. Are there intermediate calculations needed?
4. How will you verify the result?

Create a roadmap before executing''',
                    'worked_example': 'Map out the solution path step by step'
                },
                {
                    'step': 4,
                    'title': 'Execute the Solution',
                    'detailed_explanation': '''Follow the plan:
1. Apply formulas and techniques
2. Show all work clearly
3. Keep track of units
4. Maintain significant figures
5. Check reasonableness of intermediate results''',
                    'worked_example': 'Carry out calculations systematically'
                },
                {
                    'step': 5,
                    'title': 'Verify and Interpret Result',
                    'detailed_explanation': '''After finding answer:
1. Does it have correct units?
2. Is the magnitude reasonable?
3. Is the sign correct?
4. Does it satisfy original equation/constraints?
5. Can back-calculate to verify?

Interpret: What does this answer mean in context?''',
                    'worked_example': 'Check answer makes sense and is reasonable'
                }
            ],
            'theories': [
                'Problem-solving methodology',
                'Logical reasoning',
                'Mathematical principles',
                'Unit analysis',
                'Verification techniques'
            ],
            'key_concepts': 'Systematic problem-solving applies to any domain',
            'common_mistakes': 'Not reading carefully, skipping verification, algebraic errors'
        }


def generate_detailed_report(problems, theories_dict):
    """Generate detailed analysis report with comprehensive solutions"""
    
    report = {
        'summary': {
            'total_problems': len(problems),
            'problem_types': list(set(p.get('type', 'Unknown').upper() for p in problems)),
            'total_theories': sum(len(t) for t in theories_dict.values())
        },
        'problems_analyzed': []
    }
    
    solver = DetailedSolutionGenerator()
    
    for idx, problem in enumerate(problems, 1):
        solution = solver.generate_detailed_solution(
            idx,
            problem.get('text', 'No description'),
            problem.get('type', 'math')
        )
        report['problems_analyzed'].append(solution)
    
    # Generate cliff notes summary
    report['cliff_notes'] = generate_cliff_notes(report['problems_analyzed'], theories_dict)
    
    return report


def generate_cliff_notes(solutions, theories_dict):
    """Generate comprehensive cliff notes with all theories used"""
    
    cliff_notes = {
        'title': 'COMPREHENSIVE STUDY SUMMARY - CLIFF NOTES',
        'sections': []
    }
    
    # Collect all unique theories used across all problems
    theories_used = {}
    problem_types_covered = set()
    
    for solution in solutions:
        # Track problem types
        problem_types_covered.add(solution['type'])
        
        # Collect theories used in this problem
        for theory in solution.get('theories', []):
            if theory not in theories_used:
                theories_used[theory] = {
                    'name': theory,
                    'problems': [],
                    'description': ''
                }
            theories_used[theory]['problems'].append(solution['number'])
    
    # Section 1: Overview
    cliff_notes['sections'].append({
        'title': '📊 SESSION OVERVIEW',
        'content': f'''
Total Problems Solved: {len(solutions)}
Problem Types Covered: {', '.join(sorted(problem_types_covered))}
Unique Theories Applied: {len(theories_used)}
        ''',
        'important': True
    })
    
    # Section 2: Problem-Solving Methodology
    cliff_notes['sections'].append({
        'title': '🎯 UNIVERSAL PROBLEM-SOLVING METHODOLOGY',
        'steps': [
            {
                'step': 1,
                'title': 'UNDERSTAND THE PROBLEM',
                'content': 'Read carefully, identify what is given, what is unknown, identify problem type and any constraints'
            },
            {
                'step': 2,
                'title': 'GATHER INFORMATION & FORMULAS',
                'content': 'List all given values with units, identify relevant theorems, formulas, and principles'
            },
            {
                'step': 3,
                'title': 'PLAN YOUR APPROACH',
                'content': 'Determine which formulas/techniques connect given information to what you need to find'
            },
            {
                'step': 4,
                'title': 'EXECUTE SOLUTION',
                'content': 'Show all work systematically, maintain units, keep track of significant figures'
            },
            {
                'step': 5,
                'title': 'VERIFY & INTERPRET',
                'content': 'Check answer by substitution, verify units, confirm reasonableness, interpret in context'
            }
        ]
    })
    
    # Section 3: Key Concepts by Problem Type
    cliff_notes['sections'].append({
        'title': '💡 KEY CONCEPTS BY PROBLEM TYPE',
        'subsections': generate_concepts_by_type(solutions)
    })
    
    # Section 4: All Theories Used
    cliff_notes['sections'].append({
        'title': '🧠 COMPLETE THEORY REFERENCE GUIDE',
        'theories': [
            {
                'name': theory_name,
                'problems_used': theories_used[theory_name]['problems'],
                'category': categorize_theory(theory_name)
            }
            for theory_name in sorted(theories_used.keys())
        ]
    })
    
    # Section 5: Common Mistakes to Avoid
    cliff_notes['sections'].append({
        'title': '⚠️ CRITICAL MISTAKES TO AVOID',
        'mistakes': extract_mistakes(solutions)
    })
    
    # Section 6: Quick Reference Formulas
    cliff_notes['sections'].append({
        'title': '📐 QUICK REFERENCE - ESSENTIAL FORMULAS',
        'formulas': generate_formula_reference(theories_used)
    })
    
    return cliff_notes


def generate_concepts_by_type(solutions):
    """Generate key concepts organized by problem type"""
    concepts = {}
    
    for solution in solutions:
        ptype = solution['type']
        if ptype not in concepts:
            concepts[ptype] = {
                'type': ptype,
                'problems': [],
                'key_concepts': []
            }
        
        concepts[ptype]['problems'].append(solution['number'])
        concepts[ptype]['key_concepts'].append(solution.get('key_concepts', ''))
    
    return [
        {
            'type': ptype,
            'problems': data['problems'],
            'concept': data['key_concepts'][0] if data['key_concepts'] else 'See solution'
        }
        for ptype, data in sorted(concepts.items())
    ]


def categorize_theory(theory_name):
    """Categorize theory by domain"""
    theory_lower = theory_name.lower()
    
    categories = {
        'Calculus': ['derivative', 'integral', 'limit', 'theorem', 'rule', 'calculus'],
        'Algebra': ['equation', 'polynomial', 'factor', 'quadratic', 'linear', 'algebra'],
        'Physics': ['newton', 'force', 'energy', 'motion', 'kinematic', 'physics', 'momentum', 'work'],
        'Chemistry': ['stoich', 'balance', 'mole', 'reaction', 'equilibrium', 'chemistry', 'acid', 'thermodynamic'],
        'Geometry': ['geometry', 'pythagorean', 'triangle', 'circle', 'area', 'volume', 'angle'],
        'Trigonometry': ['sin', 'cos', 'tan', 'trigonometric', 'radian', 'trig']
    }
    
    for category, keywords in categories.items():
        if any(keyword in theory_lower for keyword in keywords):
            return category
    
    return 'General Mathematics'


def extract_mistakes(solutions):
    """Extract common mistakes from all solutions"""
    all_mistakes = []
    
    for solution in solutions:
        mistakes_text = solution.get('common_mistakes', '')
        if mistakes_text:
            # Split by numbered items if numbered
            mistake_items = [m.strip() for m in mistakes_text.split('\n') if m.strip()]
            all_mistakes.extend(mistake_items)
    
    # Remove duplicates and return top mistakes
    unique_mistakes = list(dict.fromkeys(all_mistakes))
    return unique_mistakes[:15]  # Top 15 mistakes


def generate_formula_reference(theories_used):
    """Generate quick reference for formulas"""
    formulas = {
        'Calculus': [
            'Power Rule: d/dx[xⁿ] = n·xⁿ⁻¹',
            'Product Rule: d/dx[u·v] = u\'v + uv\'',
            'Chain Rule: d/dx[f(g(x))] = f\'(g(x))·g\'(x)',
            'Integration: ∫ xⁿ dx = xⁿ⁺¹/(n+1) + C',
            'Fundamental Theorem: ∫ₐᵇ f(x) dx = F(b) - F(a)'
        ],
        'Physics': [
            'Newton\'s 2nd Law: F = ma',
            'Kinetic Energy: KE = ½mv²',
            'Potential Energy: PE = mgh',
            'Work: W = F·d',
            'Momentum: p = mv'
        ],
        'Chemistry': [
            'Moles: n = mass / molar mass',
            'Molarity: M = moles / volume (L)',
            'Stoichiometry: Use mole ratios from balanced equation',
            'Percent Yield: (actual/theoretical) × 100%',
            'Ideal Gas Law: PV = nRT'
        ],
        'Algebra': [
            'Quadratic Formula: x = (-b ± √(b²-4ac)) / 2a',
            'Factoring: ax² + bx + c = a(x - r₁)(x - r₂)',
            'Slope: m = (y₂ - y₁) / (x₂ - x₁)',
            'Distance Formula: d = √[(x₂-x₁)² + (y₂-y₁)²]',
            'Parabola: y = a(x - h)² + k'
        ],
        'Geometry': [
            'Pythagorean Theorem: a² + b² = c²',
            'Triangle Area: A = ½bh',
            'Circle Area: A = πr²',
            'Circle Circumference: C = 2πr',
            'Volume Cylinder: V = πr²h'
        ]
    }
    
    # Return only relevant formulas
    result = []
    for theory_name in theories_used.keys():
        category = categorize_theory(theory_name)
        if category in formulas and category not in [f['category'] for f in result]:
            result.append({
                'category': category,
                'formulas': formulas[category]
            })
    
    return result

