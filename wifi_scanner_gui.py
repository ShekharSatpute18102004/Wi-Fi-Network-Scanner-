# run python wifi_scanner_gui.py to start the GUI application
import tkinter as tk
from tkinter import ttk
from wifi_scanner import scan_wifi

class WiFiScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Wi-Fi Network Scanner")
        self.root.geometry("500x400")

        self.label = ttk.Label(root, text="Available Wi-Fi Networks:")
        self.label.pack(pady=10)

        self.tree = ttk.Treeview(root, columns=('SSID', 'Signal', 'Security'), show='headings')
        self.tree.heading('SSID', text='SSID')
        self.tree.heading('Signal', text='Signal Strength')
        self.tree.heading('Security', text='Security')
        self.tree.pack(fill=tk.BOTH, expand=True)

        self.scan_button = ttk.Button(root, text="Scan Networks", command=self.scan_networks)
        self.scan_button.pack(pady=10)

    def scan_networks(self):
        for item in self.tree.get_children():
            self.tree.delete(item)
        networks = scan_wifi()
        for network in networks:
            self.tree.insert('', tk.END, values=(network['SSID'], network['Signal'], network['Security']))

if __name__ == '__main__':
    root = tk.Tk()
    app = WiFiScannerApp(root)
    root.mainloop()
