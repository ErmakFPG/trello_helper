from pymongo import MongoClient
from pymongo import uri_parser


class TrelloTasksStorage:
    def __init__(self, connection_string):
        db_name = uri_parser.parse_uri(connection_string)['database']
        self.client = MongoClient(connection_string)
        self.db = self.client[db_name]
        self.tasks_db = self.db.tasks_db
        self.collect_item_db = self.db.collect_item_db

    def save_tasks(self, tasks):
        self.tasks_db.insert_one(tasks)

    def get_tasks(self):
        return [el for el in self.tasks_db.find()]
