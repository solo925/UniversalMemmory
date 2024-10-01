import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from visualization import visualize_memory, visualize_cpu

class MemoryGUI:
    def __init__(self, root, device):
        self.root = root
        self.device = device
        self.root.title("Unified Memory Simulation")

        # Dropdown for device selection
        self.device_label = tk.Label(root, text="Select Device:")
        self.device_label.pack(pady=5)
        
        self.device_var = tk.StringVar()
        self.device_dropdown = ttk.Combobox(root, textvariable=self.device_var, state="readonly")
        self.device_dropdown['values'] = ["Laptop", "Phone", "Server", "Smartwatch", "IoT Device", "Desktop"]
        self.device_dropdown.current(0)
        self.device_dropdown.pack(pady=5)
        self.device_dropdown.bind("<<ComboboxSelected>>", self.update_device)

        # Memory Status Button
        self.memory_button = tk.Button(root, text="Show Memory Status", command=self.show_memory_status)
        self.memory_button.pack(pady=10)

        # CPU Status Button
        self.cpu_button = tk.Button(root, text="Show CPU Status", command=self.show_cpu_status)
        self.cpu_button.pack(pady=10)

        # Allocate Memory
        self.alloc_label = tk.Label(root, text="Allocate Memory (units):")
        self.alloc_label.pack(pady=5)
        self.alloc_entry = tk.Entry(root)
        self.alloc_entry.pack(pady=5)

        self.alloc_button = tk.Button(root, text="Allocate Memory", command=self.allocate_memory)
        self.alloc_button.pack(pady=10)

        # Deallocate Memory
        self.dealloc_label = tk.Label(root, text="Deallocate Memory (start address):")
        self.dealloc_label.pack(pady=5)
        self.dealloc_entry = tk.Entry(root)
        self.dealloc_entry.pack(pady=5)

        self.dealloc_button = tk.Button(root, text="Deallocate Memory", command=self.deallocate_memory)
        self.dealloc_button.pack(pady=10)

        # Power Cycle
        self.power_button = tk.Button(root, text="Power Cycle Device", command=self.power_cycle_device)
        self.power_button.pack(pady=10)

        # Load/Save Memory State
        self.save_button = tk.Button(root, text="Save Memory State", command=self.save_memory_state)
        self.save_button.pack(pady=10)
        
        self.load_button = tk.Button(root, text="Load Memory State", command=self.load_memory_state)
        self.load_button.pack(pady=10)

        # Close Button
        self.close_button = tk.Button(root, text="Close", command=root.quit)
        self.close_button.pack(pady=10)

    def update_device(self, event):
        # Logic to update the selected device
        selected_device = self.device_var.get()
        print(f"Selected device: {selected_device}")
        # Update self.device to the selected one in actual implementation
    
    def show_memory_status(self):
        # Call visualization for memory status
        visualize_memory(self.device)

    def show_cpu_status(self):
        # Call visualization for CPU status
        visualize_cpu(self.device)

    def allocate_memory(self):
        size = int(self.alloc_entry.get())
        address = self.device.memory.allocate_memory(size)
        if address is not None:
            messagebox.showinfo("Success", f"Memory allocated at address {address}")
        else:
            messagebox.showerror("Error", "Memory allocation failed")

    def deallocate_memory(self):
        start_address = int(self.dealloc_entry.get())
        self.device.memory.deallocate_memory(start_address)

    def power_cycle_device(self):
        self.device.power_off()
        self.device.power_on()
        messagebox.showinfo("Power Cycle", f"{self.device.device_type} has been power cycled")

    def save_memory_state(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".npy")
        if file_path:
            self.device.memory.save_memory_file(file_path)
            messagebox.showinfo("Saved", "Memory state saved successfully.")

    def load_memory_state(self):
        file_path = filedialog.askopenfilename(filetypes=[("Numpy files", "*.npy")])
        if file_path:
            self.device.memory.load_memory_file(file_path)
            messagebox.showinfo("Loaded", "Memory state loaded successfully.")
