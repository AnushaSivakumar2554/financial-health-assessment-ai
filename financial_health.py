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
    income = float(input("Enter monthly income: "))
    expenses = float(input("Enter monthly expenses: "))
    savings = float(input("Enter total savings: "))
    loans = float(input("Enter total loan amount: "))

    result = assess_financial_health(income, expenses, savings, loans)
    print("Financial Health Status:", result)
