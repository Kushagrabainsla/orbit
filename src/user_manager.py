from database import Database

class UserManager:
    def __init__(self, db: Database):
        self.db = db

    def register_user(self, name, email, username, password):
        if not all([name, email, username, password]):
            raise ValueError("All fields are required")
        return self.db.create_user(name, email, username, password)

    def login_user(self, username, password):
        return self.db.authenticate_user(username, password)

    def view_profile(self, username):
        return self.db.get_user_profile(username)

    def edit_profile(self, username, name=None, bio=None):
        return self.db.update_user_profile(username, name, bio)