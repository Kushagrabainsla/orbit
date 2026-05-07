# Orbit Social Network

This project implements a basic social networking application using Python for the front-end and Neo4j for the back-end, following Clean Code principles by Robert C. Martin.

## Project Structure

- `src/`: Source code
  - `main.py`: Entry point
  - `user_manager.py`: User management logic
  - `social_graph.py`: Social graph operations
  - `search.py`: Search and exploration features
  - `database.py`: Neo4j connection and utilities
  - `load_data.py`: Dataset loading script
- `data/`: Dataset files (Facebook Combined)
- `tests/`: Unit tests
- `docs/`: Documentation
  - `README.md`: This file
  - `desc.md`: Project description
  - `decisions.md`: Design decisions and reasonings
  - `report.md`: Report content for PDF generation
  - `TESTING.md`: Testing instructions
  - `TODO.md`: Task list
- `manage_system.sh`: Script to start/stop Neo4j
- `requirements.txt`: Python dependencies

## Setup

1. Install Neo4j: `brew install neo4j` (or download Neo4j Desktop/Server)
2. Start Neo4j for the first time: `./manage_system.sh start`
3. Set up a Python virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux; use venv\Scripts\activate on Windows
   ```
4. Set the initial Neo4j password:
   - Open http://localhost:7474 in your browser
   - Log in with username: neo4j, password: neo4j
   - Follow prompts to set a new password (e.g., orbit123)
   - It's tied to the local Neo4j installation, not the project code—so each fresh setup (e.g., on a new machine or after reinstalling Neo4j) requires it.
5. Install Python dependencies: `pip install -r requirements.txt`

## Running

Activate the virtual environment if using one: `source venv/bin/activate`

`python src/main.py`

The app will automatically check and load the dataset on first run.

## Testing

See `docs/TESTING.md` for testing instructions.

## Decisions

See `docs/decisions.md` for detailed reasonings.