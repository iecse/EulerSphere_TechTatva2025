#!/usr/bin/env python3

INPUT_PATH = "/Users/mahikakapil/Desktop/Misc/eulersphere/potiontransactionshop.txt"  # Encrypted base-10 numbers
OUTPUT_PATH = "/Users/mahikakapil/Desktop/Misc/eulersphere/potiontransactionshop_dc.bf"  # Recovered Brainfuck file

def decrypt_file(input_path, output_path):
    with open(input_path, "r") as f:
        numbers = f.read().splitlines()
    
    decrypted_chars = []

    for num_str in numbers:
        num = int(num_str)
        # Extract 4×16-bit sections
        for shift in (48, 32, 16, 0):
            val = (num >> shift) & 0xFFFF
            if val != 0:  # ignore padding zeros
                decrypted_chars.append(chr(val))
    
    with open(output_path, "w") as f:
        f.write("".join(decrypted_chars))

    print(f"Decryption complete! Output saved to {output_path}")

if __name__ == "__main__":
    decrypt_file(INPUT_PATH, OUTPUT_PATH)
