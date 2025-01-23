import unittest
from src.generate import extract_title

class TestGenerate(unittest.TestCase):
    
    def test_title(self):
        text = '# Hello Title'
        expected = 'Hello Title'
        result = extract_title(text)
        self.assertEqual(result, expected)

    def test_title_err(self):
        text = 'Hello Title'
        with self.assertRaises(Exception) as ctx:
            extract_title(text)
        
        self.assertTrue('No valid title found' in str(ctx.exception))