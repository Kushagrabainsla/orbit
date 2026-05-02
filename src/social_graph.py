from database import Database

class SocialGraph:
    def __init__(self, db: Database):
        self.db = db

    def follow(self, follower, followee):
        self.db.follow_user(follower, followee)

    def unfollow(self, follower, followee):
        self.db.unfollow_user(follower, followee)

    def view_connections(self, username):
        following = self.db.get_following(username)
        followers = self.db.get_followers(username)
        return {"following": following, "followers": followers}

    def mutual_connections(self, user1, user2):
        return self.db.get_mutual_connections(user1, user2)

    def friend_recommendations(self, username):
        return self.db.recommend_friends(username)