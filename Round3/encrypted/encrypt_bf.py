#!/usr/bin/env python3
"""
Each group of 4 bytes becomes one 64-bit integer (16 bits per byte slot).

To reverse this, just unpack the 64-bit integers back into 4 bytes each.
"""

import struct

# ====== EDIT THESE PATHS ======
INPUT_PATH = "/Users/mahikakapil/Desktop/Misc/eulersphere/potiontransactionshop.bf"
OUTPUT_PATH = "/Users/mahikakapil/Desktop/Misc/eulersphere/potiontransactionshop.txt"
# ==============================



def pad_data(data, block_size=4):
    padding_len = (-len(data)) % block_size
    return data + ("\0" * padding_len)

def encrypt_file(input_path, output_path):
    with open(input_path, "r") as f:
        data = f.read()
    
    data = pad_data(data, 4)
    encrypted_numbers = []

    for i in range(0, len(data), 4):
        block = data[i:i+4]
        # Pack 4 chars into a single 64-bit number
        num = 0
        for j, c in enumerate(block):
            num |= (ord(c) & 0xFFFF) << (16*(3-j))  # shift 16-bit sections
        encrypted_numbers.append(str(num))

    with open(output_path, "w") as f:
        f.write("\n".join(encrypted_numbers))

    print(f"Encryption complete! Output saved to {output_path}")

if __name__ == "__main__":
    encrypt_file(INPUT_PATH, OUTPUT_PATH)
