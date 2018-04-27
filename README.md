# Project Idea(1-Sentence):

Build a topline dashboard to showcase the user statistics of recently launched app on various add platform 

# Purpose:

Our company has launched an app for the upcoming soccer world cup. We would like to advertise it on AppStore, GooglePlay, Facebook and Youtube and capture the conversion of our app on various platforms. 
This can be used by any company who does digital advertising.

# Use Case:

1. Calculate the click and impression of our ad on different platform(batch mode)
2. To check how many users are actively using our app (realtime)
3. To make business decision based on analytics (customer acquisition rate, type of customers based on age group, location)

# What technologies are well suited to solve those challenges?

- Ingestion: Kafka, flume
- Storage: HDFS, S3
- Processing: Hadoop Mapreduce, Spark
- Database: Cassandra, may be HBase

# What are the primary engineering challenges? 

- as of now, the simulated data and end result will involve aggregation and displaying results. I am trying to find out a way to put another layer of data to compare with existing data and introduce some kind of join operation

# Why would a Data Engineering Hiring Manager care about this project?

- this project will show my capability of using various industry standard tools to study the most basic problem companies try to solve, i.e generate revenue by advertising product and identify reasons to increase product value


![architecture](https://github.com/rohanguuds/Insight_DE_Project/blob/master/pipeline.png)


# Dataset:

I will simulate the user session data.




