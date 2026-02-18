"""
Desktop GUI Application with Graphs - AI Homework Analyzer
Full-featured desktop application with visualization support
"""

import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from tkinter.scrolledtext import ScrolledText
import threading
from pathlib import Path
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from homework_solver import HomeworkAnalyzerAlgorithm, TheoryBase
from visualizer import ReportVisualizer


class HomeworkAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("📊 AI Homework Analyzer - Desktop Edition with Graphs")
        self.root.geometry("1400x900")
        self.root.config(bg='#f0f0f0')
        
        # Set style
        style = ttk.Style()
        style.theme_use('clam')
        
        self.analyzer = HomeworkAnalyzerAlgorithm()
        self.theory_base = TheoryBase()
        self.visualizer = None
        self.problems = []
        
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the main UI"""
        # Header
        header = tk.Frame(self.root, bg='#667eea', height=80)
        header.pack(fill=tk.X)
        header.pack_propagate(False)
        
        title = tk.Label(header, text="📊 AI Homework Analyzer with Graphs",
                        font=('Arial', 20, 'bold'), bg='#667eea', fg='white')
        title.pack(pady=10)
        
        subtitle = tk.Label(header, text="Analyze PDFs and visualize with beautiful charts",
                           font=('Arial', 10), bg='#667eea', fg='white')
        subtitle.pack()
        
        # Main content frame
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Left panel - Controls and output
        left_frame = ttk.Frame(main_frame)
        left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        # File selection
        file_frame = ttk.LabelFrame(left_frame, text="📁 File Selection", padding=10)
        file_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.file_label = tk.Label(file_frame, text="No file selected",
                                   fg='#666', bg='white', padx=10, pady=8)
        self.file_label.pack(fill=tk.X)
        
        btn_frame = ttk.Frame(file_frame)
        btn_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(btn_frame, text="📂 Browse PDF",
                  command=self.select_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="🔄 Analyze",
                  command=self.analyze_file).pack(side=tk.LEFT, padx=2)
        ttk.Button(btn_frame, text="📊 Generate Graphs",
                  command=self.generate_graphs).pack(side=tk.LEFT, padx=2)
        
        # Statistics
        stats_frame = ttk.LabelFrame(left_frame, text="📈 Statistics", padding=10)
        stats_frame.pack(fill=tk.X, pady=(0, 10))
        
        self.stats_text = tk.Label(stats_frame, text="No analysis yet",
                                   justify=tk.LEFT, bg='white', padx=10, pady=10)
        self.stats_text.pack(fill=tk.X)
        
        # Output text
        output_frame = ttk.LabelFrame(left_frame, text="📋 Analysis Output", padding=5)
        output_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        self.output_text = ScrolledText(output_frame, height=15, width=50,
                                        font=('Consolas', 9), bg='white')
        self.output_text.pack(fill=tk.BOTH, expand=True)
        
        # Right panel - Graphs
        right_frame = ttk.Frame(main_frame)
        right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=(5, 0))
        
        # Graph tabs
        self.notebook = ttk.Notebook(right_frame)
        self.notebook.pack(fill=tk.BOTH, expand=True)
        
        # Create graph tabs
        self.setup_graph_tabs()
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        status_bar = tk.Label(self.root, textvariable=self.status_var,
                             bd=1, relief=tk.SUNKEN, anchor=tk.W, bg='#e0e0e0')
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def setup_graph_tabs(self):
        """Setup graph display tabs"""
        self.graph_frames = {}
        
        tab_names = [
            ('distribution', '🥧 Distribution'),
            ('count_bar', '📊 Count'),
            ('theory_coverage', '🧠 Theory'),
            ('dashboard', '📈 Dashboard'),
            ('function_example', '📐 Functions')
        ]
        
        for key, name in tab_names:
            frame = ttk.Frame(self.notebook)
            self.notebook.add(frame, text=name)
            self.graph_frames[key] = frame
    
    def select_file(self):
        """Select PDF file"""
        filename = filedialog.askopenfilename(
            title="Select PDF file",
            filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")]
        )
        
        if filename:
            self.current_file = filename
            self.file_label.config(text=f"✅ {Path(filename).name}", fg='#060')
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"File selected: {filename}\n\nClick 'Analyze' to start.")
    
    def analyze_file(self):
        """Analyze PDF in background thread"""
        if not hasattr(self, 'current_file'):
            messagebox.showwarning("Warning", "Please select a file first")
            return
        
        self.status_var.set("Analyzing PDF...")
        self.output_text.delete(1.0, tk.END)
        
        # Run in background thread
        thread = threading.Thread(target=self._analyze_thread)
        thread.daemon = True
        thread.start()
    
    def _analyze_thread(self):
        """Run analysis in background"""
        try:
            # Extract and analyze
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, "📄 Loading PDF...\n")
            self.root.update()
            
            self.problems = self.analyzer.extract_and_analyze(self.current_file)
            
            # Update output
            output_msg = f"✅ Analysis Complete!\n\n"
            output_msg += f"📊 Total Problems Found: {len(self.problems)}\n"
            output_msg += f"🏷️ Problem Types: {len(set(p['type'] for p in self.problems))}\n\n"
            output_msg += "Problems:\n"
            output_msg += "─" * 50 + "\n"
            
            for idx, problem in enumerate(self.problems[:10], 1):
                output_msg += f"\n#{idx}: {problem['type'].upper()}\n"
                output_msg += f"{problem['text'][:150]}...\n"
            
            if len(self.problems) > 10:
                output_msg += f"\n... and {len(self.problems) - 10} more problems"
            
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, output_msg)
            
            # Update statistics
            theories_dict = self.theory_base.THEORIES
            total_theories = sum(len(t) for t in theories_dict.values())
            
            stats = f"""
