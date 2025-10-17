#!/usr/bin/env python3

ORIGINAL_PATH = "/Users/mahikakapil/Desktop/Misc/eulersphere/potiontransactionshop.bf"        # Original Brainfuck file
DECRYPTED_PATH ="/Users/mahikakapil/Desktop/Misc/eulersphere/potiontransactionshop_dc.bf"   # Decrypted output

def compare_files(original_path, decrypted_path):
    with open(original_path, "rb") as f:
        original_data = f.read()
    
    with open(decrypted_path, "rb") as f:
        decrypted_data = f.read()
    
    if original_data == decrypted_data:
        print("✅ Success! The decrypted file is identical to the original.")
    else:
        print("❌ Mismatch! The decrypted file differs from the original.")

if __name__ == "__main__":
    compare_files(ORIGINAL_PATH, DECRYPTED_PATH)
