from pyflink.common import Types
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors.kafka import FlinkKafkaConsumer
from transformers import AutoTokenizer, AutoModelForSequenceClassification

from app_config import AppConfig


class StreamConsumer:
    def __init__(self):

        self.config = AppConfig().get_config()

        self.env = StreamExecutionEnvironment.get_execution_environment()

        self.topic = self.config['flink']['topic']

        self.consumer = FlinkKafkaConsumer(
            self.topic,
            Types.ROW([Types.STRING()]),
            properties={
                'bootstrap.servers': self.config['flink']['bootstrap.servers'],
                'group.id': self.config['flink']['group.id']
            }
        )

        self.stream = self.env.add_source(self.consumer)

        self.tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased-finetuned-sst-2-english")
        self.model = AutoModelForSequenceClassification.from_pretrained(
            "distilbert-base-uncased-finetuned-sst-2-english")

    def process_tweets_from_flink(self):
        def analyze_sentiment(text):
            inputs = self.tokenizer(
                text,
                return_tensors='pt'
            )
            outputs = self.model(**inputs)
            logits = outputs.logits
            predicted_class = logits.argmax().item()
            return predicted_class

        self.stream.map(
            analyze_sentiment
        ).print()

        self.env.execute("Sentiemtn Analysis"
                         ""
                         "")
