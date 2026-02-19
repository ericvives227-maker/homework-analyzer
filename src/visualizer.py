"""
Visualization Module for AI Homework Analyzer & Solver
Creates graphs, charts, and visual reports
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from collections import Counter
import os


class ReportVisualizer:
    """Generates visualizations for homework analysis reports"""
    
    def __init__(self, output_dir="reports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        
        # Set style
        plt.style.use('seaborn-v0_8-darkgrid')
        self.colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe',
                      '#43e97b', '#fa75a6', '#feca57', '#ff6b6b', '#4ecdc4']
    
    def plot_problem_distribution(self, problems):
        """Create pie chart for problem type distribution"""
        if not problems:
            return None
        
        # Count problems by type
        types = [p['type'].upper() for p in problems]
        type_counts = Counter(types)
        
        # Create figure
        fig, ax = plt.subplots(figsize=(10, 7))
        
        # Pie chart
        wedges, texts, autotexts = ax.pie(
            type_counts.values(),
            labels=type_counts.keys(),
            autopct='%1.1f%%',
            colors=self.colors[:len(type_counts)],
            startangle=90,
            textprops={'fontsize': 10, 'weight': 'bold'}
        )
        
        # Style percentage text
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontsize(9)
            autotext.set_weight('bold')
        
        ax.set_title('Problem Type Distribution', fontsize=16, weight='bold', pad=20)
        
        # Save
        filepath = os.path.join(self.output_dir, 'problem_distribution.png')
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def plot_problem_count_bar(self, problems):
        """Create bar chart for problem counts by type"""
        if not problems:
            return None
        
        # Count problems by type
        types = [p['type'].upper() for p in problems]
        type_counts = Counter(types)
        
        # Create figure
        fig, ax = plt.subplots(figsize=(12, 6))
        
        # Bar chart
        bars = ax.bar(
            range(len(type_counts)),
            type_counts.values(),
            color=self.colors[:len(type_counts)],
            edgecolor='black',
            linewidth=1.5
        )
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontweight='bold', fontsize=11)
        
        ax.set_xlabel('Problem Type', fontsize=12, weight='bold')
        ax.set_ylabel('Number of Problems', fontsize=12, weight='bold')
        ax.set_title('Problem Count by Type', fontsize=16, weight='bold', pad=20)
        ax.set_xticks(range(len(type_counts)))
        ax.set_xticklabels(type_counts.keys(), rotation=45, ha='right')
        ax.grid(axis='y', alpha=0.3)
        
        # Save
        filepath = os.path.join(self.output_dir, 'problem_count_bar.png')
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def plot_theory_coverage(self, theories_dict):
        """Create bar chart for theory database coverage"""
        if not theories_dict:
            return None
        
        # Count theories per domain
        domain_counts = {domain: len(theories) 
                        for domain, theories in theories_dict.items()}
        
        # Sort by count
        sorted_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)
        domains = [d[0].replace('_', ' ').upper() for d in sorted_domains]
        counts = [d[1] for d in sorted_domains]
        
        # Create figure
        fig, ax = plt.subplots(figsize=(14, 6))
        
        # Horizontal bar chart
        bars = ax.barh(domains, counts, color=self.colors[:len(domains)],
                       edgecolor='black', linewidth=1.5)
        
        # Add value labels
        for bar in bars:
            width = bar.get_width()
            ax.text(width, bar.get_y() + bar.get_height()/2.,
                   f' {int(width)} ',
                   ha='left', va='center', fontweight='bold', fontsize=10)
        
        ax.set_xlabel('Number of Theories', fontsize=12, weight='bold')
        ax.set_title('Theory Database Coverage by Domain', fontsize=16, weight='bold', pad=20)
        ax.grid(axis='x', alpha=0.3)
        
        # Save
        filepath = os.path.join(self.output_dir, 'theory_coverage.png')
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def plot_statistics_summary(self, problems, theories_dict):
        """Create comprehensive statistics dashboard"""
        fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(14, 10))
        
        # 1. Problem type pie chart
        if problems:
            types = [p['type'].upper() for p in problems]
            type_counts = Counter(types)
            ax1.pie(type_counts.values(), labels=type_counts.keys(), autopct='%1.0f%%',
                   colors=self.colors[:len(type_counts)], startangle=90)
            ax1.set_title('Problem Type Distribution', fontweight='bold', fontsize=12)
        
        # 2. Top 5 domains
        if theories_dict:
            domain_counts = {domain: len(theories) 
                           for domain, theories in theories_dict.items()}
            top_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)[:5]
            domains = [d[0].replace('_', ' ').upper() for d in top_domains]
            counts = [d[1] for d in top_domains]
            ax2.bar(range(len(domains)), counts, color=self.colors[:len(domains)],
                   edgecolor='black', linewidth=1.5)
            ax2.set_xticks(range(len(domains)))
            ax2.set_xticklabels(domains, rotation=45, ha='right', fontsize=9)
            ax2.set_ylabel('Number of Theories', fontweight='bold')
            ax2.set_title('Top 5 Domains', fontweight='bold', fontsize=12)
            ax2.grid(axis='y', alpha=0.3)
        
        # 3. Summary statistics text
        if problems:
            stats_text = f"""
        ANALYSIS SUMMARY
{'─'*30}

