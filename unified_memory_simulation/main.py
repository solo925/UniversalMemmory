from memory_simulation.py import UnifiedMemory
from cpu_simulation import CPU
from persistence import PersistenceManager
from app_simulation import Application

def main():
    # Initialize the memory system (e.g., 10 units of RAM and 10 units of persistent memory)
    ram_size = 10
    persistent_size = 10
    memory = UnifiedMemory(ram_size, persistent_size)

    # Initialize the CPU
    cpu = CPU(memory)

    # Persistence Management (simulating power cycle)
    persistence_manager = PersistenceManager("persistent_memory.npy")

    # Load persistent memory if available
    loaded_persistent_memory = persistence_manager.load_from_disk()
    if loaded_persistent_memory is not None:
        memory.persistent_memory = loaded_persistent_memory

    # Run the application simulation
    app = Application(cpu)
    app.run_simulation()

    # Save persistent memory before shutdown
    persistence_manager.save_to_disk(memory.persistent_memory)

if __name__ == "__main__":
    main()
