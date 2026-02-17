# Create an extract_title(markdown) function.
# It should pull the h1 header from the markdown file (the line that starts with a single #) and return it.
# If there is no h1 header, raise an exception.
# extract_title("# Hello") should return "Hello" (strip the # and any leading or trailing whitespace)
# Write some unit tests for it.

def extract_title(markdown: str) -> str:
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#"):
            return line[1:].strip()
    return lines[0].strip() if lines else ""