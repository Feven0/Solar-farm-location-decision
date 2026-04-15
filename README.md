# Solar Data Discovery: Week 0 — MoonLight Energy Solutions

## Overview
Analysis of solar farm data from **Benin**, **Sierra Leone**, and **Togo** to identify high-potential regions for solar installation.

## Project Structure

```
week0/
├── .github/workflows/ci-cd.yml   # CI/CD pipeline (GitHub Actions)
├── notebooks/                    # Jupyter notebooks for EDA per country
├── src/                          # Source modules (reusable code)
├── scripts/                      # Standalone processing scripts
├── tests/                        # Automated test suite (pytest)
├── app/                          # Streamlit dashboard (bonus task)
├── data/                         # Local data files (NOT committed to Git)
├── dashboard_screenshots/        # Screenshots of the deployed dashboard
├── requirements.txt              # Production dependencies
├── requirements-dev.txt          # Development & testing dependencies
├── config.py                     # Environment configuration
├── pytest.ini                    # Pytest configuration
└── .gitignore                    # Files to exclude from Git
```

## Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/week0.git
   cd week0
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # Windows
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements-dev.txt
   ```

4. **Run the tests**
   ```bash
   pytest
   ```

## Tasks

| Task | Branch | Deliverable |
|---|---|---|
| Task 1: Git & Environment Setup | `main` | This repo |
| Task 2: EDA (Benin) | `eda-benin` | `notebooks/benin_eda.ipynb` |
| Task 2: EDA (Sierra Leone) | `eda-sierra-leone` | `notebooks/sierra_leone_eda.ipynb` |
| Task 2: EDA (Togo) | `eda-togo` | `notebooks/togo_eda.ipynb` |
| Task 3: Cross-Country Comparison | `compare-countries` | `notebooks/compare_countries.ipynb` |
| Bonus: Streamlit Dashboard | `dashboard-dev` | `app/main.py` |

## CI/CD Pipeline

Automated pipeline runs on every push via **GitHub Actions**:
- ✅ Installs dependencies
- ✅ Runs flake8 linter
- ✅ Runs pytest suite
