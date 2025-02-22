"""
@file test_client.py
@brief A test client for interacting with the Stellar Appointment System microservice.

This script demonstrates how to send requests and receive responses from the microservice using HTTP requests.
It shows examples for scheduling, canceling, and viewing appointments (both today's and all appointments).
"""

import requests
import json

# Base URL for the Flask API
BASE_URL = "http://localhost:5000"

def pretty_print(response):
    """
    @brief Prints a formatted JSON response.
    @param response: The JSON response object from the microservice.
    """
    print(json.dumps(response, indent=4))


def schedule_appointment(patient, date, time):
    """
    @brief Sends a request to schedule an appointment.
    
    @param patient: Name of the patient.
    @param date: Date of the appointment (YYYY-MM-DD).
    @param time: Time of the appointment (HH:MM format).
    
    @return: Response from the microservice.
    """
    payload = {
        "patient": patient,
        "date": date,
        "time": time
    }
    # CALL OUT!!!
    # 01 - Send a POST request to the Flask API with appointment details
    response = requests.post(f"{BASE_URL}/schedule", json=payload)
    return response.json()


def cancel_appointment(appointment_id):
    """
    @brief Sends a request to cancel an appointment using its ID.
    
    @param appointment_id: Unique ID of the appointment to be canceled.
    
    @return: Response from the microservice.
    """
    payload = {
        "appointment_id": appointment_id
    }
    response = requests.post(f"{BASE_URL}/cancel", json=payload)
    return response.json()


def view_todays_appointments():
    """
    @brief Requests a list of today's scheduled appointments.
    
    @return: List of today's appointments.
    """
    response = requests.get(f"{BASE_URL}/view_today")
    return response.json()


def view_all_appointments():
    """
    @brief Requests a list of all scheduled appointments.
    
    @return: List of all appointments.
    """
    response = requests.get(f"{BASE_URL}/view_all")
    return response.json()


if __name__ == "__main__":
    # Demonstrate scheduling an appointment
    print("Scheduling an appointment for John Doe on 2025-02-25 at 10:00 AM")
    # CALL OUT!!!
    # 00 - Declare a variable and call a function to schedule appointment 
    # You will build something like this in your code base!
    scheduled_response = schedule_appointment("John Doe", "2025-02-25", "10:00")
    # CALL OUT!!!
    # 07 - Display the response received from the API to confirm success
    pretty_print(scheduled_response)

    # Demonstrate viewing today's appointments
    print("\nViewing today's appointments:")
    today_appointments = view_todays_appointments()
    pretty_print(today_appointments)

    # Demonstrate viewing all appointments
    print("\nViewing all scheduled appointments:")
    all_appointments = view_all_appointments()
    pretty_print(all_appointments)

    # Demonstrate canceling an appointment (using ID from scheduled appointment)
    if 'appointment_id' in scheduled_response:
        appointment_id = scheduled_response['appointment_id']
        print(f"\n Canceling appointment with ID {appointment_id}")
        cancel_response = cancel_appointment(appointment_id)
        pretty_print(cancel_response)

    # Confirm all appointments after cancellation
    print("\nViewing all appointments after cancellation:")
    updated_appointments = view_all_appointments()
    pretty_print(updated_appointments)
