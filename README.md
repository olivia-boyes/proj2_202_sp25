## 🌿 CSC 202 – Assignment 2: Linked Lists and Filtering CO₂ Emissions

### 📦 Overview

In this assignment, you’ll build a linked list of structured data rows based on real-world climate data — specifically, CO₂-equivalent emissions from around the world. You’ll practice:

- Using `@dataclass(frozen=True)` to define structured records
- Recursively building and filtering linked lists
- Reading and parsing multi-line CSV files
---

## ✅ Task 1: Define Your Linked List Structure

You will be building a custom linked list of **rows** representing individual records in the CO₂ emissions dataset.

### 🧩 Create the following:

- A `Row` class to store one line of emissions data  
- A linked list class
- 
Each row of the CSV file includes the following fields:

```plaintext
"country"
"year"
"electricity_and_heat_co2_emissions"
"electricity_and_heat_co2_emissions_per_capita"
"energy_co2_emissions"
"energy_co2_emissions_per_capita"
"total_co2_emissions_excluding_lucf"
"total_co2_emissions_excluding_lucf_per_capita"
```

You will need to convert string values into appropriate types (e.g., float or int), and use `None` for missing data (`""` in the CSV).

> You must use `@dataclass(frozen=True)` for all class definitions.

---

## ✅ Task 2: Reading the CSV File

### 🔧 Write the following function:

```python
read_csv_lines(filename: str) -> LinkedList
```

- Uses the `csv.reader` class to load rows
- Validates the header row
- Converts each row into a `Row` object
- Builds and returns a linked list of all rows (in any order is fine)

> 💡 We suggest writing a **helper function**:  
> `def parse_row(fields: list[str]) -> Row`  
> to handle data conversion.

Set the recursion limit at the top of your file:
```python
import sys
sys.setrecursionlimit(10_000)
```

---

## ✅ Task 3: Count Rows

### ✍️ Write:

```python
listlen(data: LinkedList) -> int
```

This recursively returns the number of rows in the linked list.

---

## ✅ Task 4: General Filtering

You will build a generic recursive filter that supports multiple types of queries.

### ✍️ Write:

```python
filter_rows(
    data: LinkedList,
    field_name: str,
    comparison: str,
    value: Union[str, float, int]
) -> LinkedList
```

- `field_name`: one of the CSV column names
- `comparison`: `"less_than"`, `"greater_than"`, or `"equal"`
- `value`: the value to compare against

### ⚠️ Rules:
- Only `"equal"` is allowed for the `"country"` field
- All numeric fields support `"less_than"` and `"greater_than"`
- Missing data (i.e., `None`) should be skipped



## 🧪 Task 6: Tests and Design Recipe

For each function:
- Write a **purpose statement**
- Include **type hints**
- Create **tests** using `unittest` in a file called `test_student.py`

You should define your own small CSV file with 5–10 rows for testing.  
Missing values (`""`) should be handled using `None`.

---

## 🔧 Setup and Restrictions

Your file should include the following at the top:

```python
import sys
import csv
from typing import *
from dataclasses import dataclass
import unittest
import math

sys.setrecursionlimit(10_000)
```

Do **not** import any other libraries. Your submission must be compatible with **Python 3.12.3**.

---

## 📤 Handin Instructions

Push the following files to your GitHub Classroom repo:

- `proj2.py` – your main implementation
- `test_student.py` – your test suite
- `sample.csv` – a small file for testing (optional but recommended)
