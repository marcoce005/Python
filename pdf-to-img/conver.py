import os
import argparse
from pdf2image import convert_from_path

parser = argparse.ArgumentParser()
parser.add_argument('-n', help='name-file')
args = parser.parse_args()

path = "pdf/" + args.n
name_dir = path[4 : -4]

img = convert_from_path(path)

os.mkdir(name_dir)

for i in range(len(img)):
    img[i].save(name_dir + "/" + name_dir + str(i) + ".jpg", "JPEG")