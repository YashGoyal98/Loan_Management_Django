from lms_bm_app.models import LoanDetails, UserDetails, TransactionDetails
from rest_framework import status
from .helper import Helper
from datetime import datetime
import uuid

class MakePayment:
    def __init__(self):
        pass
    def make_payment(self,data):
        """
        Helps towards registering payments made towards loan

        Args:
          data: Contains :
           ● Loan_id: Unique identifier to identify the loan
           ● Amount (depends upon User)
        Returns:
          loan Id and the loan plan if successful        """
        try:
            loan_id = data.get("loan_id")
            loan_details = LoanDetails.objects.filter(loan_id=loan_id)
            user = UserDetails.objects.filter(user_id=data.get(loan_details.user_id))
            amount = data.get("amount")
            current_month = datetime.now().month
            last_paid_month = loan_details.last_payment_date.month

            if(loan_details.is_cleared):
                return {"error":"The loan is already paid in full. Cheers!"},status.HTTP_400_BAD_REQUEST
            if(last_paid_month==current_month):
                return {"error":"Payment received this month, pay next month now!"},status.HTTP_400_BAD_REQUEST
            if(last_paid_month<current_month-1):
                return {"error":"You have missed EMI Payments! Can't pay now"},status.HTTP_400_BAD_REQUEST

            TransactionDetails.objects.create(transaction_id=uuid.uuid4(),
                                              transaction_type="LOAN_DEBIT",
                                              amount=amount,
                                              aadhar_uuid=user.adhar_uuid,
                                              transaction_date=datetime.now(),
                                              loan_id=loan_id)
            if(user.current_debt<=amount):
                return self.closeLoan(amount, loan_details, user)
            else:
                self.updateLoan(amount, loan_details, user)
                return {"message": f"Succesfully credited to your loan account, will reflect in 4 to 7 days\n LoanId : {str(loan_id)}"}, status.HTTP_200_OK

        except Exception as e:
            raise e

    def updateLoan(self, amount, loan_details, user):
        emi_data = Helper.calculate_emi_plan(principal=loan_details.principal,
                                             rate=loan_details.interest_rate,
                                             tenure=len(loan_details.due_dates),
                                             monthly_income=user.annual_income / 12,
                                             disbursal_date=datetime.now(),
                                             total_interest=loan_details.total_interest)
        loan_details.due_dates = emi_data.get("due_dates")
        loan_details.amount_paid = loan_details.amount_paid + amount
        loan_details.last_payment_date = datetime.now()
        loan_details.save()

    def closeLoan(self, amount, loan_details, user):
        user.current_debt = 0
        user.balance -= user.current_debt
        loan_details.is_cleared = True
        loan_details.due_dates = []
        user.is_debt_cleared = True
        loan_details.amount_paid = user.current_debt
        user.save()
        loan_details.save()
        TransactionDetails.objects.create(transaction_id=uuid.uuid4(),
                                          transaction_type="CREDIT",
                                          amount=amount - user.current_debt,
                                          aadhar_uuid=user.adhar_uuid,
                                          transaction_date=datetime.now())
        return {"message": "Loan is closed! Remaining amount credited to bank account should reflect in 4 to "
                           "7 days"}
