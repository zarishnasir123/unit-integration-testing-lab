# test_unit.py
import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility


# ==================== DEPOSIT FUNCTION TESTS ====================

class TestDeposit:
    """Unit tests for the deposit function"""
    
    # Test normal valid inputs
    def test_deposit_valid_amount(self):
        """Test depositing a valid positive amount"""
        assert deposit(1000, 500) == 1500
    
    def test_deposit_to_zero_balance(self):
        """Test depositing to a zero balance account"""
        assert deposit(0, 100) == 100
    
    def test_deposit_large_amount(self):
        """Test depositing a large amount"""
        assert deposit(1000, 1000000) == 1001000
    
    def test_deposit_decimal_amount(self):
        """Test depositing a decimal amount"""
        assert deposit(100.50, 50.25) == 150.75
    
    # Test boundary values
    def test_deposit_minimum_valid_amount(self):
        """Test depositing the smallest valid amount (just above 0)"""
        assert deposit(100, 0.01) == 100.01
    
    def test_deposit_boundary_one(self):
        """Test depositing exactly 1"""
        assert deposit(0, 1) == 1
    
    # Test invalid inputs
    def test_deposit_zero_amount_raises_error(self):
        """Test that depositing zero raises ValueError"""
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            deposit(100, 0)
    
    def test_deposit_negative_amount_raises_error(self):
        """Test that depositing negative amount raises ValueError"""
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            deposit(100, -50)
    
    def test_deposit_large_negative_raises_error(self):
        """Test that depositing large negative amount raises ValueError"""
        with pytest.raises(ValueError, match="Deposit amount must be positive"):
            deposit(1000, -1000000)


# ==================== WITHDRAW FUNCTION TESTS ====================

class TestWithdraw:
    """Unit tests for the withdraw function"""
    
    # Test normal valid inputs
    def test_withdraw_valid_amount(self):
        """Test withdrawing a valid amount"""
        assert withdraw(1000, 500) == 500
    
    def test_withdraw_partial_balance(self):
        """Test withdrawing part of the balance"""
        assert withdraw(500, 200) == 300
    
    def test_withdraw_decimal_amount(self):
        """Test withdrawing a decimal amount"""
        assert withdraw(100.50, 50.25) == 50.25
    
    # Test boundary values
    def test_withdraw_entire_balance(self):
        """Test withdrawing the entire balance (boundary case)"""
        assert withdraw(100, 100) == 0
    
    def test_withdraw_minimum_valid_amount(self):
        """Test withdrawing the smallest valid amount"""
        assert withdraw(100, 0.01) == 99.99
    
    def test_withdraw_boundary_one(self):
        """Test withdrawing exactly 1"""
        assert withdraw(100, 1) == 99
    
    # Test invalid inputs
    def test_withdraw_zero_amount_raises_error(self):
        """Test that withdrawing zero raises ValueError"""
        with pytest.raises(ValueError, match="Withdraw amount must be positive"):
            withdraw(100, 0)
    
    def test_withdraw_negative_amount_raises_error(self):
        """Test that withdrawing negative amount raises ValueError"""
        with pytest.raises(ValueError, match="Withdraw amount must be positive"):
            withdraw(100, -50)
    
    def test_withdraw_insufficient_balance_raises_error(self):
        """Test that withdrawing more than balance raises ValueError"""
        with pytest.raises(ValueError, match="Insufficient balance"):
            withdraw(100, 150)
    
    def test_withdraw_from_zero_balance_raises_error(self):
        """Test that withdrawing from zero balance raises ValueError"""
        with pytest.raises(ValueError, match="Insufficient balance"):
            withdraw(0, 50)


# ==================== CALCULATE INTEREST FUNCTION TESTS ====================

