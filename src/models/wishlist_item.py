import uuid
from src.models.priority import Priority


class WishlistItem:
    def __init__(self, price: int, description: str, name: str, priority: Priority):
        self.id = uuid()
        self.name = name
        self.price = price
        self.description = description
        self.priority = priority

    def validate() -> bool:
        pass
