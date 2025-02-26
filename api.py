"""
 * @file api.py
 * @brief Flask API to interact with the appointment microservice via HTTP requests.
""" 

from flask import Flask, request, jsonify
import zmq
import json

# Initialize Flask app
app = Flask(__name__)

# Setup ZeroMQ client for communication with the microservice
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

@app.route('/schedule', methods=['POST'])
def schedule():
    """
    @brief Schedules a new appointment.

    This endpoint accepts patient details including name, date, and time to schedule an appointment.
    
    @return JSON response containing the status of the request and the appointment ID if successful.

    Example request:
    {
        "patient": "John Doe",
        "date": "2025-02-10",
        "time": "14:30"
    }
    """
    data = request.get_json()
    print("Received data:", data) #debug
    if not data or not all(k in data for k in ('patient', 'date', 'time')):
        return jsonify({'status': 'error', 'message': 'Missing required fields.'}), 400

    request_data = {
        "action": "schedule",
        "p_id": data['p_id'],
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

if __name__ == '__main__':
    """
    @brief Starts the Flask API server.

    The server runs on host 0.0.0.0 and port 5000 by default.
    """
    app.run(host='0.0.0.0', port=5678)

