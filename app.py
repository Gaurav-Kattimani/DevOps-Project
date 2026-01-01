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

    # Default execution (no user input)
    result = check_loan_eligibility()

    print("\n--- Loan Eligibility Result ---")
    for key, value in result.items():
        print(f"{key}: {value}")
