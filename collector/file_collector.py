# collector/file_collector.py

import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from storage import db
from .base_collector import BaseCollector

class FileEventHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            db.insert_event("filesystem", "write", event.src_path)

    def on_created(self, event):
        if not event.is_directory:
            db.insert_event("filesystem", "write", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            db.insert_event("filesystem", "write", event.src_path)

    def on_moved(self, event):
        if not event.is_directory:
            db.insert_event("filesystem", "write", event.dest_path)

class FileCollector(BaseCollector):
    def __init__(self, path: str):
        super().__init__("FileCollector")
        self.path = path
        self.event_handler = FileEventHandler()
        self.observer = Observer()

    def start(self):
        print(f"[FileCollector] Monitoring started at: {self.path}")
        self.observer.schedule(self.event_handler, self.path, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.stop()

    def stop(self):
        print("[FileCollector] Stopping...")
        self.observer.stop()
        self.observer.join()
