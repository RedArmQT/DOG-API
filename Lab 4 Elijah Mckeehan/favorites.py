import json

FAVORITES_FILE = "favorites.json"

def load_favorites():
    try:
        with open(FAVORITES_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_favorites(favorites):
    with open(FAVORITES_FILE, "w") as file:
        json.dump(favorites, file, indent=4)

def add_to_favorites(breed):
    favorites = load_favorites()
    if breed not in favorites:
        favorites.append(breed)
        save_favorites(favorites)
        print(f"✅ {breed} added to favorites!")
    else:
        print(f"⚠️ {breed} is already in favorites.")

def view_favorites():
    favorites = load_favorites()
    if favorites:
        print("⭐ Favorite Breeds ⭐")
        for breed in favorites:
            print(f"- {breed}")
    else:
        print("No favorite breeds saved yet.")