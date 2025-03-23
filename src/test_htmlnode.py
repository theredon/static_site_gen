import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode("div", "Test Case", None, {"class": "testing", "href": "https://boot.dev"})
        self.assertEqual(
            node.props_to_html(), ' class="testing" href="https://boot.dev"'
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


if __name__ == "__main__":
    unittest.main()