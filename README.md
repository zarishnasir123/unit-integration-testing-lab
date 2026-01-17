# Unit and Integration Testing Lab

## Lab Title
**Lab-09: Unit Testing and Integration Testing with PyTest and GitHub Actions**

## Student Information
- **Student Name:** (Enter Your Name)
- **Roll Number:** (Enter Your Roll Number)
- **Course:** Software Quality Engineering
- **Resource Person:** Faiza Asghar

---

## Project Description

This project demonstrates the implementation of **Unit Testing** and **Integration Testing** concepts using Python and PyTest framework. The project contains a simple banking application (`bank_app.py`) with the following functions:

### Banking Functions:
1. **deposit(balance, amount):** Adds money to an account balance
2. **withdraw(balance, amount):** Removes money from an account balance
3. **calculate_interest(balance, rate, years):** Calculates compound interest
4. **check_loan_eligibility(balance, credit_score):** Checks if a customer is eligible for a loan
5. **transfer(balance_from, balance_to, amount):** Transfers money between two accounts

### Testing Approach:
- **Unit Tests (`test_unit.py`):** Tests each function independently with:
  - Valid input cases
  - Boundary value cases
  - Invalid input cases with exception handling

- **Integration Tests (`test_integration.py`):** Tests the interaction between multiple functions:
  - Transfer operations (which combine withdraw and deposit)
  - Combined banking workflows
  - End-to-end scenarios

---

## How to Run Tests

### Prerequisites
1. Python 3.x installed
2. pip (Python package manager)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run All Tests
```bash
pytest
```

### Step 3: Run Tests with Verbose Output
```bash
pytest -v
```

### Step 4: Run Specific Test File
```bash
# Run unit tests only
pytest test_unit.py -v

# Run integration tests only
pytest test_integration.py -v
```

### Step 5: Generate HTML Report
```bash
pytest --html=report.html -v
```
Open `report.html` in a web browser to view the detailed test report.

---

## GitHub Actions (CI/CD)

This project uses **GitHub Actions** for Continuous Integration (CI). The workflow is defined in `.github/workflows/python-tests.yml`.

### What GitHub Actions Does:
1. **Triggers on:** Every `push` and `pull_request` to the repository
2. **Environment:** Runs on Ubuntu latest with Python 3.x
3. **Steps:**
   - Checks out the code
   - Sets up Python environment
   - Installs dependencies from `requirements.txt`
   - Runs all tests using `pytest -v`

### How to Check CI Status:
1. Go to your GitHub repository
2. Click on the **Actions** tab
3. Select **Python Unit & Integration Tests** workflow
4. ✅ Green tick = All tests passed
5. ❌ Red cross = Tests failed (check logs for details)

---

## Project Structure
```
unit-integration-testing-lab/
│
├── bank_app.py              # Main application code
├── test_unit.py             # Unit test cases
├── test_integration.py      # Integration test cases
├── requirements.txt         # Python dependencies
├── README.md                # Project documentation
├── .gitignore               # Git ignore file
└── .github/
    └── workflows/
        └── python-tests.yml # GitHub Actions CI workflow
```

---

## Test Summary

### Unit Tests (test_unit.py)
| Function | Test Cases |
|----------|------------|
| deposit() | Valid deposits, boundary values, zero/negative amounts |
| withdraw() | Valid withdrawals, boundary values, insufficient balance |
| calculate_interest() | Valid calculations, zero values, negative values |
| check_loan_eligibility() | Eligible cases, boundary cases, ineligible cases |

### Integration Tests (test_integration.py)
| Scenario | Description |
|----------|-------------|
| Transfer | Tests transfer function combining withdraw and deposit |
| Combined Workflows | Multiple operations in sequence |
| Complete Banking | End-to-end banking scenarios |

---

## License
This project is created for educational purposes as part of Software Quality Engineering coursework.
