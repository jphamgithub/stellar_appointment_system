
# Stellar Appointment System

This is a simple microservice that lets you schedule, cancel, and view appointments. It uses **ZeroMQ** for communication and **SQLite** to store the data. The goal is to provide a lightweight and easy-to-run system for handling appointments.

---

## GitHub Repository
Repo Link: [Stellar Appointment System](https://github.com/jphamgithub/stellar_appointment_system.git)

---

## What This Does
- Lets you **schedule** an appointment by providing a name, date, and time.
- Lets you **cancel** an appointment by giving its ID.
- Lets you **view all** appointments for today.

It's all done through **ZeroMQ messages** instead of an API, so you need to send JSON requests.

---

## How to Set It Up

### 1. Install Required Packages
Make sure you have Python 3.7+ installed, then run:
```bash
pip install pyzmq sqlite3
```

### 2. Set Up the Database
Run this to create the database file (`appointments.db`):
```bash
python -c "import database; database.init_db()"
```

### 3. Start the Microservice
Run the server so it starts listening for appointment requests:
```bash
python scheduler.py
```

---

## How to Send Requests

Instead of using long one-liner commands, use `client.py` to simplify sending requests.

### 1. Schedule an Appointment
```bash
python client.py schedule "John Doe" "2025-02-10" "14:30"
```

### 2. Cancel an Appointment
```bash
python client.py cancel 123
```

### 3. View Today’s Appointments
```bash
python client.py view_today
```

This approach makes it easier for users to interact with the microservice without having to construct long JSON messages manually.

---

## Future Enhancements
- Currently, the system uses **ZeroMQ**. Adding an **HTTP API** (like Flask or FastAPI) would allow easier testing with curl.
- Additional features such as rescheduling appointments could be added.
- Expanding stored appointment details, such as location or assigned personnel.

---

## Repository
Repo Link: [Stellar Appointment System](https://github.com/jphamgithub/stellar_appointment_system.git)

---

This project is designed to be simple and efficient. Run the server, send requests through `client.py`, and manage appointments easily.
