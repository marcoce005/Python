import os, sys


def find(path="./tree", target="python"):
    try:
        os.chdir(path)
    except:
        return  # to ignoring files
    
    folrder = os.getcwd()
    for e in os.listdir():
        if e == target:
            print(f"...tree{folrder.split("tree")[1]}/{target}")
        find(f"{folrder}/{e}")


# find(sys.argv[1], sys.argv[2])
find()