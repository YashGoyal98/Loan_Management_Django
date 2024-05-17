from lms_bm_app.Serializers.serializers import TransactionDetailsSerializer
from lms_bm_app.models import TransactionDetails, LoanDetails
from rest_framework import status

class GetStatement:

    def __init__(self):
        pass

    def getStatement(self, data):
        """
        Fetches the loan payments and future plan

        Args:
          data: Contains :
            ● Aadhar ID: Unique User Identifier already generated and the same is given in csv.
            ● name
            ● email_id
            ● annual_income
        Returns:
          user Id if successful        """
        try:
            loan_id = data.get("loan_id")
            loan_details = LoanDetails.objects.get(loan_id=loan_id)
            transactions = TransactionDetails.objects.filter(loan_id=loan_id)
            loan_payments = []
            for transaction in transactions:
                loan_payments_serialised = TransactionDetailsSerializer(transaction).data
                loan_payments.append(loan_payments_serialised)
            return {
                "date": loan_details.loan_created_at,
                "principal": loan_details.principal,
                "interest": loan_details.interest_rate,
                "amount_paid": loan_details.amount_paid,
                "upcoming_transactions": loan_details.due_dates,
                "loan_transactions": loan_payments
            },status.HTTP_200_OK
        except Exception as e:
            raise e