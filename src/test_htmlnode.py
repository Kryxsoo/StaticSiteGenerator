import unittest

from htmlnode import HTMLNode


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
    def test_multi_props(self):
        node = HTMLNode(
            tag = "a",
            value = "Click Me!",
            props = {"href": "https://www.google.com", "target": "_blank"}
        )
        expected = ' href="https://www.google.com" target="_blank"'
        actual = node.props_to_html()
        self.assertEqual(expected, actual)

if __name__ == "__main__":
    unittest.main()