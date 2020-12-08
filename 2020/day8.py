class State:
    def __init__(self, accumulator = 0, instruction_pointer = 0):
        self.accumulator = accumulator
        self.instruction_pointer = instruction_pointer

    def apply_instruction(self, instruction):
        op, qty = instruction.split(" ")[:2] 
        if op == "nop": return self.__nop(int(qty))
        if op == "acc": return self.__acc(int(qty))
        if op == "jmp": return self.__jmp(int(qty))

    def __nop(self, num):
        return self.__jmp(1)

    def __acc(self, num):  
        return State(self.accumulator + num, self.instruction_pointer + 1)

    def __jmp(self, num):
        return State(self.accumulator, self.instruction_pointer + num)

def main():
    with open("day8.data",'r') as fs:
        instructions = list(map(lambda line: line.strip(), fs.readlines()))

    state = bootSequence(instructions)
    print("Accumulator before infinite loop: {}".format(state.accumulator))

    state = get_state_on_completion(instructions)
    print("Accumulator after fixing instructions: {}".format(state.accumulator))

def get_state_on_completion(instructions):
    for i in range(0, len(instructions)):
        modified_instructions = swap_nop_or_jmp_instruction_at_index(i, instructions)
        state = bootSequence(modified_instructions)
        if completed_all_instructions(state, modified_instructions):            
            return state  # We had a successful boot sequence!
            
    return None # No run through the instructions resulted in a 'complete' state.

def completed_all_instructions(state, instructions):
    return state.instruction_pointer == len(instructions)

def swap_nop_or_jmp_instruction_at_index(index, instructions):
    modified_instructions = instructions.copy()
    instruction = modified_instructions[index]
    if instruction.startswith("nop"):
        modified_instructions[index] = instruction.replace("nop", "jmp")
    elif instruction.startswith("jmp"):
        modified_instructions[index] = instruction.replace("jmp", "nop")
    return modified_instructions

def bootSequence(instructions): 
    state = State(0, 0)    
    all_states = []
    infinite_loop_encountered = False
    while not infinite_loop_encountered and state.instruction_pointer < len(instructions):
        processed = get_instruction_pointers(all_states)
        infinite_loop_encountered = processed.count(state.instruction_pointer) > 1
        if not infinite_loop_encountered:
            instruction = instructions[state.instruction_pointer]
            state = state.apply_instruction(instruction)
            all_states.append(state)
    
    return all_states[-1]   # Return the last state before we encountered the infinite loop
    
def get_instruction_pointers(states):
    return list(map(lambda state: state.instruction_pointer, states))

main()