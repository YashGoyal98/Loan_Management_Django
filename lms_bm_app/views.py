from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .Serializers.serializers import LoanDetailsSerializer, PaymentDetailsSerializer
from .Services.apply_loan import ApplyLoan
from .Services.make_payment import MakePayment
from .Services.register_user import RegisterUser
from .Services.get_statement import GetStatement
from rest_framework import status


class RegisterUserAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            registeredUser, status_code = RegisterUser().register_user(data=data)
            return Response(registeredUser, status=status_code)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class MakePaymentAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            PaymentDetailsSerializer(data=data).is_valid(raise_exception=True)
            PaymentData, status_code = MakePayment().make_payment(data=data)
            return Response(PaymentData, status=status_code)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class ApplyLoanAPI(APIView):
    def post(self, request):
        try:
            data = request.data
            LoanDetailsSerializer(data=data).is_valid(raise_exception=True)
            loan_data, status_code = ApplyLoan().apply_loan(data=data)
            return Response(loan_data, status=status_code)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class GetStatementAPI(APIView):
    def get(self, request):
        try:
            data = request.data
            loan_transaction_data, status_code = GetStatement().getStatement(data=data)
            return Response(loan_transaction_data, status=status_code)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
