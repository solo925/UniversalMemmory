import numpy as np

class CloudSimulation:
    def __init__(self, cloud_storage_size=1024):
        self.cloud_memory = np.zeros(cloud_storage_size, dtype='float64')

    def sync_with_cloud(self, device):
        print(f"Syncing {device.device_type} with cloud storage.")
        self.cloud_memory[:len(device.memory.persistent_memory)] = device.memory.persistent_memory

    def retrieve_from_cloud(self):
        print("Retrieving data from cloud.")
        return self.cloud_memory
