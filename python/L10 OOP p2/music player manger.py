class Playlist:

#Step 1 - Parameterized Constructor: runs the moment the playlist is created
 def __init__(self,name, genre):
     self.name = name
     self.genre = genre
     self.songs = []
     print(f"playlist '{self.name}' ({self.genre}) is ready!")

     #step 2 - add a song to the playlist
 def add_song(self,song):
    self.songs.append(song)
    print(f"'{song}' added to {self.name}.")

    #step 3 remove a song from a playlist
 def remove_song(self,song):
    if song in self.songs:
       self.songs.remove(song)
       print(f"'{song}' removed")
    else:
       print(f"'{song}' not found in playlist.")

    #step 4 display all songs
 def display(self):
    print(f"\n--- {self.name} ({self.genre}) ---")
    if self.songs:
       for i, song in enumerate(self.songs, 1):
          print(f"   {i}. {song}")
    else:
       print("No songs yet. Add some")

    #step 5 - destructor: runs automatically when the playlist is deleted
 def __del__(self):
    print(f"Playlist '{self.name}' has been deleted. Goodbye!")

    #object creation(constructor files here)
my_playlist = Playlist("Road Trip Mix", "Pop")

    #step 6 - menue driven program using the playlist class
while True:
    print("\n1. Add song 2. Remove song 3. view playlist 4.delete & quit")
    choice = input("Enter your choice:")

    if choice == "1":
       song = input("Enter song name:")
       my_playlist.add_song(song)
    elif choice == "2":
       song = input("Enter song to remove:")
       my_playlist.remove_song(song)
    elif choice == "3":
       my_playlist.display()
    elif choice == "4":
       del my_playlist #destructor fires here
       break
    else:
       print("Invalid choice. Enter 1, 2, 3, or 4")

       
       

