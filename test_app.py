import unittest
from app import check_loan_eligibility

class TestLoanEligibility(unittest.TestCase):

    def test_approved(self):
        result = check_loan_eligibility("Amit", "123", 50000, 800)
        self.assertEqual(result["Loan Status"], "Loan Approved")

    def test_conditional(self):
        result = check_loan_eligibility("Ravi", "124", 40000, 700)
        self.assertEqual(result["Loan Status"], "Approved with Conditions")

    def test_rejected(self):
        result = check_loan_eligibility("Sita", "125", 30000, 600)
        self.assertEqual(result["Loan Status"], "Loan Rejected")

if __name__ == "__main__":
    unittest.main()
