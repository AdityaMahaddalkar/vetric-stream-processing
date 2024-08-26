import logging

from consumer import StreamConsumer

logging.basicConfig(level=logging.INFO)


class ConsumerRunner:
    def __init__(self):
        self.consumer = StreamConsumer()

    def run(self):
        logging.info(f'Starting run for tweet consumption and sentiment analysis')
        try:
            self.consumer.process_tweets_from_flink()
        except Exception as e:
            logging.error(f'Exception occurred while consuming tweets and sentiment analysis = {e}')
