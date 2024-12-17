import socket

def scan_port(target, port):
    """Scan a specific port on the target."""
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  # Set a 1-second timeout

        # Try to connect to the target and port
        result = s.connect_ex((target, port))

        # If the result is 0, the port is open
        if result == 0:
            print(f"Port {port} is open!")
        s.close()
    except socket.error as e:
        print(f"Couldn't connect to {target}:{port}, {e}")

def main():
    target = input("Enter the target IP address or hostname: ")
    start_port = int(input("Enter the starting port: "))
    end_port = int(input("Enter the ending port: "))

    print(f"Scanning ports {start_port}-{end_port} on {target}...")

    # Loop through the port range and scan each port
    for port in range(start_port, end_port + 1):
        scan_port(target, port)

if __name__ == "__main__":
    main()
