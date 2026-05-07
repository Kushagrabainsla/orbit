# Team Tasks - Group Submission

**Due:** May 8 by 11:59pm  
**Points:** 70  
**Submitting:** a file upload  
**Available:** Feb 23 at 12am - May 10 at 11:59pm

## II. Team Tasks

### Overview
In this project, your team will design and develop a basic social networking application using Java (or Python) for the front end and Neo4j as the database. The system will model relationships between users, enabling social interactions such as following others, recommending connections, and efficiently querying networks using graph-based techniques. This project will give your team hands-on experience with graph databases, Java (Python)-based front-end development, and working with real-world datasets. This team project is separate from individual tasks, meaning it will have its own data modeling, use cases, and dataset, independent of those used in individual assignments.

### Requirements
- **Front-End:** Implemented in Java (or Python), providing an interactive interface for users to explore the social network. The console interface is sufficient.
- **Back-End:** Built using Neo4j, a graph database optimized for relationship-heavy data.
- **Data Source and Size:** The application should utilize a public dataset (e.g., datasets from SNAP, Kaggle, or other open data repositories) to populate the social network.
  - The required dataset size is at least 1,000 nodes and 5,000 relationships. If your chosen public dataset is smaller than this, you may expand it by generating additional synthetic data to meet the recommended size.

#### The following 11 Use Cases:

1. **User Management**
   - **UC-1: User Registration:** A new user can sign up by providing basic details (name, email, username, password). The system stores user data in Neo4j as nodes.
   - **UC-2: User Login:** A registered user can log in using their username and password. The system authenticates the credentials and grants access.
   - **UC-3: View Profile:** A user can view their own profile and update basic information.
   - **UC-4: Edit Profile:** A user can update their name, bio, and other details.

2. **Social Graph Features**
   - **UC-5: Follow Another User:** A user can follow another user, creating a "FOLLOWS" relationship in Neo4j. The relationship is stored as an edge in the graph database.
   - **UC-6: Unfollow a User:** A user can unfollow another user, removing the "FOLLOWS" relationship.
   - **UC-7: View Friends/Connections:** A user can see a list of people they are following and who follow them. You should keep "following" and "followers" separate.
   - **UC-8: Mutual Connections:** A user can see mutual friends (users followed by both parties).
   - **UC-9: Friend Recommendations:** The system suggests new people to follow based on common connections using graph traversal queries. You follow A, A follows B, then recommend B.

3. **Search & Exploration**
   - **UC-10: Search Users:** A user can search for other users by name or username. The system returns a list of matching users.
   - **UC-11: Explore Popular Users:** The system displays the most-followed users.

### Team Task Deliverables (Total: 70 points)
**Per team:** Submit `projects.zip`, which includes `report.pdf` and a folder holding all source codes.

#### report.pdf includes:
- **Team Info**
  - Member names and emails
- **Property Graph Schema** (5 points)
- **Dataset Information** (5 points)
  - Name and URL of the dataset
  - Brief description of the dataset
  - Explanation of how the raw data was processed and loaded into the database
  - Cypher statements used to create the data in the database
- **Use Case Evidence** (11 use cases x 5 points = 55 points)
  - 11 screenshots demonstrating the successful implementation of 11 use cases
  - Screenshots should be taken from the high-level interface (e.g., Java or Python Console)
  - Include the Cypher query (or queries) associated with each use case
  - Clearly label each screenshot for clarity

#### A folder that includes all source codes.