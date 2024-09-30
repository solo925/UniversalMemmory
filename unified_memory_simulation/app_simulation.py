import time
class Application:
    def __init__(self, cpu):
        self.cpu = cpu

    def compute_intensive_task(self, cycles):
        for i in range(cycles):
            self.cpu.execute_write(i, i * 1.1)
            self.cpu.execute_read(i)
            time.sleep(0.1)

    def run_multithreaded(self):
        # Run multiple tasks concurrently
        self.cpu.multitasking_simulation(self.compute_intensive_task, (10,))
        self.cpu.multitasking_simulation(self.compute_intensive_task, (10,))
        self.cpu.wait_for_tasks()
