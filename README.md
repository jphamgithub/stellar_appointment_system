
# **Stellar Appointment System**

This is a simple microservice that lets you schedule, cancel, and view appointments. It uses **ZeroMQ** for communication and **SQLite** to store the data. The idea is to make a lightweight and easy-to-run system for handling appointments.

---

## **GitHub Repository**
Repo Link: [Stellar Appointment System](https://github.com/jphamgithub/stellar_appointment_system.git)
But you're here now?
---

## **What This Does**
- Lets you **schedule** an appointment by providing a name, date, and time.
- Lets you **cancel** an appointment by giving its ID.
- Lets you **view all** appointments for today.

It's all done through **ZeroMQ messages** instead of an API, so you need to send JSON requests.

---

## **How to Set It Up**

### **1. Install Python Stuff**
Make sure you have Python 3.7+ installed, then run:
```bash
pip install pyzmq sqlite3
```

### **2. Set Up the Database**
Run this to create the database file (`appointments.db`):
```bash
python -c "import database; database.init_db()"
```

### **3. Start the Microservice**
Run the server so it starts listening for appointment requests:
```bash
python scheduler.py
```

---

## **How to Send Requests**

### **Using Python (One-Liner Command)**
Instead of making an API call, you talk to the service through **ZeroMQ**. Here are some quick one-liners to test it:

#### **Schedule an Appointment**
```bash
python -c "import zmq, json; s=zmq.Context().socket(zmq.REQ); s.connect('tcp://localhost:5555'); s.send_string(json.dumps({'action': 'schedule', 'patient': 'John Doe', 'date': '2025-02-10', 'time': '14:30'})); print(s.recv_string())"
```

#### **Cancel an Appointment**
```bash
python -c "import zmq, json; s=zmq.Context().socket(zmq.REQ); s.connect('tcp://localhost:5555'); s.send_string(json.dumps({'action': 'cancel', 'appointment_id': 123})); print(s.recv_string())"
```

#### **View Today’s Appointments**
```bash
python -c "import zmq, json; s=zmq.Context().socket(zmq.REQ); s.connect('tcp://localhost:5555'); s.send_string(json.dumps({'action': 'view_today'})); print(s.recv_string())"
```

---

## **Future Enhancements (Maybe?)**
- Right now, it's just using **ZeroMQ**, but adding an **HTTP API** (like Flask or FastAPI) would make it easier to test with curl.
- Could add more features like rescheduling an appointment instead of just canceling.
- Maybe store more appointment details, like location or doctor name?

---

## **Repo Again**
📌 [Stellar Appointment System](https://github.com/jphamgithub/stellar_appointment_system.git)

---

That's it! Just run the server, send some messages, and you should see appointments being saved and retrieved. Let me know if you have any issues! 🚀
