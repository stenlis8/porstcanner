#!/usr/bin/env python3

import socket
import argparse
from datetime import datetime
import sys

def scan_port(ip, port, output_file=None):
    """Attempts to connect to a specified port on the given IP address."""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Set timeout for socket connection
        result = sock.connect_ex((ip, port))
        if result == 0:
            result_msg = f"Port {port}: OPEN"
            print(result_msg)
            if output_file:
                with open(output_file, "a") as file:
                    file.write(result_msg + "\n")
        sock.close()
    except Exception as e:
        print(f"Error scanning port {port}: {e}")

def fast_scan(ip, output_file):
    """Scans the most common ports."""
    common_ports = [20, 21, 22, 23, 25, 53, 80, 110, 135, 139, 143, 443, 445, 993, 995, 3306, 3389, 8080]
    print("Performing fast scan on common ports...")
    for port in common_ports:
        scan_port(ip, port, output_file)

def full_scan(ip, output_file):
    """Scans all ports from 1 to 65535."""
    print("Performing full scan on all ports...")
    for port in range(1, 65536):
        scan_port(ip, port, output_file)

def range_scan(ip, start_port, end_port, output_file):
    """Scans ports in the specified range."""
    print(f"Scanning ports {start_port} to {end_port}...")
    for port in range(start_port, end_port + 1):
        scan_port(ip, port, output_file)

def main():
    parser = argparse.ArgumentParser(description="Python port scanner with different scan modes.")
    parser.add_argument("ip", help="The IP address to scan.")
    parser.add_argument("-m", "--mode", choices=["fast", "full", "range"], required=True, help="Scan mode: fast, full, or range.")
    parser.add_argument("-sp", "--start-port", type=int, help="Start port for range mode.")
    parser.add_argument("-ep", "--end-port", type=int, help="End port for range mode.")
    parser.add_argument("-o", "--output", help="Output file to save scan results.")
    args = parser.parse_args()

    # Show help message if no arguments are provided
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)

    ip = args.ip
    mode = args.mode
    output_file = args.output

    # Print starting message
    start_msg = f"Starting scan on {ip} at {datetime.now()}"
    print(start_msg)
    if output_file:
        with open(output_file, "a") as file:
            file.write(start_msg + "\n")

    if mode == "fast":
        fast_scan(ip, output_file)
    elif mode == "full":
        full_scan(ip, output_file)
    elif mode == "range":
        if args.start_port is None or args.end_port is None:
            print("Please provide both start and end ports for range mode.")
            sys.exit(1)
        range_scan(ip, args.start_port, args.end_port, output_file)

    # Print finishing message
    end_msg = f"Scan completed at {datetime.now()}"
    print(end_msg)
    if output_file:
        with open(output_file, "a") as file:
            file.write(end_msg + "\n")

if __name__ == "__main__":
    main()
