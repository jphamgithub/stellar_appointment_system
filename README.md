
# **Nova Clinic Scheduler**

Welcome to **Nova Clinic Scheduler**, a futuristic microservice for managing appointments across the galaxy. This service allows users to schedule, cancel, and view appointments with ease. Built with **ZeroMQ** for inter-process communication and **SQLite** for persistent data storage, it’s perfect for lightweight, scalable solutions.

---

## **Features**
- Schedule appointments with patient name, date, and time.
- Cancel existing appointments by ID.
- View all appointments for a given day.
- Lightweight and easy to set up using SQLite and Python.
- Uses JSON for request and response data.

---

## **File Structure**
```plaintext
nova_clinic_scheduler/
├── README.md               # Project documentation (this file)
├── scheduler.py            # Main microservice code (ZeroMQ server logic)
├── database.py             # SQLite database setup and interaction functions
├── client_example.py       # Example ZeroMQ client to send requests
├── schema.sql              # SQL script to initialize the SQLite database
├── requirements.txt        # Required Python dependencies
└── tests/
    ├── test_scheduler.py   # Unit tests for the microservice
    └── test_database.py    # Unit tests for SQLite database functions
```

---

## **Getting Started**

### **Prerequisites**
- Python 3.7 or later
- `pip` (Python package manager)

### **Install Dependencies**
Run the following command to install the required Python packages:
```bash
pip install -r requirements.txt
```

### **Dependencies**
The project relies on:
- **ZeroMQ**: For communication between the client and server (`pyzmq` package).
- **SQLite3**: A lightweight, embedded database (Python built-in library).

---

## **Setup**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/jphamgithub/stellar_appointment_system.git
   cd nova_clinic_scheduler
   ```

2. **Initialize the SQLite Database**:
   Run the `schema.sql` script to set up the database:
   ```bash
   python -c "import database; database.init_db()"
   ```

   Alternatively, execute the `schema.sql` file manually:
   ```bash
   sqlite3 appointments.db < schema.sql
   ```

3. **Start the Microservice**:
   Run the `scheduler.py` file to start the server:
   ```bash
   python scheduler.py
   ```

4. **Test the Microservice**:
   Use `client_example.py` to send requests to the server:
   ```bash
   python client_example.py
   ```

---

## **Usage**

### **ZeroMQ Communication**
The microservice uses ZeroMQ to communicate with clients. All requests must be sent in JSON format, and the server will respond with JSON.

### **Request Examples**
- **Schedule an Appointment**:
    ```json
    {
        "action": "schedule",
        "patient": "John Doe",
        "date": "2025-02-10",
        "time": "14:30"
    }
    ```

- **Cancel an Appointment**:
    ```json
    {
        "action": "cancel",
        "appointment_id": 123
    }
    ```

- **View Today’s Appointments**:
    ```json
    {
        "action": "view_today"
    }
    ```

### **Response Examples**
- **Schedule Response**:
    ```json
    {
        "status": "success",
        "appointment_id": 123
    }
    ```

- **Cancel Response**:
    ```json
    {
        "status": "success",
        "message": "Appointment 123 canceled."
    }
    ```

- **View Response**:
    ```json
    {
        "appointments": [
            {"id": 123, "patient": "John Doe", "time": "14:30"},
            {"id": 124, "patient": "Jane Smith", "time": "15:00"}
        ]
    }
    ```
