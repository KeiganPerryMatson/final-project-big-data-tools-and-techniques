# Includes for user-defined classes
from MongoDBDataAccessor import MongoDBDataAccessor

############################################
# Insert CSV Dataset Into MongoDB Database #
############################################

# Define a file path for the CSV dataset
csv_file_path = r'Mental Health Dataset.csv'

# Initialize a MongoDBDataAccessor object, used to store data into the MongoDB database
mongoDB_data_accessor = MongoDBDataAccessor()

# Use the CSV file path defined above to store the CSV data into the MongoDB Database
mongoDB_data_accessor.storeData(csv_file_path)

#################################################################################################
# MongoDB Database Was Queried In MongoDB Atlas and MongoDB Charts Were Used For Visualizations #
#################################################################################################