from memory_simulation import UnifiedMemory
from cpu_simulation import CPU

# Define common device class
class Device:
    def __init__(self, device_type, ram_size, persistent_size, cache_size, cores):
        self.device_type = device_type
        self.memory = UnifiedMemory(ram_size, persistent_size, int(cache_size))  # Ensure cache_size is an integer
        self.cpu = CPU(self.memory, device_type, cores)

    def power_off(self):
        print(f"Powering off {self.device_type}")
        self.memory.clear_ram()  # Clear volatile memory
        self.memory.clear_cache()  # Clear CPU cache

    def power_on(self):
        print(f"Powering on {self.device_type}")
        self.memory.show_memory_status()

# Define specific device classes
class Laptop(Device):
    def __init__(self):
        super().__init__('Laptop', ram_size=8, persistent_size=256, cache_size=2, cores=4)

class Phone(Device):
    def __init__(self):
        super().__init__('Phone', ram_size=4, persistent_size=128, cache_size=1, cores=2)

class Server(Device):
    def __init__(self):
        super().__init__('Server', ram_size=32, persistent_size=1024, cache_size=8, cores=16)

class Smartwatch(Device):
    def __init__(self):
        super().__init__('Smartwatch', ram_size=1, persistent_size=8, cache_size=1, cores=1)  # Adjusted to integer

class IoTDevice(Device):
    def __init__(self):
        super().__init__('IoT Device', ram_size=1, persistent_size=4, cache_size=1, cores=1)  # Adjusted to integer

class Desktop(Device):
    def __init__(self):
        super().__init__('Desktop', ram_size=16, persistent_size=512, cache_size=4, cores=8)
