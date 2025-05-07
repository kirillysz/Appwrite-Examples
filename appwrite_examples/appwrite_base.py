from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.services.storage import Storage

from config import Config

class AppwriteBase:
    def __init__(self, client: Client, cfg: Config):
        self.client = client
        self.cfg = cfg

        self.client.set_endpoint(endpoint=self.cfg.ENDPOINT)
        self.client.set_project(value=self.cfg.PROJECT_ID)
        self.client.set_key(value=self.cfg.API_KEY)
        self.client.set_self_signed(True)

        self.db = Databases(client=self.client)
        self.storage = Storage(client=self.client)
