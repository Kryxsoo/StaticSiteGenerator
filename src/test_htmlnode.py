import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode(
            tag = "a",
            value = "Click Me!",
            props = {"href": "https://www.google.com"}
        )
        expected = ' href="https://www.google.com"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

# A test for when props is None
    def test_props_is_none(self):
        node = HTMLNode(
            tag = "a",
            value = "Click Me!",
            props = None
        )
        expected = ""
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

# A test for multiple properties (like with both href and target)
    def test_para(self):
        node = HTMLNode(
            tag = "a",
            value = "Click Me!",
            props = {"href": "https://www.google.com", "target": "_blank"}
        )
        expected = '<p>This is a paragraph of text.</p>' '<a href="https://www.google.com">Click me!</a>'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

##################

# a Test to check paragraph and value
    def test_para(self):
        node = LeafNode(
            tag = "a",
            value="Click me!",
            props={"href": "https://www.google.com", "target": "_blank"}
        )
        expected = '<a href="https://www.google.com" target="_blank">Click me!</a>'
        actual = node.to_html()
        self.assertEqual(expected, actual)

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

        
##################
    
    def test_to_html_with_mixed_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)


if __name__ == "__main__":
    unittest.main()