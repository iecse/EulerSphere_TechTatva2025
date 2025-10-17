def brainfuck_to_csv(bf_code, output_file):
    tape = [0] * 30000
    ptr = 0
    output = []
    pc = 0
    code_len = len(bf_code)

    # Precompute loop jumps
    jump_map = {}
    temp_stack = []
    for i, c in enumerate(bf_code):
        if c == '[':
            temp_stack.append(i)
        elif c == ']':
            start = temp_stack.pop()
            jump_map[start] = i
            jump_map[i] = start

    while pc < code_len:
        c = bf_code[pc]
        if c == '>':
            ptr += 1
        elif c == '<':
            ptr -= 1
        elif c == '+':
            tape[ptr] = (tape[ptr] + 1) % 256
        elif c == '-':
            tape[ptr] = (tape[ptr] - 1) % 256
        elif c == '.':
            output.append(chr(tape[ptr]))
        elif c == ',':
            pass
        elif c == '[' and tape[ptr] == 0:
            pc = jump_map[pc]
        elif c == ']' and tape[ptr] != 0:
            pc = jump_map[pc]
        pc += 1

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(output))

if __name__ == "__main__":
    bfName = "MC2.bf"
    csvName = "MC2.csv"
    with open(bfName, "r") as f:
        bf_code = f.read()
    brainfuck_to_csv(bf_code, csvName)