import re
from src.BlockType import BlockType

def markdown_to_blocks(text):
    """
    Takes input a string document and returns blocks
    @params
    - text: str -> String document to be split into blocks

    @return
    - List[str]
    """

    blocks = text.split('\n\n')
    res = []
    for block in blocks:
        if not block:
            continue
        block = block.strip()
        block = block.lstrip('\n')
        res.append(block)
    
    return res

def block_to_block_type(text):
    """
    Accepts single block of markdown and returns a string representing the type of markdown block it is
    @params:
    - text: str -> Text block

    @return str
    """

    if text[0] == '#':
        levels = [BlockType.HEADING1, BlockType.HEADING2, BlockType.HEADING3, BlockType.HEADING4, BlockType.HEADING5, BlockType.HEADING6]
        level = len(text.split(' ', 1)[0])
        if level > 6:
            level = 6
        return levels[level - 1] 

    elif text[:3] == '```':
        if text[-3:] == '```':
            return BlockType.CODE
        # raise Exception('Code block not enclosed')
        return BlockType.PARAGRAPH

    elif text[0] == '>':
        parts = text.split('\n')
        for part in parts:
            if part[0] != '>':
                # raise Exception('Quote line not start with ">"')
                return BlockType.PARAGRAPH
        return BlockType.QUOTE

    elif text[0] == '-' or text[0] == '*':
        ch = text[0]
        parts = text.split('\n')
        for part in parts:
            if part[0] != ch:
                # raise Exception('Unordered lines not good')
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED

    elif re.match(r'^([0-9]+)\. .*', text):
        parts = text.split('\n')
        match = re.search(r'^([0-9]+)\.', parts[0])  # Check the first line

        if not match:
            # raise Exception("Bad Block: The first line does not start with a number and a period.")
            return BlockType.PARAGRAPH
        expected = int(match.group(1))  # Extract the first number

        for part in parts:
            match = re.match(r'^([0-9]+)\. ', part)
            if not match:
                # raise Exception("Bad Block: Line does not start with a number and a period.")
                return BlockType.PARAGRAPH
            number = int(match.group(1))
            if number != expected:
                # raise Exception(f"Bad numbering: Expected {expected}, but got {number}.")
                return BlockType.PARAGRAPH
            expected += 1  # Increment expected for the next line
        return BlockType.ORDERED
    
    else:
        return BlockType.PARAGRAPH