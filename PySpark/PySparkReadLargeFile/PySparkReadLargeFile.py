from pyspark.sql import SparkSession
from pyspark.sql.functions import split, size

try:
    ## Part 1
    
    spark = SparkSession.builder \
        .appName("WordCount") \
        .getOrCreate()

    spark.sparkContext.setLogLevel("ERROR")  # Adjust the log level as needed


    file_path = '/tmp/enwik9'

    # Read the text file into a DataFrame
    text_df = spark.read.text(file_path)


    ## Part 2

    # Split each line into words using whitespace as the delimiter
    words_df = text_df.select(split(text_df.value, " ").alias("words"))

    # Count the number of words in each line
    word_count_df = words_df.select(size(words_df.words).alias("word_count"))

    # Calculate the total word count
    total_word_count = word_count_df.selectExpr("sum(word_count) as total_word_count").collect()[0]["total_word_count"]

    print(f"Total words processed: {total_word_count}")

    ## Part 3

    spark.stop()
except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Ensure Spark session is stopped
    spark.stop()
