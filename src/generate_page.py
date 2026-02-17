from markdown_to_htmlnode import markdown_to_html_node
from extract_title import extract_title
import os

def generate_page(from_path: str, template_path: str, dest_path: str, basepath: str) -> None:
    print(f"Generating page from {from_path} to {dest_path} using template_path {template_path}")
    with open(from_path, "r") as file:
        markdown = file.read()
    with open(template_path, "r") as file:
        template = file.read()
    html_node = markdown_to_html_node(markdown)
    title = extract_title(markdown)
    html = html_node.to_html()
    html = template.replace("{{ Title }}", title)
    html = html.replace("{{ Content }}", html_node.to_html())
    html = html.replace("href=\"/", f"href=\"{basepath}")
    html = html.replace("src=\"/", f"src=\"{basepath}")
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(html)