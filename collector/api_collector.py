# collector/api_collector.py

from flask import Flask, request, jsonify
from storage import db
from .base_collector import BaseCollector
import threading

class APICollector(BaseCollector):
    def __init__(self, host="0.0.0.0", port=5000):
        super().__init__("APICollector")
        self.host = host
        self.port = port
        self.app = Flask(__name__)

        @self.app.route("/log", methods=["POST"])
        def log_event():
            data = request.get_json()
            app = data.get("app", "unknown_app")
            operation = data.get("operation", "").lower()
            resource = data.get("resource", None)

            if operation not in ("read", "write"):
                return jsonify({"error": "Invalid operation"}), 400

            db.insert_event(app, operation, resource)
            return jsonify({"status": "success"}), 201

    def start(self):
        print(f"[APICollector] Running on http://{self.host}:{self.port}")
        thread = threading.Thread(
            target=self.app.run, kwargs={"host": self.host, "port": self.port}, daemon=True
        )
        thread.start()

    def stop(self):
        print("[APICollector] Flask server will stop when main program exits.")
