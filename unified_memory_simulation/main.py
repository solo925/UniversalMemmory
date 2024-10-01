from device_simulation import Device, Laptop, Phone, Server, Smartwatch, IoTDevice, Desktop, modify_and_load_memory, power_cycle_simulation, Memory
from power_management import PowerCycle
from persistence import PersistenceManager
from network_simulation import NetworkSimulation
from cloud_simulation import CloudSimulation
from app_simulation import Application
from visualization import visualize_memory, visualize_cpu
import tkinter as tk
from tkinter import messagebox
from Tkinter_interface.memory_gui import MemoryGUI

def main():
    # Initialize devices
    laptop = Laptop()
    phone = Phone()
    server = Server()
    smartwatch = Smartwatch()
    iot_device = IoTDevice()
    desktop = Desktop()

    devices = [laptop, phone, server, smartwatch, iot_device, desktop]

    # Persistence managers for each device
    persistence_managers = {device.device_type: PersistenceManager(f'{device.device_type}_persistent.npy') for device in devices}

    # Simulate power cycles and memory management for each device
    for device in devices:
        power_cycle = PowerCycle(device, persistence_managers[device.device_type])
        power_cycle.simulate_power_off_on()

        # Allocate a memory block as part of power cycle simulation
        allocated_address = device.memory.allocate_memory(4)

        if allocated_address is not None:
            device.memory.write_to_memory(allocated_address, 50)
            device.memory.show_memory_status()

            # Deallocate memory block after use
            device.memory.deallocate_memory(allocated_address)
            device.memory.show_memory_status()

    # Simulate network interaction
    network = NetworkSimulation(devices)
    network.simulate_network_interaction()

    # Simulate cloud interaction
    cloud = CloudSimulation()
    for device in devices:
        cloud.sync_with_cloud(device)

    # Run a multi-threaded application on the desktop
    desktop_app = Application(desktop.cpu)
    desktop_app.run_multithreaded()

    # Run the power cycle simulation for the laptop
    num_cycles = 5
    power_cycle_simulation(laptop, num_cycles)

    # Demonstrate memory modification across devices
    modify_and_load_memory(laptop, desktop)

    # Visualize memory and CPU usage
    visualize_memory(desktop)
    visualize_cpu(desktop)

if __name__ == "__main__":
    # uncomment foer the gui
    
    # device = Device('Sample Device', ram_size=8, persistent_size=256, cache_size=2, cores=4)  # This is fine for GUI testing
    # root = tk.Tk()
    # gui = MemoryGUI(root, device)
    # root.mainloop()
    main()  # Running the main simulation
