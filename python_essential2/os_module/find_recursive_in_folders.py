import os


def only_folder(l):
    list = []
    for e in l:
        try:
            assert os.listdir(e)
            list.append(e)
        except:
            None
    return list


def find(path):
    try:
        os.chdir(path)
    except:
        return  # to ignore files

    if only_folder(os.listdir()) == []:
        print(os.getcwd())
        os.chdir("../")
        return

    for e in os.listdir():
        find(e)
    os.chdir("../")


print(find("tree"))
