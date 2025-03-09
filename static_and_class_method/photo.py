from math import ceil
from typing import List


class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(ceil(photos_count / 4))

    def add_photo(self, label):
        for i in range(self.pages):
            if len(self.photos[i]) < 4:
                slot = len(self.photos[i]) + 1
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {slot}"

        else:
            return "No more free slots"

    def display(self):
        dash_row = "-----------"
        result = f"{dash_row}\n"
        for i in range(self.pages):
            result += f'{("[] " * len(self.photos[i])).strip()}\n{dash_row}\n'

        return result


album = PhotoAlbum(3)

print(album.add_photo("baby"))

print(album.add_photo("first grade"))

print(album.add_photo("eight grade"))

print(album.add_photo("party with friends"))

print(album.photos)

print(album.add_photo("prom"))

print(album.add_photo("wedding"))

print(album.display())
