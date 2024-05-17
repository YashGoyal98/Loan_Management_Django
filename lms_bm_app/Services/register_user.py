from lms_bm_app.models import UserDetails
from rest_framework import status
import uuid
class RegisterUser:
    def __int__(self):
        pass

    def register_user(self,data):
        """
        Registers a user

        Args:
          data: Contains :
            ● Aadhar ID: Unique User Identifier already generated and the same is given in csv.
            ● name
            ● email_id
            ● annual_income
        Returns:
          user Id if successful        """
        try:
            aadhar_id = data.get("aadhar_id")
            name = data.get("name")
            email_id = data.get("email")
            annual_income = data.get("annual_income")
            user_id = uuid.uuid4()
            UserDetails.objects.create(
                user_id = user_id,
                name =   data.get("name"),
                email_id= data.get("email"),
                annual_income=data.get("annual_income"),
                aadhar_id = data.get("aadhar_id")
            )
            return {"user_id":user_id},status.HTTP_200_OK
        except Exception as e:
            return {"error": {str(e)}}, status.HTTP_200_OK