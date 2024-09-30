import numpy as np
import matplotlib.pyplot as plt

def visualize_memory(device):
    # Get persistent memory and RAM
    persistent_memory = device.memory.persistent_memory
    ram = device.memory.ram
    
    # Ensure persistent_memory and ram are numpy arrays for easier handling
    persistent_memory = np.array(persistent_memory)
    ram = np.array(ram)
    
    # Resample/reshape RAM to match the length of persistent memory
    if len(ram) < len(persistent_memory):
        # Repeat the elements of ram to match persistent_memory length
        factor = len(persistent_memory) // len(ram)
        ram_resampled = np.repeat(ram, factor)
        
        # Append any remaining part to make lengths match
        extra = len(persistent_memory) % len(ram)
        if extra:
            ram_resampled = np.append(ram_resampled, ram[:extra])
    
    elif len(ram) > len(persistent_memory):
        # If RAM is longer, trim it to match persistent_memory
        ram_resampled = ram[:len(persistent_memory)]
    
    else:
        # If RAM and persistent memory are already of equal length
        ram_resampled = ram
    
    # Plot the memory visualization
    plt.bar(range(len(persistent_memory)), persistent_memory, bottom=ram_resampled, label='Persistent Memory')
    plt.xlabel('Memory Slot')
    plt.ylabel('Memory Usage')
    plt.legend()
    plt.show()


def visualize_cpu(device):
    plt.bar(range(device.cpu.cores), [1] * device.cpu.cores, label='CPU Cores')
    plt.title(f"{device.device_type} CPU Core Usage")
    plt.legend()
    plt.show()
