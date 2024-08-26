import logging

from api_caller_service import APICaller
from producer import StreamProducer


class ProducerRunner:
    def __init__(self):
        self.api = APICaller()
        self.producer = StreamProducer()

    def run(self):
        while True:
            try:
                tweets = self.api.fetch_tweets()
                self.producer.send_tweets_to_flink(tweets)
            except Exception as e:
                logging.error(f'Exception in main producer loop = {e}')


if __name__ == '__main__':
    runner = ProducerRunner()
    runner.run()
