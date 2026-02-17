# Update your main.py to build the site into the docs directory instead of public. GitHub pages serves sites from the docs directory of your main branch by default.

import sys
from copy_directory import copy_directory
from generate_pages_recursive import generate_pages_recursive

def main():
    
    basepath = sys.argv[1]
    if not basepath:
        basepath = "/"
    
    copy_directory("static", "docs")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()