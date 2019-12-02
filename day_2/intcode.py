import copy

def execute_program(program):
    idx = 0
    command = program[idx]
    while command != 99:
        a = program[program[idx + 1]]
        b = program[program[idx + 2]]
        dest = program[idx + 3]
        if command == 1:
            program[dest] = a + b
        elif command == 2:
            program[dest] = a * b
        idx += 4
        command = program[idx]


if __name__ == "__main__":

    with open("program.txt", 'r') as f:
        init_program = list(map(int, f.read().strip().split(",")))

    program = copy.copy(init_program)
    
    # Step 1
    # Replace positions
    program[1] = 12
    program[2] = 2

    execute_program(program)
    print(program[0])

    goal_val = 19690720 # moon landing
    for noun in range(1, 100):
        for verb in range(1, 100):
            program = copy.copy(init_program)
            program[1] = noun
            program[2] = verb
            execute_program(program)
            if program[0] == goal_val:
                print(f"Noun: {noun}, verb: {verb}, result = {100 * noun + verb}")

