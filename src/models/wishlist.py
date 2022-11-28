from typing import List
from src.models.wishlist import Wishlist
from src.models.wishlist_item import WishlistItem


class Wishlist:
    def __init__(self, wishlist: List[WishlistItem]):
        self.wishlist = wishlist

    def add_item(self, item: WishlistItem):
        self.wishlist.append(item)
    
    def remove_item(self, id: int):
        pass

    def validate(self) -> bool:
        pass
