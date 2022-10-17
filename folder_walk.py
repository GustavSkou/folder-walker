import glob
import random as r
r.seed()


class FileFinder:
    lis_png = []
    ran_lis_png = []

    @staticmethod
    def walk_folders(path):
        ff = FileFinder

        ff.lis_png.clear()

        path = glob.glob(path + "/*")

        for ele in path:

            def walk(ele):
                path = glob.glob(ele + "/*")
                for ele in path:
                    if ele.endswith(".png"):
                        ff.lis_png.append(ele)

                    walk(ele)

            walk(ele)

        length = str(len(ff.lis_png))
        print("numbers of images: " + length)

    @staticmethod
    def randomizer():
        ff = FileFinder
        ff.ran_lis_png.clear()
        print("----------------------------------------random sample----------------------------------------")
        for x in range(5):
            ff.ran_lis_png = r.sample(ff.lis_png, 1)

            print(ff.ran_lis_png)
