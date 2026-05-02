# Testing the Orbit Social Network

## Prerequisites
- Neo4j installed and running.
- Virtual environment activated (optional, but recommended).
- Data loaded (automatic on first run).

## Running Tests
To fix import issues, run from the src directory:
`cd src && python3 -m pytest ../tests/ -v`

Or add src to PYTHONPATH:
`PYTHONPATH=src python3 -m pytest tests/ -v`

## Manual Testing
1. Start the system: `./manage_system.sh start`
2. Run the app: `python src/main.py`
3. Register a user: Choose 1, enter details.
4. Login: Choose 2, enter credentials.
5. Test use cases:
   - View profile: 1
   - Edit profile: 2
   - Follow: 3, enter username
   - Unfollow: 4
   - View connections: 5
   - Mutual: 6, enter other user
   - Recommendations: 7
   - Search: 8, enter query
   - Popular: 9
   - Logout: 10

## Expected Outputs
- Screenshots can be taken from the terminal for the report.

## Stopping
`./manage_system.sh stop`