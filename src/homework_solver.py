"""
Core analysis engine for the AI Homework Analyzer.
Provides PDF extraction, problem parsing, theory lookup, and solution formatting.
"""

from __future__ import annotations

from enum import Enum
import re
from typing import List, Dict, Optional


try:
	import pdfplumber
except Exception:  # pragma: no cover - handled gracefully at runtime
	pdfplumber = None


class ProblemType(Enum):
	"""High-level problem categories."""

	MATH = "math"
	PHYSICS = "physics"
	CHEMISTRY = "chemistry"
	MECHANICAL = "mechanical"
	CIVIL = "civil"
	ELECTRICAL = "electrical"
	CHEMICAL = "chemical"
	AEROSPACE = "aerospace"
	CALCULUS = "calculus"
	THERMODYNAMICS = "thermodynamics"
	FLUID_MECHANICS = "fluid_mechanics"
	CIRCUITS = "circuit_analysis"


class TheoryBase:
	"""Central theory database used for solution generation and visualization."""

	THEORIES: Dict[str, List[str]] = {
		"calculus": [
			"derivative",
			"integral",
			"limit",
			"chain rule",
			"product rule",
			"quotient rule",
			"fundamental theorem of calculus",
			"l'Hopital's rule",
		],
		"algebra": [
			"linear equations",
			"quadratic formula",
			"factoring techniques",
			"polynomial operations",
			"systems of equations",
		],
		"geometry": [
			"area formulas",
			"volume formulas",
			"pythagorean theorem",
			"trigonometric identities",
			"coordinate geometry",
		],
		"physics": [
			"newton's laws",
			"kinematics",
			"work-energy theorem",
			"momentum conservation",
			"power relationships",
		],
		"chemistry": [
			"stoichiometry",
			"chemical equilibrium",
			"gas laws",
			"thermochemistry",
			"acid-base reactions",
		],
		"mechanics_of_materials": [
			"stress",
			"strain",
			"hooke's law",
			"young's modulus",
			"beam bending",
		],
		"dynamics": [
			"kinematic equations",
			"free-body diagrams",
			"impulse-momentum",
			"work-energy",
		],
		"thermodynamics": [
			"first law of thermodynamics",
			"entropy",
			"enthalpy",
			"ideal gas law",
			"thermodynamic cycles",
		],
		"fluid_mechanics": [
			"continuity equation",
			"bernoulli's equation",
			"laminar vs turbulent flow",
			"pressure head",
		],
		"heat_transfer": [
			"conduction",
			"convection",
			"radiation",
			"fourier's law",
		],
		"circuit_analysis": [
			"ohm's law",
			"kirchhoff's current law",
			"kirchhoff's voltage law",
			"power in circuits",
		],
		"electromagnetics": [
			"coulomb's law",
			"electric field",
			"magnetic field",
			"gauss's law",
		],
		"mass_balance": [
			"conservation of mass",
			"process streams",
			"overall balance",
			"component balance",
		],
		"aerodynamics": [
			"lift and drag",
			"pressure distribution",
			"boundary layer",
			"mach number",
		],
		"structural_analysis": [
			"support reactions",
			"shear and moment",
			"deflection",
			"superposition",
		],
		"control_systems": [
			"transfer function",
			"feedback",
			"pid control",
			"stability",
		],
		"general": [
			"problem analysis",
			"unit consistency",
			"algebraic manipulation",
			"reasonableness check",
		],
	}


