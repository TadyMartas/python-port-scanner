import socket
import time # Add time module

# Target local host
target = "127.0.0.1"

# Ports for scanníng
ports = [21, 22, 80, 139, 443, 8080]
print(self_reply := f"Scanning target: {target}\n")

# Start the timer before scanning
start_time = time.time()

# Create open ports counter
open_ports_count = 0

for port in ports:
    # Create network socket (IPv4, TCP)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Timeout
    s.settimeout(1)

    # Try making connection to port
    result = s.connect_ex((target, port))

    # Print result based on the outcome
    if result == 0:
        print(f"[+] Port {port} OPEN")
        open_ports_count += 1 # Add up an open port to counter
    else:
        print(f"[-] Port {port} CLOSED")

    s.close()

# Stop the timer after scanning
end_time = time.time()

# Rounds the time to two decimals
duration = round(end_time - start_time, 2)

# Finds total ports in database
total_ports = len(ports)

# After scanning report outcome
if open_ports_count == 0:
    print("\n[!] ALL PORTS ARE CLOSED")
elif open_ports_count == total_ports:
    print("\n[!] ALL PORTS OPEN")
else:
    print("\n[!] SOME PORTS ARE OPEN")

# Prints the scanning time
print(f"[*] Scanning finished in {duration} seconds.")
