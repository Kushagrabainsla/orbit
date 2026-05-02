#!/bin/bash
# Manage the Orbit Social Network system
# Usage: ./manage_system.sh start|stop

if [ "$1" == "start" ]; then
    echo "Starting Neo4j..."
    brew services start neo4j
    echo "Waiting for Neo4j to start..."
    sleep 10
    echo "System started. Run 'python src/main.py' to start the app."
elif [ "$1" == "stop" ]; then
    echo "Stopping Neo4j..."
    brew services stop neo4j
    echo "System stopped."
else
    echo "Usage: $0 start|stop"
    exit 1
fi