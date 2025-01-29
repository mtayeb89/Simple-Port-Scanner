# Simple Port Scanner

A lightweight, multi-threaded port scanner written in Python for educational purposes and network diagnostics.

## Description

This port scanner is designed to help users understand network security basics by checking for open ports on a specified host. It uses multi-threading for faster scanning and provides basic service identification.

## Features

- Multi-threaded scanning for improved performance
- Service name identification for open ports
- Progress tracking and timing information
- Support for both IP addresses and hostnames
- Simple Arabic command-line interface

## Requirements

- Python 3.x
- No additional packages required (uses only standard library)

## Installation

1. Clone or download the `port_scanner.py` file
2. Ensure you have Python 3.x installed
3. No additional installation steps required

## Usage

1. Run the script:
```bash
python port_scanner.py
```

2. When prompted, enter:
   - Target IP address or hostname (e.g., "localhost" or "127.0.0.1")
   - Starting port number (e.g., 1)
   - Ending port number (e.g., 1000)

Example input:
```
Enter IP address or hostname to scan: localhost
Enter starting port (e.g., 1): 1
Enter ending port (e.g., 100): 100
```

## Output Example

```
--------------------------------------------------
Scanning host: localhost (127.0.0.1)
Start time: 2025-01-29 12:00:00
--------------------------------------------------
[+] Port 80 is open - Service: http
[+] Port 443 is open - Service: https
--------------------------------------------------
Scan completed in 2.34 seconds
Found 2 open ports
--------------------------------------------------
```

## Safety and Legal Considerations

1. Only use this scanner on your own systems or systems you have permission to scan
2. Port scanning without authorization may be illegal in some contexts
3. This tool is for educational purposes and basic network diagnostics only

## Common Port Numbers

Here are some common ports you might want to check:
- 80: HTTP (Web)
- 443: HTTPS (Secure Web)
- 21: FTP
- 22: SSH
- 25: SMTP (Email)
- 3306: MySQL
- 5432: PostgreSQL

## Troubleshooting

1. If you get "Permission denied":
   - Try running with administrator/root privileges
   - Check your firewall settings

2. If the scan is too slow:
   - Reduce the port range
   - Check your network connection

## Contributing

This is a basic implementation for educational purposes. Feel free to modify and improve the code for your needs.

## Disclaimer

This tool is provided for educational purposes only. Users are responsible for ensuring they comply with all applicable laws and regulations when using this scanner.
