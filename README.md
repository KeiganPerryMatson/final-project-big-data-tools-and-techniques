# Final Project - Big Data Tools & Techniques

## Prompt

Create a Python application by doing the following steps:

- Choose any distributed database / technology. It can be what we discussed in class or anything of your choice. Examples include Redis, Neo4J, MongoDB, Spark, ELK, etc. Do NOT not a RDBMS (SQL Server, MySQL, Oracle, Teradata, ProstreSQL, etc).
- Choose an authentic public dataset containing at least 100,000 rows and 8 columns. The dataset can be JSON, CSV, Parquet, Avro, or anything you'd like to use or is supported by your database. If it's JSON, it should be a similar data size.
- Import the data into your database.
- Using visualization tools like Tableau or Power Bi, query the data and create 3 visualizations. The quality of the work should be what you would like to present to a future employer during an interview. If you are not into visualization, then build 3 machine learning models. If desired, you can also create a combination of machine learning models and vizualizations (3 maximum).

Submit the following:

- Using a screen recorder, walk through the input data, how you imported it, what tool you used, and explain the visualization(s) or model(s). The total video length should not be more than 6 minutes and should be uploaded to Youtube. Also mention what you liked / did not like in the course. Submit the unlisted YouTube URL of the video.
- Push your project to a Github repository and share the URL.

## Execution

For this assignment, I decided to use a Kaggle dataset with the results of a mental health survey (see https://www.kaggle.com/datasets/bhavikjikadara/mental-health-dataset). After removing the date column, which I deemed not useful for my purposes, and adding a patient_id column to give each row a unique identifier, I wrote the Python code in this repository to store the data into a MongoDB database. For the latter portion of the project involving models and visualizations, I elected to use MongoDB Atlas to query the data directly from the database and create 3 visualizations. As such, functions to retrieve data from the database and to display visualizations were not necessary for this repository.

## Set-Up

In order to run this code, please do the following:

- Clone this GitHub repository locally by running the following in a command prompt window: git clone https://github.com/KeiganPerryMatson/final-project-big-data-tools-and-techniques.git
- Ensure that you have the following Python libraries installed on your local machine: pymongo, csv
- Run the application by navigating into the newly generated directory and running python ./main.py
