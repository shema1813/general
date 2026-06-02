class ArtGallery:
    
    def __init__(self, gallery_name):
        self.gallery_name = gallery_name
        self.artworks = []  # Empty list by default
        print(f"Art Gallery '{self.gallery_name}' created.")

    
    def add_artwork(self, artwork):
        self.artworks.append(artwork)
        print(f"'{artwork}' added to the gallery.")

    #
    def remove_artwork(self, artwork):
        if artwork in self.artworks:
            self.artworks.remove(artwork)
            print(f"'{artwork}' removed from the gallery.")
        else:
            print("Artwork not found.")

    def display_artworks(self):
        print(f"\nArtworks in {self.gallery_name}:")
        if not self.artworks:
            print("No artworks available.")
        else:
            for i, artwork in enumerate(self.artworks, start=1):
                print(f"{i}. {artwork}")

    
    def __del__(self):
        print(f"Art Gallery '{self.gallery_name}' is now closed.")



gallery_name = input("Enter the gallery name: ")
gallery = ArtGallery(gallery_name)

while True:
    print("\n===== Art Gallery Collection Manager =====")
    print("1. Add Artwork")
    print("2. Remove Artwork")
    print("3. Display Artworks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        artwork = input("Enter artwork name: ")
        gallery.add_artwork(artwork)

    elif choice == "2":
        artwork = input("Enter artwork name to remove: ")
        gallery.remove_artwork(artwork)

    elif choice == "3":
        gallery.display_artworks()

    elif choice == "4":
        print("Exiting program...")
        del gallery  # Calls destructor
        break

    else:
        print("Invalid choice. Please try again.")