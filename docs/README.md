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
2. Install Python dependencies: `pip install -r requirements.txt`
3. Start the system: `./manage_system.sh start`

## Running

`python src/main.py`

The app will automatically check and load the dataset on first run.

## Testing

See `docs/TESTING.md` for testing instructions.

## Decisions

See `docs/decisions.md` for detailed reasonings.