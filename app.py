import os

def check_loan_eligibility(
    name="Rahul Sharma",
    account_no="ACC1001",
    income=50000.0,
    credit_score=720
):
    if credit_score >= 750:
        status = "Loan Approved"
    elif 650 <= credit_score < 750:
        status = "Approved with Conditions"
    else:
        status = "Loan Rejected"

    return {
        "Name": name,
        "Account Number": account_no,
        "Monthly Income": income,
        "Credit Score": credit_score,
        "Loan Status": status
    }


if __name__ == "__main__":

    # Read values from environment variables (if provided)
    name = os.getenv("NAME", "Rahul Sharma")
    account_no = os.getenv("ACCOUNT_NO", "ACC1001")
    income = float(os.getenv("INCOME", 50000))
    credit_score = int(os.getenv("CREDIT_SCORE", 720))

    result = check_loan_eligibility(name, account_no, income, credit_score)

    print("\n--- Loan Eligibility Result ---")
    for key, value in result.items():
        print(f"{key}: {value}")
