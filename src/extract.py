import re

def extract_markdown_images(text: str) -> list[str]:
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    #print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    return [
        (alt_text, image_url)
        for alt_text, image_url in re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    ]

def extract_markdown_links(text: str) -> list[str]:
    # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
    return [
        (link_text, link_url)
        for link_text, link_url in re.findall(r"\[(.*?)\]\((.*?)\)", text)
    ]


