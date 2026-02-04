def assess_financial_health(income, expenses, savings, loans):
    if income <= 0:
        return "Invalid income"

    expense_ratio = expenses / income
    savings_ratio = savings / income
    loan_ratio = loans / income

    if expense_ratio > 0.7:
        return "Poor financial health: Expenses are too high"

    if savings_ratio < 0.2:
        return "Average financial health: Increase savings"

    if loan_ratio > 0.5:
        return "Risky financial health: High loan burden"

    return "Good financial health"


# Example usage
if __name__ == "__main__":
    income = 50000
    expenses = 30000
    savings = 15000
    loans = 10000

    result = assess_financial_health(income, expenses, savings, loans)
    print(result)
