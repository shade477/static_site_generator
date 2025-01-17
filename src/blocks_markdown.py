import re


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
        level = len(text.split(' ', 1)[0])
        if level > 6:
            level = 6
        return f'h{level}'

    elif text[:3] == '```':
        if text[-3:] == '```':
            return f'code'
        raise Exception('Code block not enclosed')

    elif text[0] == '>':
        parts = text.split('\n')
        for part in parts:
            if part[0] != '>':
                raise Exception('Quote line not start with ">"')
        return 'quote'

    elif text[0] == '-' or text[0] == '*':
        ch = text[0]
        parts = text.split('\n')
        for part in parts:
            if part[0] != ch:
                raise Exception('Unordered lines not good')
        return 'unordered'

    elif re.match(r'^([0-9]+)\. .*', text):
        parts = text.split('\n')
        match = re.search(r'^([0-9]+)\.', parts[0])  # Check the first line
        
        if not match:
            raise Exception("Bad Block: The first line does not start with a number and a period.")
        expected = int(match.group(1))  # Extract the first number

        for part in parts:
            match = re.match(r'^([0-9]+)\. ', part)
            if not match:
                raise Exception("Bad Block: Line does not start with a number and a period.")
            number = int(match.group(1))
            if number != expected:
                raise Exception(f"Bad numbering: Expected {expected}, but got {number}.")
            expected += 1  # Increment expected for the next line
        return 'ordered'
    
    else:
        return 'paragraph'