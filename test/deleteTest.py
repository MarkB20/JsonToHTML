import os
import shutil


def deleteTest(pathToFolder):

    list_dir = os.listdir(pathToFolder)
    # go through each file and deletes it
    for filename in list_dir:

        filePath = os.path.join(pathToFolder, filename)

        if os.path.isfile(filePath) or os.path.islink(filePath):

            print("deleting file:", filePath)

            os.unlink(filePath)

        elif os.path.isdir(filePath):

            print("deleting folder:", filePath)

            shutil.rmtree(filePath)

    fake_file = "fake file for github"
    with open(f'{pathToFolder}/dummy.txt', 'w') as f:
        f.write(fake_file)
