# Read/Write Monitor Dashboard

This project provides a simple monitoring system to track and visualize the number of **read** and **write** operations performed by different applications. It includes collectors for gathering events, a storage layer for persistence, and a dashboard for visualization.

---

## Features

* **Collectors**

  * **File Collector** – Monitors file read/write operations.
  * **Database Collector** – Wraps around DB queries and logs operations.
  * **API Collector** – Provides an endpoint to log external read/write operations.

* **Storage Layer**

  * SQLite database for event storage.
  * SQLAlchemy ORM for managing models.

* **Dashboard**

  * Built with Streamlit for interactive visualization.
  * Provides charts for operation counts, application-wise statistics, and trends over time.

---

## Project Structure

```
readwrite-monitor-dashboard/
│── main.py              # Entry point: starts collectors and dashboard
│── requirements.txt     # Python dependencies
│── config.py            # Configuration (DB path, ports, etc.)
│
├── collector/
│   │── __init__.py
│   │── base_collector.py
│   │── file_collector.py
│   │── db_collector.py
│   │── api_collector.py
│
├── storage/
│   │── __init__.py
│   │── models.py        # SQLAlchemy models
│   │── db.py            # DB initialization and session handling
│
└── dashboard/
    │── __init__.py
    │── app.py           # Streamlit dashboard
    │── charts.py        # Chart utilities
```
---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/readwrite-monitor-dashboard.git
cd readwrite-monitor-dashboard
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Initialize the database:

```bash
python -m storage.db
```

---

## Running the Project

Start the main service (collectors + dashboard):

```bash
python main.py
```

By default:

* API runs on `http://127.0.0.1:6000`
* Dashboard runs on `http://localhost:8501`

---

## Usage

* Use the **FileCollector** to monitor file activities.
* Use the **DBCollector** to wrap database queries.
* Send logs to the **APICollector** from external apps.
* Open the **Streamlit dashboard** to view real-time statistics.

---

## Tech Stack

* **Python**
* **Flask** (API)
* **Streamlit** (Dashboard)
* **SQLAlchemy + SQLite** (Storage)
* **Watchdog** (File monitoring)

---

## Future Improvements

* Cloud storage collectors (AWS S3, GCP, Azure).
* Authentication and role-based access for dashboard.
* Export reports (CSV, Excel, PDF).
* WebSocket support for real-time streaming.

---

## Author

Developed by Shreeja Karajagi, Nachikaet Anoop, and E. Saaruvathani.
For contributions, open an issue or submit a pull request.