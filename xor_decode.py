#!/usr/bin/env python3

import base64

def derive_xor_key(b64_cipher: str, known_plain: bytes) -> bytes:
    cipher_bytes = base64.b64decode(b64_cipher)
    if len(cipher_bytes) < len(known_plain):
        raise ValueError("Ciphertext shorter than known plaintext; need at least that many bytes.")
    # Key bytes are just cipher ⊕ plain for the known region
    key = bytes(c ^ p for c, p in zip(cipher_bytes, known_plain))
    return key

def xor_decrypt(cipher_bytes: bytes, key: bytes) -> bytes:
    # Repeat key over the ciphertext
    key_len = len(key)
    return bytes(b ^ key[i % key_len] for i, b in enumerate(cipher_bytes))

b64_cipher = "HmYkBwozJw4WNyAAFyB1VUcqOE1JZjUIBis7ABdmbU1GITYKBCE2TRg="
known_plain = b'{"showpassword":"no","bgcolor":"#ffffff"}'

key = derive_xor_key(b64_cipher, known_plain)
print("Derived key (bytes):", key)
print("Derived key (text):", key.decode("ascii", errors="replace"))
print("Derived key (hex):", key.hex())

full_cipher = base64.b64decode(b64_cipher)
recovered = xor_decrypt(full_cipher, key)
print("Decrypted text:", recovered)

# Use the derived key bytes directly to encrypt a new payload; key cycles automatically
payload = b'{"showpassword":"yes","bgcolor":"#ffffff"}'
encoded = base64.b64encode(xor_decrypt(payload, key))
print("Payload encoded for cookie:", encoded.decode())
