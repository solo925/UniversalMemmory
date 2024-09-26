import numpy as np

class UnifiedMemory:
    def __init__(self, ram_size, persistent_size):
        # Simulating volatile RAM (empty after power cycles)
        self.ram = np.zeros(ram_size, dtype='float64')
        # Simulating non-volatile memory (persistent across cycles)
        self.persistent_memory = np.zeros(persistent_size, dtype='float64')

    def read_from_memory(self, address, is_persistent=False):
        if is_persistent:
            return self.persistent_memory[address]
        else:
            return self.ram[address]

    def write_to_memory(self, address, value, is_persistent=False):
        if is_persistent:
            self.persistent_memory[address] = value
        else:
            self.ram[address] = value

    def show_memory_status(self):
        print(f"RAM Status: {self.ram}")
        print(f"Persistent Memory Status: {self.persistent_memory}")
