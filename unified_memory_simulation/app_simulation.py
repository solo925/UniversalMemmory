# Sample Application Interacting with Memory\
# This is a simple app simulating the state saved across power cycles.
class Application:
    def __init__(self, cpu):
        self.cpu = cpu

    def run_simulation(self):
        # Initial Writes
        self.cpu.execute_write(0, 42.0)  # Write to RAM
        self.cpu.execute_write(0, 84.0, is_persistent=True)  # Write to Persistent Memory
        self.cpu.execute_write(1, 21.0, is_persistent=True)

        # Read Data
        self.cpu.execute_read(0)  # Read from RAM
        self.cpu.execute_read(0, is_persistent=True)  # Read from Persistent Memory
        self.cpu.execute_read(1, is_persistent=True)
