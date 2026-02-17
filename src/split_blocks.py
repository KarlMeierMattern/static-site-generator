def markdown_to_blocks(markdown: str) -> list[str]:

    blocks = []

    # The .split() method can be used to split a string into blocks based on a delimiter (\n\n is a double newline).
    blocks = markdown.split("\n\n")
    #You should .strip() any leading or trailing whitespace from each block.
    blocks = [block.strip() for block in blocks]
    #Remove any "empty" blocks due to excessive newlines.
    blocks = [block for block in blocks if block != ""]

    return blocks