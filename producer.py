import json
import logging

from pyflink.common import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaProducer

from app_config import AppConfig


class StreamProducer:
    def __init__(self):
        self.config = AppConfig().get_config()

        self.env = StreamExecutionEnvironment.get_execution_environment()

        self.topic = self.config['flink']['topic']
        self.producer = FlinkKafkaProducer(
            self.topic,
            Types.ROW([Types.STRING()]),
            producer_config={
                'bootstrap.servers': self.config['flink']['bootstrap.servers'],
                'group.id': self.config['flink']['group.id']
            }
        )

    def send_tweets_to_flink(self, tweet_text_list):
        logging.info(f'Trying to send #{len(tweet_text_list)} tweets')

        ds = self.env.from_collection([json.dumps(tweet) for tweet in tweet_text_list])
        ds.add_sink(self.producer)
        self.env.execute()
