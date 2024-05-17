from django.urls import path, include
from .views import RegisterUserAPI,ApplyLoanAPI,MakePaymentAPI,MakePaymentAPI

urlpatterns = [
    path('register-user/', RegisterUserAPI.as_view(), name="register_user"),
    path('apply-loan/', ApplyLoanAPI.as_view(), name="apply_loan"),
    path('make-payment/', MakePaymentAPI.as_view(), name="make_payment"),
    path('get-statement/', MakePaymentAPI.as_view(), name="get_statement"),
]