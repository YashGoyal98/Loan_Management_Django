from celery import shared_task
import math
from lms_bm_app.models import TransactionDetails, UserDetails


@shared_task(bind=True)
def compute_credit_score(self,aadhar_id):

    transactions = TransactionDetails.objects.filter(aadhar_id=aadhar_id)
    user_details = UserDetails.objects.get(aadhar_id= aadhar_id)
    balance = 0
    credit_score=300
    for transaction in transactions:
        if(transaction.transaction_type=="CREDIT"):
            balance += transaction.amount
        elif(transaction.transaction_type=="DEBIT"):
            balance -= transaction.amount

    if(balance>=1000000):
        credit_score = 900
    elif(balance>100000):
        credit_score+= (math.floor(balance/15)) * 10
    user_details.account_balance = balance
    user_details.credit_score=credit_score
    user_details.save()