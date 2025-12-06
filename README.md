# Mini Data Analysis Project

A Python-based mini data analysis project demonstrating data loading, grouping, summarizing, and visualization using pandas and matplotlib. This project simulates a real-world exploratory data analysis workflow, perfect for showcasing data science skills.

## 🚀 Features

- **CSV Data Loading**: Load and validate CSV datasets with error handling
- **Data Exploration**: Examine data structure, types, statistics, and missing values
- **Grouping & Aggregation**: Group data by categories and compute statistical summaries (count, sum, mean, min, max)
- **Data Visualization**: Generate professional bar charts with matplotlib
- **Export Functionality**: Save visualizations as high-quality PNG files
- **Modular Code**: Clean, well-documented functions for each analysis step
- **Beginner-Friendly**: Easy to understand and extend for more complex analyses

## 🛠️ Tech Stack

- **Python 3.7+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization and plotting
- **NumPy**: Numerical computing (dependency of pandas)

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🔧 Installation & Setup

1. **Clone or download the project:**
   ```bash
   git clone https://github.com/yourusername/mini-data-analysis.git
   cd mini-data-analysis
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the analysis:**
   ```bash
   python main.py
   ```

## 📖 Usage

The script performs a complete data analysis workflow:

1. **Data Loading**: Reads `sample_data.csv` (or modify for your own CSV)
2. **Exploration**: Displays basic statistics and data overview
3. **Grouping**: Aggregates data by category with multiple metrics
4. **Visualization**: Creates and saves a bar chart

### Sample Output

```
🚀 MINI DATA ANALYSIS PROJECT
========================================
✅ Data loaded successfully from sample_data.csv
   Shape: 17 rows, 2 columns
   Columns: ['category', 'value']

📊 DATA EXPLORATION
==================================================

First 5 rows:
  category  value
0        A     10
1        A     15
2        A     12
3        B     20
4        B     18

Summary statistics:
           value
count  17.000000
mean   16.058824
std     8.257350
min     5.000000
max    30.000000

📈 GROUPING AND SUMMARIZATION (category -> value)
======================================================================
Summary by group:
          count  sum       mean  min  max
category
A             3   37  12.333333   10   15
B             4   79  19.750000   18   22
C             3   29   9.666667    8   12
D             4  110  27.500000   25   30
E             3   18   6.000000    5    7

📊 CREATING VISUALIZATION
==============================
✅ Chart saved as 'analysis_chart.png'

🎉 ANALYSIS COMPLETE!
```

## 📁 Project Structure

```
mini-data-analysis/
│
├── main.py                 # Main analysis script
├── sample_data.csv         # Sample dataset
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
└── analysis_chart.png     # Generated visualization (after running)
```

## 🎯 Key Functions

- `load_data()`: Loads CSV with error handling
- `explore_data()`: Performs basic data exploration
- `group_and_summarize()`: Groups data and computes aggregations
- `create_visualization()`: Generates and saves bar chart
- `main()`: Orchestrates the complete analysis workflow

## 🔍 Code Highlights

- **Error Handling**: Robust file loading with informative error messages
- **Modular Design**: Each analysis step in separate, reusable functions
- **Professional Visualization**: Styled charts with labels and proper formatting
- **Clean Output**: Well-formatted console output for easy reading
- **Extensible**: Easy to modify for different datasets and analysis types

## 🚀 Customization

### Using Your Own Data

1. Replace `sample_data.csv` with your CSV file
2. Update the `data_file` variable in `main.py`
3. Modify `group_col` and `value_col` variables for your column names

### Adding More Analysis

Extend the script by adding functions for:
- Additional visualizations (line plots, scatter plots)
- Statistical tests (t-tests, ANOVA)
- Data cleaning and preprocessing
- Export to different formats (Excel, JSON)

## 📊 Sample Data Format

The included `sample_data.csv` has this structure:

```csv
category,value
A,10
A,15
A,12
B,20
B,18
...
```

## 📄 License

This project is open source and available under the [MIT License](LICENSE).


*This project demonstrates fundamental data analysis skills using Python's most popular data science libraries. Perfect for portfolios and learning data manipulation techniques!*

## 🏷️ Tags

`python` `pandas` `matplotlib` `data-analysis` `visualization` `csv` `data-science` `beginner-friendly`
