import os

import pandas as pd

from .models import TransactionDetails

# Read CSV file into a DataFrame
# script.py
# current_file = os.path.abspath(os.path.dirname(__file__))
#
# #csv_filename
# csv_filename = os.path.join(current_file, './data_folder/transactions_data.csv')
#
# df = pd.read_csv(csv_filename)
#
# # Iterate through the DataFrame and create model instances
# # for index, row in df.iterrows():
# #     # Create the Transaction instance
# #     #user,date,transaction_type,amount
# #     transaction = TransactionDetails(
# #         aadhar_uuid=row['user'],
# #         transaction_date=row['date'],
# #         transaction_type=row['transaction_type'],
# #         amount=row['amount']
# #     )
# #     #to save the current transaction
# #     transaction.save()
#
# print("CSV data has been loaded into the Django database.")