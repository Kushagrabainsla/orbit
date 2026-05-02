from database import Database

class Search:
    def __init__(self, db: Database):
        self.db = db

    def search_users(self, query):
        return self.db.search_users(query)

    def explore_popular(self):
        return self.db.get_popular_users()