class CPU:
    def __init__(self, memory):
        self.memory = memory

    def execute_read(self, address, is_persistent=False):
        value = self.memory.read_from_memory(address, is_persistent)
        print(f"CPU Read from {'Persistent' if is_persistent else 'RAM'} Memory[{address}]: {value}")

    def execute_write(self, address, value, is_persistent=False):
        self.memory.write_to_memory(address, value, is_persistent)
        print(f"CPU Write to {'Persistent' if is_persistent else 'RAM'} Memory[{address}]: {value}")
