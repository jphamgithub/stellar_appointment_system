#!/bin/bash
# 🚀 Run both Scheduler and Flask API for the Stellar Appointment System

# Set default ports if not provided
API_PORT=${API_PORT:-5678}  # Default to 5678 if not set
ZMQ_PORT=${ZMQ_PORT:-5555}  # Default to 5555 if not set

# Initialize the SQLite database if needed
echo "Initializing the database..."
python3 -c "import database; database.init_db()"

# Start the Scheduler microservice in the background with a configurable port
echo "Starting Scheduler on port $ZMQ_PORT..."
ZMQ_PORT=$ZMQ_PORT python3 scheduler.py &

# Capture Scheduler Process ID (PID)
SCHEDULER_PID=$!
echo "Scheduler running with PID: $SCHEDULER_PID"

# Start the Flask API microservice in the background with a configurable port
echo "Starting Flask API on port $API_PORT..."
API_PORT=$API_PORT ZMQ_PORT=$ZMQ_PORT python3 api.py &

# Capture Flask API Process ID (PID)
API_PID=$!
echo "API running with PID: $API_PID"

# Display running status
echo "Both services are running in the background."
echo "Use the following commands to stop them:"
echo "kill $SCHEDULER_PID  # To stop the Scheduler"
echo "kill $API_PID        # To stop the Flask API"

# Wait for both processes to complete
wait $SCHEDULER_PID
wait $API_PID
