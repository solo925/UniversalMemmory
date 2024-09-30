import os
import numpy as np

class PersistenceManager:
    def __init__(self, filepath):
        self.filepath = filepath

    def save_to_disk(self, data):
        np.save(self.filepath, data)
        print(f"Persistent memory saved to {self.filepath}.")

    def load_from_disk(self):
        try:
            data = np.load(self.filepath)
            print(f"Persistent memory loaded from {self.filepath}.")
            return data
        except FileNotFoundError:
            print(f"No persistent memory file found for {self.filepath}. Initializing new persistent memory.")
            return np.zeros(10, dtype='float64')  # Default size for simplicity
