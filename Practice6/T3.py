class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

    def __str__(self):
        return f"Title: {self.title}, Artist: {self.artist}, Duration: {self.duration} minutes"

   
    def __eq__(self, other):
        if isinstance(other, Song):
            return (self.title == other.title and 
                    self.artist == other.artist and 
                    self.duration == other.duration)
        return False


class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def remove_song(self, song):
        if song in self.songs:
            self.songs.remove(song)

    def total_duration(self):
        return sum(song.duration for song in self.songs)

    def __str__(self):
        lines = [f"Playlist: {self.name}"]
        for i, s in enumerate(self.songs, start=1):
            lines.append(f"{i}. {s}")
        lines.append(f"Total Duration: {self.total_duration()} minutes")
        lines.append(f"Number of Songs: {len(self.songs)}")
        return "\n".join(lines)


# Use distinct variable names (s1, s2 for songs; p1 for playlist)
s1 = Song("Beliver", "Ed Sheeran", 3)
s2 = Song("Shape of you", "Ed Sheeran", 4)

p1 = Playlist("Favorite Songs")
p1.add_song(s1)
p1.add_song(s2)
print(p1)

# Now works because __eq__ is defined in Song
p1.remove_song(Song("Beliver", "Ed Sheeran", 3))
print("\nAfter removing 'Beliver':")
print(p1)
