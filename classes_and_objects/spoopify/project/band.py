from typing import List

from project.album import Album

from project.song import Song


class Band:
    def __init__(self, name):
        self.name = name
        self.albums: List[Album] = []

    def add_album(self, a: Album):
        if a in self.albums:
            return f"Band {self.name} already has {a.name} in their library."

        else:
            self.albums.append(a)
            return f"Band {self.name} has added their newest album {a.name}."

    def remove_album(self, album_name):
        for a in self.albums:
            if a.name == album_name:
                if a.published:
                    return "Album has been published. It cannot be removed."

                else:
                    self.albums.remove(a)
                    return f"Album {album_name} has been removed."

        else:
            return f"Album {album_name} is not found."

    def details(self):
        result = f"Band {self.name}"
        for a in self.albums:
            result += f"\n{a.details()}"

        return result




