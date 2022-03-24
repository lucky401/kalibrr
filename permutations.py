def permutations():
    global running
    global characters
    global bitmask
    if len(running) == len(characters):
        with open('permutations_output.txt', 'a') as f:
            f.write(''.join(running) + '\n')

    else:
        for i in range(len(characters)):
            if ((bitmask>>i)&1) == 0:
                bitmask |= 1<<i
                running.append(characters[i])
                permutations()
                bitmask ^= 1<<i
                running.pop()

raw = input()
characters = list(raw)
running = []
bitmask = 0
permutations()