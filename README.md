Data Analysis & Scientific Computing 📊

Welcome to my Data Analysis repository! This space tracks my hands-on learning journey in Python data science—from core matrix math to real-world 2D data wrangling.

🧠 Why NumPy & Pandas?

NumPy (Matrix Math & Vectorization): Operates on contiguous RAM memory blocks with C-optimized performance, eliminating slow Python for loops.

Pandas (Data Wrangling & Manipulation): Built on top of NumPy, Pandas introduces labeled 1D (Series) and 2D (DataFrame) structures designed for realistic, tabular data analysis, index alignment, and automated dataset handling.

📚 Topics & Concepts Mastered

1. NumPy Foundations & Linear Algebra

Array Creation & Utilities: Sequences (np.arange), linear spaces (np.linspace), blank templates (np.zeros, np.ones, np.empty), and random distributions (np.random).

Array Attributes: Dimension inspection (ndim), shape tuples (shape), and total cell counts (size).

Indexing, Slicing & Mutation: 1D/2D grid coordinate selection, multi-indexing, and in-place element reassignment.

Axes & Statistics: Aggregations (sum, mean, std, var) operating along vertical (axis=0) and horizontal (axis=1) directions.

Broadcasting & Boolean Masks: Vectorized math across compatible shapes and array filtering with bitwise operators (&, |).

Linear Algebra: Matrix transposes (.T), dot products (np.dot), and cross products (np.cross).

2. Pandas Series Mechanics (1D Labeled Data)

Series Architecture: Understanding 1D data bound to explicit index labels and Series names.

Positional vs. Label Selection:

.iloc[]: 0-based positional selection (exclusive stop index).

.loc[]: Label-based selection (inclusive stop index).

Automatic Index Alignment: Operations align strictly by label name, automatically inserting NaN when keys mismatch.

Type Coercion: Automatic promotion of integer types (int64) to float types (float64) when missing data (NaN) is introduced.

Vectorized Accessors (.str): Applying broadcasted string methods across entire Series without explicit loops.

Missing Data & Mapping: Handling NaN values with .fillna(), .cumsum(), and dict-based replacements using .map().

3. Pandas DataFrame Mastery (2D Tabular Data)

Creation & Inspection: Constructing DataFrames from Python dictionaries, setting custom primary indices (.set_index()), inspecting meta-summary (.info()), statistical properties (.describe()), and structural dimensions (.shape).

2D Matrix Slicing: Multi-row and multi-column slicing using .loc[rows, cols] and .iloc[row_idx, col_idx].

Boolean Filtering & Masking: Multi-condition filtering using bitwise logic (&, |) combined with .loc column extraction.

Calculated Columns & Mutation: Deriving new columns via vectorized math, scalar broadcasting, and dropping columns (axis=1) or rows (axis=0).

Series-to-DataFrame Alignment: Adding/subtracting row-aligned or column-aligned Series to 2D DataFrames.

Renaming & Row Insertion: Updating column names/indices safely with .rename(), and appending custom labeled rows via .loc['NEW_LABEL'].

CSV Data Ingestion & Parsing: Fast file ingestion using pd.read_csv() with optimized index assignment (index_col) and date parsing (parse_dates=True).

📁 Repository Contents

01_numpy_foundations.ipynb — Interactive notebook covering NumPy matrix operations, array creation, broadcasting, and linear algebra.

02_pandas_series.ipynb — Practice scripts and notebooks covering Pandas Series mechanics, index alignment, and vector methods.

03_pandas_dataframe.ipynb — E-commerce data analysis challenge featuring 2D tabular selection, calculated revenue metrics, alignment, and row/column mutations.

🚀 Learning Roadmap

[x] Python Programming Foundations (Functions, Loops, Logic)

[x] NumPy Foundations (Memory, Arrays, Math, Linear Algebra)

[x] Pandas Series & Mechanics (Labels, Vectorized String Accessors, Missing Data)

[x] Pandas DataFrames & Wrangling (2D Tables, Selection, Alignment, CSV Ingestion)

[ ] Data Cleaning & Aggregations (Handling Duplicates, .groupby(), Merging & Joining)

[ ] Data Visualization (Matplotlib & Seaborn)
