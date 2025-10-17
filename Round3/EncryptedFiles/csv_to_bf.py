def csv_to_brainfuck(csv_file, bf_file):
    with open(csv_file, 'r', encoding='utf-8') as f:
        data = f.read()

    bf_code = ""
    prev_val = 0  

    for char in data:
        ascii_val = ord(char)
        diff = ascii_val - prev_val
        if diff > 0:
            bf_code += '+' * diff
        elif diff < 0:
            bf_code += '-' * (-diff)
        bf_code += '.'  
        prev_val = ascii_val

    with open(bf_file, 'w', encoding='utf-8') as f:
        f.write(bf_code)

    print(f"Brainfuck code written to: {bf_file}")

if __name__ == "__main__":
    csv_to_brainfuck("Mystical Creature.csv", "Mystical Creature.bf")
    csv_to_brainfuck("potion transaction shop.csv", "potion transaction shop.bf")
    csv_to_brainfuck("questboard.csv", "questboard.bf")
