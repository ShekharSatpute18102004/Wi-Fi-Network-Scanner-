# run python wifi_scanner_gui.py to start the GUI application
import subprocess
import re
import platform
from datetime import datetime

def scan_wifi_linux():
    try:
        # Try 'nmcli' (modern Linux)
        result = subprocess.run(
            ['nmcli', '-t', '-f', 'SSID,SIGNAL,SECURITY', 'device', 'wifi', 'list'],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            networks = []
            for line in result.stdout.split('\n'):
                if line.strip():
                    parts = line.split(':')
                    if len(parts) >= 3:
                        ssid, signal, security = parts[0], parts[1], parts[2]
                        networks.append({
                            'SSID': ssid,
                            'Signal': f"{signal}%",
                            'Security': security if security else 'Open'
                        })
            return networks

        # Fallback to 'iwlist' (older Linux)
        result = subprocess.run(['iwlist', 'scan'], capture_output=True, text=True)
        if result.returncode == 0:
            networks = []
            cells = re.split(r'Cell \d+ - ', result.stdout)[1:]
            for cell in cells:
                ssid_match = re.search(r'ESSID:"(.*?)"', cell)
                signal_match = re.search(r'Signal level=(-\d+) dBm', cell)
                security_match = re.search(r'IE:.*WPA2|WPA|WEP', cell)
                
                if ssid_match and signal_match:
                    security = 'WPA2' if security_match else 'Open'
                    networks.append({
                        'SSID': ssid_match.group(1),
                        'Signal': f"{signal_match.group(1)} dBm",
                        'Security': security
                    })
            return networks

    except Exception as e:
        print(f"Linux scan failed: {e}")
    return []


def scan_wifi_windows():
    try:
        # Get basic network list (for SSID and security)
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'networks'],
            capture_output=True, text=True
        )
        networks = {}
        current_ssid = None
        for line in result.stdout.split('\n'):
            line = line.strip()
            if 'SSID' in line and 'BSSID' not in line:
                current_ssid = line.split(':')[1].strip()
                networks[current_ssid] = {'Security': 'Unknown'}
            elif 'Authentication' in line and current_ssid:
                security = line.split(':')[1].strip()
                networks[current_ssid]['Security'] = security

        # Get signal strength (requires Bssid mode)
        result = subprocess.run(
            ['netsh', 'wlan', 'show', 'networks', 'mode=Bssid'],
            capture_output=True, text=True
        )
        current_ssid = None
        for line in result.stdout.split('\n'):
            line = line.strip()
            if 'SSID' in line and 'BSSID' not in line:
                current_ssid = line.split(':')[1].strip()
            elif 'Signal' in line and current_ssid in networks:
                signal = line.split(':')[1].strip().replace('%', '')
                networks[current_ssid]['Signal'] = f"{signal}%"

        # Convert to list
        return [
            {'SSID': ssid, 'Signal': data['Signal'], 'Security': data['Security']}
            for ssid, data in networks.items()
            if 'Signal' in data
        ]

    except Exception as e:
        print(f"Windows scan failed: {e}")
    return []


def scan_wifi():
    system = platform.system()
    print(f"Scanning Wi-Fi networks on {system}...")
    if system == 'Linux':
        return scan_wifi_linux()
    elif system == 'Windows':
        return scan_wifi_windows()
    else:
        print("Unsupported OS.")
        return []


def display_networks(networks):
    if not networks:
        print("No networks found or an error occurred.")
        return
    print("\nAvailable Wi-Fi Networks:")
    print("-" * 50)
    print(f"{'SSID':<20} | {'Signal Strength':<15} | {'Security':<10}")
    print("-" * 50)
    for network in networks:
        print(f"{network['SSID']:<20} | {network['Signal']:<15} | {network['Security']:<10}")

if __name__ == '__main__':
    networks = scan_wifi()
    display_networks(networks)
