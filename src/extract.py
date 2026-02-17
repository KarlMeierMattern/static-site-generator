import re

def extract_markdown_images(text: str) -> list[str]:
    return [
        (alt_text, image_url)
        for alt_text, image_url in re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    ]

def extract_markdown_links(text: str) -> list[str]:
    return [
        (link_text, link_url)
        for link_text, link_url in re.findall(r"\[(.*?)\]\((.*?)\)", text)
    ]


