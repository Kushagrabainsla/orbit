from neo4j import GraphDatabase

class Database:
    def __init__(self, uri="bolt://localhost:7687", user="neo4j", password="password"):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.driver.session() as session:
            result = session.run(query, parameters or {})
            return [record for record in result]

    def create_user(self, name, email, username, password):
        query = """
        MERGE (u:User {username: $username})
        ON CREATE SET u.name = $name, u.email = $email, u.password = $password
        RETURN u
        """
        return self.run_query(query, {"name": name, "email": email, "username": username, "password": password})

    def authenticate_user(self, username, password):
        query = "MATCH (u:User {username: $username, password: $password}) RETURN u"
        result = self.run_query(query, {"username": username, "password": password})
        return result[0] if result else None

    def get_user_profile(self, username):
        query = "MATCH (u:User {username: $username}) RETURN u"
        result = self.run_query(query, {"username": username})
        return result[0] if result else None

    def update_user_profile(self, username, name=None, bio=None):
        query = "MATCH (u:User {username: $username}) SET u.name = COALESCE($name, u.name), u.bio = COALESCE($bio, u.bio) RETURN u"
        return self.run_query(query, {"username": username, "name": name, "bio": bio})

    def follow_user(self, follower_username, followee_username):
        query = """
        MATCH (f:User {username: $follower}), (e:User {username: $followee})
        MERGE (f)-[:FOLLOWS]->(e)
        """
        self.run_query(query, {"follower": follower_username, "followee": followee_username})

    def unfollow_user(self, follower_username, followee_username):
        query = """
        MATCH (f:User {username: $follower})-[r:FOLLOWS]->(e:User {username: $followee})
        DELETE r
        """
        self.run_query(query, {"follower": follower_username, "followee": followee_username})

    def get_following(self, username):
        query = "MATCH (u:User {username: $username})-[:FOLLOWS]->(f) RETURN f.username"
        return [r["f.username"] for r in self.run_query(query, {"username": username})]

    def get_followers(self, username):
        query = "MATCH (f)-[:FOLLOWS]->(u:User {username: $username}) RETURN f.username"
        return [r["f.username"] for r in self.run_query(query, {"username": username})]

    def get_mutual_connections(self, user1, user2):
        query = """
        MATCH (u1:User {username: $user1})-[:FOLLOWS]->(m:User)-[:FOLLOWS]->(u2:User {username: $user2})
        RETURN m.username
        """
        return [r["m.username"] for r in self.run_query(query, {"user1": user1, "user2": user2})]

    def recommend_friends(self, username):
        query = """
        MATCH (u:User {username: $username})-[:FOLLOWS]->()-[:FOLLOWS]->(rec:User)
        WHERE NOT (u)-[:FOLLOWS]->(rec) AND rec <> u
        RETURN rec.username, COUNT(*) as score ORDER BY score DESC LIMIT 10
        """
        return [r["rec.username"] for r in self.run_query(query, {"username": username})]

    def search_users(self, query_str):
        query = "MATCH (u:User) WHERE u.name CONTAINS $query OR u.username CONTAINS $query RETURN u.username"
        return [r["u.username"] for r in self.run_query(query, {"query": query_str})]

    def get_popular_users(self, limit=10):
        query = "MATCH (u:User)<-[:FOLLOWS]-() RETURN u.username, COUNT(*) as followers ORDER BY followers DESC LIMIT $limit"
        return [r["u.username"] for r in self.run_query(query, {"limit": limit})]