from datetime import datetime

from django.db import models

class TransactionDetails(models.Model):
    transaction_type = models.CharField(max_length=10, null=True)
    amount = models.FloatField(null=True)
    aadhar_uuid = models.UUIDField(null=True)
    transaction_date = models.DateTimeField(auto_now_add=True)
    loan_id = models.CharField(max_length=100, null=True)

class UserDetails(models.Model):
    user_id = models.UUIDField(primary_key=True)
    adhar_uuid = models.CharField(max_length=100)
    name = models.CharField(max_length=40)
    email_id = models.CharField(max_length=100)
    annual_income = models.FloatField()
    account_balance = models.FloatField()
    credit_score = models.IntegerField(null=True)
    loan_created_at = models.DateTimeField(null=True)
    is_debt_cleared = models.BooleanField(null=True)
    current_debt = models.FloatField(null=True)


class LoanDetails(models.Model):
    loan_id = models.UUIDField(null=True)
    loan_created_at = models.DateTimeField(auto_now_add=True, null=True)
    loan_type = models.CharField(max_length=20, null=True)
    aadhar_id = models.CharField(max_length=100)
    interest_rate = models.CharField(max_length=10)
    disbursal_date = models.DateTimeField(null=True)
    user_id = models.UUIDField(null=True)
    due_dates = models.JSONField(max_length=100)
    is_cleared = models.BooleanField(default=False)
    principal = models.FloatField(null=False)
    total_interest = models.FloatField(null=False,default=0)
    amount_paid = models.FloatField(null=True)
    last_payment_date = models.DateTimeField(default=datetime.now(),null=True)