# python-port-scanner

A simple script that scans the specified ports from the database and then reports which ports are open or closed, along with the scan time.

## Features
* **Port Scanning:** Checks the status of predefined ports (e.g., 21, 22, 80, 443) using TCP sockets.
* **Performance Tracking:** Measures and reports the total execution time in seconds.
**Result Saving:** Saves the scan results to a `scan_results.txt` file.

## How to Run
1. Make sure you have Python 3 installed.
2. Clone or download this repository.
3. Run the script using the terminal:
   ```bash
   python port_scanner.py
   ```
## Changelog

### v1.1
- Added saving scan results to `scan_results.txt`
- Results are now stored while scanning
- Improved socket handling using `with`
- Removed the need to manually close sockets

### v1.0
- Added TCP port scanning
- Added connection timeout
- Added open port counter
- Added scan duration measurement
   
## Disclaimer

This tool is intended for educational purposes and for use on systems you own or have explicit permission to test.

Do not use this tool to scan systems or networks without authorization. The author is not responsible for any misuse of this software.
