# import transformers 
from transformers import pipeline

pipe = pipeline("text-classification")
pipe("the sky is blue which looks absolutely magical")


# making the list 
pipe = pipeline("text-classification")
pipe(["the sky is blue which looks absolutely magical" , "the man is free from the cruel king"])



# pyspark 


# from pyspark.sql import SparkSession

# # Create SparkSession
# spark = SparkSession.builder.appName("PySpark Example").getOrCreate()

# # Read CSV file into a DataFrame
# data = spark.read.csv("input.csv", header=True, inferSchema=True)

# # Perform data manipulation (e.g., select columns, filter rows)
# processed_data = data.select("column1", "column2").filter(data["column3"] > 10)

# # Write the processed data to a new CSV file
# processed_data.write.csv("output.csv", header=True)

# # Stop the SparkSession
# spark.stop()
