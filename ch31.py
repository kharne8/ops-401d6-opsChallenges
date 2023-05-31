import os

def search_files(directory, filename):
    hits = 0
    searched_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == filename:
                hits += 1
                print(f"Found: {os.path.join(root, file)}")
            searched_files += 1

    return searched_files, hits

def main():
    while True:
        print("Options:")
        print("1. Windows")
        print("2. Linux")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == "1":
            os_type = "Windows"
        elif choice == "2":
            os_type = "Linux"
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        filename = input("Enter the file name to search for: ")
        directory = input("Enter the directory to search in: ")

        print(f"\nSearching for '{filename}' in '{directory}' on {os_type}...\n")

        if os_type == "Windows":
            directory = directory.replace("/", "\\")

        searched_files, hits = search_files(directory, filename)

        print("\nSearch complete.")
        print(f"Files searched: {searched_files}")
        print(f"Hits found: {hits}\n")

if __name__ == "__main__":
    main()
