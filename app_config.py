import os.path

import yaml


class AppConfig:
    def __init__(self):
        assert os.path.isfile('app.yaml')
        self.config = yaml.load('app.yaml')

    def get_config(self):
        return self.config
