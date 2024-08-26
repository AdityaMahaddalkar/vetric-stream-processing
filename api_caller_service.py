import logging
import time

import requests


class APICaller:
    def __init__(self):
        self.vetric_endpoint = 'https://api.vetric.io/twitter/v1/search/top?query=rate%20limits'

        self.max_retries = 5
        self.backoff_multiplier = 2
        self.initial_delay = 1  # second

    def fetch_tweets(self):
        delay = self.initial_delay

        for attempt in range(self.max_retries):
            try:
                response = requests.get(self.vetric_endpoint)
                if response.status_code == 200:
                    json_body = response.json()
                    return list(map(lambda tweet: tweet['tweet']['full_text'], json_body['tweets']))
                else:
                    raise Exception(f"Error getting data from Vetric. Status code = {response.status_code}")
            except Exception as e:
                logging.error(f'Error in getting tweets: {e}')
                logging.debug(f'Trying after {delay}')
                time.sleep(delay)
                delay *= self.backoff_multiplier
        raise Exception("Exceeded maximum number of retries")
