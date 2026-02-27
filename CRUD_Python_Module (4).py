from pymongo import MongoClient
from pymongo.errors import PyMongoError


class AnimalShelter:
    """CRUD class for the AAC database animals collection."""

    def __init__(self, username, password, host="localhost", port=27017):
        # Connect using the aacuser credentials (required by the project)
        uri = f"mongodb://{username}:{password}@{host}:{port}/?authSource=admin"
        self.client = MongoClient(uri)

        # Database + collection used in this course project
        self.database = self.client["aac"]
        self.collection = self.database["animals"]

    def create(self, data):
        """Insert a single document."""
        if data is None or len(data) == 0:
            return False
        try:
            self.collection.insert_one(data)
            return True
        except PyMongoError:
            return False

    def read(self, query, projection=None):
        """
        Read documents from MongoDB.
        - query: dictionary ({} returns all documents)
        - projection: dictionary to include/exclude fields, ex: {"_id": 0}
        Returns: list of dictionaries
        """
        if query is None:
            return []
        try:
            cursor = self.collection.find(query, projection)
            return list(cursor)
        except PyMongoError:
            return []

    def update(self, query, new_values):
        """Update documents that match query."""
        if query is None or new_values is None:
            return 0
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except PyMongoError:
            return 0

    def delete(self, query):
        """Delete documents that match query."""
        if query is None:
            return 0
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except PyMongoError:
            return 0