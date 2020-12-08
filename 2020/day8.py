class State:
    def __init__(self, accumulator = 0, instruction_index = 0):
        self.accumulator = accumulator
        self.instruction_index = instruction_index

    def operate_on(self, instruction):
        op, qty = instruction.split(" ")[:2] 
        if op == "nop": 
            return self.nop(int(qty))
        if op == "acc": 
            return self.acc(int(qty))
        if op == "jmp": 
            return self.jmp(int(qty))

    def nop(self, num):
        return self.jmp(1)

    def acc(self, num):  
        return State(self.accumulator + num, self.instruction_index + 1)

    def jmp(self, num):
        return State(self.accumulator, self.instruction_index + num)

def main():
    with open("day8.data",'r') as fs:
        instructions = list(map(lambda line: line.strip(), fs.readlines()))

    state = bootSequence(instructions)
    print("Accumulator before infinite loop: {}".format(state.accumulator))

def bootSequence(instructions): 
    state = State(0, 0)
    infinite_loop_encountered = False
    all_states = []
    while not infinite_loop_encountered and state.instruction_index < len(instructions):
        processed = get_instruction_indexes(all_states)
        if processed.count(state.instruction_index) > 1:
            infinite_loop_encountered = True
        else:
            instruction = instructions[state.instruction_index]
            new_state = state.operate_on(instruction)
            state = new_state
            all_states.append(state)
    
    return all_states[-1]   # Return the last state before we encountered the infinite loop
    
def get_instruction_indexes(states):
    return list(map(lambda state: state.instruction_index, states))


main()