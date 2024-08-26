# Tweets Sentiment Analysis

This project is a part of backend engineering assessment.

### This is divided into 2 parts

1. Tweets fetching and producer: This module is responsible for fetching tweets from Vetric and producing them on Apache
   Flink.
2. Tweets consuming and sentiment analysis: This module is responsible for consuming tweets from Apache Flink and
   applying sentiment analysis using Huggingface transformer and print the sentiment.

### Entry points

1. Producer entry point is `producer_main.py`
2. Consumer entry point is `consumer_main.py`