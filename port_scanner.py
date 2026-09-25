import socket
import time

# Target local host
target = "127.0.0.1"

# Ports for scanning
ports = [21, 22, 80, 139, 443, 8080]

# Start the timer before scanning
start_time = time.time()

# Create open ports counter
open_ports_count = 0

# Create scan result file
with open("scan_results.txt", "w") as file:
    for port in ports:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(1)
            result = s.connect_ex((target, port))

        # Print result based on the outcome
        if result == 0:
            print(f"[+] Port {port} OPEN")
            file.write(f"[+] Port {port} OPEN\n")
            open_ports_count += 1
        else:
            print(f"[-] Port {port} CLOSED")
            file.write(f"[-] Port {port} CLOSED\n")

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