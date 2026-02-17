# Write a recursive function that copies all the contents from a source directory to a destination directory (in our case, static to public)
# It should first delete all the contents of the destination directory (public) to ensure that the copy is clean.
# It should copy all files and subdirectories, nested files, etc.
# I recommend logging the path of each file you copy, so you can see what's happening as you run and debug your code.

import os
import shutil

def copy_directory(source: str, destination: str) -> None:
    if os.path.exists(destination):
        shutil.rmtree(destination)
    os.makedirs(destination, exist_ok=True)

    for item in os.listdir(source):
        s = os.path.join(source, item)
        d = os.path.join(destination, item)
        if os.path.isdir(s):
            copy_directory(s, d)
        else:
            shutil.copy2(s, d)
            print(f"Copied {s} to {d}")

if __name__ == "__main__":
    copy_directory("static", "public")