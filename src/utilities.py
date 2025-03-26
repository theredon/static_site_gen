import re

from textnode import TextType, TextNode

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        split_nodes = []
        chunks = node.text.split(delimiter)
        if len(chunks) % 2 == 0:
            raise Exception(f"Invalid Markdown text, unmatched {delimiter} in text: {node.text}")
        for i in range(len(chunks)):
            if chunks[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(chunks[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(chunks[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

