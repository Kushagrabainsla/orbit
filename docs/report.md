# Report for Orbit Social Network

## Team Info
- Kushagra Bainsla (kushagra.bainsla@sjsu.edu)
- Kevin Ha (kevin.k.ha@sjsu.edu)
- Prudhvi Sai Raj Dasari

## Property Graph Schema
- Nodes: User {username, name, email, password, bio}
- Relationships: FOLLOWS (directed)

## Dataset Information
- Name: Facebook Combined
- URL: https://snap.stanford.edu/data/facebook_combined.txt.gz
- Description: Anonymized Facebook social network data, representing friendships.
- Processing: Downloaded and unzipped. Loaded as users with IDs as usernames, relationships as FOLLOWS.
- Cypher: MERGE for nodes, CREATE for edges.

## Use Case Evidence
For each UC, screenshot would show console output and Cypher query.

1. UC-1: Register - Console shows input fields, success message. Cypher: MERGE (u:User {username: $username}) ON CREATE SET ...
2. UC-2: Login - Input username/password, success. Cypher: MATCH (u:User {username: $username, password: $password})
3. UC-3: View Profile - Displays user info. Cypher: MATCH (u:User {username: $username}) RETURN u
4. UC-4: Edit Profile - Updates fields. Cypher: MATCH (u:User {username: $username}) SET u.name = ...
5. UC-5: Follow - Creates relationship. Cypher: MERGE (f)-[:FOLLOWS]->(e)
6. UC-6: Unfollow - Deletes relationship. Cypher: MATCH (f)-[r:FOLLOWS]->(e) DELETE r
7. UC-7: View Connections - Lists following/followers. Cypher: MATCH (u)-[:FOLLOWS]->(f) RETURN f.username
8. UC-8: Mutual - Lists common. Cypher: MATCH (u1)-[:FOLLOWS]->(m)-[:FOLLOWS]->(u2)
9. UC-9: Recommendations - Suggests based on friends of friends. Cypher: MATCH (u)-[:FOLLOWS]->()-[:FOLLOWS]->(rec)
10. UC-10: Search - Returns matching users. Cypher: MATCH (u:User) WHERE u.name CONTAINS $query
11. UC-11: Popular - Top followed. Cypher: MATCH (u)<-[:FOLLOWS]-() RETURN u.username, COUNT(*) ORDER BY DESC