from enum import Enum

class BlockType(Enum):
    HEADING1 = 'h1'
    HEADING2 = 'h2'
    HEADING3 = 'h3'
    HEADING4 = 'h4'
    HEADING5 = 'h5'
    HEADING6 = 'h6'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED = 'unordered'
    ORDERED = 'ordered'
    PARAGRAPH = 'paragraph'