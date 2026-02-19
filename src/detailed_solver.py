"""
Detailed Solution Generator with Complete Step-by-Step Explanations
Provides comprehensive solutions with full reasoning and worked examples
"""

import re

try:
  from googletrans import Translator
except Exception:  # pragma: no cover - optional dependency
  Translator = None

try:
  from langdetect import detect, LangDetectException
except Exception:  # pragma: no cover - optional dependency
  detect = None
  LangDetectException = Exception


class DetailedSolutionGenerator:
    """Generates detailed, comprehensive step-by-step solutions"""
    
    def __init__(self):
        self.problem_patterns = {
          'derivative': r'(deriv|d/d|prime|slope|derivada|derivar)',
          'integral': r'(integr|∫|sum|integral)',
          'limit': r'(limit|lim|approaches|→|limite|l[íi]mite|tiende)',
          'equation': r'(solve|find|equation|=|resolver|resuelve|ecuaci[óo]n)',
          'simplify': r'(simplify|reduce|factor|simplificar|reducir|factorizar)',
          'geometry': r'(area|[áa]rea|volume|volumen|perimeter|per[ií]metro|angle|[áa]ngulo|triangle|tri[aá]ngulo|circle|c[ií]rculo)',
          'force': r'(force|newton|acceleration|aceleraci[óo]n|F=ma|fuerza)',
          'energy': r'(energy|work|kinetic|potential|energ[ií]a|trabajo|cin[eé]tica|potencial)',
          'chemistry': r'(stoich|balance|react|mole|qu[ií]mica|reacci[óo]n|mol)',
          'algebra': r'(quadratic|linear|factor|solve|[aá]lgebra|polynomial|polinomio|ecuaci[óo]n)'
        }


    class _LanguageSupport:
      """Lightweight language detection and translation wrapper."""

      _SPANISH_MARKERS = {
        'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'y', 'o', 'pero',
        'porque', 'para', 'con', 'sin', 'sobre', 'entre', 'dado', 'dada', 'dados',
        'dadas', 'encuentra', 'calcula', 'determina', 'resuelve', 'resolver',
        'hallar', 'problema', 'ejercicio', 'pregunta', 'si', 'entonces', 'donde'
      }

      def __init__(self):
        self._translator = Translator() if Translator else None
        self._cache = {}

      def detect_language(self, text):
        if not text:
          return 'es'
        if detect is not None:
          try:
            detected = detect(text)
            if detected:
              return detected
          except LangDetectException:
            return 'es'
        text_lower = text.lower()
        if re.search(r'[áéíóúñ¿¡]', text_lower):
          return 'es'
        hits = sum(1 for marker in self._SPANISH_MARKERS if marker in text_lower)
        return 'es' if hits >= 2 else 'en'

      def translate_text(self, text, target_lang):
        if not text or target_lang == 'en':
          return text
        if not self._translator:
          return text
        cache_key = (target_lang, text)
        if cache_key in self._cache:
          return self._cache[cache_key]
        try:
          result = self._translator.translate(text, dest=target_lang)
          translated = result.text if result else text
        except Exception:
          translated = text
        self._cache[cache_key] = translated
        return translated


    def _translate_value(value, translator, target_lang, skip_keys=None):
      if skip_keys is None:
        skip_keys = set()
      if isinstance(value, str):
        return translator.translate_text(value, target_lang)
      if isinstance(value, list):
        return [_translate_value(item, translator, target_lang, skip_keys=skip_keys) for item in value]
      if isinstance(value, dict):
        translated = {}
        for key, item in value.items():
          if key in skip_keys:
            translated[key] = item
          else:
            translated[key] = _translate_value(item, translator, target_lang, skip_keys=skip_keys)
        return translated
      return value
    
    def analyze_problem_requirements(self, text):
        """Deep analysis of what the problem is asking for"""
        analysis = {
            'exact_question': '',
            'given_info': [],
            'unknowns': [],
            'problem_objectives': [],
            'key_constraints': []
        }
        
        text_lower = text.lower()
        
        # Extract the exact question (usually what comes after "find", "solve", "calculate", etc.)
        question_patterns = [
          r'(?:find|calculate|determine|solve for|compute)\s+([^\.\n?,]+)',
          r'(?:encuentra|hallar|calcular|determinar|resuelve|resolver)\s+([^\.\n?,]+)',
          r'([^.]*?)(?:find|calculate|determine|solve|is|are|given)[^.]*',
          r'([^.]*?)(?:encuentra|calcula|determina|resuelve|es|son|dado|dada|dados|dadas)[^.]*',
        ]
        
        for pattern in question_patterns:
            match = re.search(pattern, text_lower)
            if match:
                analysis['exact_question'] = match.group(1).strip()
                break
        
        # Look for "given" statements
        if 'given' in text_lower or any(token in text_lower for token in ['dado', 'dada', 'dados', 'dadas']):
          if 'given' in text_lower:
            parts = text_lower.split('given')
          else:
            parts = re.split(r'dado|dada|dados|dadas', text_lower, maxsplit=1)
            if len(parts) > 1:
                given_text = parts[1].split('find')[0] if 'find' in parts[1] else parts[1]
                # Extract numerical values and variables
                numbers = re.findall(r'[A-Za-z_]\s*=\s*[0-9.]+|[0-9.]+\s+[A-Za-z]+', given_text)
                analysis['given_info'] = numbers[:5]  # Top 5 given pieces
        
        # Identify what's unknown (what we're solving for)
        unknown_patterns = [
          r'find\s+([A-Za-z_]\w*)',
          r'solve\s+for\s+([A-Za-z_]\w*)',
          r'calculate\s+([A-Za-z_]\w*)',
          r'(?:what|where|when)\s+(?:is|are|does)\s+(?:the\s+)?([A-Za-z_]\w*)',
          r'(?:encuentra|hallar|calcular|determina)\s+([A-Za-z_]\w*)',
          r'(?:resuelve|resolver)\s+para\s+([A-Za-z_]\w*)',
          r'(?:cual|cu[aá]l|cuanto|cu[aá]nto)\s+(?:es|son)\s+(?:el|la|los|las)?\s*([A-Za-z_]\w*)',
        ]
        
        for pattern in unknown_patterns:
            matches = re.findall(pattern, text_lower)
            analysis['unknowns'] = matches[:3]
            if matches:
                break
        
        # Identify objectives
        if any(word in text_lower for word in ['maximize', 'minimize']):
            analysis['problem_objectives'].append('Optimization (max/min)')
        if any(word in text_lower for word in ['prove', 'show', 'verify', 'demonstrate']):
            analysis['problem_objectives'].append('Proof/Verification')
        if any(word in text_lower for word in ['compare', 'contrast', 'difference']):
            analysis['problem_objectives'].append('Comparison')
        if any(word in text_lower for word in ['error', 'approximate', 'estimate']):
            analysis['problem_objectives'].append('Approximation/Error Analysis')
        
        # Extract constraints (numbers with operators, inequalities, ranges)
        constraints = re.findall(r'(?:where|assuming|condition|constraint|such that|donde|suponiendo|condici[óo]n|tal que)[^.]*', text_lower)
        analysis['key_constraints'] = constraints[:3]
        
        return analysis
    
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
        analysis = self.analyze_problem_requirements(problem_text)
        
        # Map to specific solvers
        if 'derivative' in detected_type or 'calculus' in problem_type.lower():
            return self._solve_derivative(problem_num, problem_text, analysis)
        elif 'integral' in detected_type:
            return self._solve_integral(problem_num, problem_text, analysis)
        elif 'limit' in detected_type:
            return self._solve_limit(problem_num, problem_text, analysis)
        elif any(x in detected_type for x in ['force', 'energy', 'acceleration']):
            return self._solve_physics(problem_num, problem_text, analysis)
        elif 'chemistry' in detected_type or 'stoich' in detected_type:
            return self._solve_chemistry(problem_num, problem_text, analysis)
        elif any(x in detected_type for x in ['geometry', 'area', 'volume']):
            return self._solve_geometry(problem_num, problem_text, analysis)
        elif 'algebra' in problem_type.lower() or 'equation' in detected_type:
            return self._solve_algebra(problem_num, problem_text, analysis)
        else:
            return self._solve_general(problem_num, problem_text, analysis)
    
    def _solve_derivative(self, num, text, analysis=None):
        """Detailed derivative solution"""
        if analysis is None:
            analysis = self.analyze_problem_requirements(text)
        
        return {
            'number': num,
            'type': 'CALCULUS - DERIVATIVES',
            'problem': text,
            'problem_analysis': {
                'what_is_asked': 'Find the derivative (rate of change) of the given function',
                'exact_target': 'The derivative function f\'(x) that describes the instantaneous rate of change',
                'given_information': analysis.get('given_info', ['Function f(x) to be differentiated']),
                'what_to_find': analysis.get('unknowns', ['f\'(x) - the derivative']) or ['The derivative function or slope'],
                'key_steps_overview': [
                    '1. Identify the function form (polynomial, trigonometric, exponential, etc.)',
                    '2. Determine which differentiation rule(s) apply',
                    '3. Apply the rule(s) carefully to each term',
                    '4. Simplify the resulting derivative',
                    '5. Verify and interpret the result in context'
                ]
            },
            'steps': [
                {
                    'step': 1,
                    'title': 'Identify the Function and Its Form',
                    'detailed_explanation': '''STEP 1: DETERMINE WHAT YOU'RE DIFFERENTIATING

The derivative measures how quickly a function changes. Before you can find it, you must clearly identify the function.

▸ READ THE PROBLEM CAREFULLY:
  • What is the function you need to differentiate?
  • Look for: "f(x) = ", "y = ", "the function ", or just a mathematical expression
  • The function could be buried in a word problem (e.g., "A ball is thrown..." derives a position function)

▸ IDENTIFY THE FUNCTION FORM:
  This determines which rule(s) you'll use:
  
  POLYNOMIAL: f(x) = 3x⁴ + 2x² + 5
  - Highest power terms like x⁴, x³, etc.
  - Use POWER RULE on each term
  
  PRODUCT: f(x) = x² · sin(x) or f(x) = (x² + 1)(3x - 2)
  - TWO separate functions being MULTIPLIED together
  - Requires PRODUCT RULE: (u·v)' = u'·v + u·v'
  
  QUOTIENT: f(x) = (x² + 1)/(x - 1) or f(x) = sin(x)/x
  - Function is a FRACTION (top/bottom)
  - Requires QUOTIENT RULE: (u/v)' = (u'v - uv')/v²
  
  COMPOSITION: f(x) = (3x² + 2)⁵ or f(x) = sin(x²) or f(x) = e^(2x)
  - Function INSIDE another function (nested)
  - Requires CHAIN RULE: [f(g(x))]' = f'(g(x)) · g'(x)
  
  TRIGONOMETRIC: f(x) = sin(x), cos(x), tan(x), etc.
  - Memorized derivatives needed
  - d/dx[sin(x)] = cos(x), d/dx[cos(x)] = -sin(x)
  
  EXPONENTIAL/LOGARITHMIC: f(x) = e^x, a^x, ln(x), log(x)
  - Memorized derivatives or chain rule
  - d/dx[e^x] = e^x, d/dx[ln(x)] = 1/x

▸ IDENTIFY COMPLEX COMBINATIONS:
  • Does the function have MULTIPLE terms added/subtracted?
  • Does it have products, quotients, or nested functions?
  • You'll apply rules term-by-term or rule-within-rule
  
▸ REWRITE IN STANDARD FORM IF NEEDED:
  • √x = x^(1/2) [easier to use power rule]
  • 1/x = x^(-1) [power rule applies]
  • Fractional exponents become easier with power rule''',
                    'worked_example': '''Example 1: f(x) = 3x⁴ + 2x² + 5
  → This is a POLYNOMIAL (multiple terms with powers of x)
  → Apply POWER RULE to each term separately

Example 2: f(x) = x² · cos(x)
  → This is a PRODUCT (two functions multiplied)
  → Must use PRODUCT RULE

Example 3: f(x) = sin(x³)
  → This is COMPOSITION (sin function contains x³ inside)
  → Must use CHAIN RULE
  
Example 4: f(x) = (2x + 1)/(x² - 3)
  → This is a QUOTIENT (fraction form)
  → Must use QUOTIENT RULE'''
                },
                {
                    'step': 2,
                    'title': 'Select the Appropriate Differentiation Rule(s)',
                    'detailed_explanation': '''STEP 2: CHOOSE THE RIGHT TOOL

Different functions require different rules. Choosing correctly prevents mistakes.

▸ POWER RULE - For terms like xⁿ:
  ┌─────────────────────────────────────────┐
  │  d/dx[xⁿ] = n·xⁿ⁻¹                      │
  │  (bring down exponent, reduce by 1)     │
  └─────────────────────────────────────────┘
  
  EXAMPLES:
  • d/dx[x⁴] = 4x³           [exponent 4→3, coefficient 1→4]
  • d/dx[x²] = 2x            [exponent 2→1, coefficient 1→2]
  • d/dx[x] = 1              [x is x¹, so 1·x⁰ = 1]
  • d/dx[5] = 0              [constants have exponent 0, disappear]
  • d/dx[√x] = 1/(2√x)       [rewrite as x^(1/2), apply rule]
  
  STEP-BY-STEP FOR f(x) = 3x⁴ + 2x² + 5:
  ├─ Term 1: 3x⁴ → 3·4·x³ = 12x³
  ├─ Term 2: 2x² → 2·2·x = 4x
  └─ Term 3: 5 → 0
  
  Result: f'(x) = 12x³ + 4x

▸ PRODUCT RULE - When two functions are MULTIPLIED:
  ┌──────────────────────────────────────────────────┐
  │  d/dx[u·v] = u'·v + u·v'                         │
  │  = (first')·(second) + (first)·(second')         │
  └──────────────────────────────────────────────────┘
  
  MEMORY AID: "First times derivative of Second 
               plus Second times derivative of First"
  
  VISUAL PATTERN:
     (u · v)' = u' · v  +  u · v'
      [product]  [this]    [plus this]
  
  EXAMPLE: f(x) = x² · sin(x)
  ├─ u = x², u' = 2x
  ├─ v = sin(x), v' = cos(x)
  └─ f'(x) = (2x)·sin(x) + x²·cos(x)

▸ QUOTIENT RULE - When function is a FRACTION:
  ┌─────────────────────────────────────────────────┐
  │  d/dx[u/v] = (u'·v - u·v') / v²                 │
  │                                                 │
  │  = (top'·bottom - top·bottom') / (bottom)²      │
  └─────────────────────────────────────────────────┘
  
  MEMORY AID: "LOW d-HIGH minus HIGH d-LOW, 
               over LOW LOW (squared)"
  
  VISUAL PATTERN:
         u      u'·v - u·v'
       ─── → ─────────────
         v          v²
  
  ⚠️ ORDER MATTERS! Numerator is u'v MINUS uv', not reversed!
  
  EXAMPLE: f(x) = (x³ + 2) / (x - 1)
  ├─ u = x³ + 2, u' = 3x²
  ├─ v = x - 1, v' = 1
  └─ f'(x) = [(3x²)(x-1) - (x³+2)(1)] / (x-1)²
           = [3x³ - 3x² - x³ - 2] / (x-1)²
           = [2x³ - 3x² - 2] / (x-1)²

▸ CHAIN RULE - When function is NESTED/COMPOSITE:
  ┌──────────────────────────────────────────────────┐
  │  d/dx[f(g(x))] = f'(g(x)) · g'(x)                │
  │  = (outer')·(inner') derivatives multiply        │
  └──────────────────────────────────────────────────┘
  
  MEMORY AID: "Derivative of outside times 
               derivative of inside"
  
  VISUAL PATTERN:
     [outer([inner])]' = outer' · inner'
  
  EXAMPLE 1: f(x) = (3x² + 2)⁵
  ├─ OUTSIDE: u⁵ where u = 3x² + 2
  ├─ INSIDE: 3x² + 2
  ├─ d/du[u⁵] = 5u⁴ (outside derivative)
  ├─ d/dx[3x² + 2] = 6x (inside derivative)
  └─ f'(x) = 5(3x² + 2)⁴ · 6x = 30x(3x² + 2)⁴
  
  EXAMPLE 2: f(x) = sin(x²)
  ├─ OUTSIDE: sin(something) → cos(something)
  ├─ INSIDE: x² → 2x
  └─ f'(x) = cos(x²) · 2x''',
                    'worked_example': '''POWER RULE: f(x) = x⁴ → f'(x) = 4x³

PRODUCT RULE: f(x) = 2x · e^x
  u = 2x, u' = 2
  v = e^x, v' = e^x
  f'(x) = 2·e^x + 2x·e^x = 2e^x(1 + x)

QUOTIENT RULE: f(x) = x/(x² + 1)
  f'(x) = [(1)(x² + 1) - (x)(2x)] / (x² + 1)²
        = (x² + 1 - 2x²) / (x² + 1)²
        = (1 - x²) / (x² + 1)²

CHAIN RULE: f(x) = sin(2x)
  f'(x) = cos(2x) · 2 = 2cos(2x)'''
                },
                {
                    'step': 3,
                    'title': 'Apply the Rule(s) Step-by-Step',
                    'detailed_explanation': '''STEP 3: EXECUTE THE DIFFERENTIATION

Now apply your chosen rule(s) carefully and methodically.

▸ WRITE OUT YOUR STARTING FORMULA:
  Write f(x) = [complete original function]
  Make sure you've got everything

▸ FOR POLYNOMIALS - Apply power rule to each term:
  Example: f(x) = 5x³ + 2x² - 3x + 7
  
  Line 1: f'(x) = ?
  Line 2: Take first term: 5x³ → applies power rule → 5·3·x² = 15x²
  Line 3: Take second term: 2x² → applies power rule → 2·2·x = 4x
  Line 4: Take third term: -3x → applies power rule → -3·1 = -3
  Line 5: Take fourth term: 7 → constant → 0
  Line 6: f'(x) = 15x² + 4x - 3

▸ FOR PRODUCT RULE - Show both parts:
  f(x) = u·v where u and v are functions
  Step A: Find u' and v' separately
  Step B: Write f'(x) = u'·v + u·v'
  Step C: Substitute your u', u, v', v values
  Step D: Simplify and combine like terms

▸ FOR QUOTIENT RULE - Careful with order:
  f(x) = u/v
  Top = u, Bottom = v
  Step A: Calculate u' and v'
  Step B: Write (u'·v - u·v') / v²
  IMPORTANT: Numerator is u' TIMES v, MINUS u TIMES v'
  Order matters! Don't mix it up.
  Step C: Simplify numerator, keep v² in denominator
  Step D: Factor if possible to simplify further

▸ FOR CHAIN RULE - Work from outside to inside:
  f(x) = [outer function]([inner function])
  Step A: Identify the inner and outer functions clearly
  Step B: Take derivative of outer function, leave inner intact
  Step C: Multiply by derivative of inner function
  Step D: Simplify and evaluate inner function if simple

▸ FOR MIXED/COMPLEX FUNCTIONS:
  • May need to apply TWO rules together (product + chain, for instance)
  • Apply rules in logical order (usually outside to inside)
  • Keep careful track of what you're substituting where''',
                    'worked_example': '''Example Application for f(x) = (2x + 1)³:

Setup: This is COMPOSITE (chain rule)
  Outer: something cubed [u³]
  Inner: 2x + 1

Solution:
  f'(x) = 3(2x + 1)² · (2)  [derivative of outer × derivative of inner]
        = 6(2x + 1)²  [multiply the constants]

This is the derivative - already simplified!

Alternative Example: f(x) = x·e^(-x²)

Setup: This is PRODUCT (product rule with chain rule inside)
  u = x, u' = 1
  v = e^(-x²), v' = e^(-x²) · (-2x) [chain rule for the exponent]

Solution:
  f'(x) = (1)·e^(-x²) + x·[e^(-x²)·(-2x)]
        = e^(-x²) - 2x²·e^(-x²)
        = e^(-x²)(1 - 2x²)  [factored common e^(-x²)]'''
                },
                {
                    'step': 4,
                    'title': 'Simplify the Derivative Expression',
                    'detailed_explanation': '''STEP 4: CLEAN UP YOUR ANSWER

After applying rules, simplify to make the derivative cleaner and easier to use.

▸ COMBINE LIKE TERMS:
  If you have similar terms, add them:
  Example: f'(x) = 6x² + 3x² - 2x = 9x² - 2x [combined the x² terms]

▸ FACTOR OUT COMMON TERMS IF POSSIBLE:
  Look for factors that appear in multiple terms:
  Example: f'(x) = 12x³ + 4x = 4x(3x² + 1) [factored out 4x]
  
  Why factor? 
  - Shows structure better
  - Useful for finding where derivative = 0
  - Often simpler to work with

▸ CONVERT TO STANDARD FORM:
  - Write using positive exponents when possible
  - No fractions in exponents (unless necessary)
  - Clear, readable expression

▸ DOUBLE-CHECK ALL SIGNS:
  - Are there minus signs that should be plus?
  - Did negatives propagate correctly through rules?
  - Verify signs make sense

▸ VERIFY USING DIMENSIONAL ANALYSIS:
  - If f(x) has degree n, f'(x) should have degree n-1
  - Example: f(x) is cubic (degree 3), f'(x) should be quadratic (degree 2)
  - Exponents should decrease by exactly 1 from power rule

▸ NUMERICAL CHECKS:
  - If possible, plug in a test value (x=1, x=0) and verify calculations
  - Does the derivative value make sense at that point?
  - Is there abrupt weirdness (like infinity where shouldn't be)?''',
                    'worked_example': '''Simplification Example:

Raw result: f'(x) = 3x² + 4x + 2x + 5 - 5
Combine like terms: f'(x) = 3x² + 6x

Factoring Example:
Raw result: f'(x) = 2x · sin(x) + x² · cos(x)
Could factor: f'(x) = x(2sin(x) + x·cos(x))

Sign Check Example:
If answer is f'(x) = -6x + 4, verify the minus sign:
  Original f(x) had −3x² term → contributes −6x to derivative ✓
  Original f(x) had +2x term → contributes +4 to derivative ✓'''
                },
                {
                    'step': 5,
                    'title': 'Verify Result and Interpret in Context',
                    'detailed_explanation': '''STEP 5: VERIFY CORRECTNESS AND EXPLAIN MEANING

Always verify your answer before submitting. This catches errors and builds understanding.

▸ VERIFICATION METHOD 1 - Dimensional Analysis:
  Check that exponent pattern is correct
  • If f(x) = x⁴, then f'(x) should have x³ ✓
  • Each term's exponent should decrease by exactly 1
  • Constant terms → become 0 ✓

▸ VERIFICATION METHOD 2 - Substitute Back (Limiting Cases):
  Plug in a simple value like x = 0 or x = 1:
  • Example: f(x) = 3x² + 1, so f'(x) = 6x
  • At x = 0: f'(0) = 0 makes sense (flat at origin)
  • At x = 1: f'(1) = 6 means steep slope ✓
  
▸ VERIFICATION METHOD 3 - Alternative Method:
  If time permits, solve using different rule order or method
  Compare results - they should match
  
▸ CHECK FOR COMMON MISTAKES:
  □ Did I apply power rule correctly? (exponent comes down and decreases)
  □ Did I include all terms from original function?
  □ Did I use correct rule for function type?
  □ Are signs (+ and -) correct?
  □ Did I simplify fully?

▸ INTERPRET THE RESULT:
  What does f'(x) actually represent?
  
  • f'(x) = instantaneous rate of change of f at point x
  • f'(x) = slope of tangent line to curve at x
  • f'(x) > 0 means f is increasing at that x
  • f'(x) < 0 means f is decreasing at that x
  • f'(x) = 0 means critical point (potential max/min)

▸ IF PROBLEM ASKS FOR SPECIFIC VALUE:
  "Find f'(2)" → substitute x = 2 into f'(x)
  "Find slope at x = -1" → evaluate f'(-1)
  "Find tangent line at point (a, f(a))" 
    → Use m = f'(a) in point-slope form: y - f(a) = f'(a)(x - a)

▸ FINAL ANSWER FORMAT:
  State clearly: "The derivative is f'(x) = [your answer]"
  If asked for specific value: "f'(2) = [calculated value]"
  Include interpretation if context provided''',
                    'worked_example': '''Verification for f(x) = 3x⁴ + 2x, finding f'(x):

Raw calculation: f'(x) = 12x³ + 2

✓ Check 1: Dimensional Analysis
  • 3x⁴ → differentiates to 12x³ (exponent 4→3, decreased by 1) ✓
  • 2x → differentiates to 2 (exponent 1→0) ✓

✓ Check 2: Limiting Case (x=1)
  • f'(1) = 12(1)³ + 2 = 12 + 2 = 14 ✓ (reasonable slope)

✓ Check 3: Sign Verification
  • All coefficients positive, result positive ✓

If asked "Find f'(3)":
  f'(3) = 12(3)³ + 2 = 12(27) + 2 = 324 + 2 = 326
  Answer: The slope of tangent line at x=3 is 326 (very steep!)'''
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
- First derivative f'(x) gives slope of tangent line at any point
- f'(x) > 0 → function is INCREASING (going up)
- f'(x) < 0 → function is DECREASING (going down)
- f'(x) = 0 → critical points where maxima/minima can occur
- Multiple derivative rules exist for different function types:
  • Power rule for polynomials
  • Product rule for products
  • Quotient rule for fractions
  • Chain rule for nested functions
  
The key to success: (1) Identify function type, (2) Choose correct rule, (3) Apply carefully, (4) Simplify completely''',
            'common_mistakes': '''
1. FORGETTING CHAIN RULE for composite functions
   · Example error: d/dx[(2x+1)³] = 3(2x+1)² ✗ [missing the ·2!]
   · Correct: d/dx[(2x+1)³] = 3(2x+1)² · 2 = 6(2x+1)² ✓

2. SIGN ERRORS with negative terms
   · Example error: d/dx[-x²] = 2x ✗ [lost the negative!]
   · Correct: d/dx[-x²] = -2x ✓

3. MIXING UP product rule with distribution
   · You cannot distribute when multiplying - must use proper rule
   
4. WRONG EXPONENT LOGIC (exponent doesn't just multiply coefficient)
   · Example error: d/dx[x⁵] = 5x⁵ ✗ [forgot to reduce exponent]
   · Correct: d/dx[x⁵] = 5x⁴ ✓

5. NOT SIMPLIFYING final answer
   · Leave it in factored form when possible: 4x(3x² + 1) better than 12x³ + 4x

6. FORGETTING TO INCLUDE ALL TERMS
   · Example error: f(x) = 3x² + 2x - 5, but only differentiating first term
   · Must differentiate EVERY term

7. QUOTIENT RULE WRONG ORDER (numerator matters)
   · Order: (top' × bottom) - (top × bottom') / (bottom)²
   · Not: (top × bottom') - (top' × bottom) / (bottom)² [wrong!]

8. ASSUMING CHAIN RULE WHEN PRODUCT RULE APPLIES
   · sin(x)·x uses PRODUCT rule, not chain
   · sin(x²) uses CHAIN rule
   · Know the difference!''',
            'answer_location': 'Final answer is the derivative f\'(x) found in Step 4 (Simplify) - the final simplified expression after applying rules and simplification'
        }
    
    def _solve_integral(self, num, text, analysis=None):
        """Detailed integral solution"""
        if analysis is None:
            analysis = self.analyze_problem_requirements(text)
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
8. Arithmetic errors in exponent or constant calculations''',
            'answer_location': 'Final answer is the antiderivative or definite integral value found in Step 4 (Evaluate) - the computed result after integration and evaluation'
        }
    
    def _solve_limit(self, num, text, analysis=None):
        """Detailed limit solution"""
        if analysis is None:
            analysis = self.analyze_problem_requirements(text)
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
            'common_mistakes': 'Not recognizing indeterminate forms, incorrect algebraic manipulation, not checking one-sided limits',
            'answer_location': 'Final answer is the limit value found in Step 4 (Evaluate or Simplify) - the specific numerical value or infinity that the function approaches'
        }
    
    def _solve_physics(self, num, text, analysis=None):
        """Detailed physics solution"""
        if analysis is None:
            analysis = self.analyze_problem_requirements(text)
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
8. Not considering vector directions (magnitude vs signed component)''',
            'answer_location': 'Final answer is the calculated value (force, acceleration, energy, etc.) found in Step 3 (Substitute Values and Calculate) - the computed quantity after substituting numerical values into the physics equation'
        }
    
    def _solve_chemistry(self, num, text, analysis=None):
        """Detailed chemistry solution"""
        if analysis is None:
            analysis = self.analyze_problem_requirements(text)
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
9. Forgetting to match significant figures in final answer''',
            'answer_location': 'Final answer is the calculated quantity (moles, grams, concentration, etc.) found in Step 4 (Calculate Final Result) - the computed value after applying stoichiometric ratios and conversions'
        }
    
    def _solve_geometry(self, num, text, analysis=None):
        """Detailed geometry solution"""
        if analysis is None:
            analysis = self.analyze_problem_requirements(text)
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
9. Using wrong formula (area vs. circumference confusion)''',
            'answer_location': 'Final answer is the calculated measurement (area, volume, perimeter, angle, etc.) found in Step 4 (Calculate and Verify) - the numerical value with appropriate units after applying geometric formulas'
        }
    
    def _solve_algebra(self, num, text, analysis=None):
        """Detailed algebra solution"""
        if analysis is None:
            analysis = self.analyze_problem_requirements(text)
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
10. Not distributing properly when removing parentheses''',
            'answer_location': 'Final answer is the solution value(s) found in Step 4 (Solve) or Step 5 (Verify Solution) - the value(s) of the variable that satisfy the equation'
        }
    
    def _solve_general(self, num, text, analysis=None):
        """General purpose solver for any problem"""
        if analysis is None:
            analysis = self.analyze_problem_requirements(text)
        
        return {
            'number': num,
            'type': 'GENERAL PROBLEM',
            'problem': text,
            'problem_analysis': {
                'what_is_asked': analysis.get('exact_question', 'Solve the problem'),
                'exact_target': 'Identify and solve what\'s being asked',
                'given_information': analysis.get('given_info', ['Information from problem']),
                'what_to_find': analysis.get('unknowns', ['The target unknown']),
                'problem_type': analysis.get('problem_objectives', ['General problem']),
                'key_constraints': analysis.get('key_constraints', []),
                'key_steps_overview': [
                    '1. Carefully read and understand what is being asked',
                    '2. Identify and organize all given information',
                    '3. Determine what needs to be found (your target)',
                    '4. Select the appropriate method or formula',
                    '5. Execute the solution step-by-step',
                    '6. Verify the answer makes sense in context'
                ]
            },
            'steps': [
                {
                    'step': 1,
                    'title': 'Carefully Analyze and Understand the Problem',
                    'detailed_explanation': '''STEP 1: COMPREHENSIVE PROBLEM ANALYSIS

The first critical step in solving ANY problem is to fully understand what is being asked. Many errors come from misinterpreting the problem, so take time with this step.

▸ READ THE PROBLEM MULTIPLE TIMES SLOWLY:
  • First reading: Get the overall context and general idea
  • Second reading: Identify specific quantities, numbers, and relationships
  • Third reading: Determine EXACTLY what is being asked to find
  • Fourth reading: Look for hidden conditions or special cases

▸ EXTRACT AND LIST ALL GIVEN INFORMATION:
  • Write down every numerical value with its variable symbol
  • Include units for each quantity (meters, seconds, kilograms, etc.)
  • Note any mathematical relationships between variables
  • Identify constraints or special conditions mentioned
  • Look for implied information (e.g., "object at rest" means initial velocity = 0)

▸ CLEARLY DEFINE THE UNKNOWN:
  • What quantity specifically needs to be determined?
  • What units should the answer have?
  • Are there multiple unknowns or just one main target?

▸ ASSESS PROBLEM TYPE AND CONTEXT:
  • Have you seen a similar problem in textbook or class?
  • What chapter or topic does this relate to?
  • What general method category fits (algebra, geometry, rate, force, etc.)?
  • What assumptions might be necessary (friction exists or doesn't, air resistance, etc.)?

▸ CREATE CLEAR VARIABLE DEFINITIONS:
  • Use standard symbols (v for velocity, F for force, m for mass, t for time)
  • Write: "Let x = ..." to define your variables clearly
  • Use subscripts for clarity (v₀ for initial velocity, v_f for final velocity)
  • This prevents confusion when writing equations''',
                    'worked_example': '''Example Problem: "A ball is thrown upward from ground level with an initial velocity of 20 m/s. How long does it take to return to ground level? (Use g = 10 m/s²)"

ANALYSIS:
Given:
  • v₀ = 20 m/s (initial velocity, upward direction)
  • Position₀ = 0 m (ground level start)
  • Position_final = 0 m (returns to ground)
  • g = 10 m/s² (gravitational acceleration, downward)

Find: t = time when ball returns to ground level

Context: This is a projectile motion problem using kinematic equations

Key observation: The ball returns to SAME height (ground), so displacement = 0'''
                },
                {
                    'step': 2,
                    'title': 'Identify and Gather All Relevant Formulas and Theories',
                    'detailed_explanation': '''STEP 2: SELECT THE RIGHT MATHEMATICAL TOOLS

Now that problem is understood, identify which formulas, theorems, and principles apply. Using the right tool makes solving efficient.

▸ DETERMINE PROBLEM CATEGORY:
  • Is this about motion, forces, energy, heat, electricity, geometry, algebra?
  • What specific topic within that category (constant velocity vs. acceleration)?
  • What domain of physics/math does it use?

▸ LIST ALL POTENTIALLY RELEVANT FORMULAS:
  • Write out EACH formula completely
  • Define EVERY variable in that formula clearly
  • Note the units for each variable
  • State any conditions when that formula is valid
  • Example: "v = v₀ + at is valid only for constant acceleration"

▸ DETERMINE NECESSARY INFORMATION FOR EACH FORMULA:
  • For each formula, identify what inputs it needs
  • Check if you have all those inputs from the problem
  • If you're missing something, you need a different formula or intermediate step

▸ UNDERSTAND THE THEORY BEHIND THE FORMULAS:
  • Why does each formula work? What's the underlying principle?
  • What assumptions does it make?
  • When might it NOT apply?
  • How does it relate to other formulas in this topic?

▸ IDENTIFY CONNECTIONS BETWEEN FORMULAS:
  • Can one formula be derived from another?
  • Do some formulas solve for the same quantity using different methods?
  • Which sequence of formulas will get you from given to unknown?

▸ COMPARE ALTERNATIVE APPROACHES:
  • Are there multiple ways to solve this?
  • Which path is most direct or simpler?
  • Which requires fewer intermediate calculations?''',
                    'worked_example': '''For the ball problem above:

FORMULA OPTIONS:
1. s = v₀t + ½at² [displacement formula]
   - Inputs needed: v₀ (have it), a (acceleration, have g=10 m/s²), t (unknown, solving for)
   - This looks promising!

2. v = v₀ + at [velocity formula]
   - Inputs needed: v₀, a, t
   - Doesn't directly help find time

3. v² = v₀² + 2as [energy-based formula]
   - Inputs needed: s (displacement, which is 0!)
   - This would give: v² = 20² + 0, which doesn't help

BEST CHOICE: Use s = v₀t + ½at²
  • We know s = 0 (returns to ground)
  • We know v₀ = 20 m/s (initial velocity)
  • We know a = -10 m/s² (gravity acts downward)
  • We need to find t'''
                },
                {
                    'step': 3,
                    'title': 'Develop and Outline Your Complete Solution Strategy',
                    'detailed_explanation': '''STEP 3: PLAN YOUR APPROACH BEFORE CALCULATING

Before doing ANY calculations, map out your complete solution path. This prevents mistakes and wasted effort.

▸ CREATE A STEP-BY-STEP OUTLINE:
  • What is the FIRST calculation you'll perform?
  • What does that calculation tell you?
  • What calculation comes NEXT and why?
  • How does result from step 1 feed into step 2?
  • Continue this logic until reaching final answer
  • Write outline BEFORE starting calculations

▸ IDENTIFY INTERMEDIATE VALUES:
  • What helper calculations are needed?
  • In what sequence should they occur?
  • Does calculation B depend on result of calculation A?
  • Are there any parallel paths that must merge?

▸ VERIFY LOGICAL COMPLETENESS:
  • Does each step lead naturally to the next?
  • Have you avoided large logical jumps?
  • Could someone else follow your plan without getting lost?
  • Are dependencies between steps clear?

▸ CONSIDER ALTERNATIVE SOLUTION PATHS:
  • Is there a different sequence that might be simpler?
  • Would using different formulas make it clearer?
  • What are advantages and disadvantages of each approach?
  • Which path shows the concepts most clearly?

▸ PLAN YOUR VERIFICATION STRATEGY:
  • What checks will confirm correctness?
  • Can you solve it a completely different way to verify?
  • How should the units work out?
  • What should the magnitude of answer be approximately?''',
                    'worked_example': '''SOLUTION PLAN FOR BALL PROBLEM:

Step A (Setup):
  Identify that we use: 0 = 20t - ½(10)t²
  Why: displacement = 0, so s = v₀t + ½at² becomes 0 = 20t - 5t²

Step B (Algebra):
  Rearrange: 0 = 20t - 5t²
  Factor: 0 = t(20 - 5t)
  Why: Factor out common t to get solvable form

Step C (Solve):
  From factored form get two solutions:
  • t = 0 (ball at ground at start-makes sense)
  • 20 - 5t = 0, so t = 4 seconds (what we want)

Step D (Verify):
  Check: Does t = 4s make physical sense?
  Method 1: Substitute back: 0 = 20(4) - 5(4²) = 80 - 80 = 0 ✓
  Method 2: Symmetry check (up and down should be equal time) ✓
  Method 3: Is 4 seconds reasonable for 20 m/s throw? Yes, seems right ✓'''
                },
                {
                    'step': 4,
                    'title': 'Execute Calculations Methodically, Showing All Work',
                    'detailed_explanation': '''STEP 4: DO THE MATH STEP-BY-STEP WITH FULL DETAIL

Now execute your planned approach carefully and completely. Show EVERY step so work can be followed and checked.

▸ WRITE EVERY SUBSTITUTION EXPLICITLY:
  • Start with the chosen formula
  • Show blank formula: s = v₀t + ½at²
  • Fill in each value step-by-step: s = (20)t + ½(-10)t²
  • Use proper symbols for each quantity
  • Include units in parentheses: (0 m) = (20 m/s)·t + ½(-10 m/s²)·t²

▸ PERFORM ALGEBRAIC OPERATIONS ONE AT A TIME:
  • Each line should show ONE operation
  • Never skip steps, even if they seem obvious
  • Show: 0 = 20t - 5t² (first simplified the ½(-10) to -5)
  • Then: 0 = t(20 - 5t) (factored out t)
  • Then: t = 0 or 20 - 5t = 0 (applied zero product rule)
  • Then: t = 0 or t = 4 s (solved each factor)

▸ HANDLE UNITS CAREFULLY THROUGHOUT:
  • Keep units attached to every number
  • Cancel units like algebraic variables
  • Example: (20 m/s) × (s) = 20 m (units of meters, correct for displacement)
  • If units don't work out, you made an error

▸ MAINTAIN APPROPRIATE PRECISION:
  • Don't round intermediate results (loss of precision)
  • Work with full precision until final step
  • Keep track of significant figures from input data
  • Only round the FINAL answer appropriately

▸ DOUBLE-CHECK EVERY ARITHMETIC OPERATION:
  • Verify each multiplication and division
  • Check signs carefully
  • Look for common arithmetic errors
  • Use approximation to check: Does 5 × 4² roughly equal 80? Yes, 5 × 16 = 80 ✓''',
                    'worked_example': '''DETAILED CALCULATION FOR BALL PROBLEM:

Given: v₀ = 20 m/s, a = -10 m/s² (gravity downward), s = 0 m (returns to start)
Using: s = v₀t + ½at²

SUBSTITUTION:
0 = (20)(t) + ½(-10)(t²)

SIMPLIFICATION:
0 = 20t + (-5)t²
0 = 20t - 5t²

FACTORING:
0 = 5t(4 - t)  [factored out 5t from both terms]
Actually cleaner: 0 = t(20 - 5t)

APPLYING ZERO PRODUCT RULE (if A·B = 0, then A = 0 or B = 0):
Either: t = 0
Or: 20 - 5t = 0

SOLVING SECOND EQUATION:
20 - 5t = 0
20 = 5t
t = 20/5
t = 4 seconds

UNITS CHECK:
Displacement calculation: (20 m/s)(4 s) - (5 m/s²)(4 s)² = 80 m - 80 m = 0 m ✓'''
                },
                {
                    'step': 5,
                    'title': 'Verify Results and Communicate Your Answer',
                    'detailed_explanation': '''STEP 5: VERIFY, INTERPRET, AND COMMUNICATE FINDINGS

Never accept an answer without verification. This final step catches errors and builds confidence.

▸ VERIFY THE ANSWER USING MULTIPLE METHODS:
  • Method 1 - Substitution Back: Plug answer back into original formula
    For t = 4: s = 20(4) - 5(16) = 80 - 80 = 0 ✓ Correct!
  • Method 2 - Alternate Approach: Solve using completely different method
    Could use symmetry: time to go up = time to come down = 4/2 = 2 s up + 2 s down
  • Method 3 - Limiting Cases: Check special cases or known scenarios
    At t = 2s (peak): v = 20 - 10(2) = 0 m/s ✓ velocity = 0 at peak, correct!

▸ CHECK DIMENSIONAL ANALYSIS (UNITS):
  • Verify final units match what was asked
  • The answer should be in seconds (time), ours is: t = 4 s ✓
  • All intermediate units should have canceled properly
  • If units are wrong, entire calculation is wrong

▸ ASSESS REASONABLENESS AND MAGNITUDE:
  • Does answer make physical sense?
  • Does magnitude match intuition?
  • Is it too small, too large, or just right?
  • For our answer: 4 seconds to throw ball up and catch it-yes, seems reasonable
  • As reference: 20 m/s ≈ 45 mph (a moderate throwing speed)

▸ CHECK SIGN AND DIRECTION:
  • Positive vs. negative has meaning (direction, increase vs. decrease)
  • Our answer is positive, which is correct (time can't be negative)
  • Any negative signs in solution should be physically justified

▸ VALIDATE AGAINST ORIGINAL CONSTRAINTS:
  • Does answer satisfy original problem statement?
  • Did we answer what was ASKED (not something else)?
  • Are all conditions from problem satisfied?
  • For our problem: Ball should return to ground-yes, happens at t = 4s

▸ STATE ANSWER CLEARLY WITH INTERPRETATION:
  • Write answer prominently: t = 4 seconds
  • Explain what it means: "The ball takes 4 seconds to return to ground level"
  • Note which of the multiple solutions is the answer: "We discard t = 0 as that's initial time"
  • Add context if relevant: "This is typical for a human-thrown object"

▸ DISCUSS IMPLICATIONS AND CONNECTIONS:
  • What does this result tell us about the motion?
  • At t = 2s, what is happening? (at peak, maximum height)
  • What would happen if initial velocity were different?
  • How does this connect to other related problems?''',
                    'worked_example': '''VERIFICATION FOR BALL PROBLEM:

✓ CHECK 1 - SUBSTITUTION BACK:
  s = 20t - 5t² at t = 4
  s = 20(4) - 5(16)
  s = 80 - 80
  s = 0 ✓ Correct! (ball back at ground level)

✓ CHECK 2 - ALTERNATIVE METHOD (SYMMETRY):
  Ball goes up then down
  Time to reach peak: v = v₀ - gt → 0 = 20 - 10t_peak → t_peak = 2 s
  Time down = Time up = 2 s
  Total time = 2 + 2 = 4 s ✓ Same answer!

✓ CHECK 3 - LIMITING CASE:
  At t = 2s (should be at peak):
  Height: s = 20(2) - 5(4) = 40 - 20 = 20 m (positive, above ground) ✓
  Velocity: v = 20 - 10(2) = 0 m/s ✓ (zero at peak, correct)

✓ CHECK 4 - UNITS:
  Answer is in seconds ✓ (correct time units)

✓ CHECK 5 - REASONABLENESS:
  4 seconds for a 45 mph throw? Yes, very reasonable ✓
  Peak height should be around 20 m? For 20 m/s throw, yes about right ✓

FINAL ANSWER: t = 4 seconds
INTERPRETATION: The ball takes 4 seconds to rise and fall back to ground level.'''
                }
            ],
            'theories': [
                'Problem-solving methodology',
                'Logical reasoning',
                'Mathematical principles',
                'Unit analysis',
                'Verification techniques'
            ],
            'key_concepts': '''The universal 5-step problem-solving method:
① UNDERSTAND: Read carefully, identify given/unknown, set up notation.
② GATHER TOOLS: Find relevant formulas, understand theories, assess approaches.
③ PLAN: Outline complete strategy, identify dependencies, check connections.
④ EXECUTE: Show all work step-by-step, maintain units, check arithmetic.
⑤ VERIFY: Substitute back, use alternative methods, assess reasonableness.

This systematic methodology works across all domains-mathematics, physics, chemistry, engineering, and beyond. The key is being methodical and thorough at each step. Every problem is solvable using this framework.''',
            'common_mistakes': '''1. NOT READING CAREFULLY ENOUGH
   • Misunderstanding what's being asked for
   • Missing important conditions or constraints
   • Confusing given information with unknowns
   → FIX: Read problem 3-4 times, highlight key phrases

2. SKIPPING IMMEDIATE STEPS
   • Jumping to formula without understanding
   • Trying to do too much in one step
   • Not showing work clearly
   → FIX: Write out every substitution, one operation per line

3. UNIT ERRORS
   • Forgetting units in calculations
   • Unit mismatch in formulas
   • Not canceling/converting units properly
   → FIX: Carry units through entire calculation, verify at end

4. ROUNDING TOO EARLY
   • Rounding intermediate results loses precision
   • Final answer loses accuracy
   • Calculation drift accumulates
   → FIX: Keep full precision until final answer only

5. SELECTING WRONG FORMULA
   • Choosing formula that doesn't apply
   • Missing that you need intermediate step first
   • Not checking if you have all formula inputs
   → FIX: List all options, verify you have inputs, trace formula requirements

6. ALGEBRAIC MISTAKES
   • Sign errors (+/- confusion)
   • Incorrect factoring or cancellation
   • Arithmetic errors in basic operations
   → FIX: Verify each algebraic step, check with substitute values

7. SKIPPING VERIFICATION
   • Not checking if answer is reasonable
   • Not substituting back to confirm
   • Ignoring what answer means
   → FIX: Always verify using multiple methods, assess reasonableness

8. NOT IDENTIFYING PROBLEM TYPE
   • Not recognizing which domain/method applies
   • Missing similar problems already solved
   • Not connecting to relevant theory
   → FIX: Categorize problem first, recall similar examples, identify domain''',
            'answer_location': 'Final answer is in Step 5 (Verify and Interpret Result) - the computed value after all calculations and verification'
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
    language_support = _LanguageSupport()
    language_counts = {'en': 0, 'es': 0}
    
    for idx, problem in enumerate(problems, 1):
      problem_text = problem.get('text', 'No description')
      detected_lang = language_support.detect_language(problem_text)
      if detected_lang not in language_counts:
        language_counts[detected_lang] = 0
      language_counts[detected_lang] += 1

      solution = solver.generate_detailed_solution(
            idx,
        problem_text,
            problem.get('type', 'math')
        )
      solution['language'] = detected_lang
      if detected_lang != 'en':
        translated_solution = _translate_value(
          solution,
          language_support,
          detected_lang,
          skip_keys={'problem'}
        )
        translated_solution['problem'] = problem_text
        translated_solution['language'] = detected_lang
        report['problems_analyzed'].append(translated_solution)
      else:
        report['problems_analyzed'].append(solution)
    
    # Generate cliff notes summary
    report['cliff_notes'] = generate_cliff_notes(report['problems_analyzed'], theories_dict)
    if language_counts.get('es', 0) > language_counts.get('en', 0):
      report['cliff_notes'] = _translate_value(report['cliff_notes'], language_support, 'es')
    
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

