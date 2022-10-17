from folder_walk import FileFinder

path = str

while path != "exit":
    path = input("path to search: ")
    FileFinder.walk_folders(path)
    FileFinder.randomizer()
