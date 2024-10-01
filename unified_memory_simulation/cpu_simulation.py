import threading
import time

class CPU:
    def __init__(self, memory, device_type, cores=4):
        self.memory = memory
        self.device_type = device_type
        self.cores = cores
        self.tasks = []  # List of tasks running concurrently

    def execute_read(self, address, is_persistent=False):
        value = self.memory.read_from_memory(address, is_persistent)
        print(f"{self.device_type} CPU Read from {'Persistent' if is_persistent else 'RAM'} Memory[{address}]: {value}")
        return value

    def execute_write(self, address, value, is_persistent=False):
        self.memory.write_to_memory(address, value, is_persistent)

    def manage_cache(self, address):
        self.memory.handle_cache(address)

    def multitasking_simulation(self, task_fn, args):
        task = threading.Thread(target=task_fn, args=args)
        self.tasks.append(task)
        task.start()

    def wait_for_tasks(self):
        for task in self.tasks:
            task.join()
