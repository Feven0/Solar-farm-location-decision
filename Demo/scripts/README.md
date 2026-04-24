# Project Scripts

This directory contains utility scripts for data processing and analysis.

## Overview
- `__init__.py`: Makes the directory a Python package.
- `README.md`: Documentation for scripts within this folder.

## Key Functions
The dashboard in the `app/` folder uses these scripts (integrated into `utils.py`) to:
1. **Load Data**: Dynamically fetch cleaned solar datasets for Benin, Sierra Leone, and Togo.
2. **Process Metrics**: Calculate daily averages and summary statistics (Mean, Median, Std).
3. **Statistical Analysis**: Perform One-way ANOVA to determine regional solar variability.
4. **Ranking**: Rank territories by their solar potential (GHI, DNI, DHI).

## Usage
Most functions are imported directly by `app/main.py`. If you wish to run analysis separately, you can import from `utils`.