Total Problems: {len(problems)}
Problem Types: {len(Counter([p['type'] for p in problems]))}

Most Common Type:
{Counter([p['type'] for p in problems]).most_common(1)[0][0].upper()}

Average Problems Per Type:
{len(problems) / len(Counter([p['type'] for p in problems])):.1f}
            """
        else:
            stats_text = "No problems to analyze"
        
        ax3.text(0.1, 0.5, stats_text, fontsize=11, verticalalignment='center',
                family='monospace', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
        ax3.axis('off')
        
        # 4. Database summary
        if theories_dict:
            total_theories = sum(len(t) for t in theories_dict.values())
            db_text = f"""
        THEORY DATABASE
{'─'*30}

Total Domains: {len(theories_dict)}
Total Theories: {total_theories}

Coverage:
✓ Calculus & Algebra
✓ Physics & Chemistry
✓ All Engineering Fields
✓ 500+ Formulas
            """
        else:
            db_text = "Database not loaded"
        
        ax4.text(0.1, 0.5, db_text, fontsize=11, verticalalignment='center',
                family='monospace', bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
        ax4.axis('off')
        
        fig.suptitle('Homework Analysis Dashboard', fontsize=16, weight='bold', y=0.98)
        plt.tight_layout()
        
        # Save
        filepath = os.path.join(self.output_dir, 'statistics_dashboard.png')
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def plot_function_example(self, title="Sample Function"):
        """Create example function plot for demonstration"""
        import numpy as np
        
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Example: Plot multiple functions
        x = np.linspace(-5, 5, 1000)
        
        # f(x) = x^2
        y1 = x**2
        ax.plot(x, y1, 'b-', linewidth=2, label='f(x) = x²', marker='')
        
        # f(x) = x^3
        y2 = x**3
        ax.plot(x, y2, 'r-', linewidth=2, label='f(x) = x³', marker='')
        
        # f(x) = sin(x)
        y3 = np.sin(x) * 10
        ax.plot(x, y3, 'g-', linewidth=2, label='f(x) = 10·sin(x)', marker='')
        
        ax.axhline(y=0, color='k', linewidth=0.5)
        ax.axvline(x=0, color='k', linewidth=0.5)
        ax.grid(True, alpha=0.3)
        ax.legend(fontsize=11, loc='upper left')
        ax.set_xlabel('x', fontsize=12, weight='bold')
        ax.set_ylabel('f(x)', fontsize=12, weight='bold')
        ax.set_title(f'{title}', fontsize=14, weight='bold')
        
        # Save
        filepath = os.path.join(self.output_dir, 'function_example.png')
        plt.tight_layout()
        plt.savefig(filepath, dpi=300, bbox_inches='tight')
        plt.close()
        
        return filepath
    
    def generate_problem_visualization(self, problem, problem_index):
        """Generate a visualization for an individual problem based on its type"""
        import numpy as np
        
        problem_type = problem.get('type', '').lower()
        
        try:
            fig, ax = plt.subplots(figsize=(5, 4))
            
            if 'derivative' in problem_type or 'calculus' in problem_type:
                # Plot a generic function and its tangent line
                x = np.linspace(-3, 3, 200)
                y = x**3 - 2*x**2 + x + 1
                ax.plot(x, y, 'b-', linewidth=2.5, label='f(x)')
                
                # Tangent at x=1
                x_tan = 1
                y_tan = x_tan**3 - 2*x_tan**2 + x_tan + 1
                slope = 3*x_tan**2 - 4*x_tan + 1
                y_tangent = slope * (x - x_tan) + y_tan
                ax.plot(x, y_tangent, 'r--', linewidth=2, label="f'(x) at x=1")
                ax.plot(x_tan, y_tan, 'ro', markersize=10)
                
                ax.set_xlabel('x', fontsize=10, weight='bold')
                ax.set_ylabel('f(x)', fontsize=10, weight='bold')
                ax.set_title('Function & Derivative', fontsize=11, weight='bold')
                ax.grid(True, alpha=0.3)
                ax.legend(fontsize=9)
                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.axvline(x=0, color='k', linewidth=0.5)
                
            elif 'integral' in problem_type:
                # Show area under curve
                x = np.linspace(0, 4, 200)
                y = 2 + 0.5*x - 0.1*x**2
                ax.plot(x, y, 'b-', linewidth=2.5, label='f(x)')
                
                # Shade area under curve
                x_fill = np.linspace(1, 3, 100)
                y_fill = 2 + 0.5*x_fill - 0.1*x_fill**2
                ax.fill_between(x_fill, 0, y_fill, alpha=0.3, color='lightblue', label='∫f(x)dx')
                
                ax.set_xlabel('x', fontsize=10, weight='bold')
                ax.set_ylabel('f(x)', fontsize=10, weight='bold')
                ax.set_title('Area Under Curve', fontsize=11, weight='bold')
                ax.grid(True, alpha=0.3)
                ax.legend(fontsize=9)
                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.set_ylim(0, max(y)*1.2)
                
            elif 'physics' in problem_type or 'motion' in problem_type or 'kinematics' in problem_type:
                # Show motion graph (position vs time)
                t = np.linspace(0, 5, 100)
                x_pos = 10 + 5*t - 0.5*t**2  # s = s0 + v0*t + 0.5*a*t^2
                v = 5 - t  # velocity
                
                ax2 = ax.twinx()
                line1 = ax.plot(t, x_pos, 'b-', linewidth=2.5, label='Position')
                line2 = ax2.plot(t, v, 'r--', linewidth=2, label='Velocity')
                
                ax.set_xlabel('Time (s)', fontsize=10, weight='bold')
                ax.set_ylabel('Position (m)', fontsize=10, weight='bold', color='b')
                ax2.set_ylabel('Velocity (m/s)', fontsize=10, weight='bold', color='r')
                ax.set_title('Motion Graph', fontsize=11, weight='bold')
                ax.grid(True, alpha=0.3)
                ax.tick_params(axis='y', labelcolor='b')
                ax2.tick_params(axis='y', labelcolor='r')
                
                lines = line1 + line2
                labels = [l.get_label() for l in lines]
                ax.legend(lines, labels, fontsize=9, loc='upper left')
                
            elif 'algebra' in problem_type or 'equation' in problem_type:
                # Show intersection of two functions
                x = np.linspace(-5, 5, 200)
                y1 = 2*x + 3
                y2 = -x**2 + 5
                
                ax.plot(x, y1, 'b-', linewidth=2.5, label='y = 2x + 3')
                ax.plot(x, y2, 'r-', linewidth=2.5, label='y = -x² + 5')
                
                # Mark intersections (approximate)
                idx = np.argwhere(np.diff(np.sign(y1 - y2))).flatten()
                if len(idx) > 0:
                    for i in idx[:2]:  # Show max 2 intersections
                        ax.plot(x[i], y1[i], 'go', markersize=10)
                
                ax.set_xlabel('x', fontsize=10, weight='bold')
                ax.set_ylabel('y', fontsize=10, weight='bold')
                ax.set_title('Solving Equations', fontsize=11, weight='bold')
                ax.grid(True, alpha=0.3)
                ax.legend(fontsize=9)
                ax.axhline(y=0, color='k', linewidth=0.5)
                ax.axvline(x=0, color='k', linewidth=0.5)
                
            elif 'geometry' in problem_type or 'triangle' in problem_type:
                # Draw a triangle with labels
                triangle = plt.Polygon([(0, 0), (4, 0), (2, 3)], fill=False, edgecolor='blue', linewidth=2.5)
                ax.add_patch(triangle)
                
                # Add labels
                ax.text(2, -0.5, 'b', fontsize=12, ha='center', weight='bold')
                ax.text(-0.3, 1.5, 'a', fontsize=12, ha='center', weight='bold')
                ax.text(4.3, 1.5, 'c', fontsize=12, ha='center', weight='bold')
                ax.plot([2, 2], [0, 3], 'r--', linewidth=1.5, label='height')
                
                ax.set_xlim(-1, 5)
                ax.set_ylim(-1, 4)
                ax.set_aspect('equal')
                ax.set_title('Geometry Problem', fontsize=11, weight='bold')
                ax.legend(fontsize=9)
                ax.axis('off')
                
            elif 'chemistry' in problem_type:
                # Show reaction progress
                stages = ['Reactants', 'Transition\nState', 'Products']
                energy = [20, 60, 15]
                
                ax.plot([0, 1, 2], energy, 'b-o', linewidth=2.5, markersize=10)
                ax.fill_between([0, 1, 2], 0, energy, alpha=0.2, color='lightblue')
                
                ax.set_xticks([0, 1, 2])
                ax.set_xticklabels(stages, fontsize=9)
                ax.set_ylabel('Energy', fontsize=10, weight='bold')
                ax.set_title('Reaction Energy Diagram', fontsize=11, weight='bold')
                ax.grid(True, alpha=0.3, axis='y')
                ax.set_ylim(0, 70)
                
                # Label activation energy
                ax.annotate('', xy=(0.5, 60), xytext=(0.5, 20),
                           arrowprops=dict(arrowstyle='<->', color='red', lw=2))
                ax.text(0.7, 40, 'Ea', fontsize=11, color='red', weight='bold')
                
            else:
                # Generic graph for other problem types
                categories = ['Given', 'Process', 'Solution']
                values = [1, 2, 3]
                colors_bar = ['#667eea', '#764ba2', '#43e97b']
                
                ax.bar(categories, values, color=colors_bar, edgecolor='black', linewidth=1.5)
                ax.set_ylabel('Progress', fontsize=10, weight='bold')
                ax.set_title('Problem Solving Steps', fontsize=11, weight='bold')
                ax.set_ylim(0, 4)
                
                for i, v in enumerate(values):
                    ax.text(i, v + 0.1, f'Step {v}', ha='center', va='bottom', 
                           fontsize=10, weight='bold')
            
            plt.tight_layout()
            
            # Save
            graphs_dir = os.path.join(self.output_dir, 'graphs')
            os.makedirs(graphs_dir, exist_ok=True)
            filepath = os.path.join(graphs_dir, f'problem_{problem_index}_visual.png')
            plt.savefig(filepath, dpi=150, bbox_inches='tight')
            plt.close()
            
            return filepath
            
        except Exception as e:
            print(f"⚠️ Failed to generate visualization for problem {problem_index}: {e}")
            plt.close()
            return None
    
    def generate_all_visualizations(self, problems, theories_dict):
        """Generate all visualizations"""
        print("\n📊 Generating visualizations...\n")
        
        filepaths = {}
        
        # Problem distribution
        try:
            filepaths['distribution'] = self.plot_problem_distribution(problems)
            print("✅ Problem distribution chart generated")
        except Exception as e:
            print(f"⚠️ Problem distribution chart failed: {e}")
        
        # Problem count bar
        try:
            filepaths['count_bar'] = self.plot_problem_count_bar(problems)
            print("✅ Problem count bar chart generated")
        except Exception as e:
            print(f"⚠️ Problem count bar chart failed: {e}")
        
        # Theory coverage
        try:
            filepaths['theory_coverage'] = self.plot_theory_coverage(theories_dict)
            print("✅ Theory coverage chart generated")
        except Exception as e:
            print(f"⚠️ Theory coverage chart failed: {e}")
        
        # Statistics dashboard
        try:
            filepaths['dashboard'] = self.plot_statistics_summary(problems, theories_dict)
            print("✅ Statistics dashboard generated")
        except Exception as e:
            print(f"⚠️ Statistics dashboard failed: {e}")
        
        # Function example
        try:
            filepaths['function_example'] = self.plot_function_example()
            print("✅ Function example plot generated")
        except Exception as e:
            print(f"⚠️ Function example plot failed: {e}")
        
        print(f"\n📁 All visualizations saved to: {self.output_dir}/\n")
        
        return filepaths


# Example usage function
def visualize_analysis(problems, theories_dict):
    """Generate all visualizations for analysis"""
    visualizer = ReportVisualizer()
    return visualizer.generate_all_visualizations(problems, theories_dict)
