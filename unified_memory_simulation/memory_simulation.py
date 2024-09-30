import numpy as np

class UnifiedMemory:
    def __init__(self, ram_size, persistent_size, cache_size):
        # Volatile RAM
        self.ram = np.zeros(ram_size, dtype='float64')
        # Non-volatile memory (persistent across cycles)
        self.persistent_memory = np.zeros(persistent_size, dtype='float64')
        # Cache (fast memory used by CPU)
        self.cache = np.zeros(cache_size, dtype='float64')
        # Simulate a page table for memory addresses
        self.page_table = {}  # Map from virtual to physical memory

    def read_from_memory(self, address, is_persistent=False):
        if address in self.page_table:
            physical_address = self.page_table[address]
        else:
            physical_address = address
        
        if is_persistent:
            return self.persistent_memory[physical_address]
        else:
            return self.ram[physical_address]

    def write_to_memory(self, address, value, is_persistent=False):
        if address not in self.page_table:
            self.page_table[address] = address
        
        physical_address = self.page_table[address]
        
        if is_persistent:
            self.persistent_memory[physical_address] = value
        else:
            self.ram[physical_address] = value

    def handle_cache(self, address):
        # If the address is frequently accessed, move it to cache
        if address not in self.cache:
            self.cache[address] = self.ram[address]
        print(f"Memory at {address} cached.")

    def clear_ram(self):
        self.ram.fill(0)

    def clear_cache(self):
        self.cache.fill(0)
        
    
    def show_memory_status(self):
        """Display the current status of RAM, persistent memory, and cache."""
        print("=== Memory Status ===")
        print(f"RAM: {self.ram}")
        print(f"Persistent Memory: {self.persistent_memory}")
        print(f"Cache: {self.cache}")
