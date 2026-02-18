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
