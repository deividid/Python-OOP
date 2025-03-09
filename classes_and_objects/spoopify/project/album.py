from typing import List

from project.song import Song


class Album:
    def __init__(self, name, *songs: Song):
        self.name = name
        self.published = False
        self.songs: List[Song] = [s for s in songs]

    def add_song(self, s: Song):
        if self.published:
            return "Cannot add songs. Album is published."
        elif s.single:
            return f"Cannot add {s.name}. It's a single"

        elif s in self.songs:
            return "Song is already in the album."

        else:
            self.songs.append(s)
            return f"Song {s.name} has been added to the album {self.name}."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."

        elif song_name not in [s.name for s in self.songs]:
            return "Song is not in the album."

        else:
            for s in self.songs:
                if s.name == song_name:
                    self.songs.remove(s)
                    return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."

        else:
            self.published = True
            return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}"
        for s in self.songs:
            result += f"\n{s.get_info()}"

        return result







