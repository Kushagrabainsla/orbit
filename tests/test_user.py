import unittest
from database import Database
from user_manager import UserManager

class TestUserManager(unittest.TestCase):
    def setUp(self):
        self.db = Database()
        self.um = UserManager(self.db)

    def test_register(self):
        self.um.register_user("Test User", "test@example.com", "testuser", "pass")
        user = self.um.view_profile("testuser")
        self.assertIsNotNone(user)

    def tearDown(self):
        self.db.run_query("MATCH (u:User {username: 'testuser'}) DETACH DELETE u")
        self.db.close()

if __name__ == "__main__":
    unittest.main()