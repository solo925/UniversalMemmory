from device_simulation import Laptop, Phone, Server, Smartwatch, IoTDevice, Desktop
from power_management import PowerCycle
from persistence import PersistenceManager
from network_simulation import NetworkSimulation
from cloud_simulation import CloudSimulation
from app_simulation import Application
from visualization import visualize_memory, visualize_cpu

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

    # Simulate power cycles
    for device in devices:
        power_cycle = PowerCycle(device, persistence_managers[device.device_type])
        power_cycle.simulate_power_off_on()

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

    # Visualize memory and CPU usage
    visualize_memory(desktop)
    visualize_cpu(desktop)

if __name__ == "__main__":
    main()
