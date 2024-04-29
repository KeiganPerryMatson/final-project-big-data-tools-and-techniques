# Needed for establishing a connection to the MongoDB database
import pymongo

# Needed to read in the CSV file
import csv

class MongoDBDataAccessor:

    """
    CLASS ABSTRACT: MongoDBDataAccessor

    DESCRIPTION: This class stores CSV data into the MongoDB database. 
    """

    def __init__(self):

        """
        FUNCTION ABSTRACT: Constructor

        DESCRIPTION: Creates an object of type MongoDBDataAccessor.

        ARGS: self - the class object

        RETURNS: None
        """

        # Initialize the MongoDB database connection (note that you would need to substitute your connection string below to connect to your personal database)
        self.__mongoDB_connection = pymongo.MongoClient("mongodb+srv://<username>:<password>@mental-health-database.cyquqok.mongodb.net/")

        # Define a database object
        self.__mongoDB_database = self.__mongoDB_connection['mental_health_data']

        # Define a collection object using the database object
        self.__mongoDB_collection = self.__mongoDB_database['patients']

        print("MongoDBDataAccessor initialized successfully!")

    def storeData(self, csv_file_path):

        """
        FUNCTION ABSTRACT: storeData()

        DESCRIPTION: This function uses the MongoDB database connection to upload a dictionary of CSV data.

        ARGS:
            self - the class object
            csv_file_path - the file path to the CSV file

        RETURNS: None
        """

        # Define the headers of the CSV file
        headers = ['patient_id', 'gender', 'country', 'occupation', 'self_employed', 'family_history', 'treatment', 'days_indoors', 'growing_stress', 'changes_habits',
                    'mental_health_history', 'mood_swings', 'coping_struggles', 'work_interest', 'social_weakness', 'mental_health_interview', 'care_options']

        # Open the CSV file for reading
        with open(csv_file_path, 'r', encoding = 'utf-8') as csv_file:

            # Define a dictionary reader to parse through the CSV file
            csv_reader = csv.DictReader(csv_file)

            # For every patient in the CSV dataset...
            for patient in csv_reader:
                
                # Define an empty row to house the current patient's data
                row = {}

                # For every column...
                for field in headers:

                    # Append the patient's data under this column to our row
                    row[field] = patient[field]

                # Call the MongoDB collection to insert the row
                self.__mongoDB_collection.insert_one(row)