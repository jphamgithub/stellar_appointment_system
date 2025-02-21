#!/bin/bash
# 🚀 Run both Scheduler and Flask API for the Stellar Appointment System

# Initialize the SQLite database if needed
echo "Initializing the database..."
python3 -c "import database; database.init_db()"

# Start the Scheduler microservice in the background
echo "Starting Scheduler..."
python3 scheduler.py &

# Capture Scheduler Process ID (PID)
SCHEDULER_PID=$!
echo "Scheduler running with PID: $SCHEDULER_PID"

# Start the Flask API microservice in the background
echo "Starting Flask API..."
python3 api.py &

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