class TestCalculateInterest:
    """Unit tests for the calculate_interest function"""
    
    # Test normal valid inputs
    def test_calculate_interest_valid_inputs(self):
        """Test calculating interest with valid inputs"""
        result = calculate_interest(1000, 5, 1)
        assert result == 1050.0
    
    def test_calculate_interest_multiple_years(self):
        """Test calculating compound interest over multiple years"""
        result = calculate_interest(1000, 10, 2)
        assert result == pytest.approx(1210.0, rel=1e-2)
    
    def test_calculate_interest_high_rate(self):
        """Test calculating interest with a high rate"""
        result = calculate_interest(1000, 50, 1)
        assert result == 1500.0
    
    def test_calculate_interest_decimal_values(self):
        """Test calculating interest with decimal values"""
        result = calculate_interest(1000.50, 5.5, 2)
        assert result == pytest.approx(1113.58, rel=1e-2)
    
    # Test boundary values
    def test_calculate_interest_zero_balance(self):
        """Test calculating interest with zero balance"""
        result = calculate_interest(0, 5, 1)
        assert result == 0
    
    def test_calculate_interest_zero_rate(self):
        """Test calculating interest with zero rate"""
        result = calculate_interest(1000, 0, 5)
        assert result == 1000
    
    def test_calculate_interest_zero_years(self):
        """Test calculating interest for zero years"""
        result = calculate_interest(1000, 5, 0)
        assert result == 1000
    
    def test_calculate_interest_one_year(self):
        """Test calculating interest for exactly one year"""
        result = calculate_interest(10000, 10, 1)
        assert result == 11000.0
    
    # Test invalid inputs
    def test_calculate_interest_negative_balance_raises_error(self):
        """Test that negative balance raises ValueError"""
        with pytest.raises(ValueError, match="Balance cannot be negative"):
            calculate_interest(-1000, 5, 1)
    
    def test_calculate_interest_negative_rate_raises_error(self):
        """Test that negative rate raises ValueError"""
        with pytest.raises(ValueError, match="Rate cannot be negative"):
            calculate_interest(1000, -5, 1)


# ==================== CHECK LOAN ELIGIBILITY FUNCTION TESTS ====================

class TestCheckLoanEligibility:
    """Unit tests for the check_loan_eligibility function"""
    
    # Test normal valid inputs (eligible cases)
    def test_loan_eligible_high_balance_high_score(self):
        """Test eligibility with high balance and high credit score"""
        assert check_loan_eligibility(10000, 800) is True
    
    def test_loan_eligible_exact_minimum(self):
        """Test eligibility with exact minimum requirements"""
        assert check_loan_eligibility(5000, 700) is True
    
    def test_loan_eligible_above_minimum(self):
        """Test eligibility with values above minimum"""
        assert check_loan_eligibility(6000, 750) is True
    
    # Test boundary values
    def test_loan_boundary_balance_just_below_minimum(self):
        """Test ineligibility with balance just below minimum"""
        assert check_loan_eligibility(4999, 700) is False
    
    def test_loan_boundary_score_just_below_minimum(self):
        """Test ineligibility with credit score just below minimum"""
        assert check_loan_eligibility(5000, 699) is False
    
    def test_loan_boundary_both_just_below_minimum(self):
        """Test ineligibility with both values just below minimum"""
        assert check_loan_eligibility(4999, 699) is False
    
    def test_loan_boundary_balance_at_minimum_score_above(self):
        """Test eligibility with balance at minimum, score above"""
        assert check_loan_eligibility(5000, 800) is True
    
    def test_loan_boundary_balance_above_score_at_minimum(self):
        """Test eligibility with balance above, score at minimum"""
        assert check_loan_eligibility(10000, 700) is True
    
    # Test ineligible cases
    def test_loan_ineligible_low_balance(self):
        """Test ineligibility with low balance"""
        assert check_loan_eligibility(1000, 800) is False
    
    def test_loan_ineligible_low_credit_score(self):
        """Test ineligibility with low credit score"""
        assert check_loan_eligibility(10000, 500) is False
    
    def test_loan_ineligible_both_low(self):
        """Test ineligibility with both low balance and credit score"""
        assert check_loan_eligibility(1000, 500) is False
    
    def test_loan_ineligible_zero_balance(self):
        """Test ineligibility with zero balance"""
        assert check_loan_eligibility(0, 800) is False
    
    # Test invalid inputs
    def test_loan_negative_balance_raises_error(self):
        """Test that negative balance raises ValueError"""
        with pytest.raises(ValueError, match="Balance cannot be negative"):
            check_loan_eligibility(-1000, 700)
