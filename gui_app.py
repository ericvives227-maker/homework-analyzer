"""
GUI Application for AI Homework Analyzer & Solver
Uses tkinter for cross-platform desktop GUI
"""

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from homework_solver import HomeworkAnalyzerAlgorithm


class HomeworkSolverGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 AI Homework Analyzer & Solver")
        self.root.geometry("900x700")
        self.root.configure(bg="#f0f0f0")
        
        self.pdf_file = None
        self.setup_ui()
    
    def setup_ui(self):
        """Create the GUI interface"""
        
        # Title
        title = tk.Label(
            self.root,
            text="🎓 AI HOMEWORK ANALYZER & SOLVER",
            font=("Arial", 16, "bold"),
            bg="#f0f0f0",
            fg="#333"
        )
        title.pack(pady=10)
        
        subtitle = tk.Label(
            self.root,
            text="Select a PDF homework file and get instant solutions with theories",
            font=("Arial", 10),
            bg="#f0f0f0",
            fg="#666"
        )
        subtitle.pack()
        
        # File selection frame
        file_frame = tk.Frame(self.root, bg="#ffffff", relief=tk.RIDGE, bd=1)
        file_frame.pack(padx=20, pady=15, fill=tk.X)
        
        tk.Label(file_frame, text="📁 Select PDF File:", font=("Arial", 11, "bold"), bg="#ffffff").pack(anchor="w", padx=10, pady=5)
        
        button_frame = tk.Frame(file_frame, bg="#ffffff")
        button_frame.pack(padx=10, pady=5)
        
        self.browse_btn = tk.Button(
            button_frame,
            text="📂 Browse PDF",
            command=self.browse_file,
            font=("Arial", 10),
            bg="#4CAF50",
            fg="white",
            padx=15,
            pady=8
        )
        self.browse_btn.pack(side=tk.LEFT, padx=5)
        
        self.file_label = tk.Label(
            button_frame,
            text="No file selected",
            font=("Arial", 10),
            bg="#ffffff",
            fg="#999"
        )
        self.file_label.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)
        
        # Supported subjects
        subjects_frame = tk.Frame(self.root, bg="#ffffff", relief=tk.RIDGE, bd=1)
        subjects_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=False)
        
        tk.Label(subjects_frame, text="📚 Supported Subjects:", font=("Arial", 11, "bold"), bg="#ffffff").pack(anchor="w", padx=10, pady=5)
        
        subjects_text = """✅ Mathematics (Calculus, Algebra, Geometry)
✅ Physics & Chemistry
✅ Mechanical Engineering (Materials, Dynamics, Thermodynamics, Fluids, Heat Transfer)
✅ Civil Engineering (Structural, Geotechnical, Transportation)
✅ Electrical Engineering (Circuits, Electromagnetics, Signals, Power)
✅ Chemical Engineering (Mass Balance, Kinetics, Separation)
✅ Aerospace Engineering (Aerodynamics, Flight Mechanics)
✅ Control Systems & Computer Engineering"""
        
        subjects_label = tk.Label(subjects_frame, text=subjects_text, font=("Arial", 9), bg="#ffffff", justify=tk.LEFT)
        subjects_label.pack(anchor="w", padx=10, pady=5)
        
        # Action buttons
        button_frame2 = tk.Frame(self.root, bg="#f0f0f0")
        button_frame2.pack(pady=15)
        
        self.analyze_btn = tk.Button(
            button_frame2,
            text="🚀 Analyze & Generate Solutions",
            command=self.analyze,
            font=("Arial", 11, "bold"),
            bg="#2196F3",
            fg="white",
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.analyze_btn.pack(side=tk.LEFT, padx=5)
        
        self.view_btn = tk.Button(
            button_frame2,
            text="📖 View Report",
            command=self.view_report,
            font=("Arial", 11, "bold"),
            bg="#FF9800",
            fg="white",
            padx=20,
            pady=10,
            state=tk.DISABLED
        )
        self.view_btn.pack(side=tk.LEFT, padx=5)
        
        # Status/Results area
        tk.Label(self.root, text="📊 Status & Output:", font=("Arial", 11, "bold"), bg="#f0f0f0").pack(anchor="w", padx=20, pady=(10, 5))
        
        self.output_text = scrolledtext.ScrolledText(
            self.root,
            height=12,
            font=("Courier", 9),
            bg="#2b2b2b",
            fg="#00ff00",
            insertbackground="white"
        )
        self.output_text.pack(padx=20, pady=5, fill=tk.BOTH, expand=True)
        
        # Footer
        footer = tk.Label(
            self.root,
            text="💾 Reports saved to: homework_analysis_report.txt | © 2026 AI Homework Analyzer",
            font=("Arial", 8),
            bg="#f0f0f0",
            fg="#999"
        )
        footer.pack(pady=5)
    
    def browse_file(self):
        """Open file dialog to select PDF"""
        file_path = filedialog.askopenfilename(
            title="Select a PDF homework file",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")],
            initialdir=os.getcwd()
        )
        
        if file_path:
            self.pdf_file = file_path
            filename = os.path.basename(file_path)
            self.file_label.config(text=f"✅ {filename}", fg="#4CAF50")
            self.analyze_btn.config(state=tk.NORMAL)
            self.view_btn.config(state=tk.NORMAL)
            self.log(f"✅ Selected file: {filename}\n")
    
    def log(self, message):
        """Output message to text area"""
        self.output_text.insert(tk.END, message)
        self.output_text.see(tk.END)
        self.root.update()
    
    def analyze(self):
        """Run the homework analyzer"""
        if not self.pdf_file:
            messagebox.showerror("Error", "Please select a PDF file first")
            return
        
        if not os.path.exists(self.pdf_file):
            messagebox.showerror("Error", f"File not found: {self.pdf_file}")
            return
        
        try:
            self.output_text.delete(1.0, tk.END)
            self.log("🚀 Starting analysis...\n")
            self.log(f"📄 File: {os.path.basename(self.pdf_file)}\n")
            self.log("=" * 60 + "\n")
            
            # Change to file's directory
            original_dir = os.getcwd()
            os.chdir(os.path.dirname(self.pdf_file) or ".")
            
            # Run analyzer
            algorithm = HomeworkAnalyzerAlgorithm(os.path.basename(self.pdf_file))
            algorithm.run()
            
            os.chdir(original_dir)
            
            self.log("\n" + "=" * 60)
            self.log("\n✅ Analysis complete!\n")
            self.log("📊 Results saved to: homework_analysis_report.txt\n")
            
            messagebox.showinfo("Success", "Analysis complete! Check the output area and homework_analysis_report.txt")
            
        except Exception as e:
            self.log(f"\n❌ Error: {str(e)}\n")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
    
    def view_report(self):
        """View the generated report"""
        if not os.path.exists("homework_analysis_report.txt"):
            messagebox.showwarning("Warning", "No report found. Run analysis first.")
            return
        
        try:
            with open("homework_analysis_report.txt", "r", encoding="utf-8") as f:
                content = f.read()
            
            # Create new window
            report_window = tk.Toplevel(self.root)
            report_window.title("📖 Homework Analysis Report")
            report_window.geometry("1000x700")
            
            # Text area
            text_area = scrolledtext.ScrolledText(
                report_window,
                font=("Courier", 9),
                bg="#2b2b2b",
                fg="#00ff00"
            )
            text_area.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
            text_area.insert(1.0, content)
            text_area.config(state=tk.DISABLED)
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not open report:\n{str(e)}")


def main():
    root = tk.Tk()
    app = HomeworkSolverGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
