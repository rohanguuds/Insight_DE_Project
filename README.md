# Project Idea(1-Sentence):

Build a topline dashboard to showcase the user statistics of recently launched app on various add platform by implementing a lambda architecture

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

# Proposed architecture?




![architecture](https://github.com/rohanguuds/Insight_DE_Project/blob/master/pipeline.png)


# Dataset:

I will simulate the user data.

raw e.g


{"ts":"3:34:49.000","userID":"Andreana","sessioID":"Drivers","level":"A","location":"Maryland","ip_address":"228.25.186.212"},
{"ts":"20:19:23.000","userID":"Miles","sessioID":"Twohig","level":"C","location":"Colorado","ip_address":"233.126.140.130"},
{"ts":"23:31:55.000","userID":"Jerry","sessioID":"Okell","level":"B","location":"Alaska","ip_address":"167.21.149.227"},
{"ts":"15:21:37.000","userID":"Zea","sessioID":"Cortez","level":"A","location":"Pennsylvania","ip_address":"237.88.216.46"},
{"ts":"0:52:25.000","userID":"Guinna","sessioID":"Lesurf","level":"B","location":"Texas","ip_address":"33.231.189.159"},
{"ts":"19:37:40.000","userID":"Chase","sessioID":"Jandl","level":"A","location":"New York","ip_address":"223.78.12.197"}



