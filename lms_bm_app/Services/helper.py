from datetime import datetime


class Helper:

    def __int__(self):
        pass

    def calculate_emi_plan(self, principal, rate, tenure, monthly_income, disbursal_date, total_interest):
        """
        Calculates the Equated Monthly Installment (EMI) for a loan.

        Args:
          principal: The principal loan amount.
          rate: The annual interest rate (in percentage).
          tenure: The loan tenure in months.
          monthly_income :the monthly income of the user
        Returns:
          The EMI Payment Plan.
        """
        emi_plan = []
        disbursal_date = datetime.strptime(disbursal_date, format("%Y-%m-%d"))
        monthly_rate = rate / 12 / 100
        emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
        emi = round(emi, 2)
        total_amount = total_interest + principal
        if validate(principal, rate, tenure, monthly_income, emi, total_interest):
            raise IOError
        payment_month = disbursal_date.month
        payment_year = disbursal_date.year
        for i in range(0, tenure):
            if (payment_month == 12):
                payment_month = 1
                payment_year += 1
            else:
                payment_month += 1
            interest_payment = (principal * rate) / 12
            principal_payment = emi - interest_payment
            principal -= principal_payment
            if (i == tenure):
                emi += tenure * emi - total_amount
            emi_plan.append({"date": datetime(payment_year, payment_month, 1),
                             "amount_due": emi})

        return emi_plan


def validate(principal, rate, tenure, monthly_income, emi, total_interest):
    if monthly_income * 0.6 >= emi and rate >= 14 and total_interest > 10000:
        return True
    else:
        return False
