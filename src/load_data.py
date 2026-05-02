import os
from database import Database
from tqdm import tqdm

def load_facebook_data(db: Database):
    file_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'facebook_combined.txt')
    with open(file_path, 'r') as f:
        lines = f.readlines()
    
    total_lines = len(lines)
    with tqdm(total=total_lines, desc="Loading data") as pbar:
        for line in lines:
            parts = line.strip().split()
            if len(parts) == 2:
                user1, user2 = parts
                # Create users if not exist
                db.run_query("MERGE (u:User {username: $id})", {"id": user1})
                db.run_query("MERGE (u:User {username: $id})", {"id": user2})
                # Create follows
                db.follow_user(user1, user2)
            pbar.update(1)

if __name__ == "__main__":
    db = Database()
    load_facebook_data(db)
    db.close()
    print("Data loaded successfully.")