📈 ANALYSIS RESULTS:
━━━━━━━━━━━━━━━━━━━━━━━━
Problems Found: {len(self.problems)}
Problem Types: {len(set(p['type'] for p in self.problems))}
Theory Database: {total_theories} theories
Engineering Domains: {len(theories_dict)}
            """
            
            self.stats_text.config(text=stats)
            self.status_var.set(f"✅ Analysis complete - {len(self.problems)} problems found")
            
        except Exception as e:
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, f"❌ Error: {str(e)}")
            self.status_var.set(f"❌ Error: {str(e)}")
    
    def generate_graphs(self):
        """Generate and display graphs"""
        if not self.problems:
            messagebox.showwarning("Warning", "Analyze a file first")
            return
        
        self.status_var.set("Generating graphs...")
        
        # Run in background
        thread = threading.Thread(target=self._generate_graphs_thread)
        thread.daemon = True
        thread.start()
    
    def _generate_graphs_thread(self):
        """Generate graphs in background thread"""
        try:
            theories_dict = self.theory_base.THEORIES
            self.visualizer = ReportVisualizer()
            viz_paths = self.visualizer.generate_all_visualizations(self.problems, theories_dict)
            
            # Display graphs in tabs
            self._display_graphs(viz_paths)
            
            self.status_var.set("✅ Graphs generated successfully")
            
        except Exception as e:
            self.status_var.set(f"❌ Graph generation error: {str(e)}")
    
    def _display_graphs(self, viz_paths):
        """Display graphs in tabs"""
        for key, path in viz_paths.items():
            if path and key in self.graph_frames:
                try:
                    # Clear previous content
                    for widget in self.graph_frames[key].winfo_children():
                        widget.destroy()
                    
                    # Load and display image
                    from PIL import Image, ImageTk
                    
                    img = Image.open(path)
                    # Resize to fit frame
                    img.thumbnail((600, 500), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    
                    label = tk.Label(self.graph_frames[key], image=photo, bg='white')
                    label.image = photo  # Keep a reference
                    label.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
                    
                except Exception as e:
                    label = tk.Label(self.graph_frames[key],
                                    text=f"Error displaying graph: {str(e)}",
                                    bg='white', fg='red')
                    label.pack(fill=tk.BOTH, expand=True)


def main():
    root = tk.Tk()
    app = HomeworkAnalyzerGUI(root)
    root.mainloop()


if __name__ == '__main__':
    main()
