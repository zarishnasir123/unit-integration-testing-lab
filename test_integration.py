# test_integration.py
import pytest
from bank_app import deposit, withdraw, calculate_interest, check_loan_eligibility, transfer


# ==================== TRANSFER FUNCTION INTEGRATION TESTS ====================

class TestTransferIntegration:
    """Integration tests for the transfer function which combines withdraw and deposit"""
    
    # Test successful transfers
    def test_transfer_valid_amount(self):
        """Test successful transfer between two accounts"""
        balance_from, balance_to = transfer(1000, 500, 200)
        assert balance_from == 800
        assert balance_to == 700
    
    def test_transfer_entire_balance(self):
        """Test transferring entire balance from one account to another"""
        balance_from, balance_to = transfer(500, 100, 500)
        assert balance_from == 0
        assert balance_to == 600
    
    def test_transfer_to_zero_balance_account(self):
        """Test transferring to an account with zero balance"""
        balance_from, balance_to = transfer(1000, 0, 300)
        assert balance_from == 700
        assert balance_to == 300
    
    def test_transfer_decimal_amount(self):
        """Test transferring a decimal amount"""
        balance_from, balance_to = transfer(100.50, 50.25, 25.25)
        assert balance_from == 75.25
        assert balance_to == 75.50
    
    def test_transfer_small_amount(self):
        """Test transferring a very small amount"""
        balance_from, balance_to = transfer(100, 100, 0.01)
        assert balance_from == 99.99
        assert balance_to == 100.01
    
    # Test transfer failure scenarios
    def test_transfer_insufficient_balance_raises_error(self):
        """Test that transfer fails when source has insufficient balance"""
        with pytest.raises(ValueError, match="Insufficient balance"):
            transfer(100, 500, 200)
    
    def test_transfer_zero_amount_raises_error(self):
        """Test that transfer fails with zero amount"""
        with pytest.raises(ValueError, match="Transfer amount must be positive"):
            transfer(1000, 500, 0)
    
    def test_transfer_negative_amount_raises_error(self):
        """Test that transfer fails with negative amount"""
        with pytest.raises(ValueError, match="Transfer amount must be positive"):
            transfer(1000, 500, -100)
    
    def test_transfer_from_zero_balance_raises_error(self):
        """Test that transfer fails from zero balance account"""
        with pytest.raises(ValueError, match="Insufficient balance"):
            transfer(0, 500, 100)


# ==================== COMBINED WORKFLOW INTEGRATION TESTS ====================

