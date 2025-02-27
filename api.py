"""
 * @file api.py
 * @brief Flask API to interact with the appointment microservice via HTTP requests.
""" 

from flask import Flask, request, jsonify
import zmq
import json
import os

# Initialize Flask app
app = Flask(__name__)

ZMQ_PORT = os.getenv("ZMQ_PORT", "5555")  # Default to 5555 if not set

# Setup ZeroMQ client for communication with the microservice
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect(f"tcp://localhost:{ZMQ_PORT}")  # Use the configured port

@app.route('/schedule', methods=['POST'])
def schedule():
    """
    @brief Schedules a new appointment.

    This endpoint accepts patient details including patient ID, name, date, and time.

    @return JSON response containing the status of the request and the appointment ID if successful.
    """
    data = request.get_json()
    if not data or not all(k in data for k in ('p_id', 'patient', 'date', 'time')):
        return jsonify({'status': 'error', 'message': 'Missing required fields.'}), 400

    request_data = {
        "action": "schedule",
        "p_id": data['p_id'],  # Ensure patient ID is included
        "patient": data['patient'],
        "date": data['date'],
        "time": data['time']
    }
    # CALL OUT!!!
    # 02 - Send the request data to the scheduler microservice using ZeroMQ
    socket.send_string(json.dumps(request_data))
    
    # CALL OUT!!!
    # 06 - Receive the response from scheduler.py and send it back as JSON
    response = json.loads(socket.recv_string())
    return jsonify(response)

@app.route('/cancel', methods=['POST'])
def cancel():
    """
    @brief Cancels an existing appointment.

    This endpoint requires an appointment ID to cancel a scheduled appointment.

    @return JSON response indicating success or failure of the cancellation.

    Example request:
    {
        "appointment_id": 123
    }
    """
    data = request.get_json()
    if not data or 'appointment_id' not in data:
        return jsonify({'status': 'error', 'message': 'Missing appointment ID.'}), 400

    request_data = {
        "action": "cancel",
        "appointment_id": data['appointment_id']
    }
    socket.send_string(json.dumps(request_data))
    response = json.loads(socket.recv_string())
    return jsonify(response)

@app.route('/view_today', methods=['GET'])
def view_today():
    """
    @brief Retrieves all appointments scheduled for today.

    This endpoint does not require any parameters.

    @return JSON response with a list of today's appointments.
    """
    request_data = {"action": "view_today"}
    socket.send_string(json.dumps(request_data))
    response = json.loads(socket.recv_string())
    return jsonify(response)

@app.route('/view_all', methods=['GET'])
def view_all():
    """
    @brief Retrieves all scheduled appointments.

    @return JSON response with a list of all appointments.
    """
    request_data = {"action": "view_all"}
    socket.send_string(json.dumps(request_data))
    response = json.loads(socket.recv_string())
    return jsonify(response)

# Make sure this is left at the bottom if you add more routes!!

import os

if __name__ == '__main__':
    """
    @brief Starts the Flask API server with a customizable port.

    By default, the server runs on port 5678, but it can be overridden using an environment variable
    or command-line argument.
    """
    port = int(os.getenv("API_PORT", 5678))  # Get port from environment variable, default to 5678
    app.run(host='0.0.0.0', port=port)


