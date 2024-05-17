from lms_bm_app.Serializers.serializers import TransactionDetailsSerializer
from lms_bm_app.models import TransactionDetails, LoanDetails


class GetStatement:

    def __init__(self):
        pass

    def getStatement(self, data):
        try:
            loan_id = data.get("loan_id")
            loan_details = LoanDetails.objects.get(loan_id=loan_id)
            transactions = TransactionDetails.objects.filter(loan_id=loan_id)
            transaction_loan = []
            for transaction in transactions:
                temp = TransactionDetailsSerializer(transaction).data
                transaction_loan.append(temp)
            result_data = {
                "date": loan_details.loan_created_at,
                "principal": loan_details.principal,
                "interest": loan_details.interest_rate,
                "amount_paid": loan_details.amount_paid,
                "upcoming_transactions": loan_details.due_dates,
                "loan_transactions": transaction_loan
            }
        except Exception as e:
            raise e