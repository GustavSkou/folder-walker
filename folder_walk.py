import glob


def walk_folders(path):
    lis_png = []

    path = glob.glob(path + "/*")

    for ele in path:

        def walk(ele):
            path = glob.glob(ele + "/*")
            for ele in path:
                if ele.endswith(".png"):
                    lis_png.append(ele)

                walk(ele)

        walk(ele)

    length = str(len(lis_png))
    print("numbers of images: " + length)
