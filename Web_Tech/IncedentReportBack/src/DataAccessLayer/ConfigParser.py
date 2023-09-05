import configparser as cfg
import os


class ConfigParser:
    def __init__(self):
        self.config = cfg.ConfigParser()
        self.path = '/'.join((os.path.abspath(__file__).replace('\\', '/')).split('/')[:-1])
        self.config.read(os.path.join(self.path, 'config.ini'))
        self.URI = self.config['MongoDB']['uri']
        self.db = self.config['MongoDB']['db']
        self.collection = self.config['MongoDB']['collection']

    def get_uri(self):
        return self.URI

    def get_db(self):
        return self.db

    def get_collection(self):
        return self.collection