class TestCombinedWorkflows:
    """Integration tests for combined workflows involving multiple functions"""
    
    # Workflow: Transfer followed by interest calculation
    def test_transfer_then_calculate_interest(self):
        """Test workflow: transfer money, then calculate interest on recipient account"""
        # Initial balances
        account_a = 10000
        account_b = 5000
        
        # Perform transfer
        account_a, account_b = transfer(account_a, account_b, 2000)
        assert account_a == 8000
        assert account_b == 7000
        
        # Calculate interest on recipient account (5% for 1 year)
        account_b_with_interest = calculate_interest(account_b, 5, 1)
        assert account_b_with_interest == 7350.0
    
    def test_deposit_withdraw_transfer_workflow(self):
        """Test workflow: deposit to account, withdraw from another, then transfer"""
        # Initial balances
        account_a = 1000
        account_b = 500
        
        # Deposit to account A
        account_a = deposit(account_a, 500)
        assert account_a == 1500
        
        # Withdraw from account B
        account_b = withdraw(account_b, 100)
        assert account_b == 400
        
        # Transfer from A to B
        account_a, account_b = transfer(account_a, account_b, 300)
        assert account_a == 1200
        assert account_b == 700
    
    def test_multiple_transfers_workflow(self):
        """Test workflow: multiple sequential transfers between accounts"""
        account_a = 1000
        account_b = 500
        account_c = 200
        
        # Transfer from A to B
        account_a, account_b = transfer(account_a, account_b, 200)
        assert account_a == 800
        assert account_b == 700
        
        # Transfer from B to C
        account_b, account_c = transfer(account_b, account_c, 300)
        assert account_b == 400
        assert account_c == 500
        
        # Transfer from C back to A
        account_c, account_a = transfer(account_c, account_a, 100)
        assert account_c == 400
        assert account_a == 900
    
    def test_transfer_and_loan_eligibility_check(self):
        """Test workflow: transfer money, then check loan eligibility"""
        # Initial setup
        account_a = 3000
        account_b = 4000
        credit_score = 750
        
        # Before transfer - account B is not eligible
        assert check_loan_eligibility(account_b, credit_score) is False
        
        # Transfer to make account B eligible
        account_a, account_b = transfer(account_a, account_b, 1500)
        assert account_a == 1500
        assert account_b == 5500
        
        # After transfer - account B should be eligible
        assert check_loan_eligibility(account_b, credit_score) is True
    
    def test_deposit_and_loan_eligibility_workflow(self):
        """Test workflow: deposit to reach loan eligibility threshold"""
        balance = 4500
        credit_score = 720
        
        # Not eligible initially
        assert check_loan_eligibility(balance, credit_score) is False
        
        # Deposit to become eligible
        balance = deposit(balance, 500)
        assert balance == 5000
        
        # Now should be eligible
        assert check_loan_eligibility(balance, credit_score) is True
    
    def test_interest_calculation_after_multiple_deposits(self):
        """Test workflow: multiple deposits followed by interest calculation"""
        balance = 1000
        
        # Multiple deposits
        balance = deposit(balance, 500)
        balance = deposit(balance, 300)
        balance = deposit(balance, 200)
        assert balance == 2000
        
        # Calculate compound interest (10% for 2 years)
        final_balance = calculate_interest(balance, 10, 2)
        assert final_balance == pytest.approx(2420.0, rel=1e-2)
    
    def test_withdraw_transfer_workflow_failure(self):
        """Test workflow failure: withdraw too much, then transfer fails"""
        account_a = 1000
        account_b = 500
        
        # Withdraw from account A
        account_a = withdraw(account_a, 800)
        assert account_a == 200
        
        # Try to transfer more than remaining balance - should fail
        with pytest.raises(ValueError, match="Insufficient balance"):
            transfer(account_a, account_b, 300)
    
    def test_complete_banking_workflow(self):
        """Test complete banking workflow with all operations"""
        # Customer starts with initial deposit
        savings_balance = 0
        checking_balance = 1000
        credit_score = 680
        
        # Deposit paycheck to checking
        checking_balance = deposit(checking_balance, 3000)
        assert checking_balance == 4000
        
        # Transfer to savings
        checking_balance, savings_balance = transfer(checking_balance, savings_balance, 2000)
        assert checking_balance == 2000
        assert savings_balance == 2000
        
        # Additional deposit to savings
        savings_balance = deposit(savings_balance, 3500)
        assert savings_balance == 5500
        
        # Check loan eligibility (balance >= 5000, but credit score < 700)
        assert check_loan_eligibility(savings_balance, credit_score) is False
        
        # With improved credit score
        credit_score = 720
        assert check_loan_eligibility(savings_balance, credit_score) is True
        
        # Calculate projected interest on savings (5% for 3 years)
        projected_balance = calculate_interest(savings_balance, 5, 3)
        assert projected_balance == pytest.approx(6367.19, rel=1e-2)
    
    def test_balance_consistency_after_operations(self):
        """Test that total balance remains consistent across transfers"""
        account_a = 5000
        account_b = 3000
        total_before = account_a + account_b
        
        # Perform multiple transfers
        account_a, account_b = transfer(account_a, account_b, 1000)
        account_b, account_a = transfer(account_b, account_a, 500)
        account_a, account_b = transfer(account_a, account_b, 250)
        
        # Total should remain the same
        total_after = account_a + account_b
        assert total_before == total_after
