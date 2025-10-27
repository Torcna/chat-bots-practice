from abc import ABC, abstractmethod


class Handler(ABC):
    @abstractmethod
    def can_handle(self, update: dict) -> bool: ...

    @abstractmethod
    def handle(self, update: dict) -> bool:
        """
        returns True if this handler is NOT the last one
        returns False if further processing is needed
        """

        pass
