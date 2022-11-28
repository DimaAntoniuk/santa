from typing import List
from src.models.wishlist_item import WishlistItem
from src.models.wishlist import Wishlist
from src.models.status import Status


class User:
    def __init__(self, name, status: Status, wishlist: Wishlist):
        self.name = name
        self.status = status
        self.wishlist = wishlist
    
    def add_item_to_wishlist(self, *, kwargs):
        item = WishlistItem(**kwargs)
        self.wishlist.add_item(item)

    def remove_item_from_wishlist(self, ids: List[int]):
        for id in ids:
            self.wishlist.remove_item(id)

    def register(self):
        pass
