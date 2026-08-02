# Data Analysis & Scientific Computing 📊

Welcome to my Data Analysis repository! This space tracks my hands-on learning journey in Python data science—from core matrix math to real-world data wrangling.

---

## 🧠 Why NumPy?
Before moving to high-level data frames, mastering **NumPy** is critical:
* **Memory Efficiency:** NumPy arrays store data in contiguous RAM memory blocks, using far less memory than standard Python lists.
* **Speed & Vectorization:** Math operations run on optimized C code underneath, eliminating the need for slow Python `for` loops.

---

## 📚 Topics & Concepts Mastered

### 1. Array Creation & Utility Functions
* Generating structured sequences using `np.arange()` and evenly spaced points with `np.linspace()`.
* Allocating blank templates using `np.zeros()`, `np.ones()`, and high-performance RAM allocation with `np.empty()`.
* Generating random statistical distributions using `np.random` (Normal/Bell-curve, `randint`, and floating points).

### 2. Array Attributes & Structural Consistency
* **`ndim`**: Inspecting array dimensions (1D, 2D, 3D).
* **`shape`**: Extracting precise row/column structures (e.g., `(3, 2)`).
* **`size`**: Calculating total element counts.
* **Structural Integrity**: Understanding why row/column consistency is required across multi-dimensional arrays.

### 3. Indexing, Slicing & Mutation
* 1D and multi-dimensional coordinate slicing.
* Advanced multi-indexing for specific grid values (e.g., `a[[0, 2], [0, 2]]`).
* Direct element mutation (e.g., reassigning values via `a[2] = 99`).

### 4. Matrix Axes & Statistical Operations
* Computing essential statistical metrics: `sum()`, `mean()`, Standard Deviation (`std()`), and Variance (`var()`).
* **Axis Operations**:
  * **`axis=0`**: Operations running **vertically** down columns.
  * **`axis=1`**: Operations running **horizontally** across rows.

### 5. Broadcasting & Vectorized Math
* Performing automatic arithmetic across arrays of different compatible shapes.
* Eliminating explicit loops for fast, clean, element-wise array calculations.

### 6. Boolean Masking & Data Filtering
* Filtering array values using conditional logical queries (e.g., `a[a > 50]`).
* Combining multiple filtering rules using bitwise operators (`&` AND, `|` OR).

### 7. Linear Algebra Fundamentals
* Matrix Transpose (`.T`) for swapping dimensions.
* Matrix multiplication via Dot product (`np.dot()`) and Cross product (`np.cross()`).

---

## 📁 Repository Contents
* `test.ipynb`: Interactive Jupyter Notebook containing all NumPy code implementations, matrix manipulations, and statistical tests.

---

## 🚀 Learning Roadmap
- [x] **NumPy Foundations** (Memory, Arrays, Math, Linear Algebra)
- [ ] **Pandas** (Data Cleaning, Series, DataFrames, Merging)
- [ ] **Data Visualization** (Matplotlib & Seaborn)
