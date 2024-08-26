import os.path

import yaml


class AppConfig:
    def __init__(self):
        assert os.path.isfile('app.yaml')
        with open('app.yaml', 'r') as file:
            self.config = yaml.safe_load(file)

    def get_config(self):
        return self.config
