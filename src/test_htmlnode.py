import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

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

    def test_html_repr(self):
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

    def test_leaf_repr(self):
        node = LeafNode("a", "Boot.dev", {'href': 'https://boot.dev'})
        self.assertEqual(
            node.__repr__(),
            "LeafNode(tag: a, value: Boot.dev, props: {'href': 'https://boot.dev'})"
        )

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )
    
    def test_to_html_extreme(self):
        grandchild_node = LeafNode("b", "grandchild")
        child8_node = ParentNode("div", [grandchild_node])
        child7_node = ParentNode("span", [child8_node])
        child6_node = ParentNode("div", [child7_node])
        child5_node = ParentNode("span", [child6_node])
        child4_node = ParentNode("div", [child5_node])
        child3_node = ParentNode("span", [child4_node])
        child2_node = ParentNode("div", [child3_node])
        child1_node = ParentNode("span", [child2_node])
        parent_node = ParentNode("div", [child1_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><div><span><div><span><div><span><div><b>grandchild</b></div></span></div></span></div></span></div></span></div>",
        )
        
if __name__ == "__main__":
    unittest.main()