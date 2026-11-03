# Lab 6 – Code and Branch Coverage Analysis

## Project Overview
This lab focuses on measuring and analysing code coverage and branch coverage using Python's Coverage.py and Pytest tools. The application used for testing is **Photo Print Order**.

## Objectives
- Understand code coverage and branch coverage.
- Measure the execution of application code using coverage tools.
- Identify untested statements and decision branches.
- Write additional test cases to achieve at least 90% coverage.

## Technologies Used
- Python 3
- Pytest
- Coverage.py

## Project Files

| File | Description |
|---|---|
| `photo_print_order.py` | Main application code |
| `test_photo_print_order.py` | Original test cases |
| `CodeCoverageTest_46_photo_print_order.py` | Additional test cases for code coverage |
| `BranchCoverageTest_46_photo_print_order.py` | Test cases for branch coverage |
| `Code_Coverage_Result.png` | Code coverage terminal screenshot |
| `Branch_Coverage_Result.png` | Branch coverage terminal screenshot |

## Execution Commands

### 1. Install Dependencies

```bash
pip install coverage pytest
```

### 2. Run Original Test Cases

```bash
python -m coverage run -m pytest test_photo_print_order.py
```

### 3. Code Coverage

```bash
python -m coverage erase
python -m coverage run -m pytest CodeCoverageTest_46_photo_print_order.py
python -m coverage report -m
```

### 4. Branch Coverage

```bash
python -m coverage erase
python -m coverage run --branch -m pytest BranchCoverageTest_46_photo_print_order.py
python -m coverage report -m
```

## Results

| Coverage Type | Achieved Coverage |
|---|---:|
| Code Coverage | 100% |
| Branch Coverage | 100% |

All 24 branch coverage test cases passed successfully. No application statements or branches were missed.

## Conclusion

The lab successfully demonstrates code coverage and branch coverage analysis using Python, Pytest and Coverage.py. Additional test cases were written to cover application statements and decision branches, achieving 100% code coverage and 100% branch coverage.