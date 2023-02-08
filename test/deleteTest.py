import os
import shutil


def deleteTest(path_to_folder):
    list_dir = os.listdir(path_to_folder)

    for filename in list_dir:

        file_path = os.path.join(path_to_folder, filename)

        if os.path.isfile(file_path) or os.path.islink(file_path):

            print("deleting file:", file_path)

            os.unlink(file_path)

        elif os.path.isdir(file_path):

            print("deleting folder:", file_path)

            shutil.rmtree(file_path)
