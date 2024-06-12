import sys, os, glob
from PIL import Image
# pip install pillow

def main(path):
    lst = glob.glob(path + "/*.jpg")
    out_dir = path + "/out"
    os.mkdir(out_dir)
    for f in lst:
        im = Image.open(f)
        sp = os.path.split(f)
        out_name = os.path.join(out_dir, sp[1])
        print(out_name)
        im.save(out_name)

if __name__ == '__main__':
    main(sys.argv[1])