class ProblemAnalyzer:
	"""Parses homework problems from PDFs or raw text."""

	def __init__(self, pdf_path: Optional[str] = None):
		self.pdf_path = pdf_path
		self.raw_text = ""

	def extract_text_from_pdf(self, pdf_path: Optional[str] = None) -> str:
		"""Extract text from a PDF file using pdfplumber."""

		if pdf_path:
			self.pdf_path = pdf_path

		if not self.pdf_path:
			return ""

		if pdfplumber is None:
			raise ImportError("pdfplumber is required to extract PDF text")

		extracted = []
		with pdfplumber.open(self.pdf_path) as pdf:
			for idx, page in enumerate(pdf.pages, start=1):
				page_text = page.extract_text() or ""
				extracted.append(f"--- PAGE {idx} ---\n{page_text}\n")

		self.raw_text = "\n".join(extracted)
		return self.raw_text

	def identify_problem_type(self, text: str) -> str:
		"""Identify a problem type based on keyword matching."""

		text_lower = text.lower()

		keyword_map = [
			("calculus", ["derivative", "integral", "limit", "d/d", "differentiate", "∫"]),
			("circuit_analysis", ["kirchhoff", "ohm", "voltage", "current", "circuit", "resistance"]),
			("thermodynamics", ["entropy", "enthalpy", "thermo", "heat", "cycle"]),
			("mechanics_of_materials", ["stress", "strain", "young", "beam", "torsion", "bending"]),
			("fluid_mechanics", ["fluid", "flow", "bernoulli", "continuity", "viscosity"]),
			("heat_transfer", ["conduction", "convection", "radiation", "heat transfer"]),
			("electromagnetics", ["coulomb", "electric", "magnetic", "charge", "field"]),
			("mass_balance", ["mass balance", "stream", "composition", "reactor", "flowrate"]),
			("structural_analysis", ["deflection", "shear", "moment", "support", "truss"]),
			("control_systems", ["controller", "transfer function", "feedback", "pid", "pi controller"]),
			("chemistry", ["stoichiometry", "mole", "reaction", "equilibrium", "acid", "base"]),
			("physics", ["force", "newton", "acceleration", "energy", "momentum", "work"]),
			("algebra", ["quadratic", "linear", "factor", "solve", "polynomial", "equation"]),
			("geometry", ["triangle", "circle", "area", "volume", "perimeter", "angle"]),
			("aerodynamics", ["airfoil", "lift", "drag", "mach", "aero"]),
		]

		for category, keywords in keyword_map:
			if any(keyword in text_lower for keyword in keywords):
				return category

		return "other"

	def parse_problems(self) -> List[Dict[str, str]]:
		"""Parse problems from raw text using multiple delimiter patterns."""

		if not self.raw_text:
			return []

		text = self.raw_text.replace("\r\n", "\n")

		patterns = [
			r"(?:^|\n)\s*(?:Problem|Prob\.?|Question|Q|Exercise|Ex\.?|E|Pr\.?)[\s#]*([0-9]+)\s*[:.\-]*\s*",
			r"(?:^|\n)\s*([0-9]+)\s*[.)\-]\s+",
			r"(?:^|\n)\s*(?:Section|Part)\s*([0-9]+)\s*[:.\-]*\s*",
			r"(?:^|\n)\s*(?:Pagina|Página|Page)\s*([0-9]+)\s*[:.\-]*\s*",
		]

		for pattern in patterns:
			matches = list(re.finditer(pattern, text, flags=re.IGNORECASE | re.MULTILINE))
			if not matches:
				continue

			problems: List[Dict[str, str]] = []
			for idx, match in enumerate(matches, start=1):
				start = match.end()
				end = matches[idx].start() if idx < len(matches) else len(text)
				problem_text = text[start:end].strip()
				if not problem_text:
					continue

				number_str = match.group(1) if match.groups() else str(idx)
				try:
					number = int(number_str)
				except ValueError:
					number = idx

				problems.append({
					"number": number,
					"text": problem_text,
					"type": self.identify_problem_type(problem_text),
				})

			if problems:
				return problems

		chunks = [chunk.strip() for chunk in re.split(r"\n{2,}", text) if chunk.strip()]
		problems = []
		for idx, chunk in enumerate(chunks, start=1):
			if len(chunk) < 10:
				continue
			problems.append({
				"number": idx,
				"text": chunk,
				"type": self.identify_problem_type(chunk),
			})
		return problems


class HomeworkAnalyzerAlgorithm(ProblemAnalyzer):
	"""End-to-end analyzer used by web and GUI apps."""

	def extract_and_analyze(self, pdf_path: Optional[str] = None) -> List[Dict[str, str]]:
		"""Extract PDF text and return parsed problems."""

		self.extract_text_from_pdf(pdf_path)
		return self.parse_problems()


class SolutionGenerator:
	"""Formats a human-readable solution report for a single problem."""

	def __init__(self):
		self.theory_base = TheoryBase()

	def _get_theories(self, problem_type: str) -> List[str]:
		key = (problem_type or "").lower()
		return self.theory_base.THEORIES.get(key, self.theory_base.THEORIES["general"])

	def format_solution(self, number: int, problem_text: str, problem_type: str) -> str:
		theories = self._get_theories(problem_type)
		problem_type_upper = (problem_type or "GENERAL").upper()

		header = f"\n{'='*100}\nPROBLEM {number}\n[{problem_type_upper}]\n{'='*100}\n"
		statement = f"📋 PROBLEM STATEMENT\n{problem_text}\n\n"

		theory_lines = "\n".join(f"• {theory.upper()}" for theory in theories)
		theories_block = f"🧠 RELEVANT THEORIES\n{theory_lines}\n\n"

		steps = [
			"1. Identify the given values and unknowns.",
			"2. Select the appropriate formulas or laws.",
			"3. Set up the equations carefully.",
			"4. Solve step-by-step with correct units.",
			"5. Verify the result for reasonableness.",
		]
		steps_block = "\n".join(steps)
		solution_steps = f"📝 SOLUTION STEPS\n{steps_block}\n\n"

		walkthrough = (
			"💬 DETAILED VERBAL WALKTHROUGH\n"
			"We start by interpreting the problem and listing known quantities. "
			"Next, we choose the governing theory and build the equations. "
			"Then we compute the result and check units and magnitude to ensure correctness.\n"
		)

		return header + statement + theories_block + solution_steps + walkthrough

