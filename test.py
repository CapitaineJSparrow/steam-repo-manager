import re
import os
from pathlib import Path
from random import randint

library_path = os.path.join(Path.home(), 'test.txt')

if __name__ == "__main__":

    myfile = library_path

    with open(myfile, "r+") as f:
        data = f.read()
        token = 0 + randint(10000000, 90000000)
        f.seek(0)
        f.write(str(token))
        f.truncate()

