# 📊 Graph Visualization Quick Reference Card

## 🚀 Quick Commands

```bash
# Generate graphs from PDF (Command Line)
python src/homework_solver.py "homework.pdf"

# Launch desktop GUI with graphs
python gui_app_graphs.py

# Launch web app with graphs  
python web_app_graphs.py
# Then visit: http://localhost:5000

# Test graph generation
python test_graphs.py
```

---

## 📈 5 Graphs at a Glance

| # | Graph | Type | Shows | File |
|---|-------|------|-------|------|
| 1️⃣ | **Distribution** | Pie | Problem type percentages | `problem_distribution.png` |
| 2️⃣ | **Count** | Bar | Problems per type | `problem_count_bar.png` |
| 3️⃣ | **Coverage** | H-Bar | Theories per domain | `theory_coverage.png` |
| 4️⃣ | **Dashboard** | Multi | Complete analysis | `statistics_dashboard.png` |
| 5️⃣ | **Functions** | Line | Example plots | `function_example.png` |

---

## 🎨 Deployment Comparison

| Aspect | **CLI** | **GUI** | **Web** |
|--------|--------|--------|--------|
| **Launch** | `python src/homework_solver.py` | `python gui_app_graphs.py` | `python web_app_graphs.py` |
| **Access** | Terminal | Desktop window | Browser (http://localhost:5000) |
| **Graphs** | Auto-saved | Tabbed display | Embedded in page |
| **Users** | Single | Single | Multi (local team) |
| **Files** | Terminal output + PNG | GUI window | Web page |
| **Best for** | Batch jobs | Interactive work | Sharing |
| **Difficulty** | ⭐ Easy | ⭐⭐ Medium | ⭐⭐ Medium |

---

## 💾 Output Files Location

```
d:\homework.ai.py\
├── reports\
│   ├── problem_distribution.png      ← Pie chart
│   ├── problem_count_bar.png         ← Bar chart
│   ├── theory_coverage.png           ← Coverage chart
│   ├── statistics_dashboard.png      ← Dashboard
│   ├── function_example.png          ← Function plot
│   ├── uploads\                      ← Uploaded PDFs (web app)
│   └── homework_analysis_report.txt  ← Text report
└── src\visualizer.py                 ← Graph generation code
```

---

## 🔧 Customization

### Change Graph Colors
Edit `src/visualizer.py` line 18:
```python
self.colors = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#00f2fe', ...]
```

### Custom Output Directory
```python
visualizer = ReportVisualizer(output_dir="my_custom_path")
```

### Adjust Resolution
Edit `src/visualizer.py` (search for `dpi=300`):
```python
# Lower DPI for faster processing
plt.savefig(filepath, dpi=100)  # Fast
# Higher DPI for printing
plt.savefig(filepath, dpi=600)  # High quality
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Modules not found | `python -m pip install matplotlib Pillow` |
| Graphs not displaying | Check `reports/` directory exists |
| GUI shows blank tabs | Make sure `Pillow` is installed |
| Web app won't start | Port 5000 in use - modify `web_app_graphs.py` line 100 |
| Emoji warnings | Harmless - graphs still generate correctly |

---

## 📊 Graph Specifications

| Spec | Value |
|------|-------|
| **Format** | PNG (lossless) |
| **Resolution** | 300 DPI (publication quality) |
| **Colors** | RGB (16.7M colors) |
| **Typical Size** | 100-350 KB per graph |
| **Generation Time** | ~1-2 seconds per graph set |

---

## 🎯 Use Cases

### Student Use
```bash
python src/homework_solver.py homework.pdf
# Check graphs in reports/ folder
```

### Teacher/Grader
```bash
python gui_app_graphs.py
# Process all student submissions with visual feedback
```

### Batch Processing
```bash
# Process multiple PDFs
Get-ChildItem *.pdf | ForEach-Object {
    python src/homework_solver.py $_.Name
}
```

---

## 📱 Feature Matrix

```
CLI App
├─ ✅ Graph generation
├─ ✅ Console output
├─ ✅ File saving
├─ ❌ GUI
└─ ❌ Web interface

Desktop GUI
├─ ✅ Graph generation
├─ ✅ File browser
├─ ✅ Tabbed display
├─ ✅ Interactive
└─ ❌ Network access

Web App
├─ ✅ Graph generation
├─ ✅ File upload
├─ ✅ Web interface
├─ ✅ Team access
└─ ✅ Mobile friendly
```

---

## 🚀 Performance Tips

1. **Fast Processing**: Use CLI for batch jobs
2. **Interactive Work**: Use GUI for one-at-a-time analysis
3. **Team Sharing**: Use Web app for accessibility
4. **Large PDFs**: Consider using lower DPI (100 vs 300)
5. **Multiple Graphs**: All 5 generate together (don't cherry-pick)

---

## 📚 File Extensions

- **Graphs**: `.png` (recommended) or convert to `.jpg`, `.webp`
- **Reports**: `.txt` (plain text) or embed graphs in `.md`
- **PDFs**: `.pdf` (input only)

---

## ⚙️ Dependencies (All Installed ✅)

```
✅ matplotlib 3.10.8  - Graph generation
✅ Pillow 12.1.1      - Image handling
✅ pdfplumber 0.11.x  - PDF processing
✅ Flask 2.0+         - Web app (web only)
```

---

## 🎓 Learn More

📖 **Full Documentation**: See `GRAPHS_GUIDE.md`  
📊 **Summary**: See `GRAPHS_SUMMARY.md`  
🧪 **Test Code**: See `test_graphs.py`  
💻 **GUI Code**: See `gui_app_graphs.py`  
🌐 **Web Code**: See `web_app_graphs.py`  
🎨 **Viz Code**: See `src/visualizer.py`  

---

## ✨ What's Included

✅ 5 professional graph types  
✅ 3 deployment options (CLI, GUI, Web)  
✅ 300 DPI publication-quality output  
✅ Full customization support  
✅ Batch processing capability  
✅ Real-time analysis  
✅ Team sharing ready  

---

## 🎉 Ready to Use!

All components are tested and verified working.

**Pick your interface and get started:**
- ⚡ **Fast**: `python src/homework_solver.py homework.pdf`
- 🖥️ **Friendly**: `python gui_app_graphs.py`
- 🌐 **Shareable**: `python web_app_graphs.py`

**Happy analyzing! 📊📚**
