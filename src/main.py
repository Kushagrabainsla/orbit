from database import Database
from user_manager import UserManager
from social_graph import SocialGraph
from search import Search
from load_data import load_facebook_data

class SocialNetworkApp:
    def __init__(self):
        self.db = Database()
        self.user_manager = UserManager(self.db)
        self.social_graph = SocialGraph(self.db)
        self.search = Search(self.db)
        self.current_user = None

    def check_and_load_data(self):
        # Check if data is loaded by counting nodes
        result = self.db.run_query("MATCH (u:User) RETURN count(u) as count")
        count = result[0]['count'] if result else 0
        if count == 0:
            print("Data not loaded. Loading data...")
            load_facebook_data(self.db)
            print("Data loaded successfully.")
        else:
            print("Data already loaded.")

    def run(self):
        self.check_and_load_data()
        while True:
            if not self.current_user:
                self.show_main_menu()
            else:
                self.show_user_menu()

    def show_main_menu(self):
        print("\n=== Orbit Social Network ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose: ")
        if choice == "1":
            self.register()
        elif choice == "2":
            self.login()
        elif choice == "3":
            self.db.close()
            exit()

    def show_user_menu(self):
        print(f"\nLogged in as {self.current_user['username']}")
        print("1. View Profile")
        print("2. Edit Profile")
        print("3. Follow User")
        print("4. Unfollow User")
        print("5. View Connections")
        print("6. Mutual Connections")
        print("7. Friend Recommendations")
        print("8. Search Users")
        print("9. Explore Popular")
        print("10. Logout")
        choice = input("Choose: ")
        if choice == "1":
            self.view_profile()
        elif choice == "2":
            self.edit_profile()
        elif choice == "3":
            self.follow_user()
        elif choice == "4":
            self.unfollow_user()
        elif choice == "5":
            self.view_connections()
        elif choice == "6":
            self.mutual_connections()
        elif choice == "7":
            self.friend_recommendations()
        elif choice == "8":
            self.search_users()
        elif choice == "9":
            self.explore_popular()
        elif choice == "10":
            self.current_user = None

    def register(self):
        name = input("Name: ")
        email = input("Email: ")
        username = input("Username: ")
        password = input("Password: ")
        try:
            self.user_manager.register_user(name, email, username, password)
            print("Registered successfully!")
        except ValueError as e:
            print(f"Error: {e}")

    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        user = self.user_manager.login_user(username, password)
        if user:
            self.current_user = dict(user['u'])
            print("Logged in!")
        else:
            print("Invalid credentials")

    def view_profile(self):
        profile = self.user_manager.view_profile(self.current_user['username'])
        if profile:
            print(f"Name: {profile['u']['name']}")
            print(f"Email: {profile['u']['email']}")
            print(f"Bio: {profile['u'].get('bio', 'N/A')}")

    def edit_profile(self):
        name = input("New name (leave blank to skip): ")
        bio = input("New bio (leave blank to skip): ")
        self.user_manager.edit_profile(self.current_user['username'], name or None, bio or None)
        print("Profile updated!")

    def follow_user(self):
        username = input("Username to follow: ")
        self.social_graph.follow(self.current_user['username'], username)
        print("Followed!")

    def unfollow_user(self):
        username = input("Username to unfollow: ")
        self.social_graph.unfollow(self.current_user['username'], username)
        print("Unfollowed!")

    def view_connections(self):
        connections = self.social_graph.view_connections(self.current_user['username'])
        print("Following:", connections['following'])
        print("Followers:", connections['followers'])

    def mutual_connections(self):
        user2 = input("Other username: ")
        mutual = self.social_graph.mutual_connections(self.current_user['username'], user2)
        print("Mutual connections:", mutual)

    def friend_recommendations(self):
        recs = self.social_graph.friend_recommendations(self.current_user['username'])
        print("Recommendations:", recs)

    def search_users(self):
        query = input("Search query: ")
        results = self.search.search_users(query)
        print("Results:", results)

    def explore_popular(self):
        popular = self.search.explore_popular()
        print("Popular users:", popular)

if __name__ == "__main__":
    app = SocialNetworkApp()
    app.run()