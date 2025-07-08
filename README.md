# 📶 Wi-Fi Network Scanner

## 📌 Problem Statement
Users often need to view nearby Wi-Fi networks and assess their signal strength to choose the most reliable connection. However, operating systems don't always give detailed or customizable output.

## 🎯 Objective
To create a Python-based scanner that lists all nearby Wi-Fi networks with:
- Signal strength (RSSI or percentage)
- SSID (network name)
- Security protocol (if available)
- Channel or frequency

---

##  🧠 Features
- Scans nearby Wi-Fi networks.
- Displays SSID, signal strength, and security type.
- Cross-platform support (Windows and Linux).
- Simple command-line interface.
  
## 🧰 Requirements

- Python 3.x
- Platform-specific libraries:
  - `pywifi` (cross-platform, preferred for Windows/Linux)
  - `subprocess` or `os` for direct command-line interaction

## 📂 Project Structure
```
wifi-network-scanner/
├── wifi_scanner.py # Command-line Wi-Fi scanner script
├── wifi_scanner_gui.py # GUI-based scanner using Tkinter
├── README.md               # Documentation file
```

## ⚙️ How It Works
Depending on the platform, the script uses either:
- The ```pywifi``` library to access wireless interfaces and scan for available networks.
- The ```subprocess``` module to run system commands (like ```netsh wlan show networks``` on Windows or ```iwlist``` on Linux).

### Install dependencies:
```
pip install pywifi
```

## 🚀 How to Run
1. Clone or download the repo
```
git clone https://github.com/ShekharSatpute18102004/Wi-Fi-Network-Scanner-.git
cd wifi-network-scanner
```
2. Run the script
```
python wifi_scanner.py
```
⚠️ Note: May require admin/sudo permissions on some systems.

### 📸 Screenshots
<img width="372" alt="output 1" src="https://github.com/user-attachments/assets/e92260df-b5a1-4b8e-8ad2-b700701f1b3e" />

### 🔐 Permissions
- On Windows, no admin is needed for most cases.
- On Linux, you might need to run with sudo for access to wireless interfaces:
```
sudo python3 wifi_scanner.py
```
### 📄 License
MIT License – Free to use and modify.
