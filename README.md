# 📊 Data Analysis & Scientific Computing with Python
### NumPy & Pandas Foundations | Hands-On Data Science Portfolio

![Language](https://img.shields.io/badge/Language-Python_3.x-3776AB?style=for-the-badge&logo=python)
![Library](https://img.shields.io/badge/Library-NumPy-013243?style=for-the-badge&logo=numpy)
![Library](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas)
![Library](https://img.shields.io/badge/Library-Matplotlib-11557c?style=for-the-badge&logo=python)
![Library](https://img.shields.io/badge/Library-Seaborn-4C72B0?style=for-the-badge&logo=python)
![IDE](https://img.shields.io/badge/Environment-Jupyter-F37626?style=for-the-badge&logo=jupyter)

Welcome to my **Data Analysis & Scientific Computing** repository! This space tracks my hands-on learning journey—culminating in the completion of five comprehensive data projects—mastering low-level matrix mathematics, real-world data wrangling, and statistical visual storytelling using Python's foundational data science stack.

---

## 📌 Technical Scope & Core Concepts

Moving from standard Python logic to high-performance scientific computing requires transitioning away from slow `for` loops toward hardware-optimized computational mechanics, and learning to interpret raw numbers through visual geometry.

### Key Architectural Concepts Mastered:
* **Memory Efficiency & Vectorization**: Utilizing NumPy’s contiguous C-array memory layouts to compute element-wise math across multi-dimensional arrays without standard Python loop overhead.
* **Axis Operations & Aggregations**: Manipulating multi-dimensional matrices along vertical (axis=0) and horizontal (axis=1) directions for row and column statistics.
* **1D Labeled Mechanics (Pandas Series)**: Mastered index-label alignment, explicit positional (`.iloc`) vs. label-based (`.loc`) data extraction, and handling type coercion (int64 -> float64) when missing values (NaN) are present.
* **2D Tabular Data Wrangling (Pandas DataFrames)**: Building N x M datasets, broadcasting arithmetic across columns, performing multi-condition boolean filtering using bitwise logic (`&`, `|`), updating schemas dynamically, and importing external CSV records.
* **Data Integrity & Pipeline Cleaning**: Designing scripts to audit raw datasets, resolve NaN conflicts safely without losing statistical weight, and standardize categorical string inputs.
* **Visual Data Storytelling**: Translating complex tabular aggregations into readable geometric formats (distributions, categorical comparisons, and multi-variable correlation grids) using Matplotlib and Seaborn.

---

## 📚 Curriculum & Learning Module Index

| Module | Core Topic | Primary Tech | Key Concepts & Solutions |
| :--- | :--- | :---: | :--- |
| **01** | **NumPy Foundations** | NumPy | Memory blocks, array creation, shape manipulation, broadcasting, axis statistics. |
| **02** | **Pandas Series Mechanics** | Pandas | 1D arrays, `.loc` vs `.iloc`, index alignment, vectorized string accessors. |
| **03** | **Pandas DataFrame Mastery** | Pandas | 2D matrix selection, boolean filtering, calculated metrics, CSV ingestion. |
| **04** | **Data Cleaning Strategies** | Pandas | Missing value imputation (`.fillna()`), dropping nulls (`.dropna()`), deduplication. |
| **05** | **Aggregation & Grouping** | Pandas | Cross-sectional data rollups (`.groupby()`), pivot tables, and dataset merging. |
| **06** | **Statistical Visualization** | Seaborn, Matplotlib | Figure canvases, KDE histograms, violin plots, scatter trends, and correlation heatmaps. |

---

## 💡 Key Module & Project Highlights

### ⚡ `01_numpy_foundations.ipynb` — Array Vectorization & Linear Algebra
* **Objective:** Replace manual loop structures with C-optimized vectorized operations.
* **Technical Implementation:** Utilized `np.arange()` and `np.linspace()`. Managed 2D matrix shape transformations, applied axis aggregations, and applied dynamic scalar broadcasting.

### 🛠️ `02_pandas_series.ipynb` — 1D Labeled Mechanics & Index Alignment
* **Objective:** Understand how Pandas binds data values to flexible index labels.
* **Technical Implementation:** Built indexed Series from Python dictionaries, demonstrated label alignment during arithmetic, extracted targeted values via `.loc[]`, and applied vectorized string cleanups.

### 📈 `03_pandas_dataframe.ipynb` & `clean.py` — 2D Data Wrangling & Cleaning
* **Objective:** Manipulate realistic inventory and student tables, alter schema metadata, and enforce data integrity.
* **Technical Implementation:** Created custom indexing, filtered records using bitwise boolean masks, performed vector adjustments, and executed rigorous data cleaning pipelines to sanitize messy raw inputs into a reliable `cleaned_student_data.csv` file.

### 🎨 `analysis.py` — Analytical Grouping & Visual Storytelling
* **Objective:** Group cleaned data for statistical insights and render complex metrics into accessible visual formats.
* **Technical Implementation:** Configured Matplotlib figure canvases and plotted Seaborn geometries. Built `sns.histplot` for study hour distributions, `sns.violinplot` to measure volume and spread across grade categories, and generated dynamic correlation matrices using `sns.heatmap` to identify hidden variable relationships.

---

## 🧠 Detailed Breakdown of Mastered Topics

### 1. NumPy & DataFrames (The Mathematical Engine)
* **Axes Aggregations**: Horizontal (axis=1) vs. Vertical (axis=0) statistical reductions.
* **Boolean Masking**: Fast vector slicing using logical statement arrays.
* **Index Alignment**: Arithmetic operates strictly by matching index label names.
* **Matrix Selection**: Multi-axis extraction using `df.loc[rows, cols]` and `df.iloc[row_idx, col_idx]`.

### 2. Data Cleaning & Missing Value Strategies
* **Sanitization**: Identifying corrupted or missing data points (`.isna()`, `.isnull()`).
* **Imputation vs. Deletion**: Strategically applying `.fillna()` to preserve row weight versus `.dropna()` for irreparable records.
* **Deduplication**: Removing redundant matrix rows via `.drop_duplicates()` to prevent skewed statistical aggregations.

### 3. Data Aggregation & Relational Merging
* **Grouping (`.groupby()`)**: Splitting continuous data by categorical keys, applying mathematical functions (mean, sum, count), and combining results.
* **Pivot Tables**: Reshaping 2D structures to view multi-dimensional summaries.
* **Dataset Joins**: Combining separated CSV tables using inner/outer merge logic based on shared primary keys (e.g., `student_id`).

### 4. Data Visualization 
* **Canvas Management**: Controlling Matplotlib figure sizes (`figsize`), rotating axis labels (`plt.xticks`), and optimizing layout margins (`plt.tight_layout()`).
* **Distributions & Counts**: Utilizing `sns.histplot` with Kernel Density Estimates (KDE) and `sns.countplot` for categorical volume.
* **Categorical Spreads**: Deploying `sns.violinplot` to view both statistical ranges and density volume simultaneously.
* **Correlation Mapping**: Calculating numeric matrix correlations (`.corr()`) and projecting them into color-coded `sns.heatmap` grids.

---

## 📁 Repository Organization

```text
Data-Analysis/
├── 01_numpy_foundations.ipynb
├── 02_pandas_series.ipynb
├── 03_pandas_dataframe.ipynb
├── 04_pandas_Data_Cleaning.ipynb
├── analysis.py
├── clean.py
├── student_audit.py
├── messy_student_data.csv
├── cleaned_student_data.csv

## 🚀 Learning Roadmap

[x] Python Foundations (CS50P: Functions, Loops, Logic, Exception Handling, File I/O)

[x] NumPy Foundations (Contiguous Memory, N-Dim Arrays, Vectorization, Linear Algebra)

[x] Pandas Series & DataFrames (Index Alignment, Wrangling, Boolean Slicing, Mutations)

[x] Data Cleaning & Missing Value Strategies (.fillna(), .dropna(), deduplication)

[x] Data Aggregation & Grouping (groupby(), .pivot_table(), merging datasets)

[x] Data Visualization (Matplotlib & Seaborn charting)








└── README.md
