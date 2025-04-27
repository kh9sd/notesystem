import pathlib
from pathlib import Path
from pprint import pprint
from natsort import natsorted
import cv2

#print(f"{os.getcwd()=}")
#print(f"{os.listdir()=}")

files = [f for f in pathlib.Path().glob("*.png")]
# pprint(files)
files = natsorted(files, key=str)
pprint(files)

# shit = files[0].resolve()
# print(shit)

MAX_WIDTH = 600

for img_path in files:
    img_path_abs = img_path.resolve()
    print(f"On {img_path_abs}")

    img = cv2.imread(img_path_abs, cv2.IMREAD_UNCHANGED)
    img_height = img.shape[0]
    img_width = img.shape[1]
    # print(f"{img_height=} {img_width=}")

    scaling_factor = 600 / img_width
    img = cv2.resize(img, None, fx=scaling_factor, fy=scaling_factor)
    cv2.imshow('custom window', img)
    ret = cv2.waitKey(0)
    ret_key = (ret & 0xFF)
    if (ret_key == ord('o')):
        #print(f"{img_path=}")
        root_path = Path.cwd()
        new_path = root_path / "done_splits" / img_path
        #print(f"{new_path=}")
        print(f"ok key, moving to {new_path}")

        img_path.rename(new_path)
    elif (ret_key == ord('n')):
        print("no key, no change")
    else:
        print("weird key, no change")

    cv2.destroyAllWindows()
