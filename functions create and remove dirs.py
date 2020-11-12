import os


def create_dirs():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), "dir_{}".format(i))
        os.mkdir(new_path)


def remove_dirs():
    for i in range(1, 10):
        new_path = os.path.join(os.getcwd(), "dir_{}".format(i))
        os.removedirs(new_path)
