class NetworkSimulation:
    def __init__(self, devices):
        self.devices = devices

    def simulate_network_interaction(self):
        print("Simulating network interaction between devices...")
        for device in self.devices:
            device.cpu.execute_write(0, 100.0, is_persistent=True)
            for other_device in self.devices:
                if other_device != device:
                    other_device.cpu.execute_read(0, is_persistent=True)

