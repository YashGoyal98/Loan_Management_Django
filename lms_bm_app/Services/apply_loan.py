from lms_bm_app.models import UserDetails
from rest_framework import status
from ..models import UserDetails, LoanDetails
from datetime import datetime
from .helper import Helper
import uuid

class ApplyLoan:


    def __int__(self):
        self.loan_limit = {
            "Cars": 750000,
            "Home": 8500000,
            "Education": 5000000,
            "Personal": 1000000
        }

    def apply_loan(self,data):
        """
        Applies for a loan

        Args:
          data: Contains :
            ● unique_user_id: Unique User Identifier (UUID)
            ● loan_type: Loan type as supported above
            ● loan_amount: Amount of Loan in rupees
            ● interest_rate: Rate of interest in percentage
            ● term_period: time period of repayment in months
            ● disbursement_date: Date of disbursal
        Returns:
          loan Id and the loan plan if successful        """
        try:
            user = UserDetails.objects.filter(user_id=data.get("user_id"))
            amount = data.get("loan_amount")
            loan_type = data.get("loan_type")
            interest = data.get("interest_rate")
            tenure = data.get("term_period")
            disbursal_date=data.get("disbursal_date")
            total_interest = amount*((1+interest/100)**tenure)
            emi_data = Helper.calculate_emi_plan(
                principal=amount,
                rate=interest,
                tenure=tenure,
                disbursal_date=disbursal_date,
                monthly_income=user.annual_income/12,
                total_interest=total_interest
            )
            user.loan_created_at = datetime.now()
            user.current_debt = emi_data.get("total_amount")
            user.save()
            loan_id = uuid.uuid4()
            due_dates = emi_data.get("due_dates")
            LoanDetails.objects.create(
                loan_id = loan_id,
                loan_created_at = user.loan_created_at,
                loan_type = loan_type,
                aadhar_id = user.aadhar_id,
                interest_rate = interest,
                disbursal_date = disbursal_date,
                user_id = user.user_id,
                due_dates = due_dates,
                total_interest=total_interest
            )
            return { "loan_id": loan_id,"due_dates": due_dates},status.HTTP_200_OK

        except Exception as e:
            raise e