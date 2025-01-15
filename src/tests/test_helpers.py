import unittest
from src.inline_markdown import extract_markdown_images, extract_markdown_links, markdown_to_blocks

class TestExtractLinks(unittest.TestCase):
    def test_image_normal(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        expected_arr = [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        result = extract_markdown_images(text)
        self.assertListEqual(result, expected_arr)

    def test_link_normal(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        expected_arr = [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        result = extract_markdown_links(text)
        self.assertListEqual(result, expected_arr)

