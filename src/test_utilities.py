import unittest

from utilities import split_nodes_delimiter, extract_markdown_links, extract_markdown_images
from textnode import TextNode, TextType


class TestUtilities(unittest.TestCase):
    def test_code_split(self):
        node = TextNode("This is text with a `code block` word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.NORMAL)
            ],
            new_nodes,
        )

    def test_bold_split(self):
        node = TextNode("This is text with a **bold** word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" word", TextType.NORMAL)
            ],
            new_nodes,
        )

    def test_bold_split_multiple(self):
        node = TextNode("This is text with a **bold** word and **another**", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("bold", TextType.BOLD),
                TextNode(" word and ", TextType.NORMAL),
                TextNode("another", TextType.BOLD)
            ],
            new_nodes,
        )
        
    def test_italic_split(self):
        node = TextNode("This is text with a _italic_ word", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.NORMAL),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.NORMAL)
            ],
            new_nodes,
        )
    
    def text_split_multiple_types(self):
        node = TextNode("This is a **bold way** to _italicize_ markdown for `code`", TextType.NORMAL)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        new_nodes = split_nodes_delimiter(new_nodes, "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is a ", TextType.NORMAL),
                TextNode("bold way", TextType.BOLD),
                TextNode(" to ", TextType.NORMAL),
                TextNode("italicize", TextType.ITALIC),
                TextNode(" markdown for ", TextType.NORMAL),
                TextNode("code", TextType.CODE)
            ],
            new_nodes,
        )
    
    def test_missing_split(self):
        node = TextNode("This is text with a _italic word", TextType.NORMAL)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "_", TextType.ITALIC)

    def test_extract_markdown_images(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)
    
    def test_extract_markdown_images_multiple(self):
        matches = extract_markdown_images(
            "Why don't you ![ride](https://i.imgur.com/asdfasdf.jpeg) with a ![donkey](https://i.imgur.com/aidser.png), it would be ![funny](https://i.imgur.com/dirasdf.jpg)"
            
        )
        self.assertListEqual(
            [
                ("ride", "https://i.imgur.com/asdfasdf.jpeg"),
                ("donkey", "https://i.imgur.com/aidser.png"),
                ("funny", "https://i.imgur.com/dirasdf.jpg"),
            ],
            matches
        )

    def test_extract_markdon_links(self):
        matches = extract_markdown_links(
            "To search the web go to [google.com](https://google.com)"
        )
        self.assertListEqual([("google.com", "https://google.com")], matches)
    
    def test_extract_markdown_links_multiple(self):
        matches = extract_markdown_links(
            "My favorite sites are [google.com](https://google.com), [Boot Dev](https://www.youtube.com/@bootdotdev), and [Facebook](https://www.facebook.com)"
            
        )
        self.assertListEqual(
            [
                ("google.com", "https://google.com"),
                ("Boot Dev", "https://www.youtube.com/@bootdotdev"),
                ("Facebook", "https://www.facebook.com"),
            ],
            matches
        )

if __name__ == "__main__":
    unittest.main()