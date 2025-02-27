from dog_api import get_random_dog, get_dog_by_breed, list_all_breeds
from favorites import add_to_favorites, view_favorites

def main():
    while True:
        print("\n Dog API Viewer ")
        print("1. Get a random dog image")
        print("2. Get an image of a dog by breed")
        print("3. List all available breeds")
        print("4. Save a breed to favorites")
        print("5. View favorite breeds")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            get_random_dog()  # Now opens an image!
        elif choice == "2":
            breed = input("Enter breed name: ").strip().lower()
            get_dog_by_breed(breed)  # Now opens an image!
        elif choice == "3":
            print(list_all_breeds())
        elif choice == "4":
            breed = input("Enter breed name to save: ").strip().lower()
            add_to_favorites(breed)
        elif choice == "5":
            view_favorites()
        elif choice == "6":
            print("Goodbye! 🐾")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    main()
