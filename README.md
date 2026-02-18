# AI Homework Analyzer & Solver - University Engineering Edition

Analyzes school homework PDFs, solves problems step-by-step, and explains the theory and methods used for each solution. Comprehensive support for all major engineering disciplines.

## Features

- ✅ **PDF Text Extraction**: Automatically extracts text from homework PDFs
- ✅ **Problem Classification**: Identifies problem types across multiple engineering disciplines
- ✅ **Comprehensive Theory Database**: Includes theories for:
  - Mathematics (Calculus, Algebra, Geometry)
  - Physics & Chemistry
  - Mechanical Engineering (Materials, Dynamics, Thermodynamics, Fluids, Heat Transfer)
  - Civil Engineering (Structural, Geotechnical, Transportation)
  - Electrical Engineering (Circuits, Electromagnetics, Signals, Power)
  - Chemical Engineering (Mass Balance, Kinetics, Separation)
  - Aerospace Engineering (Aerodynamics, Flight Mechanics)
  - Control Systems & Computer Engineering
  - Materials Science
  - Biomedical Engineering

- ✅ **Solution Framework**: Structured problem solving with:
  - Problem statement identification
  - Relevant theory extraction
  - Step-by-step solution methodology
  - Detailed verbal explanations
  - Unit verification

- ✅ **Report Generation**: Creates comprehensive analysis report

## Installation

### Prerequisites
- Python 3.7+
- pip

### Setup
```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage
1. Place your homework PDF in the project directory
2. Run the solver:
   ```bash
   python src/homework_solver.py
   ```
3. The program will automatically detect available PDFs and process them
4. Results are saved to `homework_analysis_report.txt`

### Specifying a PDF File
Edit the main section of `homework_solver.py` and change:
```python
pdf_file = "your_homework.pdf"
```

## Project Structure

```
homework.ai.py/
├── src/
│   └── homework_solver.py           # Main application
├── tests/
│   └── test_homework_solver.py      # Unit tests
├── samples/
│   └── sample_homework.txt          # Sample test data
├── requirements.txt                  # Python dependencies
├── README.md                        # This file
└── homework_analysis_report.txt     # Generated report (after running)
```

## Supported Problem Types

### Core Sciences
- **Mathematics**: Calculus, Algebra, Geometry
- **Physics**: Kinematics, Newton's Laws, Energy, Momentum
- **Chemistry**: Reactions, Atomic Structure, Bonding

### Mechanical Engineering
- Mechanics of Materials (Stress, Strain, Hooke's Law, Torsion)
- Dynamics (Rotational Motion, Torque, Angular Momentum)
- Thermodynamics (First/Second Laws, Cycles, Efficiency)
- Fluid Mechanics (Bernoulli, Continuity, Reynolds Number)
- Heat Transfer (Conduction, Convection, Radiation)

### Civil Engineering
- Structural Analysis (Equilibrium, Shear/Bending, Deflection)
- Geotechnical (Soil Classification, Bearing Capacity, Consolidation)
- Transportation (Pavement Design, Traffic Flow)

### Electrical Engineering
- Circuit Analysis (Ohm's Law, Kirchhoff's Laws, Power)
- Electromagnetics (Electric/Magnetic Fields, Maxwell's Equations)
- Signal Processing (Fourier, Laplace, Transfer Functions)
- Power Systems (Three-Phase, Power Factor, Transformers)

### Chemical Engineering
- Mass Balance (Conversion, Yield, Selectivity)
- Energy Balance (Enthalpy, Heat of Reaction)
- Reaction Kinetics (Arrhenius Equation, Reaction Order)
- Separation Processes (Distillation, Extraction, Absorption)

### Aerospace Engineering
- Aerodynamics (Lift, Drag, Mach Number, Boundary Layer)
- Flight Mechanics (Thrust, Range, Specific Impulse)

### Advanced Topics
- Control Systems (PID Controllers, Stability, Feedback)
- Computer Engineering (Digital Logic, Microprocessor Architecture)
- Materials Science (Crystal Structure, Phase Diagrams, Properties)

## Theory Database

The application includes an extensive theory database covering:
- **50+ core engineering domains**
- **500+ specific theories and formulas**
- **Detailed descriptions and applications**

Each theory includes:
- Mathematical notation
- Physical interpretation
- Common applications
- Units and dimensions

## Output Format

The generated report includes for each problem:

1. **Problem Statement**: Exact text from the PDF
2. **Relevant Theories**: Applicable formulas and concepts
3. **Solution Steps**: Structured problem-solving methodology
4. **Verbal Explanation**: Detailed walkthrough of solution approach
5. **Verification**: Unit consistency and reasonableness checks

## Example Report

```
PROBLEM 1 - [CALCULUS]

📋 PROBLEM STATEMENT:
Find the derivative of f(x) = x³ + 2x² - 5x + 3

🧠 RELEVANT THEORIES & CONCEPTS:
• DERIVATIVE: Rate of change of a function at a specific point
• POWER RULE: d/dx[x^n] = n*x^(n-1)
• LINEARITY: d/dx[f(x) + g(x)] = f'(x) + g'(x)
...

📝 SOLUTION STEPS:
Step 1: Identify exactly what the problem is asking
Step 2: Write down all given information and units
...
```

## Testing

Run unit tests:
```bash
python tests/test_homework_solver.py
```

## Sample Usage

See `samples/sample_homework.txt` for example input.

## Configuration

To customize problem detection keywords, edit the `identify_problem_type()` method in `ProblemAnalyzer` class.

To add new theories, update the `THEORIES` dictionary in `TheoryBase` class.

## Requirements

- **pdfplumber >= 0.10.0**: For PDF text extraction

## Limitations

- Requires clear, extractable text in PDFs (scanned images not supported without OCR)
- AI explanations are template-based (not AI-generated per problem)
- Best results with typed PDFs from standard homework platforms

## Future Enhancements

- [ ] OCR support for scanned PDFs
- [ ] AI-generated step-by-step solutions
- [ ] LaTeX equation support
- [ ] Problem difficulty assessment
- [ ] Solution verification framework
- [ ] Interactive problem solver
- [ ] Database of solved examples
- [ ] Performance tracking

## License

This project is provided as-is for educational purposes.

## Support

For issues or questions:
1. Check that your PDF is readable and extractable
2. Verify Python and dependencies are properly installed
3. Ensure PDF file is in the correct directory

## Author

AI Homework Analyzer & Solver Team

## Version

1.0.0 - Initial Release (February 2026)
