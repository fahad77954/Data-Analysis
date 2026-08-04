# 📊 Data Analysis & Scientific Computing with Python
### NumPy & Pandas Foundations | Hands-On Data Science Portfolio

![Language](https://img.shields.io/badge/Language-Python_3.x-3776AB?style=for-the-badge&logo=python)
![Library](https://img.shields.io/badge/Library-NumPy-013243?style=for-the-badge&logo=numpy)
![Library](https://img.shields.io/badge/Library-Pandas-150458?style=for-the-badge&logo=pandas)
![IDE](https://img.shields.io/badge/Environment-Jupyter-F37626?style=for-the-badge&logo=jupyter)

Welcome to my **Data Analysis & Scientific Computing** repository! This space tracks my hands-on learning journey mastering low-level matrix mathematics, vectorized array processing, and real-world 2D data wrangling using Python's foundational data science stack: **NumPy** and **Pandas**.

---

## 📌 Technical Scope & Core Concepts

Moving from standard Python logic to high-performance scientific computing requires transitioning away from slow `for` loops toward hardware-optimized computational mechanics.

### Key Architectural Concepts Mastered:
* **Memory Efficiency & Vectorization**: Utilizing NumPy’s contiguous C-array memory layouts to compute element-wise math across multi-dimensional arrays without standard Python loop overhead.
* **Axis Operations & Aggregations**: Manipulating multi-dimensional matrices along vertical ($\text{axis}=0$) and horizontal ($\text{axis}=1$) directions for row and column statistics.
* **1D Labeled Mechanics (Pandas Series)**: Mastered index-label alignment, explicit positional (`.iloc`) vs. label-based (`.loc`) data extraction, and handling type coercion ($int64 \rightarrow float64$) when missing values ($NaN$) are present.
* **2D Tabular Data Wrangling (Pandas DataFrames)**: Building $N \times M$ datasets, broadcasting arithmetic across columns, performing multi-condition boolean filtering using bitwise logic (`&`, `|`), updating schemas dynamically, and importing external CSV records.

---

## 📚 Curriculum & Learning Module Index

| Module | Core Topic | Primary Tech | Key Concepts & Solutions |
| :--- | :--- | :---: | :--- |
| **01** | **NumPy Foundations** | NumPy | Memory blocks, array creation (`arange`, `linspace`), shape manipulation (`ndim`, `shape`), broadcasting, axis statistics, dot/cross products. |
| **02** | **Pandas Series Mechanics** | Pandas | 1D labeled arrays, explicit `.loc` vs positional `.iloc` indexing, index alignment, `.str` vectorized accessors, missing data handling. |
| **03** | **Pandas DataFrame Mastery** | Pandas, CSV | 2D matrix selection, multi-condition boolean filtering, calculated revenue metrics, schema updates (`.rename()`), row appending, CSV ingestion. |

---

## 💡 Key Module & Project Highlights

### ⚡ `01_numpy_foundations.ipynb` — Array Vectorization & Linear Algebra
* **Objective:** Replace manual loop structures with C-optimized vectorized operations and compute linear algebra calculations across N-dimensional space.
* **Technical Implementation:** Utilized `np.arange()`, `np.linspace()`, and random distributions. Managed 2D matrix shape transformations (`shape`, `ndim`), applied axis aggregations (`axis=0` down columns, `axis=1` across rows), applied dynamic scalar broadcasting, and performed matrix dot products (`np.dot`).

### 🛠️ `02_pandas_series.ipynb` — 1D Labeled Mechanics & Index Alignment
* **Objective:** Understand how Pandas binds data values to flexible index labels and handles missing dataset entries reliably.
* **Technical Implementation:** Built indexed Series from Python dictionaries, demonstrated label alignment during arithmetic, extracted targeted values via `.loc[]` and `.iloc[]`, applied vectorized string cleanups using `.str`, and filled $NaN$ missing entries using `.fillna()`.

### 📈 `03_pandas_dataframe.ipynb` — 2D Data Wrangling & Schema Management
* **Objective:** Manipulate realistic product inventory tables, dynamically alter schema metadata, and calculate revenue metrics.
* **Technical Implementation:** Created multi-column inventory DataFrames, created custom indexing (`Product IDs`), filtered records using bitwise boolean masks (`(stock_qty < 50) | (unit_price >= 100)`), performed vector series adjustments (`price_adj`), updated schema column names (`.rename()`), appended new record Series, and ingested external dataset files.

---

## 🧠 Detailed Breakdown of Mastered Topics

### 1. NumPy Foundations & Matrix Math
* **Array Generation**: Sequences (`np.arange`), linear spaces (`np.linspace`), template matrices (`zeros`, `ones`, `empty`), and statistical random distributions (`np.random`).
* **Attributes & Reshaping**: Dimension counts (`ndim`), tuple geometries (`shape`), and total element volume (`size`).
* **Axes Aggregations**: Horizontal ($\text{axis}=1$) vs. Vertical ($\text{axis}=0$) statistical reductions (`sum`, `mean`, `std`, `var`).
* **Boolean Masking**: Fast vector slicing using logical statement arrays (e.g., `a[a > 50]`).
* **Linear Algebra**: Matrix transpositions (`.T`), matrix products (`np.dot`), and vector cross products (`np.cross`).

### 2. Pandas Series Mechanics (1D Labeled Data)
* **Index Alignment**: Arithmetic operates strictly by matching index label names; missing matches automatically populate $NaN$.
* **Explicit Selection**: Position-based extraction via `.iloc[]` (0-based integer offset, exclusive) vs. label-based `.loc[]` (label matching, inclusive).
* **Vectorized Accessors (`.str`)**: Broadcasting standard Python string operations across full data series.
* **Missing Data Management**: Handling $NaN$ entries using `.fillna()`, cumulative math (`.cumsum()`), and dictionary value substitution (`.map()`).

### 3. Pandas DataFrame Mastery (2D Tabular Data)
* **Creation & Structural Metadata**: Constructing tables from dictionary collections, setting custom indices (`.set_index()`), inspecting schemas (`.info()`, `.describe()`).
* **Matrix Selection & Slicing**: Multi-axis extraction using `df.loc[rows, cols]` and `df.iloc[row_idx, col_idx]`.
* **Data Mutation & Column Metrics**: Calculating derived columns (e.g., `monthly_revenue = unit_price * monthly_sales`) and broadcasting scalar updates.
* **Schema Updates & Row Insertion**: Renaming columns and index keys safely via `.rename()`, and inserting new record entries using `.loc['NEW_ID']`.
* **CSV Ingestion**: Importing flat files using `pd.read_csv()`, configuring index columns, and setting header parameters.

---

## 📁 Repository Organization

```text
data-analysis/
├── 01_numpy_foundations.ipynb
├── 02_pandas_series.ipynb
├── 03_pandas_dataframe.ipynb
└── README.md
