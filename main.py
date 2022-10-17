import folder_walk as fw

path = str

while path != "exit":
    path = input("path to search: ")
    fw.walk_folders(path)
