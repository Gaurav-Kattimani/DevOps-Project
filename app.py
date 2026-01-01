def check_loan_eligibility(name, account_no, income, credit_score):
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
    name = input("Enter customer name: ")
    account_no = input("Enter account number: ")
    income = float(input("Enter monthly income: "))
    credit_score = int(input("Enter credit score: "))

    result = check_loan_eligibility(name, account_no, income, credit_score)

    print("\n--- Loan Eligibility Result ---")
    for key, value in result.items():
        print(f"{key}: {value}")
