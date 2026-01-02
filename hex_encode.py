#!/usr/bin/env python3

from sys import argv

phrase = argv[1] if len(argv) > 1 else "Hello, World!"
  
def hex_encode_char(phrase: str) -> str:
    # Emit each byte as \xHH (use double backslash so the literal slash is kept)
    return ''.join(f'\\x{byte:02x}' for byte in phrase.encode('utf-8'))
encoded_phrase = hex_encode_char(phrase)

print(f"Original phrase: {phrase}")
print(f"Hex encoded phrase: \n{encoded_phrase}")
