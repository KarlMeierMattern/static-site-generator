# Create a generate_pages_recursive(dir_path_content, template_path, dest_dir_path) function. It should:
# Crawl every entry in the content directory
# For each markdown file found, generate a new .html file using the same template.html. The generated pages should be written to the public directory in the same directory structure.
# Change your main function to use generate_pages_recursive instead of generate_page. You should generate a page for every markdown file in the content directory and write the results to the public directory.

import os
from generate_page import generate_page

def generate_pages_recursive(dir_path_content: str, template_path: str, dest_dir_path: str, basepath: str = "/") -> None:
    for item in os.listdir(dir_path_content):
        path = os.path.join(dir_path_content, item)
        if os.path.isdir(path):
            generate_pages_recursive(path, template_path, os.path.join(dest_dir_path, item), basepath)
        elif item.endswith(".md"):
            generate_page(path, template_path, os.path.join(dest_dir_path, item.replace(".md", ".html")), basepath)