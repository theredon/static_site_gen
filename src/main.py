from textnode import TextNode, TextType
from utilities import extract_markdown_images, extract_markdown_links

def main():
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))

main()