# Unit and Integration Testing Lab (Assignment 02)

## My Information  
**Name:** Zarish Nasir  
**Roll Number:** 231400133
**Course:** Software Quality Engineering (SE-315L)  
**University:** GIFT University, Gujranwala  

---

## Project Description  

This project demonstrates the implementation of **Unit Testing and Integration Testing** using **Python and PyTest**. A simple banking application (`bank_app.py`) has been developed with core functions such as:

- `deposit()`
- `withdraw()`
- `calculate_interest()`
- `check_loan_eligibility()`
- `transfer()`

### Testing Approach:
- **Unit Tests (`test_unit.py`)**  
  Each function was tested independently using:
  - Valid inputs  
  - Boundary values  
  - Invalid inputs using `pytest.raises()`  

- **Integration Tests (`test_integration.py`)**  
  These tests verify how multiple functions work together, including:
  - Successful money transfer  
  - Transfer failure scenarios  
  - Combined workflow: transfer followed by interest calculation  

---

## Technologies Used  

- Python 3.x  
- PyTest  
- GitHub  
- GitHub Actions (CI/CD)  

---

## How to Run Tests Locally  

### Step 1 — Install Dependencies  
Run:
```bash
pip install -r requirements.txt
