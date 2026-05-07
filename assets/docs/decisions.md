# Design Decisions and Reasonings

## Language Choice: Python
- **Reasoning**: Python is simpler for rapid development and console applications. It has excellent libraries for Neo4j integration. Java would require more boilerplate, but Python aligns with Clean Code's simplicity principle. Since the front-end is console-based, Python's readability is advantageous.

## Architecture: Modular Design
- **Reasoning**: Following Clean Code, each module has a single responsibility. `user_manager.py` handles user operations, `social_graph.py` manages relationships, etc. This makes the code easy to understand, test, and maintain.

## Database: Neo4j
- **Reasoning**: As specified, Neo4j is ideal for graph-based social networks. Cypher queries are used for all operations to leverage graph traversal efficiently.

## Dataset: Facebook Combined from SNAP
- **Reasoning**: Public dataset from Stanford SNAP (https://snap.stanford.edu/data/facebook_combined.txt.gz). It has 4,039 nodes and 88,234 edges, exceeding the minimum requirements. Real data provides better testing than synthetic.

## Data Loading
- **Reasoning**: Load users as nodes with properties (id, name). Relationships as FOLLOWS edges. Used Cypher MERGE to avoid duplicates.

## Use Case Implementation
- **Reasoning**: Each UC is a method in the appropriate module. Authentication is simple (no hashing for demo, but in production, use bcrypt). Queries use Cypher for efficiency.

## Front-end: Console Menu
- **Reasoning**: Simple, sufficient for requirements. Uses input() for interaction. Keeps it clean and focused.

## Testing: Unit Tests
- **Reasoning**: Basic tests for key functions. Ensures modularity and reliability.

## Folder Structure
- **Reasoning**: Standard Python project layout. `src/` for code, `data/` for assets, `docs/` for docs, `tests/` for tests. Easy to understand and submit.

## Clean Code Principles Applied
- **Meaningful Names**: Variables and functions named clearly (e.g., `create_user` not `cu`).
- **Single Responsibility**: Each function does one thing.
- **DRY**: No code duplication.
- **Comments**: Only where necessary, code is self-documenting.
- **Error Handling**: Basic try-except for database operations.

## Security Considerations
- **Reasoning**: Passwords stored in plain text for demo. In real app, hash them. No input validation beyond basic, but added some.

## Scalability
- **Reasoning**: Queries are efficient, but for large graphs, consider indexing. Dataset is manageable.

## Submission
- **Reasoning**: Folder structure allows easy zipping. Report in markdown for easy conversion to PDF.