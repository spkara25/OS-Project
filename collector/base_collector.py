from abc import ABC, abstractmethod

class BaseCollector(ABC):
    """Abstract base class for all collectors."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass
