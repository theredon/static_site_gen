import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Test Case", None, {"class": "testing", "href": "https://boot.dev"})
        self.assertEqual(
            node.props_to_html(), " class='testing' href='https://boot.dev'"
        )
    
    def test_values(self):
        node = HTMLNode("p", "Value McValueson")
        self.assertEqual(
            node.tag,
            "p",
        )
        self.assertEqual(
            node.value,
            "Value McValueson",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode("span", "I dont do tests information well", None, {'html': 'https://boot.dev'})
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(tag: span, value: I dont do tests information well, children: None, props: {'html': 'https://boot.dev'})"
        )

    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Leaf testing p tag and value")
        self.assertEqual(node.to_html(), "<p>Leaf testing p tag and value</p>")
    
    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click for Google", {"href": "https://google.com"})
        self.assertEqual(node.to_html(), "<a href='https://google.com'>Click for Google</a>")

    def test_repr(self):
        node = LeafNode("a", "Boot.dev", {'href': 'https://boot.dev'})
        self.assertEqual(
            node.__repr__(),
            "LeafNode(tag: a, value: Boot.dev, props: {'href': 'https://boot.dev'})"
        )


if __name__ == "__main__":
    unittest.main()