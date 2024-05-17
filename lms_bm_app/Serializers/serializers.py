from rest_framework import serializers

class TransactionDetailsSerializer(serializers.Serializer):
    transaction_id = serializers.UUIDField()
    transaction_type = serializers.CharField(max_length=20)
    amount = serializers.FloatField()
    user_id = serializers.UUIDField()
    transaction_date = serializers.DateTimeField()
    loan_id = serializers.CharField(max_length=100)

class PaymentDetailsSerializer(serializers.Serializer):
    loan_id = serializers.UUIDField()
    amount = serializers.FloatField()

class UserDetailsSerializer(serializers.Serializer):
    adhar_id = serializers.UUIDField()
    annual_income = serializers.FloatField()
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()

class LoanDetailsSerializer(serializers.Serializer):
    user_id = serializers.UUIDField()
    loan_type = serializers.ChoiceField(choices=["Cars", "Home", "Education", "Personal"])
    loan_amount = serializers.FloatField()
    interest_rate = serializers.IntegerField()
    term_period = serializers.IntegerField()
    disbursement_date = serializers.DateTimeField()