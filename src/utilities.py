import re

from textnode import TextType, TextNode, LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(None, text_node.text)
    if text_node.text_type == TextType.BOLD:
        return LeafNode("b", text_node.text)
    if text_node.text_type == TextType.ITALIC:
        return LeafNode("i", text_node.text)
    if text_node.text_type == TextType.CODE:
        return LeafNode("code", text_node.text)
    if text_node.text_type == TextType.LINK:
        return LeafNode("a", text_node.text, {'href': text_node.url})
    if text_node.text_type == TextType.IMAGE:
        return LeafNode("img", "", {'src': text_node.url, 'alt': text_node.text})
    raise Exception(f"Invalid text type: {text_node.text_type}")


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


def split_nodes_images(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        node_text = node.text
        images = extract_markdown_images(node_text)
        if len(images) == 0:
            new_nodes.append(node)
            continue
        for image in images:
            chunks = node_text.split(f"![{image[0]}]({image[1]})",1 )
            if len(chunks) != 2:
                raise Exception("Invalid Markdown text, unmatched image section close")
            if chunks[0] != "":
                new_nodes.append(TextNode(chunks[0], TextType.NORMAL))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1],))
            node_text = chunks[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.NORMAL))
    return new_nodes


def split_nodes_links(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.NORMAL:
            new_nodes.append(node)
            continue
        node_text = node.text
        links = extract_markdown_links(node_text)
        if len(links) == 0:
            new_nodes.append(node)
            continue
        for link in links:
            chunks = node_text.split(f"[{link[0]}]({link[1]})",1 )
            if len(chunks) != 2:
                raise Exception("Invalid Markdown text, unmatched links section close")
            if chunks[0] != "":
                new_nodes.append(TextNode(chunks[0], TextType.NORMAL))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1],))
            node_text = chunks[1]
        if node_text != "":
            new_nodes.append(TextNode(node_text, TextType.NORMAL))
    return new_nodes