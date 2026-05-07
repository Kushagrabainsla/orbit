# Orbit Social Network - Submission Checklist

## Project Setup
- [x] Create project structure with src/, data/, docs/, tests/
- [x] Set up Python virtual environment
- [x] Install Neo4j database
- [x] Install Python dependencies (neo4j, tqdm, pytest)

## Code Implementation
- [x] Implement Database class for Neo4j connection
- [x] Implement UserManager for user operations
- [x] Implement SocialGraph for relationships
- [x] Implement Search for user discovery
- [x] Implement data loading with progress bar
- [x] Implement main app with console interface
- [x] Implement all 11 use cases:
  - [x] UC-1: User Registration
  - [x] UC-2: User Login
  - [x] UC-3: View Profile
  - [x] UC-4: Edit Profile
  - [x] UC-5: Follow User
  - [x] UC-6: Unfollow User
  - [x] UC-7: View Connections
  - [x] UC-8: Mutual Connections
  - [x] UC-9: Friend Recommendations
  - [x] UC-10: Search Users
  - [x] UC-11: Explore Popular Users

## Testing
- [x] Write basic unit tests
- [x] Test Neo4j connection
- [x] Verify dataset loading (4039 nodes, 88234 edges)

## Documentation
- [x] Write README.md with setup and usage
- [x] Write decisions.md with design reasoning
- [x] Write report.md with team info, schema, dataset, use cases
- [x] Write TESTING.md with test instructions
- [x] Organize all docs in docs/ directory
- [x] Update all docs for consistency

## Scripts and Configuration
- [x] Create manage_system.sh for start/stop
- [x] Add .gitignore for Python/Neo4j
- [x] Update requirements.txt with all dependencies

## Pre-Submission Tasks
- [ ] Take screenshots for all 11 use cases
- [ ] Embed screenshots in docs/report.md
- [ ] Convert docs/report.md to report.pdf using pandoc
- [ ] Final review of all files
- [ ] Create projects.zip containing:
  - src/ (source code)
  - data/ (dataset)
  - docs/ (documentation)
  - tests/ (unit tests)
  - manage_system.sh (start/stop script)
  - requirements.txt (dependencies)
  - report.pdf (generated report)
- [ ] Submit projects.zip and report.pdf