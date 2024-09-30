import time
class PowerCycle:
    def __init__(self, device, persistence_manager):
        self.device = device
        self.persistence_manager = persistence_manager

    def simulate_power_off_on(self, cycles=3):
        for cycle in range(cycles):
            print(f"\n=== Power Cycle {cycle + 1} ===")
            self.device.power_off()
            self.persistence_manager.save_to_disk(self.device.memory.persistent_memory)

            # Simulating delay or downtime
            time.sleep(1)

            # Power on the device
            self.device.memory.persistent_memory = self.persistence_manager.load_from_disk()
            self.device.power_on()
