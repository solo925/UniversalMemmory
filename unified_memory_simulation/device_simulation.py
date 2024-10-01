import numpy as np
from cpu_simulation import CPU  # Assuming you have this module available


class Memory:
    def __init__(self, ram_size, persistent_size):
        self.ram = np.zeros(ram_size, dtype='float64')
        self.persistent_memory = np.zeros(persistent_size, dtype='float64')
        self.cache = np.zeros(2, dtype='float64')
        self.allocated_blocks = []

    def write_to_memory(self, address, value, is_persistent=False):
        """Write a value to memory at a specific address."""
        if is_persistent:
            if 0 <= address < len(self.persistent_memory):
                self.persistent_memory[address] = value
                print(f"Wrote {value} to persistent memory at address {address}")
            else:
                print(f"Error: Address {address} out of range for persistent memory.")
        else:
            if 0 <= address < len(self.ram):
                self.ram[address] = value
                print(f"Wrote {value} to RAM at address {address}")
            else:
                print(f"Error: Address {address} out of range for RAM.")

    def read_from_memory(self, address, is_persistent=False):
        """Read a value from memory at a specific address."""
        if is_persistent:
            if 0 <= address < len(self.persistent_memory):
                value = self.persistent_memory[address]
                print(f"Read {value} from persistent memory at address {address}")
                return value
            else:
                print(f"Error: Address {address} out of range for persistent memory.")
                return None
        else:
            if 0 <= address < len(self.ram):
                value = self.ram[address]
                print(f"Read {value} from RAM at address {address}")
                return value
            else:
                print(f"Error: Address {address} out of range for RAM.")
                return None

    def manipulate_memory(self):
        """Fill RAM with random values and copy to persistent memory."""
        self.ram = np.random.randint(0, 100, size=self.ram.shape)
        self.persistent_memory[:len(self.ram)] = self.ram

    def allocate_memory(self, size):
        """Safely allocate memory if sufficient space is available."""
        available_ram = len(self.ram) - sum([end - start + 1 for start, end in self.allocated_blocks])

        if size <= 0:
            print("Skipping allocation: requested size is invalid.")
            return None

        if available_ram >= size:
            try:
                allocated_address = self._allocate_memory(size)
                print(f"Successfully allocated {size} units of memory at address {allocated_address}.")
                return allocated_address
            except MemoryError as e:
                print(f"Memory allocation failed: {e}")
                return None
        else:
            print(f"Not enough available memory for allocation. Requested: {size}, Available: {available_ram}")
            return None

    def _allocate_memory(self, size):
        """Private helper to allocate memory."""
        if not self.allocated_blocks:
            allocated_address = 0
        else:
            allocated_address = self.allocated_blocks[-1][1] + 1
            if allocated_address + size > len(self.ram):
                raise MemoryError("Not enough memory available for allocation.")

        self.allocated_blocks.append((allocated_address, allocated_address + size - 1))
        return allocated_address

    def deallocate_memory(self, start_address):
        """Deallocate a block of memory starting from a given address."""
        for block in self.allocated_blocks:
            if block[0] == start_address:
                self.allocated_blocks.remove(block)
                print(f"Deallocated memory block starting at address {start_address}")
                return
        print(f"Error: No memory block found starting at address {start_address}")

    def clear_ram(self):
        """Clear the RAM (set all values to zero)."""
        self.ram.fill(0)

    def clear_cache(self):
        """Clear the cache (set all values to zero)."""
        self.cache.fill(0)

    def show_memory_status(self):
        """Display current memory usage statistics."""
        print("Memory Status:")
        print(f"RAM: {self.ram}")
        print(f"Persistent Memory: {self.persistent_memory}")
        print(f"Allocated Blocks: {self.allocated_blocks}")


# Define common device class
class Device:
    def __init__(self, device_type, ram_size, persistent_size, cache_size, cores):
        self.device_type = device_type
        self.memory = Memory(ram_size, persistent_size)  # Use Memory class for memory management
        self.cpu = CPU(self.memory, device_type, cores)
        self.power_state = "on"  # Add a power state

    def power_off(self):
        self.power_state = "off"
        print(f"Powering off {self.device_type}")
        self.memory.clear_ram()  # Clear volatile memory
        self.memory.clear_cache()  # Clear CPU cache

    def power_on(self):
        self.power_state = "on"
        print(f"Powering on {self.device_type}")
        self.memory.show_memory_status()

    def validate_power_on(self):
        if self.power_state == "off":
            raise RuntimeError(f"{self.device_type} is powered off and cannot perform this operation.")


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
        super().__init__('Smartwatch', ram_size=1, persistent_size=8, cache_size=1, cores=1)


class IoTDevice(Device):
    def __init__(self):
        super().__init__('IoT Device', ram_size=1, persistent_size=4, cache_size=1, cores=1)


class Desktop(Device):
    def __init__(self):
        super().__init__('Desktop', ram_size=16, persistent_size=512, cache_size=4, cores=8)


def modify_and_load_memory(device1, device2):
    """Simulate modifying memory on one device and loading it onto another."""
    print("Manipulating memory about to be executed...")
    device1.memory.manipulate_memory()  # Manipulate memory of device1

    # Simulate powering off device 1 to show memory persistence
    device1.power_off()  # Power off device1 to simulate saving changes to persistent memory
    device1.power_on()   # Power on device1 to demonstrate memory load

    # Load the modified persistent memory into device 2
    print(f"Device 1 persistent memory after modification: {device1.memory.persistent_memory}")
    device2.memory.persistent_memory = device1.memory.persistent_memory.copy()
    print(f"Device 2 persistent memory after loading: {device2.memory.persistent_memory}")


def power_cycle_simulation(device, num_cycles):
    """Simulate multiple power cycles on a device."""
    for cycle in range(num_cycles):
        print(f"Power Cycle {cycle + 1}")
        device.memory.manipulate_memory()  # Manipulate memory during power cycle
        device.power_off()
        device.power_on()
        device.memory.show_memory_status()  # Visualize memory after power cycle


# Example of using load_memory_file in your context
def example_load_memory_file(device, file_path):
    """Example function for loading memory from a file."""
    loaded_data = device.memory.load_memory_file(file_path)
    if loaded_data is not None:
        print(f"Loaded data: {loaded_data}")
        # You can also set this data to RAM or persistent memory if needed


