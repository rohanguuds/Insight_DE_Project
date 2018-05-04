# Project Idea(1-Sentence):

Optimize ad campaign by setting up a benchmark performance and comparing the value metric in real time. 

# Purpose:

Our company has launched an app for the upcoming soccer world cup. We would like to advertise it on AppStore, GooglePlay, Facebook and Youtube and capture the conversion of our app on various platforms. 
This can be used by any company who does digital advertising.

# Use Case:

1. Calculate the click, impression bounce rate and set up a value metric of our campaign(batch mode)
2. To check how many users are actively using our app (realtime)
3. To make business decision based on analytics (customer acquisition rate, type of customers based on age group, location)

# What technologies are well suited to solve those challenges?

- Ingestion: Kafka
- Storage: HDFS
- Processing: Spark, Spark Streaming
- Database: Cassandra

# What are the primary engineering challenges? 

- as of now, the simulated data and end result will involve aggregation and displaying results. I am trying to find out a way to put another layer of data to compare with existing data and introduce some kind of join operation




![architecture](https://github.com/rohanguuds/Insight_DE_Project/blob/master/pipeline.png)


# Dataset:

I will simulate the user session data.




